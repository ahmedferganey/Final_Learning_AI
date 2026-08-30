# Recommended Complete Study Order — AI-Powered Software Development / Agentic Software Engineering

This should be a **separate specialization layered on top of your existing software/cloud roadmap**, rather than repeating programming, Git, backend, testing, Docker, and DevOps.

The target is:

> **Software Engineer → AI-Powered Software Engineer → Agentic Software Engineer**

Not:

> Data Scientist → ML Researcher → LLM Researcher.

The emphasis is **using agents to engineer production software** and eventually designing the developer-agent systems themselves.

---

# Phase 1 — Generative AI for Software Engineers

Start with the minimum AI knowledge required to understand what your coding agent is doing.

1. **Generative AI Fundamentals**
2. **Large Language Model Fundamentals**
3. **Tokens, Context Windows and Inference**
4. **LLM Capabilities and Limitations**
5. **Hallucination and Uncertainty**
6. **Reasoning Models for Software Engineering**
7. **AI-Assisted vs Agentic Software Development**

You do **not** need deep neural-network mathematics, model training, PyTorch internals, or transformer research before continuing.

Dependency:

```text
Software Engineering
        ↓
Generative AI
        ↓
LLMs
        ↓
Agentic AI
```

---

# Phase 2 — Prompt Engineering for Software Development

Learn to communicate engineering intent precisely.

8. **Prompt Engineering Fundamentals**
9. **Software Engineering Prompt Patterns**
10. **Task Decomposition**
11. **Constraint-Based Prompting**
12. **Examples / Few-Shot Prompting**
13. **Structured Outputs**
14. **Iterative Prompt Refinement**
15. **Prompting for Code Generation**
16. **Prompting for Debugging**
17. **Prompting for Refactoring**
18. **Prompting for Code Review**

The important transition is:

```text
"Build me an API"
```

to:

```text
Goal
Constraints
Architecture boundaries
Acceptance criteria
Existing context
Tests
Definition of done
```

---

# Phase 3 — Context Engineering

This is more important for serious agentic development than simply learning more prompt tricks.

19. **Context Engineering Fundamentals**
20. **Repository Context**
21. **Instruction Hierarchy**
22. **Project-Level Agent Instructions**
23. **Just-in-Time Context Retrieval**
24. **Context Selection and Filtering**
25. **Context Compaction**
26. **Persistent Agent Notes / Memory**
27. **Long-Horizon Context Management**
28. **Sub-Agent Context Isolation**

Dependency:

```text
Prompt Engineering
       ↓
Context Engineering
       ↓
Reliable Agent Behavior
```

---

# Phase 4 — Agentic AI Fundamentals

Now study how an actual agent works.

29. **AI Agent Fundamentals**
30. **Agent Loop Architecture**
31. **Observe → Reason → Act → Observe**
32. **Tool Calling**
33. **Agent State**
34. **Planning**
35. **Task Execution**
36. **Reflection and Verification**
37. **Human-in-the-Loop Systems**
38. **Agent Permissions and Approval Gates**
39. **Agent Failure Recovery**

A useful mental model is:

```text
User Goal
   ↓
Agent
   ↓
Understand Context
   ↓
Create Plan
   ↓
Use Tool
   ↓
Observe Result
   ↓
Update Plan
   ↓
Repeat
   ↓
Verify Result
```

---

# Phase 5 — AI Coding Agent Mastery

Now use real software-engineering agents.

40. **CLI-Based Coding Agents**
41. **IDE-Based Coding Agents**
42. **Repository Navigation with Agents**
43. **Agent Plan Mode**
44. **Agent Execution Mode**
45. **File Creation and Modification**
46. **Terminal / Shell Tool Use**
47. **Git Operations with Agents**
48. **Test Execution**
49. **Diff Inspection**
50. **Agent Permissions**
51. **Sandboxed Execution**

Pick **one primary agent first**.

Recommended candidates:

```text
Codex
Claude Code
GitHub Copilot Coding Agent
```

Do not spend months learning five different interfaces. The transferable skill is supervising an **agentic engineering loop**.

---

# Phase 6 — Spec-Driven Development

This is one of the most important phases for agentic software engineering.

52. **Requirements Engineering with AI**
53. **Intent-Driven Development**
54. **Spec-Driven Development**
55. **Project Constitution**
56. **Feature Specifications**
57. **Requirements Clarification**
58. **Technical Planning**
59. **Task Decomposition**
60. **Acceptance Criteria**
61. **Cross-Artifact Analysis**
62. **Implementation from Specifications**
63. **Specification Convergence**
64. **Specification ↔ Implementation Drift**

The workflow is:

