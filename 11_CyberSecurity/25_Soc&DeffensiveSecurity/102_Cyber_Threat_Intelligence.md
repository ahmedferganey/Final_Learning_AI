# 102. Cyber Threat Intelligence

> Phase 25 — SOC & Defensive Security

## 1. Topic Title

**Cyber Threat Intelligence**

## 2. Learning Objectives

- Explain the intelligence cycle and intelligence requirements.
- Differentiate strategic, operational, tactical, and technical intelligence.
- Evaluate sources, confidence, bias, recency, and relevance.
- Use indicators, ATT&CK, STIX/TAXII, and behavioral intelligence.
- Produce intelligence for SOC, hunting, engineering, and executives.

## 3. Prerequisites

```text
Cybersecurity Fundamentals
Network Security
Linux Administration
Windows Administration
Active Directory fundamentals
Cloud fundamentals
Phase 21 Network Security
Phase 22 Penetration Testing fundamentals
```

## 4. Core Concepts Explanation

# Part 1 — CTI Purpose

### Core Explanation

Cyber threat intelligence transforms threat information into contextual analysis that supports decisions.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 2 — Information vs Intelligence

### Core Explanation

Facts become intelligence only after analysis, context, relevance, and judgment.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 3 — Intelligence Requirement

### Core Explanation

Requirements define the decision or question that collection and analysis should support.

### Diagram / Command / Query Example

```text
Direction → Collection → Processing → Analysis → Dissemination → Feedback ↺
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 4 — Priority Intelligence Requirement

### Core Explanation

PIRs focus limited resources on the highest-priority threat questions.

### Diagram / Command / Query Example

```text
Direction → Collection → Processing → Analysis → Dissemination → Feedback ↺
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 5 — Intelligence Cycle

### Core Explanation

The cycle includes direction, collection, processing, analysis, dissemination, and feedback.

### Diagram / Command / Query Example

```text
Direction → Collection → Processing → Analysis → Dissemination → Feedback ↺
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 6 — Direction

### Core Explanation

Direction defines stakeholder need, scope, priority, and deadline.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 7 — Collection

### Core Explanation

Collection gathers relevant internal and external information.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 8 — Processing

### Core Explanation

Processing converts raw data into structured usable form.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 9 — Analysis

### Core Explanation

Analysis evaluates evidence, relationships, alternatives, confidence, and implications.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 10 — Dissemination

### Core Explanation

Dissemination delivers the right product to the right audience.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 11 — Feedback

### Core Explanation

Feedback determines whether the product answered the requirement.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 12 — Strategic Intelligence

### Core Explanation

Strategic intelligence supports leadership decisions about long-term risk and investment.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 13 — Operational Intelligence

### Core Explanation

Operational intelligence supports campaigns, incidents, and near-term planning.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 14 — Tactical Intelligence

### Core Explanation

Tactical intelligence focuses on adversary behavior, tools, techniques, and defensive implications.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 15 — Technical Intelligence

### Core Explanation

Technical intelligence includes indicators, malware, infrastructure, signatures, and technical artifacts.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 16 — Internal Intelligence

### Core Explanation

Incidents, detections, hunts, abuse, and exploitation provide organization-specific intelligence.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 17 — External Intelligence

### Core Explanation

Vendors, governments, ISACs, open sources, and trusted communities provide external context.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 18 — Source Reliability

### Core Explanation

Assess whether a source has a history of accurate and timely reporting.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 19 — Information Credibility

### Core Explanation

Assess whether a specific claim is corroborated by evidence.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 20 — Confidence

### Core Explanation

Confidence reflects source quality, corroboration, recency, and analytic consistency.

### Diagram / Command / Query Example

```text
confidence = source reliability + evidence quality + corroboration + recency + analytic consistency
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 21 — Uncertainty

### Core Explanation

Products should state important uncertainty rather than hide it.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 22 — Bias

### Core Explanation

