# Prerequisites for AI-Powered Software Development

This roadmap contains **only the prerequisite knowledge that directly supports AI-Powered Software Development / Agentic Software Engineering**.

It intentionally excludes infrastructure-heavy and cybersecurity-specialist material that is not required before starting the agentic software development track.

The overall dependency is:

```text
Computer + Programming Fundamentals
        ↓
Software Engineering + Git
        ↓
Web + Database + Linux Basics
        ↓
Backend + APIs
        ↓
Testing + CI/CD
        ↓
Docker + Cloud Fundamentals
        ↓
Cloud-Native Development
        ↓
AI-Powered Software Development
        ↓
Agentic Software Engineering
```

---

# Phase 1 — Core Computer & Software Foundations

Learn the minimum computer-science vocabulary required to understand modern software systems.

1. **Operating Systems Fundamentals**
2. **Computer Networks Fundamentals**
3. **Introduction to Programming**
4. **Database Fundamentals**
5. **Introduction to Software Engineering**

You do **not** need advanced networking or system administration at this stage.

Dependency:

```text
Computer Fundamentals
        ↓
Programming
        ↓
Software Engineering
```

---

# Phase 2 — Programming Foundations

This is the most important prerequisite phase.

6. **Python Programming Fundamentals**
7. **Object-Oriented Programming Fundamentals**
8. **Data Structures and Algorithms**
9. **Bash / Shell Scripting Fundamentals**
10. **JavaScript / TypeScript Fundamentals**

Recommended order:

```text
Programming Fundamentals
        ↓
Python
        ↓
OOP
        ↓
Data Structures & Algorithms
        ↓
Bash
        ↓
JavaScript / TypeScript
```

## Why these matter

- **Python** — AI APIs, automation, backend systems, agents, SDKs, tooling.
- **OOP** — application architecture and maintainable software.
- **DSA** — problem solving and understanding generated code.
- **Bash** — coding agents frequently interact with terminals and development environments.
- **JavaScript / TypeScript** — modern full-stack and web application development.

You do **not** need C/C++ as a prerequisite for this specialization unless you want systems programming.

---

# Phase 3 — Git & Collaborative Development

AI coding agents operate heavily around repositories, branches, commits, diffs, and pull requests.

11. **Git Fundamentals**
12. **GitHub / GitLab Workflow**
13. **Branching and Merging**
14. **Pull Requests**
15. **Code Review Fundamentals**
16. **Merge Conflict Resolution**
17. **Semantic Commit Practices**

Dependency:

```text
Programming
    ↓
Git
    ↓
Branches
    ↓
Pull Requests
    ↓
Code Review
```

You should be comfortable reading a diff before allowing an AI agent to modify a production repository.

---

# Phase 4 — Linux & Developer Environment Fundamentals

You do **not** need full Linux administration.

Learn only what is useful for development and agent-based workflows.

18. **Linux Essentials**
19. **Filesystem and Permissions**
20. **Processes and Environment Variables**
21. **Package Management**
22. **Shell Commands**
23. **Bash Automation**
24. **SSH Fundamentals**

Recommended level:

```text
Linux user/developer
```

Not:

```text
Linux enterprise administrator
```

Topics such as RHCSA III, HA clustering, enterprise server administration, and advanced infrastructure management are **not prerequisites** for AI-powered software development.

---

# Phase 5 — Web Fundamentals

You need enough web knowledge to understand the applications that agents will help you build.

25. **How the Web Works**
26. **HTTP / HTTPS Fundamentals**
27. **Client–Server Architecture**
28. **HTML Fundamentals**
29. **CSS Fundamentals**
30. **JavaScript / TypeScript for Web Development**
31. **JSON**
32. **Browser and Server Communication**

Focus especially on:

```text
HTTP
APIs
JSON
Client ↔ Server
Authentication basics
```

---

# Phase 6 — Database Foundations

