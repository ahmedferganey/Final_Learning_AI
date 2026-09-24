# Robotics Engineering — Stage 07: Ongoing Parallel Habits

**Companion to:** *Complete Robotics Engineering Roadmap* + Stages 01–06  
**When:** **every week from month 1 through month 36+**; begins immediately, never waits for completion of Stages 01–06  
**Time budget:** normally **2–3 of the existing 12–18 focused hours/week**, not 2–3 extra hours; temporarily 4–5 h/week around formal reviews and capstone handoff  
**Primary deliverable:** a coherent, independently reproducible engineering portfolio with honest depth labels, verifiable project gates, review history, safe test boundaries and credible CV evidence  
**No standalone numbered P-gate:** Stage 07 supplies the **evidence and quality system** for P01–P13. It is not a new specialization or another certification.

> **Invariant safety boundary:** safety-critical stop/control functions must never depend on cloud or Internet connectivity, a dashboard, an LLM or an ordinary ROS 2 node. A CI pass, home test suite, simulated workcell, mentor review or environmental experiment is **not** a safety certification, qualified acceptance test or authorization for deployment. Real industrial and controlled defense work requires appropriate qualified specialists, site/program permissions, applicable current standards and legal/security review.
>
> **Unchanged field/defense-adjacent scope:** logistics, inspection, remote sensing, search-and-rescue support, and survey/hazard mapping only; **no weapon integration, target selection or autonomous engagement**. Publish only public/non-controlled material and follow organizational/export/security rules for real work.

---

## 0. What this stage changes about the way you learn

Stages 01–06 are **what you build**. Stage 07 is **how you know you really built it**, can explain its limits, and can safely hand it to another engineer.

```text
                             STAGE 07: ALWAYS PARALLEL

  Stage 01 → Stage 02 → Stage 03 → Stage 04 → Stage 06 → career / further study
      │          │          │          │          │
      ├──────────┴──────────┴──────────┴──────────┤
      │ requirements, notes, drawings, test evidence│
      │ Git / reviews / reproduction / fault reports│
      │ safety / information boundaries / budgets    │
      │ credentials / portfolio / mentorship         │
      └───────────────────────────────────────────────┘
                      ↑
             Stage 05 math on demand
```

### Depth labels — preserve the original meaning

| Label | Observable threshold | What it does **not** mean |
|---|---|---|
| **E — Exposure** | Explain the concept and reproduce a guided example | Independent operation or meaningful failure testing |
| **W — Working competence** | Independently implement and debug one bounded task; supply measurements and tests | Proficiency across the whole domain |
| **P — Focused proficiency** | Design, integrate, fault-test, review, maintain and independently reproduce one bounded system | Professional license, certification, controlled-program access, domain-wide mastery |

**Progress rule:** completing hours, tutorials or certificates does **not** promote E to W or W to P. Promote only after the specific stage gate has accepted evidence.

### Seven recurring workstreams

| ID | Workstream | Minimum rhythm | Main artifact |
|---|---|---|---|
| H1 | Documentation and engineering decisions | Each work session + monthly cleanup | README, calculations, design log, ADRs |
| H2 | Testing, metrics and reproducibility | Every meaningful change; monthly independent run | Verification matrix, CI/local test result, plots |
| H3 | External review and mentorship | Target every ~12 weeks + gate reviews | Review request, feedback and closure log |
| H4 | Safety, standards and information boundaries | Every new hazard/interface; quarterly audit | Hazard log, operating envelope, standards register |
| H5 | Staged cost, time and asset management | Monthly / before purchases | Budget ledger, inventory, forecast |
| H6 | Portfolio, credentials and career evidence | Monthly; quarterly edit | Project case studies, CV evidence, credential plan |
| H7 | Recovery and continuing learning | Weekly adjust; quarterly decision | Blocker log, cut/defer list, updated dates |

---

# H1 — DOCUMENTATION AND ENGINEERING COMMUNICATION

## 1. Source-control discipline and artifact naming

### 1.1 Every project starts with a traceable identity

- [ ] Name the project for the engineering question, not a marketing claim.
- [ ] Assign the original roadmap gate ID exactly: **P01–P13**, and stage number.
- [ ] Record whether the platform is `SIM`, `BENCH` (guarded low-energy), or `SUPERVISED_SITE` (authorized and qualified only).
- [ ] Add goal, operator/user, operating environment and prohibited operations.
- [ ] State numeric quantities with SI units, sign conventions and coordinate frames where applicable.
- [ ] Identify the current baseline version, dependencies and known limitations.
- [ ] Add one reproducible start command or clear installation procedure.
- [ ] Add a maintenance owner (you), review owner (if agreed), and last-reviewed date.
- [ ] Document source and permissions for datasets, CAD models and third-party components.
- [ ] Mark confidential, proprietary, personal or controlled materials as **not for public upload** until authorized.