Analysts should recognize confirmation, anchoring, availability, and source-selection bias.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 23 — Alternative Hypothesis

### Core Explanation

Consider plausible competing explanations before final judgments.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 24 — Recency

### Core Explanation

Hashes, infrastructure, behaviors, and strategic assessments age at different rates.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 25 — Relevance

### Core Explanation

Intelligence should map to technologies, regions, sectors, assets, or threat scenarios that matter.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 26 — Actionability

### Core Explanation

Useful intelligence supports a decision, detection, hunt, patch, block, or hardening action.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 27 — IOC

### Core Explanation

An indicator of compromise is an observable artifact associated with suspicious or malicious activity.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 28 — Indicator Context

### Core Explanation

Indicators need source, first/last seen, confidence, malware/campaign context, and intended use.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 29 — Indicator Lifetime

### Core Explanation

Infrastructure indicators can become stale quickly and need expiration logic.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 30 — False Positive IOC

### Core Explanation

Shared cloud, CDN, VPN, or hosting infrastructure can make raw blocklists dangerous.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 31 — Behavioral Indicator

### Core Explanation

Behavior-based intelligence can remain useful after hashes, domains, or IPs change.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 32 — Pyramid of Pain

### Core Explanation

The Pyramid of Pain illustrates that adversary TTPs are generally more expensive to change than hashes or IPs.

### Diagram / Command / Query Example

```text
Harder to change: TTPs → Tools → Host/Network Artifacts → Domains → IPs → Hashes : Easier
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 33 — TTPs

### Core Explanation

Tactics, techniques, and procedures describe adversary goals and behavior.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 34 — MITRE ATT&CK

### Core Explanation

ATT&CK provides a common vocabulary for tactics, techniques, and defensive knowledge.

### Diagram / Command / Query Example

```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 35 — ATT&CK Tactic

### Core Explanation

A tactic represents a high-level adversary objective.

### Diagram / Command / Query Example

```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 36 — ATT&CK Technique

### Core Explanation

A technique describes how an adversary achieves an objective.

### Diagram / Command / Query Example

```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 37 — ATT&CK Mapping Quality

### Core Explanation

Map only confirmed or well-supported behavior rather than forcing every observation into ATT&CK.

### Diagram / Command / Query Example

```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 38 — Campaign

### Core Explanation

A campaign groups related adversary activity over time.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 39 — Threat Actor

### Core Explanation

Threat actor labels represent groups or clusters attributed with varying confidence.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 40 — Attribution

### Core Explanation

Attribution is difficult and should distinguish technical similarity from confident identity claims.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 41 — Malware Family

### Core Explanation

A malware family groups related samples by code, configuration, or behavior.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 42 — Infrastructure

### Core Explanation

Domains, IPs, certificates, hosting, email, and accounts can reveal threat relationships.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 43 — Passive DNS

### Core Explanation

Passive DNS can reveal historical domain-to-IP relationships from legitimate datasets.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 44 — Certificate Transparency

### Core Explanation

Certificate logs can reveal infrastructure relationships and newly issued names.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 45 — Vulnerability Intelligence

### Core Explanation

Threat intelligence can prioritize vulnerabilities based on active exploitation and attacker interest.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 46 — Exploit Activity

### Core Explanation

Evidence of active exploitation increases urgency beyond technical severity alone.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 47 — CISA KEV Awareness

### Core Explanation

Known-exploited-vulnerability catalogs can inform remediation prioritization when applicable.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 48 — STIX

### Core Explanation

STIX models cyber threat entities and relationships in machine-readable form.

### Diagram / Command / Query Example

```json
{"type":"indicator","spec_version":"2.1","name":"Training Example","pattern_type":"stix","pattern":"[domain-name:value = 'example.invalid']"}
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 49 — TAXII

### Core Explanation

TAXII is a protocol for exchanging cyber threat intelligence collections.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 50 — STIX Indicator

### Core Explanation

STIX indicators encode detection patterns and related metadata.

