# Robotics Engineering — Stage 05: Optional / As-Needed Mathematics

**Companion to:** *Complete Robotics Engineering Roadmap* and Stages 01–04  
**Stage type:** cross-cutting, pull-based reference — **NOT another chronological stage**  
**When:** short problem-driven study sprints alongside Stages 02–06; typical first triggers months 5–30+  
**Study load:** normally 0 h/week until triggered; then ~2–4 h/week for 2–6 weeks, with an explicit end condition  
**End state:** learn, use and verify only the advanced mathematics required by an actual robot, model, logged failure or selected research project.

> **Scope and safety:** This document provides mathematics for civilian/industrial robotics and non-weaponized field systems. The field/defense-adjacent branch remains limited to logistics, inspection, remote sensing, search-and-rescue support and survey/hazard mapping; it excludes weapon integration, target selection and autonomous engagement. Mathematical performance is not evidence of a safe, certified or authorized machine.

## 0. How Stage 05 fits the seven-lane learning graph

```text
Stage 01  Core math + P01–P03 ──────────────────────────────────┐
Stage 02  Circuits / MCU / PID + P04–P05 ───────────────────────┤
Stage 03  ROS 2 / tf2 / simulation + P06–P07 ───────────────────┤
Stage 04  Estimation / perception / one planner + P08–P11 ─────┼──> Stage 06
                                                               │
Stage 05  Optional math: pull ONLY after a documented trigger ─┘
                                                               │
Stage 07  Documentation / tests / review / safety ─────────────┘  [runs always]
```

**Critical correction:** Stage 05 has **no mandatory months 23–26 or dedicated four-month prerequisite**. It is a side branch. Do not delay P05, P07, P08, P09, P11 or the selected P12/P13 capstone to finish this document. Most of the material may legitimately remain **E — Exposure**, even at month 36.

| Label | Meaning in this file | Acceptable evidence |
|---|---|---|
| **E — Exposure** | Reproduce/explain a small example | Annotated notebook + one passing check |
| **W — Working competence** | Implement and debug on bounded data | Baseline comparison, failure case, unit tests |
| **P — Focused proficiency** | Design/evaluate one advanced method in a bounded project | Hold-out tests, sensitivity, external critique; no blanket field proficiency |

## 1. The strict no-front-loading decision rule

- [ ] State the *specific* measured failure, missing capability or research question.
- [ ] Name the blocked gate: P05, P07, P08, P09/P10, P11, P12 or P13.
- [ ] Save baseline code, inputs, version numbers, seeds, units, frames and observed results.
- [ ] Write what must improve and by how much; choose the acceptance metric **before** trying the advanced method.
- [ ] Check whether an incorrect unit, sign, frame, calibration, timestamp, sensor model, wiring or baseline tuning explains the problem first.
- [ ] Try the simplest justified fix using core mathematics and a maintained library.
- [ ] Select **one** module below, identify its minimum subsection and time-box the study.
- [ ] Repeat the *same* test with the new approach; report benefit, computation/memory cost and failure cases.
- [ ] Have a second person check the relevant derivation/assumptions if the result affects actuation or an important project decision.
- [ ] Stop the detour if there is no demonstrated gain; return to the primary project.

```text
Failure / requirement
    ↓
Units, frames, time and basic model checked?
    ├── No → Repair core path; Stage 05 is NOT the fix.
    └── Yes → Can a simple baseline or verified library solve it?
               ├── Yes → Use baseline; continue main gate.
               └── No  → Pull smallest math module → measure change
                         ├── Improves metric → retain with tests
                         └── No improvement → revert and document
```

## 2. Prerequisite core mathematics — repair these before advanced topics

| Core item | Already belongs to | Quick diagnostic |
|---|---|---|
| SI units, vectors, derivatives, simple integration | Stage 01 | Derive torque and motor speed; dimension-check outputs |
| Matrices, rotation, homogeneous transforms, FK/IK/Jacobian | Stage 01 | Compose/invert transforms; verify arm FK numerically |
| First/second-order ODE, sample period, PID/anti-windup | Stage 02 | Reproduce bounded axis response including saturation |
| `tf2`, quaternions as *representations*, time and transform direction | Stage 03 | Audit frames and time on a simulated robot |
| Probability, covariance, least squares, basic KF/EKF intuition | Stage 04 | Explain uncertainty and compare fusion vs dead reckoning |
| Graph search and bounds for the chosen planner | Stage 04 | Explain blocked route/failed grasp and recovery |

