# Robotics Engineering — Curated Online Courses for All Seven Stages

**Companion to:** `Complete_Robotics_Engineering_Roadmap_Revised_v2.md` and `Robotics_Stage_01` through `Robotics_Stage_07`  
**Research checked:** September 24, 2026  
**Purpose:** a clickable *learning-resource map* that links actual named courses, teaching series, and official guided tutorials to the exact project gates of the seven-stage roadmap. This is **not** a second, larger sequential syllabus.

> **How to read:** **Anchor** = the primary guided route for that subtopic; **Alternative** = choose it **instead** if its presentation or price suits you; **Reference / lab** = use while building; **Optional** = only if a gap or specialization requires it. **Free course** does not necessarily mean **free verified certificate**. A platform course-completion certificate is not the same as a separate professional exam/certification. Course listings, fees, eligibility, provider names, software versions and access can change; check the linked provider before purchase. Time recommendations below are **suggested portions of your robotics study schedule**, not promises about how long a provider’s entire course takes.

**Existing seven-stage structure:** 01 Foundations (M1–3: P01–P03) → 02 Electronics + Control (M4–6: P04–P05) → 03 ROS 2 + Robot Software (M7–14: P06–P07) → 04 Estimation + Perception + Planning (M15–22: P08–P11) → 06 One Specialization (M23–36: P12, plus P13 if IoT primary). **05 Advanced Mathematics** is an *on-demand* side lane; **07 Ongoing Parallel Habits** runs throughout. Keep **12–18 total focused hours/week**, not 12–18 hours per course.

**Project evidence rule:** for every resource, copy a useful technique into your own repository; derive/check units where relevant; run at least one test or measured comparison; record the course name and link in your learning log. Watching the whole video series without doing the stage gate does not count as completing that gate.

## Fast-start learning stack — one anchor per need