```text
Intent
  ↓
Specification
  ↓
Plan
  ↓
Tasks
  ↓
Implementation
```

rather than:

```text
Prompt
  ↓
Huge amount of generated code
  ↓
Hope it works
```

A Spec-Kit-style workflow:

```text
constitution
    ↓
specify
    ↓
clarify
    ↓
plan
    ↓
checklist
    ↓
tasks
    ↓
analyze
    ↓
implement
    ↓
converge
```

This should become your **default workflow for serious features**.

---

# Phase 7 — Agent-Friendly Repository Engineering

This is where the developer starts designing the environment for the agent instead of constantly correcting it.

65. **Agent-Friendly Repository Design**
66. **Repository Instruction Files**
67. **Architecture Documentation for Agents**
68. **Development Commands**
69. **Deterministic Build Environments**
70. **One-Command Testing**
71. **Automated Formatting and Linting**
72. **Strong Type Systems / Static Analysis**
73. **Machine-Readable Errors**
74. **Agent Skills and Reusable Instructions**
75. **Repository Guardrails**

Think:

```text
Agent capability
      +
Good repository structure
      +
Good tests
      +
Clear instructions
      +
Fast feedback
      =
Reliable agent
```

---

# Phase 8 — AI-Assisted Software Architecture

Do not let the agent make architecture decisions blindly.

76. **AI-Assisted Requirements Analysis**
77. **System Design with AI**
78. **Architecture Trade-Off Analysis**
79. **C4 Modeling**
80. **Architecture Decision Records**
81. **API Contract Design**
82. **Database Modeling**
83. **Domain Modeling**
84. **Non-Functional Requirements**
85. **Performance Requirements**
86. **Scalability Requirements**
87. **Security Requirements**

Workflow:

```text
Business Requirement
        ↓
Specification
        ↓
Architecture Alternatives
        ↓
Trade-off Analysis
        ↓
ADR
        ↓
Implementation Plan
```

You remain responsible for the engineering decision.

---

# Phase 9 — AI-Driven Implementation

Now use agents to perform actual production development.

88. **Vertical-Slice Development**
89. **Incremental Implementation**
90. **AI-Assisted TDD**
91. **Feature Implementation**
92. **Code Generation**
93. **Refactoring**
94. **Legacy Code Modernization**
95. **Dependency Migrations**
96. **Framework Upgrades**
97. **Database Migrations**
98. **Documentation Generation**

Prefer:

```text
Small specification
      ↓
Small implementation
      ↓
Tests
      ↓
Validation
      ↓
Commit
```

over giving an agent an entire application in one request.

---

# Phase 10 — AI Testing & Verification

This is absolutely critical.

99. **Unit Testing with AI**
100. **Integration Testing**
101. **API Testing**
102. **Contract Testing**
103. **End-to-End Testing**
104. **Property-Based Testing**
105. **Regression Testing**
106. **Static Analysis**
107. **Security Testing**
108. **Test Coverage Analysis**
109. **Agent-Generated Test Cases**
110. **Independent Verification Agents**

A powerful pattern is:

```text
Developer Agent
      ↓
Implementation

Tester Agent
      ↓
Independent tests

Reviewer Agent
      ↓
Review

CI
      ↓
Final deterministic verification
```

The agent saying:

> "Implementation completed successfully"

is **not evidence that the implementation is correct**.

Tests and deterministic validation are the evidence.

---

# Phase 11 — AI-Assisted Debugging & Code Review

111. **Bug Reproduction with Agents**
112. **Root-Cause Analysis**
113. **Log Analysis**
114. **Stack-Trace Analysis**
115. **Regression Detection**
116. **AI Code Review**
117. **Security Code Review**
118. **Performance Review**
119. **Architecture Review**
120. **PR Review Automation**
121. **Agent-Assisted Incident Investigation**

Ideal loop:

```text
Bug Report
   ↓
Reproduce
   ↓
Find Root Cause
   ↓
Create Failing Test
   ↓
Fix
   ↓
Regression Tests
   ↓
Review
```

not:

```text
Bug report
   ↓
Agent guesses
   ↓
Changes random code
```

---

# Phase 12 — Tool-Using Agents & MCP

Now move from an agent that only understands your repository to an agent that can interact with your engineering ecosystem.

122. **Function / Tool Calling**
123. **Tool Schema Design**
124. **Model Context Protocol Fundamentals**
125. **MCP Clients**
126. **MCP Servers**
127. **MCP Tools**
128. **MCP Resources**
129. **MCP Prompts**
130. **MCP Authentication and Authorization**
131. **MCP Tasks and Extensions**
132. **Building Custom MCP Servers**
133. **Securing MCP Integrations**