**If a core diagnostic fails:** repair the corresponding earlier stage, not a more advanced substitute. In particular, using `tf2` does **not** require full Lie-algebra derivations.

## 3. Module selector — return triggers, effort and realistic depth

| Module | Start only when… | Earliest useful window | Focused sprint | Target |
|---|---|---:|---:|---|
| M01 Eigenvalues, Laplace, Bode | An unexplained oscillation, resonance or stability/timing issue remains after basic PID checks | Month 5+ | 10–20 h | E→W |
| M02 Pseudoinverse, SVD, conditioning | IK/calibration is redundant, singular or numerically unstable | Month 9+ | 10–18 h | E→W |
| M03 `SO(3)`/`SE(3)`, Lie `exp/log` | Writing custom 3D estimation, pose optimization or advanced arm kinematics | Month 16+ | 15–30 h | E; W if needed |
| M04 State space, controllability, observability, LQR | Required state is unmeasurable or PID cannot meet a stated bounded target | Month 16+ | 15–25 h | E→W |
| M05 Stochastic processes, particles, factor graphs | A real estimation problem exceeds the validated basic filter | Month 19+ | 15–30 h | E→W |
| M06 Nonlinear optimization / SLAM internals | Writing/changing a solver or research method, not merely integrating a package | Month 22+ | 20–40 h | E; W if thesis needs it |
| M07 MPC, robust/adaptive, impedance/admittance | The chosen safe capstone has proven constraints/contact/dynamics unmet by simpler control | Month 26+ | 20–40 h | E→W in one case |
| M08 Coupled rigid-body dynamics | Simplified mechanical model fails for the selected mechanism or speed | Month 17+ | 12–25 h | E→W |

**Sprint budget is study/build time, not promised mastery.** Only one math detour should be active during a core/capstone gate. The windows are *earliest sensible triggers*, not start dates.

---

## 4. M01 — Eigenanalysis, Laplace transforms and frequency-domain control

**Question this module answers:** why does the measured/simulated axis ring, oscillate, drift or lose stability when sample time, inertia, friction or gain changes?

### Low-level learning checklist

- [ ] Review complex numbers, roots of a quadratic and the sign of real parts.
- [ ] Linearize a small model about one operating point; state its validity envelope.
- [ ] Form a 2-state system matrix; calculate characteristic polynomial and eigenvalues.
- [ ] Relate poles to growth/decay, oscillation frequency and damping in *this* model.
- [ ] Identify zero/pole/gain of simple first- and second-order transfer functions.
- [ ] Use Laplace transforms for a step input and compare with time-domain ODE integration.
- [ ] Read magnitude and phase plots; distinguish frequency units Hz vs rad/s.
- [ ] Recognize resonance, roll-off, sensor noise amplification and delay effects.
- [ ] Explain why an ideal derivative can amplify noisy measurements.
- [ ] Vary sample period and include actuator saturation; do not assume a continuous model validates a digital controller.
- [ ] Check gain/phase-margin *concepts* against a trustworthy computed plot.
- [ ] Write limitations: friction, backlash, unmodeled modes, thermal behavior and sampling.

**Micro-project M01:** reproduce P05 baseline; perturb load, sample interval and gain; identify a failure and compare time and frequency evidence. **Pass:** plots with units, model equations and a practical change supported by the same benchmark. **Stop here** unless the chosen capstone needs synthesis beyond PID.

## 5. M02 — Pseudoinverse, SVD and numerical conditioning

**Question:** why does an arm or calibration solver produce huge joint changes, unstable answers or inconsistent output near a singular configuration?

### Low-level learning checklist

