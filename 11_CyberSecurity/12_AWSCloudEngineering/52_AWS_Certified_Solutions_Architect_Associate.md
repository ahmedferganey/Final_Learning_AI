# 52. AWS Certified Solutions Architect – Associate

> Phase 12 — AWS Cloud Engineering

This course moves from **AWS service recognition** into **architecture design**.

Course 49 asked:

```text
"What does this AWS service do?"
```

Course 52 asks:

```text
"Given business, security, availability, performance, and cost requirements,
which AWS architecture should we design, and why?"
```

That is the central Solutions Architect mindset.

---

# Current Certification Baseline

Current certification:

```text
AWS Certified Solutions Architect – Associate
Exam code: SAA-C03
```

Current official exam format:

```text
Exam duration: 130 minutes
Total questions: 65
Scored questions: 50
Unscored questions: 15
Question types:
  - Multiple choice
  - Multiple response
Minimum passing scaled score: 720
Score range: 100–1,000
Certification validity: 3 years
```

Current official scored domains:

```text
Domain 1 — Design Secure Architectures                 30%
Domain 2 — Design Resilient Architectures              26%
Domain 3 — Design High-Performing Architectures        24%
Domain 4 — Design Cost-Optimized Architectures         20%
```

AWS describes the target candidate as someone with **at least one year of hands-on experience designing cloud solutions using AWS services**.

This Markdown goes beyond exam memorization and includes:

```text
architecture reasoning
packet/data flows
CLI examples
configuration examples
failure analysis
trade-off analysis
cost decisions
hands-on labs
scenario drills
troubleshooting
complete capstone
```

---

# Solutions Architect Mental Model

Every architecture problem can be reduced to six questions:

```text
1. What does the business need?
2. What data exists and how is it accessed?
3. What can fail?
4. What must be protected?
5. What performance must be achieved?
6. What cost is acceptable?
```

Then map requirements to AWS building blocks:

```text
Business Requirement
        ↓
Well-Architected Decision
        ↓
Identity / Security
        ↓
Networking
        ↓
Compute
        ↓
Storage
        ↓
Database
        ↓
Integration
        ↓
Observability
        ↓
Backup / DR
        ↓
Cost Optimization
```

A typical resilient AWS architecture:

```text
                               Users
                                 |
                             Route 53
                                 |
                        CloudFront + WAF
                                 |
                      Application Load Balancer
                        /                     \
                 Availability Zone A    Availability Zone B
                        |                     |
                      EC2-1                 EC2-2
                        \                     /
                         \                   /
                          RDS/Aurora Multi-AZ
                                  |
                                 S3
                                  |
                           Cross-Region Backup
```

A modern decoupled architecture:

```text
Client
  |
API Gateway
  |
Lambda / ECS / EKS
  |
  +---------> SQS ---------> Workers
  |
  +---------> EventBridge --> Other Services
  |
  +---------> DynamoDB / Aurora
```

A multi-account foundation:

```text
AWS Organizations
       |
       +-- Security OU
       |    +-- Security Account
       |    +-- Log Archive Account
       |
       +-- Infrastructure OU
       |    +-- Network Account
       |    +-- Shared Services
       |
       +-- Workloads OU
            +-- Production
            +-- Staging
            +-- Development
```

---

## 1. Topic Title

**AWS Certified Solutions Architect – Associate**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Translate business requirements into AWS architectures.
- Apply the AWS Well-Architected Framework during architecture decisions.
- Design secure multi-account AWS environments.
- Design IAM and federation strategies.
- Design secure VPC architectures.
- Design public, private, and isolated subnet structures.
- Select security groups, NACLs, AWS Network Firewall, WAF, and Shield appropriately.
- Design secure hybrid connectivity using VPN and Direct Connect.
- Design private service access using VPC endpoints and PrivateLink.
- Select encryption and key-management strategies.
- Design secure secret-management patterns.
- Select appropriate EC2 instance families and purchasing models.
- Design Auto Scaling and Elastic Load Balancing architectures.
- Select between EC2, Lambda, ECS, EKS, Fargate, Elastic Beanstalk, and Batch.
- Design highly available workloads across Availability Zones.
- Design multi-Region architectures where justified.
- Select Route 53 routing and failover strategies.
- Select S3, EBS, EFS, FSx, and hybrid-storage services based on requirements.
- Design S3 lifecycle, replication, protection, and performance patterns.
- Select relational and non-relational databases based on access patterns.
- Design RDS/Aurora Multi-AZ and read-scaling architectures.
- Design DynamoDB capacity, partition, global, caching, and consistency patterns conceptually.
- Use ElastiCache and RDS Proxy appropriately.
- Design queue-based, pub/sub, and event-driven architectures.
- Select SQS, SNS, EventBridge, Step Functions, and API Gateway correctly.
- Design highly available and fault-tolerant distributed applications.
- Select DR strategies based on RPO/RTO.
- Design backup, replication, pilot-light, warm-standby, and active-active architectures.
- Select high-performance storage, compute, databases, and network services.
- Design CloudFront and Global Accelerator architectures.
- Select data-ingestion and analytics services.
- Design cost-optimized storage, compute, database, and networking.
- Recognize data-transfer cost patterns.
- Use Cost Explorer, Budgets, CUR, Compute Optimizer, and Savings Plans conceptually.
- Review an existing AWS architecture and identify improvements.
- Explain architectural trade-offs instead of choosing services by memorization.
- Solve SAA-C03 scenario questions systematically.
- Perform safe read-oriented AWS CLI architecture discovery.
- Build a complete production AWS architecture design.

---

## 3. Prerequisites

Required:

- 48. Cloud Computing Fundamentals
- 49. AWS Cloud Practitioner
- networking fundamentals
- Linux administration
- storage fundamentals
- database fundamentals
- virtualization
- Git
- configuration management

Recommended practical environment:

```text
AWS sandbox/training account
AWS CLI v2
diagramming tool
Git repository
optional Terraform later
```

Before any AWS lab:

```bash
aws sts get-caller-identity
```

Confirm:

```text
Account
ARN
role/user
Region
```

Use:

```bash
aws configure list
```

or IAM Identity Center profiles to verify credential source.

---

## 4. Core Concepts Explanation

# Part 1 — The Solutions Architect Role

A Solutions Architect converts requirements into architecture.

The role does **not** begin with:

```text
Which service do I like?
```

It begins with:

```text
Business requirement
technical constraint
security constraint
availability target
performance target
cost constraint
```

Then AWS services are selected because they satisfy those requirements.

# Part 2 — Requirement Categories

Classify requirements:

```text
Functional
  - what the system must do

Non-functional
  - availability
  - latency
  - throughput
  - security
  - RPO/RTO
  - scalability
  - cost
```

SAA questions usually hide architecture clues inside non-functional requirements.

# Part 3 — Constraint Recognition

Words matter.

```text
"minimum operational overhead"
→ managed/serverless

"must retain full OS control"
→ EC2

"lowest cost and interruption tolerant"
→ Spot

"millisecond key-value at massive scale"
→ DynamoDB

"shared POSIX filesystem"
→ EFS

"global static content"
→ CloudFront
```

# Part 4 — Architecture Trade-offs

Most architecture decisions trade among:

```text
cost
control
availability
performance
simplicity
portability
operational effort
```

There is rarely one universally best service.

# Part 5 — AWS Well-Architected Framework

The six pillars are:

```text
Operational Excellence
Security
Reliability
Performance Efficiency
Cost Optimization
Sustainability
```

SAA-C03 explicitly validates architecture design against Well-Architected principles.

# Part 6 — Security Pillar Architecture

Ask:

```text
Who can access?
From where?
To what?
How is data encrypted?
How is activity logged?
How is blast radius limited?
```

Typical services:

```text
IAM
Organizations
KMS
Secrets Manager
WAF
Shield
CloudTrail
Config
GuardDuty
```

# Part 7 — Reliability Pillar Architecture

Ask:

```text
What fails?
What detects failure?
What replaces the failed component?
Where is state stored?
How is data recovered?
```

Use:

```text
Multi-AZ
Auto Scaling
ELB
Route 53
backups
replication
queues
```

# Part 8 — Performance Efficiency Pillar Architecture

Ask:

```text
What is the access pattern?
Read-heavy or write-heavy?
Latency-sensitive?
Throughput-heavy?
Bursting?
Global?
```

Then select compute, storage, database, and network technology accordingly.

# Part 9 — Cost Optimization Pillar Architecture

Ask:

```text
Is the resource idle?
Can it scale down?
Is demand predictable?
Can workload be interrupted?
Is data in the correct tier?
Can egress be reduced?
```

# Part 10 — Architecture Review Method

For every diagram, inspect:

```text
Identity
Network
Compute
State
Failure Domains
Data Protection
Monitoring
Cost
```

If any of these is undefined, the architecture is incomplete.

# Part 11 — AWS Global Infrastructure for Architects

Architecture uses:

```text
Region
Availability Zone
edge infrastructure
Local Zones
Outposts
```

The core SAA decision is usually:

```text
single AZ
vs
Multi-AZ
vs
multi-Region
```

# Part 12 — Single-AZ Risk

```text
ALB
 |
EC2
 |
RDS
```

all in one AZ creates a correlated failure domain.

For production HA:

```text
spread compute across AZs
use resilient data service configuration
```

# Part 13 — Multi-AZ

Multi-AZ protects against localized infrastructure failure.

```text
Region
├─ AZ-A: App1
└─ AZ-B: App2
```

A regional load balancer can distribute to both.

# Part 14 — Multi-Region

Use multi-Region only when requirement justifies it:

```text
regional DR
global latency
data sovereignty
regional failure tolerance
```

Costs include:

```text
replication
data transfer
operational complexity
consistency
deployment complexity
```

# Part 15 — Edge Architecture

Edge services include:

```text
CloudFront
Global Accelerator
Route 53
WAF
Shield
```

They move traffic decisions/security/caching closer to users.

# Part 16 — Multi-Account Architecture

Account isolation is one of the strongest AWS blast-radius controls.

Example:

```text
Production Account
Development Account
Security Account
Log Archive Account
Network Account
```

A compromised developer credential should not automatically control production.

# Part 17 — AWS Organizations

Organizations provides:

```text
account hierarchy
OUs
SCPs
consolidated billing
central governance
```

It is central to enterprise architecture.

# Part 18 — Service Control Policies

SCP:

```text
sets maximum permitted actions
```

It does **not** grant permissions.

Effective access still requires an IAM allow and absence of an applicable deny.

# Part 19 — Control Tower

Control Tower helps establish a governed multi-account environment.

Think:

```text
landing zone
account factory
controls/guardrails
central logging/governance
```

# Part 20 — AWS RAM

Resource Access Manager shares supported resources across AWS accounts.

Use case:

```text
central networking/shared infrastructure
→ share subnets/resources with workload accounts
```

Avoid duplicating shared resources unnecessarily.

# Part 21 — IAM Design Principle

Prefer:

```text
federated human access
temporary credentials
roles
least privilege
```

Avoid:

```text
long-lived IAM access keys
shared accounts
root use
```

# Part 22 — IAM Identity Center

Workforce architecture:

```text
Corporate IdP
      ↓
IAM Identity Center
      ↓
Permission Set
      ↓
Role in AWS Account
```

This scales better than one IAM user per account.

# Part 23 — Cross-Account Access

Pattern:

```text
User in Admin Account
      ↓ STS AssumeRole
Production Role
      ↓
Production Resources
```

No duplicate long-lived credentials are required.

# Part 24 — Trust Policy

An IAM role has a trust policy defining:

```text
who may assume the role
```

Permission policy defines:

```text
what the assumed role can do
```

Do not confuse the two.

# Part 25 — Identity Policy vs Resource Policy

Identity policy:

```text
attached to user/role
```

Resource policy:

```text
attached to resource
```

Examples of resources supporting policies include:

```text
S3
SQS
SNS
KMS
Lambda
```

depending on service.

# Part 26 — Permission Evaluation

Simplified:

```text
implicit deny by default
+
applicable allow
-
any explicit deny
=
effective permission
```

SCPs, boundaries, resource policies, and session policies can further constrain access.

# Part 27 — Permission Boundary

Permissions boundary limits the maximum permissions an IAM user/role policy can grant.

Useful when:

```text
delegated administrators may create roles
but must not exceed approved privilege
```

# Part 28 — STS Temporary Credentials

STS credentials expire.

This reduces risk compared with permanent access keys.

Use for:

```text
roles
federation
cross-account
workloads
```

# Part 29 — EC2 Instance Role

Architecture:

```text
EC2
 ↓ Instance Profile
IAM Role
 ↓ temporary credentials
S3/DynamoDB/etc.
```

Do not place AWS access keys in EC2 configuration files.

# Part 30 — Lambda Execution Role

Lambda receives AWS permissions through its execution role.

Apply least privilege:

```text
function needs PutItem to one DynamoDB table
```

not:

```text
AdministratorAccess
```

# Part 31 — VPC Architecture

VPC is regional.

Example:

```text
VPC 10.20.0.0/16

AZ-A:
  Public-A
  App-A
  DB-A

AZ-B:
  Public-B
  App-B
  DB-B
```

Subnets are AZ-specific.

# Part 32 — CIDR Planning

Plan for:

```text
current workload
growth
on-prem ranges
future VPCs
other clouds
acquisitions
```

Overlapping CIDRs complicate routing and hybrid connectivity.

# Part 33 — Public Subnet

A subnet is public when its route table routes Internet-bound traffic to an Internet Gateway.

Typical:

```text
0.0.0.0/0 → igw
```

The resource still requires a public address and firewall permission.

# Part 34 — Private Subnet

Private subnet lacks direct Internet Gateway route.

Typical app instances:

```text
private IP only
outbound via NAT
```

Inbound traffic arrives through ALB/private paths.

# Part 35 — Isolated Subnet

Database subnet can have:

```text
no Internet default route
```

It only communicates with approved internal services.

This minimizes exposure.

# Part 36 — Route Table Design

Example:

```text
Public subnet:
VPC CIDR → local
0.0.0.0/0 → IGW

Private app:
VPC CIDR → local
0.0.0.0/0 → NAT

DB:
VPC CIDR → local
```

# Part 37 — Internet Gateway

IGW provides VPC Internet routing.

It does not itself:

```text
open firewall ports
assign public IPs
make private resources public
```

# Part 38 — NAT Gateway

Private IPv4 instances can initiate Internet traffic:

```text
Private EC2
 ↓
NAT Gateway
 ↓
IGW
 ↓
Internet
```

For AZ resilience, commonly place NAT capacity per AZ and route same-AZ private subnets accordingly.

# Part 39 — NAT Gateway Cost Trade-off

NAT Gateway adds:

```text
hourly cost
data-processing cost
possible cross-AZ transfer if architecture is poor
```

Alternatives for AWS-service traffic:

```text
VPC endpoints
```

can reduce NAT dependency.

# Part 40 — Security Groups

Stateful resource-level firewall.

Recommended pattern:

```text
ALB-SG:
443 from Internet

APP-SG:
8080 from ALB-SG

DB-SG:
5432 from APP-SG
```

Referencing SGs is preferable to hardcoded IPs between application tiers.

# Part 41 — NACLs

Stateless subnet-level ACL.

Can:

```text
allow
deny
```

and requires rules for both traffic directions.

Use for coarse subnet boundary controls where needed.

# Part 42 — Security Group vs NACL

```text
Security Group:
stateful
resource/ENI
allow rules

NACL:
stateless
subnet
allow + deny
```

This distinction appears frequently in SAA scenarios.

# Part 43 — VPC Flow Logs

Flow Logs capture metadata about IP traffic.

Useful for:

```text
accepted/rejected traffic
network troubleshooting
security investigation
```

They do not capture full packet payloads.

# Part 44 — AWS Network Firewall

Managed network firewall for VPC traffic inspection.

Use when requirements include:

```text
centralized stateful filtering
domain/protocol inspection patterns
network security policy
```

# Part 45 — AWS WAF

Layer-7 HTTP request filtering.

Use for:

```text
SQL injection patterns
XSS patterns
IP/rate restrictions
managed rules
```

Attach to supported web-facing AWS services.

# Part 46 — AWS Shield

DDoS protection.

Think:

```text
Shield → DDoS
WAF → HTTP request filtering
```

They solve different layers.

# Part 47 — Firewall Manager

Centralizes firewall/security policies across accounts.

Useful with Organizations for:

```text
WAF
Shield
security groups
Network Firewall policies
```

depending on supported policy type.

# Part 48 — VPC Peering

Direct private VPC connectivity.

Limitation:

```text
non-transitive
```

Large many-VPC topologies can become difficult.

# Part 49 — Transit Gateway

Hub-and-spoke:

```text
VPC A \
VPC B  → Transit Gateway → On-Prem
VPC C /
```

Scales connectivity better than full-mesh peering.