### 1.2 Git and repository hygiene

- [ ] Use Git for source, configuration and small illustrative evidence; keep giant logs out of ordinary commits.
- [ ] Commit working increments with meaningful messages (e.g., `test(tf): reject frame inversion`).
- [ ] Prefer a short-lived branch for risky changes; review and merge deliberately.
- [ ] Keep generated binaries, credentials, device keys and machine-specific secrets out of Git.
- [ ] Provide `.gitignore`, license/usage notes when appropriate and a dependency manifest.
- [ ] Tag each passed project gate, e.g., `p07-reviewed-v1`.
- [ ] Record the exact commit used to produce each plotted result.
- [ ] Link Git issues to an observed failure, expected result, evidence and corrective action.
- [ ] Verify a fresh clone works **without** unrecorded files from your own machine.
- [ ] Use private repositories where disclosure/contract/legal constraints require them; do not assume private hosting itself makes upload authorized.

### 1.3 Design record and decision log

- [ ] Keep a one-page project architecture drawing updated as interfaces change.
- [ ] Maintain a table of subsystem inputs, outputs, units, timing and ownership.
- [ ] Write the alternative designs considered before choosing a key actuator, sensor, planner or middleware.
- [ ] Record the reason for each decision and an observable reversal criterion.
- [ ] Document what was measured versus calculated versus simulated versus assumed.
- [ ] Record any standards edition/status checked and its **specific applicable scope**.
- [ ] Date each review and record unresolved issues with their risk or consequence.
- [ ] Keep meeting/mentor feedback separate from your own conclusions.

**Decision-record template** (`docs/adr/0001-example.md`):

```markdown
# ADR-0001 — [Decision]
Date:
Project / gate / commit:
Status: proposed | accepted | superseded
Problem and constraints:
Options considered:
Why this option was chosen:
Assumptions and measurements:
Safety / privacy / export implications:
What will trigger reconsideration:
Reviewers / open questions:
```

## 2. Minimum repository contract

```text
robotics-portfolio/
├── README.md
├── ROADMAP_PROGRESS.md            # gates and truthful E/W/P claims
├── docs/
│   ├── requirements.md
│   ├── operating_envelope.md
│   ├── architecture.md
│   ├── interfaces.md
│   ├── units_and_frames.md
│   ├── hazard_log.md
│   ├── standards_register.md
│   ├── verification_matrix.md
│   ├── test_report.md
│   ├── review_log.md
│   ├── cost_ledger.md
│   └── adr/
├── calculations/                 # notebooks / clear assumptions
├── cad/                          # source and permitted neutral exports
├── electronics/                  # schematic / BOM / bench boundary
├── firmware/
├── ros2_ws/src/
├── simulation/
├── configs/                      # non-secret versioned parameters
├── tests/
├── scripts/
├── data/README.md                # provenance and safe download path
├── evidence/README.md            # plots, clips, run IDs, no secrets
└── .github/workflows/            # software CI, not a safety certificate
```

**Do not create dozens of empty folders at P01.** Add only what the current gate needs, then retain consistent names across later projects.

---

# H2 — TESTING, METRICS AND REPRODUCIBILITY

## 3. Think in requirements → test → evidence links

### 3.1 Requirements writing (minimum per project)

- [ ] Each requirement names an observed behavior, not “works well.”
- [ ] Each criterion contains unit, threshold/tolerance or explicit qualitative observation.
- [ ] Record test conditions, assumptions and intended operating envelope.
- [ ] Add at least one nominal case, one boundary case and one realistic failed case.
- [ ] Separate a software requirement from any required independent safety function.
- [ ] Link every critical requirement to a repeatable test and archived evidence.
- [ ] Mark `NOT TESTED`, `SIMULATED`, `BENCH MEASURED` or `QUALIFIED EXTERNAL TEST` accurately.
- [ ] If physical instrumentation is absent, **do not** describe model output as measured hardware data.
- [ ] State what constitutes a failed gate and who is authorized to accept rework.

### 3.2 Testing ladder — add depth as the stage requires

| Level | Example | Earliest useful stage | Evidence |
|---|---|---|---|
| Unit test | motor-unit conversion, FK transform inverse, frame naming | 01 | test result, expected output |
| Numerical/reference test | derived model against known/independent result | 01–02 | notebook and error plot |
| Software integration | Python/C++ ROS topic, service, action, launch | 03 | clean build + run logs |
| Simulation scenario | robot commands, contacts/limits and repeatable world | 03–04 | config, clip and run ID |
| Logged-data replay | reproduce timestamp/estimation bug from a bag | 03–04 | rosbag2 ID and reproduction steps |
| Fault injection | missing sensor, stale command, broker loss, bad update | 02–06 | expected vs actual state trace |
| Guarded bench | low-energy physical response under reviewed controls | 02+ optional | wiring review, logs, operator boundary |
| Site qualification | safety-related work to applicable current requirements | outside self-study | authorized qualified organization’s records |