### Diagram / Command / Query Example

```json
{"type":"indicator","spec_version":"2.1","name":"Training Example","pattern_type":"stix","pattern":"[domain-name:value = 'example.invalid']"}
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 51 — STIX Relationship

### Core Explanation

Relationships connect indicators, malware, campaigns, actors, vulnerabilities, and other objects.

### Diagram / Command / Query Example

```json
{"type":"indicator","spec_version":"2.1","name":"Training Example","pattern_type":"stix","pattern":"[domain-name:value = 'example.invalid']"}
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 52 — MISP Awareness

### Core Explanation

MISP supports collaborative threat-information and indicator management.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 53 — TIP Awareness

### Core Explanation

Threat Intelligence Platforms organize feeds, indicators, relationships, scoring, and sightings.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 54 — Feed Normalization

### Core Explanation

Feeds require deduplication, field mapping, scoring, and expiration logic.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 55 — Feed Quality

### Core Explanation

More indicators do not automatically create better intelligence.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 56 — IOC Scoring

### Core Explanation

Score indicators using source, confidence, age, sightings, specificity, and false-positive risk.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 57 — Indicator Expiration

### Core Explanation

Expire or downgrade indicators when evidence becomes stale.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 58 — Sightings

### Core Explanation

Internal sightings show whether external intelligence appears in organizational telemetry.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 59 — Retro Hunt

### Core Explanation

New intelligence can trigger searches across historical logs for prior activity.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 60 — Detection Support

### Core Explanation

CTI can provide behavioral hypotheses and test cases for detection engineers.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 61 — Hunting Support

### Core Explanation

CTI gives hunters likely behaviors, targets, infrastructure, and pivots.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 62 — Vulnerability Support

### Core Explanation

CTI can help prioritize patching using exploitation evidence and relevance.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 63 — Executive Support

### Core Explanation

Strategic CTI should explain business exposure, uncertainty, and recommended action.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 64 — Collection Plan

### Core Explanation

A collection plan maps requirements to sources, owners, and cadence.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 65 — Collection Gap

### Core Explanation

A gap identifies required information current sources cannot provide.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 66 — OSINT

### Core Explanation

Open-source intelligence uses publicly available data while respecting privacy and legal boundaries.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 67 — Commercial Feed

### Core Explanation

Paid feeds may provide curated malware, fraud, vulnerability, or infrastructure context.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 68 — Government Advisory

### Core Explanation

Government advisories may provide authoritative remediation and sector-level threat information.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 69 — ISAC / ISAO

### Core Explanation

Sector communities can provide industry-specific context and trusted sharing.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 70 — TLP

### Core Explanation

Traffic Light Protocol communicates sharing restrictions for intelligence.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 71 — Intelligence Product

### Core Explanation

A product should match audience, decision, evidence, confidence, and required action.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 72 — Executive Note

### Core Explanation

Executives need concise business impact, trend, confidence, and decisions.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 73 — SOC Note

### Core Explanation

SOC teams need observables, behavior, context, queries, and triage guidance.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 74 — Hunt Package

### Core Explanation

Hunters need hypotheses, ATT&CK mapping, data requirements, pivots, and expected benign patterns.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 75 — Engineering Advisory

### Core Explanation

Engineers need affected technology, mitigation, patch, hardening, and validation guidance.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 76 — Source Citation

### Core Explanation

Maintain source references so claims can be verified and updated.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 77 — Confidence Statement

### Core Explanation

Use explicit confidence language and rationale.

### Diagram / Command / Query Example

```text
confidence = source reliability + evidence quality + corroboration + recency + analytic consistency
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 78 — CTI Metrics

### Core Explanation

Measure requirement coverage, usefulness, timeliness, sightings, actions, and feedback rather than feed volume.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

# Part 79 — CTI Governance

### Core Explanation

Define source approval, sharing rules, retention, privacy, and partner handling.

### Diagram / Command / Query Example

```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