# Part 50 — PrivateLink

Private service consumption:

```text
Consumer VPC
 ↓ interface endpoint
PrivateLink
 ↓
Provider Service
```

No VPC peering/full routing relationship is required.

# Part 51 — Gateway Endpoints

Gateway endpoints are used for:

```text
S3
DynamoDB
```

They provide private routing without NAT for supported traffic.

# Part 52 — Interface Endpoints

Interface endpoints create ENIs with private IPs for many AWS services using PrivateLink.

Use when:

```text
private access to AWS APIs
no Internet/NAT desired
```

# Part 53 — Site-to-Site VPN

Encrypted hybrid connectivity over Internet.

Good for:

```text
rapid hybrid setup
backup connectivity
moderate bandwidth
```

# Part 54 — Direct Connect

Dedicated private connectivity.

Use when:

```text
stable high bandwidth
hybrid enterprise
predictable network path
```

Encryption may require additional design.

# Part 55 — VPN + Direct Connect

Common resilient hybrid design:

```text
Primary: Direct Connect
Backup: Site-to-Site VPN
```

or encrypted VPN over Direct Connect where required by design.

# Part 56 — CloudHub / Transit Hybrid Concepts

Large hybrid environments may centralize connectivity through:

```text
Transit Gateway
Direct Connect Gateway
VPN attachments
```

The core architect decision is scalable routing and failure isolation.

# Part 57 — Route 53

Route 53 provides:

```text
DNS
health checks
traffic routing
domain registration
```

Architecture questions often involve routing policy selection.

# Part 58 — Simple Routing

Use when:

```text
one primary endpoint
no advanced routing policy required
```

# Part 59 — Weighted Routing

Split traffic:

```text
90% → old version
10% → new version
```

Useful for:

```text
canary release
A/B testing
gradual migration
```

# Part 60 — Latency-Based Routing

Routes users to the Region expected to provide lowest network latency.

Use for global active deployments.

# Part 61 — Failover Routing

```text
Primary healthy
→ primary

Primary unhealthy
→ secondary
```

Used in active-passive DR architectures.

# Part 62 — Geolocation Routing

Routes based on user geographic location.

Use for:

```text
localization
regulatory routing
content differentiation
```

# Part 63 — Multivalue Answer Routing

Can return multiple healthy records.

Provides simple DNS-level distribution but is not equivalent to a full load balancer.

# Part 64 — Elastic Load Balancing

Load balancers improve:

```text
availability
distribution
health-based routing
scaling
```

Choose type by protocol and architecture.

# Part 65 — Application Load Balancer

Layer 7:

```text
HTTP
HTTPS
host routing
path routing
headers
target groups
```

Ideal for web/microservice architectures.

# Part 66 — ALB Host-Based Routing

Example:

```text
api.example.com → API target group
shop.example.com → Shop target group
```

# Part 67 — ALB Path-Based Routing

Example:

```text
/images/* → image service
/api/*    → API service
```

Reduces need for separate load balancers.

# Part 68 — Network Load Balancer

Layer 4.

Use for:

```text
TCP/UDP/TLS
very high throughput
low latency
static IP requirements
```

# Part 69 — Gateway Load Balancer

Deploys/scales network appliances.

```text
traffic
 ↓
GWLB
 ↓
firewall/inspection appliance fleet
```

# Part 70 — Load Balancer Health Checks

Architecture depends on meaningful health checks.

Bad:

```text
TCP port open
```

when application is broken.

Better:

```text
/health
```

that verifies the service can perform required operations.

# Part 71 — EC2 Architecture

Select:

```text
instance family
size
AMI
EBS
network
IAM role
placement
purchase model
scaling
```

based on requirements.

# Part 72 — Instance Family Selection

Broad mapping:

```text
general purpose → balanced
compute optimized → CPU-heavy
memory optimized → RAM-heavy
storage optimized → local I/O-heavy
accelerated → GPU/accelerator
```

# Part 73 — Right-Sizing

Measure:

```text
CPU
memory
network
disk throughput
IOPS
latency
```

then choose appropriate instance.

Oversizing is cost waste; undersizing causes performance instability.

# Part 74 — On-Demand

Use for:

```text
short-term
unknown demand
no commitment
```

Highest flexibility.

# Part 75 — Spot

Use for:

```text
fault-tolerant
interruptible
batch
distributed workers
CI
```

Design interruption handling.

# Part 76 — Savings Plans

Use for predictable baseline compute usage where commitment is acceptable.

Architect should measure utilization before committing.

# Part 77 — Reserved Instances

Pricing commitment model for eligible EC2/RDS contexts.

Remember:

```text
discount
≠
capacity guarantee
```

# Part 78 — Capacity Reservations

Reserve EC2 capacity in an AZ.

Use when:

```text
capacity must be available
```

especially during failover or special events.

# Part 79 — Dedicated Hosts

Use when:

```text
socket/core licensing
compliance
physical-server visibility/control requirement
```

# Part 80 — Placement Groups

Placement options optimize failure/performance characteristics.

Conceptual types:

```text
cluster
spread
partition
```

Select based on workload.

# Part 81 — Cluster Placement Group

Places instances close together for low-latency/high-throughput networking.

Use for HPC-like tightly coupled workloads.

Tradeoff:

```text
higher correlated failure risk
```

# Part 82 — Spread Placement Group

Places small number of critical instances across distinct hardware.

Use when reducing correlated hardware failure matters.

# Part 83 — Partition Placement Group

Partitions large fleets across hardware partitions.

Useful for distributed systems such as:

```text
Hadoop
Cassandra
Kafka-style architectures
```

where members are aware of partitions/failure domains.

# Part 84 — EC2 Auto Scaling

ASG provides:

```text
desired capacity
minimum
maximum
health replacement
scaling
multi-AZ distribution
```

# Part 85 — Launch Template

Defines:

```text
AMI
instance type
security groups
IAM role
user data
storage
```

for reusable EC2 launches.

# Part 86 — Target Tracking Scaling

Example:

```text
maintain average CPU ≈ 50%
```

Good default for many elastic workloads.

# Part 87 — Step Scaling

Example:

```text
CPU > 70% → +2
CPU > 90% → +5
```

Useful when response should vary by alarm severity.

# Part 88 — Scheduled Scaling

Use when demand is predictable.

Example:

```text
weekday 08:00
increase desired capacity
```

# Part 89 — Predictive Scaling Concept

Uses historical patterns to anticipate capacity demand.

Useful for recurring predictable patterns.

# Part 90 — EC2 Hibernation

Preserves RAM state to EBS for supported instances/configurations.

Use when applications have expensive in-memory initialization and hibernation constraints are met.

# Part 91 — Immutable EC2 Architecture

Instead of patching long-lived servers:

```text
build AMI
 ↓
launch new ASG instances
 ↓
shift traffic
 ↓
terminate old
```

This reduces configuration drift.

# Part 92 — AMI Strategy

Use:

```text
versioned golden AMIs
patch baseline
security agents
application prerequisites
```

combined with lightweight startup configuration.

# Part 93 — Lambda Architecture

Use Lambda when:

```text
event-driven
short-lived execution
automatic scaling
minimal server operations
```

Common integrations:

```text
API Gateway
S3
SQS
SNS
EventBridge
DynamoDB Streams
```

# Part 94 — Lambda Concurrency

Concurrency determines simultaneous executions.

Architectural concerns:

```text
downstream DB capacity
reserved concurrency
throttling
burst behavior
```

Serverless compute can overwhelm a stateful backend if not controlled.

# Part 95 — Lambda Memory and Performance

Lambda allocates CPU/resources in relation to configured memory.

More memory can reduce execution duration.

Cost optimization requires measuring:

```text
memory × duration
```

not always choosing the smallest memory.

# Part 96 — Lambda VPC Access

A function can connect to private VPC resources.

Do not place Lambda in VPC merely "for security" unless it requires private networking; consider service access patterns and endpoints.

# Part 97 — Lambda Dead-Letter / Failure Destinations

Asynchronous failures need durable handling.

Architect:

```text
retry
DLQ/destination
alarm
reprocessing
```

# Part 98 — ECS

AWS-native container orchestration.

Run tasks/services on:

```text
EC2
Fargate
```

# Part 99 — EKS

Managed Kubernetes.

Use when:

```text
Kubernetes API/ecosystem required
portability/standard tooling needed
```

Operational complexity is higher than simpler managed compute.

# Part 100 — Fargate

Serverless compute for containers.

Use when:

```text
container workload
no EC2 node management
```

Cost/performance should be compared with EC2-backed container capacity for steady high-scale workloads.

# Part 101 — ECR

Container image registry.

Architecture:

```text
CI
 ↓
ECR
 ↓
ECS/EKS
```

Use IAM, scanning, immutable tags where appropriate, and image lifecycle policies.

# Part 102 — Elastic Beanstalk

PaaS-style application deployment.

Use when:

```text
traditional web app
AWS-managed environment provisioning
less platform engineering
```

while retaining underlying AWS resources.

# Part 103 — AWS Batch

Batch scheduling for compute jobs.

Use:

```text
queued jobs
parallel processing
variable compute demand
```

with managed scheduling.

# Part 104 — Storage Decision Framework

Ask:

```text
block?
file?
object?
shared?
latency?
IOPS?
throughput?
durability?
access frequency?
```

# Part 105 — Amazon S3

Object storage.

Best for:

```text
static assets
backup
logs
data lake
documents
archives
artifacts
```

Not a block filesystem.

# Part 106 — S3 Storage Classes

Select based on access pattern:

```text
Standard
Intelligent-Tiering
Standard-IA
One Zone-IA
Glacier Instant Retrieval
Glacier Flexible Retrieval
Glacier Deep Archive
```

# Part 107 — S3 Intelligent-Tiering

Use when access is:

```text
unknown
changing
```

to automatically adjust between supported access tiers.

# Part 108 — S3 Lifecycle

Example:

```text
0–30d   Standard
31–90d  Standard-IA
>90d    Glacier
>7y     Expire
```

Include old versions where versioning is enabled.

# Part 109 — S3 Versioning

Protects against:

```text
overwrite
delete
```

by preserving object versions.

It is especially useful with backup/replication designs.

# Part 110 — S3 Object Lock

WORM-style retention.

Use for:

```text
compliance
ransomware-resistant backup
immutable records
```

# Part 111 — S3 Replication

Options include:

```text
same-Region
cross-Region
cross-account
```

depending on requirement.

Use for:

```text
DR
compliance
account isolation
latency
```

# Part 112 — S3 Transfer Acceleration

Uses AWS edge network to accelerate uploads over long geographic distances to an S3 bucket.

Use only when transfer benefit justifies additional cost.

# Part 113 — S3 Multipart Upload

Large files should use multipart upload.

Benefits:

```text
parallel parts
retry individual parts
improved throughput
```

# Part 114 — S3 Request Performance

S3 scales automatically for high request rates.

Architect around:

```text
parallelism
multipart transfer
client networking
object size
```

rather than legacy prefix-randomization assumptions.

# Part 115 — S3 Presigned URL

Temporary delegated object access.

Architecture:

```text
App authenticates user
 ↓
creates presigned URL
 ↓
client uploads/downloads directly to S3
```

Reduces application-server data transfer.

# Part 116 — Amazon EBS

AZ-scoped block storage for EC2.

Use for:

```text
boot volumes
databases
filesystems
transactional storage
```

# Part 117 — EBS gp3

General-purpose SSD where performance can be provisioned more independently from size than older models.

Good default for many workloads.

# Part 118 — EBS io2

Provisioned IOPS SSD for high-performance/high-durability I/O workloads.

Use when:

```text
database IOPS/latency requirements
```

justify the cost.

# Part 119 — EBS st1

Throughput-optimized HDD.

Use for:

```text
large sequential workloads
logs
data processing
```

not boot volumes or small random I/O.

# Part 120 — EBS sc1

Cold HDD for lowest-cost infrequently accessed throughput-oriented workloads.

# Part 121 — EBS Snapshots

Incremental block snapshot model.

Use for:

```text
backup
restore
copy
cross-Region DR
AMI creation
```

# Part 122 — EBS Multi-Attach Concept

Supported io-class volumes can attach to multiple instances under specific constraints.

Application/filesystem must be cluster-aware.

Do not use as a generic shared filesystem replacement.

# Part 123 — Amazon EFS

Managed elastic NFS file storage.

```text
EC2-A \
EC2-B  → EFS
EC2-C /
```

Useful for shared Linux file access.

# Part 124 — EFS Performance Model

Consider:

```text
throughput mode
performance mode
access pattern
number of clients
```

Use lifecycle classes for cost optimization.

# Part 125 — FSx

Purpose-built managed filesystems.

Examples:

```text
FSx for Windows File Server
FSx for Lustre
FSx for NetApp ONTAP
FSx for OpenZFS
```

Select based on filesystem/protocol/workload.

# Part 126 — FSx for Lustre

High-performance parallel filesystem.

Use for:

```text
HPC
ML
media processing
large-scale analytics
```

and can integrate with S3.

# Part 127 — Storage Gateway

Hybrid storage bridge.

Modes/services support file, volume, and tape-oriented hybrid use cases.

# Part 128 — AWS DataSync

Online accelerated data transfer between supported storage systems and AWS.

Use for:

```text
large file migration
recurring sync
NAS migration
```

# Part 129 — AWS Transfer Family

Managed endpoints for protocols such as:

```text
SFTP
FTPS
FTP
AS2
```

integrated with S3/EFS depending on configuration.

# Part 130 — Snow Family

Physical edge/data-transfer devices.

Use when:

```text
network transfer is too slow
large offline data migration
edge compute requirement
```

# Part 131 — Database Selection Framework

Ask:

```text
relational?
document?
key-value?
graph?
in-memory?
write pattern?
read pattern?
consistency?
global?
scale?
```

Choose purpose-built service.

# Part 132 — Amazon RDS

Managed relational service.

Use when application requires traditional relational engines and SQL.

AWS manages more infrastructure operations than a DB on EC2.

# Part 133 — RDS Multi-AZ

Primary purpose:

```text
high availability
```

A standby exists in another AZ according to deployment model.

Do not treat standby as application read-scaling target unless the selected newer deployment mode explicitly supports readable standbys.

# Part 134 — RDS Read Replica

Primary purpose:

```text
read scaling
```

and sometimes DR/migration patterns.

Replication is generally asynchronous.

# Part 135 — RDS Proxy

Pools/manages database connections.

Useful for:

```text
Lambda high concurrency
connection storms
application failover handling
```

to reduce pressure on RDS/Aurora.

# Part 136 — Aurora

AWS cloud-native relational database compatible with MySQL/PostgreSQL protocols.

Uses distributed storage architecture and supports replicas/HA patterns.

# Part 137 — Aurora Replicas

Use for:

```text
read scaling
fast failover targets
```

Application can use reader endpoint for read distribution.

# Part 138 — Aurora Serverless

Use when relational workload capacity is:

```text
variable
intermittent
hard to forecast
```

and supported engine/version/configuration fits.

# Part 139 — DynamoDB

Serverless key-value/document NoSQL.

Use for:

```text
single-digit-millisecond access
massive scale
known key-based access patterns
```

# Part 140 — DynamoDB Partition Key

Partition key determines data distribution.

Bad:

```text
all writes use same key
```

→ hot partition risk.

Good key distributes workload across partitions.

# Part 141 — DynamoDB Composite Key

```text
Partition Key + Sort Key
```

supports grouped/queryable item collections.

Example:

```text
PK = CUSTOMER#123
SK = ORDER#2026-001
```

# Part 142 — DynamoDB Capacity Modes

Broad options:

```text
on-demand
provisioned
```

Choose by predictability and cost/performance requirements.

# Part 143 — DynamoDB DAX

DynamoDB Accelerator is an in-memory cache for DynamoDB.

Use when:

```text
microsecond read latency
read-heavy workload
```

# Part 144 — DynamoDB Global Tables

Multi-Region active-active replicated DynamoDB architecture.

Use for:

```text
global low latency
regional resilience
```

with conflict/consistency implications understood.

# Part 145 — DynamoDB Streams

Captures item-level change events.

Use with:

```text
Lambda
event processing
replication/workflows
```

# Part 146 — ElastiCache

Managed in-memory cache.

Use for:

```text
sessions
hot reads
query caching
leaderboards
rate limiting
```

depending on engine/features.

# Part 147 — Cache-Aside Pattern

```text
App
 ↓ check cache
hit → return

miss
 ↓ database
 ↓ populate cache
```

Need TTL/invalidation strategy.

# Part 148 — DocumentDB

Managed document database with MongoDB-compatible API focus.

Use for document-oriented workloads requiring that compatibility model.

# Part 149 — Neptune

Graph database.

Use for:

```text
fraud graph
social relationships
knowledge graph
recommendation relationships
```

# Part 150 — Keyspaces

Managed Apache Cassandra-compatible wide-column database service.