- [ ] Differentiate a planar FK map and compute its Jacobian.
- [ ] Define rank, null space and under/over-determined systems on small matrices.
- [ ] Explain what a least-squares solution minimizes.
- [ ] Compare inverse, pseudoinverse and damped least-squares updates.
- [ ] Implement `numpy.linalg.svd` and inspect singular values.
- [ ] Plot condition number or smallest singular value along a path.
- [ ] Show where joint velocity becomes unbounded in an undamped scheme.
- [ ] Add joint limits and a numerical termination condition.
- [ ] Check finite-difference Jacobian against the derived Jacobian.
- [ ] Compare runtime, accuracy, smoothness and sensitivity across solvers.

**Micro-project M02:** move P03 arm toward stretched configuration and compare analytic IK, pseudoinverse and damped least squares. **Pass:** a reproduced singularity plus a bounded regularized result; do not claim one method solves all geometry.

## 6. M03 — Lie groups, `SO(3)`, `SE(3)` and pose perturbations

**Question:** are custom 3D pose updates, interpolation or estimation residuals wrong because rotations and translations are treated as ordinary unconstrained vectors?

### Low-level learning checklist

- [ ] Reconfirm frame labels, active/passive rotations and left/right multiplication.
- [ ] Check rotation orthonormality, determinant and rigid-transform inverse.
- [ ] Implement skew-symmetric `hat` and inverse `vee` mappings for 3-vectors.
- [ ] Explain `SO(3)` and `SE(3)` as constrained rotation/pose sets at a conceptual level.
- [ ] Compare axis-angle, quaternion and matrix representations and normalization.
- [ ] Compute matrix exponential/log on simple rotations with a verified library.
- [ ] Identify small-angle approximation error with a numerical experiment.
- [ ] Explain left vs right perturbation for **your chosen** frame convention.
- [ ] Compose pose uncertainty only under stated approximations.
- [ ] Test inverse/round-trip and perturbation direction on random valid poses.
- [ ] Keep this math in a small library rather than modifying unrelated ROS transforms.

**Micro-project M03:** replicate a pose-update example from a trusted source and catch one intentionally injected frame/sign bug. **Pass:** round-trip checks and diagram. **Not necessary** merely to operate `tf2` or a supported SLAM/MoveIt/Nav2 package.

## 7. M04 — State-space control, observability, controllability and LQR

**Question:** can a chosen actuator/robot state be estimated and controlled with available sensors and inputs, and when does an alternative controller help?

### Low-level learning checklist

- [ ] Define state, input, measurement, disturbance and sample time.
- [ ] Write `x_dot = A x + B u` or a justified sampled equivalent.
- [ ] Explain why two physically different states can produce the same measurement.
- [ ] Build a small observability matrix and inspect its rank.
- [ ] Build a small controllability matrix and inspect its rank.
- [ ] Check units/scales before choosing state penalties.
- [ ] Simulate state feedback with actuator limits.
- [ ] Introduce LQR cost at a conceptual level; label any tuning assumptions.
- [ ] Compare against well-tuned PID under identical disturbances.
- [ ] Test saturation, stale sensing and missing state estimates.
- [ ] Never substitute a research controller for independent stop/energy isolation.

**Micro-project M04:** compare PID vs state feedback on a simulated safe axis. **Pass:** predeclared metric, comparable inputs and explicit reason why the added complexity is or is not warranted.

## 8. M05 — Stochastic processes, particle filters and factor graphs

**Question:** does a localization/fusion failure reflect multimodal uncertainty, correlated noise or changing biases that the Stage 04 baseline cannot represent?

### Low-level learning checklist

- [ ] Recheck mean/variance/covariance and which frame a covariance belongs to.
- [ ] Distinguish random measurement noise, systematic bias and drift.
- [ ] Generate and plot noise with a documented seed and distribution.
- [ ] Examine temporally correlated errors and why independent-noise assumptions can fail.
- [ ] Compare KF/EKF estimates to known simulated ground truth.
- [ ] Understand particle state, weighting, normalization, resampling and degeneracy.
- [ ] Use a toy 1D/2D example with ambiguous measurements.
- [ ] Understand factors as constraints between variables and their measurement residuals.
- [ ] Identify data-association and loop-closure errors conceptually.
- [ ] Test outliers, lost measurements and deliberate sensor-bias changes.
- [ ] Report accuracy, consistency, compute/memory cost and recovery failures.