AI-powered applications frequently need persistent state, user data, agent state, logs, and application data.

33. **Relational Database Fundamentals**
34. **SQL**
35. **PostgreSQL Fundamentals**
36. **Database Modeling**
37. **Primary / Foreign Keys**
38. **Indexes**
39. **Transactions**
40. **Basic NoSQL Concepts**
41. **Database Migrations**

Recommended primary database:

```text
PostgreSQL
```

You do **not** need Oracle DBA I/II or enterprise database administration as prerequisites.

---

# Phase 7 — Backend Development

This is a critical prerequisite for serious AI-powered software development.

42. **Backend Development Fundamentals**
43. **Python Backend Development**
44. **FastAPI**
45. **Request / Response Lifecycle**
46. **Dependency Injection Fundamentals**
47. **Configuration Management**
48. **Environment Variables**
49. **Logging**
50. **Error Handling**
51. **Async Programming Fundamentals**
52. **Background Tasks**

Recommended core stack:

```text
Python
+
FastAPI
+
Pydantic
+
SQLAlchemy
+
PostgreSQL
```

Node.js can be studied as an alternative or secondary backend environment.

---

# Phase 8 — APIs & Integration

Agents are fundamentally tool-using software systems, so API knowledge is essential.

53. **Web Services Fundamentals**
54. **REST API Development**
55. **HTTP Methods and Status Codes**
56. **Request Validation**
57. **API Authentication**
58. **JWT Fundamentals**
59. **OAuth Fundamentals**
60. **API Versioning**
61. **API Documentation / OpenAPI**
62. **Webhooks Fundamentals**
63. **External API Integration**
64. **Rate Limiting and Retry Fundamentals**

Dependency:

```text
Backend
   ↓
HTTP
   ↓
REST APIs
   ↓
Authentication
   ↓
External Integrations
```

This phase becomes especially important later when you study:

```text
LLM APIs
Tool Calling
MCP
Agent Tools
```

---

# Phase 9 — Software Architecture & System Design Foundations

You do not need to become a distributed-systems expert first, but you must understand basic architecture.

65. **Clean Code Fundamentals**
66. **SOLID Principles**
67. **Separation of Concerns**
68. **Layered Architecture**
69. **Modular Architecture**
70. **Dependency Management**
71. **Design Patterns Fundamentals**
72. **Domain Modeling Fundamentals**
73. **API-First Design**
74. **Architecture Decision Records**
75. **Basic System Design**
76. **Monolith vs Microservices**
77. **Caching Fundamentals**
78. **Message Queue Fundamentals**

Focus on being able to judge whether AI-generated architecture is sensible.

---

# Phase 10 — Testing & Software Quality

This is mandatory before relying heavily on coding agents.

79. **Unit Testing**
80. **Integration Testing**
81. **API Testing**
82. **End-to-End Testing Fundamentals**
83. **Test-Driven Development Fundamentals**
84. **Mocking**
85. **Test Fixtures**
86. **Regression Testing**
87. **Code Coverage**
88. **Static Analysis**
89. **Linting**
90. **Formatting**
91. **Type Checking**

Recommended Python tools:

```text
pytest
ruff
mypy / pyright
```

The key principle is:

```text
AI-generated code
        ↓
Automated verification
        ↓
Human review
```

not:

```text
AI-generated code
        ↓
Trust it
```

---

# Phase 11 — Containers

You need enough container knowledge to create reproducible development and execution environments for both applications and coding agents.

92. **Container Fundamentals**
93. **Docker Fundamentals**
94. **Docker Images**
95. **Dockerfiles**
96. **Containers**
97. **Volumes**
98. **Networks**
99. **Environment Variables**
100. **Docker Compose**
101. **Multi-Stage Builds**
102. **Containerized Application Development**

Dependency:

```text
Linux
  ↓
Application
  ↓
Docker
  ↓
Docker Compose
```

You do **not** need OpenShift as a prerequisite.