Use for Cassandra workloads without managing clusters.

# Part 151 — Loose Coupling

Tightly coupled:

```text
Web → Worker directly
```

If Worker fails:

```text
Web fails
```

Loosely coupled:

```text
Web → Queue → Worker
```

Queue absorbs temporary failure/bursts.

# Part 152 — SQS

Queue for:

```text
buffering
decoupling
async work
retry
```

Consumers poll/process messages.

# Part 153 — SQS Standard

Provides:

```text
very high throughput
at-least-once delivery
best-effort ordering
```

Consumers must be idempotent.

# Part 154 — SQS FIFO

Use when requirement includes:

```text
strict ordering
deduplication semantics
```

within FIFO constraints.

# Part 155 — Visibility Timeout

When worker receives message:

```text
message temporarily hidden
```

If worker finishes:

```text
delete message
```

If it fails:

```text
visibility expires
→ message becomes visible again
```

# Part 156 — Dead-Letter Queue

After repeated processing failures:

```text
main queue
 ↓ max receives
DLQ
```

Use alarms and remediation/replay process.

# Part 157 — SNS

Pub/sub fan-out:

```text
Publisher
 ↓
SNS Topic
 ├─ SQS A
 ├─ SQS B
 └─ Lambda
```

# Part 158 — SNS + SQS Fan-Out

Pattern:

```text
one event
→ multiple independent durable consumers
```

Each subscriber gets its own queue.

# Part 159 — EventBridge

Event bus/routing service.

Use for:

```text
AWS service events
application events
SaaS events
rules
targets
```

# Part 160 — SQS vs EventBridge

```text
SQS:
durable work queue

EventBridge:
event routing based on event patterns
```

They can be combined.

# Part 161 — Step Functions

Workflow orchestration:

```text
Task A
 ↓
Choice
├─ success → Task B
└─ failure → Retry/Compensate
```

Use instead of implementing complex workflow state manually.

# Part 162 — API Gateway

Managed API front door.

Use for:

```text
REST/HTTP/WebSocket APIs
authentication
throttling
request management
Lambda/service integrations
```

# Part 163 — API Gateway + Lambda

Serverless API:

```text
Client
 ↓
API Gateway
 ↓
Lambda
 ↓
DynamoDB
```

scales without EC2 server management.

# Part 164 — Resilient Architecture Principle

Design for failure:

```text
instances fail
AZs fail
dependencies throttle
messages duplicate
networks partition
humans make mistakes
```

Architecture should recover automatically where practical.

# Part 165 — Eliminate Single Points of Failure

Inspect:

```text
one NAT?
one EC2?
one AZ?
one database?
one VPN tunnel?
one Region?
one administrator?
```

Then decide if redundancy is required by business target.

# Part 166 — Stateless Application Tier

Store state externally:

```text
session → ElastiCache/DynamoDB
files → S3/EFS
data → DB
```

Then instances can be replaced/scaled freely.

# Part 167 — Health-Based Replacement

ASG can replace unhealthy instances.

Combine:

```text
ELB health checks
ASG
immutable launch template
```

for self-healing compute.

# Part 168 — Graceful Degradation

When optional dependency fails:

```text
recommendation service unavailable
```

core checkout may still operate.

Architecture should distinguish:

```text
critical
noncritical
```

dependencies.

# Part 169 — Backpressure

If consumers cannot keep up:

```text
queue depth grows
```

Use:

```text
SQS
autoscaling based on queue depth
rate limits
```

rather than dropping requests.

# Part 170 — Idempotency

Because retries/duplicate messages happen:

```text
same request twice
→ same final state
```

Use idempotency keys/conditional writes where relevant.

# Part 171 — Disaster Recovery Strategy Overview

From lowest cost/highest RTO to highest cost/lowest RTO:

```text
Backup & Restore
Pilot Light
Warm Standby
Multi-Site Active/Active
```

# Part 172 — Backup and Restore

```text
Primary Region
 ↓ backups
Secondary storage
```

During disaster:

```text
restore infrastructure/data
```

Lowest steady cost, highest recovery time.

# Part 173 — Pilot Light

Core data/services run in DR Region at minimal scale.

During disaster:

```text
scale application infrastructure
switch traffic
```

# Part 174 — Warm Standby

Scaled-down but functional copy runs in secondary Region.

During disaster:

```text
scale up
shift traffic
```

Lower RTO than pilot light.

# Part 175 — Active-Active

Both Regions serve production.

```text
Region A ↔ Region B
```

Lowest potential RTO, highest complexity and cost.

Requires data consistency/conflict strategy.

# Part 176 — RPO

RPO determines tolerated data loss.

Example:

```text
RPO 5 minutes
```

means backup/replication must protect data frequently enough.

# Part 177 — RTO

RTO determines tolerated outage time.

Example:

```text
RTO 30 minutes
```

rules out recovery processes that require hours.

# Part 178 — Route 53 DR

Use health checks/failover routing for DNS-based disaster failover.

Account for:

```text
TTL
health detection
application readiness
database state
```

# Part 179 — S3 Cross-Region Replication for DR

Use CRR when object data must be replicated to another Region.

Consider:

```text
versioning
replication IAM
KMS permissions
replication time requirement
```

# Part 180 — RDS Cross-Region Read Replica

Can support:

```text
DR
global reads
migration
```

for supported engines.

Promotion during disaster changes architecture and may require DNS/application updates.

# Part 181 — Aurora Global Database Concept

Designed for cross-Region Aurora replication with low-latency replication architecture and regional failover patterns.

Use for global relational workloads requiring multi-Region design.

# Part 182 — DynamoDB Global Tables for DR

Active-active data across Regions.

Use when application architecture supports multi-Region writes and conflict model.

# Part 183 — AWS Backup

Central backup policy/orchestration for supported services.

Design:

```text
backup plans
vaults
retention
cross-account copies
cross-Region copies
```

# Part 184 — Cross-Account Backup

Security architecture:

```text
Production Account
 ↓ backup copy
Backup Account
```

reduces risk that compromise of production permissions destroys backup copies.

# Part 185 — High-Performance Storage Selection

Map workload:

```text
massive object throughput → S3
low-latency block → EBS
shared Linux file → EFS
HPC parallel file → FSx Lustre
Windows SMB → FSx Windows
```

# Part 186 — EBS Performance

Architect with:

```text
IOPS
throughput
latency
queue depth
instance EBS bandwidth
volume type
```

Provisioning a fast volume cannot exceed EC2 instance storage limits.

# Part 187 — S3 Performance Architecture

Use:

```text
parallel requests
multipart uploads
CloudFront for downloads
Transfer Acceleration for distant upload scenarios
```

depending on requirement.

# Part 188 — EFS Performance Architecture

Measure:

```text
throughput
metadata operations
client concurrency
file sizes
```

and choose performance/throughput mode.

# Part 189 — High-Performance Compute

Select:

```text
EC2 family
Auto Scaling
Lambda
ECS/EKS/Fargate
Batch
EMR
```

based on execution model.

# Part 190 — Horizontal vs Vertical Scaling

Vertical:

```text
bigger instance
```

Horizontal:

```text
more instances
```

Cloud-native stateless services generally favor horizontal scaling.

# Part 191 — Scaling Metric Selection

CPU is not always best.

Better workload metrics may include:

```text
SQS queue depth
requests per target
latency
concurrent sessions
custom business metric
```

# Part 192 — Compute Decoupling

Architecture:

```text
API fleet
 ↓
SQS
 ↓
worker fleet
```

Each tier scales independently.

# Part 193 — Database Performance Selection

Ask:

```text
transactional?
analytical?
key lookup?
graph?
cache?
global?
read-heavy?
write-heavy?
```

# Part 194 — Read-Heavy Relational Workload

Use:

```text
RDS/Aurora primary
+
read replicas
+
ElastiCache if repeated hot reads
```

# Part 195 — Connection Scaling

High application concurrency can exhaust DB connections.

Use:

```text
connection pool
RDS Proxy
application pool
```

especially with Lambda bursts.

# Part 196 — DynamoDB Read/Write Scaling

Use:

```text
good partition key
on-demand/provisioned mode
autoscaling
DAX where read latency requires
```

Avoid hot partitions.

# Part 197 — CloudFront

CDN for:

```text
static/dynamic web content
S3 origins
ALB origins
edge caching
TLS
WAF integration
```

# Part 198 — Cache Behavior

Control:

```text
TTL
cache key
headers
cookies
query strings
```

Bad cache keys reduce hit rate and increase origin cost.

# Part 199 — Origin Access Control

For private S3 origins:

```text
CloudFront
 ↓ signed AWS request
private S3 bucket
```

so users cannot bypass CloudFront directly.

# Part 200 — Global Accelerator

Use when:

```text
global users
TCP/UDP or HTTP
static anycast IP
fast failover to healthy regional endpoint
```

It does not cache content like CloudFront.

# Part 201 — CloudFront vs Global Accelerator

```text
CloudFront:
CDN/content caching/HTTP delivery

Global Accelerator:
network acceleration/static anycast IP/endpoint failover
```

# Part 202 — Data Ingestion Architecture

Common patterns:

```text
batch
stream
file transfer
database replication
event ingestion
```

Choose service by frequency, volume, latency, format.

# Part 203 — Kinesis

Streaming service family.

Use for:

```text
real-time event streams
telemetry
clickstream
logs
```

# Part 204 — Amazon Data Firehose

Managed streaming delivery to destinations.

Use when:

```text
ingest stream
transform optionally
deliver to S3/analytics destinations
```

with less consumer infrastructure.

# Part 205 — Amazon MSK

Managed Apache Kafka.

Use when:

```text
Kafka API/ecosystem required
existing Kafka application
```

# Part 206 — AWS Glue

Managed data integration:

```text
catalog
ETL
data transformation
```

Common data-lake architecture component.

# Part 207 — Athena

Serverless SQL over data in S3.

Cost/performance improve with:

```text
partitioning
columnar formats
compression
selective columns
```

# Part 208 — Parquet Transformation

Converting:

```text
CSV
→ Parquet
```

can reduce:

```text
scanned bytes
query cost
query time
```

for analytical workloads.

# Part 209 — Lake Formation

Helps build/govern data lakes with centralized access controls.

Use where data-lake governance is required across AWS analytics services.

# Part 210 — Redshift

Data warehouse.

Use for:

```text
large analytical SQL
BI
warehouse workloads
```

not ordinary transactional OLTP.

# Part 211 — EMR

Managed big-data frameworks such as Spark/Hadoop.

Use when workloads depend on those ecosystems and need cluster/data-processing architecture.

# Part 212 — Cost Optimization Framework

Cost is an architecture property.

Review:

```text
resource count
resource size
hours
storage tier
requests
data transfer
licenses
managed-service premium
operational labor
```

# Part 213 — Right-Sizing Compute

Use telemetry and Compute Optimizer-style recommendations.

Do not optimize solely for average CPU; inspect peaks, memory, I/O, and business risk.

# Part 214 — Purchase Model Decision

```text
unpredictable → On-Demand
steady baseline → Savings Plans / RI
interruptible → Spot
capacity guarantee → Capacity Reservation
physical licensing → Dedicated Host
```

# Part 215 — Spot Fleet Architecture

For resilient workloads:

```text
multiple instance types
multiple AZs
multiple capacity pools
```

reduce interruption/capacity risk.

# Part 216 — Serverless Cost Optimization

Serverless can reduce cost for:

```text
bursty
low duty-cycle
event-driven
```

workloads.

For steady high utilization, compare with containers/EC2.

# Part 217 — Storage Cost Optimization

Use:

```text
S3 lifecycle
Intelligent-Tiering
EBS right-sizing
delete unattached volumes
snapshot lifecycle
EFS lifecycle
correct FSx tier
```

# Part 218 — S3 Request Cost

Architecture affects number of requests.

Millions of tiny objects/requests can create request cost and inefficiency.

Batch/compress where appropriate.

# Part 219 — Database Cost Optimization

Consider:

```text
instance size
serverless mode
read replicas
reserved pricing
storage
I/O
cache
retention
idle nonproduction
```

# Part 220 — DynamoDB Cost Optimization

Compare:

```text
on-demand
provisioned + autoscaling
reserved capacity where applicable
```

based on traffic predictability.

# Part 221 — Network Transfer Cost

Common cost-sensitive flows:

```text
cross-AZ
cross-Region
Internet egress
NAT processing
```

Design topology consciously.

# Part 222 — VPC Endpoints and Cost

For high-volume AWS service access from private subnets:

```text
private EC2 → endpoint → S3/DynamoDB/service
```

may reduce NAT usage and improve security.

Compare endpoint cost for interface endpoints versus NAT/data-transfer patterns.

# Part 223 — CloudFront and Egress Cost

CloudFront can:

```text
cache at edge
reduce origin requests
improve latency
```

and may change data-transfer economics.

Evaluate current pricing, not assumed rates.

# Part 224 — Single NAT vs Per-AZ NAT

Single NAT:

```text
lower hourly count
but
cross-AZ dependency/transfer
single-AZ failure impact
```

Per-AZ NAT:

```text
higher fixed cost
better AZ independence
possible lower cross-AZ transfer
```

Choose by availability and cost requirements.

# Part 225 — Cost Explorer

Use for:

```text
historical spend
service trends
account/tag analysis
forecast
```

# Part 226 — AWS Budgets

Use for:

```text
cost threshold
usage threshold
commitment utilization/coverage alerts
```

depending on budget type.

# Part 227 — Cost and Usage Report

Detailed line-item billing dataset.

Use for:

```text
FinOps
chargeback
custom analytics
unit economics
```

# Part 228 — Cost Allocation Tags

Example:

```text
Owner
Application
Environment
CostCenter
```

Activate appropriate tags for billing analysis.

# Part 229 — Architecture Scenario Method

Read SAA questions in this order:

```text
1. Identify requirement.
2. Identify constraints.
3. Eliminate technically wrong answers.
4. Compare remaining on:
   security
   resilience
   performance
   cost
   operational overhead
```

# Part 230 — Keyword: Minimum Operational Overhead

Favor:

```text
managed services
serverless
Auto Scaling
managed databases
S3
Lambda
Fargate
```

when they satisfy all requirements.

# Part 231 — Keyword: Most Cost Effective

Do not pick the cheapest-looking resource in isolation.

Consider:

```text
requests
transfer
management
duration
commitment
availability
```

# Part 232 — Keyword: Highly Available

Look for:

```text
Multi-AZ
load balancing
Auto Scaling
managed failover
redundant connectivity
```

# Part 233 — Keyword: Fault Tolerant

Fault tolerance implies continuing service through failures, often with stronger redundancy than simple recovery.

# Part 234 — Keyword: Decouple

Think:

```text
SQS
SNS
EventBridge
API Gateway
Step Functions
```

depending on communication pattern.

# Part 235 — Keyword: Global Low Latency

Potential services:

```text
CloudFront
Global Accelerator
Route 53 latency routing
multi-Region application
DynamoDB Global Tables
Aurora Global Database
```

depending on data/protocol.

# Part 236 — Keyword: Private Access to AWS Service

Think:

```text
VPC endpoint
PrivateLink
gateway endpoint
interface endpoint
```

instead of Internet/NAT.

# Part 237 — Keyword: Shared Linux Filesystem

Think:

```text
EFS
```

not EBS or S3.

# Part 238 — Keyword: High-Performance HPC Filesystem

Think:

```text
FSx for Lustre
```

# Part 239 — Keyword: Database Read Scaling

Think:

```text
read replica
Aurora replicas
cache
DAX
```

depending on database.

# Part 240 — Keyword: Database HA

Think:

```text
RDS Multi-AZ
Aurora multi-AZ storage/replicas
```

not simply read replicas.

# Part 241 — Keyword: Large Offline Transfer

Think:

```text
Snow Family
```

when network transfer is impractical.

# Part 242 — Keyword: Online Large File Migration

Think:

```text
DataSync
```

for supported file/object storage migration.

# Part 243 — Keyword: Existing SFTP Workflow

Think:

```text
AWS Transfer Family
```

rather than building an SFTP EC2 server.

# Part 244 — Keyword: API Activity Audit

Think:

```text
CloudTrail
```

# Part 245 — Keyword: Resource Configuration Compliance

Think:

```text
AWS Config
```

# Part 246 — Keyword: Application Metrics and Alarms

Think:

```text
CloudWatch
```

# Part 247 — Keyword: Distributed Request Trace

Think:

```text
AWS X-Ray
```

# Part 248 — Keyword: Secrets Rotation

Think:

```text
Secrets Manager
```

especially database/application credentials.

# Part 249 — Keyword: Encryption Key Control

Think:

```text
KMS
CloudHSM when dedicated HSM requirements
```

# Part 250 — Keyword: Web Layer Attack Filtering

Think:

```text
WAF
```

# Part 251 — Keyword: DDoS