### Why It Matters

This topic contributes to defensive visibility, detection, investigation quality, response speed, or prevention of recurrence. A strong SOC does not merely collect alerts; it converts reliable evidence into decisions and feeds outcomes back into engineering.

### Practical Use

Apply the concept to synthetic telemetry, your own lab, or authorized organizational logs. Record scope, time range, data sources, assumptions, and expected result before querying.

### Common Problems

- Treating one alert or IOC as proof.
- Ignoring data quality, parsing, time, or ownership.
- Failing to distinguish confidence from severity.
- Closing cases without disposition or tuning.
- Keeping intelligence or hunt results that never produce action.

### Best Practice

Start from a question, collect the minimum necessary evidence, correlate independent sources, state confidence and limitations, and convert the result into response, detection, hardening, or a documented gap.

---

## 5. Hands-on Lab / Practical Exercises

## Lab 1 — CTI Purpose

### Objective
Practice **CTI Purpose** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 2 — Information vs Intelligence

### Objective
Practice **Information vs Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 3 — Intelligence Requirement

### Objective
Practice **Intelligence Requirement** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Direction → Collection → Processing → Analysis → Dissemination → Feedback ↺
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 4 — Priority Intelligence Requirement

### Objective
Practice **Priority Intelligence Requirement** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Direction → Collection → Processing → Analysis → Dissemination → Feedback ↺
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 5 — Intelligence Cycle

### Objective
Practice **Intelligence Cycle** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Direction → Collection → Processing → Analysis → Dissemination → Feedback ↺
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 6 — Direction

### Objective
Practice **Direction** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 7 — Collection

### Objective
Practice **Collection** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 8 — Processing

### Objective
Practice **Processing** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 9 — Analysis

### Objective
Practice **Analysis** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 10 — Dissemination

### Objective
Practice **Dissemination** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 11 — Feedback

### Objective
Practice **Feedback** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 12 — Strategic Intelligence

### Objective
Practice **Strategic Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 13 — Operational Intelligence

### Objective
Practice **Operational Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 14 — Tactical Intelligence

### Objective
Practice **Tactical Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 15 — Technical Intelligence

### Objective
Practice **Technical Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 16 — Internal Intelligence

### Objective
Practice **Internal Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 17 — External Intelligence

### Objective
Practice **External Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 18 — Source Reliability

### Objective
Practice **Source Reliability** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 19 — Information Credibility

### Objective
Practice **Information Credibility** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 20 — Confidence

### Objective
Practice **Confidence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
confidence = source reliability + evidence quality + corroboration + recency + analytic consistency
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 21 — Uncertainty

### Objective
Practice **Uncertainty** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 22 — Bias

### Objective
Practice **Bias** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 23 — Alternative Hypothesis

### Objective
Practice **Alternative Hypothesis** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 24 — Recency

### Objective
Practice **Recency** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 25 — Relevance

### Objective
Practice **Relevance** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 26 — Actionability

### Objective
Practice **Actionability** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 27 — IOC

### Objective
Practice **IOC** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 28 — Indicator Context

### Objective
Practice **Indicator Context** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 29 — Indicator Lifetime

### Objective
Practice **Indicator Lifetime** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 30 — False Positive IOC

### Objective
Practice **False Positive IOC** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 31 — Behavioral Indicator

### Objective
Practice **Behavioral Indicator** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 32 — Pyramid of Pain

### Objective
Practice **Pyramid of Pain** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Harder to change: TTPs → Tools → Host/Network Artifacts → Domains → IPs → Hashes : Easier
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 33 — TTPs

### Objective
Practice **TTPs** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 34 — MITRE ATT&CK

### Objective
Practice **MITRE ATT&CK** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 35 — ATT&CK Tactic

### Objective
Practice **ATT&CK Tactic** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 36 — ATT&CK Technique

### Objective
Practice **ATT&CK Technique** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 37 — ATT&CK Mapping Quality