### 3.3 Test data discipline

- [ ] Identify sample rate, clock source and timestamp convention.
- [ ] Log units, frame ID, calibration/config version and software commit.
- [ ] Preserve relevant raw data or a lawful accessible retrieval method.
- [ ] Record environment (lighting, load, surface, temperature, noise) when influential.
- [ ] Plot error and a baseline comparison, not only success screenshots.
- [ ] Quantify trial count and variability; distinguish demonstration from reliable performance.
- [ ] Make log filenames linkable to requirements and experiment IDs.
- [ ] Retain known failures and explain their disposition.
- [ ] Keep test fixtures and simulated scenarios under version control where practical.
- [ ] Define what data are too sensitive or bulky to publish and provide a safe substitute.

### 3.4 CI: useful but carefully scoped

- [ ] Start with syntax, formatting and unit tests; add integration tests gradually.
- [ ] Pin or record Ubuntu, Python, compiler, ROS 2 and Gazebo versions.
- [ ] Run build and tests on every meaningful pull request when feasible.
- [ ] Distinguish fast deterministic CI from costly/fragile simulator scenarios.
- [ ] Make transient test failures visible rather than deleting tests.
- [ ] Produce a build/test summary tied to the tested commit.
- [ ] Keep secrets out of CI logs and public build artifacts.
- [ ] For firmware, clearly indicate which tests use a mocked MCU rather than actual hardware.
- [ ] Never report green CI as proof of functional-safety certification.

### 3.5 Monthly independent reproduction drill

```text
1. Create a clean checkout on another directory or machine.
2. Follow the README without relying on undocumented local state.
3. Install the stated compatible dependencies and configuration.
4. Run one canonical command or documented sequence.
5. Recreate one baseline plot and one failed-case plot.
6. Verify units, timestamps, frames, expected output and run IDs.
7. Record omissions and repair the instructions.
8. Tag the passing revision; retain remaining limitations.
```

**Gate rule:** if the artifact cannot be reproduced, the evidence is not yet ready for CV or graduate applications, regardless of how impressive a video looks.

---

# H3 — EXTERNAL REVIEW AND MENTORSHIP

## 4. Review calendar aligned with the earlier stages

| When / original gate | Who to look for | Focus of review | What you provide | Closure standard |
|---|---|---|---|---|
| Month 3 — P02/P03 | robotics/kinematics peer, university lab | units, transform order, frames, FK/IK edge cases | diagrams, tests, CAD and notebook | reproduce corrected edge case |
| Month 6 — P04/P05 | **qualified** electrical/controls person for bench design | wiring, protection, timing, saturation, timeout and stop claims | schematic, test boundary, plots | revised rig/test plan; no unsafe tests |
| Month 12 — P06/P07 | ROS 2 peer, maintainer/community | packages, `tf2`, QoS, time, launch and reproducibility | minimal repo, launch, logs, frame tree | fresh clean build and closed issue |
| Month 18 — P08 | estimation/controls practitioner | noise assumptions, drift, covariance, ground truth, timestamp errors | raw/replay data, baseline/fusion plots | corrected model and repeat test |
| Month 22–24 — P09–P11 | systems engineer/domain peer | task recovery, interfaces, hazard and one-track choice | run video, state chart, matrix | bounded scope and gap list |
| Months 27–30 — P12/P13 design | industrial / field / IoT specialist | **A:** PLC/robot fault logic; **B:** communications/localization claims; **C:** auth/OTA/offline boundaries | architecture, test plan, public data | corrected acceptance criteria |
| Months 33–36 — P12/P13 handoff | domain reviewer + systems/software peer | independent reproduction, realistic limits, faults, maintenance | full package, evidence map | action log resolved or risk accepted by rightful authority |

### 4.1 Get the most out of a review

- [ ] Ask one or two *precise* technical questions rather than “review my entire robot.”
- [ ] Include expected vs actual behavior and the smallest reproducible failure.
- [ ] Include exact software/firmware version, commit, unit and frame conventions.
- [ ] Provide a diagram or schematic instead of a paragraph where it clarifies interfaces.
- [ ] Show what you tried and what result changed.
- [ ] Name the test boundary: simulated, de-energized, or authorized supervised low-energy.
- [ ] Strip secrets, personally identifying data, employer IP and controlled information.
- [ ] Separate feedback received from your interpretation of it.
- [ ] Convert each actionable point into a Git issue and a regression test where possible.
- [ ] Send a concise follow-up with what changed, what remains open and why.
- [ ] Do not claim expert sign-off because a forum post received no objections.