Think:

```text
Shield
CloudFront
Route 53
AWS edge architecture
```

depending on question.

# Part 252 — Architecture Discovery with AWS CLI

Read-only commands help validate architecture:

```bash
aws sts get-caller-identity
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-route-tables
aws ec2 describe-security-groups
aws elbv2 describe-load-balancers
aws autoscaling describe-auto-scaling-groups
```

# Part 253 — Inspect VPCs

```bash
aws ec2 describe-vpcs \
  --query 'Vpcs[].{VpcId:VpcId,CIDR:CidrBlock,Default:IsDefault}' \
  --output table
```

# Part 254 — Inspect Subnets

```bash
aws ec2 describe-subnets \
  --query 'Subnets[].{Subnet:SubnetId,VPC:VpcId,AZ:AvailabilityZone,CIDR:CidrBlock}' \
  --output table
```

Look for balanced AZ distribution.

# Part 255 — Inspect Routes

```bash
aws ec2 describe-route-tables \
  --query 'RouteTables[].{RT:RouteTableId,Routes:Routes}' \
  --output json
```

Identify:

```text
IGW
NAT
TGW
peering
endpoint routes
```

# Part 256 — Inspect Security Groups

```bash
aws ec2 describe-security-groups \
  --query 'SecurityGroups[].{Name:GroupName,Id:GroupId,Vpc:VpcId}' \
  --output table
```

Then inspect ingress/egress for overly broad access.

# Part 257 — Inspect Load Balancers

```bash
aws elbv2 describe-load-balancers \
  --query 'LoadBalancers[].{Name:LoadBalancerName,Type:Type,Scheme:Scheme,Vpc:VpcId}' \
  --output table
```

# Part 258 — Inspect Auto Scaling

```bash
aws autoscaling describe-auto-scaling-groups \
  --query 'AutoScalingGroups[].{Name:AutoScalingGroupName,Min:MinSize,Desired:DesiredCapacity,Max:MaxSize}' \
  --output table
```

# Part 259 — Inspect RDS

```bash
aws rds describe-db-instances \
  --query 'DBInstances[].{DB:DBInstanceIdentifier,Engine:Engine,MultiAZ:MultiAZ,Class:DBInstanceClass}' \
  --output table
```

# Part 260 — Inspect S3 Public Access Controls

For a known bucket:

```bash
aws s3api get-public-access-block \
  --bucket BUCKET_NAME
```

Use read-only security checks before changing policy.

# Part 261 — Troubleshooting Method

Trace:

```text
DNS
 ↓
edge/CDN/WAF
 ↓
load balancer
 ↓
route
 ↓
security group/NACL
 ↓
compute
 ↓
application
 ↓
database/storage
 ↓
identity/dependency
```

# Part 262 — ALB 5xx Troubleshooting

Check:

```text
ALB metrics
target health
application logs
backend timeout
security groups
dependency latency
```

Differentiate:

```text
load balancer-generated errors
target-generated errors
```

# Part 263 — EC2 Unreachable

Check:

```text
instance state
subnet
route
public/private address
SG
NACL
OS firewall
sshd/RDP
SSM option
```

# Part 264 — Private EC2 Cannot Reach Internet

Check:

```text
private route → NAT
NAT subnet route → IGW
NAT healthy
SG egress
NACL
DNS
```

# Part 265 — RDS Unreachable

Check:

```text
DB state
subnet group
security group
route
DNS
port
credentials
TLS
connection limit
```

# Part 266 — S3 AccessDenied

Check:

```text
IAM policy
bucket policy
SCP
KMS key policy
VPC endpoint policy
Block Public Access
object ownership
```

Avoid solving by granting `s3:*`.

# Part 267 — Lambda Throttling

Check:

```text
account/function concurrency
reserved concurrency
downstream limits
retry behavior
queue backlog
```

# Part 268 — DynamoDB Throttling

Check:

```text
capacity mode
hot partition
partition key
provisioned capacity
autoscaling
request distribution
```

# Part 269 — SQS Backlog

Check:

```text
ApproximateNumberOfMessagesVisible
worker count
processing duration
visibility timeout
DLQ
downstream bottleneck
```

Scale workers on queue demand where appropriate.

# Part 270 — CloudFront Stale Content

Check:

```text
TTL
Cache-Control
cache key
invalidation
origin versioning
```

Prefer versioned asset names where practical.

# Part 271 — Security Architecture Review

Checklist:

```text
federated identities?
MFA?
least privilege?
private tiers?
WAF?
CloudTrail?
KMS?
secrets?
backup isolation?
SCPs?
```

# Part 272 — Reliability Architecture Review

Checklist:

```text
multiple AZs?
health checks?
self-healing?
state externalized?
DB failover?
queue buffering?
backup?
RPO/RTO?
quota planning?
```

# Part 273 — Performance Architecture Review

Checklist:

```text
right compute?
right storage?
cache?
read replicas?
CDN?
connection pooling?
partition strategy?
network placement?
```

# Part 274 — Cost Architecture Review

Checklist:

```text
right-size?
correct pricing model?
idle resources?
storage lifecycle?
egress?
NAT?
unnecessary replicas?
commitment?
serverless fit?
```

# Part 275 — Architecture Documentation

A professional design should include:

```text
requirements
assumptions
diagram
data flows
IAM
network
compute
storage
database
HA
DR
security
monitoring
cost
risks
decisions
```

# Part 276 — Architecture Decision Record

Example:

```text
Decision:
Use Aurora instead of self-managed MySQL on EC2.

Why:
managed HA
lower operations
read scaling
business RTO

Trade-off:
higher managed-service dependency/cost
```

Record why, not only what.

# Part 277 — Failure-Mode Table

Example:

```text
Failure         Detection        Response
EC2 failure     ALB/ASG health   replace
AZ failure      multi-AZ health  other AZ
DB primary      RDS health       failover
Region          Route53/ops      DR Region
```

# Part 278 — Architecture Cost Table

Estimate by category:

```text
Compute
Database
Storage
Requests
Data transfer
NAT
Load balancers
Backup
Observability
Support
```

Never claim "cost optimized" without modeling costs.

# Part 279 — Exam-Time Decision Process

For each question:

```text
underline MUST requirements
ignore irrelevant story details
identify architecture domain
eliminate violations
choose answer satisfying all requirements
prefer managed/simple when operational overhead matters
```

# Part 280 — Solutions Architect Final Mental Model

The correct architecture is not:

```text
the one with the most AWS services
```

It is:

```text
the simplest architecture that satisfies
security
resilience
performance
cost
and business requirements
with acceptable operational complexity.
```

---

# Supplemental Deep-Study Layer — AWS Certified Solutions Architect – Associate

> **Source distinction:** The complete uploaded course remains preserved. The sections below are supplemental engineering expansion added for deeper architecture, operations, CLI/configuration, failure analysis, labs, and production troubleshooting.

Focus: deeper architecture reasoning, failure domains, networking, data consistency, resilience, observability, security, FinOps, and production decision quality.

Learning sequence:

```text
Requirement
   ↓
Architecture Choice
   ↓
Identity / Network / Data Path
   ↓
CLI or Configuration Evidence
   ↓
Expected Behavior
   ↓
Failure Injection
   ↓
Troubleshooting
   ↓
Recovery
   ↓
Cost + Security + Reliability Review
```

## Advanced Deep Dive 1 — Requirement Traceability

### Concept and Detailed Explanation

A professional architecture should map every significant AWS resource to a business or non-functional requirement. Build a traceability matrix from requirement to service to verification evidence. This prevents diagrams from becoming collections of services with no reason to exist.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Business requirement
   ↓
Architecture decision
   ↓
AWS resource
   ↓
measurable evidence
   ↓
ADR / risk
```

### CLI / Configuration / Calculation

```bash
aws resourcegroupstaggingapi get-resources --output table 2>/dev/null || true
```

### Expected Behavior

Each production component has an owner, environment, purpose, and requirement.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Aurora Multi-AZ is justified by order-processing RTO, not simply because Aurora is popular.

### Troubleshooting Workflow

```text
missing decision
 ↓ identify requirement
 ↓ map service to requirement
 ↓ define evidence
 ↓ remove unnecessary component
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Maintain requirement-to-resource traceability and ADRs for high-impact decisions.

---

## Advanced Deep Dive 2 — Failure-Domain Mapping

### Concept and Detailed Explanation

High availability is meaningful only when replicas are isolated from the failure you are trying to tolerate. Map process, instance, host, Availability Zone, Region, account, identity, network, KMS, DNS, and third-party dependencies.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Region
 ├─ AZ-A → App-A
 └─ AZ-B → App-B
       ↓
 Regional DB
Shared: IAM / DNS / KMS / external API
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-subnets --query 'Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone,CIDR:CidrBlock}' --output table
```

### Expected Behavior

Replicas required for HA are spread across independent failure domains and shared dependencies are documented.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Two app instances span AZs but one NAT Gateway in AZ-A remains a zonal dependency.

### Troubleshooting Workflow

```text
claimed HA
 ↓ list replicas
 ↓ map AZ/Region/account
 ↓ identify shared dependency
 ↓ test failure path
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

State exactly which failure domain each redundancy mechanism protects against.

---

## Advanced Deep Dive 3 — Composite Availability Math

### Concept and Detailed Explanation

For serial required dependencies, end-to-end availability is approximately the product of the component availabilities when failures are independent. This helps architects understand why a chain of strong services can still produce a weaker user-facing SLO.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
User → DNS → Edge → App → DB
     all required
        ↓
multiply availability
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
vals=[0.9999,0.9999,0.9995,0.9995]
a=1
for v in vals:a*=v
print(f'{a*100:.5f}%')
PY
```

### Expected Behavior

The calculated user-path availability is lower than the strongest individual service.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

An internal 99.99% design target protects a 99.9% customer SLA.

### Troubleshooting Workflow

```text
SLO missed
 ↓ map request path
 ↓ quantify each dependency
 ↓ identify weakest/shared dependency
 ↓ redesign or add redundancy
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Model availability from the user journey, not one AWS SLA.

---

## Advanced Deep Dive 4 — Service Quotas as Reliability Dependencies

### Concept and Detailed Explanation

Quotas can block autoscaling, migration, or disaster recovery. Capacity design should include quota headroom in every account and Region used for production or DR.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Normal demand
 ↓ scale / failover
 ↓ service quota
   ├─ enough → continue
   └─ exceeded → recovery/scaling fails
```

### CLI / Configuration / Calculation

```bash
aws service-quotas list-services --output table 2>/dev/null | head -40
```

### Expected Behavior

Critical services have documented headroom for peak and failover demand.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Warm-standby Region has insufficient vCPU quota to scale to production size during a disaster.

### Troubleshooting Workflow

```text
launch fails
 ↓ quota?
 ↓ regional capacity?
 ↓ subnet IP?
 ↓ family availability?
 ↓ request increase/redesign
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Review quotas during design and game days, not during the outage.

---

## Advanced Deep Dive 5 — Subnet IP Capacity

### Concept and Detailed Explanation

Subnets are capacity pools for ENIs. EC2, load balancers, interface endpoints, ECS tasks, EKS pods, and other managed resources consume addresses. Small CIDRs can become a scale ceiling.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Subnet CIDR
 ↓ usable addresses
 ↓ ENI consumers
 ↓ AvailableIpAddressCount
 ↓ scaling/deployment capacity
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-subnets --query 'Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone,CIDR:CidrBlock,Free:AvailableIpAddressCount}' --output table
```

### Expected Behavior

Subnets have enough free addresses for peak scale plus deployment/failure overlap.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

ECS cannot launch more tasks even though Fargate quota is available because the private subnet is exhausted.

### Troubleshooting Workflow

```text
placement failure
 ↓ free subnet IPs
 ↓ ENI consumers
 ↓ deployment surge
 ↓ add/larger subnet
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Capacity-plan IP addresses like CPU, memory, and database connections.

---

## Advanced Deep Dive 6 — Enterprise CIDR Governance

### Concept and Detailed Explanation

Overlapping CIDRs make hybrid and multicloud routing difficult. Central IP allocation prevents independent teams from consuming address ranges that later collide with on-premises, acquisitions, or other clouds.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Enterprise address plan
 ├─ On-Prem
 ├─ AWS Prod
 ├─ AWS NonProd
 ├─ Other Cloud
 └─ Future/Acquisition
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-vpcs --query 'Vpcs[].{Vpc:VpcId,CIDR:CidrBlock}' --output table
```

### Expected Behavior

VPC ranges are unique and ownership is documented.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

An acquired company's 10.20.0.0/16 overlaps production, forcing temporary NAT-based migration.

### Troubleshooting Workflow

```text
hybrid route ambiguous
 ↓ compare CIDRs
 ↓ overlap?
 ↓ renumber/NAT/proxy
 ↓ central allocation
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Govern address allocation before creating many independent VPCs.

---

## Advanced Deep Dive 7 — IPv6 Dual Stack

### Concept and Detailed Explanation

IPv6 removes the basic need for NAT-based address conservation but not the need for routing, security groups, NACLs, DNS, egress policy, logging, and application support. IPv6 exposure must be reviewed separately from IPv4.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Client
 ↓ A / AAAA
dual-stack edge
 ↓
IPv4 / IPv6 workloads
 ↓
security/routing for each family
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-vpcs --query 'Vpcs[].{Vpc:VpcId,Ipv6:CidrBlockAssociationSet[].Ipv6CidrBlock}' --output json
```

### Expected Behavior

IPv6 routes and firewall rules are intentionally equivalent to the desired security posture.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

IPv4 is tightly restricted but an overly broad IPv6 ingress rule exposes the same service.

### Troubleshooting Workflow

```text
IPv6 issue
 ↓ AAAA resolution
 ↓ IPv6 route
 ↓ SG/NACL
 ↓ app bind address
 ↓ egress policy
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Review IPv4 and IPv6 paths independently.

---

## Advanced Deep Dive 8 — Route 53 Resolver Hybrid DNS

### Concept and Detailed Explanation

Hybrid DNS requires documented authority and forwarding. Resolver inbound/outbound endpoints and rules should connect on-premises DNS with private AWS zones without loops or conflicting authority.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
On-Prem DNS
   ↕ forwarding
Route 53 Resolver
   ↕
Private Hosted Zones / AWS service names
```

### CLI / Configuration / Calculation

```bash
aws route53resolver list-resolver-endpoints --output table 2>/dev/null || true
aws route53resolver list-resolver-rules --output table 2>/dev/null || true
```

### Expected Behavior

Private names resolve consistently from both AWS and on-premises clients.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A migrated app cannot find corporate LDAP because no outbound Resolver rule forwards the corporate zone.

### Troubleshooting Workflow

```text
DNS failure
 ↓ client resolver
 ↓ authority
 ↓ forwarding rule
 ↓ resolver endpoint
 ↓ route/SG
 ↓ cache/TTL
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Document DNS authority and forwarding just like IP routing.

---

## Advanced Deep Dive 9 — Transit Gateway Segmentation

### Concept and Detailed Explanation

Transit Gateway can provide separate routing domains, not just hub connectivity. Production, nonproduction, shared services, hybrid, and inspection attachments should not automatically share every route.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Prod VPCs ─→ TGW Prod RT
Dev VPCs  ─→ TGW Dev RT
On-Prem   ─→ TGW Hybrid RT
                 ↓
            Shared / Firewall
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-transit-gateway-route-tables --output table 2>/dev/null || true
aws ec2 describe-transit-gateway-attachments --output table 2>/dev/null || true
```

### Expected Behavior

Only approved segments learn each other's routes and return paths remain symmetric.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Sandbox VPC is attached but cannot reach production because it uses another TGW routing domain.

### Troubleshooting Workflow

```text
TGW flow fails
 ↓ attachment
 ↓ association
 ↓ propagation/static route
 ↓ VPC route
 ↓ return path
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use TGW route tables as segmentation controls.

---

## Advanced Deep Dive 10 — PrivateLink Service Publishing

### Concept and Detailed Explanation

PrivateLink is ideal when consumers need private access to one service without broad VPC-to-VPC routing. This reduces network transitivity and provider CIDR exposure.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Consumer VPC
 ↓ Interface Endpoint
PrivateLink
 ↓ Endpoint Service / NLB
 ↓ Provider application
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-vpc-endpoints --output table 2>/dev/null || true
aws ec2 describe-vpc-endpoint-services --output table 2>/dev/null || true
```

### Expected Behavior

Consumers can reach only the published service through private addressing.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A central payments API is exposed to many workload accounts without peering every VPC.

### Troubleshooting Workflow

```text
endpoint fails
 ↓ service acceptance
 ↓ endpoint state
 ↓ DNS
 ↓ SG
 ↓ NLB target health
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Choose PrivateLink for private service consumption, not general network connectivity.

---

## Advanced Deep Dive 11 — Gateway vs Interface Endpoint Economics