---

# Phase 12 — Cloud Fundamentals

For this track, cloud knowledge should be developer-focused rather than infrastructure-specialist.

103. **Cloud Computing Fundamentals**
104. **IaaS / PaaS / SaaS**
105. **Compute**
106. **Storage**
107. **Managed Databases**
108. **Networking Basics**
109. **IAM Fundamentals**
110. **Secrets Management**
111. **Application Deployment**
112. **Logging and Monitoring**
113. **Serverless Fundamentals**

Choose **one cloud platform first**:

```text
AWS
or
Azure
or
GCP
```

You do not need to master all three before beginning AI-powered development.

Recommended depth:

```text
Cloud application developer
```

rather than:

```text
Cloud infrastructure administrator
```

---

# Phase 13 — Infrastructure as Code Fundamentals

Only basic IaC knowledge is required.

114. **Infrastructure as Code Fundamentals**
115. **Terraform Fundamentals**
116. **Variables and Outputs**
117. **Providers and Resources**
118. **Terraform State Fundamentals**
119. **Environment Configuration**

Learn enough to understand how an AI agent may provision or modify infrastructure safely.

Deep Terraform administration is optional at this stage.

---

# Phase 14 — CI/CD & DevOps Fundamentals

Agentic development becomes much safer when every generated change passes deterministic automation.

120. **DevOps Fundamentals**
121. **Continuous Integration**
122. **Continuous Delivery**
123. **Build Pipelines**
124. **Automated Testing in CI**
125. **Linting in CI**
126. **Static Analysis in CI**
127. **Docker Build Automation**
128. **Environment Management**
129. **Deployment Fundamentals**
130. **Rollback Fundamentals**
131. **GitHub Actions / Equivalent CI Platform**

Core workflow:

```text
Developer / Agent
       ↓
Git Push
       ↓
CI
       ↓
Lint
       ↓
Type Check
       ↓
Tests
       ↓
Build
       ↓
Deploy
```

---

# Phase 15 — Cloud-Native Application Fundamentals

Only study the application-development side required for modern production software.

132. **Cloud-Native Application Development**
133. **Stateless Application Design**
134. **12-Factor Application Principles**
135. **Containerized Application Deployment**
136. **Application Configuration**
137. **Health Checks**
138. **Observability Fundamentals**
139. **Structured Logging**
140. **Metrics Fundamentals**
141. **Distributed Application Basics**

---

# Phase 16 — Kubernetes Fundamentals — Optional but Valuable

Kubernetes is **useful**, particularly for production AI systems, but it does not need to block your entry into agentic software development.

142. **Kubernetes Fundamentals**
143. **Pods**
144. **Deployments**
145. **Services**
146. **ConfigMaps**
147. **Secrets**
148. **Basic Application Deployment**
149. **Health Probes**
150. **Basic Scaling**

Recommended level:

```text
Deploy applications to Kubernetes
```

You do not initially need:

```text
Advanced Kubernetes Administration
Cluster internals
OpenShift administration
```

---

# Phase 17 — Security Fundamentals for Developers

You need development security, not a full cybersecurity specialization.

151. **Secure Software Development Fundamentals**
152. **Authentication vs Authorization**
153. **Secrets Management**
154. **Environment Variable Security**
155. **OWASP Fundamentals**
156. **Dependency Security**
157. **Input Validation**
158. **API Security Fundamentals**
159. **Least Privilege**
160. **Secure Logging**
161. **Supply-Chain Security Fundamentals**

These concepts become especially important later when coding agents gain:

```text
Filesystem access
Terminal access
Git access
Cloud access
Database access
MCP tools
```

---

# Prerequisite Dependency Map