**Review request template** (`docs/review_request.md`):

```markdown
# Review request — [gate / component]
Commit / configuration / run ID:
Operating mode: SIM | BENCH | authorized site
Expected behavior (units / frames / limits):
Actual behavior + screenshot / log / plot:
Minimum reproduction steps:
Previous hypotheses and experiments:
One or two specific reviewer questions:
Safety and information-sharing boundaries:
My proposed next experiment:
```

### 4.2 Mentorship and contribution channels

- [ ] Keep a running shortlist of university labs, makerspaces, ROS groups, professional societies and industry mentors.
- [ ] Ask for **a single scoped review**, not indefinite unpaid supervision.
- [ ] Offer a concise architecture diagram, known limitations and minimal repo.
- [ ] Contribute a documentation fix, regression test or scoped bug fix to an open-source project used in your portfolio.
- [ ] Follow upstream contributor guidelines and avoid dumping capstone code on maintainers.
- [ ] Seek a qualified reviewer for electrical power, machinery or site-risk decisions; a general code review does not replace one.
- [ ] Record mentor guidance and your implementation evidence without implying employment, affiliation or certification.

---

# H4 — SAFETY, STANDARDS AND INFORMATION GOVERNANCE

## 5. Every-stage safety checklist

- [ ] Describe the platform’s kinetic, electrical, thermal and stored-energy hazards.
- [ ] Document who can command motion, how to halt it and how to prevent unexpected restart.
- [ ] Distinguish normal software stop from an independently engineered protective/emergency stop.
- [ ] Define local timeout/stale-command behavior *before* any networked command tests.
- [ ] Keep hazardous/high-energy tests out of unsupported DIY setups.
- [ ] Use low-energy guarding and **qualified review** when a physical rig has credible hazards.
- [ ] Verify that loss of Internet/cloud/broker/dashboard cannot defeat independent local stop/control.
- [ ] Check exposure of bystanders, pets, public roads, airspace and site access before physical experiments.
- [ ] Treat supervised site work, environmental qualification and formal standards conformance as outside a hobby gate.
- [ ] Add a safe-restart test after each firmware/software update that changes motion behavior.
- [ ] Add an owner and resolution status to each hazard; never close one by “seems fine.”

### 5.1 Hazard log template

| ID | Hazard / initiating event | Harm or loss | Protective measure | Verification method | Status/owner |
|---|---|---|---|---|---|
| H-001 | Example: stale velocity command | unintended continued motion | local watchdog and independent stop strategy | bounded timeout test; qualified review as required | open / owner |

**Example does not prescribe a safety architecture or prove a safety rating.** Actual protective measures and performance requirements depend on the hazards, applicable standards and competent design review.

### 5.2 Standards and compliance register

- [ ] Store exact standard or regulation identifier, edition and date verified.
- [ ] Record what system and jurisdiction/application it governs.
- [ ] Identify exclusions rather than extending a robot standard to every platform.
- [ ] Distinguish public overview from full authorized/licensed standard text.
- [ ] Reverify editions and contract/site applicability when moving from study to a real design decision.
- [ ] Mark items as `LEARNING ONLY`, `POSSIBLY APPLICABLE — VERIFY`, or `APPLICABLE — AUTHORIZED REVIEW`.
- [ ] Document the name/role of the **responsible organization** for qualification or legal/compliance decisions.

| Reference family | Relevant in this roadmap | Stage 07 reminder |
|---|---|---|
| ISO 10218 / ISO 12100 / ISO 13849 and applicable industrial standards | chosen industrial system | check current edition, scope, national law and competent safety assessment; not transferable automatically to defense/airborne/underwater |
| MIL-STD-810 and MIL-STD-882 public literacy; public NGVA/STANAG 4754 references | non-weaponized field orientation | current issue, distribution and program tailoring require authorized review; no DIY qualification claim |
| ITAR/EAR and relevant local/export requirements | possible defense-sector work | jurisdiction, item/data/end user/end use require legal/organization process; public learning is not a classification |
| Privacy, software licensing, RF and aviation/site rules | all stages where applicable | verify locality and permissions; do not assume research exemptions |

### 5.3 Information release decision

```text
Before publishing CAD, source code, video, logs or datasets:
  Is it mine to publish and is the license compatible?
    ↓ yes
  Does it include customer/employer IP, access tokens or private people?
    ↓ no
  Does it involve controlled/program-restricted material or uncertain export status?
    ↓ no, as confirmed under the relevant process
  Is the test safe to describe without enabling unsafe reproduction?
    ↓ yes
  Publish a clearly labeled educational artifact and its limits.
Otherwise → keep private under approved controls; seek authorized guidance.
```