### Concept and Detailed Explanation

S3/DynamoDB gateway endpoints and interface endpoints for many other services use different routing and billing models. Endpoints can reduce NAT exposure and cost, but interface endpoints have their own fixed and variable charges.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Private workload
 ├─ S3/DynamoDB → gateway endpoint
 ├─ Secrets/ECR/etc → interface endpoint
 └─ Internet-only → NAT/egress
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-vpc-endpoints --query 'VpcEndpoints[].{Id:VpcEndpointId,Type:VpcEndpointType,Service:ServiceName}' --output table
```

### Expected Behavior

Private AWS-service traffic follows an intentionally selected cost/security path.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

S3 traffic bypasses NAT through a gateway endpoint while Secrets Manager uses interface endpoints.

### Troubleshooting Workflow

```text
cost/security review
 ↓ traffic volume
 ↓ endpoint supported?
 ↓ endpoint cost
 ↓ NAT cost/cross-AZ
 ↓ choose
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Model endpoint and NAT cost using expected traffic.

---

## Advanced Deep Dive 12 — KMS as Availability Dependency

### Concept and Detailed Explanation

Customer-managed KMS keys improve control but can make encrypted EBS, S3, RDS, backup, and secret data unavailable if disabled, deleted, or denied. Key management is therefore an availability concern too.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Application
 ↓ AWS service
 ↓ encrypted data
 ↓ KMS key state + policy
 ↓ decrypt/data key
```

### CLI / Configuration / Calculation

```bash
aws kms list-aliases --output table 2>/dev/null || true
aws kms describe-key --key-id <KEY_ID> 2>/dev/null || true
```

### Expected Behavior

Key administrators, key users, deletion controls, monitoring, and DR dependencies are defined.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

DR restore fails because the destination role lacks permission to use the backup KMS key.

### Troubleshooting Workflow

```text
encrypted data unavailable
 ↓ key ID/state
 ↓ IAM
 ↓ key policy/grant
 ↓ account/Region
 ↓ encryption context
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat KMS as security infrastructure and an application dependency.

---

## Advanced Deep Dive 13 — Secrets Rotation as Distributed Change

### Concept and Detailed Explanation

Rotating a credential changes both the provider and every consumer. Safe rotation requires consumer refresh behavior, overlap/version transition where appropriate, verification, and old-credential retirement.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Create new
 ↓ provider accepts
 ↓ consumers refresh
 ↓ verify
 ↓ retire old
```

### CLI / Configuration / Calculation

```bash
aws secretsmanager describe-secret --secret-id <SECRET_ID> 2>/dev/null || true
```

### Expected Behavior

Consumers continue authenticating throughout rotation and stale clients are detectable.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Database password rotates but one service caches the old value until its refresh interval.

### Troubleshooting Workflow

```text
post-rotation failure
 ↓ secret current version
 ↓ provider credential
 ↓ consumer cache
 ↓ network/IAM
 ↓ complete/rollback rotation
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design application secret refresh before enabling automatic rotation.

---

## Advanced Deep Dive 14 — S3 Authorization Layers

### Concept and Detailed Explanation

S3 access can involve IAM, bucket/access-point policies, Block Public Access, endpoint policy, SCPs, ownership settings, and KMS. Diagnose AccessDenied systematically.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Caller
 ↓ IAM/SCP
 ↓ bucket/access point
 ↓ Block Public Access
 ↓ endpoint policy
 ↓ KMS
 ↓ object
```

### CLI / Configuration / Calculation

```bash
aws s3api get-public-access-block --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-policy --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-encryption --bucket <BUCKET> 2>/dev/null || true
```

### Expected Behavior

An allow/deny can be explained without adding broad permissions.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Role has GetObject but KMS denies decrypt, causing S3 AccessDenied.

### Troubleshooting Workflow

```text
S3 AccessDenied
 ↓ caller/action/resource
 ↓ IAM/SCP
 ↓ bucket/access point
 ↓ endpoint/BPA
 ↓ KMS
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Troubleshoot S3 as layered authorization.

---

## Advanced Deep Dive 15 — EBS Snapshot Consistency

### Concept and Detailed Explanation

Block snapshots are not automatically application-consistent. Transactional applications may require checkpointing, filesystem freeze, native backup, or application quiescing before snapshot creation.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
App memory
 ↓ filesystem buffers
 ↓ EBS
 ↓ snapshot

quiesce → snapshot → resume
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-snapshots --owner-ids self --max-results 20 2>/dev/null || true
```

### Expected Behavior

Restore testing proves the application can recover and data is consistent.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A database snapshot restores but needs long crash recovery because writes were not quiesced.

### Troubleshooting Workflow

```text
restore problem
 ↓ volume attach
 ↓ filesystem integrity
 ↓ DB/application recovery
 ↓ native logs
 ↓ validate data
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Define required consistency level for every backup.

---

## Advanced Deep Dive 16 — RDS HA vs Read Scaling

### Concept and Detailed Explanation

High availability and read scaling are separate requirements. Multi-AZ deployments, readable standbys, and read replicas have different behaviors depending on the selected RDS/Aurora architecture.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
HA path:
App → writer ⇄ managed standby/failover

Read scale:
Reads → replicas
Writes → writer
```

### CLI / Configuration / Calculation

```bash
aws rds describe-db-instances --query 'DBInstances[].{DB:DBInstanceIdentifier,MultiAZ:MultiAZ,ReplicaSource:ReadReplicaSourceDBInstanceIdentifier}' --output table
```

### Expected Behavior

The database topology maps explicitly to HA, read scaling, and DR requirements.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Reporting is moved to a read replica rather than assuming the HA standby is a general read endpoint.

### Troubleshooting Workflow

```text
DB topology confusion
 ↓ HA requirement?
 ↓ read requirement?
 ↓ DR requirement?
 ↓ endpoint behavior
 ↓ failover/lag test
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Write separate requirements for availability and read scaling.

---

## Advanced Deep Dive 17 — Aurora Endpoint Strategy

### Concept and Detailed Explanation

Aurora applications should use logical writer/reader endpoints and robust reconnection. Hardcoding individual instance endpoints undermines managed failover.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Writes → writer endpoint → writer
Reads → reader endpoint → replicas
Failure → promotion + endpoint behavior
```

### CLI / Configuration / Calculation

```bash
aws rds describe-db-clusters --output table 2>/dev/null || true
```

### Expected Behavior

Applications reconnect after failover and read traffic uses replicas intentionally.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

App using cluster writer endpoint recovers after replica promotion, while a hardcoded instance hostname would not.

### Troubleshooting Workflow

```text
Aurora issue
 ↓ cluster event
 ↓ endpoint used
 ↓ DNS/client cache
 ↓ pool/retry
 ↓ replica health
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use logical endpoints and test planned failover.

---

## Advanced Deep Dive 18 — DynamoDB Hot-Key Analysis

### Concept and Detailed Explanation

Aggregate table capacity can be healthy while a hot partition key throttles. Key cardinality, traffic distribution, item size, GSIs, and access patterns are core architecture concerns.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Requests
 ↓ partition key
 ↓ hash
Partitions A/B/C
hot A → throttling
```

### CLI / Configuration / Calculation

```bash
aws dynamodb describe-table --table-name <TABLE> 2>/dev/null || true
aws cloudwatch list-metrics --namespace AWS/DynamoDB 2>/dev/null | head -40
```

### Expected Behavior

Traffic distributes across enough partition keys to meet demand.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Using one key such as TODAY for all manufacturing events creates concentrated writes.

### Troubleshooting Workflow

```text
throttles
 ↓ capacity mode
 ↓ key distribution
 ↓ GSI
 ↓ hot item/partition
 ↓ redesign/shard
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design DynamoDB from access patterns and traffic distribution.

---

## Advanced Deep Dive 19 — DynamoDB Conditional Writes

### Concept and Detailed Explanation

Distributed clients retry and race. Conditional writes support create-if-absent and optimistic concurrency atomically, avoiding read-then-write races.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Request
 ↓ conditional Put/Update
condition true → commit
false → duplicate/stale rejection
```

### CLI / Configuration / Calculation

```bash
# Conceptual condition:
# attribute_not_exists(request_id)
aws dynamodb describe-table --table-name <TABLE> 2>/dev/null || true
```

### Expected Behavior

Duplicate request retries do not create duplicate business effects.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Payment callback uses transaction ID as an idempotency key.

### Troubleshooting Workflow

```text
conditional failure
 ↓ duplicate?
 ↓ stale version?
 ↓ read current state
 ↓ retry/merge/reject
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Push concurrency checks into atomic database operations.

---

## Advanced Deep Dive 20 — SQS Visibility Timeout

### Concept and Detailed Explanation

Visibility timeout is a processing lease. Too short creates duplicate processing; too long delays retry after worker failure. Set it using measured processing-duration distribution.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
receive
 ↓ hidden lease
 ↓ success → delete
failure/timeout → visible again
```

### CLI / Configuration / Calculation

```bash
aws sqs get-queue-attributes --queue-url <URL> --attribute-names VisibilityTimeout 2>/dev/null || true
```

### Expected Behavior

Normal jobs finish before visibility expiry and failed jobs retry predictably.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Eight-minute jobs stop duplicating after visibility is set from p99 duration and extended where needed.

### Troubleshooting Workflow

```text
duplicate work
 ↓ processing p95/p99
 ↓ visibility
 ↓ delete timing
 ↓ idempotency
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Set visibility timeout from real processing time and keep consumers idempotent.

---

## Advanced Deep Dive 21 — SQS FIFO Message Groups

### Concept and Detailed Explanation

FIFO ordering is scoped to message groups. Using one group for all events serializes throughput; partition ordering by business entity when possible.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Group A: A1 → A2 → A3
Group B: B1 → B2
A and B can progress independently
```

### CLI / Configuration / Calculation

```bash
aws sqs get-queue-attributes --queue-url <URL> --attribute-names FifoQueue 2>/dev/null || true
```

### Expected Behavior

Only entities requiring ordering are serialized.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Order ID is used as message-group ID so each order is ordered but many orders process in parallel.

### Troubleshooting Workflow

```text
FIFO throughput low
 ↓ group cardinality
 ↓ consumer concurrency
 ↓ deduplication
 ↓ redesign grouping
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Choose the narrowest domain that truly requires ordering.

---

## Advanced Deep Dive 22 — Event Schema Governance

### Concept and Detailed Explanation

Event-driven architecture decouples routing but not contracts. Events need stable envelopes, schema version, owner, idempotency identity, compatibility policy, and replay expectations.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Producer
 ↓ event bus
 ├─ Consumer A
 ├─ Consumer B
 └─ archive/replay
```

### CLI / Configuration / Calculation

```bash
aws events list-event-buses --output table 2>/dev/null || true
aws events list-rules --output table 2>/dev/null || true
```

### Expected Behavior

Consumers evolve independently without relying on undocumented fields.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

`OrderCreated` includes event ID, schema version, aggregate ID, and timestamp.

### Troubleshooting Workflow

```text
consumer broke
 ↓ schema version
 ↓ rule pattern
 ↓ payload compatibility
 ↓ replay/adapter
 ↓ fix contract
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat event schemas as versioned APIs.

---

## Advanced Deep Dive 23 — Step Functions Compensation

### Concept and Detailed Explanation

Distributed workflows cannot usually roll back atomically. Distinguish transient retry from business failure and define compensating actions for already-completed steps.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Reserve stock
 ↓ charge
 ↓ shipping fails
 ↓ refund
 ↓ release stock
```

### CLI / Configuration / Calculation

```bash
aws stepfunctions list-state-machines --output table 2>/dev/null || true
```

### Expected Behavior

Workflow history shows completed, failed, retried, and compensated actions.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A booking workflow refunds after downstream allocation fails.

### Troubleshooting Workflow

```text
workflow failure
 ↓ state history
 ↓ transient/business?
 ↓ committed side effects
 ↓ compensate/forward fix
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design compensation and idempotency before orchestrating irreversible work.

---

## Advanced Deep Dive 24 — Lambda Concurrency and Downstream Capacity

### Concept and Detailed Explanation

Serverless compute can scale faster than relational databases or third-party APIs. Reserved concurrency, queues, RDS Proxy, pooling, and throttling protect downstream systems.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Burst
 ↓ Lambda concurrency
 ↓ RDS Proxy / queue / rate limit
 ↓ finite backend
```

### CLI / Configuration / Calculation

```bash
aws lambda get-account-settings 2>/dev/null || true
aws lambda list-functions --query 'Functions[].{Name:FunctionName,Timeout:Timeout,Memory:MemorySize}' --output table
```

### Expected Behavior

Function scale cannot exceed safe downstream capacity for protected paths.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A DB-using Lambda function is capped while other stateless functions remain elastic.

### Troubleshooting Workflow

```text
backend saturated
 ↓ Lambda concurrency
 ↓ event source backlog
 ↓ proxy/pool
 ↓ DB/API limits
 ↓ cap/buffer
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Scale the whole dependency chain, not only compute.

---

## Advanced Deep Dive 25 — ECS Capacity Provider Strategy

### Concept and Detailed Explanation

ECS can combine reliable baseline capacity with lower-cost interruptible pools. Capacity providers should be selected according to workload interruption tolerance and specialized hardware requirements.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
ECS service
 ↓ provider strategy
 ├─ reliable baseline
 ├─ Spot burst
 └─ specialized EC2
```

### CLI / Configuration / Calculation

```bash
aws ecs describe-capacity-providers --output table 2>/dev/null || true
```

### Expected Behavior

Critical service capacity survives interruption of discounted pools.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Stateless workers use Spot for burst while keeping an on-demand baseline.

### Troubleshooting Workflow

```text
task placement/interruption
 ↓ provider
 ↓ quota/capacity
 ↓ workload idempotent?
 ↓ queue/recovery
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use mixed capacity only when the workload can tolerate each pool's behavior.

---

## Advanced Deep Dive 26 — CloudFront Cache-Key Design

### Concept and Detailed Explanation

Cache keys should vary only on request attributes that actually change the response. Forwarding every cookie, header, or query parameter reduces hit ratio and increases origin cost.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Viewer request
 ↓ cache key
 hit → edge
 miss → origin → cache fill
```

### CLI / Configuration / Calculation

```bash
aws cloudfront list-distributions --output table 2>/dev/null || true
```

### Expected Behavior

Static/cacheable responses achieve a high hit ratio while personalized paths remain correct.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Static assets ignore irrelevant cookies; authenticated API responses are not broadly cached.

### Troubleshooting Workflow

```text
origin load high
 ↓ hit ratio
 ↓ cache policy
 ↓ headers/cookies/query
 ↓ TTL
 ↓ origin behavior
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Keep cache keys minimal and intentional.

---

## Advanced Deep Dive 27 — Autoscaling Metric Selection

### Concept and Detailed Explanation

CPU is useful only when it correlates with demand. Queue depth per worker, requests per target, latency, concurrency, and business metrics can be better control signals.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Demand
 ↓ metric
 ↓ scaling policy
 ↓ capacity
 ↓ metric changes
 ↺
```

### CLI / Configuration / Calculation

```bash
aws autoscaling describe-policies --auto-scaling-group-name <ASG> 2>/dev/null || true
```

### Expected Behavior

Capacity responds to the actual bottleneck without oscillation.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Async workers scale on queue backlog rather than CPU because they spend time waiting on remote APIs.

### Troubleshooting Workflow

```text
scaling wrong
 ↓ metric-demand correlation
 ↓ warmup/cooldown
 ↓ min/max
 ↓ downstream limits
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Choose the metric closest to demand/backlog.

---

## Advanced Deep Dive 28 — Scale-In and Graceful Drain

### Concept and Detailed Explanation

Scale-in removes compute. Applications should stop receiving new work, drain connections, finish or hand off jobs, persist state, and exit before termination.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
select instance
 ↓ deregister/drain
 ↓ finish work
 ↓ persist/release
 ↓ terminate
```

### CLI / Configuration / Calculation

```bash
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names <ASG> 2>/dev/null || true
```

### Expected Behavior

Routine scale-in does not drop unique work or in-flight requests.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Worker lifecycle hook stops polling SQS, completes current message, then allows termination.

### Troubleshooting Workflow

```text
scale-in loss
 ↓ local state?
 ↓ traffic drain?
 ↓ queue ack?
 ↓ lifecycle hook?
 ↓ idempotent retry?
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design graceful termination before enabling aggressive scale-in.

---

## Advanced Deep Dive 29 — DR Dependency Completeness

### Concept and Detailed Explanation