**Micro-project M05:** reproduce a scenario with two plausible locations in simulation; compare a unimodal baseline and a small particle-filter demo. **Pass:** show when the added method genuinely helps, and where it fails.

## 9. M06 — Nonlinear optimization and SLAM internals

**Question:** are you implementing or altering a solver, calibration, bundle adjustment or SLAM method rather than simply using a supported robotics package?

### Low-level learning checklist

- [ ] Translate an engineering measurement into a residual with units.
- [ ] Write a least-squares cost; distinguish squared error from a robust loss.
- [ ] Inspect gradient/Jacobian shapes and finite-difference derivatives.
- [ ] Understand initialization, local minima and poorly conditioned estimates.
- [ ] Compare gradient-based and Gauss–Newton/LM ideas on a toy problem.
- [ ] Explain factor/pose graph nodes and constraint edges.
- [ ] Recognize gauge freedom and the role of anchored reference frames.
- [ ] Identify loop-closure false positives in a replayable dataset.
- [ ] Record solver iterations, timing, residual distribution and failure modes.
- [ ] Evaluate against a known baseline and held-out scenarios.

**Micro-project M06:** optimize a small simulated pose graph with a bad outlier and compare error with/without robust treatment. **Pass:** transparent benchmark and reproducibility, not a claim of a production SLAM stack.

## 10. M07 — MPC, robust/adaptive control and impedance/admittance

**Question:** does the selected bounded capstone have documented hard constraints, uncertainty or benign contact that well-tuned simpler control cannot meet?

### Low-level learning checklist

- [ ] Restate plant model, state/input bounds, objective and prediction horizon.
- [ ] Verify feasibility of the intended task with simple kinematic/actuator limits.
- [ ] Distinguish unconstrained optimization from a constrained trajectory.
- [ ] Implement a *simulated* short-horizon optimal-control toy problem.
- [ ] Explain model mismatch and sensitivity to delay/calibration error.
- [ ] Compare to safe PID/feedforward baseline with matched limits.
- [ ] Understand what impedance vs admittance means for a benign low-energy interaction.
- [ ] Include contact force/velocity limits and failure handling in simulation.
- [ ] Test infeasible optimization, stale sensing and compute-time overrun.
- [ ] Record why this method is needed **in this project**.

**Micro-project M07:** constrained simulated axis/benign pick-and-place; compare tracking, overshoot, input bound violations and compute time. **Pass:** no unsafe physical contact experiment and no safety-certification claim.

## 11. M08 — Advanced rigid-body dynamics and inertia tensors

**Question:** do coupled loads, fast motion, arm configuration or vibration make the Stage 01–02 simplified torque model inadequate?

### Low-level learning checklist

- [ ] Calculate/estimate mass, COM and inertia for an explicit CAD geometry.
- [ ] Define local vs world frame for inertia values.
- [ ] Apply the parallel-axis theorem with correct distance units.
- [ ] Evaluate link position/velocity/acceleration across a benign trajectory.
- [ ] Compare simplified static/one-axis torque with a coupled model.
- [ ] Account for transmission friction, backlash and efficiency as measured/assumed terms.
- [ ] Examine joint peak vs continuous torque and thermal duty-cycle implications.
- [ ] Check model sensitivity to payload location and mass uncertainty.
- [ ] Validate against a second calculation or permissible low-energy measurements.
- [ ] Update a motor-sizing sheet only after explaining the numerical difference.

**Micro-project M08:** redesign a P03 link/payload case, explain why a simplified motor choice changes or remains valid; document uncertainty.

---

## 12. Choose math by specialization, NOT by catalog completion

| Chosen Stage 06 track | Commonly useful modules *if triggered* | Usually safe to leave at E |
|---|---|---|
| Industrial virtual workcell | M02 near IK singularity; M08 if changing payload/inertia; M01 for oscillation | Factor-graph SLAM; research MPC unless proven needed |
| Non-weaponized rugged-field inspection/logistics | M05 for genuinely ambiguous localization; M03 for custom 3D state estimates; M08 for payload/endurance model | Full arm impedance control; custom SLAM solver if existing package suffices |
| IoT/IIoT robot-fleet integration | **Normally none** beyond core math; statistics for fleet health is a separate bounded analytics task | Lie groups, LQR/MPC and full SLAM unless the robot subsystem itself requires them |
| Master’s/PhD research | Relevant module only after thesis hypothesis/advisor/lab context | Everything unrelated to the research question |