**Never use a public AI chat, public issue tracker, generic cloud bucket or personal GitHub to circumvent an employer/program’s information controls.** This roadmap is not legal advice.

---

# H5 — TIME, BUDGET AND ASSET MANAGEMENT

## 6. Time-box the habits inside the existing weekly hours

| Activity | Typical 15-hour week | Frequency |
|---|---:|---|
| Current-stage math/theory | 2 h | weekly |
| Software / embedded implementation | 4 h | weekly |
| CAD / electronics / simulation | 3 h | weekly |
| Project integration and tests | 4 h | weekly |
| **Stage 07 notes, review and planning** | **2 h** | weekly |
| **Total** | **15 h** | **not 17 h** |

**Week of a formal review:** move ~1–3 h *from theory/features* into review response and test repair. A review week is engineering work, not a surprise surcharge.

### 6.1 A sustainable four-week loop

| Week | Do | Evidence |
|---|---|---|
| 1 — plan | set one gate increment, acceptance test and risks | scope/issue list |
| 2 — implement | build smallest tested change | commit, result |
| 3 — stress | test a boundary and one likely failure | plots, bug report |
| 4 — demonstrate | live/replay demo, documentation, review request if due | demo + concise report |

**Every ~12 weeks:** reserve a review-and-rework week; review the budget, gate status and whether a planned topic is still load-bearing.

### 6.2 Purchase gates rather than shopping lists

- [ ] Attach each purchase to an upcoming experiment with a pass/fail question.
- [ ] Check what can be borrowed or simulated at zero incremental hardware cost.
- [ ] Verify voltage, current, heat, connectors, fuse/protection and compatibility for physical items.
- [ ] Check real vendor documentation before mixing drivers, batteries or motors.
- [ ] Include shipping, local taxes, exchange-rate uncertainty and **15–25% contingency**.
- [ ] Count failed parts/consumables/spares, not only the first-kit price.
- [ ] Identify a safe bench location and any qualified supervision costs before purchasing.
- [ ] Set cloud free-tier and spend alerts; delete unused resources after IoT exercises.
- [ ] Record subscription/license renewals and certifications separately from hardware.
- [ ] Compare “physical proof” and “simulation proof” honestly; don't buy physical equipment solely to remove an E label.

### 6.3 Existing shared-roadmap budget, not a new Stage 07 charge

| Main stage | Indicative **incremental** budget (USD, planning band) | Simulation-only alternative |
|---|---:|---|
| 01 — P01–P03 | $0–60 | existing computer + free tools |
| 02 — P04–P05 | $70–250 | simulated motor and recorded/virtual encoder; bench-only claims not made |
| 03–04 — P06–P11 | $150–500 | ROS 2/Gazebo and logged data; no physical P11 claim |
| 06-A industrial | $100–700 | virtual PLC/robot workcell; no real fieldbus or safety-rating claim |
| 06-B rugged field | $150–1,000 | simulated sensor/link/environment failures; no qualification claim |
| 06-C IoT/IIoT | $0–350, usage variable | local broker and 3–10 simulated identities; no production PKI claim |
| Optional qualified lab/training | $0–1,500+ | defer hazardous/qualified tests until authorized access exists |

These are inherited educational estimates, **not current retailer prices**, and exclude existing PC, professional certification fees, site access and tuition. **Stage 07's incremental tool cost can be $0**: Markdown, Git, issue trackers, spreadsheets/CSV and local backups are sufficient.

### 6.4 Monthly cost/time ledger template

```csv
month,stage,gate,planned_hours,actual_hours,cost_type,planned_usd,actual_usd,reason,simulation_option,decision
1,01,P01,60,0,software,0,0,units notebook,existing PC,planned
```

- [ ] Review completed vs planned hours without converting fatigue into an ethical failure.
- [ ] Note blocker type: math, software, access, hardware, safety, reviewer, time or budget.
- [ ] Keep decisions and forecast dates visible; shift dates when evidence is missing.
- [ ] Spend any surplus on test quality and reviewer access before collecting extra sensors.

---

# H6 — PORTFOLIO, CREDENTIALS AND CAREER / ACADEMIC SIGNAL

## 7. A project page an engineer can actually evaluate

Each of P01–P13 deserves a concise page or README section. Expand from 1 page at early gates to a complete handoff dossier at P12/P13.