A secondary Region is not ready just because data is replicated. Artifacts, images, IAM, KMS, secrets, certificates, DNS, networking, quotas, monitoring, and external integrations must also be available.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
DR Region
 ├─ network
 ├─ compute/artifacts
 ├─ data
 ├─ IAM/KMS/secrets
 ├─ DNS/certs
 ├─ quotas
 └─ monitoring
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-vpcs --region <DR_REGION> 2>/dev/null || true
aws backup list-backup-vaults --region <DR_REGION> 2>/dev/null || true
```

### Expected Behavior

A game day proves the complete workload can serve a business transaction in DR.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Backups exist but container image and KMS access are missing in the DR Region.

### Troubleshooting Workflow

```text
DR failure
 ↓ missing dependency?
 ↓ artifact/data/key/identity/quota/DNS
 ↓ fix bill of materials
 ↓ retest
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Maintain a complete DR dependency inventory.

---

## Advanced Deep Dive 30 — RTO Decomposition

### Concept and Detailed Explanation

RTO includes detection, declaration, scaling/provisioning, restore/promotion, DNS/routing, startup, cache warm-up, and business validation. Infrastructure failover time alone is not RTO.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
failure
 ↓ detect
 ↓ declare
 ↓ recover data
 ↓ scale/provision
 ↓ route
 ↓ validate
 = actual RTO
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
steps={'detect':5,'declare':5,'recover':15,'scale':10,'dns':5,'validate':10}
print(sum(steps.values()),'minutes')
PY
```

### Expected Behavior

Each recovery phase is measured and the total meets the business target.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A warm standby scales quickly but manual application validation causes RTO miss.

### Troubleshooting Workflow

```text
RTO miss
 ↓ time each phase
 ↓ largest delay
 ↓ automate/pre-stage
 ↓ repeat test
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Measure RTO from outage start to successful business transaction.

---

## Advanced Deep Dive 31 — Backup Administrative Isolation

### Concept and Detailed Explanation

Cyber recovery requires backup copies that compromised production administrators cannot easily delete. Use separate accounts, restricted vault policies, retention controls, and tested restore roles.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Production
 ↓ backup copy
Backup/Security account
 ↓ protected vault
 ↓ restore test
```

### CLI / Configuration / Calculation

```bash
aws backup list-backup-vaults --output table 2>/dev/null || true
```

### Expected Behavior

Production credential compromise does not destroy every recovery point.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Cross-account backup remains available after a production admin role is compromised.

### Troubleshooting Workflow

```text
backup at risk
 ↓ delete authority
 ↓ vault policy/lock
 ↓ KMS admin
 ↓ cross-account copy
 ↓ restore
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Separate backup administration from workload administration.

---

## Advanced Deep Dive 32 — Well-Architected Risk Prioritization

### Concept and Detailed Explanation

Architecture reviews generate many findings. Prioritize by customer impact, likelihood, detectability, recovery difficulty, and remediation cost rather than treating all recommendations equally.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Finding
 ↓ impact + likelihood
 ↓ detect/recover difficulty
 ↓ priority
 ↓ owner/date
 ↓ verification
```

### CLI / Configuration / Calculation

```bash
aws cloudwatch describe-alarms --output table 2>/dev/null || true
aws configservice describe-config-rules --output table 2>/dev/null || true
```

### Expected Behavior

High-risk gaps receive owners, deadlines, and verification criteria.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Missing backups are fixed before a minor right-sizing opportunity.

### Troubleshooting Workflow

```text
too many findings
 ↓ business impact
 ↓ probability
 ↓ recoverability
 ↓ prioritize
 ↓ track closure
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use risk-based prioritization, not checklist equality.

---

## Advanced Deep Dive 33 — Cost per Business Transaction

### Concept and Detailed Explanation

Normalize cloud spend by business output such as order, API call, active user, GB processed, or manufacturing batch. Absolute spend can rise while efficiency improves.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
AWS cost
 ÷ business output
 = unit economics
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
cost=42000
orders=350000
print(round(cost/orders,4))
PY
```

### Expected Behavior

Engineering and finance can distinguish growth from inefficiency.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Spend rises 20% but orders rise 50%, reducing cost per order.

### Troubleshooting Workflow

```text
cost concern
 ↓ absolute spend
 ↓ business volume
 ↓ unit cost
 ↓ service/usage driver
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Track a business-relevant unit-cost metric for major workloads.

---

## Advanced Deep Dive 34 — Retry Storm Prevention

### Concept and Detailed Explanation

Retries can increase resilience or amplify outages. Use bounded retries, exponential backoff, jitter, and idempotency; avoid multiple layers retrying the same failure aggressively.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
failure
 ↓ bounded retry
 ↓ exponential delay + jitter
 ↓ recover
 or
 fail/queue
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
import random
for i in range(5):
    print(round((2**i)+random.random(),2))
PY
```

### Expected Behavior

Transient faults recover without synchronized retry storms.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Thousands of workers back off from a throttled database rather than retrying immediately.

### Troubleshooting Workflow

```text
dependency overloaded
 ↓ retry rate
 ↓ timeout
 ↓ multiple retry layers?
 ↓ backoff/jitter
 ↓ queue/circuit breaker
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Retry only transient errors and cap total retry time.

---

## Advanced Deep Dive 35 — Circuit Breaker and Graceful Degradation

### Concept and Detailed Explanation

A failing optional dependency should not consume all application capacity. Circuit breakers fail fast after repeated errors and allow recovery probes later.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
CLOSED → calls flow
 failures
 ↓
OPEN → fail fast
 wait
 ↓
HALF-OPEN → test
 success → CLOSED
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
timeout=500ms
failure_threshold=10
open_duration=30s
fallback=omit_recommendations
EOF
```

### Expected Behavior

Core service remains usable when optional dependencies fail.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Recommendation API failure does not take down checkout.

### Troubleshooting Workflow

```text
circuit opens
 ↓ dependency health
 ↓ timeout
 ↓ threshold
 ↓ fallback
 ↓ recovery probe
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Classify critical vs optional dependencies and design degradation.

---

## Advanced Deep Dive 36 — Architecture Documentation as Operational Asset

### Concept and Detailed Explanation

Diagrams should expose trust boundaries, AZs/subnets, ingress/egress, data stores, identities, dependencies, and failure paths. Version documentation with infrastructure code.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Requirements
 ↓ architecture
 ↓ data flows
 ↓ IAM/network
 ↓ failure/DR
 ↓ runbooks/ADRs
```

### CLI / Configuration / Calculation

```bash
mkdir -p architecture/decisions architecture/runbooks
touch architecture/ARCHITECTURE.md architecture/DATA_FLOWS.md
```

### Expected Behavior

On-call engineers can understand request flow and ownership quickly.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

During an incident the team immediately sees the private endpoint and SG between worker and S3.

### Troubleshooting Workflow

```text
diagram stale
 ↓ compare CLI/IaC
 ↓ identify drift
 ↓ update source
 ↓ assign owner/review date
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Version architecture documentation alongside IaC.

---

# Supplemental Hands-on Lab Series — AWS Certified Solutions Architect – Associate

## Enhanced Lab 1 — Requirement Traceability

### Objective

Turn **Requirement Traceability** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws resourcegroupstaggingapi get-resources --output table 2>/dev/null || true
```

### Expected Result

Each production component has an owner, environment, purpose, and requirement.

### Troubleshooting Path

```text
missing decision
 ↓ identify requirement
 ↓ map service to requirement
 ↓ define evidence
 ↓ remove unnecessary component
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 2 — Failure-Domain Mapping

### Objective

Turn **Failure-Domain Mapping** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-subnets --query 'Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone,CIDR:CidrBlock}' --output table
```

### Expected Result

Replicas required for HA are spread across independent failure domains and shared dependencies are documented.

### Troubleshooting Path

```text
claimed HA
 ↓ list replicas
 ↓ map AZ/Region/account
 ↓ identify shared dependency
 ↓ test failure path
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 3 — Composite Availability Math

### Objective

Turn **Composite Availability Math** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
python3 - <<'PY'
vals=[0.9999,0.9999,0.9995,0.9995]
a=1
for v in vals:a*=v
print(f'{a*100:.5f}%')
PY
```

### Expected Result

The calculated user-path availability is lower than the strongest individual service.

### Troubleshooting Path

```text
SLO missed
 ↓ map request path
 ↓ quantify each dependency
 ↓ identify weakest/shared dependency
 ↓ redesign or add redundancy
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 4 — Service Quotas as Reliability Dependencies

### Objective

Turn **Service Quotas as Reliability Dependencies** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws service-quotas list-services --output table 2>/dev/null | head -40
```

### Expected Result

Critical services have documented headroom for peak and failover demand.

### Troubleshooting Path

```text
launch fails
 ↓ quota?
 ↓ regional capacity?
 ↓ subnet IP?
 ↓ family availability?
 ↓ request increase/redesign
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 5 — Subnet IP Capacity

### Objective

Turn **Subnet IP Capacity** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-subnets --query 'Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone,CIDR:CidrBlock,Free:AvailableIpAddressCount}' --output table
```

### Expected Result

Subnets have enough free addresses for peak scale plus deployment/failure overlap.

### Troubleshooting Path

```text
placement failure
 ↓ free subnet IPs
 ↓ ENI consumers
 ↓ deployment surge
 ↓ add/larger subnet
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 6 — Enterprise CIDR Governance

### Objective

Turn **Enterprise CIDR Governance** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-vpcs --query 'Vpcs[].{Vpc:VpcId,CIDR:CidrBlock}' --output table
```

### Expected Result

VPC ranges are unique and ownership is documented.

### Troubleshooting Path

```text
hybrid route ambiguous
 ↓ compare CIDRs
 ↓ overlap?
 ↓ renumber/NAT/proxy
 ↓ central allocation
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 7 — IPv6 Dual Stack

### Objective

Turn **IPv6 Dual Stack** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-vpcs --query 'Vpcs[].{Vpc:VpcId,Ipv6:CidrBlockAssociationSet[].Ipv6CidrBlock}' --output json
```

### Expected Result

IPv6 routes and firewall rules are intentionally equivalent to the desired security posture.

### Troubleshooting Path

```text
IPv6 issue
 ↓ AAAA resolution
 ↓ IPv6 route
 ↓ SG/NACL
 ↓ app bind address
 ↓ egress policy
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 8 — Route 53 Resolver Hybrid DNS

### Objective

Turn **Route 53 Resolver Hybrid DNS** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws route53resolver list-resolver-endpoints --output table 2>/dev/null || true
aws route53resolver list-resolver-rules --output table 2>/dev/null || true
```

### Expected Result

Private names resolve consistently from both AWS and on-premises clients.

### Troubleshooting Path

```text
DNS failure
 ↓ client resolver
 ↓ authority
 ↓ forwarding rule
 ↓ resolver endpoint
 ↓ route/SG
 ↓ cache/TTL
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 9 — Transit Gateway Segmentation

### Objective

Turn **Transit Gateway Segmentation** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-transit-gateway-route-tables --output table 2>/dev/null || true
aws ec2 describe-transit-gateway-attachments --output table 2>/dev/null || true
```

### Expected Result

Only approved segments learn each other's routes and return paths remain symmetric.

### Troubleshooting Path

```text
TGW flow fails
 ↓ attachment
 ↓ association
 ↓ propagation/static route
 ↓ VPC route
 ↓ return path
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 10 — PrivateLink Service Publishing

### Objective

Turn **PrivateLink Service Publishing** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-vpc-endpoints --output table 2>/dev/null || true
aws ec2 describe-vpc-endpoint-services --output table 2>/dev/null || true
```

### Expected Result

Consumers can reach only the published service through private addressing.

### Troubleshooting Path

```text
endpoint fails
 ↓ service acceptance
 ↓ endpoint state
 ↓ DNS
 ↓ SG
 ↓ NLB target health
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 11 — Gateway vs Interface Endpoint Economics

### Objective

Turn **Gateway vs Interface Endpoint Economics** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-vpc-endpoints --query 'VpcEndpoints[].{Id:VpcEndpointId,Type:VpcEndpointType,Service:ServiceName}' --output table
```

### Expected Result

Private AWS-service traffic follows an intentionally selected cost/security path.

### Troubleshooting Path

```text
cost/security review
 ↓ traffic volume
 ↓ endpoint supported?
 ↓ endpoint cost
 ↓ NAT cost/cross-AZ
 ↓ choose
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 12 — KMS as Availability Dependency

### Objective

Turn **KMS as Availability Dependency** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws kms list-aliases --output table 2>/dev/null || true
aws kms describe-key --key-id <KEY_ID> 2>/dev/null || true
```

### Expected Result

Key administrators, key users, deletion controls, monitoring, and DR dependencies are defined.

### Troubleshooting Path

```text
encrypted data unavailable
 ↓ key ID/state
 ↓ IAM
 ↓ key policy/grant
 ↓ account/Region
 ↓ encryption context
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 13 — Secrets Rotation as Distributed Change

### Objective

Turn **Secrets Rotation as Distributed Change** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws secretsmanager describe-secret --secret-id <SECRET_ID> 2>/dev/null || true
```

### Expected Result

Consumers continue authenticating throughout rotation and stale clients are detectable.

### Troubleshooting Path

```text
post-rotation failure
 ↓ secret current version
 ↓ provider credential
 ↓ consumer cache
 ↓ network/IAM
 ↓ complete/rollback rotation
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 14 — S3 Authorization Layers

### Objective

Turn **S3 Authorization Layers** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws s3api get-public-access-block --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-policy --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-encryption --bucket <BUCKET> 2>/dev/null || true
```

### Expected Result

An allow/deny can be explained without adding broad permissions.

### Troubleshooting Path

```text
S3 AccessDenied
 ↓ caller/action/resource
 ↓ IAM/SCP
 ↓ bucket/access point
 ↓ endpoint/BPA
 ↓ KMS
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 15 — EBS Snapshot Consistency

### Objective

Turn **EBS Snapshot Consistency** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-snapshots --owner-ids self --max-results 20 2>/dev/null || true
```

### Expected Result

Restore testing proves the application can recover and data is consistent.

### Troubleshooting Path

```text
restore problem
 ↓ volume attach
 ↓ filesystem integrity
 ↓ DB/application recovery
 ↓ native logs
 ↓ validate data
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 16 — RDS HA vs Read Scaling

### Objective

Turn **RDS HA vs Read Scaling** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws rds describe-db-instances --query 'DBInstances[].{DB:DBInstanceIdentifier,MultiAZ:MultiAZ,ReplicaSource:ReadReplicaSourceDBInstanceIdentifier}' --output table
```

### Expected Result

The database topology maps explicitly to HA, read scaling, and DR requirements.

### Troubleshooting Path

```text
DB topology confusion
 ↓ HA requirement?
 ↓ read requirement?
 ↓ DR requirement?
 ↓ endpoint behavior
 ↓ failover/lag test
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 17 — Aurora Endpoint Strategy

### Objective

Turn **Aurora Endpoint Strategy** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws rds describe-db-clusters --output table 2>/dev/null || true
```

### Expected Result

Applications reconnect after failover and read traffic uses replicas intentionally.

### Troubleshooting Path

```text
Aurora issue
 ↓ cluster event
 ↓ endpoint used
 ↓ DNS/client cache
 ↓ pool/retry
 ↓ replica health
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 18 — DynamoDB Hot-Key Analysis

### Objective

Turn **DynamoDB Hot-Key Analysis** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws dynamodb describe-table --table-name <TABLE> 2>/dev/null || true
aws cloudwatch list-metrics --namespace AWS/DynamoDB 2>/dev/null | head -40
```

### Expected Result

Traffic distributes across enough partition keys to meet demand.

### Troubleshooting Path

```text
throttles
 ↓ capacity mode
 ↓ key distribution
 ↓ GSI
 ↓ hot item/partition
 ↓ redesign/shard
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 19 — DynamoDB Conditional Writes

### Objective

Turn **DynamoDB Conditional Writes** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
# Conceptual condition:
# attribute_not_exists(request_id)
aws dynamodb describe-table --table-name <TABLE> 2>/dev/null || true
```

### Expected Result

Duplicate request retries do not create duplicate business effects.

### Troubleshooting Path

```text
conditional failure
 ↓ duplicate?
 ↓ stale version?
 ↓ read current state
 ↓ retry/merge/reject
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 20 — SQS Visibility Timeout

### Objective

Turn **SQS Visibility Timeout** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws sqs get-queue-attributes --queue-url <URL> --attribute-names VisibilityTimeout 2>/dev/null || true
```

### Expected Result

Normal jobs finish before visibility expiry and failed jobs retry predictably.

### Troubleshooting Path

```text
duplicate work
 ↓ processing p95/p99
 ↓ visibility
 ↓ delete timing
 ↓ idempotency
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 21 — SQS FIFO Message Groups

### Objective

Turn **SQS FIFO Message Groups** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws sqs get-queue-attributes --queue-url <URL> --attribute-names FifoQueue 2>/dev/null || true
```

### Expected Result

Only entities requiring ordering are serialized.

### Troubleshooting Path

```text
FIFO throughput low
 ↓ group cardinality
 ↓ consumer concurrency
 ↓ deduplication
 ↓ redesign grouping
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 22 — Event Schema Governance

