# Recommended Complete Study Order

## Phase 1 — Computer & IT Foundations

Start here before Linux, cloud, DevOps, or cybersecurity.

1. **Operating Systems Fundamentals** 
2. **Computer Networks Fundamentals** 
3. **Introduction to Programming** 
4. **Database Fundamentals** 
5. **Introduction to Software Engineering** 
6. **Cloud Computing and Virtualization Foundations** 
7. **Introduction to Cybersecurity** 

These give you the vocabulary required by almost everything later.

---

# Phase 2 — Programming Foundations

Do these before backend development, automation, DevOps scripting, security scripting, APIs, etc.

8. **Python Programming Fundamentals** 
9. **C Programming Fundamentals** 
10. **Object-Oriented Programming Fundamentals** 
11. **Data Structures and Algorithms** 
12. **Bash Shell Scripting** 

Suggested dependency:

**Programming Fundamentals**
 ↓
 **Python / C**
 ↓
 **OOP**
 ↓
 **Data Structures & Algorithms**
 ↓
 **Bash / automation**

The unified track explicitly includes Python, C/OOP fundamentals, DSA and Bash in its fundamental curriculum. 

---

# Phase 3 — Web Foundations

Before backend, APIs, application security and web penetration testing:

13. **HTML5 and CSS3** 
14. **Client-Side Technologies** 
15. **Web Fundamentals** 

The PDF doesn't explicitly list a standalone **JavaScript Fundamentals** course, even though it later includes Node.js. So don't treat JavaScript as an official additional course from this PDF; when searching for a Node.js course later, choose one that covers the JavaScript prerequisites if you don't already know them.

---

# Phase 4 — Networking

This is one of the most important dependency chains in the entire track.

16. **Cisco Network Associate** 
17. **Cisco Internetworking** 
18. **Advanced Routing Design and Implementation** 
19. **Advanced Switching Design and Implementation** 

Think of the progression as:

**Computer Networks Fundamentals**
 → **CCNA-level Networking**
 → **Internetworking**
 → **Advanced Routing**
 → **Advanced Switching**

The unified curriculum groups these under **Networking & Enterprise Infrastructure**. 

When searching, a very practical search term for #16 is:

**CCNA 200-301 Complete Course**

---

# Phase 5 — Linux System Administration

Now move deeply into Linux.

20. **Linux Essentials** 
21. **Red Hat System Administration I** 
22. **Red Hat System Administration II** 
23. **Red Hat System Administration III** 
24. **Linux Web Server Administration** 
25. **Red Hat High Availability Clustering** 

Dependency:

**Operating Systems Fundamentals**
 ↓
 **Linux Essentials**
 ↓
 **RHCSA / RH124-style Administration I**
 ↓
 **Administration II**
 ↓
 **Administration III**
 ↓
 **Web Server Administration / HA Clustering**

The unified PDF specifically calls out Red Hat System Administration I–III, web server administration, and HA clustering. 

---

# Phase 6 — Windows Enterprise Administration

Do this after OS and networking fundamentals.

26. **Microsoft Windows Server Infrastructure** 
27. **Microsoft Active Directory Administration** 

Study:

**Windows Server Infrastructure**
 → **Active Directory**

For searching, good course names would be:

- `Windows Server Administration` 
- `Windows Server Active Directory Administration` 

These correspond to the PDF's Windows Infrastructure and Active Directory topics. 

---

# Phase 7 — Database Fundamentals → Administration

You already studied Database Fundamentals. Now progress into actual database technologies.

28. **MySQL Database** 
29. **Oracle SQL and PL/SQL** 
30. **Oracle Database Administration I** 
31. **Oracle Database Administration II** 
32. **NoSQL Databases** 
33. **Cloud Database Fundamentals** 

Dependency:

**Database Fundamentals**
 ↓
 **SQL / MySQL**
 ↓
 **Oracle SQL & PL/SQL**
 ↓
 **Oracle DBA I**
 ↓
 **Oracle DBA II**

NoSQL can come after relational database fundamentals.