- [ ] Problem and user, with permitted use case and operating boundary.
- [ ] Architecture showing mechanical, electrical, firmware, ROS 2 and cloud layers only where relevant.
- [ ] Your exact contribution; attribute tutorials, teams, datasets and upstream libraries.
- [ ] Constraints: payload, compute, timing, accuracy, reliability and budget as appropriate.
- [ ] Design trade-off with rejected option(s), not merely a list of technologies.
- [ ] Reproducible setup and sample input.
- [ ] Demo image/video **plus** raw/derived evidence and command to reproduce.
- [ ] Baseline comparison and at least one documented failure/fix.
- [ ] Safety and information scope; simulation vs physical claim clearly marked.
- [ ] E/W/P status supported by acceptance tests and reviewer notes.
- [ ] Known limitations, future work and applicable version details.

### 7.1 CV claim → proof map

| CV or interview claim | Minimum supporting artifact | Avoid claiming |
|---|---|---|
| “Built a ROS 2 simulated robot” | P07 repo, Xacro/URDF, launch, video, tests | real-hardware deployment if none |
| “Implemented sensor fusion” | P08 baseline vs fused plots, timing, failure analysis | solved general SLAM |
| “Integrated industrial robot logic” | P12-A PLC/robot state traces and metrics | real factory commissioning or safety certification |
| “Built field robot reliability prototype” | P12-B safe degraded-mode test and endurance model | MIL-STD qualification or defense acceptance |
| “Implemented robot-fleet telemetry and OTA” | P13 unique identities, dashboard, WAN loss, rollback evidence | production PKI or Internet-dependent safety control |

### 7.2 Monthly public communication (only permitted artifacts)

- [ ] Publish or privately present a short engineering note: problem → method → result → limit.
- [ ] Give numbers with units and denominators where relevant (e.g., trial count).
- [ ] Include one negative result or diagnostic improvement.
- [ ] Explain one transferable lesson across mechanical/electrical/software boundaries.
- [ ] Link to a tagged commit rather than the mutable latest branch when showing a particular result.
- [ ] Review for controlled data, privacy, employer IP, credentials and unsafe demo steps.
- [ ] Keep graphics readable and avoid ungrounded performance claims.

## 8. Credentials: prioritize exact named awards only when they fit

**A certificate is a credential, not a substitute for proof.** Some robotics providers issue course-completion certificates rather than proctored professional certifications. Describe them accurately on a CV; do not call a course-completion badge an accredited engineering qualification. Check the issuer's official page for the **exact current credential name**, exam code/availability, eligibility, price, renewal and geographic access **at the time you register**.

| When relevant | Named credential or training example | What it can support | What it cannot prove alone |
|---|---|---|---|
| Stage 01–03, Linux-heavy | **Linux Foundation Certified System Administrator (LFCS)** | Linux administration evidence | ROS 2 or robotics integration proficiency |
| Stage 01–03, repository collaboration | **GitHub Foundations** | GitHub platform/workflow knowledge | engineering review maturity |
| Stage 01, if Python needs a formal proof | **PCAP – Certified Associate in Python Programming** | general Python competence | robotics control or kinematics |
| Stage 06-C, if cloud is chosen | **AWS Certified Cloud Practitioner** | cloud vocabulary | fleet identity, OTA and robot safety |
| Stage 06-C, Azure path chosen | **Microsoft Certified: Azure Fundamentals (AZ-900)** | Azure foundations | production IoT integration |
| Stage 06-A/C, SCADA relevant | **Ignition Core Certification** | specific SCADA platform competence | industrial safety rating / all-vendor PLC competence |
| Stage 06-B, systems roles | **INCOSE ASEP**, subject to eligibility and current program rules | systems engineering knowledge | field qualification, clearances or export authorization |

**Do not collect all seven.** Choose only those that map to your target role, budget and existing skills. Vendor-specific robot/PLC training is often tied to the actual equipment available; verify the issuer’s exact current course title before putting it on a study plan or CV. List it as **completed training**, not certification, unless the issuer specifically grants a credential under that title.

### 8.1 Credential decision gate

- [ ] Identify one named target role and two or three relevant job requirements.
- [ ] Decide whether an award closes a real evidence gap or simply repeats existing work.
- [ ] Validate the credential on the issuer’s official website and log the verification date.
- [ ] Record total fees, prerequisites, time cost, exam modality and expiry/renewal.
- [ ] Ensure the certificate will not delay P03/P05/P07/P08/P12/P13 acceptance.
- [ ] Pair the credential with one portfolio project proving an applied skill.
- [ ] Store a proof URL/credential ID only where publication is appropriate.
- [ ] Reevaluate each quarter; if behind, delay the exam rather than cut tests.

### 8.2 Graduate-study and research support — optional parallel branch