### Objective
Practice **ATT&CK Mapping Quality** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Observed behavior → ATT&CK tactic → technique → detection / mitigation / hunt
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 38 — Campaign

### Objective
Practice **Campaign** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 39 — Threat Actor

### Objective
Practice **Threat Actor** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 40 — Attribution

### Objective
Practice **Attribution** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 41 — Malware Family

### Objective
Practice **Malware Family** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 42 — Infrastructure

### Objective
Practice **Infrastructure** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 43 — Passive DNS

### Objective
Practice **Passive DNS** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 44 — Certificate Transparency

### Objective
Practice **Certificate Transparency** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 45 — Vulnerability Intelligence

### Objective
Practice **Vulnerability Intelligence** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 46 — Exploit Activity

### Objective
Practice **Exploit Activity** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 47 — CISA KEV Awareness

### Objective
Practice **CISA KEV Awareness** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 48 — STIX

### Objective
Practice **STIX** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```json
{"type":"indicator","spec_version":"2.1","name":"Training Example","pattern_type":"stix","pattern":"[domain-name:value = 'example.invalid']"}
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 49 — TAXII

### Objective
Practice **TAXII** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 50 — STIX Indicator

### Objective
Practice **STIX Indicator** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```json
{"type":"indicator","spec_version":"2.1","name":"Training Example","pattern_type":"stix","pattern":"[domain-name:value = 'example.invalid']"}
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 51 — STIX Relationship