The PDF includes MySQL, NoSQL, Oracle SQL/PLSQL, Oracle DBA I/II, and database setup for cloud applications. 

---

# Phase 8 — Storage & Data Center

Now that you understand networking, Linux/Windows and databases:

34. **Information Storage and Management** 
35. **Data Center Infrastructure Design** 
36. **Enterprise Backup and Recovery** 
37. **Veeam Backup and Replication** 

Recommended order:

**Storage Fundamentals**
 → **Data Center Design**
 → **Backup Concepts**
 → **Veeam**

These subjects appear under the PDF's **Data Center, Virtualization & Backup** section. 

---

# Phase 9 — Virtualization

Now start turning physical infrastructure concepts into virtual infrastructure.

38. **Virtualization Fundamentals** 
39. **VMware vSphere: Install, Configure and Manage** 
40. **VMware NSX** 
41. **OpenStack Fundamentals** 
42. **OpenStack Deployment and Operation** 
43. **OpenStack APIs** 
44. **Nutanix Multicloud Infrastructure** 

Recommended dependency:

**Virtualization Fundamentals**
 ↓
 **VMware vSphere**
 ↓
 **VMware NSX**

And separately:

**Virtualization Fundamentals**
 ↓
 **OpenStack Fundamentals**
 ↓
 **OpenStack Deployment & Operation**
 ↓
 **OpenStack APIs**

Nutanix can follow the virtualization foundation.

The unified PDF explicitly lists VMware vSphere, VMware NSX, OpenStack deployment/operation/APIs, and Nutanix. 

---

# Phase 10 — Git & Configuration Automation

Before serious DevOps:

45. **Git and Version Control Systems** 
46. **Configuration Management** 
47. **Ansible** 

Recommended dependency:

**Linux + Bash**
 → **Git**
 → **Configuration Management Concepts**
 → **Ansible**

Ansible makes significantly more sense once you're comfortable administering Linux manually.

---

# Phase 11 — Cloud Fundamentals

Do not jump directly to AWS SysOps before understanding cloud concepts.

48. **Cloud Computing Fundamentals** 
49. **AWS Cloud Practitioner** 
50. **Microsoft Azure Fundamentals** 
51. **Google Cloud Platform Fundamentals** 

The PDF's prerequisite page explicitly includes **Introduction to Cloud Computing** and **AWS Cloud Practitioner Essentials** before the more advanced cloud content. 

---

# Phase 12 — AWS Cloud Engineering

Then go deeper into AWS:

52. **AWS Certified Solutions Architect – Associate** 
53. **AWS SysOps Administration** 
54. **Amazon PaaS Web Services** 

Dependency:

**Cloud Fundamentals**
 → **AWS Cloud Practitioner**
 → **AWS Solutions Architect Associate**
 → **AWS SysOps Administration**
 → **AWS PaaS Services**

---

# Phase 13 — Microsoft Azure

After general cloud concepts:

55. **Microsoft Azure Administration** 

Good search term:

**Microsoft Azure Administrator AZ-104**

The unified PDF explicitly includes Microsoft Azure / Azure Administrator as part of the cloud path. 

---

# Phase 14 — Google Cloud Platform

56. **Google Cloud Platform** 

Search:

**Google Cloud Platform Fundamentals**

or

**Google Cloud Associate Cloud Engineer**

The PDF identifies GCP as one of the cloud platforms, but does not specify a certification-level course beyond that. 

---

# Phase 15 — Containers

Do this after Linux, networking and basic cloud.

57. **Application Containers** 
58. **Docker Fundamentals** 
59. **Kubernetes Fundamentals** 
60. **Kubernetes Administration** 
61. **OpenShift** 

Strong dependency chain:

**Linux**
 → **Networking**
 → **Containers concepts**
 → **Docker**
 → **Kubernetes**
 → **OpenShift**

This is one of the most important sequences in the whole curriculum.

The PDF places Docker/Kubernetes/OpenShift in its DevOps/platform engineering material. 

---