Example:

```text
Coding Agent
     │
     ├── GitHub
     ├── Jira / Linear
     ├── Documentation
     ├── Database
     ├── CI/CD
     ├── Monitoring
     └── Cloud Platform
           ↑
          MCP
```

---

# Phase 13 — Building Developer Agents

Up to this point you mostly **used** agents.

Now learn to **build them**.

134. **Agent SDK Fundamentals**
135. **Agent Runtime Architecture**
136. **Custom Tool Integration**
137. **Agent State Management**
138. **Memory**
139. **Task Planning**
140. **Agent Handoffs**
141. **Error Recovery**
142. **Agent Guardrails**
143. **Long-Running Agents**
144. **Agent Persistence**

Good technologies to learn here include:

```text
OpenAI Agents SDK
LangGraph
```

You don't need ten agent frameworks.

Learn the architecture first.

---

# Phase 14 — Multi-Agent Software Engineering

Now scale beyond a single coding agent.

145. **Multi-Agent Fundamentals**
146. **Supervisor-Agent Architecture**
147. **Planner Agent**
148. **Architecture Agent**
149. **Implementation Agent**
150. **Testing Agent**
151. **Reviewer Agent**
152. **Security Agent**
153. **Documentation Agent**
154. **Agent Handoffs**
155. **Parallel Execution**
156. **Worktree / Branch Isolation**
157. **Merge Coordination**
158. **Conflict Resolution**

Example:

```text
                 Orchestrator
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
 Architecture      Backend        Frontend
    Agent           Agent           Agent
       │              │              │
       └──────────────┼──────────────┘
                      ↓
                 Testing Agent
                      ↓
                 Review Agent
                      ↓
                     PR
```

---

# Phase 15 — Agentic CI/CD & SDLC Automation

Now connect agents to the full engineering lifecycle.

159. **AI-Augmented CI/CD**
160. **Issue → Agent Workflow**
161. **Issue → Specification**
162. **Specification → Implementation**
163. **Automated Test Generation**
164. **Automated PR Generation**
165. **AI PR Review**
166. **Automated Documentation**
167. **Dependency Upgrade Agents**
168. **Release Note Generation**
169. **CI Failure Diagnosis**
170. **Deployment Verification**
171. **Incident Triage Agents**

Eventually:

```text
Issue
  ↓
Agent analyzes
  ↓
Specification
  ↓
Plan
  ↓
Tasks
  ↓
Implementation
  ↓
Tests
  ↓
PR
  ↓
Review Agents
  ↓
Human Approval
  ↓
CI/CD
  ↓
Production
  ↓
Monitoring
  ↓
Feedback
```

---

# Phase 16 — Agent Evaluation & Observability

Traditional tests are necessary, but they are not enough when you build reusable agents.

172. **Agent Evaluation Fundamentals**
173. **Golden Task Sets**
174. **Task Success Rate**
175. **Regression Evals**
176. **Tool-Call Evaluation**
177. **Agent Trajectory Evaluation**
178. **LLM-as-Judge**
179. **Human Evaluation**
180. **Latency Measurement**
181. **Token / Cost Measurement**
182. **Agent Tracing**
183. **Failure Classification**
184. **Continuous Agent Evaluation**

Think:

```text
Software Tests
       +
Agent Evals
       +
Telemetry
       =
Production Confidence
```

---

# Phase 17 — Security for Agentic Software Development

Do not leave this as an optional subject.

185. **Prompt Injection**
186. **Indirect Prompt Injection**
187. **Malicious Repository Content**
188. **Secret Management**
189. **Least-Privilege Agent Access**
190. **Sandboxing**
191. **Filesystem Permissions**
192. **Network Egress Controls**
193. **Command Execution Controls**
194. **Human Approval Gates**
195. **MCP Security**
196. **Tool Authorization**
197. **Supply-Chain Security**
198. **Audit Logging**
199. **Agent Activity Tracing**
200. **Secure Autonomous Execution**

The security model should be:

```text
Agent
 ↓
Sandbox
 ↓
Least Privilege
 ↓
Approved Tools
 ↓
Restricted Secrets
 ↓
Controlled Network
 ↓
Audit Trail
 ↓
Human Approval for High-Risk Actions
```

---

# Phase 18 — Production Agentic Software Engineering

This is the final integration phase.

201. **Agentic SDLC Architecture**
202. **Agent Control Planes**
203. **Agent Job Queues**
204. **Long-Running Software Tasks**
205. **Parallel Agent Fleets**
206. **Agent Checkpointing**
207. **Failure Recovery**
208. **Human Escalation**
209. **Production Governance**
210. **Cost / Quality Optimization**
211. **Agent Reliability Engineering**
212. **Enterprise Agentic Development**