- [ ] Keep a short literature map for the engineering problems actually encountered.
- [ ] Reproduce a relevant published baseline before proposing novelty.
- [ ] Compare methods on the same bounded dataset/scenario and declared metrics.
- [ ] Preserve negative results and method limitations, not just a final diagram.
- [ ] Ask a supervisor/lab mentor for a feasible thesis scope tied to one chosen domain.
- [ ] Show authorship and data provenance for code, datasets and prior work.
- [ ] Distinguish an MSc engineering thesis from a PhD research contribution; neither is unlocked by course completion alone.

**Academic project ladder:** `reproduce → modify → integrate → benchmark → publish/present where appropriate`. A thesis should contribute evidence or new knowledge under an advisor’s requirements, not simply restate the roadmap.

---

# H7 — RECOVERY, RETROSPECTIVES AND LONG-TERM CONTINUITY

## 9. The anti-burnout and anti-breadth rules

- [ ] Set a weekly *minimum viable increment* (one tested feature or corrected failure).
- [ ] Do not run Stage 05 optional mathematics as a second full curriculum.
- [ ] Keep **one** primary P09 planner: Nav2 OR MoveIt 2; other remains E unless extra time is available.
- [ ] Keep **one** primary Stage 06 specialization for the 30–36 month target.
- [ ] Reserve months 31–36 for testing, integration, rework and independent reproduction.
- [ ] Downgrade claimed depth rather than silently dropping acceptance criteria.
- [ ] Defer purchases and exams before cutting load-bearing engineering tasks.
- [ ] Log a blocker early and seek a scoped reviewer before struggling indefinitely.
- [ ] If physical access is absent, use simulation and label the evidence correctly.
- [ ] Take legitimate breaks; resume from a recorded next action rather than rebuilding the project from scratch.

### 9.1 Quarter-by-quarter Stage 07 emphasis

| Main stage period | What Stage 07 should emphasize | Formal checkpoint |
|---|---|---|
| Months 1–3 | units, frames, derivations, project repo and first review | P01–P03 evidence + frame review |
| Months 4–6 | wiring/test boundary, motor data, control plots | P04/P05 electrical/control review |
| Months 7–10 | package discipline, C++/Python tests, launch and CI | P06 clean clone |
| Months 11–14 | `tf2` audit, robot model, ROS time/QoS, rosbag2 | P07 independent simulation run |
| Months 15–18 | sensor provenance, ground truth, covariance and timing | P08 estimation review |
| Months 19–22 | one planner, recovery, perception error and integration | P09–P11 bounded-system demo |
| Months 23–26 | track choice, domain scope and first hazard/threat work | orientation and design review |
| Months 27–30 | acceptance tests, interface defects, domain reviewer | P12/P13 design freeze |
| Months 31–36 | repeated trials, independent reproduction and portfolio claims | P12; P13 for IoT-primary |
| Months 37+ if combining tracks | distinct second-track results and review, not one project relabeled twice | new separate evidence |

### 9.2 Recovery / triage matrix

| At checkpoint | Never cut | Defer/cut first | Recommended recovery |
|---|---|---|---|
| Month 3 | SI units, transforms, frame tests and P01–P03 proof | ornamental CAD detail, extra languages | shrink P03 visualizer; repair math and test cases |
| Month 6 | safe power boundary, timing, encoder feedback, bounded PID and fault state | extra actuators, RTOS, LQR/MPC, hardware glamour | simulation if bench unavailable; retain P04/P05 faults |
| Month 12 | ROS nodes, `tf2`, URDF, one simulator, tests, rosbag2 | micro-ROS, custom middleware, extra models | freeze stack; one small robot + clean P07 repo |
| Month 18 | timestamps, calibrated error, baseline vs fusion | SLAM internals, particle filters, advanced ML | logged data + simple filter and failure report |
| Month 22–24 | one planner, recovery, integration, hazards | second planner, unchosen track, physical build if unsafe | P11 simulation-only with honest W label |
| Month 30: industrial | I/O/state model, timeout/recovery and workcell test | second PLC, robot vendor or fieldbus | narrow to one virtual cell |
| Month 30: field | safe lost-link/localization limits, FMEA, power model | multiple radios/platforms, broad environmental matrix | one benign mock route and repeated simulated faults |
| Month 30: IoT | identity, least privilege, offline safety, OTA recovery | second cloud, elaborate ML dashboard | one platform + 3 simulated robots and P13 core |

**Non-negotiable:** never defer operator protection, energy isolation where necessary, required legal/site approvals, data controls, hazard identification, or the distinction between educational evidence and formal certification. If an approved safe physical test is unavailable, stay simulated or de-energized.

### 9.3 Monthly retrospective template