# Phase 16 — Infrastructure as Code

Once you understand actual infrastructure:

62. **Infrastructure as Code Fundamentals** 
63. **Terraform** 
64. **Terraform Remote State Management** 

Dependency:

**Cloud + Networking + Linux**
 → **Infrastructure as Code concepts**
 → **Terraform**
 → **Terraform Remote State**

Don't study Terraform deeply before knowing what VPCs, subnets, VMs, storage, IAM, etc. actually are.

---

# Phase 17 — DevOps Fundamentals

Now all the prerequisites start coming together.

65. **DevOps Concepts and Toolchain** 
66. **Continuous Integration** 
67. **Continuous Delivery** 
68. **CI/CD Automation, Integration and Testing** 
69. **Unit and Automated Testing** 

Then combine:

**Git + Linux + Python/Bash + Docker + Cloud**
 ↓
 **DevOps**
 ↓
 **CI/CD**

The PDF explicitly identifies DevOps concepts/toolchain and CI/CD automation/integration/testing. 

---

# Phase 18 — Backend & Cloud Application Development

Now move into application/platform engineering.

70. **Backend Development Fundamentals** 
71. **Node.js** 
72. **Web Services and APIs** 
73. **REST API Development** 
74. **Message Queuing** 
75. **Microservices Architecture** 
76. **Enterprise Application Architecture and Integration** 

Dependency:

**Programming + OOP + Database + Web**
 ↓
 **Backend Development**
 ↓
 **Web Services / APIs**
 ↓
 **Message Queues**
 ↓
 **Microservices**
 ↓
 **Enterprise Integration**

The unified PDF names Node.js, backend development, web services/APIs, microservices, message queuing, and enterprise application architecture/integration. 

---

# Phase 19 — Cloud-Native Development

Combine your development and infrastructure knowledge:

77. **Cloud-Native Application Development** 
78. **Containerized Application Deployment** 
79. **Kubernetes Application Deployment** 
80. **Cloud Application Architecture** 

These names represent the cloud-native/application deployment domain described in the unified curriculum rather than separate formally named ITI courses; the PDF explicitly describes backend/cloud-native development and application deployment as curriculum outcomes. 

---

# Phase 20 — Cybersecurity Fundamentals

Only now start the deeper security sequence.

81. **Cybersecurity Fundamentals** 
82. **Information Security Fundamentals** 
83. **Network Security Fundamentals** 
84. **Security Assessment Fundamentals** 
85. **Ethical Hacking Fundamentals** 

You already learned networking, operating systems, Active Directory, cloud and applications—which makes security much easier to understand properly.

---

# Phase 21 — Network Security

86. **Firewall Technologies** 
87. **Network Security Assessment** 
88. **Network Penetration Testing** 

Firewall technology is explicitly present in the unified PDF's cybersecurity engineering section. 

---

# Phase 22 — Penetration Testing

Then:

89. **Metasploit Essentials** 
90. **Ethical Hacking and Security Assessment** 
91. **Bug Hunting** 
92. **Web Application Penetration Testing** 
93. **Mobile Application Penetration Testing** 
94. **Active Directory Penetration Testing** 

Dependency:

**Networking + Linux + Web + AD + Security Fundamentals**
 ↓
 **Ethical Hacking**
 ↓
 **Metasploit**
 ↓
 **Web / Mobile / AD Pentesting**

All of these areas are explicitly included in the cybersecurity portions of the unified PDF. 

---

# Phase 23 — Application Security

95. **Application Security** 
96. **Web Application Security** 
97. **API Security** 

The PDF explicitly says **Application Security** and includes web penetration testing; API security is best treated as part of the web/API application-security material rather than a separately named course in the PDF.

---

# Phase 24 — Malware & Reverse Engineering

98. **Malware Analysis** 
99. **Reverse Engineering** 

Study malware analysis first and then deepen your reverse-engineering skills.

Both appear explicitly under Cybersecurity Engineering. 

---

# Phase 25 — SOC & Defensive Security