At this point your job starts shifting from:

```text
Write every line of code
```

toward:

```text
Define intent
     ↓
Design architecture
     ↓
Create specifications
     ↓
Engineer context
     ↓
Delegate execution
     ↓
Evaluate results
     ↓
Review critical decisions
     ↓
Improve the engineering harness
```

---

# Phase 19 — Portfolio Projects

Do **not** finish the roadmap with tutorials.

Build these progressively.

## Project 1 — AI-Assisted Feature Development

Take an existing backend application and use an agent to:

```text
Requirement
→ Plan
→ Code
→ Unit Tests
→ Integration Tests
→ Documentation
→ PR
```

---

## Project 2 — Spec-Driven Full-Stack Application

Use:

```text
Spec Kit
+
Coding Agent
+
Git
+
Automated Tests
+
Docker
+
CI/CD
```

Workflow:

```text
constitution
→ specify
→ clarify
→ plan
→ checklist
→ tasks
→ analyze
→ implement
→ converge
```

---

## Project 3 — AI Bug-Fixing Engineer

Build a developer agent that receives:

```text
GitHub Issue
```

and automatically:

```text
Reads issue
↓
Investigates repo
↓
Reproduces bug
↓
Writes failing test
↓
Implements fix
↓
Runs regression suite
↓
Creates proposed PR
```

Human approves the final PR.

---

## Project 4 — MCP Developer Workspace

Build MCP integrations for:

```text
GitHub
Documentation
Database
Issue Tracker
CI/CD
```

Then allow your development agent to use those tools.

---

## Project 5 — Multi-Agent Software Engineering System

Build:

```text
Project Manager Agent
        ↓
Planner Agent
        ↓
┌──────────────┬───────────────┐
Backend Agent  Frontend Agent
└──────────────┴───────────────┘
        ↓
Test Agent
        ↓
Security Agent
        ↓
Code Review Agent
        ↓
Human Approval
        ↓
PR
```

This should be the major portfolio project.

---

# Complete Dependency Map

Your entire specialization can be reduced to:

```text
Existing Software Engineering Foundations
                ↓
Generative AI for Developers
                ↓
LLM Fundamentals
                ↓
Prompt Engineering
                ↓
Context Engineering
                ↓
Agentic AI Fundamentals
                ↓
Coding Agent Mastery
                ↓
Spec-Driven Development
                ↓
Agent-Friendly Repositories
                ↓
AI-Assisted Architecture
                ↓
AI-Driven Implementation
                ↓
AI Testing & Verification
                ↓
AI Debugging & Code Review
                ↓
Tool Calling
                ↓
MCP
                ↓
Custom Developer Agents
                ↓
Multi-Agent Engineering
                ↓
Agentic CI/CD
                ↓
Agent Evals & Observability
                ↓
Agent Security
                ↓
Production Agentic SDLC
```

---

# What NOT to Put in This Track

To keep this specialization focused, exclude these from the main sequence:

```text
❌ Deep ML mathematics
❌ Classical ML algorithms
❌ Computer Vision
❌ CNNs
❌ Model training from scratch
❌ Distributed GPU training
❌ CUDA programming
❌ Deep transformer mathematics
❌ Data Science
❌ Data Analytics
❌ MLOps for model-training pipelines
```

Make these **optional**:

```text
△ Fine-tuning
△ Embedding-model internals
△ Advanced RAG
△ Vector database engineering
△ LLM serving
△ Model quantization
```

Those belong more strongly to an **AI Engineer / ML Engineer** track.

For **AI-Powered Software Development**, the high-value areas are:

```text
1. Software Engineering
2. Coding Agents
3. Context Engineering
4. Spec-Driven Development
5. Testing & Verification
6. Agent-Friendly Repositories
7. MCP / Tool Integration
8. Multi-Agent Engineering
9. CI/CD Automation
10. Agent Security & Evals
```

---

# The 10 Subjects to Start With First

1. **Generative AI for Software Engineers**
2. **LLM Fundamentals**
3. **Prompt Engineering for Software Development**
4. **Context Engineering**
5. **Agentic AI Fundamentals**
6. **Coding Agent Mastery**
7. **Spec-Driven Development**
8. **AI-Assisted Testing & Verification**
9. **MCP Fundamentals**
10. **Multi-Agent Software Engineering**

Then continue into:

```text
Agentic CI/CD
→ Agent Evals
→ Security
→ Production Agent Orchestration
```

This track is specifically designed for becoming an **AI-Powered / Agentic Software Engineer**, while the original software, cloud, and DevOps roadmap remains the underlying engineering foundation.