### Objective

Turn **Event Schema Governance** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws events list-event-buses --output table 2>/dev/null || true
aws events list-rules --output table 2>/dev/null || true
```

### Expected Result

Consumers evolve independently without relying on undocumented fields.

### Troubleshooting Path

```text
consumer broke
 ↓ schema version
 ↓ rule pattern
 ↓ payload compatibility
 ↓ replay/adapter
 ↓ fix contract
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 23 — Step Functions Compensation

### Objective

Turn **Step Functions Compensation** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws stepfunctions list-state-machines --output table 2>/dev/null || true
```

### Expected Result

Workflow history shows completed, failed, retried, and compensated actions.

### Troubleshooting Path

```text
workflow failure
 ↓ state history
 ↓ transient/business?
 ↓ committed side effects
 ↓ compensate/forward fix
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 24 — Lambda Concurrency and Downstream Capacity

### Objective

Turn **Lambda Concurrency and Downstream Capacity** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws lambda get-account-settings 2>/dev/null || true
aws lambda list-functions --query 'Functions[].{Name:FunctionName,Timeout:Timeout,Memory:MemorySize}' --output table
```

### Expected Result

Function scale cannot exceed safe downstream capacity for protected paths.

### Troubleshooting Path

```text
backend saturated
 ↓ Lambda concurrency
 ↓ event source backlog
 ↓ proxy/pool
 ↓ DB/API limits
 ↓ cap/buffer
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 25 — ECS Capacity Provider Strategy

### Objective

Turn **ECS Capacity Provider Strategy** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ecs describe-capacity-providers --output table 2>/dev/null || true
```

### Expected Result

Critical service capacity survives interruption of discounted pools.

### Troubleshooting Path

```text
task placement/interruption
 ↓ provider
 ↓ quota/capacity
 ↓ workload idempotent?
 ↓ queue/recovery
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 26 — CloudFront Cache-Key Design

### Objective

Turn **CloudFront Cache-Key Design** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws cloudfront list-distributions --output table 2>/dev/null || true
```

### Expected Result

Static/cacheable responses achieve a high hit ratio while personalized paths remain correct.

### Troubleshooting Path

```text
origin load high
 ↓ hit ratio
 ↓ cache policy
 ↓ headers/cookies/query
 ↓ TTL
 ↓ origin behavior
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 27 — Autoscaling Metric Selection

### Objective

Turn **Autoscaling Metric Selection** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws autoscaling describe-policies --auto-scaling-group-name <ASG> 2>/dev/null || true
```

### Expected Result

Capacity responds to the actual bottleneck without oscillation.

### Troubleshooting Path

```text
scaling wrong
 ↓ metric-demand correlation
 ↓ warmup/cooldown
 ↓ min/max
 ↓ downstream limits
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 28 — Scale-In and Graceful Drain

### Objective

Turn **Scale-In and Graceful Drain** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names <ASG> 2>/dev/null || true
```

### Expected Result

Routine scale-in does not drop unique work or in-flight requests.

### Troubleshooting Path

```text
scale-in loss
 ↓ local state?
 ↓ traffic drain?
 ↓ queue ack?
 ↓ lifecycle hook?
 ↓ idempotent retry?
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 29 — DR Dependency Completeness

### Objective

Turn **DR Dependency Completeness** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws ec2 describe-vpcs --region <DR_REGION> 2>/dev/null || true
aws backup list-backup-vaults --region <DR_REGION> 2>/dev/null || true
```

### Expected Result

A game day proves the complete workload can serve a business transaction in DR.

### Troubleshooting Path

```text
DR failure
 ↓ missing dependency?
 ↓ artifact/data/key/identity/quota/DNS
 ↓ fix bill of materials
 ↓ retest
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 30 — RTO Decomposition

### Objective

Turn **RTO Decomposition** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
python3 - <<'PY'
steps={'detect':5,'declare':5,'recover':15,'scale':10,'dns':5,'validate':10}
print(sum(steps.values()),'minutes')
PY
```

### Expected Result

Each recovery phase is measured and the total meets the business target.

### Troubleshooting Path

```text
RTO miss
 ↓ time each phase
 ↓ largest delay
 ↓ automate/pre-stage
 ↓ repeat test
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 31 — Backup Administrative Isolation

### Objective

Turn **Backup Administrative Isolation** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws backup list-backup-vaults --output table 2>/dev/null || true
```

### Expected Result

Production credential compromise does not destroy every recovery point.

### Troubleshooting Path

```text
backup at risk
 ↓ delete authority
 ↓ vault policy/lock
 ↓ KMS admin
 ↓ cross-account copy
 ↓ restore
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 32 — Well-Architected Risk Prioritization

### Objective

Turn **Well-Architected Risk Prioritization** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
aws cloudwatch describe-alarms --output table 2>/dev/null || true
aws configservice describe-config-rules --output table 2>/dev/null || true
```

### Expected Result

High-risk gaps receive owners, deadlines, and verification criteria.

### Troubleshooting Path

```text
too many findings
 ↓ business impact
 ↓ probability
 ↓ recoverability
 ↓ prioritize
 ↓ track closure
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 33 — Cost per Business Transaction

### Objective

Turn **Cost per Business Transaction** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
python3 - <<'PY'
cost=42000
orders=350000
print(round(cost/orders,4))
PY
```

### Expected Result

Engineering and finance can distinguish growth from inefficiency.

### Troubleshooting Path

```text
cost concern
 ↓ absolute spend
 ↓ business volume
 ↓ unit cost
 ↓ service/usage driver
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 34 — Retry Storm Prevention

### Objective

Turn **Retry Storm Prevention** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
python3 - <<'PY'
import random
for i in range(5):
    print(round((2**i)+random.random(),2))
PY
```

### Expected Result

Transient faults recover without synchronized retry storms.

### Troubleshooting Path

```text
dependency overloaded
 ↓ retry rate
 ↓ timeout
 ↓ multiple retry layers?
 ↓ backoff/jitter
 ↓ queue/circuit breaker
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 35 — Circuit Breaker and Graceful Degradation

### Objective

Turn **Circuit Breaker and Graceful Degradation** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
cat <<'EOF'
timeout=500ms
failure_threshold=10
open_duration=30s
fallback=omit_recommendations
EOF
```

### Expected Result

Core service remains usable when optional dependencies fail.

### Troubleshooting Path

```text
circuit opens
 ↓ dependency health
 ↓ timeout
 ↓ threshold
 ↓ fallback
 ↓ recovery probe
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## Enhanced Lab 36 — Architecture Documentation as Operational Asset

### Objective

Turn **Architecture Documentation as Operational Asset** into an evidence-based AWS exercise.

### Procedure

1. Verify identity and Region before any write:
   ```bash
   aws sts get-caller-identity
   aws configure get region
   ```
2. Draw the expected architecture/data path.
3. Record the desired security and failure behavior.
4. Run the read-only discovery command below.
5. Compare actual state with the design.
6. In a disposable lab, introduce one safe reversible fault where practical.
7. Follow the troubleshooting path without changing multiple layers at once.
8. Restore the intended state.
9. Record `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Evidence Starter

```bash
mkdir -p architecture/decisions architecture/runbooks
touch architecture/ARCHITECTURE.md architecture/DATA_FLOWS.md
```

### Expected Result

On-call engineers can understand request flow and ownership quickly.

### Troubleshooting Path

```text
diagram stale
 ↓ compare CLI/IaC
 ↓ identify drift
 ↓ update source
 ↓ assign owner/review date
```

### Lab Deliverable

```text
Diagram
Requirement
Observed State
Failure Introduced
Evidence
Root Cause
Fix
Verification
Security/Cost Impact
```

---

## 5. Hands-on Lab / Practical Exercises

> Use a sandbox/training account. Favor read-only inspection and low-cost resources. Verify current AWS pricing before creating resources.

### Lab 1 — SAA Baseline Architecture Review

Draw:

```text
Internet
 ↓
EC2
 ↓
RDS
```

Identify at least 15 problems under:

```text
security
resilience
performance
cost
operations
```

Then redesign.

### Lab 2 — Multi-Account Design

Create:

```text
Organization
├─ Security OU
│  ├─ Security
│  └─ Log Archive
├─ Infrastructure OU
│  ├─ Network
│  └─ Shared Services
└─ Workloads OU
   ├─ Prod
   ├─ Stage
   └─ Dev
```

Define three SCP concepts.

### Lab 3 — IAM Cross-Account Architecture

Design:

```text
Corporate IdP
 ↓
IAM Identity Center
 ↓
Permission Set
 ↓