100. **Security Operations Center Fundamentals** 
101. **Security Monitoring Fundamentals** 
102. **Cyber Threat Intelligence** 
103. **Cyber Threat Hunting** 

Dependency:

**Security Fundamentals + Networking + OS administration**
 → **SOC**
 → **Threat Intelligence**
 → **Threat Hunting**

The PDF lists SOC fundamentals, threat hunting and threat intelligence. 

---

# Phase 26 — Incident Response & Forensics

104. **Incident Handling Fundamentals** 
105. **Incident Response** 
106. **Computer Forensics** 
107. **Network Forensics** 

Recommended sequence:

**SOC Fundamentals**
 → **Incident Handling**
 → **Incident Response**
 → **Computer Forensics**
 → **Network Forensics**

These are all explicitly represented in the unified curriculum. 

---

# Phase 27 — OT Security

108. **Operational Technology (OT) Security** 

Take this after:

**Networking + Cybersecurity + Network Security**

OT security appears explicitly in the PDF. 

---

# Phase 28 — GRC

109. **Governance, Risk and Compliance Fundamentals** 
110. **Cybersecurity Risk Assessment** 
111. **Security Compliance** 

The PDF groups **risk assessment and compliance** under Security Operations, IR & Governance. 

---

# Phase 29 — Cloud Security

This comes late intentionally.

112. **Cloud Security Fundamentals** 
113. **AWS Security Fundamentals** 
114. **Azure Security Fundamentals** 
115. **Cloud Security and Governance** 

You need to understand cloud architecture **before** securing cloud architecture.

The unified curriculum explicitly includes **Cloud security and governance**. 

---

# Phase 30 — DevSecOps

116. **DevSecOps Fundamentals** 
117. **DevSecOps CI/CD Security** 
118. **Container Security** 
119. **Kubernetes Security** 
120. **Infrastructure as Code Security** 

The PDF explicitly includes **DevSecOps**; the detailed subtopics above are a practical decomposition of that domain rather than separately named courses in the PDF. 

---

# Phase 31 — AI for IT, Cloud & Security

Leave this until you understand the domain that AI is assisting.

121. **Introduction to Generative AI and Prompt Engineering** 
122. **AI for System Administrators** 
123. **AI for Cloud Engineers** 
124. **Generative AI for DevOps Engineers** 
125. **AI Security** 

The unified curriculum includes introductory GenAI/prompt engineering and specifically identifies AI-assisted operations/security and AI security. 

---

# Phase 32 — Professional Skills

These don't depend heavily on the technical sequence, so you can study them in parallel:

126. **Communication Essentials for Professionals** 
127. **High Impact Presentations** 
128. **Progressive Teamwork** 
129. **Professional Demeanor** 
130. **Job Seeking Skills** 
131. **Freelancing Basics** 

They form the PDF's Soft Skills category. 

---

# The Dependency Map I Recommend

If you want the simplest possible representation, think of the entire track like this:

```
```

```
1. Computer Fundamentals
   ↓
2. Programming + OOP + DSA
   ↓
3. Networking
   ↓
4. Linux + Windows Administration
   ↓
5. Databases + Web Fundamentals
   ↓
6. Storage + Data Centers
   ↓
7. Virtualization
   ↓
8. Cloud Fundamentals
   ↓
9. AWS + Azure + GCP
   ↓
10. Git + Ansible
   ↓
11. Docker
   ↓
12. Kubernetes
   ↓
13. OpenShift
   ↓
14. Terraform / IaC
   ↓
15. DevOps + CI/CD
   ↓
16. Backend + APIs + Microservices
   ↓
17. Cloud-Native Development
   ↓
18. Cybersecurity Fundamentals
   ↓
19. Network Security
   ↓
20. Ethical Hacking / Pentesting
   ↓
21. Application Security
   ↓
22. Malware / Reverse Engineering
   ↓
23. SOC
   ↓
24. Threat Intelligence / Hunting
   ↓
25. Incident Response / Forensics
   ↓
26. GRC
   ↓
27. Cloud Security
   ↓
28. DevSecOps
   ↓
29. AI for Cloud / DevOps / Security
```