```text
1. Computer Fundamentals
        ↓
2. Python + OOP + DSA
        ↓
3. Git
        ↓
4. Linux + Bash
        ↓
5. Web Fundamentals
        ↓
6. SQL + PostgreSQL
        ↓
7. Backend Development
        ↓
8. REST APIs + Integrations
        ↓
9. Software Architecture Fundamentals
        ↓
10. Automated Testing
        ↓
11. Docker
        ↓
12. Cloud Fundamentals
        ↓
13. Basic Terraform
        ↓
14. CI/CD
        ↓
15. Cloud-Native Development
        ↓
16. Kubernetes Fundamentals [Optional]
        ↓
17. Developer Security Fundamentals
        ↓
AI-Powered Software Development
        ↓
Agentic Software Engineering
```


---

# Minimum Prerequisites Before Starting the AI Track

You **do not need to finish every phase above** before touching agentic AI.

The minimum recommended foundation is:

1. **Python**
2. **OOP**
3. **Basic Data Structures & Algorithms**
4. **Git & GitHub**
5. **Linux / Bash Fundamentals**
6. **HTTP / Web Fundamentals**
7. **SQL + PostgreSQL**
8. **Backend Development**
9. **REST APIs**
10. **Software Architecture Fundamentals**
11. **Unit + Integration Testing**
12. **Docker**
13. **Basic CI/CD**

At that point, you can begin:

```text
Generative AI for Software Engineers
        ↓
LLM Fundamentals
        ↓
Prompt Engineering
        ↓
Context Engineering
        ↓
Agentic AI Fundamentals
        ↓
Coding Agents
        ↓
Spec-Driven Development
```

Then learn **cloud, Terraform, Kubernetes, and advanced deployment topics in parallel** as your projects require them.

---

# Final Recommended Boundary

## Required Before / Early in the AI Track

```text
Python
OOP
DSA fundamentals
Git
Linux/Bash
Web/HTTP
SQL/PostgreSQL
Backend
REST APIs
Software Architecture
Testing
Docker
CI/CD
```

## Learn Alongside the AI Track

```text
Cloud Fundamentals
Terraform Fundamentals
Cloud-Native Development
Kubernetes Fundamentals
Developer Security
Observability
Message Queues
Microservices
```


This keeps the prerequisite roadmap focused on becoming an **AI-Powered Software Engineer**, rather than accidentally turning it into a full Cloud Engineer, DevOps Engineer, Network Engineer, or Systems Administrator curriculum.



# If you want only the minimum files before starting AI

```plaintext

1  - Operating Systems Fundamentals
2  - Computer Networks Fundamentals
3  - Introduction to Programming
4  - Database Fundamentals
5  - Introduction to Software Engineering

8  - Python Programming Fundamentals
10 - Object-Oriented Programming Fundamentals
11 - Data Structures and Algorithms
12 - Bash Shell Scripting

13 - HTML5 and CSS3
14 - Client-Side Technologies
15 - Web Fundamentals

20 - Linux Essentials

28 - MySQL Database

45 - Git and Version Control Systems

57 - Application Containers
58 - Docker Fundamentals

65 - DevOps Concepts and Toolchain
66 - Continuous Integration
67 - Continuous Delivery
68 - CI/CD Automation, Integration and Testing
69 - Unit and Automated Testing

70 - Backend Development Fundamentals
72 - Web Services and APIs
73 - REST API Development

75 - Microservices Architecture
76 - Enterprise Application Architecture and Integration

```

# Learn alongside AI rather than waiting to finish them

```plaintext
48 - Cloud Computing Fundamentals
49 - AWS Cloud Practitioner
50 - Microsoft Azure Fundamentals
51 - GCP Fundamentals

59 - Kubernetes Fundamentals
60 - Kubernetes Administration

62 - Infrastructure as Code Fundamentals
63 - Terraform
64 - Terraform Remote State Management

74 - Message Queuing
75 - Microservices Architecture

77 - Cloud-Native Application Development
78 - Containerized Application Deployment
79 - Kubernetes Application Deployment
80 - Cloud Application Architecture
```