**IoT warning:** more advanced control mathematics does not make Internet-based safety control acceptable. Local independent stop/control remains independent of the broker and cloud.

## 13. Review, acceptance and stop conditions

| Checkpoint | Ask the reviewer to challenge | Evidence |
|---|---|---|
| Before sprint | Is core math actually correct? Is advanced math necessary? | Failure report and proposed baseline |
| Mid-sprint | Assumptions, axes/frames, units, derivatives and test fairness | Notebook, unit tests, diagrams |
| End-sprint | Measured improvement vs baseline; numerical failures; generalization | Side-by-side plots, fixed benchmark, issues resolved |
| During P12/P13 | Did math work displace necessary integration/safety/review time? | Updated schedule and capstone acceptance matrix |

### Exit checklist for *one selected module*

- [ ] I can explain the actual trigger in two sentences.
- [ ] I can state all quantities with units and frames where applicable.
- [ ] I have a simple saved baseline and a fair comparison.
- [ ] I can reproduce one deliberately adverse/failure case.
- [ ] I can describe numerical/physical limits and compute cost.
- [ ] A review question was asked and the response/action documented where feasible.
- [ ] The core project is unblocked or I have deliberately reverted the detour.

### If behind schedule

| If you are… | Preserve | Defer |
|---|---|---|
| Behind at month 6 | P05 units, timing, bounded PID, safe fault response | M01 proofs, LQR/MPC |
| Behind at month 12 | P07 transforms, time, model, `ros2_control`, reproduction | M02/M03 unless a real block exists |
| Behind at month 18 | P08 noise, covariance, fusion-vs-baseline | Particles/factor graphs/M03 unless needed |
| Behind at month 22 | One planner, P11 stop/recovery and tests | Full SLAM/optimization, other planner |
| Behind at month 30 | Selected P12 or P13 acceptance and review | Unrelated advanced math, second specialization |

**Never defer:** correct units/frames/time, safe power, independent stop strategy, regression testing, credible fault behavior, relevant approvals and scope boundaries.

## 14. Tools, cost and reference material

**Incremental budget:** **$0 hardware** for the complete Stage 05 simulation/notebook route on an existing suitable computer; optional paid courses/books or lab access only if a real need exists. Extra math is primarily a **time budget**; it must be charged against the current project. No special GPU is required for the small example problems here.

- [ ] NumPy/SciPy/SymPy/Matplotlib (numerical notebooks, linear algebra, ODEs, plots).
- [ ] A versioned benchmark dataset and test harness with fixed random seeds.
- [ ] Known quantities and frames documented in Markdown.
- [ ] A small reproducible repository or `math_extensions/` inside the blocked gate's repo.

**Source-aligned learning references:**

- [Modern Robotics — Lynch & Park](https://modernrobotics.northwestern.edu/) — use relevant transformations/kinematics/dynamics chapters.
- [MIT Underactuated Robotics](https://underactuated.mit.edu/) — advanced control/dynamics only when justified.
- [Feedback Systems — Åström & Murray](https://fbsbook.org/) — frequency-domain and state-space topics.
- [MIT OpenCourseWare](https://ocw.mit.edu/) — targeted calculus/linear algebra/control refreshers.
- [SciPy documentation](https://docs.scipy.org/doc/scipy/) — verified numerical routines.

```text
stage-05-math-sprint/
├── README.md                  # actual trigger, scope and stop condition
├── baseline/                  # frozen previous method
├── notebooks/                 # derivations with units and frames
├── data/README.md             # provenance and synthetic/real labels
├── tests/                     # round trips, finite differences, edge cases
├── results/                   # baseline vs change, timings and failures
├── review/                    # review question, findings and fixes
└── decision.md                # keep advanced method? yes/no and why
```

**North-star result:** “I learned exactly the mathematics that a measured robotics problem needed, proved its effect, and returned to integration.”