## One important clarification

The **course/domain names are grounded in your Unified Cloud PDF**, but the **dependency ordering above is my curriculum organization**. The PDF itself provides categories and an integrated skill map, not an explicit “Course A must be completed before Course B” sequence. 

For your goal—**searching for a course online and learning one subject at a time**—I would start with just these first 10:

1. **Operating Systems Fundamentals** 
2. **Computer Networks Fundamentals** 
3. **Introduction to Programming** 
4. **Python Programming Fundamentals** 
5. **Object-Oriented Programming Fundamentals** 
6. **Data Structures and Algorithms** 
7. **Database Fundamentals** 
8. **Linux Essentials** 
9. **Bash Shell Scripting** 
10. **Introduction to Cybersecurity** 

Then move to **CCNA → Red Hat/Linux → Windows Server → virtualization → cloud → Docker/Kubernetes → Terraform/DevOps → cybersecurity**.

This order will prevent you from repeatedly reaching courses where the instructor assumes knowledge you haven't learned yet.







---
---
| Career     | Level                          | Experience | Realistic Egypt range | Strong multinational / premium employer | Highest observed company benchmark in Egypt                                 |
| ---------- | ------------------------------ | ---------: | --------------------: | --------------------------------------: | --------------------------------------------------------------------------- |
| 🏭 Process | **Junior Process Engineer**    |    0–2 yrs |            **8K–15K** |                             **15K–22K** | **ENPPI — 28K/month** reported for 1–3 yrs                                  |
| 🏭 Process | **Process Engineer**           |    2–5 yrs |           **12K–22K** |                            **20K–30K+** | **Elsewedy Electric — 12K–28K/month**, ~23K median                          |
| 🏭 Process | **Senior Process Engineer**    |   5–8+ yrs |           **22K–40K** |                            **35K–55K+** | **ENPPI — up to ~46K/month company range; 69K reported at 10–14 yrs**       |
| ☁️ Cloud   | **Junior Cloud Engineer**      |    0–2 yrs |           **12K–22K** |                            **20K–30K+** | **PwC — ~48K–52K/month** for Cloud Solution Architect*                      |
| ☁️ Cloud   | **Cloud Engineer**             |    2–5 yrs |           **18K–35K** |                            **30K–55K+** | **PwC — ~48K–52K/month**, ~50K median*                                      |
| ☁️ Cloud   | **Senior Cloud Engineer**      |   5–8+ yrs |           **25K–45K** |                            **40K–70K+** | **InovaSys — ~60K–200K/month**, ~100K median for Cloud Solutions Architect* |
| 🤖 AI      | **Junior Agentic AI Engineer** |    0–2 yrs |           **18K–32K** |                            **30K–45K+** | **Ejada — ~18K–19K/month** for Junior AI Engineer                           |
| 🤖 AI      | **Agentic AI Engineer**        |    2–5 yrs |           **35K–60K** |                            **55K–90K+** | **Deloitte — ~32K–37K/month**, ~34K median for AI Engineer                  |
| 🤖 AI      | **Senior Agentic AI Engineer** |   5–8+ yrs |           **50K–90K** |                           **90K–150K+** | 🥇 **IBM — ~124K–134K/month**, ~**129K median**                             |
| 🔐 Cyber   | **Junior DevSecOps Engineer**  |    0–2 yrs |           **15K–25K** |                            **25K–35K+** | **Valeo — ~15K–18K/month** for Junior DevOps Engineer                       |
| 🔐 Cyber   | **DevSecOps Engineer**         |    2–5 yrs |           **30K–50K** |                            **45K–75K+** | **Orange Business — ~18K–39K/month**, ~37K median for DevOps Engineer       |
| 🔐 Cyber   | **Senior DevSecOps Engineer**  |   5–8+ yrs |           **45K–70K** |                           **70K–120K+** | **PepsiCo — ~657K–713K/year ≈ 55K–59K/month**, ~57K median                  |