```markdown
# Monthly robotics retrospective — YYYY-MM
Stage(s) / gate(s):
Planned hours / actual hours:
What was demonstrated, and on what commit?
What numerical evidence is new? Include units and trial counts.
What failure was discovered and reproduced?
What correction was implemented and retested?
What is still unverified or unsafe?
What did a reviewer say? What remains open?
Costs this month / next stage purchase decision:
E/W/P status with evidence URL:
Top 1–3 priorities next month:
Topics/certifications explicitly deferred:
```

---

# 10. Thirty-six-month heartbeat (plus extension)

| Rhythm | Smallest useful action | Typical time |
|---|---|---:|
| Every work session | annotate assumption, units, code change and next experiment | 5–15 min within task |
| Every week | push/test working increment, update blocker list and budget | ~2 h reserved across week |
| Every four weeks | demonstrate, compare baseline, retain failed case, clean README | ~2–4 h drawn from study/build time |
| Every ~12 weeks | external review request + rework buffer + stage decision | ~4–8 h within that period |
| Each gate P01–P13 | evidence map, fault test, operating boundary, depth label, tag | integrated with gate work |
| Every six months | independent reproduction and CV/job-path check | ~half to one study day |
| Before public release | license/secret/IP/controlled-data review | as required; block release if unresolved |
| Before real deployment | authorized qualified safety/legal/program review | **not a self-study time box** |

### One-page dashboard to update monthly

```markdown
# ROADMAP_PROGRESS
| Gate | Target month | State | Depth | Mode | Evidence/tag | Reviewer/open risk |
|---|---:|---|---|---|---|---|
| P01 | 1–2 | NOT STARTED | — | SIM | — | — |
| P02 | 2–3 | NOT STARTED | — | SIM | — | — |
| P03 | 3 | NOT STARTED | — | SIM | — | — |
| P04 | 4–5 | NOT STARTED | — | SIM or BENCH | — | — |
| P05 | 5–6 (+ recovery) | NOT STARTED | — | SIM or BENCH | — | — |
| P06 | 7–10 | NOT STARTED | — | SOFTWARE | — | — |
| P07 | 11–14 | NOT STARTED | — | SIM | — | — |
| P08 | 15–18 | NOT STARTED | — | SIM / LOG REPLAY | — | — |
| P09 | 19–22 | NOT STARTED | — | SIM | — | — |
| P10 | 15–22 | NOT STARTED | — | SIM / DATA | — | — |
| P11 | 19–22 | NOT STARTED | — | SIM / BENCH | — | — |
| P12 | 23–36 | NOT STARTED | — | CHOSEN TRACK | — | — |
| P13 | 31–36 if IoT primary | NOT STARTED | — | SIM / BENCH | — | — |
```

**P13:** for IoT-primary learners, complete at W→P within Stage 06; for industrial/field-primary learners it remains optional E/W unless the timeline extends. **P12:** 24-month version is orientation; 30–36-month version is one bounded specialization capstone. No single timetable establishes competence without evidence.

---

# 11. Stage 07 acceptance checklist — how to know the habits are working

This is a **process self-audit**, not a separate certification or another stage-ending exam. Apply it at months 3, 6, 12, 18, 24, 30 and 36.

- [ ] I can identify the current gate, its dependencies, actual status and honest depth label.
- [ ] Every numerical result has a unit and an identified model/measurement source.
- [ ] The current repository can be rebuilt from its own instructions.
- [ ] At least one failed or boundary scenario is archived for the current gate.
- [ ] Tests link to requirements and a known software/configuration revision.
- [ ] Safety-critical functions do not depend on cloud/Internet/LLM availability.
- [ ] The hardware/simulation boundary is stated without exaggeration.
- [ ] Current operating hazards and information-sharing limits are documented.
- [ ] At least one scoped external review has been requested at the relevant checkpoint; feedback or lack of feedback is accurately logged.
- [ ] Reviewer actions have owners and closure evidence; unresolved issues remain visible.
- [ ] Standards scope/version is rechecked at the point of a real applicable decision.
- [ ] Cost and time forecast are current and do not require unsafe shortcuts.
- [ ] Certifications in the plan are named accurately and selected for a specific role, not because they appear on a diagram.
- [ ] The public portfolio contains only material I am permitted to release.
- [ ] The next work session has one explicit action; advanced mathematics is only added for a demonstrated need.
- [ ] My CV distinguishes training, certifications, simulation, lab work and qualified industrial/defense experience.
- [ ] If I am behind, I shifted the timeline or scope instead of declaring an untested gate complete.

**Stage 07 north star:** *Every robotics claim can be traced to a bounded requirement, a reproducible artifact, a measured or explicitly simulated result, a failure case, a safety/information boundary, and an honest account of what remains unproven.*