Assumed Role in Prod
```

Explain trust and permission policy separately.

### Lab 4 — Least-Privilege Policy

Create a lab policy allowing:

```text
GetObject
```

only for:

```text
arn:aws:s3:::company-reports/prod/*
```

No wildcard service admin permissions.

### Lab 5 — VPC CIDR Plan

Design:

```text
10.20.0.0/16
```

across three AZs:

```text
public
app
database
endpoints
```

Avoid overlap with:

```text
10.10.0.0/16 on-prem
```

### Lab 6 — Public/Private/Isolated Routing

Create conceptual route tables for:

```text
public
private
isolated
```

Show:

```text
IGW
NAT
local
```

### Lab 7 — Security Group Chain

Design:

```text
ALB-SG
APP-SG
DB-SG
```

where each tier accepts traffic only from previous tier.

### Lab 8 — NACL Failure Exercise

Create a scenario where:

```text
SG permits HTTPS
NACL return path blocks ephemeral port
```

Explain why connection fails.

### Lab 9 — VPC Endpoints vs NAT

Compare monthly architecture for private EC2 accessing:

```text
S3
DynamoDB
Secrets Manager
```

Determine which traffic can avoid NAT using endpoints.

### Lab 10 — Hybrid Network Design

Design:

```text
Direct Connect primary
Site-to-Site VPN backup
Transit Gateway
three VPCs
```

Include BGP/routing concepts.

### Lab 11 — Route 53 Routing Scenarios

Choose:

```text
simple
weighted
latency
failover
geolocation
multivalue
```

for six requirements.

### Lab 12 — Load Balancer Selection

Choose:

```text
ALB
NLB
GWLB
```

for:

```text
HTTP microservices
TCP trading feed
firewall appliance fleet
```

### Lab 13 — EC2 Family Selection

Map:

```text
web
HPC CPU
in-memory DB
local-NVMe analytics
GPU ML
```

to instance family category.

### Lab 14 — EC2 Purchase Model

Choose:

```text
On-Demand
Spot
Savings Plan/RI
Capacity Reservation
Dedicated Host
```

for five workloads.

### Lab 15 — Auto Scaling Design

Design:

```text
min 2
desired 4
max 20
three AZs
ALB
target tracking
```

Then simulate one AZ failure.

### Lab 16 — Lambda vs ECS vs EC2

For ten application workloads select:

```text
Lambda
Fargate
ECS on EC2
EKS
EC2
```

and justify operational overhead/performance.

### Lab 17 — S3 Architecture

Design a secure content bucket with:

```text
Block Public Access
versioning
SSE-KMS
lifecycle
CloudFront OAC
access logging/audit strategy
```

### Lab 18 — S3 Lifecycle Cost Design

Data:

```text
100 TB
first 30d active
then monthly access
after 1y archive
retain 7y
```

Design storage-class transitions.

### Lab 19 — EBS Selection

Choose:

```text
gp3
io2
st1
sc1
```

for:

```text
web boot
high-IOPS database
sequential log processing
cold bulk data
```

### Lab 20 — File Storage Selection

Choose:

```text
EFS
FSx Windows
FSx Lustre
FSx ONTAP
```

for four workloads.

### Lab 21 — Database Selection

Choose:

```text
RDS
Aurora
DynamoDB
DocumentDB
Neptune
Keyspaces
ElastiCache
```

for seven application patterns.

### Lab 22 — Multi-AZ vs Read Replica

Draw:

```text
RDS Multi-AZ → HA

Read Replica → read scaling
```

Write five exam-style scenarios.

### Lab 23 — DynamoDB Key Design

Bad:

```text
PK = "TODAY"
```

for every transaction.

Redesign using distributed keys.

Explain hot-partition risk.

### Lab 24 — SQS Worker Architecture

Design:

```text
API
 ↓
SQS
 ↓
ASG workers
 ↓
database
```

Scale workers from queue depth.

Add DLQ.

### Lab 25 — SNS Fan-Out

Design:

```text
OrderPlaced
 ↓
SNS
 ├─ Billing Queue
 ├─ Shipping Queue
 └─ Analytics Queue
```

Explain why separate queues protect consumers.

### Lab 26 — EventBridge vs SNS vs SQS

Given ten scenarios, choose the correct service and explain the communication pattern.

### Lab 27 — DR Strategy Selection

For four workloads with different:

```text
RPO
RTO
budget
```

choose:

```text
backup/restore
pilot light
warm standby
active-active
```

### Lab 28 — Cross-Account Backup Design

Create:

```text
Prod Account
 ↓ AWS Backup copy
Backup Account
 ↓ cross-Region copy
DR Region
```

Explain ransomware/blast-radius benefits.

### Lab 29 — CloudFront Architecture

Design:

```text
Route 53
 ↓
CloudFront
 ↓
private S3 origin
+
ALB dynamic origin
```

Use separate cache behaviors.

### Lab 30 — Global Accelerator Scenario

Compare CloudFront and Global Accelerator for:

```text
static website
TCP game
global API
UDP service
```

### Lab 31 — High-Performance Data Pipeline

Design:

```text
Kinesis
 ↓
Firehose/Dataflow-style processing
 ↓
S3
 ↓
Glue Catalog
 ↓
Athena
```

Convert CSV to Parquet.

### Lab 32 — Big Data Service Selection

Choose:

```text
EMR
Glue
Athena
Redshift
MSK
Kinesis
```

for six data workloads.

### Lab 33 — Cost-Optimized Compute

Given a fleet:

```text
20 EC2
average CPU 12%
24/7
```

create:

```text
right-sizing plan
purchase-model plan
autoscaling plan
nonprod schedule
```

### Lab 34 — NAT Cost Analysis

Compare:

```text
one NAT Gateway
three NAT Gateways
S3 gateway endpoint
Secrets Manager interface endpoint
```

using **fictional prices**.

Explain availability vs cost.

### Lab 35 — Architecture CLI Discovery

Run read-only:

```bash
aws sts get-caller-identity
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-route-tables
aws ec2 describe-security-groups
```

Build a diagram from actual lab output.

### Lab 36 — RDS Architecture Discovery

```bash
aws rds describe-db-instances \
  --query 'DBInstances[].{DB:DBInstanceIdentifier,Engine:Engine,MultiAZ:MultiAZ}' \
  --output table
```

Identify HA gaps.

### Lab 37 — S3 Security Inspection

For a test bucket:

```bash
aws s3api get-public-access-block --bucket BUCKET
aws s3api get-bucket-versioning --bucket BUCKET
aws s3api get-bucket-encryption --bucket BUCKET
```

Read only.

### Lab 38 — Architecture Review Workshop

Review a fictional design:

```text
public EC2
single AZ
database on instance store
access keys in app
no backup
no monitoring
```

Create a prioritized remediation plan.

### Lab 39 — 40 Scenario Drill

Write 40 SAA-style scenarios across:

```text
secure
resilient
high-performing
cost-optimized
```

For each record:

```text
requirement
best answer
why
why closest distractor is wrong
```

### Lab 40 — Failure Game Day Tabletop

Simulate:

```text
one EC2 failure
one AZ failure
RDS primary failure
SQS backlog
DynamoDB throttling
S3 access denied
Region outage
credential compromise
```

For each define:

```text
Detection
Impact
Automatic Response
Manual Response
RPO/RTO Effect
Prevention
```

---

## 6. Mini Project

# Mini Project — Design a Production AWS Commerce Platform

## Business Requirements

```text
50,000 daily users
5,000 peak concurrent users
global customers
24/7
payment/order workflow
customer data
product images
analytics
RPO = 5 minutes for orders
RTO = 30 minutes for core ordering
RPO = 24 hours for analytics
production + staging + development
hybrid connection to ERP
```

## Required Architecture

```text
                           Route 53
                              |
                         CloudFront
                              |
                         WAF + Shield
                              |
                    Application Load Balancer
                     /                   \
                  AZ-A                   AZ-B
                   |                      |
              ECS/EC2/App1          ECS/EC2/App2
                   \                      /
                    \                    /
                      Aurora / RDS HA
                           |
                       ElastiCache
                           |
             +-------------+-------------+
             |                           |
           SQS/SNS                    S3 Objects
             |                           |
          Workers                    Analytics
                                         |
                                  Glue/Athena/Redshift
```

## Multi-Account Foundation

```text
Organizations
├─ Security
├─ Log Archive
├─ Network
├─ Shared Services
├─ Production
├─ Staging
└─ Development
```

## Identity

Design:

```text
IAM Identity Center
federation
MFA
least privilege
cross-account roles
workload roles
KMS key policies
break-glass process
```

## Network

Design:

```text
3 AZ VPC
public ingress subnets
private app subnets
isolated DB subnets
NAT
VPC endpoints
Transit Gateway
Direct Connect
VPN backup
Route 53
```

## Security

Include:

```text
WAF
Shield
Network Firewall if justified
CloudTrail
Config
GuardDuty
Security Hub
KMS
Secrets Manager
S3 Block Public Access
backup isolation
```

## Compute

Compare:

```text
EC2
ECS/Fargate
EKS
Lambda
```

and justify final selection by:

```text
operations
scale
latency
cost
team skill
```

## Storage

Select:

```text
S3
EBS
EFS
FSx
```

for each workload.

Design:

```text
versioning
lifecycle
replication
immutability
```

## Database

Choose among:

```text
Aurora/RDS
DynamoDB
ElastiCache
```

for:

```text
orders
catalog
session/cache
```

Explain access patterns.

## Messaging

Use:

```text
SQS
SNS
EventBridge
Step Functions
```

where appropriate.

## Resilience

Document response to:

```text
instance failure
AZ failure
database failure
queue consumer failure
Region failure
```

## DR

Define:

```text
RPO
RTO
strategy
secondary Region
data replication
DNS failover
test procedure
```

## Performance

Define:

```text
autoscaling metrics
CloudFront
database read scaling
cache
queue scaling
storage performance
```

## Cost

Build a fictional monthly model covering:

```text
EC2/Fargate
RDS/Aurora
S3
NAT
CloudFront
data transfer
backup
logging
support
```

Then propose 10 optimizations.

## Observability

Use:

```text
CloudWatch
CloudTrail
Config
X-Ray
Health
alarms
dashboards
```

## Automation

Design:

```text
Git
 ↓
IaC
 ↓
AWS Accounts
 ↓
Configuration / application deployment
```

IaC implementation comes later in the roadmap.

## Deliverables

```text
README.md
REQUIREMENTS.md
ARCHITECTURE.md
ACCOUNTS.md
IAM.md
NETWORK.md
COMPUTE.md
STORAGE.md
DATABASE.md
MESSAGING.md
SECURITY.md
RESILIENCE.md
DR.md
PERFORMANCE.md
COST.md
OBSERVABILITY.md
DECISIONS/
RUNBOOKS/
```

Required ADRs:

```text
ADR-001-Compute-Platform.md
ADR-002-Database.md
ADR-003-Multi-Region-DR.md
ADR-004-Private-Service-Access.md
ADR-005-Messaging.md
```

Required runbooks:

```text
RUNBOOK_EC2_FAILURE.md
RUNBOOK_AZ_FAILURE.md
RUNBOOK_DB_FAILOVER.md
RUNBOOK_REGION_DR.md
RUNBOOK_SQS_BACKLOG.md
RUNBOOK_DYNAMODB_THROTTLE.md
RUNBOOK_S3_ACCESS_DENIED.md
RUNBOOK_CREDENTIAL_COMPROMISE.md
RUNBOOK_COST_SPIKE.md
```

---

## 7. Recommended Resources

This Markdown is designed to contain the complete learning flow.

Use current official AWS documentation when implementing production systems:

```text
AWS Certified Solutions Architect – Associate SAA-C03 Exam Guide
SAA-C03 In-Scope AWS Services
AWS Well-Architected Framework
AWS Architecture Center
AWS Prescriptive Guidance
IAM User Guide
Amazon VPC User Guide
EC2 User Guide
S3 User Guide
RDS User Guide
DynamoDB Developer Guide
AWS Disaster Recovery guidance
AWS Pricing documentation
```

For command syntax:

```bash
aws help
aws ec2 help
aws s3api help
aws rds help
```

---

## 8. Certification Relevance

Direct certification:

```text
AWS Certified Solutions Architect – Associate
SAA-C03
```

Current exam:

```text
130 minutes
65 total questions
50 scored
15 unscored
720 minimum passing score
3-year certification validity
```

Current domains:

```text
Design Secure Architectures          30%
Design Resilient Architectures       26%
Design High-Performing Architectures 24%
Design Cost-Optimized Architectures  20%
```

This course prepares directly for:

```text
53. AWS SysOps Administration
54. Amazon PaaS Web Services
Infrastructure as Code
Terraform
DevOps
Cloud Security
AWS Solutions Architect Professional
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Choose services before understanding requirements.  
  **Best practice:** extract business and non-functional requirements first.

- **Mistake:** One production AZ.  
  **Best practice:** design across multiple AZs when HA requires it.

- **Mistake:** Use read replicas as a substitute for Multi-AZ HA.  
  **Best practice:** distinguish availability from read scaling.

- **Mistake:** Store AWS keys on EC2.  
  **Best practice:** use IAM roles and temporary credentials.

- **Mistake:** Put every account in one flat security boundary.  
  **Best practice:** use multi-account isolation and Organizations.

- **Mistake:** Public database for convenience.  
  **Best practice:** isolated/private database tier.

- **Mistake:** One NAT Gateway for a mission-critical three-AZ application without considering failure/cross-AZ cost.  
  **Best practice:** deliberately choose NAT topology based on availability/cost.

- **Mistake:** Use EC2 for every workload.  
  **Best practice:** select managed/serverless/container services when they reduce operations and fit requirements.

- **Mistake:** Use S3 as a mounted block filesystem.  
  **Best practice:** select object/file/block storage correctly.

- **Mistake:** Use EBS as a generic multi-host shared filesystem.  
  **Best practice:** use EFS/FSx when shared filesystem semantics are required.

- **Mistake:** DynamoDB without access-pattern design.  
  **Best practice:** design keys/queries first.

- **Mistake:** Lambda directly floods RDS with connections.  
  **Best practice:** connection pooling/RDS Proxy and concurrency controls.

- **Mistake:** Retry non-idempotent operations blindly.  
  **Best practice:** design idempotency.

- **Mistake:** Replication equals backup.  
  **Best practice:** preserve historical, isolated recovery copies.

- **Mistake:** Choose multi-Region without business justification.  
  **Best practice:** derive from RPO/RTO, latency, residency, and risk.

- **Mistake:** Optimize compute price but ignore network egress/NAT.  
  **Best practice:** model total architecture cost.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Current exam code?

**Answer:** SAA-C03.

### Q2. Largest exam domain?

**Answer:** Design Secure Architectures, 30%.

### Q3. Minimum passing score?

**Answer:** 720 scaled score.

### Q4. How many total questions?

**Answer:** 65.

### Q5. Multi-AZ vs multi-Region?

**Answer:** Multi-AZ protects against zonal failures inside one Region; multi-Region addresses regional/global requirements.

### Q6. What is an SCP?

**Answer:** Organizations policy limiting maximum permissions; it does not grant access.

### Q7. Best workforce access model?

**Answer:** Federation/IAM Identity Center with temporary role credentials.

### Q8. Public vs private subnet?

**Answer:** Public subnet routes to IGW; private subnet has no direct IGW route for its workloads.

### Q9. Security Group vs NACL?

**Answer:** Stateful resource firewall vs stateless subnet ACL.

### Q10. Private access to S3 without NAT?

**Answer:** S3 gateway VPC endpoint.

### Q11. Scalable many-VPC connectivity?

**Answer:** Transit Gateway.

### Q12. ALB vs NLB?

**Answer:** Layer 7 HTTP/S routing vs Layer 4 TCP/UDP/TLS high-performance load balancing.

### Q13. CloudFront vs Global Accelerator?

**Answer:** CDN/caching vs network acceleration/static anycast endpoint routing.

### Q14. EC2 Spot?

**Answer:** Discounted interruptible spare capacity.

### Q15. Capacity Reservation?

**Answer:** Reserves EC2 capacity in a specific Availability Zone.

### Q16. Lambda best fit?

**Answer:** Event-driven, short-running, elastic workloads with minimal server administration.

### Q17. Fargate?

**Answer:** Serverless compute for containers.

### Q18. S3?

**Answer:** Object storage.

### Q19. EBS?

**Answer:** AZ-scoped block storage.

### Q20. EFS?

**Answer:** Managed shared NFS file storage.

### Q21. FSx for Lustre?

**Answer:** High-performance parallel filesystem for HPC/data-intensive workloads.

### Q22. RDS Multi-AZ?

**Answer:** High availability/failover.

### Q23. Read replica?

**Answer:** Read scaling, with possible DR use depending on design.

### Q24. RDS Proxy?

**Answer:** Database connection pooling/proxy to reduce connection pressure and improve failover handling.

### Q25. DynamoDB?

**Answer:** Serverless key-value/document database.

### Q26. Hot partition?

**Answer:** Disproportionate requests to one partition key/data partition causing capacity bottleneck.

### Q27. DAX?

**Answer:** In-memory accelerator/cache for DynamoDB.

### Q28. SQS?

**Answer:** Durable message queue for decoupling.

### Q29. SNS?

**Answer:** Pub/sub fan-out notification service.

### Q30. EventBridge?

**Answer:** Event bus/routing service.

### Q31. Step Functions?

**Answer:** Managed workflow/state-machine orchestration.

### Q32. Backup and restore DR?

**Answer:** Lowest-cost DR pattern but usually highest RTO.

### Q33. Warm standby?

**Answer:** Reduced-capacity functional environment in DR Region that scales up during disaster.

### Q34. Active-active?

**Answer:** Multiple Regions actively serve traffic; lowest potential RTO and highest complexity.

### Q35. RPO?

**Answer:** Maximum tolerated data-loss window.

### Q36. RTO?

**Answer:** Maximum tolerated outage/recovery time.

### Q37. Athena?

**Answer:** Serverless SQL querying, commonly over S3 data.

### Q38. Glue?

**Answer:** Data catalog/integration/ETL service.

### Q39. Kinesis?

**Answer:** Streaming data service family.

### Q40. Cost Explorer?

**Answer:** Analyze historical/current AWS spending and usage trends.

---

# Expanded Self-Assessment Bank — AWS Certified Solutions Architect – Associate

### Q1. What is the key lesson from **Requirement Traceability**?
**Answer:** Maintain requirement-to-resource traceability and ADRs for high-impact decisions.

### Q2. What is the key lesson from **Failure-Domain Mapping**?
**Answer:** State exactly which failure domain each redundancy mechanism protects against.

### Q3. What is the key lesson from **Composite Availability Math**?
**Answer:** Model availability from the user journey, not one AWS SLA.

### Q4. What is the key lesson from **Service Quotas as Reliability Dependencies**?
**Answer:** Review quotas during design and game days, not during the outage.

### Q5. What is the key lesson from **Subnet IP Capacity**?
**Answer:** Capacity-plan IP addresses like CPU, memory, and database connections.

### Q6. What is the key lesson from **Enterprise CIDR Governance**?
**Answer:** Govern address allocation before creating many independent VPCs.

### Q7. What is the key lesson from **IPv6 Dual Stack**?
**Answer:** Review IPv4 and IPv6 paths independently.

### Q8. What is the key lesson from **Route 53 Resolver Hybrid DNS**?
**Answer:** Document DNS authority and forwarding just like IP routing.

### Q9. What is the key lesson from **Transit Gateway Segmentation**?
**Answer:** Use TGW route tables as segmentation controls.

### Q10. What is the key lesson from **PrivateLink Service Publishing**?
**Answer:** Choose PrivateLink for private service consumption, not general network connectivity.

### Q11. What is the key lesson from **Gateway vs Interface Endpoint Economics**?
**Answer:** Model endpoint and NAT cost using expected traffic.

### Q12. What is the key lesson from **KMS as Availability Dependency**?
**Answer:** Treat KMS as security infrastructure and an application dependency.

### Q13. What is the key lesson from **Secrets Rotation as Distributed Change**?
**Answer:** Design application secret refresh before enabling automatic rotation.

### Q14. What is the key lesson from **S3 Authorization Layers**?
**Answer:** Troubleshoot S3 as layered authorization.

### Q15. What is the key lesson from **EBS Snapshot Consistency**?
**Answer:** Define required consistency level for every backup.

### Q16. What is the key lesson from **RDS HA vs Read Scaling**?
**Answer:** Write separate requirements for availability and read scaling.

### Q17. What is the key lesson from **Aurora Endpoint Strategy**?
**Answer:** Use logical endpoints and test planned failover.

### Q18. What is the key lesson from **DynamoDB Hot-Key Analysis**?
**Answer:** Design DynamoDB from access patterns and traffic distribution.

### Q19. What is the key lesson from **DynamoDB Conditional Writes**?
**Answer:** Push concurrency checks into atomic database operations.

### Q20. What is the key lesson from **SQS Visibility Timeout**?
**Answer:** Set visibility timeout from real processing time and keep consumers idempotent.

### Q21. What is the key lesson from **SQS FIFO Message Groups**?
**Answer:** Choose the narrowest domain that truly requires ordering.

### Q22. What is the key lesson from **Event Schema Governance**?
**Answer:** Treat event schemas as versioned APIs.

### Q23. What is the key lesson from **Step Functions Compensation**?
**Answer:** Design compensation and idempotency before orchestrating irreversible work.

### Q24. What is the key lesson from **Lambda Concurrency and Downstream Capacity**?
**Answer:** Scale the whole dependency chain, not only compute.

### Q25. What is the key lesson from **ECS Capacity Provider Strategy**?
**Answer:** Use mixed capacity only when the workload can tolerate each pool's behavior.

### Q26. What is the key lesson from **CloudFront Cache-Key Design**?
**Answer:** Keep cache keys minimal and intentional.

### Q27. What is the key lesson from **Autoscaling Metric Selection**?
**Answer:** Choose the metric closest to demand/backlog.

### Q28. What is the key lesson from **Scale-In and Graceful Drain**?
**Answer:** Design graceful termination before enabling aggressive scale-in.

### Q29. What is the key lesson from **DR Dependency Completeness**?
**Answer:** Maintain a complete DR dependency inventory.

### Q30. What is the key lesson from **RTO Decomposition**?
**Answer:** Measure RTO from outage start to successful business transaction.

### Q31. What is the key lesson from **Backup Administrative Isolation**?
**Answer:** Separate backup administration from workload administration.

### Q32. What is the key lesson from **Well-Architected Risk Prioritization**?
**Answer:** Use risk-based prioritization, not checklist equality.

### Q33. What is the key lesson from **Cost per Business Transaction**?
**Answer:** Track a business-relevant unit-cost metric for major workloads.

### Q34. What is the key lesson from **Retry Storm Prevention**?
**Answer:** Retry only transient errors and cap total retry time.

### Q35. What is the key lesson from **Circuit Breaker and Graceful Degradation**?
**Answer:** Classify critical vs optional dependencies and design degradation.

### Q36. What is the key lesson from **Architecture Documentation as Operational Asset**?
**Answer:** Version architecture documentation alongside IaC.


## Completion Checklist

- [ ] I understand current SAA-C03 structure.
- [ ] I can translate requirements into architecture decisions.
- [ ] I understand all six Well-Architected pillars.
- [ ] I can design a multi-account AWS foundation.
- [ ] I understand federation/STS/IAM roles/SCPs.
- [ ] I can design secure VPC subnet tiers.
- [ ] I understand IGW/NAT/endpoints/PrivateLink.
- [ ] I understand peering/Transit Gateway/VPN/Direct Connect.
- [ ] I understand SG/NACL/WAF/Shield/Network Firewall.
- [ ] I understand Route 53 routing policies.
- [ ] I understand ALB/NLB/GWLB.
- [ ] I can select EC2 families and purchase models.
- [ ] I understand ASG/scaling strategies.
- [ ] I can select EC2/Lambda/ECS/EKS/Fargate.
- [ ] I understand S3 security/lifecycle/replication.
- [ ] I can select EBS/EFS/FSx.
- [ ] I understand hybrid transfer/storage services.
- [ ] I can select RDS/Aurora/DynamoDB/cache/graph/document DB.
- [ ] I understand Multi-AZ/read replicas/RDS Proxy.
- [ ] I understand DynamoDB key/capacity/global patterns.
- [ ] I understand SQS/SNS/EventBridge/Step Functions.
- [ ] I can design decoupled/event-driven architecture.
- [ ] I can select a DR strategy from RPO/RTO.
- [ ] I understand Multi-AZ and multi-Region designs.
- [ ] I understand CloudFront/Global Accelerator.
- [ ] I understand high-performance data ingestion/analytics.
- [ ] I understand compute/storage/database/network cost optimization.
- [ ] I can perform architecture discovery with AWS CLI.
- [ ] I can troubleshoot common AWS architecture failures.
- [ ] I completed all 40 labs.
- [ ] I completed the Production AWS Commerce Platform capstone.