| Need | Choose this named resource first | Why it is mapped here |
|---|---|---|
| Linear algebra / frames | [MIT 18.06SC — Linear Algebra, Gilbert Strang](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | Matrix operations and coordinate transforms for P02/P03. |
| Robotics kinematics | [Modern Robotics: Mechanics, Planning, and Control — Northwestern University](https://www.coursera.org/specializations/modernrobotics) | The shared theoretical thread from P03 to planning. Use **selected lessons**, not all six courses in Stage 1. |
| Electronics | [Introduction to Electronics — Georgia Tech](https://www.coursera.org/learn/electronics) | Electronics refresh for motor/sensor bench. |
| Firmware | [Introduction to Embedded Systems Software and Development Environments — University of Colorado Boulder](https://www.coursera.org/learn/introduction-embedded-systems/) | Embedded C, GCC/Make, testing and configuration management. |
| Feedback | [MIT 6.302 — Feedback Systems](https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/) | The motor model/response ideas that P05 tests. |
| ROS 2 | [ROS 2 Jazzy Tutorials — Open Robotics](https://docs.ros.org/en/jazzy/Tutorials.html) | Versioned, task-based learning for P06. |
| Estimation | [State Estimation and Localization for Self-Driving Cars — University of Toronto](https://www.coursera.org/learn/state-estimation-localization-self-driving-cars) | Sensor, covariance and filtering practice for P08; adapt ideas to a small rover. |
| Computer vision | [OpenCV Bootcamp — OpenCV University](https://opencv.org/university/free-opencv-course/) | Free, focused route into P10; not sufficient on its own for full robot perception. |
| Planning | [Motion Planning for Self-Driving Cars — University of Toronto](https://www.coursera.org/learn/motion-planning-self-driving-cars) | A*, Dijkstra, trajectory and behavior fundamentals for P09. |
| ML **when P10 needs it** | [Machine Learning Specialization — Andrew Ng, DeepLearning.AI + Stanford Online](https://www.coursera.org/specializations/machine-learning-introduction) | The recognizable Andrew Ng course you asked to see; do **not** insert it ahead of basic sensing/control. |
| DL **when P10 needs learned vision** | [Deep Learning Specialization — Andrew Ng / DeepLearning.AI](https://www.coursera.org/specializations/deep-learning) | CNNs and model-debugging foundations; optional if geometry solves P10. |

---

# STAGE 01 — FOUNDATIONS (MONTHS 1–3; P01, P02, P03)

**Goal:** establish units, vectors, calculus, matrices, 2D/3D transforms, CAD and a tested 2-link-arm model. You can test out of basic Python/mechanics and spend the saved hours on transforms and verification.

| Roadmap subtopic | Named online course / series — exact URL | Use in Stage 1 | Route |
|---|---|---|---|
| Units, algebra, trig, derivative/integral refresher | [Khan Academy — Differential Calculus](https://www.khanacademy.org/math/calculus) | Revisit only derivatives needed for velocities/Jacobian; do not restart all secondary-school math. | Gap-filler |
| Vectors, matrices, inverses, transformation chains | [MIT OpenCourseWare — 18.06SC Linear Algebra (Gilbert Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | Select systems, matrix multiplication, linear transformations; write P02 tests. | **Anchor** |
| Visual intuition for matrix multiplication and basis changes | [3Blue1Brown — Essence of Linear Algebra, Chapter 3: Linear Transformations and Matrices (YouTube)](https://www.youtube.com/watch?v=kYB8IZa5AuE) | Visual complement before/alongside Strang; then implement your own rotation/translation. | Alternative / supplement |
| Robotics configuration, frames and 2-link arm | [Northwestern / Coursera — Modern Robotics, Course 1: Foundations of Robot Motion](https://www.coursera.org/learn/modernrobotics-course1) | Select introductory configuration/frames material; full screw-theory depth is **not** a P03 prerequisite. | Anchor modules |
| Robot kinematics beyond the introductory modules | [Northwestern — Modern Robotics: Mechanics, Planning, and Control Specialization](https://www.coursera.org/specializations/modernrobotics) | Use the kinematics portions to verify FK/IK/Jacobian; revisit other courses in Stages 4–5. | Reference |
| Basic statics, free-body diagrams, torque | [Georgia Tech / Coursera — Introduction to Engineering Mechanics](https://www.coursera.org/learn/engineering-mechanics-statics) | Select torque/equilibrium modules for P01; you may skip already-mastered sections. | Refresher |
| Mechanics: inertia, torque, energy | [MIT OCW — 8.01SC Classical Mechanics](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) | Choose rotation and work/energy; apply to wheel/arm sizing. | Reference |
| Python fundamentals + unit tests if needed | [Harvard — CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Only the gaps relevant to NumPy, file output and tested calculations. The course is free to learn; a verified edX credential is a separate choice. | Alternative |
| Modern C++ to prepare for ROS 2 | [LearnCpp — The C++ Tutorial](https://www.learncpp.com/) | Compile/debug, functions, containers and references; continue in Stage 3. | **Anchor** |
| Shell, processes and permissions | [Linux Foundation — Introduction to Linux (LFS101)](https://training.linuxfoundation.org/training/introduction-to-linux/) | Command line, processes, packages and permissions; read only what your existing Linux competence needs. | Reference |
| Git, commits, branches, pull requests | [GitHub Skills — Introduction to GitHub](https://github.com/skills/introduction-to-github) | Create the P01–P03 repo and a reviewable PR. | Short lab |
| Parametric CAD / assemblies | [Autodesk — Get Started with Inventor (official tutorial collection)](https://www.autodesk.com/learn/ondemand/collection/get-started-with-inventor) | **Optional publisher learning hub**; if a particular lesson is unavailable, use your existing Inventor experience; produce a 2-link arm model and drawings. | Optional hub |

**Practical learning route:** weeks 1–4 P01 with units and motor-sizing; weeks 4–8 P02 with matrices/transforms; weeks 8–13 P03 with CAD, FK/IK and Jacobian. **Stage exit:** unit-checked notebook + frame inversion tests + 2-link visualizer and limits, not a pile of course completion badges.

---

# STAGE 02 — ELECTRONICS + CONTROL (MONTHS 4–6; P04, P05)

**Goal:** turn abstract motor torque and control into a protected low-energy bench **or honestly labeled simulation**. Use one motor/encoder/driver architecture; avoid buying extra actuator families.

| Roadmap subtopic | Named online course / series — exact URL | How to use | Route |
|---|---|---|---|
| Circuit refresh, components, analog measurement | [Georgia Tech / Coursera — Introduction to Electronics](https://www.coursera.org/learn/electronics) | Kirchhoff, diodes/transistors, op amps only as relevant to your rig; supplement protection/wiring from actual component datasheets. | **Anchor** |
| Basic MCU, GPIO, PWM and serial data | [UC Irvine / Coursera — The Arduino Platform and C Programming](https://www.coursera.org/learn/arduino-platform) | Quick hands-on option for a low-energy Arduino lab; use an MCU simulator when no physical setup is available. | Alternative |
| Embedded C, compiling, memory, Git, build tools | [University of Colorado Boulder / Coursera — Introduction to Embedded Systems Software and Development Environments](https://www.coursera.org/learn/introduction-embedded-systems/) | Build firmware and reproducible logs for P04; course assignments need not all be repeated. | **Anchor** |
| Bare-metal STM32 peripheral drivers | [FastBit / Udemy — Mastering Microcontroller and Embedded Driver Development](https://www.udemy.com/course/mastering-microcontroller-with-peripheral-driver-development/) | Deepen GPIO, timers, I²C/SPI/UART **only if using STM32**; not mandatory for an Arduino/simulated rig. | Optional deep dive |
| Motor/load feedback, transient response and margins | [MIT OpenCourseWare — 6.302 Feedback Systems](https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/) | Use motor-lab and response material for P05; save full Nyquist/root locus for Stage 5 if needed. | **Anchor** |
| Practical modeling and control extensions | [MIT — Underactuated Robotics, Russ Tedrake](https://underactuated.mit.edu/) | Read selected modeling/control sections after baseline PID works. | Reference / later |
| Sensor/motor systems beyond one axis | [University of Colorado Boulder / Coursera — Embedding Sensors and Motors Specialization](https://www.coursera.org/specializations/embedding-sensors-motors/) | Revisit later for sensor/actuator families; do **not** take the whole specialization before P05. | Alternative |

**P04 evidence:** protected wiring diagram or explicit simulation scope, command/sensor/current logs, safe-state demonstration. **P05 evidence:** controller code, plant assumptions, setpoint/load-change plots, sample time, saturation and anti-windup, stale-command/fault behavior. Physical work requires appropriate low-energy protection and qualified review; a software timeout is not an independent safety function.

---

# STAGE 03 — ROS 2 + ROBOT SOFTWARE (MONTHS 7–14; P06, P07)

**Goal:** one pinned, reproducible Ubuntu/ROS 2/Gazebo stack; a clean ROS 2 workspace; then a simulated model with validated frames, controllers, logs and tests. Use **Jazzy-versioned** material for your chosen Jazzy stack. Course/tutorials here are not interchangeable with certification exams.

| Roadmap subtopic | Named course / guided lab — exact URL | Use it for | Route |
|---|---|---|---|
| Nodes, topics, services, actions, parameters, packages | [Open Robotics — ROS 2 Jazzy Tutorials](https://docs.ros.org/en/jazzy/Tutorials.html) | Work through beginner → intermediate tasks; build P06 Python **and** C++ nodes. | **Anchor** |
| Overview of ROS 2 setup and compatibility | [Open Robotics — ROS 2 Jazzy Documentation](https://docs.ros.org/en/jazzy/) | Pin versioned install and developer references in README. | Reference |
| C++ build/debug alongside Python | [LearnCpp — The C++ Tutorial](https://www.learncpp.com/) | Focus on classes, ownership, errors, CMake-related compiler issues that your actual ROS package exposes. | Parallel |
| Geometry, transforms, timing, URDF/Xacro | [Open Robotics — ROS 2 Jazzy Tutorials](https://docs.ros.org/en/jazzy/Tutorials.html) | Complete `tf2`, URDF and launch tutorials; add frame/clock regression tests. | **Anchor units** |
| Modern Gazebo, simulation and model creation | [Gazebo Harmonic — Documentation and Tutorials](https://gazebosim.org/docs/harmonic/) | SDF/world basics, joints, simulated sensing and ros_gz bridge as appropriate. **Do not use Gazebo Classic tutorials as if they were Harmonic.** | **Anchor** |
| ROS 2/Gazebo version pairing | [Gazebo — Installing gazebo_ros packages for ROS 2](https://gazebosim.org/docs/harmonic/ros_installation/) | Verify matching distribution packages before any installation. | Reference |
| Controller manager, controller/hardware interfaces | [ros2_control — Getting Started (Jazzy)](https://control.ros.org/jazzy/doc/getting_started/getting_started.html) | Add controllers to the existing P07 robot. | **Anchor** |
| Ready-to-run simulated drive train | [ros2_control — DiffBot Demo (Jazzy)](https://control.ros.org/jazzy/doc/ros2_control_demos/example_2/doc/userdoc.html) | Compare your joint states, differential drive and Xacro to a maintained example. | Hands-on lab |
| Gazebo bridge to `ros2_control` | [gz_ros2_control — Jazzy Documentation](https://control.ros.org/jazzy/doc/gz_ros2_control/doc/index.html) | Use when connecting the **modern** Gazebo simulator to controllers. | Reference / lab |
| Debugging/model testing at package level | [Open Robotics — ROS 2 Jazzy How-to Guides](https://docs.ros.org/en/jazzy/How-To-Guides.html) | Target a specific unresolved runtime or package problem; tutorials come first. | Reference |

**P06 evidence:** clean build + 2 nodes + interfaces/actions/parameters + tests + launch + bag + fault handling. **P07 evidence:** URDF/Xacro + correct `tf2` + RViz + modern Gazebo + `ros2_control` + rosbag2 replay + diagnostics and a new-machine reproduction test. **Month-12 review:** frame tree, clock, QoS and architecture.

---

# STAGE 04 — ESTIMATION + PERCEPTION + PLANNING (MONTHS 15–22; P08–P11)

**Goal:** baseline vs fused state, calibrated inspection/perception, **one** planner, and one repeatable integrated robot. Machine learning is a **conditional tool for P10**, not a prerequisite for P08 or P09.

| Roadmap subtopic | Named course / guided learning — exact URL | How to use | Route |
|---|---|---|---|
| Probability and uncertain sensor measurements | [MIT OCW — 18.06SC Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | Review covariance-related matrix operations **only as needed** for P08; pair with estimation course below. | Math refresher |
| Odometry, IMU, least squares, KF/EKF | [University of Toronto / Coursera — State Estimation and Localization for Self-Driving Cars](https://www.coursera.org/learn/state-estimation-localization-self-driving-cars) | Follow baseline → noisy sensors → fusion, re-implement for small robot; automotive assumptions are not directly your rover's assumptions. | **Anchor P08** |
| OpenCV/image manipulation | [OpenCV University — OpenCV Bootcamp](https://opencv.org/university/free-opencv-course/) | Start P10 with morphology, edges, feature alignment, image/video basics. | **Anchor P10** |
| Calibrated vision and visual odometry | [University of Toronto / Coursera — Visual Perception for Self-Driving Cars](https://www.coursera.org/learn/visual-perception-self-driving-cars) | Use camera model/calibration and feature material; benchmark latency and failure conditions. | Deepening |
| More complete paid CV curriculum | [OpenCV University — Fundamentals of Computer Vision & Image Processing](https://opencv.org/university/fundamentals-of-computer-vision-and-image-processing/) | Alternative to piecing together multiple CV courses if a paid structured program is useful. | Alternative |
| Machine learning for inspection/classification | [Andrew Ng / Coursera — Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) | **Only if** your P10 task needs learned classification; use model evaluation and train/validation/test practice. | Conditional |
| CNNs / learned object detection or segmentation | [Andrew Ng / DeepLearning.AI — Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) | Study CNNs and generalization **after** a geometric baseline; budget inference time and energy. | Conditional / advanced |
| Graph search, constrained path and behavior planning | [University of Toronto / Coursera — Motion Planning for Self-Driving Cars](https://www.coursera.org/learn/motion-planning-self-driving-cars) | Dijkstra/A*, path vs trajectory, state machines. | **Anchor P09 theory** |
| Broader robot planning | [Northwestern / Coursera — Modern Robotics, Course 4: Robot Motion Planning and Control](https://www.coursera.org/learn/modernrobotics-course4) | Select chapters on planning/control relevant to chosen platform. | Alternative |
| **Mobile route only:** navigation stack | [Nav2 — Getting Started (Jazzy)](https://docs.nav2.org/jazzy/getting_started/) | One simulation world, navigation task and recovery. | **Choose A** |
| **Arm route only:** manipulation stack | [MoveIt 2 — Documentation and Tutorials](https://moveit.picknik.ai/) | Plan/execute one bounded pick/place task and handle a failed grasp. | **Choose B** |
| Task-level research/control extensions | [MIT — Underactuated Robotics](https://underactuated.mit.edu/) | Only if P09/P11 behavior cannot be solved with the bounded baseline. | Optional |

**P08:** baseline/fused drift, covariance and time-alignment evidence. **P10:** calibrated algorithm or ML pipeline with held-out tests and latency. **P09:** **Nav2 OR MoveIt 2**, with fault/recovery evidence. **P11:** fuse the chosen path and prove repeatability, a bounded operating envelope and operator override. Do not use cloud/LLMs as safety controllers.

---

# STAGE 05 — OPTIONAL / AS-NEEDED MATHEMATICS (NO EXTRA SEQUENTIAL MONTHS)

**This is a topic-to-course lookup table, not a mandatory list of courses.** Return when an observed failure or a chosen graduate research question requires deeper theory; preserve the strict math gates in Stages 1–4.

| Stage 5 module | Trigger / project symptom | Named course / reference — exact URL | Small proof before returning to main stage |
|---|---|---|---|
| M01 Eigenanalysis / Laplace / Bode | P05 oscillation/stability question not explained by time response | [MIT OCW — 6.302 Feedback Systems](https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/) | Explain a measured/simulated instability and improvement. |
| M02 Pseudoinverse, SVD, conditioning | P03/P09 singular IK or bad calibration | [MIT OCW — 18.06SC Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | Plot conditioning and show damped solution vs naive inverse. |
| M03 SO(3), SE(3), screw theory | Custom 3D estimator/manipulator; **not** ordinary `tf2` use | [Modern Robotics — Course 1: Foundations of Robot Motion](https://www.coursera.org/learn/modernrobotics-course1) | Pose perturbation test with correct frames. |
| M04 State-space, controllability/observability, LQR | PID or sensor set has demonstrable limits | [MIT — Underactuated Robotics](https://underactuated.mit.edu/) | Compare constrained problem to tuned baseline. |
| M05 Particle filtering/factor graphs | P08/field localization genuinely needs richer estimation | [State Estimation and Localization for Self-Driving Cars](https://www.coursera.org/learn/state-estimation-localization-self-driving-cars) | Reproduce degraded-sensor failure and recovery; supplement course with papers for factor graphs. |
| M06 Nonlinear optimization/SLAM internals | Building a solver or research contribution rather than calling a library | [MIT — Underactuated Robotics](https://underactuated.mit.edu/) | Accuracy/runtime/failure benchmark with baseline. |
| M07 MPC, robust/adaptive/impedance control | P12 constrained motion/contact not solved by PID | [MIT — Underactuated Robotics](https://underactuated.mit.edu/) | Compared controller under repeated perturbations. |
| M08 Advanced rigid-body dynamics | High-speed manipulator or coupled inertia invalidates simple model | [Modern Robotics: Mechanics, Planning, and Control](https://www.coursera.org/specializations/modernrobotics) | Compare higher-fidelity model with measurements. |

**Caveat:** M05–M07 resources may introduce the theory but do not exhaustively teach every factor-graph, custom-SLAM, robust-control or MPC research technique. For those, use a paper/textbook chosen *after* the project exposes the need, and record its exact citation in the research log.

---

# STAGE 06 — SPECIALIZATION (MONTHS 23–36; SELECT ONE PRIMARY)

**Pick one domain at real W→P depth.** The others stay at E unless you extend the plan to roughly **40–48 months for two tracks**. P12 is your domain capstone; **P13 is required at W→P for the IoT/IIoT primary track**. There is no single course or universally recognized exam that makes someone a qualified industrial/defense robotics engineer.

## Track A — INDUSTRIAL ROBOTICS (P12-A)

| Subject | Actual course / guided series — exact URL | Use / evidence | Priority |
|---|---|---|---|
| PLC/HMI, ladder and TIA Portal | [Siemens SITRAIN — SIMATIC Programming 1 in the TIA Portal (TIA-PRO1)](https://www.sitrain-learning.siemens.com/en/product/chapter/QAJ7KOP/course/PAE0J7A/description.do) | Vendor foundation. Follow the simulation/lab exercises, create I/O list and fault state machine. Availability and language vary by region. | **Anchor if Siemens platform** |
| Overview: sensors, PLC, gripper, mechatronics | [Coursera — Fundamentals of Robotics & Industrial Automation](https://www.coursera.org/learn/fundamentals-of-robotics--industrial-automation) | Supplement vendor course with the system-level view. | Alternative |
| SCADA/MES/dashboards, tags/alarms | [Inductive University — Learn Ignition](https://inductiveautomation.com/resources/video/inductive-university) | Free guided video library and IU credential pathway for a *virtual* production dashboard. | **Anchor** |
| More intensive SCADA training | [Inductive Automation — Training Classes & Certification](https://inductiveautomation.com/training/classes-and-certification) | Optional paid vendor class/testing; **IU credential ≠ Ignition Core Certification**. | Optional |
| OT cybersecurity and zoning | [ISA — Using ISA/IEC 62443 Standards to Secure Your Control Systems (IC32)](https://www.isa.org/training/course-description/ic32) | Model zones/conduits and interface scope; not a substitute for qualified machine-safety assessment. | Optional specialization |
| Technical architecture / requirements | [UNSW / Coursera — Introduction to Systems Engineering](https://www.coursera.org/learn/systems-engineering) | Requirements, V&V and recovery matrix for P12-A. | Shared |

**Domain gates:** virtual robot-cell sequence → PLC/robot handshake and timeouts → traceable inspection → **P12-A** integrated simulated cell with cycle time and faults. Actual workcell access, guarding and safety-rated controls require qualified site supervision and authorization; a MOOC cannot certify a cell.

## Track B — RUGGED FIELD / DEFENSE-ADJACENT ROBOTICS (P12-B)

**The user-defined scope remains strictly non-weaponized:** logistics/resupply, inspection, remote sensing, search-and-rescue support, survey/hazard mapping; **no weapon integration, target selection or autonomous engagement**. The educational links here are systems-engineering, localization and geographic-information resources, *not* military accreditation or operational qualifications.

| Subject | Actual course / guided series — exact URL | Use / evidence | Priority |
|---|---|---|---|
| Requirements, interfaces, lifecycle and safety case thinking | [UNSW / Coursera — Introduction to Systems Engineering](https://www.coursera.org/learn/systems-engineering) | Write payload/endurance/comms requirements, FMEA method, acceptance matrix. | **Anchor** |
| Clear, verifiable requirements | [UNSW / Coursera — Requirements Writing](https://www.coursera.org/learn/requirements-writing) | Convert qualitative claims into measurable field requirements. | Supporting |
| GNSS/IMU/odometry degradation | [University of Toronto — State Estimation and Localization for Self-Driving Cars](https://www.coursera.org/learn/state-estimation-localization-self-driving-cars) | Simulate localization loss, confidence growth, local safe state and operator takeover; not tactical guidance. | **Anchor** |
| Geospatial inspection and survey maps | [UC Davis / Coursera — Geographic Information Systems (GIS) Specialization](https://www.coursera.org/specializations/gis) | Learn raster/vector workflows for permitted survey/hazard maps; choose relevant courses only. | **Anchor when GIS needed** |
| Field perception | [University of Toronto — Visual Perception for Self-Driving Cars](https://www.coursera.org/learn/visual-perception-self-driving-cars) | Test robustness to lighting, dust proxies/occlusion in a benign test environment. | Optional |
| Environmental/systems safety public-reference literacy | [DLA ASSIST — Official Standards Lookup](https://quicksearch.dla.mil/) | **Reference lookup, not a course**: locate current public MIL-STD-810 / 882 issue and distribution before reading. Do not claim qualification. | Reference only |

**P12-B:** one supervised/fully simulated benign inspection or cargo rover; repeatable GNSS-loss and comms-loss experiments, localization-confidence policy, fault log and field service plan. Any controlled project requires the organization’s authorization, information-security and export/legal processes; these courses grant none of them.

## Track C — IoT / IIoT ROBOTICS INTEGRATION (P13 + P12-C)

| Subject | Actual named course / guided series — exact URL | Use / evidence | Priority |
|---|---|---|---|
| Lightweight device messaging | [HiveMQ — MQTT Essentials](https://www.hivemq.com/mqtt/) | QoS, retain, sessions, last-will, topic/policy plan; **guided article/video series, not an exam**. | **Anchor** |
| Industrial IoT architecture | [University of Colorado Boulder / Coursera — Developing Industrial Internet of Things Specialization](https://www.coursera.org/specializations/developing-industrial-iot/) | Select networking/security/project material for chosen architecture. | Supporting |
| M2M / constrained-device protocols | [University of Colorado Boulder / Coursera — Embedded Interface Design Specialization](https://www.coursera.org/specializations/embedded-interface-design) | The M2M & IoT protocol course is relevant if your gateway needs constrained-device interfaces. | Optional |
| One vendor IoT platform (AWS path) | [AWS IoT Core — AWS IoT Tutorials](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials.html) | **Official guided tutorials**, not a course certificate: one device identity, topic policy, telemetry, shadow, Jobs/update planning. | **Choose AWS** |
| Choose a platform without guessing courses | [AWS — Learn More About AWS IoT (training-resource index)](https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-learn-more.html) | Start with the provider’s current list; do not infer that generic Cloud Practitioner teaches fleet security. | Reference |
| Low-cost self-hosted platform (alternative path) | [ThingsBoard — Getting Started](https://thingsboard.io/docs/getting-started/) | **Official step-by-step lab**, not a credential: devices, telemetry, dashboards and alarms. | **Choose ThingsBoard instead** |
| Digital twins, OTA, dashboards and identity | [ThingsBoard — User Guides](https://thingsboard.io/docs/user-guide/) | Follow the appropriate guides for your P13 feature set. | Reference |
| Plant-level SCADA/MES tie-in | [Inductive University — Learn Ignition](https://inductiveautomation.com/resources/video/inductive-university) | Bridge **selected non-critical** telemetry to modeled plant tags. | Optional industrial pairing |
| OT/IoT security | [ISA — Using ISA/IEC 62443 Standards to Secure Your Control Systems (IC32)](https://www.isa.org/training/course-description/ic32) | Add trust boundaries, least privilege, update change-control literacy. | Optional advanced |

**P13:** ≥3 uniquely identified robots (virtual identities allowed), telemetry schema and fleet dashboard, explicit broker/cloud outage behavior, staged update and rollback/abort evidence, key revocation and independent reproduction. **A robot's independent local stop/control must never depend on AWS, Azure, MQTT, a dashboard or other Internet services.** Learn only *one* IoT platform deeply during the main 36-month track.

---

# STAGE 07 — ONGOING PARALLEL HABITS (MONTH 1 → 36+)

**Continuous 2–3 hours per week from the existing study budget**, plus the monthly demo / roughly quarterly review cycle. No new P gate: this is the quality/reproducibility discipline for **P01–P13**.

| Stage 7 habit | Actual course / guided series — exact URL | Apply immediately |
|---|---|---|
| H1 Technical communication and scope | [Google for Developers — Technical Writing One](https://developers.google.com/tech-writing/one) | Clear README, limitations, requirements, short engineering note. Free self-study units; not a Google professional exam. |
| H1/H6 Git and visible portfolio | [GitHub Skills — Introduction to GitHub](https://github.com/skills/introduction-to-github) | Branch, PR, versioned code and project explanation. |
| H2 Continuous integration | [GitHub Skills — Hello GitHub Actions](https://github.com/skills/hello-github-actions) | One minimal build/test workflow. |
| H2 Automated tests and coverage | [GitHub Skills — Test with Actions](https://github.com/skills/test-with-actions) | Reproducible tests attached to stage gate. |
| H3/H4 Requirements, design reviews and V&V | [UNSW / Coursera — Introduction to Systems Engineering](https://www.coursera.org/learn/systems-engineering) | Requirements → test evidence → issue/review closure. |
| H4 Write testable requirements | [UNSW / Coursera — Requirements Writing](https://www.coursera.org/learn/requirements-writing) | Replace “works well” with a measurable operating envelope. |
| H6/H7 Continued source evaluation | [Google for Developers — Technical Writing Courses for Engineers](https://developers.google.com/tech-writing) | Improve presentations, changelogs, reviewer questions and project handoff. |

**Every 4 weeks:** demonstration + measurement + bug/failure + commit. **Every ~12 weeks:** second-person review of the *current gate*, action log and revised tests. **Monthly:** inspect costs, time, hardware safety and whether your chosen course is actually moving a gate. **When behind:** stop collecting tutorials/certificates; reduce optional depth and finish the smallest complete testable system.

---

# Course-selection rules, CV evidence and purchase discipline

## How many to study at once

| Period | Good parallel load | Avoid |
|---|---|---|
| M1–3 | One math/robotics anchor + one lightweight programming reference + P01–P03 work | Full CS50, full 18.06, full Modern Robotics, full CAD course simultaneously |
| M4–6 | One electronics/embedded anchor + one control reference + P04/P05 | Buying 3 MCUs and doing three embedded specializations |
| M7–14 | ROS 2 official tutorial ladder + specific C++/Gazebo references + P06/P07 | Mixing tutorials from incompatible Gazebo/ROS versions |
| M15–22 | One estimation anchor + one P10 vision route + **one** planner + P08–P11 | Mandatory ML and DL specializations for a geometry-only inspection task |
| M23–36 | **One** specialization anchor + project documentation/review | Three full specialization MOOCs and multiple capstones at once |
| Always | Documentation/testing and on-demand advanced math | Turning Stage 5 or Stage 7 into extra consecutive years |

## Certificate versus learning resource

- **Course/specialization completion:** e.g., Coursera's Andrew Ng **Machine Learning Specialization** or a verified edX track; list as a course certificate only **if earned**.
- **Publisher learning badge/credential:** e.g., Linux Foundation Introduction to Linux badge; label precisely as the issuer labels it.
- **Professional certification:** a separate assessed credential with its own requirements; do **not** claim it because you watched training videos. In particular, **Ignition IU Credential is not Ignition Core Certification** — Inductive Automation explicitly distinguishes them.
- **Official documentation / guided lab:** ROS 2, Gazebo, Nav2, MoveIt 2, AWS IoT Core, ThingsBoard; these are legitimate learning resources but are **not automatically issued certificates**.
- **Strongest accompanying CV artifact:** P05 response plots, P07 clean simulation, P08 uncertainty results, P11 integrated recovery, P12 one bounded domain capstone, and P13 only where IoT is primary or separately completed.

## Suggested study-record entry

```md
### Resource: [exact name](https://provider.example/course-page)
Stage and gate: 03 / P07
Why I selected it: ...
Only modules I need: ...
Date/version checked: ...
Evidence produced: [commit / test / plot / CAD / bag / schematic]
Main difference from course example: ...
Unverified claim or safety boundary: ...
Next gate unlocked: ...
```

**Final note:** Course pages and official tutorials were located via public provider/publisher search on **2026-09-24**. For Stage 6, particularly vendor training and defense-adjacent work, provider availability and jurisdictional requirements vary. A source link is a place to learn, not a guarantee of admission, certificate availability, professional competence, industrial commissioning authority, or military-program clearance.