### Objective
Practice **STIX Relationship** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```json
{"type":"indicator","spec_version":"2.1","name":"Training Example","pattern_type":"stix","pattern":"[domain-name:value = 'example.invalid']"}
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 52 — MISP Awareness

### Objective
Practice **MISP Awareness** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 53 — TIP Awareness

### Objective
Practice **TIP Awareness** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 54 — Feed Normalization

### Objective
Practice **Feed Normalization** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## Lab 55 — Feed Quality

### Objective
Practice **Feed Quality** using defensive synthetic or authorized data.

### Procedure
1. Define the question.
2. Define time range and entities.
3. Identify required telemetry.
4. Run the minimum query or review.
5. Correlate at least one second source when possible.
6. Record evidence and confidence.
7. Decide disposition/action.
8. Document a tuning, detection, or data-quality improvement.
9. Replay or retest after the change.

### Starter Example
```text
Signal / Question → Context → Evidence → Correlation → Decision → Action → Feedback
```

```text
Question:
Scope:
Data sources:
Query/method:
Observations:
Evidence:
Confidence:
Disposition:
Action:
Improvement:
```

---

## 6. Mini Project

# Mini Project — Produce a CTI Package

Create three intelligence requirements for a synthetic cloud-focused phishing scenario. Evaluate five approved sources, assign confidence, map ATT&CK behaviors, create one STIX-style indicator, and produce an executive note, SOC note, hunt package, and engineering advisory.

### Required Deliverables

1. Scope / scenario
2. Data-source inventory
3. Workflow / architecture diagram
4. Queries / analysis methods
5. Evidence repository
6. Findings and confidence
7. Response or engineering actions
8. Detection improvements
9. Retest / replay evidence
10. Executive or operational summary

## 7. Recommended Resources

- MITRE ATT&CK — https://attack.mitre.org/
- OASIS STIX 2.1 — https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html
- OASIS TAXII 2.1 — https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html
- CISA Advisories — https://www.cisa.gov/news-events/cybersecurity-advisories
- FIRST TLP — https://www.first.org/tlp/

## 8. Certification Relevance

Relevant to cyber threat intelligence, threat hunting, SOC, vulnerability prioritization, detection engineering, and incident response.

## 9. Common Mistakes & Best Practices

### Common Mistakes
- Optimizing for alert volume instead of risk reduction.
- Ignoring missing or delayed telemetry.
- Building detections with no owner or test.
- Using threat feeds without context or expiration.
- Hunting randomly without a hypothesis.

### Best Practices
- Keep data-source health visible.
- Separate facts, inference, and hypotheses.
- Maintain repeatable playbooks.
- Version and test detections.
- Turn incidents and hunts into engineering improvements.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the key lesson from **CTI Purpose**?

**Short answer:** Cyber threat intelligence transforms threat information into contextual analysis that supports decisions.

### Q2. What is the key lesson from **Information vs Intelligence**?

**Short answer:** Facts become intelligence only after analysis, context, relevance, and judgment.

### Q3. What is the key lesson from **Intelligence Requirement**?

**Short answer:** Requirements define the decision or question that collection and analysis should support.

### Q4. What is the key lesson from **Priority Intelligence Requirement**?

**Short answer:** PIRs focus limited resources on the highest-priority threat questions.

### Q5. What is the key lesson from **Intelligence Cycle**?

**Short answer:** The cycle includes direction, collection, processing, analysis, dissemination, and feedback.

### Q6. What is the key lesson from **Direction**?

**Short answer:** Direction defines stakeholder need, scope, priority, and deadline.

### Q7. What is the key lesson from **Collection**?

**Short answer:** Collection gathers relevant internal and external information.

### Q8. What is the key lesson from **Processing**?

**Short answer:** Processing converts raw data into structured usable form.

### Q9. What is the key lesson from **Analysis**?

**Short answer:** Analysis evaluates evidence, relationships, alternatives, confidence, and implications.

### Q10. What is the key lesson from **Dissemination**?

**Short answer:** Dissemination delivers the right product to the right audience.

### Q11. What is the key lesson from **Feedback**?

**Short answer:** Feedback determines whether the product answered the requirement.

### Q12. What is the key lesson from **Strategic Intelligence**?

**Short answer:** Strategic intelligence supports leadership decisions about long-term risk and investment.

### Q13. What is the key lesson from **Operational Intelligence**?

**Short answer:** Operational intelligence supports campaigns, incidents, and near-term planning.

### Q14. What is the key lesson from **Tactical Intelligence**?

**Short answer:** Tactical intelligence focuses on adversary behavior, tools, techniques, and defensive implications.

### Q15. What is the key lesson from **Technical Intelligence**?

**Short answer:** Technical intelligence includes indicators, malware, infrastructure, signatures, and technical artifacts.

### Q16. What is the key lesson from **Internal Intelligence**?

**Short answer:** Incidents, detections, hunts, abuse, and exploitation provide organization-specific intelligence.

### Q17. What is the key lesson from **External Intelligence**?

**Short answer:** Vendors, governments, ISACs, open sources, and trusted communities provide external context.

### Q18. What is the key lesson from **Source Reliability**?

**Short answer:** Assess whether a source has a history of accurate and timely reporting.

### Q19. What is the key lesson from **Information Credibility**?

**Short answer:** Assess whether a specific claim is corroborated by evidence.

### Q20. What is the key lesson from **Confidence**?

**Short answer:** Confidence reflects source quality, corroboration, recency, and analytic consistency.

### Q21. What is the key lesson from **Uncertainty**?

**Short answer:** Products should state important uncertainty rather than hide it.

### Q22. What is the key lesson from **Bias**?

**Short answer:** Analysts should recognize confirmation, anchoring, availability, and source-selection bias.

### Q23. What is the key lesson from **Alternative Hypothesis**?

**Short answer:** Consider plausible competing explanations before final judgments.

### Q24. What is the key lesson from **Recency**?

**Short answer:** Hashes, infrastructure, behaviors, and strategic assessments age at different rates.

### Q25. What is the key lesson from **Relevance**?

**Short answer:** Intelligence should map to technologies, regions, sectors, assets, or threat scenarios that matter.

### Q26. What is the key lesson from **Actionability**?

**Short answer:** Useful intelligence supports a decision, detection, hunt, patch, block, or hardening action.

### Q27. What is the key lesson from **IOC**?

**Short answer:** An indicator of compromise is an observable artifact associated with suspicious or malicious activity.

### Q28. What is the key lesson from **Indicator Context**?

**Short answer:** Indicators need source, first/last seen, confidence, malware/campaign context, and intended use.

### Q29. What is the key lesson from **Indicator Lifetime**?

**Short answer:** Infrastructure indicators can become stale quickly and need expiration logic.

### Q30. What is the key lesson from **False Positive IOC**?

**Short answer:** Shared cloud, CDN, VPN, or hosting infrastructure can make raw blocklists dangerous.

### Q31. What is the key lesson from **Behavioral Indicator**?

**Short answer:** Behavior-based intelligence can remain useful after hashes, domains, or IPs change.

### Q32. What is the key lesson from **Pyramid of Pain**?

**Short answer:** The Pyramid of Pain illustrates that adversary TTPs are generally more expensive to change than hashes or IPs.

### Q33. What is the key lesson from **TTPs**?

**Short answer:** Tactics, techniques, and procedures describe adversary goals and behavior.

### Q34. What is the key lesson from **MITRE ATT&CK**?

**Short answer:** ATT&CK provides a common vocabulary for tactics, techniques, and defensive knowledge.

### Q35. What is the key lesson from **ATT&CK Tactic**?

**Short answer:** A tactic represents a high-level adversary objective.

### Q36. What is the key lesson from **ATT&CK Technique**?

**Short answer:** A technique describes how an adversary achieves an objective.

### Q37. What is the key lesson from **ATT&CK Mapping Quality**?

**Short answer:** Map only confirmed or well-supported behavior rather than forcing every observation into ATT&CK.

### Q38. What is the key lesson from **Campaign**?

**Short answer:** A campaign groups related adversary activity over time.

### Q39. What is the key lesson from **Threat Actor**?

**Short answer:** Threat actor labels represent groups or clusters attributed with varying confidence.

### Q40. What is the key lesson from **Attribution**?

**Short answer:** Attribution is difficult and should distinguish technical similarity from confident identity claims.

### Q41. What is the key lesson from **Malware Family**?

**Short answer:** A malware family groups related samples by code, configuration, or behavior.

### Q42. What is the key lesson from **Infrastructure**?

**Short answer:** Domains, IPs, certificates, hosting, email, and accounts can reveal threat relationships.

### Q43. What is the key lesson from **Passive DNS**?

**Short answer:** Passive DNS can reveal historical domain-to-IP relationships from legitimate datasets.

### Q44. What is the key lesson from **Certificate Transparency**?

**Short answer:** Certificate logs can reveal infrastructure relationships and newly issued names.

### Q45. What is the key lesson from **Vulnerability Intelligence**?

**Short answer:** Threat intelligence can prioritize vulnerabilities based on active exploitation and attacker interest.

### Q46. What is the key lesson from **Exploit Activity**?

**Short answer:** Evidence of active exploitation increases urgency beyond technical severity alone.

### Q47. What is the key lesson from **CISA KEV Awareness**?

**Short answer:** Known-exploited-vulnerability catalogs can inform remediation prioritization when applicable.

### Q48. What is the key lesson from **STIX**?

**Short answer:** STIX models cyber threat entities and relationships in machine-readable form.

### Q49. What is the key lesson from **TAXII**?

**Short answer:** TAXII is a protocol for exchanging cyber threat intelligence collections.

### Q50. What is the key lesson from **STIX Indicator**?

**Short answer:** STIX indicators encode detection patterns and related metadata.

### Q51. What is the key lesson from **STIX Relationship**?

**Short answer:** Relationships connect indicators, malware, campaigns, actors, vulnerabilities, and other objects.

### Q52. What is the key lesson from **MISP Awareness**?

**Short answer:** MISP supports collaborative threat-information and indicator management.

### Q53. What is the key lesson from **TIP Awareness**?

**Short answer:** Threat Intelligence Platforms organize feeds, indicators, relationships, scoring, and sightings.

### Q54. What is the key lesson from **Feed Normalization**?

**Short answer:** Feeds require deduplication, field mapping, scoring, and expiration logic.

### Q55. What is the key lesson from **Feed Quality**?

**Short answer:** More indicators do not automatically create better intelligence.

### Q56. What is the key lesson from **IOC Scoring**?

**Short answer:** Score indicators using source, confidence, age, sightings, specificity, and false-positive risk.

### Q57. What is the key lesson from **Indicator Expiration**?

**Short answer:** Expire or downgrade indicators when evidence becomes stale.

### Q58. What is the key lesson from **Sightings**?

**Short answer:** Internal sightings show whether external intelligence appears in organizational telemetry.

### Q59. What is the key lesson from **Retro Hunt**?

**Short answer:** New intelligence can trigger searches across historical logs for prior activity.

### Q60. What is the key lesson from **Detection Support**?

**Short answer:** CTI can provide behavioral hypotheses and test cases for detection engineers.

### Q61. What is the key lesson from **Hunting Support**?

**Short answer:** CTI gives hunters likely behaviors, targets, infrastructure, and pivots.

### Q62. What is the key lesson from **Vulnerability Support**?

**Short answer:** CTI can help prioritize patching using exploitation evidence and relevance.

### Q63. What is the key lesson from **Executive Support**?

**Short answer:** Strategic CTI should explain business exposure, uncertainty, and recommended action.

### Q64. What is the key lesson from **Collection Plan**?

**Short answer:** A collection plan maps requirements to sources, owners, and cadence.

### Q65. What is the key lesson from **Collection Gap**?

**Short answer:** A gap identifies required information current sources cannot provide.

### Q66. What is the key lesson from **OSINT**?

**Short answer:** Open-source intelligence uses publicly available data while respecting privacy and legal boundaries.

### Q67. What is the key lesson from **Commercial Feed**?

**Short answer:** Paid feeds may provide curated malware, fraud, vulnerability, or infrastructure context.

### Q68. What is the key lesson from **Government Advisory**?

**Short answer:** Government advisories may provide authoritative remediation and sector-level threat information.

### Q69. What is the key lesson from **ISAC / ISAO**?

**Short answer:** Sector communities can provide industry-specific context and trusted sharing.

### Q70. What is the key lesson from **TLP**?

**Short answer:** Traffic Light Protocol communicates sharing restrictions for intelligence.

### Q71. What is the key lesson from **Intelligence Product**?

**Short answer:** A product should match audience, decision, evidence, confidence, and required action.

### Q72. What is the key lesson from **Executive Note**?

**Short answer:** Executives need concise business impact, trend, confidence, and decisions.

### Q73. What is the key lesson from **SOC Note**?

**Short answer:** SOC teams need observables, behavior, context, queries, and triage guidance.

### Q74. What is the key lesson from **Hunt Package**?

**Short answer:** Hunters need hypotheses, ATT&CK mapping, data requirements, pivots, and expected benign patterns.

### Q75. What is the key lesson from **Engineering Advisory**?

**Short answer:** Engineers need affected technology, mitigation, patch, hardening, and validation guidance.

### Q76. What is the key lesson from **Source Citation**?

**Short answer:** Maintain source references so claims can be verified and updated.

### Q77. What is the key lesson from **Confidence Statement**?

**Short answer:** Use explicit confidence language and rationale.

### Q78. What is the key lesson from **CTI Metrics**?

**Short answer:** Measure requirement coverage, usefulness, timeliness, sightings, actions, and feedback rather than feed volume.

### Q79. What is the key lesson from **CTI Governance**?

**Short answer:** Define source approval, sharing rules, retention, privacy, and partner handling.

## Completion Checklist
- [ ] I completed at least 30 labs.
- [ ] I completed the mini project.
- [ ] I can identify required telemetry before querying.
- [ ] I can state confidence and limitations.
- [ ] I can convert analysis into defensive action.
