# 49. AWS Cloud Practitioner

> Phase 11 — Cloud Fundamentals

This course turns the provider-neutral cloud concepts from Course 48 into the AWS operating model.

It is deliberately broader and more practical than pure exam memorization. The objective is to understand **why a service exists, what problem it solves, how it fits into AWS architecture, how to recognize it in an exam question, and how it behaves in a real environment**.

The current certification baseline is:

```text
AWS Certified Cloud Practitioner
Exam code: CLF-C02
```

As of August 2026, CLF-C02 remains the active AWS Certified Cloud Practitioner exam.

The official scored-domain weightings are:

```text
Domain 1 — Cloud Concepts                         24%
Domain 2 — Security and Compliance               30%
Domain 3 — Cloud Technology and Services         34%
Domain 4 — Billing, Pricing, and Support          12%
```

The exam contains:

```text
50 scored questions
15 unscored questions
65 total questions
```

with:

```text
multiple-choice
multiple-response
```

question types.

The reported scaled-score range is:

```text
100–1,000
```

and the minimum passing score is:

```text
700
```

The official exam guide describes the target candidate as having up to roughly six months of AWS Cloud exposure and explicitly places deep implementation, coding, architecture design, troubleshooting, and performance testing outside the exam's target scope.

This course **does teach some implementation and troubleshooting anyway** because your goal is to become an infrastructure/cloud engineer, not merely pass a foundational exam.

---

# AWS Mental Model

Start with:

```text
AWS Account
    |
    +-- Identity
    |
    +-- Region
           |
           +-- VPC
           |    |
           |    +-- Subnets
           |    +-- Routes
           |    +-- Security Groups
           |
           +-- EC2
           +-- RDS
           +-- EBS
           +-- Load Balancers
           +-- Regional Services
    |
    +-- Global Services
         |
         +-- IAM
         +-- Route 53
         +-- CloudFront control plane
         +-- Organizations
```

A typical AWS web application:

```text
                           Users
                             |
                         Route 53
                             |
                         CloudFront
                             |
                            WAF
                             |
                 Application Load Balancer
                    /                   \
             Availability Zone A   Availability Zone B
                    |                   |
                  EC2-1               EC2-2
                    \                   /
                     \                 /
                      Amazon RDS Multi-AZ
                              |
                            Backup
                              |
                             S3
```

The operating layers are:

```text
AWS Global Infrastructure
        ↓
Account / Organization
        ↓
IAM
        ↓
VPC / Networking
        ↓
Compute / Containers / Serverless
        ↓
Storage / Databases
        ↓
Application Integration
        ↓
Monitoring / Governance
        ↓
Security
        ↓
Billing / Support
```

The learning pattern is:

```text
Service
  ↓
What Problem It Solves
  ↓
Architecture
  ↓
Exam Recognition
  ↓
CLI / Config Example
  ↓
Operational Behavior
  ↓
Security / Cost Implications
  ↓
Common Mistakes
```

---

## 1. Topic Title

**AWS Cloud Practitioner**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain AWS Cloud value propositions.
- Explain elasticity, agility, global reach, resilience, and economies of scale.
- Explain AWS global infrastructure.
- Differentiate Regions, Availability Zones, edge locations, Local Zones, Outposts, and Wavelength-style edge concepts at a fundamentals level.
- Explain AWS shared responsibility.
- Explain AWS Well-Architected Framework and its six pillars.
- Explain AWS account fundamentals.
- Explain root-user security.
- Explain IAM users, groups, roles, policies, permission boundaries conceptually, and temporary credentials.
- Explain IAM Identity Center.
- Explain federation and cross-account role access.
- Explain AWS Organizations, organizational units, consolidated billing, SCPs, and multi-account design.
- Explain AWS Control Tower conceptually.
- Explain Amazon VPC.
- Explain subnets, route tables, internet gateways, NAT gateways, security groups, network ACLs, Elastic IP concepts, and VPC endpoints.
- Explain AWS PrivateLink.
- Explain VPC peering, Transit Gateway, Site-to-Site VPN, Client VPN, and Direct Connect.
- Explain Route 53.
- Explain CloudFront and Global Accelerator.
- Explain Amazon EC2.
- Explain instance families, AMIs, EBS, instance store, user data, metadata, Elastic IPs, load balancers, and Auto Scaling.
- Explain On-Demand, Reserved Instances, Savings Plans, Spot, Dedicated Hosts, Dedicated Instances, and Capacity Reservations conceptually.
- Explain Lightsail and Elastic Beanstalk.
- Explain AWS Batch and Outposts at a fundamentals level.
- Explain ECS, EKS, ECR, Fargate, and Lambda.
- Explain Amazon S3 in depth at the Cloud Practitioner level.
- Explain S3 storage classes, lifecycle, versioning, encryption, replication, Object Lock, and access controls.
- Explain EBS, EFS, FSx, Storage Gateway, Snow Family, Backup, and Elastic Disaster Recovery.
- Explain RDS, Aurora, DynamoDB, ElastiCache, DocumentDB, Neptune.
- Explain DMS and SCT.
- Explain SQS, SNS, EventBridge, and Step Functions.
- Explain API Gateway.
- Explain Athena, Glue, Kinesis, EMR, Redshift, OpenSearch, and QuickSight.
- Explain SageMaker AI and major AI/ML recognition services included in the CLF-C02 service list.
- Explain CloudWatch, CloudTrail, Config, Systems Manager, Trusted Advisor, Compute Optimizer, Service Quotas, Health Dashboard, and Well-Architected Tool.
- Explain CloudFormation and Infrastructure as Code.
- Explain IAM, KMS, Secrets Manager, ACM, CloudHSM, Cognito, Directory Service, GuardDuty, Inspector, Macie, Detective, Security Hub, Shield, WAF, Firewall Manager, Artifact, and Audit Manager.
- Explain AWS Marketplace.
- Explain Cost Explorer, Budgets, Cost and Usage Reports, Pricing Calculator, cost-allocation tags, and consolidated billing.
- Explain AWS Support and current support-plan direction.
- Explain the role of AWS re:Post, documentation, Prescriptive Guidance, Professional Services, Partners, and Marketplace.
- Recognize the correct AWS service from common Cloud Practitioner scenarios.
- Use the AWS CLI safely for basic read-only discovery.
- Design a small production-style AWS architecture.
- Troubleshoot foundational AWS access, network, compute, storage, and cost issues.

---

## 3. Prerequisites

Required:

- 48. Cloud Computing Fundamentals
- networking fundamentals
- Linux fundamentals
- storage fundamentals
- databases
- Git and configuration-management basics

Optional tools:

```text
AWS account
AWS Management Console
AWS CLI v2
```

If you use a real AWS account:

```text
set a budget
enable MFA
avoid creating expensive resources
delete labs when finished
never publish access keys
```

A practical local verification command after CLI setup is:

```bash
aws sts get-caller-identity
```

Expected structure:

```json
{
  "UserId": "...",
  "Account": "123456789012",
  "Arn": "..."
}
```

Do not paste real account IDs, access keys, or session tokens into public repositories or screenshots.

---

## 4. Core Concepts Explanation

# Part 1 — Why AWS

AWS provides on-demand infrastructure and managed services through global cloud infrastructure.

Typical business benefits:

```text
avoid large upfront procurement
provision quickly
scale with demand
use global infrastructure
consume managed services
automate through APIs
```

The Cloud Practitioner exam focuses heavily on recognizing these business and technical advantages.

# Part 2 — Agility

Agility means reducing the time from requirement to usable infrastructure.

Traditional:

```text
purchase server
→ wait
→ rack
→ install
→ configure
```

AWS:

```text
API/console
→ provision
```

This makes experimentation and product iteration faster.

# Part 3 — Elasticity

Elasticity means increasing or reducing resources as demand changes.

```text
low traffic → 2 instances
peak traffic → 20 instances
low traffic → 2 instances
```

AWS Auto Scaling and serverless services are common elasticity mechanisms.

# Part 4 — Economies of Scale

A hyperscale provider operates infrastructure at a scale unavailable to most individual companies.

Conceptually:

```text
large provider purchasing power
+
shared infrastructure
+
automation
=
lower unit economics
```

You still need cost governance; cloud does not automatically make every workload cheaper.

# Part 5 — Trade Capital Expense for Variable Expense

Instead of purchasing fixed infrastructure upfront:

```text
CAPEX:
buy servers now
```

cloud often uses:

```text
variable OPEX:
pay for consumed services
```

Some organizations still use commitments/reservations to reduce variable costs.

# Part 6 — Stop Guessing Capacity

On-prem:

```text
buy for future peak
→ overprovision
```

AWS:

```text
start smaller
measure
scale
```

This works best when architecture actually supports scaling.

# Part 7 — Global Reach

AWS Regions allow workloads to run near users or meet geographic requirements.

Use cases:

```text
lower latency
disaster recovery
data residency
business expansion
```

# Part 8 — Managed Services

Managed services shift operational work to AWS.

Example:

```text
database on EC2:
you manage OS + DB

Amazon RDS:
AWS manages more database infrastructure operations
```

The customer still manages data, schema, permissions, queries, and service configuration.

# Part 9 — AWS Global Infrastructure

Core concepts:

```text
Region
Availability Zone
edge location
Local Zone
Outposts
```

The exact number of Regions and AZs changes over time, so architecture should depend on the model—not memorizing a permanent count.

# Part 10 — Region

An AWS Region is a geographic location containing multiple Availability Zones.

Region examples use codes such as:

```text
us-east-1
eu-west-1
me-central-1
```

Choose Region based on:

```text
latency
service availability
compliance
cost
data residency
DR
```

# Part 11 — Availability Zone

An Availability Zone consists of one or more discrete datacenters designed with independent power, networking, and connectivity from other AZs in the Region.

```text
Region
├─ AZ-A
├─ AZ-B
└─ AZ-C
```

Use multiple AZs for high availability.

# Part 12 — Availability Zone Names Are Account-Mapped

The letter in:

```text
us-east-1a
```

does not necessarily identify the same physical AZ for every AWS account.

AWS provides AZ IDs for consistent physical-zone identification when cross-account alignment matters.

# Part 13 — Edge Location

Edge locations support services that benefit from proximity to users.

Most recognizable example:

```text
Amazon CloudFront
```

which caches/distributes content through AWS edge infrastructure.

# Part 14 — Local Zones

AWS Local Zones place selected AWS infrastructure/services closer to metropolitan areas where ultra-low latency or data locality is needed.

Think:

```text
Region
  ↓ extended closer
Local Zone
  ↓
latency-sensitive workload
```

# Part 15 — AWS Outposts

AWS Outposts extends AWS infrastructure and services into customer/on-premises locations.

Use case:

```text
low-latency local processing
local data requirement
hybrid operations
```

while using AWS-consistent infrastructure and APIs.

# Part 16 — Multi-AZ Architecture

Bad:

```text
One EC2
One AZ
```

Better:

```text
ALB
├─ EC2 AZ-A
└─ EC2 AZ-B
```

A single AZ failure can then be tolerated if all dependent layers are also resilient.

# Part 17 — Multi-Region Architecture

Use multiple Regions when business requirements demand:

```text
regional disaster recovery
global latency
business continuity
data sovereignty
```

Multi-Region is more expensive and operationally complex than Multi-AZ.

# Part 18 — Shared Responsibility

AWS describes:

```text
AWS:
security OF the cloud

Customer:
security IN the cloud
```

AWS operates datacenters, hardware, and foundational cloud infrastructure.

Customers configure identities, data access, workload security, and many service settings.

# Part 19 — Shared Responsibility — EC2

For EC2:

```text
AWS:
facility
hardware
hypervisor

Customer:
guest OS
patching
host firewall
application
data
IAM/network configuration
```

This resembles traditional VM administration.

# Part 20 — Shared Responsibility — RDS

With RDS, AWS also manages more of:

```text
database host OS
database software infrastructure operations
patch orchestration
backup mechanisms
```

Customer still manages:

```text
schema
users
data
queries
DB parameters/config
network access
```

# Part 21 — Shared Responsibility — Lambda

AWS manages the server/OS/runtime infrastructure layer.

Customer manages:

```text
function code
dependencies
permissions
environment configuration
data
event sources
```

The responsibility boundary shifts with service abstraction.

# Part 22 — AWS Well-Architected Framework

The Framework helps review architecture using six pillars:

```text
Operational Excellence
Security
Reliability
Performance Efficiency
Cost Optimization
Sustainability
```

Cloud Practitioner questions may ask which principle/pillar matches a scenario.

# Part 23 — Operational Excellence Pillar

Focus:

```text
operations as code
observability
small reversible changes
learning from failures
continuous improvement
```

Example AWS tools:

```text
CloudFormation
CloudWatch
Systems Manager
```

# Part 24 — Security Pillar

Focus:

```text
identity
traceability
defense in depth
data protection
incident preparation
automation
```

AWS services include IAM, CloudTrail, KMS, GuardDuty, WAF, and others.

# Part 25 — Reliability Pillar

Focus:

```text
recover from failure
automatically scale
test recovery
manage change
use distributed design
```

Multi-AZ architectures are a core example.

# Part 26 — Performance Efficiency Pillar

Focus:

```text
select correct resource type
monitor performance
use managed services
experiment
adapt as technology changes
```

Right instance family/database/storage service matters.

# Part 27 — Cost Optimization Pillar

Focus:

```text
measure
right-size
remove waste
choose pricing model
match service to need
```

Tools:

```text
Cost Explorer
Budgets
Compute Optimizer
```

# Part 28 — Sustainability Pillar

Focus:

```text
maximize utilization
minimize unnecessary resources
use efficient managed services
scale with demand
```

Efficient architectures can reduce both environmental impact and cost.

# Part 29 — AWS Account

An AWS account is a strong isolation and administrative/billing boundary.

Resources belong to an account.

A mature organization uses multiple accounts rather than placing all:

```text
production
development
security
logging
shared services
```

in one account.

# Part 30 — AWS Root User

The root user has full account authority and can perform certain account-level tasks.

Best practice:

```text
do not use root for daily work
protect credentials
use MFA
avoid root access keys
```

In AWS Organizations, modern centralized root-access management can further reduce member-account root credentials.

# Part 31 — IAM

AWS Identity and Access Management controls AWS identities and permissions.

Core objects:

```text
users
groups
roles
policies
```

IAM is a global service.

# Part 32 — IAM User

An IAM user represents a long-lived AWS identity inside an account.

Modern preference for workforce access is generally federation/IAM Identity Center rather than creating large populations of permanent IAM users.

# Part 33 — IAM Group

Group permissions for IAM users.

```text
Developers
   |
   +-- Alice
   +-- Bob
```

Attach permissions to groups rather than duplicating policies on every user.

# Part 34 — IAM Role

A role provides permissions that can be assumed temporarily.

Use cases:

```text
EC2 workload
Lambda function
cross-account admin
federated user
AWS service
```

Roles avoid long-lived credentials in many scenarios.

# Part 35 — IAM Policy

Policies are JSON permission documents.

Example structure:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::example-bucket/*"
  }]
}
```

# Part 36 — Policy Components

Common:

```text
Effect
Action
Resource
Condition
Principal (in resource/trust policies)
```

The exam expects conceptual understanding more than authoring advanced JSON.

# Part 37 — Explicit Deny

A useful IAM rule:

```text
explicit DENY
overrides
ALLOW
```

Permission evaluation can involve identity policies, resource policies, SCPs, permission boundaries, session policies, and other controls.

# Part 38 — Least Privilege

Grant only required permissions.

Bad:

```text
AdministratorAccess
for every workload
```

Better:

```text
only read from required S3 prefix
only publish to required SNS topic
```

# Part 39 — IAM Managed Policy vs Customer Managed Policy

AWS-managed policy:

```text
created/maintained by AWS
```

Customer-managed policy:

```text
created by your organization
customized to your needs
```

Inline policies are embedded directly into one identity and are less reusable.

# Part 40 — Temporary Credentials

AWS Security Token Service (STS) provides temporary credentials.

Typical role flow:

```text
identity
 ↓ AssumeRole
STS
 ↓ temporary keys/token
AWS API
```

Temporary credentials are preferred over long-lived access keys.

# Part 41 — AWS IAM Identity Center

IAM Identity Center provides centralized workforce access across AWS accounts and applications.

Architecture:

```text
Corporate IdP / Identity Center
      ↓
User
      ↓
Permission Set
      ↓
AWS Account Role
```

This is a major multi-account access pattern.

# Part 42 — Federation

Federation lets external identity providers authenticate users who then receive AWS permissions.

Example:

```text
Microsoft Entra ID / enterprise IdP
          ↓
federation
          ↓
AWS temporary role
```

# Part 43 — Cross-Account Role

Instead of creating duplicate users:

```text
Admin Account
   ↓ AssumeRole
Production Account
```

Cross-account roles support centralized identity and separation of accounts.

# Part 44 — MFA

MFA is critical for privileged access.

Methods include supported:

```text
security keys
authenticator apps
other MFA devices
```

Protect root and administrative identities.

# Part 45 — Access Keys

Access key:

```text
Access Key ID
Secret Access Key
```

is a programmatic credential.

Never:

```text
commit to Git
embed in AMI
hard-code in application
publish in screenshots
```

# Part 46 — Workload Credentials

For EC2:

```text
EC2
 ↓ instance profile/role
STS temporary credentials
 ↓
AWS service
```

This is safer than storing static access keys on the server.

# Part 47 — AWS Organizations

Organizations centrally manages multiple AWS accounts.

Structure:

```text
Organization
├─ Management Account
├─ OU Production
│  ├─ App Account
│  └─ Data Account
└─ OU NonProd
   └─ Dev Account
```

# Part 48 — Organizational Unit

OU groups accounts for governance.

Examples:

```text
Security
Infrastructure
Production
Sandbox
```

Policies such as SCPs can be attached to OUs.

# Part 49 — Service Control Policy

SCP sets the maximum available permissions for member-account identities.

Important:

```text
SCP does not itself grant permission
```

It limits what IAM policies can grant.

# Part 50 — SCP Example

Concept:

```text
IAM policy:
Allow EC2 in every Region

SCP:
Deny regions outside approved list
```

Effective access is constrained by the SCP.

# Part 51 — Consolidated Billing

AWS Organizations can combine billing across member accounts.

Benefits:

```text
single bill
central cost view
sharing of some volume/commitment benefits
account-level cost allocation
```

# Part 52 — AWS Control Tower

Control Tower helps establish and govern a multi-account AWS environment using landing-zone concepts and guardrails.

Think:

```text
Organizations
+
IAM Identity Center
+
logging/security baseline
+
controls
```

# Part 53 — Amazon VPC

VPC is a logically isolated virtual network.

Example:

```text
VPC 10.20.0.0/16
├─ Public Subnet A
├─ Public Subnet B
├─ Private App A
├─ Private App B
├─ Private DB A
└─ Private DB B
```

# Part 54 — Subnet

A subnet belongs to exactly one Availability Zone.

This is a key AWS fact:

```text
VPC → Regional
Subnet → AZ-specific
```

Deploying across AZs requires multiple subnets.

# Part 55 — Route Table

Routes determine traffic forwarding.

Example public subnet:

```text
10.20.0.0/16 → local
0.0.0.0/0    → Internet Gateway
```

# Part 56 — Internet Gateway

An Internet Gateway attaches to a VPC and enables Internet routing for resources with appropriate addressing/routes.

Public EC2 reachability still also requires:

```text
public/Elastic IP
route
security rule
OS firewall
listening application
```

# Part 57 — Public Subnet

A subnet is considered public when its route table provides a path to an Internet Gateway.

A VM in that subnet still needs suitable public addressing and security rules to be reachable.

# Part 58 — Private Subnet

Private subnet:

```text
no direct Internet Gateway route for inbound/outbound workload path
```

Private EC2 can access selected services via:

```text
NAT
VPC endpoints
private connectivity
```

# Part 59 — NAT Gateway

Allows private IPv4 workloads to initiate outbound Internet connections.

```text
Private EC2
 ↓
NAT Gateway in public subnet
 ↓
Internet Gateway
 ↓
Internet
```

It does not accept arbitrary inbound connections to private instances.

# Part 60 — Security Group

Stateful virtual firewall associated with network interfaces/resources.

Example:

```text
ALB SG:
allow 443 from Internet

Web SG:
allow 443 only from ALB SG
```

This is stronger than opening the web servers directly.

# Part 61 — Security Group Stateful Behavior

If inbound connection is allowed:

```text
client → EC2 TCP/443
```

response traffic is automatically allowed as part of the stateful connection.

# Part 62 — Network ACL

NACL applies at subnet level and is stateless.

```text
inbound rules
outbound rules
```

must account for both directions.

Security groups are usually the primary workload firewall; NACLs provide an additional subnet boundary.

# Part 63 — Security Group vs NACL

```text
Security Group:
stateful
resource/ENI level
allow rules

NACL:
stateless
subnet level
allow and deny rules
```

This is a common exam comparison.

# Part 64 — Elastic Network Interface

ENI is a virtual network interface in VPC.

It can contain:

```text
private IPs
security groups
MAC address
public-IP association indirectly
```

EC2 instances attach ENIs.

# Part 65 — Public IPv4 and Elastic IP

Elastic IP is a static public IPv4 address allocated to your AWS account.

Use only where needed.

Public IPv4 addressing is a billable resource in modern AWS pricing models, so uncontrolled usage also affects cost.

# Part 66 — VPC Peering

Connect two VPCs directly.

```text
VPC A ↔ VPC B
```

Peering is not transitive:

```text
A ↔ B
B ↔ C
```

does not automatically imply:

```text
A ↔ C
```

# Part 67 — AWS Transit Gateway

Transit Gateway provides hub-and-spoke connectivity for many VPCs and networks.

```text
VPC A \
VPC B  → Transit Gateway → On-Prem
VPC C /
```

Useful at scale compared with many individual peerings.

# Part 68 — Site-to-Site VPN

Encrypted IPsec connectivity:

```text
On-Prem Router
    ↕ VPN
AWS Virtual/Transit Gateway
```

Useful for hybrid connectivity and backup paths.

# Part 69 — AWS Client VPN

Managed remote-access VPN for individual users/devices.

```text
Engineer Laptop
   ↓ encrypted tunnel
AWS Client VPN
   ↓
VPC resources
```

# Part 70 — AWS Direct Connect

Dedicated network connection from customer/partner location to AWS.

Benefits can include:

```text
predictable connectivity
private routing
high bandwidth
hybrid workloads
```

It is not automatically encrypted end-to-end; encryption may require additional design.

# Part 71 — AWS PrivateLink

PrivateLink provides private connectivity to supported services through VPC endpoints without exposing traffic to public Internet.

```text
Consumer VPC
 ↓ private endpoint
Provider Service
```

# Part 72 — VPC Endpoint

Endpoints provide private connectivity to supported AWS services.

Two broad concepts:

```text
gateway endpoints
interface endpoints / PrivateLink
```

S3 and DynamoDB are classic gateway-endpoint examples.

# Part 73 — Amazon Route 53

Route 53 is AWS DNS and domain/traffic-routing service.

Functions:

```text
domain registration
authoritative DNS
health checks
routing policies
```

# Part 74 — Route 53 Routing Policies

Common concepts:

```text
simple
weighted
latency-based
failover
geolocation
geoproximity
multivalue
```

Exam questions often describe the business objective and ask which policy fits.

# Part 75 — Route 53 Failover

Example:

```text
Primary endpoint healthy
→ send traffic primary

health check fails
→ use secondary
```

DNS failover depends on health checks and TTL behavior.

# Part 76 — Amazon CloudFront

CloudFront is AWS CDN.

```text
User
 ↓
Edge Location
 ↓ cache hit
Content

cache miss
 ↓
Origin such as S3/ALB
```

Benefits:

```text
lower latency
origin offload
global distribution
security integration
```

# Part 77 — CloudFront Origin

Origins can include:

```text
S3
Application Load Balancer
EC2/application endpoint
custom HTTP origin
```

Use origin access controls/policies to avoid unnecessary direct public S3 origin access.

# Part 78 — AWS Global Accelerator

Global Accelerator improves availability/performance for global applications using AWS global network and static anycast IP addresses.

Difference:

```text
CloudFront:
content/CDN + HTTP-oriented caching

Global Accelerator:
network traffic acceleration to regional endpoints
```

# Part 79 — Amazon EC2

Elastic Compute Cloud provides virtual machines.

You choose:

```text
AMI
instance type
network
storage
security group
IAM role
```

Then manage the guest OS.

# Part 80 — EC2 Instance Type

Instance types combine:

```text
vCPU
memory
network
storage capabilities
accelerators
```

Families target different workloads.

# Part 81 — General Purpose Instances

Balanced:

```text
compute
memory
network
```

Use for:

```text
web servers
small databases
development
general enterprise apps
```

# Part 82 — Compute Optimized

Higher CPU relative to memory.

Use for:

```text
batch compute
high-performance web servers
media processing
scientific compute
```

# Part 83 — Memory Optimized

Higher memory capacity.

Use for:

```text
in-memory database
large cache
memory-intensive analytics
```

# Part 84 — Storage Optimized

Designed for high local-storage throughput/IOPS use cases.

Use for workloads requiring fast local storage patterns.

# Part 85 — Accelerated Computing

Uses:

```text
GPU
special accelerators
```

for:

```text
ML
graphics
HPC
video
```

# Part 86 — AMI

Amazon Machine Image is the template used to launch EC2.

Contains:

```text
OS
software baseline
root-volume configuration
permissions
```

Use controlled AMIs for repeatable infrastructure.

# Part 87 — EC2 User Data

Startup/bootstrap script.

Example:

```bash
#!/bin/bash
dnf install -y nginx
systemctl enable --now nginx
echo "AWS Lab" > /usr/share/nginx/html/index.html
```

Use user data for bootstrap, not as an uncontrolled long-term configuration strategy.

# Part 88 — EC2 Instance Metadata

Metadata exposes information/credentials to the instance.

Examples:

```text
instance ID
Region/AZ
network
IAM role credentials
```

Applications should use modern metadata protections and never expose metadata access through SSRF vulnerabilities.

# Part 89 — EC2 Instance Store

Physically attached ephemeral storage.

Characteristics:

```text
high performance
data tied to host/instance lifecycle
not durable like EBS
```

Do not store sole copies of critical data there.

# Part 90 — Amazon EBS

Elastic Block Store provides persistent block volumes for EC2.

```text
EC2
 ↓
EBS Volume
 ↓
filesystem/database
```

EBS volumes are AZ-scoped.

# Part 91 — EBS Snapshot

Snapshots back up EBS volume data into AWS-managed snapshot storage.

Use for:

```text
backup
restore
clone
cross-region copy
```

Snapshots are incremental at the storage-management level.

# Part 92 — Elastic Load Balancing

ELB distributes traffic to healthy targets.

Main concepts include:

```text
Application Load Balancer
Network Load Balancer
Gateway Load Balancer
```

Cloud Practitioner focuses on knowing load balancer purpose and broad use cases.

# Part 93 — Application Load Balancer

Layer 7 HTTP/HTTPS.

Supports:

```text
host-based routing
path-based routing
application health checks
```

Great for web applications and microservices.

# Part 94 — Network Load Balancer

Layer 4 high-performance TCP/UDP/TLS load balancing.

Use for:

```text
very high connection scale
static IP needs
non-HTTP protocols
```

# Part 95 — Gateway Load Balancer

Helps deploy/scale virtual network appliances.

Use cases:

```text
firewalls
intrusion inspection
network security appliances
```

# Part 96 — EC2 Auto Scaling

Maintains desired EC2 capacity.

```text
Launch Template
   ↓
Auto Scaling Group
   ↓
EC2 fleet
```

Can replace unhealthy instances and scale based on demand.

# Part 97 — Target Tracking Scaling

Example:

```text
maintain average CPU around 50%
```

Auto Scaling adjusts fleet size toward target.

# Part 98 — EC2 On-Demand

No long-term usage commitment.

Best for:

```text
short-term
unpredictable
testing
new workloads
```

Generally higher unit cost than commitment models.

# Part 99 — Reserved Instances

Reserved Instances provide billing discounts for eligible EC2 usage under commitment terms.

They are primarily a **pricing benefit**, not a reserved VM.

Do not confuse with Capacity Reservations.

# Part 100 — Savings Plans

Savings Plans provide discounts in exchange for committing to a level of compute spend/usage over a term.

They can offer more flexibility than traditional RI models depending on plan type.

# Part 101 — Spot Instances

Use spare EC2 capacity at large discounts, but capacity can be interrupted.

Good:

```text
fault-tolerant batch
CI
distributed workers
```

Poor fit:

```text
single critical non-redundant server
```

# Part 102 — Capacity Reservation

Capacity Reservation holds EC2 capacity in a specific AZ for your use.

Purpose:

```text
capacity assurance
```

not primarily discount.

# Part 103 — Dedicated Host

Physical server dedicated to your use.

Use cases may include:

```text
compliance
server-bound software licensing
visibility into sockets/cores
```

# Part 104 — Dedicated Instance

Instances run on hardware dedicated to a single customer account, but with less direct physical-host control than Dedicated Hosts.

Know the conceptual distinction for exam scenarios.

# Part 105 — Amazon Lightsail

Simplified VPS-style AWS service.

Provides bundled/simple:

```text
virtual servers
storage
networking
databases
```

Good for simple applications where full AWS architecture flexibility is unnecessary.

# Part 106 — AWS Elastic Beanstalk

PaaS-style application deployment service.

You provide:

```text
application code
```

Elastic Beanstalk provisions/manages AWS resources such as compute, scaling, and load balancing based on environment configuration.

# Part 107 — AWS Batch

Managed batch job orchestration.

Use when:

```text
large job queues
parallel/batch processing
compute scheduling
```

AWS manages job scheduling against configured compute environments.

# Part 108 — Amazon ECR

Elastic Container Registry stores container images.

```text
Docker build
 ↓
ECR
 ↓
ECS/EKS
```

Use IAM-based access and image scanning/security processes.

# Part 109 — Amazon ECS

Elastic Container Service is AWS container orchestration.

Runs containers on:

```text
EC2 capacity
or
Fargate
```

It is AWS-native and simpler than Kubernetes for many use cases.

# Part 110 — Amazon EKS

Elastic Kubernetes Service provides managed Kubernetes.

AWS manages significant control-plane infrastructure; customer manages cluster configuration, workloads, IAM/RBAC, networking choices, and worker compute depending on mode.

# Part 111 — AWS Fargate

Serverless compute engine for containers.

Use with:

```text
ECS
EKS
```

You specify container workload resources without managing EC2 worker hosts directly.

# Part 112 — AWS Lambda

Event-driven serverless functions.

```text
Event
 ↓
Lambda
 ↓
code executes
```

Examples:

```text
S3 upload
API request
scheduled event
queue message
```

# Part 113 — Lambda Pricing/Scaling Concept

Cost depends on dimensions such as:

```text
requests
execution duration
allocated resources
```

Lambda scales automatically, but applications must be designed for concurrency, time limits, stateless execution, and dependency behavior.

# Part 114 — Amazon S3

Simple Storage Service is object storage.

Structure:

```text
Bucket
  |
  +-- Object Key
      |
      +-- Data
      +-- Metadata
```

S3 is one of the most important Cloud Practitioner services.

# Part 115 — S3 Is Regional

An S3 bucket is created in a Region.

The bucket name must satisfy global naming uniqueness requirements, but object data location follows bucket Region and selected replication features.

# Part 116 — S3 Object

Object consists of:

```text
key
value/data
metadata
version ID if versioning
```

S3 is API/object storage, not a mounted POSIX block filesystem.

# Part 117 — S3 Strong Consistency

Modern Amazon S3 provides strong read-after-write consistency for object PUT/DELETE and related operations.

After a successful write, subsequent reads/list behavior reflects the change according to current S3 consistency guarantees.

# Part 118 — S3 Versioning

Versioning preserves object versions.

```text
report.csv v1
report.csv v2
report.csv v3
```

Useful for accidental overwrite/delete recovery.

It increases stored data and cost.

# Part 119 — S3 Lifecycle

Lifecycle can transition/delete objects automatically.

Example:

```text
Day 0   → S3 Standard
Day 30  → Standard-IA
Day 90  → Glacier class
Year 7  → Expire
```

Use according to access and retention requirements.

# Part 120 — S3 Standard

General-purpose storage class for frequently accessed data.

Use for:

```text
active application objects
web content
data frequently read/written
```

# Part 121 — S3 Intelligent-Tiering

Automatically moves objects among access tiers based on access patterns.

Useful when:

```text
access frequency is unknown/changing
```

without manually predicting lifecycle transitions.

# Part 122 — S3 Standard-IA

Infrequent Access:

```text
lower storage price than Standard
retrieval charge
multi-AZ resilience
```

Use for less frequently accessed but rapidly retrievable data.

# Part 123 — S3 One Zone-IA

Stores in one AZ.

Lower resilience/cost than multi-AZ IA.

Use only for data that can be recreated or where single-AZ storage meets requirements.

# Part 124 — S3 Glacier Instant Retrieval

Archive-oriented class for rarely accessed data requiring millisecond-style immediate retrieval.

Understand the pattern:

```text
low access frequency
fast retrieval requirement
```

# Part 125 — S3 Glacier Flexible Retrieval

Archive storage where retrieval can take longer than online classes.

Suitable for backups/archive data where retrieval speed can be minutes/hours depending on retrieval option.

# Part 126 — S3 Glacier Deep Archive

Lowest-cost long-term archive-oriented class.

Use where data is rarely retrieved and long retrieval times are acceptable.

# Part 127 — S3 Encryption

S3 supports server-side encryption approaches using:

```text
S3-managed keys
AWS KMS keys
customer-provided keys in supported workflows
```

Also use TLS in transit.

# Part 128 — S3 Bucket Policy

Resource-based JSON policy attached to bucket.

Use to control:

```text
principals
actions
resources
conditions
```

Example patterns include cross-account access or deny of unencrypted transport.

# Part 129 — S3 Block Public Access

Block Public Access helps prevent unintended public S3 access.

For most private data:

```text
keep public access blocked
```

Use CloudFront or controlled access patterns instead of making buckets public unnecessarily.

# Part 130 — S3 Replication

Replication can copy objects:

```text
same Region
cross Region
```

Use cases:

```text
compliance
DR
latency
account isolation
```

# Part 131 — S3 Object Lock

Object Lock supports WORM-style retention.

Useful for:

```text
compliance
ransomware-resistant backup design
```

when configured appropriately.

# Part 132 — Amazon EFS

Elastic File System is managed shared file storage for Linux workloads using NFS.

```text
EC2 A \
EC2 B  → EFS
EC2 C /
```

It can span multiple AZs depending on design.

# Part 133 — Amazon FSx

Managed file-system family for specific file technologies/workloads.

Examples include managed file systems for:

```text
Windows
Lustre/HPC
NetApp ONTAP
OpenZFS
```

Recognize FSx as managed specialized file storage.

# Part 134 — AWS Storage Gateway

Hybrid storage service connecting on-prem environments with AWS storage.

Use cases:

```text
file integration
volume/tape-style backup
hybrid storage
```

# Part 135 — AWS Snow Family

Physical/edge devices for data transfer and edge processing where network transfer is insufficient or edge capability is needed.

Exam scenario:

```text
very large dataset
limited network
→ Snow device
```

# Part 136 — AWS Backup

Centralized backup policy/service across supported AWS resources.

Use for:

```text
backup plans
retention
vaults
cross-account/region patterns
central governance
```

# Part 137 — AWS Elastic Disaster Recovery

DR service used to recover supported on-prem/cloud servers into AWS through replication and launch orchestration.

Think:

```text
source servers
 ↓ replicate
AWS staging
 ↓ disaster
launch recovery instances
```

# Part 138 — Amazon RDS

Managed relational database service.

Supports engines such as:

```text
MySQL
PostgreSQL
MariaDB
Oracle
SQL Server
```

depending on Region/service availability.

# Part 139 — RDS Multi-AZ

Multi-AZ focuses on high availability.

```text
Primary
  ↓ synchronous/managed standby architecture
Standby in another AZ
```

If primary fails, AWS can fail over according to service design.

# Part 140 — RDS Read Replica

Read replica focuses on read scaling and some DR patterns.

```text
Primary
  ↓ asynchronous replication
Read Replica
```

Do not confuse:

```text
Multi-AZ = HA
Read Replica = read scalability
```

# Part 141 — Amazon Aurora

AWS cloud-native relational database compatible with MySQL/PostgreSQL interfaces.

Designed around distributed managed storage and high availability.

Cloud Practitioner recognition:

```text
AWS-managed high-performance relational database
```

# Part 142 — Amazon DynamoDB

Serverless managed key-value/document NoSQL database.

Characteristics:

```text
very low latency
automatic scaling options
no server management
key-based access patterns
```

# Part 143 — DynamoDB Use Case

Good:

```text
shopping cart
session/profile data
high-scale key-value access
IoT state
```

Poor fit if the main requirement is complex relational joins and transactional SQL reporting.

# Part 144 — Amazon ElastiCache

Managed in-memory caching.

Use:

```text
Redis/Valkey/Memcached-style workloads depending on service options
```

for:

```text
session cache
database acceleration
low-latency data
```

# Part 145 — Amazon DocumentDB

Managed document database with MongoDB-compatible workload focus.

Recognition:

```text
JSON/document-style database
```

# Part 146 — Amazon Neptune

Managed graph database.

Use for:

```text
relationships
social graphs
fraud graphs
knowledge graphs
recommendation relationships
```

# Part 147 — Database on EC2 vs RDS

EC2 database:

```text
maximum OS/DB control
more operational responsibility
```

RDS:

```text
less OS administration
managed backup/patch/HA capabilities
```

Choose based on control vs operational overhead.

# Part 148 — AWS DMS

Database Migration Service helps migrate/replicate databases.

Use for:

```text
homogeneous migration
heterogeneous migration with related schema work
continuous replication
minimal-downtime migration
```

# Part 149 — AWS Schema Conversion Tool

SCT helps convert database schema/code for heterogeneous migrations where source/target engines differ.

Concept:

```text
Oracle schema
 ↓ convert
PostgreSQL/Aurora target
```

# Part 150 — Amazon SQS

Simple Queue Service provides message queues.

```text
Producer
 ↓
Queue
 ↓
Worker
```

Decouples components and buffers bursts.

# Part 151 — SQS Standard vs FIFO Concept

Standard:

```text
very high throughput
at-least-once delivery model
best-effort ordering
```

FIFO:

```text
ordering
deduplication semantics
```

Use based on business requirement.

# Part 152 — Amazon SNS

Simple Notification Service provides pub/sub notifications.

```text
Publisher
 ↓
SNS Topic
 ├─ Email
 ├─ SQS
 ├─ Lambda
 └─ Other subscribers
```

# Part 153 — SQS vs SNS

```text
SQS:
queue / pull-style worker decoupling

SNS:
publish to multiple subscribers
```

A common architecture combines them:

```text
SNS
├─ SQS Queue A
└─ SQS Queue B
```

# Part 154 — Amazon EventBridge

Event bus for routing application/AWS/SaaS events by rules.

```text
Event Source
 ↓
EventBridge
 ↓ rule
Target
```

Targets can include Lambda, Step Functions, queues, and other services.

# Part 155 — AWS Step Functions

Serverless workflow orchestration.

```text
Step 1
 ↓
Step 2
 ├─ success → Step 3
 └─ failure → retry/recover
```

Useful for coordinating Lambda and AWS service workflows.

# Part 156 — Amazon API Gateway

Managed service for creating/publishing/protecting APIs.

Typical architecture:

```text
Client
 ↓
API Gateway
 ↓
Lambda / HTTP Backend / AWS Service
```

Provides features around routing, authorization, throttling, and monitoring.

# Part 157 — Amazon Athena

Serverless interactive SQL query service, commonly querying data in S3.

```text
S3 data
 ↓
Athena SQL
 ↓
results
```

Pay-per-query patterns encourage efficient partitioning/compression.

# Part 158 — AWS Glue

Managed data integration/catalog/ETL service.

Key recognition:

```text
data catalog
ETL
data discovery
```

# Part 159 — Amazon Kinesis

Real-time streaming data services.

Use for:

```text
logs
events
IoT streams
clickstreams
real-time processing
```

# Part 160 — Amazon EMR

Managed big-data platform around ecosystems such as Hadoop/Spark.

Use for large-scale data processing where these frameworks are appropriate.

# Part 161 — Amazon Redshift

Cloud data warehouse.

Use for:

```text
large analytical SQL
BI
data warehouse
```

not typical OLTP application transactions.

# Part 162 — Amazon OpenSearch Service

Managed search/analytics service.

Use for:

```text
log analytics
full-text search
observability/search workloads
```

# Part 163 — Amazon QuickSight

AWS business-intelligence visualization/service.

Use for:

```text
dashboards
analytics
business reporting
```

# Part 164 — Amazon SageMaker AI

Managed platform for building, training, and deploying machine-learning models.

Cloud Practitioner recognition:

```text
end-to-end ML development platform
```

# Part 165 — Amazon Comprehend

Natural-language processing/text insights.

Use for:

```text
sentiment
entities
key phrases
language analysis
```

# Part 166 — Amazon Lex

Conversational AI service for chat/voice interfaces.

Think:

```text
chatbot
conversational interface
```

# Part 167 — Amazon Polly

Text-to-speech.

```text
text
 ↓
Polly
 ↓
spoken audio
```

# Part 168 — Amazon Rekognition

Image/video analysis.

Use for:

```text
object/scene detection
image analysis
vision workloads
```

subject to responsible-use requirements and service capabilities.

# Part 169 — Amazon Textract

Extracts text and structured information from documents.

Think:

```text
scanned form/PDF
 ↓
Textract
 ↓
text/tables/forms
```

# Part 170 — Amazon Transcribe

Speech-to-text.

```text
audio
 ↓
Transcribe
 ↓
text
```

# Part 171 — Amazon Translate

Machine translation for text between supported languages.

# Part 172 — Amazon Kendra

Enterprise search service using intelligent search capabilities across organizational content.

# Part 173 — Amazon Q

AWS's generative-AI assistant/product family for business and development use cases.

In Cloud Practitioner recognition, know it as an AWS generative AI assistant capability rather than a foundational compute/database service.

# Part 174 — Amazon CloudWatch

Monitoring/observability service.

Collects and works with:

```text
metrics
logs
alarms
dashboards
events/observability data
```

CloudWatch answers:

```text
What is happening operationally?
```

# Part 175 — CloudWatch Metric

Example:

```text
EC2 CPUUtilization
```

You can create an alarm:

```text
CPU > threshold
→ alarm state
→ notification/action
```

# Part 176 — CloudWatch Logs

Centralized log collection/query/retention for supported workloads.

Examples:

```text
application logs
Lambda logs
OS logs via agent
service logs
```

# Part 177 — AWS CloudTrail

Records AWS API/account activity.

Answers:

```text
Who called what API?
When?
From where?
Against which resource?
```

Essential for audit and incident response.

# Part 178 — CloudWatch vs CloudTrail

Common exam distinction:

```text
CloudWatch:
performance/operations monitoring

CloudTrail:
API/account activity audit
```

# Part 179 — AWS Config

Tracks resource configuration state and changes and evaluates rules.

Answers:

```text
What did the resource configuration look like?
Is it compliant with a rule?
How did it change?
```

# Part 180 — CloudTrail vs Config

```text
CloudTrail:
API activity

Config:
resource configuration/compliance history
```

Use both for strong governance.

# Part 181 — AWS Systems Manager

Operations-management service family for AWS/hybrid nodes.

Capabilities include concepts such as:

```text
fleet management
patching
parameter management
run commands
session access
automation
inventory
```

Recognize it as centralized operations.

# Part 182 — Systems Manager Parameter Store

Stores configuration parameters and can store encrypted values.

For dedicated secret rotation and credential lifecycle, Secrets Manager is often the more recognizable service.

Both may appear in security questions.

# Part 183 — AWS Trusted Advisor

Provides checks/recommendations across areas such as:

```text
cost optimization
performance
security
fault tolerance
service limits/quotas
```

Available checks/features vary by support level/account context.

# Part 184 — AWS Compute Optimizer

Analyzes utilization and recommends resource sizing/configuration changes for supported resources.

Use for:

```text
right-sizing
cost/performance optimization
```

# Part 185 — Service Quotas

View/manage account quotas for AWS services.

If you cannot create another resource despite available budget, you may have reached a service quota.

# Part 186 — AWS Health Dashboard

Provides information about AWS service health and account-specific events.

Use during incidents to determine whether an AWS event is affecting your resources.

# Part 187 — AWS Well-Architected Tool

Helps review workloads against Well-Architected best practices and record improvement plans.

# Part 188 — AWS CloudFormation

Infrastructure as Code service.

Template:

```yaml
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
```

CloudFormation creates/updates/deletes a stack of AWS resources.

# Part 189 — CloudFormation Stack

Stack:

```text
template
 ↓
CloudFormation
 ↓
set of managed AWS resources
```

This provides repeatable infrastructure compared with manual console creation.

# Part 190 — AWS Management Console

Browser interface.

Good for:

```text
learning
inspection
one-off administration
```

For repeatable production changes, prefer CLI/SDK/IaC workflows.

# Part 191 — AWS CLI

Unified command-line tool.

Read-only examples:

```bash
aws sts get-caller-identity
aws ec2 describe-regions
aws s3api list-buckets
```

Always verify profile and account before changing resources.

# Part 192 — AWS SDK

Programming-language libraries for AWS APIs.

Example Python concept:

```python
import boto3

s3 = boto3.client("s3")
for bucket in s3.list_buckets()["Buckets"]:
    print(bucket["Name"])
```

Use roles/temporary credentials rather than embedded keys.

# Part 193 — Amazon GuardDuty

Managed threat-detection service analyzing AWS data sources/signals for suspicious behavior.

Recognition:

```text
threat detection
malicious activity
compromised credentials/resources
```

# Part 194 — Amazon Inspector

Automated vulnerability-management/scanning service for supported workloads such as EC2/container/Lambda package vulnerabilities depending on service capabilities.

Recognition:

```text
software vulnerability/exposure findings
```

# Part 195 — Amazon Macie

Data-security/privacy service focused on discovering sensitive data in S3 and identifying related risks.

Recognition:

```text
sensitive data in S3
```

# Part 196 — AWS Security Hub

Aggregates and correlates security findings/posture from AWS security services and supported integrations.

Think:

```text
central security findings dashboard
```

# Part 197 — Amazon Detective

Helps investigate security findings by correlating activity and relationships.

Use after detection to understand:

```text
what happened?
which entities are related?
```

# Part 198 — AWS Shield

Managed DDoS protection.

Broad recognition:

```text
Shield Standard
baseline DDoS protection

Shield Advanced
enhanced DDoS protection/support features
```

Do not confuse with WAF.

# Part 199 — AWS WAF

Web Application Firewall filters HTTP/S requests.

Rules can inspect:

```text
IP
headers
URI
query
known attack patterns
rate
```

Use with CloudFront, ALB, API Gateway, and supported services.

# Part 200 — WAF vs Shield

```text
WAF:
application-layer HTTP filtering

Shield:
DDoS protection
```

They often work together.

# Part 201 — AWS Firewall Manager

Central management of firewall/security policies across multiple accounts/resources.

Useful in Organizations environments for consistent policy deployment.

# Part 202 — AWS KMS

Managed key-management service.

Used by many AWS services for encryption.

Concept:

```text
AWS service
 ↓
KMS key
 ↓
encrypted data
```

Policies determine who/services can use keys.

# Part 203 — AWS CloudHSM

Dedicated hardware security module service.

Use where customers require direct control of HSM-backed cryptographic material/operations beyond standard KMS abstractions.

# Part 204 — AWS Secrets Manager

Stores and manages secrets.

Use for:

```text
database password
API credential
application secret
```

Supports rotation integrations and controlled retrieval.

# Part 205 — AWS Certificate Manager

Provision/manage TLS certificates for supported AWS integrations.

Use with services such as:

```text
ALB
CloudFront
API Gateway
```

depending on certificate Region/service rules.

# Part 206 — Amazon Cognito

Identity service for application end users.

Think:

```text
customer sign-up/sign-in
application user identity
```

This is different from IAM workforce/admin permissions.

# Part 207 — AWS Directory Service

Managed directory integrations/services for workloads requiring Microsoft Active Directory or directory capabilities in AWS.

# Part 208 — AWS Artifact

Portal for AWS compliance reports and agreements.

Exam clue:

```text
Need AWS SOC/ISO/compliance report
→ AWS Artifact
```

# Part 209 — AWS Audit Manager

Helps collect/evaluate evidence for audits against frameworks.

Recognition:

```text
continuous audit evidence
compliance assessment support
```

# Part 210 — Amazon EventBridge vs CloudTrail

CloudTrail records API activity.

EventBridge routes events.

A CloudTrail/API event can be used as a source/event pattern for automation, but their primary purposes differ.

# Part 211 — AWS Marketplace

Catalog for third-party and AWS-compatible software/services/data/professional offerings.

Benefits include:

```text
simplified procurement
AWS billing integration
commercial software access
```

# Part 212 — AWS Amplify

Frontend/mobile application development and hosting/integration service.

Recognition:

```text
build/deploy frontend/mobile web experiences
```

# Part 213 — AWS AppSync

Managed GraphQL API service with real-time/offline data features.

At Cloud Practitioner level, recognize it as frontend/mobile API/data integration rather than general VM compute.

# Part 214 — AWS IoT Core

Connects/manages messaging for IoT devices.

Architecture:

```text
devices
 ↓ secure messaging
IoT Core
 ↓
AWS applications/services
```

# Part 215 — Amazon Connect

Cloud contact-center service.

Recognition:

```text
customer service/contact center
```

# Part 216 — Amazon SES

Simple Email Service for application email sending/receiving capabilities.

Recognition:

```text
transactional/marketing application email
```

# Part 217 — Amazon WorkSpaces

Managed virtual desktop service.

Recognition:

```text
persistent virtual desktop for end users
```

# Part 218 — Amazon AppStream 2.0

Streams desktop applications to users without requiring local installation of the full application environment.

# Part 219 — Amazon WorkSpaces Secure Browser

Managed secure browser access for enterprise web content/applications.

# Part 220 — AWS Application Migration Service

Helps lift-and-shift servers into AWS.

Recognition:

```text
rehost servers to EC2
```

# Part 221 — AWS Application Discovery Service

Collects information about on-prem application/server environments to support migration planning.

# Part 222 — Migration Evaluator

Assessment/business-case tooling for migration planning and cost analysis.

Think:

```text
collect environment data
estimate AWS migration economics
```

# Part 223 — AWS Migration Hub

Central place to track migration progress across applications/tools.

# Part 224 — AWS Cloud Adoption Framework

CAF helps organizations plan cloud transformation across business and technology perspectives.

Cloud Practitioner themes include:

```text
people
governance
platform
security
operations
business
```

Use it as organizational transformation guidance, not a specific AWS service.

# Part 225 — AWS Pricing Principle — Pay for Use

AWS services commonly charge based on measurable usage.

Examples:

```text
instance time
GB-month
requests
data transfer
database capacity
```

Exact pricing must be checked for the current service/Region.

# Part 226 — On-Demand Pricing

Pay without long-term commitment.

Advantages:

```text
flexibility
no forecast required
```

Tradeoff:

```text
usually higher unit cost than commitments
```

# Part 227 — Reserved Instance Pricing Concept

Commitment-based discount for eligible EC2 usage.

Exam questions often compare:

```text
steady predictable EC2 workload
→ consider RI/Savings Plans
```

# Part 228 — Savings Plans Pricing Concept

Commit to eligible compute spend/usage over time.

Use for stable baseline demand with greater flexibility than certain RI models.

# Part 229 — Spot Pricing Concept

Low-cost spare capacity, interruptible.

Exam clue:

```text
fault-tolerant batch workload
lowest EC2 cost
→ Spot
```

# Part 230 — Data Transfer Cost

Many AWS data-transfer patterns differ in cost.

Important concepts:

```text
incoming transfer often low/no service charge in many common cases
outbound Internet can cost
inter-Region transfer can cost
cross-AZ traffic can cost depending on service/path
```

Always model architecture-specific data movement.

# Part 231 — S3 Cost Dimensions

S3 cost can include:

```text
storage class
GB stored
requests
retrieval
data transfer
management features
```

Selecting a cheaper storage class without considering retrieval/access can increase total cost.

# Part 232 — AWS Pricing Calculator

Used to estimate AWS service costs before deployment.

Exam clue:

```text
estimate future architecture cost
→ AWS Pricing Calculator
```

# Part 233 — AWS Cost Explorer

Analyze historical/current cost and usage trends.

Use for:

```text
which service/account/tag is spending?
how is cost trending?
```

# Part 234 — AWS Budgets

Set cost/usage/reservation/Savings Plan-related budget thresholds and alerts.

Exam clue:

```text
notify when monthly spend approaches $X
→ AWS Budgets
```

# Part 235 — Cost and Usage Reports

Detailed billing/usage dataset for granular analysis.

Useful for:

```text
FinOps
custom analytics
chargeback
detailed line-item cost
```

# Part 236 — Cost Allocation Tags

Activate/use tags for billing allocation.

Examples:

```text
CostCenter
Application
Environment
Owner
```

This makes cost attributable to teams/workloads.

# Part 237 — Consolidated Billing

Organizations provides consolidated billing.

Allows central payment and organization-level cost visibility while retaining account separation.

# Part 238 — AWS Free Tier Concept

AWS has free-offer mechanisms for eligible services/accounts, but limits and terms change.

Do not assume:

```text
AWS account = everything free for one year
```

Check the current service/account offer before creating resources.

# Part 239 — AWS Support

Every AWS customer receives Basic Support.

Premium support offerings evolve.

As of August 2026, AWS is transitioning its support lineup: current AWS material highlights Business Support+, Enterprise Support, and Unified Operations, while legacy Developer Support, Business Support, and Enterprise On-Ramp are scheduled for discontinuation on January 1, 2027.

# Part 240 — Exam Support-Plan Compatibility Note

The current CLF-C02 exam guide still names:

```text
Developer Support
Business Support
Enterprise On-Ramp
Enterprise Support
```

because exam content lags live commercial transitions.

For the exam:

```text
understand the exam-guide names
```

For real operations in 2026:

```text
also understand the current transition
```

# Part 241 — Basic Support

Included for AWS customers.

Provides core account/customer-service and documentation/community access, plus selected health/trusted-advisor capabilities according to current AWS support terms.

# Part 242 — Business Support+

Current AWS support offering positioned as the minimum AWS-recommended level for production workloads.

It includes 24/7 expert/support capabilities beyond Basic and AI-assisted support features according to current AWS support descriptions.

# Part 243 — Enterprise Support

Designed for business-critical enterprise workloads requiring proactive guidance and enhanced expert support.

Includes designated Technical Account Manager guidance under current plan descriptions.

# Part 244 — Unified Operations

Current premium AWS offering aimed at mission-critical operations needing enhanced resilience and application-specific expert support.

This is newer than the CLF-C02 exam guide's original support-plan taxonomy.

# Part 245 — AWS Support Center

Portal for support-case interactions and support resources according to plan/account eligibility.

# Part 246 — AWS re:Post

AWS community knowledge service for technical questions and AWS guidance.

Exam recognition:

```text
community Q&A / AWS knowledge
```

# Part 247 — AWS Documentation

Official AWS documentation is the first technical source for:

```text
service behavior
API
limits
configuration
security
```

Use current docs rather than relying on old blogs for production behavior.

# Part 248 — AWS Prescriptive Guidance

Provides architecture/migration/implementation patterns and guidance for common enterprise scenarios.

# Part 249 — AWS Professional Services

AWS consulting/implementation expertise for customers needing assistance with transformation, migration, architecture, and operational programs.

# Part 250 — AWS Partner Network

AWS ecosystem of consulting/technology partners.

Includes:

```text
system integrators
independent software vendors
managed providers
specialized partners
```

# Part 251 — Trusted Advisor and Support

Trusted Advisor recommendations/check access varies by support/account context.

Exam scenarios often associate it with:

```text
cost optimization
security
performance
fault tolerance
service limits
```

# Part 252 — AWS Health vs CloudWatch

```text
AWS Health:
AWS events affecting services/account resources

CloudWatch:
your workload/service metrics/logs/alarms
```

# Part 253 — AWS Architecture Recognition Pattern

If question says:

```text
global static content
low latency
cache at edge
```

think:

```text
CloudFront
```

If:

```text
DNS / domain routing
```

think:

```text
Route 53
```

# Part 254 — Compute Recognition Pattern

```text
VM control → EC2
simple VPS → Lightsail
deploy web app without managing platform → Elastic Beanstalk
containers → ECS/EKS
serverless containers → Fargate
event function → Lambda
```

# Part 255 — Storage Recognition Pattern

```text
object → S3
block disk → EBS
shared Linux file → EFS
specialized managed filesystem → FSx
hybrid storage → Storage Gateway
offline/physical data transfer → Snow Family
```

# Part 256 — Database Recognition Pattern

```text
managed relational → RDS
AWS cloud-native relational → Aurora
key-value/document serverless → DynamoDB
cache → ElastiCache
document → DocumentDB
graph → Neptune
```

# Part 257 — Security Recognition Pattern

```text
IAM permissions → IAM
central workforce access → IAM Identity Center
keys → KMS
application secrets → Secrets Manager
DDoS → Shield
HTTP filtering → WAF
threat detection → GuardDuty
vulnerability findings → Inspector
sensitive S3 data → Macie
finding aggregation → Security Hub
investigation → Detective
compliance reports → Artifact
```

# Part 258 — Management Recognition Pattern

```text
metrics/logs/alarms → CloudWatch
API audit → CloudTrail
config/compliance state → Config
fleet operations → Systems Manager
recommendations → Trusted Advisor
right-sizing → Compute Optimizer
IaC → CloudFormation
multi-account governance → Organizations/Control Tower
```

# Part 259 — Cost Recognition Pattern

```text
forecast architecture cost → Pricing Calculator
analyze actual spend → Cost Explorer
alert on budget threshold → Budgets
granular billing dataset → Cost and Usage Reports
allocate by owner/app → cost allocation tags
```

# Part 260 — Application Integration Recognition Pattern

```text
queue → SQS
fan-out notifications → SNS
event bus/rules → EventBridge
workflow/state orchestration → Step Functions
managed API front door → API Gateway
```

# Part 261 — Analytics Recognition Pattern

```text
SQL on S3 → Athena
ETL/catalog → Glue
streaming → Kinesis
big data Spark/Hadoop → EMR
warehouse → Redshift
search/log analytics → OpenSearch
BI dashboard → QuickSight
```

# Part 262 — Migration Recognition Pattern

```text
rehost servers → Application Migration Service
discover environment → Application Discovery Service
track migrations → Migration Hub
database replication/migration → DMS
schema conversion → SCT
physical data transfer → Snow Family
business-case assessment → Migration Evaluator
```

# Part 263 — Availability Question Strategy

If question asks:

```text
high availability in one Region
```

think:

```text
multiple Availability Zones
```

If question asks:

```text
regional disaster recovery / global users / sovereignty
```

think:

```text
multiple Regions
```

# Part 264 — Shared Responsibility Question Strategy

Ask:

```text
Which layer does AWS manage for this service?
Which layer still belongs to customer?
```

More-managed service:

```text
more infrastructure responsibility shifts to AWS
```

but:

```text
identity/data/configuration remain customer concerns
```

# Part 265 — Pricing Question Strategy

Ask:

```text
steady or variable?
interruptible?
need capacity guarantee?
need dedicated hardware?
```

Map to:

```text
On-Demand
Savings Plans / RI
Spot
Capacity Reservation
Dedicated Host
```

# Part 266 — Exam Distractor Strategy

Incorrect answers are often real AWS services that solve a different problem.

Example:

```text
Need API audit:
CloudTrail

Distractors:
CloudWatch
Config
Trusted Advisor
```

Learn the **primary purpose** of each service.

# Part 267 — AWS CLI Credential Safety

Prefer:

```text
IAM Identity Center
role credentials
temporary credentials
named profiles
```

Avoid:

```text
hard-coded keys
keys in shell scripts
keys in Git
```

# Part 268 — CLI Profile Check

Before changing anything:

```bash
aws sts get-caller-identity --profile lab
```

Verify:

```text
Account
ARN
role/user
```

This prevents running commands in the wrong account.

# Part 269 — Describe Regions

Read-only:

```bash
aws ec2 describe-regions \
  --query 'Regions[].RegionName' \
  --output table
```

This demonstrates API-driven global infrastructure discovery.

# Part 270 — Describe Availability Zones

```bash
aws ec2 describe-availability-zones \
  --region us-east-1 \
  --query 'AvailabilityZones[].{Name:ZoneName,ID:ZoneId,State:State}' \
  --output table
```

Do not assume your account's AZ letter maps to another account's physical zone.

# Part 271 — List S3 Buckets

Read-only:

```bash
aws s3api list-buckets \
  --query 'Buckets[].Name' \
  --output table
```

Bucket contents still require separate permissions.

# Part 272 — List EC2 Instances

Read-only:

```bash
aws ec2 describe-instances \
  --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,Type:InstanceType}' \
  --output table
```

# Part 273 — CloudFormation Example

Minimal S3 bucket template:

```yaml
AWSTemplateFormatVersion: '2010-09-09'

Resources:
  LabBucket:
    Type: AWS::S3::Bucket
```

Deploying creates a stack-managed bucket; deleting the stack attempts to remove stack resources subject to retention/state rules.

# Part 274 — IAM Policy Example

Read-only S3 object access to one bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject"
    ],
    "Resource": "arn:aws:s3:::example-bucket/*"
  }]
}
```

This is far narrower than `s3:*` on `*`.

# Part 275 — S3 Policy Security Example

Conceptual deny for non-TLS requests:

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": [
    "arn:aws:s3:::example-bucket",
    "arn:aws:s3:::example-bucket/*"
  ],
  "Condition": {
    "Bool": {
      "aws:SecureTransport": "false"
    }
  }
}
```

Use resource-policy testing before production rollout.

# Part 276 — Three-Tier AWS Architecture

```text
Route 53
   ↓
CloudFront + WAF
   ↓
ALB
  / \
AZ-A AZ-B
 |     |
EC2   EC2
  \   /
RDS Multi-AZ
   |
S3 Backup/Objects
```

This architecture combines global delivery, security, Multi-AZ compute, managed database, and object storage.

# Part 277 — Serverless AWS Architecture

```text
Client
 ↓
CloudFront
 ↓
API Gateway
 ↓
Lambda
 ↓
DynamoDB
 ↓
EventBridge/SQS
```

Benefits:

```text
automatic scaling
minimal server administration
pay-per-use patterns
```

# Part 278 — Event-Driven AWS Architecture

```text
S3 Upload
   ↓
EventBridge
   ↓
Lambda
   ↓
SQS
   ↓
Workers
```

Use queues when you need buffering and retry isolation.

# Part 279 — Security Baseline Architecture

```text
Organizations
  ↓
IAM Identity Center
  ↓
SCPs
  ↓
Accounts
  |
  +-- CloudTrail
  +-- Config
  +-- GuardDuty
  +-- Security Hub
  +-- KMS
  +-- Backup
```

This is a foundational multi-account security model.

# Part 280 — AWS Practitioner Mental Model

Do not memorize:

```text
200 AWS service names
```

Instead ask:

```text
What category?
What problem?
Managed or self-managed?
Regional or global?
Who is responsible?
How is it secured?
How is it priced?
Which AWS service's primary purpose matches?
```

That reasoning makes both the exam and later AWS engineering courses easier.

---

# Enhanced Deep-Study Layer — AWS Cloud Practitioner

This enhancement preserves the complete uploaded Course 49 and adds a deeper AWS engineering layer around account boundaries, IAM/STS/Identity Center/SCPs, VPC routing, NAT/endpoints/Transit Gateway, Route 53 and CloudFront, EC2/AMI/Auto Scaling/EBS, S3 policy and recovery, RDS/Aurora/DynamoDB, SQS/SNS/EventBridge/Lambda, CloudWatch/CloudTrail/Config/Systems Manager, AWS security services, KMS/Secrets Manager, AWS Backup/DR, cost architecture, and evidence-first troubleshooting.

The original file remains the Cloud Practitioner/CLF-C02 source baseline. Exact AWS commercial offerings, pricing, quotas, certification rules, and support-plan details are release/time-sensitive and should always be checked against official AWS documentation before real production or exam decisions.

The additional learning sequence used throughout this enhancement is:

```text
Concept
  ↓
Detailed Explanation
  ↓
Architecture / Failure Model
  ↓
Command / Config / Calculation
  ↓
Expected Behavior
  ↓
Why It Works
  ↓
Production Example
  ↓
Troubleshooting
  ↓
Best Practice
```

## Advanced Deep Dive 1 — AWS Account as a Hard Administrative Boundary

### Concept and Detailed Explanation
An AWS account is more than a billing container. It is a strong isolation boundary for IAM, quotas, many service resources, CloudTrail context, and blast radius. Mature AWS environments intentionally separate production, security, log archive, networking, shared services, and sandbox workloads into different accounts.

Multi-account design limits the effect of compromised credentials or mistaken policies and improves cost and governance separation.

### Architecture / Failure Model
```text
AWS Organization
├─ Security Account
├─ Log Archive Account
├─ Network Account
├─ Production OU
│  ├─ App-Prod
│  └─ Data-Prod
└─ NonProd OU
   ├─ Dev
   └─ Sandbox
```

### Command / Config / Calculation
```text
aws sts get-caller-identity

# Before any write:
# verify Account and Arn in output.
```

### Expected Behavior
Operators can identify the account boundary before making changes and production is not mixed with experimentation.

### Why It Works
Many AWS permissions and resource limits are scoped by account; cross-account access must be explicitly established.

### Production Example
A developer with administrator access to a sandbox account cannot directly delete production resources because production lives in a different account.

### Troubleshooting Workflow
```text
wrong-account incident
  ↓
aws sts get-caller-identity
  ↓
profile/role source
  ↓
account purpose
  ↓
stop writes
  ↓
switch correct role/profile
```

### Best Practice
Make account identity verification the first step of every privileged AWS CLI workflow.

---

## Advanced Deep Dive 2 — Root User as an Emergency Identity

### Concept and Detailed Explanation
The root user has unique account-level authority and should not be a normal administrative identity. Protect root credentials, enforce MFA, avoid root access keys, and use federated or role-based administration for daily work.

The operational model should make root access rare, monitored, and recoverable.

### Architecture / Failure Model
```text
Root credentials
   |
offline / strongly protected
   |
emergency-only account tasks

Daily admin
   |
IAM Identity Center / federated role
```

### Command / Config / Calculation
```text
Security checklist:
root MFA
no root access keys
root email controlled
root login alerts
break-glass procedure
periodic recovery test
```

### Expected Behavior
Routine cloud administration occurs without root sessions and any root use creates a high-priority audit event.

### Why It Works
Root bypasses many ordinary delegation patterns and therefore represents maximum account privilege.

### Production Example
An organization uses Identity Center for all engineers and stores root recovery credentials in a controlled emergency process.

### Troubleshooting Workflow
```text
root login observed
  ↓
was it authorized?
  ↓
CloudTrail/account audit
  ↓
credential/MFA review
  ↓
contain if unexpected
```

### Best Practice
Treat root login like use of a physical master key.

---

## Advanced Deep Dive 3 — IAM Policy Evaluation as Layered Authorization

### Concept and Detailed Explanation
AWS authorization can involve identity policies, resource policies, SCPs, permission boundaries, session policies, VPC endpoint policies, and service-specific controls. An allow in one policy does not guarantee access because another layer can restrict it.

A practical mental model is: authenticate the principal, collect applicable permission boundaries, then evaluate explicit denies before effective allows.

### Architecture / Failure Model
```text
Principal authenticated
   |
identity policy
resource policy
SCP
permission boundary
session policy
service control
   |
explicit deny?
  / yes  no
 |    |
DENY  evaluate allowed action/resource/condition
```

### Command / Config / Calculation
```text
# Inspect caller
aws sts get-caller-identity

# Policy simulation where authorized:
aws iam simulate-principal-policy   --policy-source-arn <PRINCIPAL_ARN>   --action-names s3:GetObject   --resource-arns arn:aws:s3:::example-bucket/object 2>/dev/null || true
```

### Expected Behavior
An AccessDenied investigation identifies the exact policy layer limiting the action instead of simply adding AdministratorAccess.

### Why It Works
AWS deliberately composes multiple policy types so central governance can bound local permissions.

### Production Example
An IAM role allows EC2 creation, but an Organizations SCP denies unapproved Regions; the request remains denied.

### Troubleshooting Workflow
```text
AccessDenied
  ↓
caller identity
  ↓
action/resource
  ↓
explicit deny?
  ↓
SCP/boundary/session/resource policy
  ↓
conditions
```

### Best Practice
Never troubleshoot IAM by broadening privileges until the denying layer is understood.

---

## Advanced Deep Dive 4 — IAM Role Trust Policy vs Permission Policy

### Concept and Detailed Explanation
An IAM role has two separate questions: who may assume the role, and what the role may do after assumption. The trust policy answers the first; permission policies answer the second.

Confusing them is a common source of cross-account and service-role failures.

### Architecture / Failure Model
```text
Caller
  |
role trust policy:
"May this principal assume me?"
  |
STS session
  |
role permission policy:
"What may this session do?"
  |
AWS resource
```

### Command / Config / Calculation
```text
# Read role metadata
aws iam get-role --role-name <ROLE_NAME> 2>/dev/null || true

# List attached policies
aws iam list-attached-role-policies   --role-name <ROLE_NAME> 2>/dev/null || true
```

### Expected Behavior
A role can be assumed only by trusted principals and the resulting session receives only intended permissions.

### Why It Works
STS separates role assumption authorization from the permissions granted to the session.

### Production Example
A cross-account role has correct S3 permissions but cannot be assumed because the source account principal is missing from the trust policy.

### Troubleshooting Workflow
```text
AssumeRole denied
  ↓
source principal identity
  ↓
target role trust policy
  ↓
external ID/MFA/condition?
  ↓
source permission to sts:AssumeRole
```

### Best Practice
Debug role assumption before debugging the permissions the role would have after assumption.

---

## Advanced Deep Dive 5 — STS Temporary Credentials and Session Lifetime

### Concept and Detailed Explanation
STS issues temporary access key, secret key, and session token credentials. They expire automatically and can carry session context such as role session name, tags, and external identity information.

Temporary credentials dramatically reduce the risk of forgotten permanent keys, but applications must refresh them correctly.

### Architecture / Failure Model
```text
Human/workload identity
   |
AssumeRole / federation
   |
STS
   |
temporary key + secret + session token
   |
expiry
```

### Command / Config / Calculation
```text
aws sts get-caller-identity

# In SDKs/managed environments, prefer provider credential chains
# rather than manually exporting long-lived keys.
```

### Expected Behavior
Long-running workloads refresh role credentials before expiry without storing permanent access keys.

### Why It Works
AWS SDK credential providers can automatically retrieve and renew temporary credentials from supported identity sources.

### Production Example
An EC2 application uses its instance role; the SDK refreshes temporary credentials automatically.

### Troubleshooting Workflow
```text
ExpiredToken
  ↓
credential source
  ↓
session expiry
  ↓
SDK/provider refresh?
  ↓
clock skew?
  ↓
reauthenticate
```

### Best Practice
Use SDK/provider credential chains instead of manually copying STS credentials into files.

---

## Advanced Deep Dive 6 — IAM Identity Center Permission Sets

### Concept and Detailed Explanation
IAM Identity Center maps workforce users/groups to permission sets that materialize as roles in target AWS accounts. This creates centralized access governance without creating separate IAM users in every account.

The permission set defines the AWS permissions, while the assignment defines who receives them in which account.

### Architecture / Failure Model
```text
Corporate IdP / Identity Center
       |
User / Group
       |
Permission Set
       |
Account Assignment
       |
AWS role session
```

### Command / Config / Calculation
```text
aws sso login --profile <profile> 2>/dev/null || true
aws sts get-caller-identity --profile <profile> 2>/dev/null || true
```

### Expected Behavior
One workforce identity can receive different scoped roles across dev, production, and security accounts.

### Why It Works
Identity Center centralizes authentication and creates temporary role sessions in member accounts.

### Production Example
Platform engineers receive Admin in sandbox but ReadOnly in security accounts through separate permission-set assignments.

### Troubleshooting Workflow
```text
user cannot access account
  ↓
identity synced?
  ↓
account assignment?
  ↓
permission set provisioned?
  ↓
session/login profile?
```

### Best Practice
Manage workforce access through groups and permission-set assignments rather than per-user account exceptions.

---

## Advanced Deep Dive 7 — SCPs as Maximum-Permission Guardrails

### Concept and Detailed Explanation
Service Control Policies do not grant permissions. They define what member-account principals can ever be allowed to do. Effective permission still requires an IAM or resource policy allow.

This makes SCPs suitable for organization-wide invariants such as restricting Regions or preventing security-log deletion.

### Architecture / Failure Model
```text
IAM policy says ALLOW
        |
SCP maximum boundary
        |
if action outside SCP boundary
        ↓
      DENY
```

### Command / Config / Calculation
```text
SCP design examples:
deny leaving Organization
deny disabling audit trail
deny unsupported Regions
deny creation of root access keys
```

### Expected Behavior
Local account administrators cannot bypass organization-level prohibited actions through their own IAM policies.

### Why It Works
SCP evaluation limits member accounts from above the account level.

### Production Example
A production administrator has AdministratorAccess but cannot disable the organization security trail because an SCP denies the action.

### Troubleshooting Workflow
```text
unexpected SCP denial
  ↓
which OU/account?
  ↓
policies inherited?
  ↓
explicit deny?
  ↓
is exception legitimate?
```

### Best Practice
Keep SCPs focused on high-value invariants and test them in lower-risk OUs before broad attachment.

---

## Advanced Deep Dive 8 — VPC as a Regional Routing Domain

### Concept and Detailed Explanation
An Amazon VPC is regional. Subnets are zonal slices of the VPC address space. Route tables, gateways, security controls, DNS options, and endpoints combine to determine how workloads communicate.

The VPC should be treated as a routed network design, not merely a prerequisite wizard step.

### Architecture / Failure Model
```text
Region
└─ VPC 10.20.0.0/16
   ├─ Subnet A 10.20.1.0/24 → AZ-A
   ├─ Subnet B 10.20.2.0/24 → AZ-B
   ├─ route tables
   ├─ gateways/endpoints
   └─ security controls
```

### Command / Config / Calculation
```text
aws ec2 describe-vpcs --output table 2>/dev/null || true
aws ec2 describe-subnets --output table 2>/dev/null || true
aws ec2 describe-route-tables --output json 2>/dev/null || true
```

### Expected Behavior
You can trace a source subnet through its associated route table to the intended next hop.

### Why It Works
VPC routing is defined by longest-prefix-match routes attached to subnet routing contexts.

### Production Example
An EC2 instance is healthy but cannot reach on-prem because its subnet uses a route table that lacks the Transit Gateway route.

### Troubleshooting Workflow
```text
connectivity issue
  ↓
source ENI/subnet
  ↓
associated route table
  ↓
next hop
  ↓
security group/NACL
  ↓
return route
```

### Best Practice
Start VPC troubleshooting from the source ENI and subnet, not from a generic VPC diagram.

---

## Advanced Deep Dive 9 — Public Subnet Is a Routing Property

### Concept and Detailed Explanation
A subnet becomes 'public' when its route table has a route to an Internet Gateway, but an EC2 instance still needs a public IPv4/IPv6 path and security policy to be Internet-reachable. Merely placing a resource in a public subnet does not expose it automatically.

### Architecture / Failure Model
```text
EC2
  |
public IP?
  |
subnet route 0.0.0.0/0 → IGW?
  |
security group?
  |
NACL?
  |
Internet
```

### Command / Config / Calculation
```text
aws ec2 describe-route-tables   --filters Name=association.subnet-id,Values=<SUBNET_ID>   2>/dev/null || true
```

### Expected Behavior
Internet reachability is explained by address, route, and security layers together.

### Why It Works
AWS separates public addressing, routing, and firewall policy into independent controls.

### Production Example
An instance in a public subnet remains unreachable because it has no public IP.

### Troubleshooting Workflow
```text
EC2 Internet inbound fails
  ↓
public address?
  ↓
route to IGW?
  ↓
SG inbound?
  ↓
NACL?
  ↓
OS/app listening?
```

### Best Practice
Do not use the label 'public subnet' as proof that a workload is publicly reachable.

---

## Advanced Deep Dive 10 — NAT Gateway Architecture and AZ Failure

### Concept and Detailed Explanation
A NAT Gateway enables private IPv4 workloads to initiate Internet-bound connections. For resilient designs, NAT should be placed per Availability Zone with each private subnet routing to the NAT in the same AZ, avoiding cross-AZ dependency and traffic charges where architecture/pricing applies.

A single NAT for several AZs is cheaper in simple labs but can become a zonal single point for egress.

### Architecture / Failure Model
```text
AZ-A:
Private A → NAT-A → IGW

AZ-B:
Private B → NAT-B → IGW
```

### Command / Config / Calculation
```text
aws ec2 describe-nat-gateways 2>/dev/null || true
aws ec2 describe-route-tables 2>/dev/null || true
```

### Expected Behavior
Loss of one AZ does not remove outbound Internet access from private workloads in another healthy AZ.

### Why It Works
NAT Gateway is deployed in a subnet/AZ and private subnet route tables explicitly choose it as next hop.

### Production Example
A two-AZ application uses one NAT in AZ-A; when AZ-A fails, private instances in AZ-B cannot reach external package/API endpoints.

### Troubleshooting Workflow
```text
private egress failure
  ↓
subnet route
  ↓
NAT state/AZ
  ↓
public subnet route to IGW
  ↓
NACL/DNS/external service
```

### Best Practice
For production multi-AZ egress, align NAT failure domains with private subnet AZs.

---

## Advanced Deep Dive 11 — Security Groups as Stateful ENI Policy

### Concept and Detailed Explanation
Security groups are stateful allow-list policies associated with ENIs and supported resources. They support referencing other security groups, which expresses application relationships more robustly than hard-coded IP ranges.

They do not support explicit deny rules; absence of allow means denied.

### Architecture / Failure Model
```text
Internet
  |
ALB-SG allows 443 from users
  |
Web-SG allows 8080 from ALB-SG
  |
DB-SG allows 5432 from Web-SG
```

### Command / Config / Calculation
```text
aws ec2 describe-security-groups   --group-ids <SG_ID> 2>/dev/null || true
```

### Expected Behavior
Backend tiers accept traffic only from intended upstream security identities.

### Why It Works
Stateful connection tracking automatically permits return traffic for allowed sessions.

### Production Example
A database security group references the application security group rather than the application's changing autoscaling IP addresses.

### Troubleshooting Workflow
```text
connection denied
  ↓
source ENI/SG
  ↓
destination SG rule
  ↓
protocol/port
  ↓
NACL/route
  ↓
service listening
```

### Best Practice
Prefer security-group references for tier-to-tier access inside AWS where supported.

---

## Advanced Deep Dive 12 — NACLs, Stateless Rules, and Ephemeral Ports

### Concept and Detailed Explanation
Network ACLs are stateless subnet-level filters. Both request and response traffic must match rules, including ephemeral client ports. This makes NACL troubleshooting different from security groups.

NACLs can provide coarse subnet guardrails but should not become an unnecessarily complex second firewall rule system.

### Architecture / Failure Model
```text
Client ephemeral port 50000
   ↓ TCP/443
Server

Return:
Server 443
   ↓ TCP/50000
Client

NACL evaluates both directions separately
```

### Command / Config / Calculation
```text
aws ec2 describe-network-acls 2>/dev/null || true
```

### Expected Behavior
Allowed application flows include both forward and return NACL rules while security groups handle stateful workload policy.

### Why It Works
Stateless filters do not remember connection state.

### Production Example
HTTPS inbound is allowed, but return ephemeral ports are denied by the NACL, causing connection failures despite a correct security group.

### Troubleshooting Workflow
```text
SG looks correct but traffic fails
  ↓
NACL inbound
  ↓
NACL outbound
  ↓
ephemeral port range
  ↓
route
```

### Best Practice
Keep NACL rules simple and document why each explicit deny/allow exists.

---

## Advanced Deep Dive 13 — VPC Endpoints and Private AWS Service Access

### Concept and Detailed Explanation
VPC endpoints allow private communication with supported AWS services without requiring a public Internet/NAT path. Gateway endpoints and interface endpoints have different implementations and supported services.

Endpoint policies, route changes, private DNS, and security groups can all affect access.

### Architecture / Failure Model
```text
Private EC2
   |
VPC Endpoint
   |
AWS Service
(no Internet/NAT required for that path)
```

### Command / Config / Calculation
```text
aws ec2 describe-vpc-endpoints 2>/dev/null || true

# Check DNS from instance:
getent hosts <service-endpoint> 2>/dev/null || true
```

### Expected Behavior
Private workloads reach the AWS service using the configured private endpoint path.

### Why It Works
Endpoints insert service-specific private connectivity into the VPC routing/DNS model.

### Production Example
A private application stops paying NAT data-processing cost for large S3 transfers after using an S3 gateway endpoint.

### Troubleshooting Workflow
```text
endpoint access fails
  ↓
endpoint state
  ↓
route/private DNS
  ↓
endpoint policy
  ↓
SG for interface endpoint
  ↓
IAM/resource policy
```

### Best Practice
Remember that endpoint policy is an additional authorization layer, not a replacement for IAM.

---

## Advanced Deep Dive 14 — Transit Gateway Route-Table Segmentation

### Concept and Detailed Explanation
AWS Transit Gateway can provide hub-and-spoke connectivity, but attaching every VPC to one shared route domain can create excessive lateral reachability. Separate TGW route tables can segment production, nonproduction, shared services, and inspection paths.

Connectivity and security design therefore depend on both attachment and route-table association/propagation.

### Architecture / Failure Model
```text
Prod VPCs ----               > TGW Prod RT ---- Firewall/Shared
NonProd VPCs -> TGW NonProd RT
On-Prem ------> TGW Hybrid RT
```

### Command / Config / Calculation
```text
aws ec2 describe-transit-gateway-attachments 2>/dev/null || true
aws ec2 describe-transit-gateway-route-tables 2>/dev/null || true
```

### Expected Behavior
Only approved segments learn routes to each other and return paths remain symmetric through required inspection.

### Why It Works
Transit Gateway uses independent routing domains to control which attachments exchange prefixes.

### Production Example
A sandbox VPC is attached to the TGW but cannot reach production because it is associated with a separate route table.

### Troubleshooting Workflow
```text
TGW flow fails
  ↓
attachment state
  ↓
route-table association
  ↓
route propagation/static routes
  ↓
inspection path
  ↓
VPC return routes
```

### Best Practice
Treat TGW route tables as security segmentation boundaries, not just routing tables.

---

## Advanced Deep Dive 15 — Route 53 DNS Routing vs Load Balancing

### Concept and Detailed Explanation
Route 53 makes DNS answers based on routing policies and health checks; it does not proxy every application connection like an ALB. DNS clients cache answers according to TTL, so failover is not instant in the same way as a connection-level load balancer health decision.

Use DNS routing for endpoint/region selection and load balancers for per-request/backend distribution.

### Architecture / Failure Model
```text
User DNS query
   |
Route 53 policy
   |
returns endpoint A or B
   |
client connects directly to endpoint/LB
```

### Command / Config / Calculation
```text
dig app.example.com
dig +trace app.example.com 2>/dev/null || true

Review:
record TTL
routing policy
health check
alias target
```

### Expected Behavior
DNS answers match the configured policy, but existing/cache-held client connections may continue using previous endpoints until TTL/session behavior changes.

### Why It Works
DNS controls name resolution, while load balancers control connection/request routing.

### Production Example
A multi-region app uses Route 53 failover between regional ALBs, and each ALB distributes traffic across instances in its Region.

### Troubleshooting Workflow
```text
DNS failover slow
  ↓
health-check state
  ↓
record policy
  ↓
TTL/cache
  ↓
client resolver
  ↓
target health
```

### Best Practice
Choose TTL based on change/failover requirements and query cost/behavior.

---

## Advanced Deep Dive 16 — CloudFront Cache Keys and Origin Load

### Concept and Detailed Explanation
CloudFront caching efficiency depends on the cache key: the combination of path, query strings, headers, and cookies used to identify a cached object. Including too many variable request attributes can destroy cache hit ratio and send most traffic back to the origin.

The best cache key includes only request data that truly changes the response.

### Architecture / Failure Model
```text
Viewer request
   |
cache key:
path + selected query/header/cookie
   |
cache hit? ---- yes → edge response
   |
  no
   |
origin request
```

### Command / Config / Calculation
```text
Review:
cache policy
origin request policy
TTL
query strings
cookies
headers
cache hit ratio
origin request count
```

### Expected Behavior
Frequently reusable content achieves a high cache hit ratio while personalized content varies only on necessary dimensions.

### Why It Works
CloudFront serves an object only when the incoming request maps to a matching cache key.

### Production Example
A site accidentally forwards every cookie into the cache key, reducing cache hits and increasing ALB/EC2 load.

### Troubleshooting Workflow
```text
origin load high
  ↓
CloudFront hit ratio
  ↓
cache key dimensions
  ↓
TTL
  ↓
cache-control headers
  ↓
origin errors/latency
```

### Best Practice
Keep cache keys minimal and intentional.

---

## Advanced Deep Dive 17 — CloudFront Origin Access Control

### Concept and Detailed Explanation
For private S3 origins, CloudFront can be the only intended public delivery path. Origin Access Control (OAC) allows CloudFront to access the bucket while the bucket remains nonpublic.

This separates public delivery from direct storage exposure.

### Architecture / Failure Model
```text
Users
  |
CloudFront
  |
OAC-signed origin request
  |
Private S3 bucket
```

### Command / Config / Calculation
```text
Security review:
S3 Block Public Access enabled
bucket policy allows CloudFront distribution
direct public object URL denied
CloudFront URL succeeds
```

### Expected Behavior
Objects are available through CloudFront but not through unauthenticated direct S3 access.

### Why It Works
OAC lets the S3 resource policy trust the CloudFront distribution/service path rather than the Internet.

### Production Example
A static website serves globally through CloudFront while the origin bucket remains private.

### Troubleshooting Workflow
```text
CloudFront 403
  ↓
distribution origin
  ↓
OAC configuration
  ↓
bucket policy
  ↓
object existence/KMS permissions
```

### Best Practice
Keep private origins private and expose only the delivery layer.

---

## Advanced Deep Dive 18 — Global Accelerator vs CloudFront Decision

### Concept and Detailed Explanation
Global Accelerator and CloudFront both use AWS global edge/network infrastructure but solve different primary problems. CloudFront is a content delivery network with caching and HTTP-oriented edge behavior. Global Accelerator provides static anycast IPs and accelerates traffic to healthy regional endpoints without requiring cache semantics.

### Architecture / Failure Model
```text
CloudFront:
viewer → edge cache → HTTP origin

Global Accelerator:
client → anycast IP → AWS backbone → regional endpoint
```

### Command / Config / Calculation
```text
Decision:
need caching? → CloudFront
need static global IP / TCP/UDP acceleration? → Global Accelerator
need both? architecture may combine services depending on use case
```

### Expected Behavior
The selected service matches protocol, caching, and endpoint-routing requirements.

### Why It Works
CloudFront optimizes content delivery; Global Accelerator optimizes network path and endpoint selection.

### Production Example
A gaming service using non-HTTP traffic chooses Global Accelerator, while static assets use CloudFront.

### Troubleshooting Workflow
```text
global performance issue
  ↓
protocol?
  ↓
cacheable content?
  ↓
static IP requirement?
  ↓
regional endpoint health?
```

### Best Practice
Choose by primary traffic behavior, not by the word 'global'.

---

## Advanced Deep Dive 19 — EC2 Boot Path and Troubleshooting

### Concept and Detailed Explanation
An EC2 instance must pass several layers before an application becomes reachable: AWS instance state, system status, instance status, networking, guest OS boot, filesystem mounts, cloud-init/user data, service startup, and application health.

The console showing `running` proves only the EC2 control-plane state.

### Architecture / Failure Model
```text
EC2 state = running
   |
system status
   |
instance status
   |
network
   |
OS boot
   |
cloud-init
   |
service
   |
application
```

### Command / Config / Calculation
```text
aws ec2 describe-instance-status   --instance-ids <INSTANCE_ID> 2>/dev/null || true

# On host:
systemctl --failed
journalctl -b -p err
cloud-init status 2>/dev/null || true
```

### Expected Behavior
Engineers can determine whether failure belongs to AWS infrastructure, guest OS, bootstrap, or application.

### Why It Works
EC2 health separates underlying host/platform checks from guest-instance reachability checks.

### Production Example
An instance is `running` but fails its instance-status check because the guest kernel is hung.

### Troubleshooting Workflow
```text
EC2 unreachable
  ↓
instance state
  ↓
system check
  ↓
instance check
  ↓
ENI/routes/SG
  ↓
OS/service
```

### Best Practice
Use EC2 status checks before assuming SSH or application configuration is the root cause.

---

## Advanced Deep Dive 20 — AMI Lifecycle and Golden Image Pipelines

### Concept and Detailed Explanation
An AMI should be treated as a versioned build artifact, not a manually patched mystery snapshot. A repeatable pipeline starts from a trusted base, patches/hardens it, installs agents, validates it, publishes a new AMI, and records source/build metadata.

The old AMI remains available for rollback until retention policy removes it.

### Architecture / Failure Model
```text
Base AMI
   |
Packer/Image Builder pipeline
   |
patch + harden
   |
test
   |
publish AMI v2
   |
launch template
   |
Auto Scaling rollout
```

### Command / Config / Calculation
```text
AMI metadata:
source_ami
build_commit
build_date
security_scan
owner
deprecation_date
```

### Expected Behavior
Each running fleet instance maps to a known tested AMI version.

### Why It Works
Immutable image pipelines reduce configuration drift and support replacement rather than in-place repair.

### Production Example
A new critical OS patch produces AMI v2026.08.20 and an Auto Scaling rolling replacement.

### Troubleshooting Workflow
```text
unknown AMI in fleet
  ↓
instance ImageId
  ↓
AMI tags/metadata
  ↓
build provenance
  ↓
replace with approved image
```

### Best Practice
Never make manual production EC2 changes that are not reflected in the image/configuration source of truth.

---

## Advanced Deep Dive 21 — Launch Templates as Fleet Contracts

### Concept and Detailed Explanation
A launch template defines the repeatable EC2 configuration used by Auto Scaling and other launch workflows: AMI, instance type, security groups, IAM instance profile, user data, storage, metadata settings, and more.

Versioning the launch template lets a fleet roll forward or back deliberately.

### Architecture / Failure Model
```text
Launch Template v1
   |
ASG instances

Update → Launch Template v2
   |
instance refresh
   |
new fleet
```

### Command / Config / Calculation
```text
aws ec2 describe-launch-template-versions   --launch-template-id <LT_ID> 2>/dev/null || true
```

### Expected Behavior
New instances are created from one explicit template version rather than ad hoc console state.

### Why It Works
Auto Scaling needs a deterministic specification for replacement capacity.

### Production Example
An instance refresh replaces old AMI instances with a new hardened launch-template version.

### Troubleshooting Workflow
```text
new instances misconfigured
  ↓
ASG launch template version
  ↓
AMI
  ↓
user data
  ↓
IAM profile
  ↓
SG/subnets
```

### Best Practice
Pin production Auto Scaling groups to a controlled launch-template version or managed default policy.

---

## Advanced Deep Dive 22 — Auto Scaling Group Desired, Minimum, and Maximum Capacity

### Concept and Detailed Explanation
An Auto Scaling Group maintains a desired number of EC2 instances within minimum and maximum bounds. Scaling policies change desired capacity, while health checks can replace unhealthy members.

If minimum capacity is below the application's redundancy requirement, scale-in can violate availability even though the ASG is functioning correctly.

### Architecture / Failure Model
```text
min ≤ desired ≤ max

policy/health event
   |
desired changes
   |
ASG launches/terminates
```

### Command / Config / Calculation
```text
aws autoscaling describe-auto-scaling-groups   --auto-scaling-group-names <ASG> 2>/dev/null || true
```

### Expected Behavior
The group maintains at least the required healthy baseline and can scale toward the configured maximum.

### Why It Works
ASG reconciliation continuously compares desired member count with observed healthy instances.

### Production Example
A two-AZ app sets min=2 so normal scale-in cannot reduce the service to one instance.

### Troubleshooting Workflow
```text
ASG not scaling
  ↓
policy alarm/metric
  ↓
desired/min/max
  ↓
launch failures
  ↓
subnet capacity/quota
  ↓
health checks
```

### Best Practice
Set minimum capacity from availability requirements, not only average demand.

---

## Advanced Deep Dive 23 — Instance Refresh and Controlled Fleet Replacement

### Concept and Detailed Explanation
Instance Refresh can roll an Auto Scaling Group onto a new launch-template/AMI configuration while maintaining a minimum healthy percentage. It is safer than terminating the whole fleet manually.

Warm-up and checkpoint behavior matter because newly launched instances may need time before they can carry production load.

### Architecture / Failure Model
```text
Old fleet
  |
replace batch
  |
new instances launch
  |
warm up + health
  |
next batch
  |
all new version
```

### Command / Config / Calculation
```text
Refresh design:
minimum_healthy_percentage
instance_warmup
checkpoint_percentage
rollback criteria
launch template version
```

### Expected Behavior
Fleet replacement preserves application capacity and stops when new instances fail health criteria.

### Why It Works
Rolling replacement constrains simultaneous change and lets health signals gate progress.

### Production Example
A bad AMI fails ALB health checks; the refresh stops before every old instance is removed.

### Troubleshooting Workflow
```text
refresh stuck
  ↓
new instance launch?
  ↓
health check?
  ↓
warmup time?
  ↓
capacity/quota?
  ↓
template version?
```

### Best Practice
Use health-gated rolling replacement for immutable EC2 fleets.

---

## Advanced Deep Dive 24 — EBS Volume Type Selection by Workload

### Concept and Detailed Explanation
EBS is block storage, but different volume families trade cost, IOPS, throughput, and latency characteristics. Cloud Practitioner does not require deep tuning, yet an engineer must understand that database random I/O and large sequential throughput workloads have different storage needs.

Also check the EC2 instance's own EBS bandwidth limit; a faster volume cannot exceed the host path.

### Architecture / Failure Model
```text
Application
   |
EC2 instance EBS bandwidth
   |
EBS volume
   |
IOPS / throughput / latency
```

### Command / Config / Calculation
```text
# Guest evidence
lsblk
iostat -xz 1 5 2>/dev/null || true

# AWS-side
aws ec2 describe-volumes   --volume-ids <VOLUME_ID> 2>/dev/null || true
```

### Expected Behavior
Storage selection matches the measured I/O pattern and neither volume nor instance path is an unexplained bottleneck.

### Why It Works
EBS performance has service limits and host attachment limits.

### Production Example
A database provisions high IOPS but remains throughput-limited by its smaller EC2 instance's EBS bandwidth.

### Troubleshooting Workflow
```text
EBS slow
  ↓
guest queue/latency
  ↓
volume type/provisioned limits
  ↓
instance EBS bandwidth
  ↓
burst/throughput
```

### Best Practice
Benchmark storage with the actual EC2 instance type and workload pattern.

---

## Advanced Deep Dive 25 — EBS Snapshots and Application Consistency

### Concept and Detailed Explanation
EBS snapshots capture block state, but a crash-consistent block snapshot is not automatically application-consistent. Databases and transactional applications may need filesystem freeze, application quiescing, or native backup integration so in-memory transactions and logs are in a recoverable state.

### Architecture / Failure Model
```text
Application memory
   |
filesystem buffers
   |
EBS blocks
   |
snapshot

Application-consistent backup:
quiesce/flush → snapshot → resume
```

### Command / Config / Calculation
```text
Backup procedure:
1. app-native checkpoint/flush
2. filesystem sync/quiesce if required
3. create snapshot
4. verify snapshot completion
5. periodic restore test
```

### Expected Behavior
Restored snapshots boot and the application/database passes integrity checks.

### Why It Works
EBS can copy blocks consistently at the storage layer without understanding application transaction semantics.

### Production Example
A database volume snapshot restores, but recovery takes longer because dirty in-memory state was not quiesced.

### Troubleshooting Workflow
```text
snapshot restore problem
  ↓
volume attaches?
  ↓
filesystem integrity
  ↓
DB crash recovery
  ↓
native logs/backups
```

### Best Practice
Define whether each backup needs crash consistency or application consistency.

---

## Advanced Deep Dive 26 — S3 Bucket Policy, IAM Policy, and Access Points

### Concept and Detailed Explanation
S3 access can involve IAM identity policy, bucket policy, access-point policy, KMS policy, VPC endpoint policy, Block Public Access, and object ownership settings. A single `Allow` is not enough if another layer denies the request.

S3 Access Points can provide separate access-policy entry points for different applications sharing one bucket.

### Architecture / Failure Model
```text
Principal
  |
IAM policy
  |
S3 access point / bucket policy
  |
Block Public Access
  |
KMS key policy if encrypted
  |
Object
```

### Command / Config / Calculation
```text
aws s3api get-bucket-policy --bucket <BUCKET> 2>/dev/null || true
aws s3api get-public-access-block --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-encryption --bucket <BUCKET> 2>/dev/null || true
```

### Expected Behavior
Applications receive narrow, explainable access paths without making the bucket broadly public.

### Why It Works
S3 combines identity and resource policies with service guardrails.

### Production Example
Analytics and backup applications use separate access points with different prefixes and policies against one data bucket.

### Troubleshooting Workflow
```text
S3 AccessDenied
  ↓
caller identity
  ↓
IAM action/resource
  ↓
bucket/access-point policy
  ↓
Block Public Access
  ↓
KMS
  ↓
endpoint policy
```

### Best Practice
Troubleshoot S3 authorization as a layered policy evaluation.

---

## Advanced Deep Dive 27 — S3 Versioning, Replication, and Delete Protection

### Concept and Detailed Explanation
S3 versioning preserves historical object versions. Replication can copy versions to another bucket, Region, or account depending on configuration. For cyber resilience, destination-account separation and Object Lock can create a stronger recovery boundary.

Replication is not backup by itself because destructive changes can also replicate.

### Architecture / Failure Model
```text
Source bucket
 versioning
   |
replication
   |
Destination bucket
 versioning
 Object Lock / separate account
```

### Command / Config / Calculation
```text
aws s3api get-bucket-versioning --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-replication --bucket <BUCKET> 2>/dev/null || true
```

### Expected Behavior
Operators can recover prior object versions and know which replica/backup copies are protected from deletion.

### Why It Works
Version IDs and replication provide independent object copies, while retention controls restrict destructive operations.

### Production Example
Production objects replicate cross-account into a security-owned backup bucket with retention controls.

### Troubleshooting Workflow
```text
object deleted
  ↓
source versions
  ↓
replica versions
  ↓
delete marker replicated?
  ↓
locked backup?
  ↓
restore
```

### Best Practice
Design S3 recovery for accidental and malicious deletion separately.

---

## Advanced Deep Dive 28 — S3 Lifecycle and Cost Without Destroying Recovery

### Concept and Detailed Explanation
Lifecycle rules can transition current and noncurrent object versions or expire them. Aggressive expiration can silently remove the historical versions or backups you expected to use during recovery.

Lifecycle design should reflect retention policy, restore time, retrieval charges, and legal requirements.

### Architecture / Failure Model
```text
Current object
  ↓ age
Standard → IA → Archive

Noncurrent versions
  ↓ separate policy
retain → archive → expire
```

### Command / Config / Calculation
```text
Lifecycle worksheet:
current version transition
noncurrent version transition
noncurrent expiration
delete markers
minimum retention
legal hold
restore RTO
```

### Expected Behavior
Storage cost declines over time without violating required recovery or compliance periods.

### Why It Works
S3 lifecycle operates automatically according to age/state, so a mistaken rule can systematically delete large datasets.

### Production Example
A team archives logs after 90 days but retains seven years of compliance records instead of expiring all noncurrent versions after one year.

### Troubleshooting Workflow
```text
unexpected object versions gone
  ↓
lifecycle policy history
  ↓
versioning
  ↓
retention/Object Lock
  ↓
backup copy
```

### Best Practice
Review lifecycle policies like destructive code changes.

---

## Advanced Deep Dive 29 — RDS Multi-AZ Failover Mechanics

### Concept and Detailed Explanation
RDS Multi-AZ is designed for availability, not read scaling. The service maintains a standby/secondary architecture and redirects the database endpoint during failover according to engine/deployment design.

Applications should connect using the DNS endpoint, use retry logic, and tolerate a brief connection interruption.

### Architecture / Failure Model
```text
App
  |
RDS DNS endpoint
  |
Primary AZ-A
  ⇄ managed replication
Standby AZ-B

Failure
  ↓
endpoint resolves/routes to new primary
```

### Command / Config / Calculation
```text
Application settings:
connect_timeout
retry_with_backoff
connection_pool_recycle
DNS-respecting client
transaction retry policy
```

### Expected Behavior
After failover, the application reconnects through the same logical database endpoint and resumes operation.

### Why It Works
RDS abstracts the active host behind a service endpoint so failover can change underlying infrastructure.

### Production Example
An AZ event causes RDS failover; applications using robust connection pools recover while one app with a hard-coded IP stays broken.

### Troubleshooting Workflow
```text
RDS failover incident
  ↓
AWS/RDS event
  ↓
endpoint DNS
  ↓
app connection pool
  ↓
retry behavior
  ↓
transaction consistency
```

### Best Practice
Never hard-code managed database IP addresses.

---

## Advanced Deep Dive 30 — RDS Read Replicas and Read Scaling

### Concept and Detailed Explanation
Read replicas copy data from a primary and serve read workloads. They can reduce read pressure and support some DR patterns, but replication is generally asynchronous for standard read-replica architectures, so applications must tolerate replica lag.

They are not a substitute for Multi-AZ high availability.

### Architecture / Failure Model
```text
Writes → Primary
           |
      async replication
       /          Read Replica 1  Read Replica 2
  ↑ reads            ↑ reads
```

### Command / Config / Calculation
```text
Read-scaling design:
write endpoint
read endpoint(s)
maximum acceptable replica lag
read-after-write requirement
promotion/failover plan
```

### Expected Behavior
Read-heavy traffic is distributed while write consistency requirements still use the primary when necessary.

### Why It Works
Asynchronous replicas trade strict freshness for scale and geographic flexibility.

### Production Example
A reporting workload moves to a read replica so expensive SELECT queries no longer compete with OLTP writes.

### Troubleshooting Workflow
```text
stale read
  ↓
replica lag
  ↓
read-after-write requirement?
  ↓
route critical read to primary
```

### Best Practice
Use replicas only for reads that can tolerate their consistency characteristics.

---

## Advanced Deep Dive 31 — Aurora Cluster Endpoint vs Reader Endpoint

### Concept and Detailed Explanation
Aurora exposes cluster-level endpoints that abstract the current writer and reader fleet. The writer endpoint follows the primary instance, while reader endpoints can distribute read connections across replicas.

Applications should use endpoint purpose instead of pinning to individual instance endpoints unless there is a specific operational reason.

### Architecture / Failure Model
```text
Application writes
   |
Writer Endpoint
   |
Aurora writer

Application reads
   |
Reader Endpoint
   |
Aurora replicas
```

### Command / Config / Calculation
```text
Connection design:
write_dsn = cluster_writer_endpoint
read_dsn  = cluster_reader_endpoint
connection_retry = enabled
```

### Expected Behavior
Writes follow the active writer after failover and read traffic can use replicas.

### Why It Works
Aurora's service endpoints decouple application connection strings from specific DB instances.

### Production Example
A reporting service uses the reader endpoint while the transactional application writes through the cluster endpoint.

### Troubleshooting Workflow
```text
Aurora connectivity issue
  ↓
which endpoint?
  ↓
writer/reader role
  ↓
DNS
  ↓
security group
  ↓
cluster event/failover
```

### Best Practice
Use logical service endpoints, not fixed instance addresses, for normal application connectivity.

---

## Advanced Deep Dive 32 — DynamoDB Partition-Key Design

### Concept and Detailed Explanation
DynamoDB scales by partitioning data. The partition key determines how items distribute across storage/throughput partitions. A low-cardinality or highly skewed key can create hot partitions even when total table capacity looks sufficient.

The first design question is therefore access pattern and key distribution, not table column structure.

### Architecture / Failure Model
```text
Requests
  |
partition key
  |
hash/distribution
  |
+-- Partition A
+-- Partition B
+-- Partition C
```

### Command / Config / Calculation
```text
Access-pattern worksheet:
operation
partition key
sort key
expected RPS
item size
key cardinality
hot-key risk
```

### Expected Behavior
Traffic distributes across many partition-key values rather than concentrating on one key.

### Why It Works
DynamoDB maps partition-key values to physical partitions and enforces throughput/storage limits at distributed boundaries.

### Production Example
Using `country=EG` as the only partition key for millions of high-rate events creates a hot key; using device/customer IDs distributes load better.

### Troubleshooting Workflow
```text
DynamoDB throttling
  ↓
table capacity mode
  ↓
hot partition/key?
  ↓
request distribution
  ↓
item size
  ↓
redesign key or shard
```

### Best Practice
Design DynamoDB from query/access patterns and traffic distribution.

---

## Advanced Deep Dive 33 — DynamoDB Conditional Writes and Idempotency

### Concept and Detailed Explanation
Distributed applications often retry requests. DynamoDB conditional expressions can enforce 'create only if absent', version checks, or state transitions so a retry does not overwrite unexpected data.

This is a practical way to implement optimistic concurrency and idempotent workflows.

### Architecture / Failure Model
```text
Client retry
  |
Put/Update with condition
  |
condition true → commit
condition false → reject safely
```

### Command / Config / Calculation
```text
# Conceptual condition:
attribute_not_exists(order_id)

# Or optimistic version:
expected version = 7
update → version 8
```

### Expected Behavior
Duplicate create attempts fail safely instead of producing a second logical object or overwriting a newer version.

### Why It Works
Conditional writes move concurrency checks into the atomic database operation.

### Production Example
A payment callback retries; the item is created only once because `attribute_not_exists(payment_id)` protects the write.

### Troubleshooting Workflow
```text
conditional check failed
  ↓
duplicate request?
  ↓
stale version?
  ↓
read current item
  ↓
decide retry/merge/reject
```

### Best Practice
Use conditional writes for idempotency and optimistic concurrency instead of read-then-write races.

---

## Advanced Deep Dive 34 — ElastiCache Failure and Cache-Aside Behavior

### Concept and Detailed Explanation
ElastiCache should usually improve performance without becoming the sole source of business truth. In a cache-aside pattern, the application checks cache first, reads the database on miss, and repopulates cache.

The architecture must consider cache node failure, eviction, TTL, replication, and stampede behavior.

### Architecture / Failure Model
```text
App
  |
cache lookup
  | hit → return
  | miss
  v
Database
  |
populate cache
```

### Command / Config / Calculation
```text
Cache controls:
TTL
max memory/eviction
replication
failover
key naming
stampede protection
fallback to DB
```

### Expected Behavior
Cache loss temporarily increases database load but does not lose authoritative data.

### Why It Works
Cache entries are derived copies and can be rebuilt from the source of truth.

### Production Example
A cache node restarts; the application continues using RDS while cache warms back up.

### Troubleshooting Workflow
```text
cache outage
  ↓
app fallback works?
  ↓
DB load
  ↓
cache cluster health
  ↓
TTL/evictions
```

### Best Practice
Test the application with the cache unavailable.

---

## Advanced Deep Dive 35 — SQS Visibility Timeout and Duplicate Processing

### Concept and Detailed Explanation
When a consumer receives an SQS message, the message becomes temporarily invisible. If the consumer does not delete it before the visibility timeout expires, the message becomes available again.

The timeout should exceed normal processing time, and consumers should remain idempotent because duplicate delivery is still possible.

### Architecture / Failure Model
```text
Queue
  |
worker receives
  |
message hidden for visibility timeout
  |
success → delete
failure/timeout → visible again
```

### Command / Config / Calculation
```text
Design:
p95_processing_time = 45s
visibility_timeout  = > p99 + margin
max_receive_count   = bounded
DLQ                 = configured
```

### Expected Behavior
Normal jobs complete and delete before visibility expiry; failed jobs retry and eventually reach a DLQ if repeatedly unsuccessful.

### Why It Works
SQS separates receipt from final deletion so failed workers do not permanently lose messages.

### Production Example
A 3-minute video job uses a 30-second visibility timeout and gets processed by multiple workers; increasing/extending visibility fixes the retry timing.

### Troubleshooting Workflow
```text
duplicate SQS work
  ↓
processing duration
  ↓
visibility timeout
  ↓
delete/ack timing
  ↓
consumer idempotency
```

### Best Practice
Set visibility timeout from real processing-duration measurements.

---

## Advanced Deep Dive 36 — SQS FIFO Ordering Scope

### Concept and Detailed Explanation
FIFO queues provide ordering within message groups rather than one unlimited global ordered stream. Message-group IDs let independent groups process concurrently while preserving order inside each group.

A single group ID can serialize all work and become a throughput bottleneck.

### Architecture / Failure Model
```text
MessageGroup A:
A1 → A2 → A3 ordered

MessageGroup B:
B1 → B2 ordered

A and B can progress independently
```

### Command / Config / Calculation
```text
Design:
message_group_id = customer_id
deduplication_id = business_event_id
```

### Expected Behavior
Events for one logical entity remain ordered while unrelated entities can process in parallel.

### Why It Works
FIFO ordering is enforced per message group, enabling controlled concurrency.

### Production Example
Order events use `order_id` as the group key so updates for one order stay ordered while thousands of orders process concurrently.

### Troubleshooting Workflow
```text
FIFO throughput low
  ↓
all messages one group?
  ↓
group-key cardinality
  ↓
consumer concurrency
```

### Best Practice
Choose message groups around the smallest domain that truly requires ordering.

---

## Advanced Deep Dive 37 — SNS Fan-Out with Independent Queues

### Concept and Detailed Explanation
A common AWS pattern publishes one event to an SNS topic and delivers it to several SQS queues. Each consumer gets independent buffering, retry, scaling, and failure isolation.

This is more resilient than having one producer call every downstream service synchronously.

### Architecture / Failure Model
```text
Producer
  |
SNS Topic
  ├─ SQS Billing
  ├─ SQS Email
  └─ SQS Analytics
```

### Command / Config / Calculation
```text
Design:
topic event schema
subscriber filters
queue retry/DLQ
consumer idempotency
encryption/access policy
```

### Expected Behavior
Failure of one subscriber does not prevent other subscribers from receiving and processing the event.

### Why It Works
SNS distributes messages while SQS decouples delivery from consumer availability.

### Production Example
Order creation fans out to billing, notification, and analytics without coupling the API to each downstream service's uptime.

### Troubleshooting Workflow
```text
one subscriber missing events
  ↓
SNS subscription
  ↓
filter policy
  ↓
queue policy
  ↓
DLQ/delivery status
```

### Best Practice
Use separate queues when subscribers need independent retry and scaling.

---

## Advanced Deep Dive 38 — EventBridge Event Bus and Schema Boundaries

### Concept and Detailed Explanation
EventBridge routes events according to rules. It is useful for domain events, AWS service events, and SaaS integrations. The hard part is not creating a rule; it is designing stable event schemas, ownership, versioning, and retry behavior.

Consumers should not depend on undocumented fields that producers may change.

### Architecture / Failure Model
```text
Producer
  |
EventBridge Bus
  |
rules
  ├─ Lambda
  ├─ SQS
  └─ Step Functions
```

### Command / Config / Calculation
```text
Event envelope:
source
detail-type
id
time
detail:
  schema_version
  entity_id
  event_type
```

### Expected Behavior
Events can evolve without unexpectedly breaking every consumer.

### Why It Works
An event bus decouples producer routing from consumer implementation, but shared schema contracts remain necessary.

### Production Example
A manufacturing event includes schema_version so a new producer field does not break older consumers.

### Troubleshooting Workflow
```text
consumer broke after event change
  ↓
schema version
  ↓
rule pattern
  ↓
consumer assumptions
  ↓
compatibility/replay
```

### Best Practice
Treat event schemas as versioned APIs.

---

## Advanced Deep Dive 39 — Step Functions Retry and Compensation

### Concept and Detailed Explanation
Step Functions can coordinate serverless and AWS service workflows with retries, catches, branches, waits, and compensation logic. This makes failure handling explicit rather than buried in application code.

A retry should be used only for transient errors; deterministic business failures should follow alternate states.

### Architecture / Failure Model
```text
State A
  ↓
State B
  ├─ transient error → retry/backoff
  ├─ business reject → alternate path
  └─ fatal → compensation
```

### Command / Config / Calculation
```text
Retry:
  max_attempts
  interval_seconds
  backoff_rate

Catch:
  error_equals
  next: compensation_state
```

### Expected Behavior
Transient faults recover automatically while business failures follow predictable workflows.

### Why It Works
State-machine semantics externalize orchestration and failure transitions.

### Production Example
An image-processing workflow retries a temporary Lambda timeout but sends invalid-format files to a rejection path instead.

### Troubleshooting Workflow
```text
workflow stuck/failing
  ↓
execution history
  ↓
which state?
  ↓
retry exhausted?
  ↓
input/output shape
  ↓
compensation path
```

### Best Practice
Design retry, timeout, and compensation per state rather than one global error rule.

---

## Advanced Deep Dive 40 — Lambda Concurrency and Throttling

### Concept and Detailed Explanation
Lambda automatically scales, but account/function concurrency limits and downstream systems still bound safe throughput. Reserved concurrency can protect one function or protect the rest of the account from one runaway function.

Throttling can be healthy backpressure if events are buffered by SQS or EventBridge retry mechanisms.

### Architecture / Failure Model
```text
Burst
  |
Lambda concurrency
  |
downstream DB/API
  |
finite capacity
```

### Command / Config / Calculation
```text
Concurrency plan:
account_concurrency
reserved_function_concurrency
provisioned_concurrency_if_needed
queue depth
DB connection limit
```

### Expected Behavior
Function scaling does not exhaust shared account concurrency or overload downstream dependencies.

### Why It Works
Lambda allocates execution environments concurrently; quotas and reserved concurrency shape that allocation.

### Production Example
A queue consumer Lambda uses reserved concurrency 50 so it cannot create 500 simultaneous database connections.

### Troubleshooting Workflow
```text
Lambda throttled
  ↓
function concurrency
  ↓
account concurrency
  ↓
reserved concurrency
  ↓
event source retry/backlog
  ↓
downstream limit
```

### Best Practice
Use concurrency controls as architecture safety limits, not only performance knobs.

---

## Advanced Deep Dive 41 — Lambda Cold Start vs Provisioned Capacity

### Concept and Detailed Explanation
A cold start occurs when Lambda needs a new execution environment and initializes runtime/code before handling the request. Impact varies by runtime, package size, VPC/network setup, initialization work, and traffic pattern.

For latency-sensitive workloads, reduce initialization or use provisioned concurrency where justified.

### Architecture / Failure Model
```text
request
  |
existing warm environment?
 / yes  no
 |    |
run  initialize runtime/code
      |
      run
```

### Command / Config / Calculation
```text
Measure:
p50/p95/p99 duration
init duration
package size
dependency initialization
concurrency burst
```

### Expected Behavior
Latency SLOs are based on measured cold and warm behavior, not assumptions.

### Why It Works
Elastic serverless platforms create execution environments on demand.

### Production Example
A low-latency API sees p99 spikes during morning traffic bursts because new function environments initialize expensive libraries.

### Troubleshooting Workflow
```text
Lambda latency spike
  ↓
init duration?
  ↓
cold-start frequency
  ↓
package/runtime
  ↓
VPC/dependency initialization
  ↓
provisioned concurrency if justified
```

### Best Practice
Optimize initialization before paying for permanently warm capacity.

---

## Advanced Deep Dive 42 — API Gateway Throttling and Abuse Protection

### Concept and Detailed Explanation
API Gateway can enforce request throttling/quotas and integrate authentication, WAF, and backend routing. Throttling protects backend capacity and provides a clear failure mode instead of letting overload cascade into databases and functions.

Rate limits should reflect business plans and downstream capacity.

### Architecture / Failure Model
```text
Clients
  |
WAF/Auth
  |
API Gateway
  |
throttle
  |
Lambda / service
```

### Command / Config / Calculation
```text
Rate policy:
steady_rate
burst
per-client/API-key quota if used
backend max throughput
429 retry guidance
```

### Expected Behavior
Excess traffic receives controlled throttling while healthy request volume continues.

### Why It Works
API Gateway can reject traffic before consuming expensive backend capacity.

### Production Example
A public API limits burst traffic so a bot cannot create unbounded Lambda concurrency.

### Troubleshooting Workflow
```text
API returns 429
  ↓
usage plan/throttle
  ↓
account/service quotas
  ↓
backend saturation
  ↓
client retry behavior
```

### Best Practice
Return clear retry semantics and use exponential backoff for throttled clients.

---

## Advanced Deep Dive 43 — Athena Cost and Partition Design

### Concept and Detailed Explanation
Athena is serverless SQL over data in S3. Cost/performance are strongly influenced by how much data each query scans. Columnar formats, compression, and partitioning reduce scanned bytes.

A poorly organized data lake can make simple queries expensive.

### Architecture / Failure Model
```text
S3 data
  |
partition by date/region
  |
columnar compressed files
  |
Athena scans only needed partitions/columns
```

### Command / Config / Calculation
```text
Example layout:
s3://lake/orders/year=2026/month=08/day=20/*.parquet
```

### Expected Behavior
Queries filtering by partition columns scan only relevant data rather than the entire dataset.

### Why It Works
Athena charges/operates around scanned data volume, so storage layout becomes query economics.

### Production Example
A daily report scans one day's Parquet partition instead of years of raw JSON logs.

### Troubleshooting Workflow
```text
Athena slow/expensive
  ↓
bytes scanned
  ↓
partition pruning
  ↓
file format/compression
  ↓
small-file problem
```

### Best Practice
Design S3 analytical data layout for query patterns.

---

## Advanced Deep Dive 44 — Glue Data Catalog as Shared Metadata

### Concept and Detailed Explanation
AWS Glue Data Catalog stores table/schema metadata used by analytics services such as Athena and ETL workflows. The data remains in systems like S3; the catalog describes how to interpret it.

Schema evolution and ownership matter because many consumers may depend on the same table definition.

### Architecture / Failure Model
```text
S3 objects
  |
Glue Catalog
  |
table/schema/partition metadata
  |
Athena / ETL / analytics
```

### Command / Config / Calculation
```text
Metadata:
database
table
columns/types
location
partition keys
schema version/owner
```

### Expected Behavior
Multiple analytics tools interpret the same dataset consistently.

### Why It Works
Separating storage from metadata lets serverless analytics discover structured views over object data.

### Production Example
A new source field changes type; the data owner updates/catalogs schema with compatibility review before dependent reports break.

### Troubleshooting Workflow
```text
Athena schema error
  ↓
Glue table definition
  ↓
actual object format
  ↓
partition metadata
  ↓
schema evolution
```

### Best Practice
Assign ownership to catalog schemas just as you would database schemas.

---

## Advanced Deep Dive 45 — Redshift vs RDS Workload Shape

### Concept and Detailed Explanation
RDS targets transactional relational workloads; Redshift targets analytical data-warehouse workloads. Both accept SQL-style queries, but their storage/execution architecture and workload assumptions differ.

Choosing by the keyword 'SQL' is insufficient.

### Architecture / Failure Model
```text
OLTP:
many small reads/writes
transactions
indexes/point lookups
→ RDS/Aurora

OLAP:
large scans/aggregations
BI
columnar analytics
→ Redshift
```

### Command / Config / Calculation
```text
Decision:
transaction rate
query scan size
concurrency
latency target
data volume
joins/aggregations
write pattern
```

### Expected Behavior
The service matches the dominant workload pattern.

### Why It Works
Transactional and analytical databases optimize for different access patterns.

### Production Example
ERP order entry stays in RDS; historical reporting is loaded into Redshift.

### Troubleshooting Workflow
```text
database performance wrong
  ↓
OLTP or OLAP?
  ↓
query shape
  ↓
data volume
  ↓
service fit
```

### Best Practice
Select database technology from workload behavior, not from query language alone.

---

## Advanced Deep Dive 46 — CloudWatch Metrics, Logs, and Alarms Together

### Concept and Detailed Explanation
CloudWatch is not one thing. Metrics provide numeric time-series data, Logs store events/text, and alarms evaluate metric conditions over time. A good operational design links all three.

Alarms should represent conditions requiring action, not every metric fluctuation.

### Architecture / Failure Model
```text
Resource
  |
Metrics ----> Alarm ----> Notification/Action
  |
Logs ------> Query / Investigation
```

### Command / Config / Calculation
```text
aws cloudwatch list-metrics 2>/dev/null | head
aws logs describe-log-groups 2>/dev/null || true
aws cloudwatch describe-alarms 2>/dev/null || true
```

### Expected Behavior
An alarm identifies the affected service, and operators can pivot to related logs for diagnosis.

### Why It Works
Metrics summarize state efficiently; logs preserve detailed event evidence.

### Production Example
High ALB 5xx alarm leads engineers to application logs showing database timeout errors.

### Troubleshooting Workflow
```text
alarm fires
  ↓
metric/statistic/window
  ↓
resource dimensions
  ↓
correlated logs
  ↓
recent changes
```

### Best Practice
Alert on user-impacting symptoms and keep dashboards for diagnostic context.

---

## Advanced Deep Dive 47 — CloudTrail as the Administrative Audit Trail

### Concept and Detailed Explanation
CloudTrail records AWS API activity and is fundamental for answering who changed a resource. Organization-level trails or centralized event stores improve visibility across accounts.

Logging should be protected from the same administrators whose actions it records where practical.

### Architecture / Failure Model
```text
User / Role / AWS Service
   |
API Call
   |
CloudTrail event
   |
central S3 / event store
   |
SIEM / investigation
```

### Command / Config / Calculation
```text
aws cloudtrail lookup-events   --max-results 10   --output table 2>/dev/null || true
```

### Expected Behavior
Security teams can trace privileged changes back to session identity, source, time, and API action.

### Why It Works
AWS infrastructure changes occur through APIs, so API history is a primary control-plane evidence source.

### Production Example
An EC2 security group suddenly allows 0.0.0.0/0 SSH; CloudTrail shows the role and API call that changed it.

### Troubleshooting Workflow
```text
unexpected resource change
  ↓
resource ID/time
  ↓
CloudTrail lookup
  ↓
principal/session
  ↓
source IP/user agent
  ↓
related actions
```

### Best Practice
Centralize and protect CloudTrail logs across the organization.

---

## Advanced Deep Dive 48 — AWS Config for State History and Compliance

### Concept and Detailed Explanation
CloudTrail tells you which API calls occurred; AWS Config helps answer what a resource configuration looked like and whether it complied with rules over time.

This distinction is powerful during audits and incident response.

### Architecture / Failure Model
```text
CloudTrail:
"who called Modify..."

AWS Config:
"resource looked like X before,
then Y after, and rule became NON_COMPLIANT"
```

### Command / Config / Calculation
```text
aws configservice describe-config-rules 2>/dev/null || true
aws configservice get-compliance-summary-by-config-rule 2>/dev/null || true
```

### Expected Behavior
Operators can correlate configuration-state changes with the CloudTrail calls that caused them.

### Why It Works
API events and resulting resource state are related but distinct evidence types.

### Production Example
A bucket becomes public; Config shows when compliance changed and CloudTrail identifies the actor/action.

### Troubleshooting Workflow
```text
noncompliant resource
  ↓
Config timeline
  ↓
which property changed
  ↓
CloudTrail event
  ↓
remediate
```

### Best Practice
Use Config for state/compliance evidence and CloudTrail for API attribution.

---

## Advanced Deep Dive 49 — Systems Manager Session Manager vs Public SSH

### Concept and Detailed Explanation
Session Manager can provide shell access to supported managed nodes without requiring inbound SSH from the Internet or direct distribution of SSH private keys. Access is governed through IAM and logged according to configuration.

This can simplify administration of private EC2 fleets.

### Architecture / Failure Model
```text
Engineer
  |
IAM / SSO
  |
Systems Manager
  |
SSM Agent
  |
Private EC2
(no public SSH required)
```

### Command / Config / Calculation
```text
aws ssm describe-instance-information 2>/dev/null || true
aws ssm start-session --target <INSTANCE_ID> 2>/dev/null || true
```

### Expected Behavior
Authorized administrators can reach managed instances through AWS control channels while inbound port 22 remains closed.

### Why It Works
Session Manager uses Systems Manager registration/agent and IAM authorization rather than direct network SSH exposure.

### Production Example
A private production server has no public IP and no inbound SSH rule but remains administrable through Session Manager.

### Troubleshooting Workflow
```text
Session Manager unavailable
  ↓
instance managed by SSM?
  ↓
agent running
  ↓
IAM instance role
  ↓
network path/endpoints
  ↓
SSM service health
```

### Best Practice
Prefer identity-aware managed access over broad public SSH/RDP exposure.

---

## Advanced Deep Dive 50 — GuardDuty, Security Hub, and Detective as a Workflow

### Concept and Detailed Explanation
These services solve different stages of security operations. GuardDuty detects suspicious activity, Security Hub aggregates/prioritizes findings and posture, and Detective helps investigators analyze relationships and behavior.

They should not be treated as interchangeable 'security services.'

### Architecture / Failure Model
```text
CloudTrail/VPC/DNS/security signals
   |
GuardDuty findings
   |
Security Hub aggregation
   |
Detective investigation context
   |
response
```

### Command / Config / Calculation
```text
Security workflow:
finding
severity
resource
account
region
evidence
containment
root cause
remediation
```

### Expected Behavior
A finding can move from detection to centralized triage to investigation without losing resource/account context.

### Why It Works
Detection, aggregation, and investigation are different operational functions.

### Production Example
GuardDuty detects suspicious credential use; Security Hub surfaces it centrally; Detective helps trace related API/network activity.

### Troubleshooting Workflow
```text
security finding
  ↓
validate severity/context
  ↓
affected principal/resource
  ↓
related findings
  ↓
contain
  ↓
investigate
```

### Best Practice
Learn each service by its primary security-operations role.

---

## Advanced Deep Dive 51 — Inspector vs Macie: Vulnerability vs Sensitive Data

### Concept and Detailed Explanation
Amazon Inspector focuses on vulnerability/exposure findings for supported compute workloads. Amazon Macie focuses on discovering and protecting sensitive data in S3.

The correct service follows the object of analysis: software packages/exposure vs data content/classification.

### Architecture / Failure Model
```text
Compute/Image/Lambda package
  ↓
Inspector
  ↓
vulnerability findings

S3 objects
  ↓
Macie
  ↓
sensitive-data findings
```

### Command / Config / Calculation
```text
Scenario test:
"Find CVEs on EC2/container images" → Inspector
"Find PII in S3" → Macie
```

### Expected Behavior
The security team selects the service whose primary analysis target matches the risk.

### Why It Works
Different security problems require different telemetry and analysis engines.

### Production Example
Macie discovers customer identifiers in an unexpected S3 bucket while Inspector reports a vulnerable package on EC2.

### Troubleshooting Workflow
```text
wrong tool confusion
  ↓
is risk software vulnerability or data classification?
  ↓
choose Inspector or Macie
```

### Best Practice
Map AWS security services to the asset/risk they inspect.

---

## Advanced Deep Dive 52 — KMS Key Policy and IAM Together

### Concept and Detailed Explanation
KMS authorization is special because key policy is central to whether a principal can use a key, and IAM permissions must align with the key's policy/grants model. A user can have broad service permissions but still fail decrypt operations because KMS authorization blocks the key.

This often appears when S3, EBS, or RDS data uses customer-managed keys.

### Architecture / Failure Model
```text
Principal
  |
IAM allow kms:Decrypt
  |
KMS key policy/grant
  |
encrypted AWS service data
```

### Command / Config / Calculation
```text
aws kms describe-key --key-id <KEY_ID> 2>/dev/null || true
aws kms get-key-policy   --key-id <KEY_ID>   --policy-name default 2>/dev/null || true
```

### Expected Behavior
Only intended principals/services can use the key and encrypted resources remain accessible to legitimate workloads.

### Why It Works
KMS keys have their own resource-level authorization boundary.

### Production Example
An EC2 role can read an S3 object path but receives AccessDenied because it cannot decrypt the object's KMS key.

### Troubleshooting Workflow
```text
encrypted resource AccessDenied
  ↓
service/IAM permission
  ↓
KMS key ID
  ↓
key policy/grants
  ↓
conditions/encryption context
```

### Best Practice
Include KMS policy analysis in every encrypted-resource access investigation.

---

## Advanced Deep Dive 53 — Secrets Manager Rotation as a Multi-Step Workflow

### Concept and Detailed Explanation
Secrets Manager can integrate secret storage and rotation, but rotation is still a distributed lifecycle: create pending credential, update provider, test, promote current version, and retire the old credential.

Applications should retrieve secrets dynamically or refresh them predictably rather than cache them forever.

### Architecture / Failure Model
```text
CURRENT secret
   |
create PENDING
   |
update database/service
   |
test
   |
promote PENDING → CURRENT
   |
retire old
```

### Command / Config / Calculation
```text
Rotation checklist:
secret versions
rotation Lambda/integration
consumer refresh behavior
provider supports overlap?
rollback path
audit
```

### Expected Behavior
Consumers continue authenticating during and after rotation without exposing plaintext in code.

### Why It Works
Versioned secret stages allow controlled transition between old and new credentials.

### Production Example
A database password rotates successfully, but one long-lived application pod keeps the old cached password until restart; refresh behavior must be designed.

### Troubleshooting Workflow
```text
post-rotation auth failures
  ↓
current secret version
  ↓
provider credential state
  ↓
consumer cache
  ↓
rotation logs
```

### Best Practice
Test consumer secret-refresh behavior before enabling automatic rotation.

---

## Advanced Deep Dive 54 — AWS Backup Vault Isolation

### Concept and Detailed Explanation
AWS Backup centralizes backup policies, but cyber recovery improves when backup vaults, accounts, and permissions are isolated from workload administrators. Vault Lock and cross-account copies can reduce the chance that compromised production credentials delete every recovery point.

Backup architecture should also include restore testing.

### Architecture / Failure Model
```text
Production Account
   |
AWS Backup
   |
cross-account copy
   |
Backup/Security Account
   |
protected vault / retention controls
```

### Command / Config / Calculation
```text
Backup review:
plan
resource coverage
vault
cross-account copy
retention
delete permissions
restore test date
RPO/RTO
```

### Expected Behavior
Critical backups survive loss or compromise of the workload account according to the designed threat model.

### Why It Works
Account and IAM separation creates an administrative failure boundary in addition to storage redundancy.

### Production Example
Ransomware compromises a production admin role but cannot delete locked cross-account backup recovery points.

### Troubleshooting Workflow
```text
restore unavailable
  ↓
backup job success
  ↓
vault/recovery point
  ↓
KMS permissions
  ↓
cross-account role
  ↓
restore procedure
```

### Best Practice
Measure backup quality by successful restores, not by backup-job success alone.

---

## Advanced Deep Dive 55 — Regional DR Patterns on AWS

### Concept and Detailed Explanation
AWS disaster-recovery architectures are often described as backup-and-restore, pilot light, warm standby, and multi-site/active-active. Each trades cost against RTO/RPO and operational complexity.

The right pattern should be derived from business objectives and tested recovery time.

### Architecture / Failure Model
```text
Lower cost / higher RTO
Backup & Restore
   ↓
Pilot Light
   ↓
Warm Standby
   ↓
Multi-Site Active/Active
Higher cost / lower RTO
```

### Command / Config / Calculation
```text
DR decision:
RPO
RTO
data replication
pre-provisioned compute
DNS/traffic cutover
quota/capacity
test frequency
cost
```

### Expected Behavior
The selected pattern meets measured RTO/RPO rather than merely having a second Region.

### Why It Works
More pre-provisioned and continuously synchronized capacity reduces recovery work after disaster.

### Production Example
A Tier-1 portal uses warm standby while a low-priority archive system uses backup-and-restore.

### Troubleshooting Workflow
```text
DR test misses RTO
  ↓
which phase slow?
  ↓
capacity provisioning?
  ↓
data restore?
  ↓
DNS/cutover?
  ↓
app validation?
```

### Best Practice
Choose DR pattern per workload tier; do not force one pattern across all systems.

---

## Advanced Deep Dive 56 — Route 53 and Multi-Region Failover

### Concept and Detailed Explanation
Route 53 can direct users between regional endpoints using failover, latency, weighted, or other routing policies. For DR, DNS is only one part of the solution: secondary compute, data, certificates, network, quotas, and dependencies must already be recoverable.

Low TTL can improve new-query failover speed but does not terminate existing connections.

### Architecture / Failure Model
```text
Region A ALB ← health check
      |
Route 53 failover record
      |
Region B ALB
```

### Command / Config / Calculation
```text
DR DNS record:
primary endpoint
secondary endpoint
TTL
health check
failover criteria
manual override
```

### Expected Behavior
New DNS resolutions move to the healthy DR endpoint when the policy detects/declares primary failure.

### Why It Works
Route 53 changes DNS answers; it cannot repair missing application/data readiness in the secondary Region.

### Production Example
A DR exercise proves Route 53 failover works but reveals Region B lacks a current database copy.

### Troubleshooting Workflow
```text
DNS switched but app fails
  ↓
secondary ALB health
  ↓
app capacity
  ↓
DB/data freshness
  ↓
network/secrets/certs
```

### Best Practice
Test complete regional recovery, not only DNS failover.

---

## Advanced Deep Dive 57 — AWS Cost Explorer vs Budgets vs Pricing Calculator

### Concept and Detailed Explanation
These services answer different questions. Pricing Calculator estimates future architecture cost. Cost Explorer analyzes actual historical/current spend and usage. Budgets compares spend/usage against defined thresholds and alerts.

Confusing them is common in both exams and operations.

### Architecture / Failure Model
```text
Before deployment:
Pricing Calculator

After deployment:
Cost Explorer

Threshold monitoring:
AWS Budgets
```

### Command / Config / Calculation
```text
Scenario:
"How much might this design cost?" → Pricing Calculator
"Why did EC2 spend rise last month?" → Cost Explorer
"Alert at $5,000/month" → Budgets
```

### Expected Behavior
Teams use the tool matching forecast, analysis, or alerting needs.

### Why It Works
Forecasting, analytics, and threshold monitoring require different data and workflows.

### Production Example
A FinOps team estimates a migration with Pricing Calculator, tracks real spend in Cost Explorer, and alerts teams through Budgets.

### Troubleshooting Workflow
```text
cost question
  ↓
future estimate?
  ↓
historical analysis?
  ↓
threshold alert?
```

### Best Practice
Memorize cost tools by question type, not by name.

---

## Advanced Deep Dive 58 — Cost Allocation Tags and Ownership

### Concept and Detailed Explanation
Cost allocation tags make spend attributable to applications, teams, environments, or cost centers. They become useful only when tagging is consistent and activated for billing analysis.

Untaggable/shared costs still need an allocation method.

### Architecture / Failure Model
```text
AWS Resource
  |
tags:
Application
Owner
Environment
CostCenter
  |
billing data
  |
showback/chargeback
```

### Command / Config / Calculation
```text
Mandatory tags:
Owner
Application
Environment
CostCenter
ManagedBy
DataClassification
```

### Expected Behavior
Most cloud spend can be traced to an accountable owner and business service.

### Why It Works
AWS billing can group eligible resource costs by activated allocation tags.

### Production Example
An orphaned NAT Gateway is found quickly because every network resource must have Owner and Application tags.

### Troubleshooting Workflow
```text
unallocated spend
  ↓
resource tag coverage
  ↓
shared service?
  ↓
untaggable charge?
  ↓
allocation rule
```

### Best Practice
Make ownership tags mandatory at resource creation.

---

## Advanced Deep Dive 59 — Savings Plans, RIs, and Capacity Reservations as Different Decisions

### Concept and Detailed Explanation
Savings Plans and Reserved Instances primarily address price optimization for predictable compute usage. Capacity Reservations address the ability to launch capacity in a specific AZ. These are separate dimensions: cost commitment and capacity assurance.

Dedicated Hosts add a different requirement around physical-host dedication/licensing.

### Architecture / Failure Model
```text
Question 1:
How reduce predictable compute price?
→ Savings Plan / RI

Question 2:
How guarantee EC2 capacity in AZ?
→ Capacity Reservation

Question 3:
Need dedicated physical host?
→ Dedicated Host
```

### Command / Config / Calculation
```text
Decision inputs:
usage predictability
instance flexibility
AZ capacity requirement
licensing
term/commitment
```

### Expected Behavior
Architecture uses the pricing/capacity mechanism that matches the business requirement.

### Why It Works
Discount and capacity products solve different resource-allocation problems.

### Production Example
A disaster-recovery site purchases capacity reservation for scarce instance types but separately analyzes Savings Plans for steady production compute.

### Troubleshooting Workflow
```text
pricing/capacity confusion
  ↓
discount needed?
  ↓
capacity guarantee?
  ↓
hardware dedication?
```

### Best Practice
Separate price optimization from capacity assurance in design reviews.

---

## Advanced Deep Dive 60 — AWS Practitioner Troubleshooting by Evidence Layer

### Concept and Detailed Explanation
Cloud Practitioner certification is not a deep troubleshooting exam, but engineering skill improves when AWS services are organized into evidence layers: identity, DNS, network, compute, application, data, observability, and provider/account health.

The service name should follow the failed layer.

### Architecture / Failure Model
```text
User
 ↓
Route 53
 ↓
CloudFront/WAF
 ↓
ALB
 ↓
VPC route/SG/NACL
 ↓
EC2/ECS/Lambda
 ↓
RDS/S3/DynamoDB
 ↓
CloudWatch/CloudTrail/Config
```

### Command / Config / Calculation
```text
Triage:
1. aws sts get-caller-identity
2. DNS resolution
3. route/SG/NACL
4. target health
5. compute/service health
6. data dependency
7. CloudWatch logs/metrics
8. CloudTrail recent changes
```

### Expected Behavior
Engineers identify the likely AWS service and evidence source before making changes.

### Why It Works
Layered architectures propagate lower-level failures upward into user symptoms.

### Production Example
An ALB 502 incident is traced to unhealthy EC2 targets rather than changing Route 53.

### Troubleshooting Workflow
```text
AWS incident
  ↓
blast radius
  ↓
failed layer
  ↓
matching AWS evidence/tool
  ↓
smallest correction
```

### Best Practice
Learn AWS services as parts of an end-to-end request path.

---


# Enhanced Practical Lab Series — AWS Cloud Practitioner

These labs extend the uploaded course and are designed to convert cloud concepts into operational reasoning. Use free-tier/training sandboxes or tabletop simulation where creating real resources would incur cost.

## Enhanced Lab 1 — AWS Account as a Hard Administrative Boundary

### Objective
Prove the behavior of **AWS Account as a Hard Administrative Boundary** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws sts get-caller-identity

# Before any write:
# verify Account and Arn in output.
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Operators can identify the account boundary before making changes and production is not mixed with experimentation.

### Troubleshooting Path
```text
wrong-account incident
  ↓
aws sts get-caller-identity
  ↓
profile/role source
  ↓
account purpose
  ↓
stop writes
  ↓
switch correct role/profile
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 2 — Root User as an Emergency Identity

### Objective
Prove the behavior of **Root User as an Emergency Identity** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Security checklist:
root MFA
no root access keys
root email controlled
root login alerts
break-glass procedure
periodic recovery test
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Routine cloud administration occurs without root sessions and any root use creates a high-priority audit event.

### Troubleshooting Path
```text
root login observed
  ↓
was it authorized?
  ↓
CloudTrail/account audit
  ↓
credential/MFA review
  ↓
contain if unexpected
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 3 — IAM Policy Evaluation as Layered Authorization

### Objective
Prove the behavior of **IAM Policy Evaluation as Layered Authorization** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
# Inspect caller
aws sts get-caller-identity

# Policy simulation where authorized:
aws iam simulate-principal-policy   --policy-source-arn <PRINCIPAL_ARN>   --action-names s3:GetObject   --resource-arns arn:aws:s3:::example-bucket/object 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
An AccessDenied investigation identifies the exact policy layer limiting the action instead of simply adding AdministratorAccess.

### Troubleshooting Path
```text
AccessDenied
  ↓
caller identity
  ↓
action/resource
  ↓
explicit deny?
  ↓
SCP/boundary/session/resource policy
  ↓
conditions
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 4 — IAM Role Trust Policy vs Permission Policy

### Objective
Prove the behavior of **IAM Role Trust Policy vs Permission Policy** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
# Read role metadata
aws iam get-role --role-name <ROLE_NAME> 2>/dev/null || true

# List attached policies
aws iam list-attached-role-policies   --role-name <ROLE_NAME> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
A role can be assumed only by trusted principals and the resulting session receives only intended permissions.

### Troubleshooting Path
```text
AssumeRole denied
  ↓
source principal identity
  ↓
target role trust policy
  ↓
external ID/MFA/condition?
  ↓
source permission to sts:AssumeRole
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 5 — STS Temporary Credentials and Session Lifetime

### Objective
Prove the behavior of **STS Temporary Credentials and Session Lifetime** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws sts get-caller-identity

# In SDKs/managed environments, prefer provider credential chains
# rather than manually exporting long-lived keys.
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Long-running workloads refresh role credentials before expiry without storing permanent access keys.

### Troubleshooting Path
```text
ExpiredToken
  ↓
credential source
  ↓
session expiry
  ↓
SDK/provider refresh?
  ↓
clock skew?
  ↓
reauthenticate
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 6 — IAM Identity Center Permission Sets

### Objective
Prove the behavior of **IAM Identity Center Permission Sets** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws sso login --profile <profile> 2>/dev/null || true
aws sts get-caller-identity --profile <profile> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
One workforce identity can receive different scoped roles across dev, production, and security accounts.

### Troubleshooting Path
```text
user cannot access account
  ↓
identity synced?
  ↓
account assignment?
  ↓
permission set provisioned?
  ↓
session/login profile?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 7 — SCPs as Maximum-Permission Guardrails

### Objective
Prove the behavior of **SCPs as Maximum-Permission Guardrails** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
SCP design examples:
deny leaving Organization
deny disabling audit trail
deny unsupported Regions
deny creation of root access keys
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Local account administrators cannot bypass organization-level prohibited actions through their own IAM policies.

### Troubleshooting Path
```text
unexpected SCP denial
  ↓
which OU/account?
  ↓
policies inherited?
  ↓
explicit deny?
  ↓
is exception legitimate?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 8 — VPC as a Regional Routing Domain

### Objective
Prove the behavior of **VPC as a Regional Routing Domain** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-vpcs --output table 2>/dev/null || true
aws ec2 describe-subnets --output table 2>/dev/null || true
aws ec2 describe-route-tables --output json 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
You can trace a source subnet through its associated route table to the intended next hop.

### Troubleshooting Path
```text
connectivity issue
  ↓
source ENI/subnet
  ↓
associated route table
  ↓
next hop
  ↓
security group/NACL
  ↓
return route
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 9 — Public Subnet Is a Routing Property

### Objective
Prove the behavior of **Public Subnet Is a Routing Property** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-route-tables   --filters Name=association.subnet-id,Values=<SUBNET_ID>   2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Internet reachability is explained by address, route, and security layers together.

### Troubleshooting Path
```text
EC2 Internet inbound fails
  ↓
public address?
  ↓
route to IGW?
  ↓
SG inbound?
  ↓
NACL?
  ↓
OS/app listening?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 10 — NAT Gateway Architecture and AZ Failure

### Objective
Prove the behavior of **NAT Gateway Architecture and AZ Failure** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-nat-gateways 2>/dev/null || true
aws ec2 describe-route-tables 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Loss of one AZ does not remove outbound Internet access from private workloads in another healthy AZ.

### Troubleshooting Path
```text
private egress failure
  ↓
subnet route
  ↓
NAT state/AZ
  ↓
public subnet route to IGW
  ↓
NACL/DNS/external service
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 11 — Security Groups as Stateful ENI Policy

### Objective
Prove the behavior of **Security Groups as Stateful ENI Policy** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-security-groups   --group-ids <SG_ID> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Backend tiers accept traffic only from intended upstream security identities.

### Troubleshooting Path
```text
connection denied
  ↓
source ENI/SG
  ↓
destination SG rule
  ↓
protocol/port
  ↓
NACL/route
  ↓
service listening
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 12 — NACLs, Stateless Rules, and Ephemeral Ports

### Objective
Prove the behavior of **NACLs, Stateless Rules, and Ephemeral Ports** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-network-acls 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Allowed application flows include both forward and return NACL rules while security groups handle stateful workload policy.

### Troubleshooting Path
```text
SG looks correct but traffic fails
  ↓
NACL inbound
  ↓
NACL outbound
  ↓
ephemeral port range
  ↓
route
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 13 — VPC Endpoints and Private AWS Service Access

### Objective
Prove the behavior of **VPC Endpoints and Private AWS Service Access** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-vpc-endpoints 2>/dev/null || true

# Check DNS from instance:
getent hosts <service-endpoint> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Private workloads reach the AWS service using the configured private endpoint path.

### Troubleshooting Path
```text
endpoint access fails
  ↓
endpoint state
  ↓
route/private DNS
  ↓
endpoint policy
  ↓
SG for interface endpoint
  ↓
IAM/resource policy
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 14 — Transit Gateway Route-Table Segmentation

### Objective
Prove the behavior of **Transit Gateway Route-Table Segmentation** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-transit-gateway-attachments 2>/dev/null || true
aws ec2 describe-transit-gateway-route-tables 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Only approved segments learn routes to each other and return paths remain symmetric through required inspection.

### Troubleshooting Path
```text
TGW flow fails
  ↓
attachment state
  ↓
route-table association
  ↓
route propagation/static routes
  ↓
inspection path
  ↓
VPC return routes
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 15 — Route 53 DNS Routing vs Load Balancing

### Objective
Prove the behavior of **Route 53 DNS Routing vs Load Balancing** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
dig app.example.com
dig +trace app.example.com 2>/dev/null || true

Review:
record TTL
routing policy
health check
alias target
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
DNS answers match the configured policy, but existing/cache-held client connections may continue using previous endpoints until TTL/session behavior changes.

### Troubleshooting Path
```text
DNS failover slow
  ↓
health-check state
  ↓
record policy
  ↓
TTL/cache
  ↓
client resolver
  ↓
target health
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 16 — CloudFront Cache Keys and Origin Load

### Objective
Prove the behavior of **CloudFront Cache Keys and Origin Load** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Review:
cache policy
origin request policy
TTL
query strings
cookies
headers
cache hit ratio
origin request count
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Frequently reusable content achieves a high cache hit ratio while personalized content varies only on necessary dimensions.

### Troubleshooting Path
```text
origin load high
  ↓
CloudFront hit ratio
  ↓
cache key dimensions
  ↓
TTL
  ↓
cache-control headers
  ↓
origin errors/latency
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 17 — CloudFront Origin Access Control

### Objective
Prove the behavior of **CloudFront Origin Access Control** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Security review:
S3 Block Public Access enabled
bucket policy allows CloudFront distribution
direct public object URL denied
CloudFront URL succeeds
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Objects are available through CloudFront but not through unauthenticated direct S3 access.

### Troubleshooting Path
```text
CloudFront 403
  ↓
distribution origin
  ↓
OAC configuration
  ↓
bucket policy
  ↓
object existence/KMS permissions
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 18 — Global Accelerator vs CloudFront Decision

### Objective
Prove the behavior of **Global Accelerator vs CloudFront Decision** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Decision:
need caching? → CloudFront
need static global IP / TCP/UDP acceleration? → Global Accelerator
need both? architecture may combine services depending on use case
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The selected service matches protocol, caching, and endpoint-routing requirements.

### Troubleshooting Path
```text
global performance issue
  ↓
protocol?
  ↓
cacheable content?
  ↓
static IP requirement?
  ↓
regional endpoint health?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 19 — EC2 Boot Path and Troubleshooting

### Objective
Prove the behavior of **EC2 Boot Path and Troubleshooting** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-instance-status   --instance-ids <INSTANCE_ID> 2>/dev/null || true

# On host:
systemctl --failed
journalctl -b -p err
cloud-init status 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Engineers can determine whether failure belongs to AWS infrastructure, guest OS, bootstrap, or application.

### Troubleshooting Path
```text
EC2 unreachable
  ↓
instance state
  ↓
system check
  ↓
instance check
  ↓
ENI/routes/SG
  ↓
OS/service
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 20 — AMI Lifecycle and Golden Image Pipelines

### Objective
Prove the behavior of **AMI Lifecycle and Golden Image Pipelines** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
AMI metadata:
source_ami
build_commit
build_date
security_scan
owner
deprecation_date
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Each running fleet instance maps to a known tested AMI version.

### Troubleshooting Path
```text
unknown AMI in fleet
  ↓
instance ImageId
  ↓
AMI tags/metadata
  ↓
build provenance
  ↓
replace with approved image
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 21 — Launch Templates as Fleet Contracts

### Objective
Prove the behavior of **Launch Templates as Fleet Contracts** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ec2 describe-launch-template-versions   --launch-template-id <LT_ID> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
New instances are created from one explicit template version rather than ad hoc console state.

### Troubleshooting Path
```text
new instances misconfigured
  ↓
ASG launch template version
  ↓
AMI
  ↓
user data
  ↓
IAM profile
  ↓
SG/subnets
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 22 — Auto Scaling Group Desired, Minimum, and Maximum Capacity

### Objective
Prove the behavior of **Auto Scaling Group Desired, Minimum, and Maximum Capacity** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws autoscaling describe-auto-scaling-groups   --auto-scaling-group-names <ASG> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The group maintains at least the required healthy baseline and can scale toward the configured maximum.

### Troubleshooting Path
```text
ASG not scaling
  ↓
policy alarm/metric
  ↓
desired/min/max
  ↓
launch failures
  ↓
subnet capacity/quota
  ↓
health checks
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 23 — Instance Refresh and Controlled Fleet Replacement

### Objective
Prove the behavior of **Instance Refresh and Controlled Fleet Replacement** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Refresh design:
minimum_healthy_percentage
instance_warmup
checkpoint_percentage
rollback criteria
launch template version
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Fleet replacement preserves application capacity and stops when new instances fail health criteria.

### Troubleshooting Path
```text
refresh stuck
  ↓
new instance launch?
  ↓
health check?
  ↓
warmup time?
  ↓
capacity/quota?
  ↓
template version?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 24 — EBS Volume Type Selection by Workload

### Objective
Prove the behavior of **EBS Volume Type Selection by Workload** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
# Guest evidence
lsblk
iostat -xz 1 5 2>/dev/null || true

# AWS-side
aws ec2 describe-volumes   --volume-ids <VOLUME_ID> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Storage selection matches the measured I/O pattern and neither volume nor instance path is an unexplained bottleneck.

### Troubleshooting Path
```text
EBS slow
  ↓
guest queue/latency
  ↓
volume type/provisioned limits
  ↓
instance EBS bandwidth
  ↓
burst/throughput
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 25 — EBS Snapshots and Application Consistency

### Objective
Prove the behavior of **EBS Snapshots and Application Consistency** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Backup procedure:
1. app-native checkpoint/flush
2. filesystem sync/quiesce if required
3. create snapshot
4. verify snapshot completion
5. periodic restore test
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Restored snapshots boot and the application/database passes integrity checks.

### Troubleshooting Path
```text
snapshot restore problem
  ↓
volume attaches?
  ↓
filesystem integrity
  ↓
DB crash recovery
  ↓
native logs/backups
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 26 — S3 Bucket Policy, IAM Policy, and Access Points

### Objective
Prove the behavior of **S3 Bucket Policy, IAM Policy, and Access Points** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws s3api get-bucket-policy --bucket <BUCKET> 2>/dev/null || true
aws s3api get-public-access-block --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-encryption --bucket <BUCKET> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Applications receive narrow, explainable access paths without making the bucket broadly public.

### Troubleshooting Path
```text
S3 AccessDenied
  ↓
caller identity
  ↓
IAM action/resource
  ↓
bucket/access-point policy
  ↓
Block Public Access
  ↓
KMS
  ↓
endpoint policy
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 27 — S3 Versioning, Replication, and Delete Protection

### Objective
Prove the behavior of **S3 Versioning, Replication, and Delete Protection** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws s3api get-bucket-versioning --bucket <BUCKET> 2>/dev/null || true
aws s3api get-bucket-replication --bucket <BUCKET> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Operators can recover prior object versions and know which replica/backup copies are protected from deletion.

### Troubleshooting Path
```text
object deleted
  ↓
source versions
  ↓
replica versions
  ↓
delete marker replicated?
  ↓
locked backup?
  ↓
restore
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 28 — S3 Lifecycle and Cost Without Destroying Recovery

### Objective
Prove the behavior of **S3 Lifecycle and Cost Without Destroying Recovery** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Lifecycle worksheet:
current version transition
noncurrent version transition
noncurrent expiration
delete markers
minimum retention
legal hold
restore RTO
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Storage cost declines over time without violating required recovery or compliance periods.

### Troubleshooting Path
```text
unexpected object versions gone
  ↓
lifecycle policy history
  ↓
versioning
  ↓
retention/Object Lock
  ↓
backup copy
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 29 — RDS Multi-AZ Failover Mechanics

### Objective
Prove the behavior of **RDS Multi-AZ Failover Mechanics** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Application settings:
connect_timeout
retry_with_backoff
connection_pool_recycle
DNS-respecting client
transaction retry policy
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
After failover, the application reconnects through the same logical database endpoint and resumes operation.

### Troubleshooting Path
```text
RDS failover incident
  ↓
AWS/RDS event
  ↓
endpoint DNS
  ↓
app connection pool
  ↓
retry behavior
  ↓
transaction consistency
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 30 — RDS Read Replicas and Read Scaling

### Objective
Prove the behavior of **RDS Read Replicas and Read Scaling** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Read-scaling design:
write endpoint
read endpoint(s)
maximum acceptable replica lag
read-after-write requirement
promotion/failover plan
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Read-heavy traffic is distributed while write consistency requirements still use the primary when necessary.

### Troubleshooting Path
```text
stale read
  ↓
replica lag
  ↓
read-after-write requirement?
  ↓
route critical read to primary
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 31 — Aurora Cluster Endpoint vs Reader Endpoint

### Objective
Prove the behavior of **Aurora Cluster Endpoint vs Reader Endpoint** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Connection design:
write_dsn = cluster_writer_endpoint
read_dsn  = cluster_reader_endpoint
connection_retry = enabled
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Writes follow the active writer after failover and read traffic can use replicas.

### Troubleshooting Path
```text
Aurora connectivity issue
  ↓
which endpoint?
  ↓
writer/reader role
  ↓
DNS
  ↓
security group
  ↓
cluster event/failover
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 32 — DynamoDB Partition-Key Design

### Objective
Prove the behavior of **DynamoDB Partition-Key Design** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Access-pattern worksheet:
operation
partition key
sort key
expected RPS
item size
key cardinality
hot-key risk
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Traffic distributes across many partition-key values rather than concentrating on one key.

### Troubleshooting Path
```text
DynamoDB throttling
  ↓
table capacity mode
  ↓
hot partition/key?
  ↓
request distribution
  ↓
item size
  ↓
redesign key or shard
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 33 — DynamoDB Conditional Writes and Idempotency

### Objective
Prove the behavior of **DynamoDB Conditional Writes and Idempotency** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
# Conceptual condition:
attribute_not_exists(order_id)

# Or optimistic version:
expected version = 7
update → version 8
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Duplicate create attempts fail safely instead of producing a second logical object or overwriting a newer version.

### Troubleshooting Path
```text
conditional check failed
  ↓
duplicate request?
  ↓
stale version?
  ↓
read current item
  ↓
decide retry/merge/reject
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 34 — ElastiCache Failure and Cache-Aside Behavior

### Objective
Prove the behavior of **ElastiCache Failure and Cache-Aside Behavior** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Cache controls:
TTL
max memory/eviction
replication
failover
key naming
stampede protection
fallback to DB
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Cache loss temporarily increases database load but does not lose authoritative data.

### Troubleshooting Path
```text
cache outage
  ↓
app fallback works?
  ↓
DB load
  ↓
cache cluster health
  ↓
TTL/evictions
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 35 — SQS Visibility Timeout and Duplicate Processing

### Objective
Prove the behavior of **SQS Visibility Timeout and Duplicate Processing** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Design:
p95_processing_time = 45s
visibility_timeout  = > p99 + margin
max_receive_count   = bounded
DLQ                 = configured
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Normal jobs complete and delete before visibility expiry; failed jobs retry and eventually reach a DLQ if repeatedly unsuccessful.

### Troubleshooting Path
```text
duplicate SQS work
  ↓
processing duration
  ↓
visibility timeout
  ↓
delete/ack timing
  ↓
consumer idempotency
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 36 — SQS FIFO Ordering Scope

### Objective
Prove the behavior of **SQS FIFO Ordering Scope** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Design:
message_group_id = customer_id
deduplication_id = business_event_id
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Events for one logical entity remain ordered while unrelated entities can process in parallel.

### Troubleshooting Path
```text
FIFO throughput low
  ↓
all messages one group?
  ↓
group-key cardinality
  ↓
consumer concurrency
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 37 — SNS Fan-Out with Independent Queues

### Objective
Prove the behavior of **SNS Fan-Out with Independent Queues** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Design:
topic event schema
subscriber filters
queue retry/DLQ
consumer idempotency
encryption/access policy
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Failure of one subscriber does not prevent other subscribers from receiving and processing the event.

### Troubleshooting Path
```text
one subscriber missing events
  ↓
SNS subscription
  ↓
filter policy
  ↓
queue policy
  ↓
DLQ/delivery status
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 38 — EventBridge Event Bus and Schema Boundaries

### Objective
Prove the behavior of **EventBridge Event Bus and Schema Boundaries** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Event envelope:
source
detail-type
id
time
detail:
  schema_version
  entity_id
  event_type
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Events can evolve without unexpectedly breaking every consumer.

### Troubleshooting Path
```text
consumer broke after event change
  ↓
schema version
  ↓
rule pattern
  ↓
consumer assumptions
  ↓
compatibility/replay
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 39 — Step Functions Retry and Compensation

### Objective
Prove the behavior of **Step Functions Retry and Compensation** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Retry:
  max_attempts
  interval_seconds
  backoff_rate

Catch:
  error_equals
  next: compensation_state
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Transient faults recover automatically while business failures follow predictable workflows.

### Troubleshooting Path
```text
workflow stuck/failing
  ↓
execution history
  ↓
which state?
  ↓
retry exhausted?
  ↓
input/output shape
  ↓
compensation path
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 40 — Lambda Concurrency and Throttling

### Objective
Prove the behavior of **Lambda Concurrency and Throttling** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Concurrency plan:
account_concurrency
reserved_function_concurrency
provisioned_concurrency_if_needed
queue depth
DB connection limit
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Function scaling does not exhaust shared account concurrency or overload downstream dependencies.

### Troubleshooting Path
```text
Lambda throttled
  ↓
function concurrency
  ↓
account concurrency
  ↓
reserved concurrency
  ↓
event source retry/backlog
  ↓
downstream limit
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 41 — Lambda Cold Start vs Provisioned Capacity

### Objective
Prove the behavior of **Lambda Cold Start vs Provisioned Capacity** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Measure:
p50/p95/p99 duration
init duration
package size
dependency initialization
concurrency burst
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Latency SLOs are based on measured cold and warm behavior, not assumptions.

### Troubleshooting Path
```text
Lambda latency spike
  ↓
init duration?
  ↓
cold-start frequency
  ↓
package/runtime
  ↓
VPC/dependency initialization
  ↓
provisioned concurrency if justified
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 42 — API Gateway Throttling and Abuse Protection

### Objective
Prove the behavior of **API Gateway Throttling and Abuse Protection** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Rate policy:
steady_rate
burst
per-client/API-key quota if used
backend max throughput
429 retry guidance
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Excess traffic receives controlled throttling while healthy request volume continues.

### Troubleshooting Path
```text
API returns 429
  ↓
usage plan/throttle
  ↓
account/service quotas
  ↓
backend saturation
  ↓
client retry behavior
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 43 — Athena Cost and Partition Design

### Objective
Prove the behavior of **Athena Cost and Partition Design** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Example layout:
s3://lake/orders/year=2026/month=08/day=20/*.parquet
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Queries filtering by partition columns scan only relevant data rather than the entire dataset.

### Troubleshooting Path
```text
Athena slow/expensive
  ↓
bytes scanned
  ↓
partition pruning
  ↓
file format/compression
  ↓
small-file problem
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 44 — Glue Data Catalog as Shared Metadata

### Objective
Prove the behavior of **Glue Data Catalog as Shared Metadata** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Metadata:
database
table
columns/types
location
partition keys
schema version/owner
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Multiple analytics tools interpret the same dataset consistently.

### Troubleshooting Path
```text
Athena schema error
  ↓
Glue table definition
  ↓
actual object format
  ↓
partition metadata
  ↓
schema evolution
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 45 — Redshift vs RDS Workload Shape

### Objective
Prove the behavior of **Redshift vs RDS Workload Shape** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Decision:
transaction rate
query scan size
concurrency
latency target
data volume
joins/aggregations
write pattern
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The service matches the dominant workload pattern.

### Troubleshooting Path
```text
database performance wrong
  ↓
OLTP or OLAP?
  ↓
query shape
  ↓
data volume
  ↓
service fit
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 46 — CloudWatch Metrics, Logs, and Alarms Together

### Objective
Prove the behavior of **CloudWatch Metrics, Logs, and Alarms Together** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws cloudwatch list-metrics 2>/dev/null | head
aws logs describe-log-groups 2>/dev/null || true
aws cloudwatch describe-alarms 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
An alarm identifies the affected service, and operators can pivot to related logs for diagnosis.

### Troubleshooting Path
```text
alarm fires
  ↓
metric/statistic/window
  ↓
resource dimensions
  ↓
correlated logs
  ↓
recent changes
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 47 — CloudTrail as the Administrative Audit Trail

### Objective
Prove the behavior of **CloudTrail as the Administrative Audit Trail** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws cloudtrail lookup-events   --max-results 10   --output table 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Security teams can trace privileged changes back to session identity, source, time, and API action.

### Troubleshooting Path
```text
unexpected resource change
  ↓
resource ID/time
  ↓
CloudTrail lookup
  ↓
principal/session
  ↓
source IP/user agent
  ↓
related actions
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 48 — AWS Config for State History and Compliance

### Objective
Prove the behavior of **AWS Config for State History and Compliance** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws configservice describe-config-rules 2>/dev/null || true
aws configservice get-compliance-summary-by-config-rule 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Operators can correlate configuration-state changes with the CloudTrail calls that caused them.

### Troubleshooting Path
```text
noncompliant resource
  ↓
Config timeline
  ↓
which property changed
  ↓
CloudTrail event
  ↓
remediate
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 49 — Systems Manager Session Manager vs Public SSH

### Objective
Prove the behavior of **Systems Manager Session Manager vs Public SSH** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws ssm describe-instance-information 2>/dev/null || true
aws ssm start-session --target <INSTANCE_ID> 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Authorized administrators can reach managed instances through AWS control channels while inbound port 22 remains closed.

### Troubleshooting Path
```text
Session Manager unavailable
  ↓
instance managed by SSM?
  ↓
agent running
  ↓
IAM instance role
  ↓
network path/endpoints
  ↓
SSM service health
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 50 — GuardDuty, Security Hub, and Detective as a Workflow

### Objective
Prove the behavior of **GuardDuty, Security Hub, and Detective as a Workflow** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Security workflow:
finding
severity
resource
account
region
evidence
containment
root cause
remediation
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
A finding can move from detection to centralized triage to investigation without losing resource/account context.

### Troubleshooting Path
```text
security finding
  ↓
validate severity/context
  ↓
affected principal/resource
  ↓
related findings
  ↓
contain
  ↓
investigate
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 51 — Inspector vs Macie: Vulnerability vs Sensitive Data

### Objective
Prove the behavior of **Inspector vs Macie: Vulnerability vs Sensitive Data** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Scenario test:
"Find CVEs on EC2/container images" → Inspector
"Find PII in S3" → Macie
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The security team selects the service whose primary analysis target matches the risk.

### Troubleshooting Path
```text
wrong tool confusion
  ↓
is risk software vulnerability or data classification?
  ↓
choose Inspector or Macie
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 52 — KMS Key Policy and IAM Together

### Objective
Prove the behavior of **KMS Key Policy and IAM Together** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
aws kms describe-key --key-id <KEY_ID> 2>/dev/null || true
aws kms get-key-policy   --key-id <KEY_ID>   --policy-name default 2>/dev/null || true
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Only intended principals/services can use the key and encrypted resources remain accessible to legitimate workloads.

### Troubleshooting Path
```text
encrypted resource AccessDenied
  ↓
service/IAM permission
  ↓
KMS key ID
  ↓
key policy/grants
  ↓
conditions/encryption context
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 53 — Secrets Manager Rotation as a Multi-Step Workflow

### Objective
Prove the behavior of **Secrets Manager Rotation as a Multi-Step Workflow** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Rotation checklist:
secret versions
rotation Lambda/integration
consumer refresh behavior
provider supports overlap?
rollback path
audit
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Consumers continue authenticating during and after rotation without exposing plaintext in code.

### Troubleshooting Path
```text
post-rotation auth failures
  ↓
current secret version
  ↓
provider credential state
  ↓
consumer cache
  ↓
rotation logs
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 54 — AWS Backup Vault Isolation

### Objective
Prove the behavior of **AWS Backup Vault Isolation** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Backup review:
plan
resource coverage
vault
cross-account copy
retention
delete permissions
restore test date
RPO/RTO
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Critical backups survive loss or compromise of the workload account according to the designed threat model.

### Troubleshooting Path
```text
restore unavailable
  ↓
backup job success
  ↓
vault/recovery point
  ↓
KMS permissions
  ↓
cross-account role
  ↓
restore procedure
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 55 — Regional DR Patterns on AWS

### Objective
Prove the behavior of **Regional DR Patterns on AWS** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
DR decision:
RPO
RTO
data replication
pre-provisioned compute
DNS/traffic cutover
quota/capacity
test frequency
cost
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The selected pattern meets measured RTO/RPO rather than merely having a second Region.

### Troubleshooting Path
```text
DR test misses RTO
  ↓
which phase slow?
  ↓
capacity provisioning?
  ↓
data restore?
  ↓
DNS/cutover?
  ↓
app validation?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 56 — Route 53 and Multi-Region Failover

### Objective
Prove the behavior of **Route 53 and Multi-Region Failover** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
DR DNS record:
primary endpoint
secondary endpoint
TTL
health check
failover criteria
manual override
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
New DNS resolutions move to the healthy DR endpoint when the policy detects/declares primary failure.

### Troubleshooting Path
```text
DNS switched but app fails
  ↓
secondary ALB health
  ↓
app capacity
  ↓
DB/data freshness
  ↓
network/secrets/certs
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 57 — AWS Cost Explorer vs Budgets vs Pricing Calculator

### Objective
Prove the behavior of **AWS Cost Explorer vs Budgets vs Pricing Calculator** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Scenario:
"How much might this design cost?" → Pricing Calculator
"Why did EC2 spend rise last month?" → Cost Explorer
"Alert at $5,000/month" → Budgets
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Teams use the tool matching forecast, analysis, or alerting needs.

### Troubleshooting Path
```text
cost question
  ↓
future estimate?
  ↓
historical analysis?
  ↓
threshold alert?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 58 — Cost Allocation Tags and Ownership

### Objective
Prove the behavior of **Cost Allocation Tags and Ownership** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Mandatory tags:
Owner
Application
Environment
CostCenter
ManagedBy
DataClassification
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Most cloud spend can be traced to an accountable owner and business service.

### Troubleshooting Path
```text
unallocated spend
  ↓
resource tag coverage
  ↓
shared service?
  ↓
untaggable charge?
  ↓
allocation rule
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 59 — Savings Plans, RIs, and Capacity Reservations as Different Decisions

### Objective
Prove the behavior of **Savings Plans, RIs, and Capacity Reservations as Different Decisions** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Decision inputs:
usage predictability
instance flexibility
AZ capacity requirement
licensing
term/commitment
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Architecture uses the pricing/capacity mechanism that matches the business requirement.

### Troubleshooting Path
```text
pricing/capacity confusion
  ↓
discount needed?
  ↓
capacity guarantee?
  ↓
hardware dedication?
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---

## Enhanced Lab 60 — AWS Practitioner Troubleshooting by Evidence Layer

### Objective
Prove the behavior of **AWS Practitioner Troubleshooting by Evidence Layer** with architecture reasoning, observable evidence, and a recovery path.

### Preparation
1. Define the intended architecture/state.
2. Record region/account/project, network, identity, and cost context where relevant.
3. Capture a before-state using read-only commands or a design worksheet.
4. Define the expected result before making a change.

### Mental Model
```text
Requirement
   ↓
Cloud control plane
   ↓
Resource / policy
   ↓
Data plane behavior
   ↓
Evidence / metrics / logs
```

### Commands / Data
```text
Triage:
1. aws sts get-caller-identity
2. DNS resolution
3. route/SG/NACL
4. target health
5. compute/service health
6. data dependency
7. CloudWatch logs/metrics
8. CloudTrail recent changes
```

### Procedure
1. Draw the architecture or dependency path.
2. Identify the control-plane object(s) involved.
3. Identify the data-plane behavior that should result.
4. Apply or simulate the smallest safe change.
5. Capture metrics/logs/routes/policies/state after the change.
6. Introduce one reversible failure or misconfiguration in a disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Restore the intended state and verify again.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Engineers identify the likely AWS service and evidence source before making changes.

### Troubleshooting Path
```text
AWS incident
  ↓
blast radius
  ↓
failed layer
  ↓
matching AWS evidence/tool
  ↓
smallest correction
```

### Safety / Cost Control
Prefer read-only AWS CLI commands, Skill Builder/lab environments, or disposable accounts. Verify `aws sts get-caller-identity` before writes, keep MFA enabled, never publish credentials/account secrets, and delete billable lab resources after use.

---


## 5. Hands-on Lab / Practical Exercises

> Cost rule: Prefer read-only or free/low-cost resources. Before creating anything, check current AWS pricing and delete the resource after the lab.

### Lab 1 — Secure the AWS Account

Checklist:

```text
root user protected
MFA enabled
no root access keys
workforce/admin identity created
billing alerts/budget configured
```

Explain why daily root use is unsafe.

### Lab 2 — Verify AWS CLI Identity

Configure a safe lab profile using IAM Identity Center or temporary credentials.

```bash
aws sts get-caller-identity --profile lab
```

Document:

```text
Account
ARN
Identity type
```

### Lab 3 — Discover Regions and AZs

```bash
aws ec2 describe-regions \
  --query 'Regions[].RegionName' \
  --output table

aws ec2 describe-availability-zones \
  --region us-east-1 \
  --output table
```

Explain Region vs AZ.

### Lab 4 — Shared Responsibility Matrix

Create a table for:

```text
EC2
RDS
Lambda
S3
SaaS-like external application
```

Rows:

```text
hardware
hypervisor
OS
runtime
application
IAM
data
encryption configuration
```

### Lab 5 — IAM Least-Privilege Policy

Write a lab JSON policy that allows:

```text
s3:ListBucket
s3:GetObject
```

only for one test bucket.

Explain:

```text
Effect
Action
Resource
```

### Lab 6 — IAM Role Architecture

Draw:

```text
EC2
 ↓ instance profile
IAM Role
 ↓ STS temporary credentials
S3
```

Explain why it is safer than an access key stored in `/etc/app.conf`.

### Lab 7 — AWS Organizations Design

Design:

```text
Management
Security
Log Archive
Network
Production
NonProduction
Sandbox
```

accounts/OUs.

Create three conceptual SCPs:

```text
deny unapproved Regions
deny disabling security logging
deny creation of public S3 where appropriate
```

### Lab 8 — VPC CIDR Design

Use:

```text
10.20.0.0/16
```

Create:

```text
Public A
Public B
App A
App B
DB A
DB B
```

across two AZs.

Avoid overlap with:

```text
10.10.0.0/16 on-prem
```

### Lab 9 — Route Table Exercise

For the public subnet:

```text
10.20.0.0/16 → local
0.0.0.0/0    → IGW
```

For private app subnet:

```text
10.20.0.0/16 → local
0.0.0.0/0    → NAT
```

Explain why DB subnets may not need Internet default routes.

### Lab 10 — Security Group Design

Create conceptual groups:

```text
ALB-SG
Web-SG
DB-SG
```

Rules:

```text
Internet → ALB TCP/443
ALB-SG → Web-SG TCP/8080
Web-SG → DB-SG TCP/5432
```

No direct Internet-to-DB rule.

### Lab 11 — Security Group vs NACL

Create scenario:

```text
security group allows 443
NACL denies return ephemeral ports
```

Explain why the stateless NACL can still break traffic.

### Lab 12 — EC2 Design

Choose instance-family category for:

```text
web server
CPU rendering
memory cache
large local storage workload
GPU training
```

Do not choose an exact current instance SKU; focus on category reasoning.

### Lab 13 — EC2 User Data

Prepare:

```bash
#!/bin/bash
dnf install -y nginx
systemctl enable --now nginx
echo "AWS Practitioner Lab" > /usr/share/nginx/html/index.html
```

Explain:

```text
bootstrap
vs
long-term configuration management
```

### Lab 14 — EC2 Pricing Selection

For each workload choose:

```text
On-Demand
Savings Plans / RI
Spot
Capacity Reservation
Dedicated Host
```

Scenarios:

```text
3-hour test
24/7 predictable web fleet
fault-tolerant batch
must guarantee AZ capacity
software license tied to physical sockets
```

### Lab 15 — Auto Scaling Architecture

Design:

```text
ALB
 ↓
Auto Scaling Group
 ├─ AZ-A
 └─ AZ-B
```

Policy:

```text
desired = 2
min = 2
max = 10
target CPU = conceptual 50%
```

Simulate one-instance failure.

### Lab 16 — S3 Storage-Class Selection

Choose for:

```text
active website images
unknown access patterns
monthly report archives
single-AZ recreatable copies
rarely accessed compliance data
deep archive
```

Use:

```text
Standard
Intelligent-Tiering
Standard-IA
One Zone-IA
Glacier classes
```

### Lab 17 — S3 Lifecycle Design

Design:

```text
Day 0 → Standard
Day 30 → Standard-IA
Day 180 → Glacier
Year 7 → expire
```

Add:

```text
versioning
encryption
Object Lock for protected backups if required
```

### Lab 18 — Storage Service Selection

Map:

```text
EC2 boot/database disk → ?
shared Linux filesystem → ?
Windows managed file share → ?
object backup → ?
hybrid on-prem file integration → ?
offline 500-TB transfer → ?
```

Expected categories:

```text
EBS
EFS
FSx
S3
Storage Gateway
Snow Family
```

### Lab 19 — Database Service Selection

Map:

```text
managed MySQL → RDS
high-performance AWS relational → Aurora
shopping cart key-value → DynamoDB
session cache → ElastiCache
document DB → DocumentDB
relationship graph → Neptune
```

Explain why.

### Lab 20 — RDS Multi-AZ vs Read Replica

Draw:

```text
Multi-AZ
primary → standby
goal: HA

Read Replica
primary → replica
goal: read scaling
```

Create three exam-style scenarios.

### Lab 21 — Messaging Selection

Choose:

```text
SQS
SNS
EventBridge
Step Functions
```

for:

```text
worker queue
fan-out alert
event-routing bus
multi-step serverless workflow
```

### Lab 22 — Analytics Selection

Choose:

```text
Athena
Glue
Kinesis
EMR
Redshift
OpenSearch
QuickSight
```

for seven scenarios.

### Lab 23 — Security Service Matrix

Create:

```text
GuardDuty       threat detection
Inspector       vulnerability management
Macie           sensitive S3 data
Security Hub    finding aggregation
Detective       investigation
Shield          DDoS
WAF             web filtering
KMS             encryption keys
Secrets Manager secrets
Artifact        compliance documents
```

Then create ten scenario questions.

### Lab 24 — CloudWatch / CloudTrail / Config

For each requirement select one:

```text
EC2 CPU alarm
who deleted instance
was S3 bucket public yesterday
application logs
resource compliance
```

Explain why.

### Lab 25 — CloudFormation

Create a small template:

```yaml
AWSTemplateFormatVersion: '2010-09-09'

Resources:
  LabBucket:
    Type: AWS::S3::Bucket
```

Explain:

```text
template
stack
resource
change
delete
```

Do not deploy if you cannot monitor cost/cleanup.

### Lab 26 — Cost Management

Given fictional monthly cost:

```text
EC2:        $1,000
RDS:          $700
S3:           $150
Data egress:  $600
Other:        $200
```

Use concepts:

```text
Cost Explorer
Budgets
Cost allocation tags
Pricing Calculator
Compute Optimizer
```

to create an optimization plan.

### Lab 27 — Support Selection

For each scenario identify the most appropriate **conceptual** support level:

```text
personal learning
production business workload
business-critical enterprise
mission-critical operational environment
```

Then separately note the CLF-C02 legacy plan names still present in the exam guide.

### Lab 28 — AWS Architecture Diagram

Design:

```text
Route 53
 ↓
CloudFront
 ↓
WAF
 ↓
ALB
 ↓
EC2 Auto Scaling across two AZs
 ↓
RDS Multi-AZ
 ↓
S3 backups/static objects
```

Add:

```text
CloudWatch
CloudTrail
KMS
IAM
AWS Backup
```

### Lab 29 — Exam Scenario Drill

Answer 30 scenario prompts such as:

```text
Need API audit?
Need object storage?
Need queue?
Need CDN?
Need DDoS protection?
Need S3 sensitive-data discovery?
Need right-sizing?
Need cost alert?
Need SQL on S3?
Need private dedicated on-prem link?
```

For every answer write:

```text
service
why
why the two closest distractors are wrong
```

### Lab 30 — Foundational AWS Troubleshooting Challenge

Analyze:

1. IAM user gets AccessDenied.
2. EC2 is running but unreachable.
3. private EC2 cannot download updates.
4. ALB marks target unhealthy.
5. RDS connection fails.
6. S3 returns AccessDenied.
7. CloudFront serves old content.
8. Auto Scaling does not scale.
9. CloudTrail event needs to be found.
10. AWS Config reports noncompliance.
11. CloudWatch alarm fires.
12. Cost spikes unexpectedly.
13. service quota is reached.
14. Region has an AWS service event.
15. access key is exposed in Git.

For each:

```text
Layer
Likely Cause
AWS Service/Tool
Evidence
Correction
Prevention
```

---

## 6. Mini Project

# Mini Project — AWS Customer Portal Foundation

Design a production-style AWS environment for:

```text
customer/order portal
5,000 daily users
500 peak concurrent users
sensitive customer data
production + staging
RPO = 1 hour
RTO = 4 hours
```

## Architecture

```text
                           Route 53
                               |
                           CloudFront
                               |
                              WAF
                               |
                    Application Load Balancer
                      /                  \
                AZ-A                      AZ-B
                 |                         |
             EC2 / ECS                 EC2 / ECS
                 \                         /
                  \                       /
                     Amazon RDS Multi-AZ
                              |
                         AWS Backup
                              |
                              S3
```

## Account Design

```text
Organization
├─ Security
├─ Log Archive
├─ Shared Services
├─ Production
└─ NonProduction
```

## IAM

Design:

```text
IAM Identity Center
MFA
CloudAdmin
SecurityAudit
Developer
BillingReadOnly
CI/CD Role
Application Role
Break-glass strategy
```

## VPC

Design:

```text
10.20.0.0/16

2 public subnets
2 private app subnets
2 private DB subnets

IGW
NAT
route tables
security groups
VPC endpoints where useful
```

## Compute

Choose and justify:

```text
EC2
ECS
EKS
Lambda
Elastic Beanstalk
```

for different components.

## Storage

Choose:

```text
S3
EBS
EFS
FSx
Backup
```

where appropriate.

## Data

Use:

```text
RDS/Aurora for transactional data
DynamoDB only if justified
ElastiCache for performance if justified
S3 for objects
```

## Security

Include:

```text
CloudTrail
Config
GuardDuty
Security Hub
Inspector
KMS
Secrets Manager
WAF
Shield
AWS Backup
```

Explain which are mandatory vs optional for the scenario.

## Monitoring

Include:

```text
CloudWatch metrics
CloudWatch Logs
alarms
AWS Health
Trusted Advisor
```

## Cost

Define:

```text
mandatory cost allocation tags
Budgets
Cost Explorer
Pricing Calculator estimate
right-sizing process
Savings Plans/RI analysis
Spot candidates
```

## Automation

Design:

```text
Git
 ↓
CloudFormation / Terraform later
 ↓
AWS APIs
 ↓
Ansible for guest/application config where required
```

## Deliverables

```text
README.md
AWS_ARCHITECTURE.md
ACCOUNTS.md
IAM.md
VPC.md
COMPUTE.md
STORAGE.md
DATABASE.md
SECURITY.md
MONITORING.md
BACKUP_DR.md
COST.md
SUPPORT.md
RUNBOOKS/
```

## Required Runbooks

```text
RUNBOOK_IAM_ACCESS_DENIED.md
RUNBOOK_EC2_UNREACHABLE.md
RUNBOOK_ALB_UNHEALTHY.md
RUNBOOK_RDS_FAILURE.md
RUNBOOK_S3_ACCESS.md
RUNBOOK_COST_SPIKE.md
RUNBOOK_EXPOSED_ACCESS_KEY.md
RUNBOOK_REGION_EVENT.md
```

---


# Expanded Capstone — AWS Production Landing Zone + Customer Platform

Build a design that prepares you for later AWS Solutions Architect and SysOps courses while remaining understandable at Cloud Practitioner level.

## 1. AWS Organization

Design:

```text
Management
├── Security OU
│   ├── Security Tooling
│   └── Log Archive
├── Infrastructure OU
│   ├── Network
│   └── Shared Services
├── Production OU
│   ├── Customer Portal
│   └── Data
└── NonProduction OU
    ├── Staging
    └── Sandbox
```

Document:

```text
SCP intent
IAM Identity Center
account owners
billing
CloudTrail
Config
GuardDuty/Security Hub
backup
```

## 2. IAM

Define:

```text
PlatformAdmin
NetworkAdmin
SecurityAudit
ApplicationDeployer
ReadOnly
BillingReadOnly
CI/CD Role
Application Role
Backup Role
Break-Glass
```

For each:

```text
trust relationship
permission scope
account assignment
session duration
MFA/federation
```

## 3. VPC

Use:

```text
10.20.0.0/16
```

Across two AZs:

```text
2 public subnets
2 private app subnets
2 private DB subnets
```

Include:

```text
IGW
per-AZ NAT design
route tables
security groups
simple NACL policy
VPC endpoints
Transit Gateway/hybrid route concept
private DNS
```

## 4. Security Group Chain

```text
Internet
  ↓ TCP/443
ALB-SG
  ↓ app port
APP-SG
  ↓ DB port
DB-SG
```

No direct Internet-to-app or Internet-to-database rule.

## 5. Compute

Use an Auto Scaling Group with:

```text
Launch Template
versioned AMI
IAM instance profile
IMDS hardening
minimum capacity = availability requirement
target tracking
instance refresh
ALB health checks
```

Optional comparison:

```text
EC2
ECS/Fargate
Elastic Beanstalk
Lambda
```

## 6. CloudFront / WAF / Route 53

Design:

```text
Route 53
   ↓
CloudFront
   ↓
WAF
   ↓
ALB
```

Keep static S3 origin private using controlled CloudFront-origin access.

## 7. Data

Use:

```text
RDS/Aurora for transactions
Multi-AZ for HA
read replica only if read scaling required
ElastiCache if justified
S3 for documents/static data
```

Document:

```text
connection pooling
retry after RDS failover
backup retention
KMS keys
secret retrieval
```

## 8. Messaging

Use one asynchronous business flow:

```text
Order Created
   ↓
SNS or EventBridge
   ├─ SQS Billing
   ├─ SQS Email
   └─ SQS Analytics
```

Include:

```text
DLQ
visibility timeout
idempotency key
schema version
```

## 9. Serverless Flow

Design:

```text
S3 Upload
  ↓
EventBridge
  ↓
Lambda
  ↓
processed object / DynamoDB
```

Document concurrency and downstream limits.

## 10. Security Services

Map purpose:

```text
CloudTrail     API audit
Config         state/compliance
GuardDuty      threat detection
Inspector      software vulnerability
Macie          S3 sensitive data
Security Hub   finding aggregation
Detective      investigation
WAF            web filtering
Shield         DDoS
KMS            key management
Secrets Manager secrets
ACM            certificates
```

## 11. AWS Backup / Cyber Recovery

Create:

```text
Production Account
  ↓
AWS Backup
  ↓ cross-account copy
Backup/Security Account
  ↓
protected vault / retention controls
```

Perform a documented restore test.

## 12. Observability

Create a dashboard for:

```text
ALB request count
ALB 4xx/5xx
target response time
healthy host count
EC2 CPU
RDS connections
RDS CPU/storage
SQS queue depth
Lambda errors/throttles
CloudFront hit ratio
```

Link incidents to:

```text
CloudTrail
Config
CloudWatch Logs
AWS Health
```

## 13. Cost Model

Use:

```text
Pricing Calculator → forecast
Cost Explorer      → actual analysis
Budgets            → threshold alerts
cost tags          → ownership
Compute Optimizer  → right-sizing
```

Classify:

```text
baseline commitment candidate
Spot candidate
capacity-reservation requirement
data-transfer/egress risk
```

## 14. DR

Choose and justify one:

```text
backup/restore
pilot light
warm standby
multi-site
```

Include:

```text
Route 53 failover
secondary-region capacity/quota
data replication
KMS/secrets
certificates
DNS
business verification
failback
```

## 15. Required Runbooks

```text
RUNBOOK_WRONG_ACCOUNT.md
RUNBOOK_IAM_ACCESS_DENIED.md
RUNBOOK_ASSUME_ROLE.md
RUNBOOK_EC2_UNREACHABLE.md
RUNBOOK_PRIVATE_EGRESS.md
RUNBOOK_ALB_UNHEALTHY.md
RUNBOOK_RDS_FAILOVER.md
RUNBOOK_S3_ACCESS_DENIED.md
RUNBOOK_LAMBDA_THROTTLE.md
RUNBOOK_SQS_BACKLOG.md
RUNBOOK_SECURITY_FINDING.md
RUNBOOK_KMS_ACCESS.md
RUNBOOK_SECRET_ROTATION.md
RUNBOOK_BACKUP_RESTORE.md
RUNBOOK_COST_SPIKE.md
RUNBOOK_REGION_DR.md
```

## Deliverables

```text
README.md
ORGANIZATION.md
IAM.md
SCP.md
VPC.md
COMPUTE.md
EDGE_AND_DNS.md
STORAGE.md
DATABASE.md
MESSAGING.md
SERVERLESS.md
SECURITY.md
BACKUP_DR.md
OBSERVABILITY.md
COST.md
RUNBOOKS/
```


## 7. Recommended Resources

This file is intended to be self-contained for learning and exam preparation.

For current production behavior, use official AWS sources.

Primary references:

- AWS Certified Cloud Practitioner CLF-C02 Exam Guide
- CLF-C02 In-Scope AWS Services
- AWS Well-Architected Framework
- AWS Shared Responsibility Model
- AWS IAM User Guide
- AWS Organizations User Guide
- Amazon VPC User Guide
- Amazon EC2 User Guide
- Amazon S3 User Guide
- Amazon RDS User Guide
- AWS Billing and Cost Management documentation
- AWS Support documentation
- AWS Architecture Center
- AWS Prescriptive Guidance
- AWS re:Post

Important current-course note:

```text
Certification content can remain stable
while live AWS commercial offerings change.
```

This is especially relevant to AWS Support plans in 2026.

---

## 8. Certification Relevance

Direct certification:

```text
AWS Certified Cloud Practitioner — CLF-C02
```

Official current scored domains:

```text
Domain 1 — Cloud Concepts                         24%
Domain 2 — Security and Compliance               30%
Domain 3 — Cloud Technology and Services         34%
Domain 4 — Billing, Pricing, and Support          12%
```

Official current exam structure:

```text
50 scored
15 unscored
65 total

multiple choice
multiple response

minimum passing scaled score: 700
```

The exam specifically expects:

```text
AWS Cloud value
shared responsibility
Well-Architected
security
cost/economics
core AWS services
service selection
```

This course intentionally adds hands-on practice beyond the exam.

It prepares directly for:

```text
52. AWS Certified Solutions Architect – Associate
53. AWS SysOps / CloudOps Administration
54. Amazon PaaS Web Services
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Memorize service names without use cases.  
  **Best practice:** learn the primary problem solved by each service.

- **Mistake:** Use root user daily.  
  **Best practice:** protect root and use federated/role-based access.

- **Mistake:** Store access keys in code.  
  **Best practice:** use roles and temporary credentials.

- **Mistake:** Treat an SCP as an IAM permission grant.  
  **Best practice:** SCP limits maximum permissions; IAM still grants access.

- **Mistake:** Confuse Security Groups and NACLs.  
  **Best practice:** remember stateful-resource-level vs stateless-subnet-level.

- **Mistake:** Confuse RDS Multi-AZ and Read Replica.  
  **Best practice:** HA vs read scaling.

- **Mistake:** Confuse S3 and EBS.  
  **Best practice:** object storage vs block disk.

- **Mistake:** Confuse CloudWatch and CloudTrail.  
  **Best practice:** operational monitoring vs API auditing.

- **Mistake:** Confuse Config and CloudTrail.  
  **Best practice:** configuration/compliance state vs API calls.

- **Mistake:** Confuse WAF and Shield.  
  **Best practice:** web-request filtering vs DDoS protection.

- **Mistake:** Confuse Reserved Instances and Capacity Reservations.  
  **Best practice:** discount vs capacity assurance.

- **Mistake:** Use Spot for a single critical server.  
  **Best practice:** use Spot for interruption-tolerant workloads.

- **Mistake:** Make S3 public for application delivery.  
  **Best practice:** use controlled access and CloudFront where appropriate.

- **Mistake:** Put DB in public subnet because the app needs it.  
  **Best practice:** private DB and controlled app-to-DB security group path.

- **Mistake:** Use exact AWS service counts as permanent facts.  
  **Best practice:** understand infrastructure model and check current official numbers.

- **Mistake:** Study old AWS Support-plan tables without checking current offerings.  
  **Best practice:** learn both the active exam guide and current AWS support transition.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the current Cloud Practitioner exam code?

**Short answer:** CLF-C02.

### Q2. What are the four exam domains?

**Short answer:** Cloud Concepts; Security and Compliance; Cloud Technology and Services; Billing, Pricing, and Support.

### Q3. Which domain has the largest weighting?

**Short answer:** Cloud Technology and Services at 34%.

### Q4. Minimum passing scaled score?

**Short answer:** 700.

### Q5. Region vs Availability Zone?

**Short answer:** Region is a geographic AWS area; AZ is an isolated infrastructure location within a Region.

### Q6. How do you design high availability inside one Region?

**Short answer:** Use multiple Availability Zones.

### Q7. Who patches the guest OS on EC2?

**Short answer:** Customer.

### Q8. Who manages the physical hypervisor infrastructure?

**Short answer:** AWS.

### Q9. What are the six Well-Architected pillars?

**Short answer:** Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.

### Q10. IAM role vs IAM user?

**Short answer:** Role is assumed for temporary credentials; IAM user is a long-lived account identity.

### Q11. What is an SCP?

**Short answer:** Organizations policy that restricts maximum available permissions; it does not grant access.

### Q12. What is IAM Identity Center?

**Short answer:** Centralized workforce access across AWS accounts/applications.

### Q13. What is VPC?

**Short answer:** Logically isolated AWS virtual network.

### Q14. Is a subnet regional?

**Short answer:** No. An AWS subnet belongs to one Availability Zone.

### Q15. Security Group vs NACL?

**Short answer:** Security Group is stateful and resource-level; NACL is stateless and subnet-level.

### Q16. What does NAT Gateway do?

**Short answer:** Allows private IPv4 workloads to initiate outbound connectivity without direct inbound Internet access.

### Q17. What is Direct Connect?

**Short answer:** Dedicated network connectivity between customer/network provider environment and AWS.

### Q18. Route 53?

**Short answer:** AWS DNS/domain/traffic-routing service.

### Q19. CloudFront?

**Short answer:** AWS CDN/edge content-delivery service.

### Q20. EC2?

**Short answer:** AWS virtual-machine compute service.

### Q21. Which EC2 option is interruptible but low cost?

**Short answer:** Spot Instances.

### Q22. Reserved Instance vs Capacity Reservation?

**Short answer:** RI is primarily a pricing discount; Capacity Reservation reserves capacity.

### Q23. EBS?

**Short answer:** Persistent block storage for EC2.

### Q24. EFS?

**Short answer:** Managed shared NFS file storage.

### Q25. S3?

**Short answer:** Regional object-storage service.

### Q26. Which S3 class automatically adapts to changing access patterns?

**Short answer:** S3 Intelligent-Tiering.

### Q27. What does S3 versioning provide?

**Short answer:** Retention of multiple object versions for recovery/history.

### Q28. RDS?

**Short answer:** Managed relational database service.

### Q29. Aurora?

**Short answer:** AWS cloud-native relational database compatible with MySQL/PostgreSQL interfaces.

### Q30. DynamoDB?

**Short answer:** Managed serverless key-value/document NoSQL database.

### Q31. Multi-AZ vs Read Replica?

**Short answer:** Multi-AZ primarily HA; Read Replica primarily read scaling.

### Q32. SQS?

**Short answer:** Managed message queue.

### Q33. SNS?

**Short answer:** Managed pub/sub notification service.

### Q34. EventBridge?

**Short answer:** Managed event bus/routing service.

### Q35. CloudWatch?

**Short answer:** Monitoring, metrics, logs, alarms, dashboards.

### Q36. CloudTrail?

**Short answer:** AWS API/account activity audit trail.

### Q37. AWS Config?

**Short answer:** Resource configuration tracking and compliance evaluation.

### Q38. GuardDuty?

**Short answer:** Managed threat-detection service.

### Q39. Inspector?

**Short answer:** Vulnerability-management/scanning service for supported workloads.

### Q40. Macie?

**Short answer:** Sensitive-data discovery/security focused on Amazon S3.

### Q41. Security Hub?

**Short answer:** Central security finding/posture aggregation.

### Q42. WAF vs Shield?

**Short answer:** WAF filters web requests; Shield provides DDoS protection.

### Q43. KMS?

**Short answer:** Managed encryption-key service.

### Q44. Secrets Manager?

**Short answer:** Managed secret storage/rotation capability.

### Q45. Artifact?

**Short answer:** Portal for AWS compliance reports and agreements.

### Q46. Cost Explorer?

**Short answer:** Analyze actual AWS cost and usage trends.

### Q47. Budgets?

**Short answer:** Set spending/usage thresholds and alerts.

### Q48. Pricing Calculator?

**Short answer:** Estimate future AWS architecture/service costs.

### Q49. Trusted Advisor?

**Short answer:** Recommendations across cost, performance, security, resilience, and service limits depending on eligibility.

### Q50. Main exam strategy?

**Short answer:** Identify the business/technical requirement and choose the AWS service whose primary purpose best matches it.

---

# Expanded Self-Assessment Bank — AWS Cloud Practitioner

### Q1. What is the core operational lesson behind **AWS Account as a Hard Administrative Boundary**?
**Answer:** Make account identity verification the first step of every privileged AWS CLI workflow.

### Q2. What is the core operational lesson behind **Root User as an Emergency Identity**?
**Answer:** Treat root login like use of a physical master key.

### Q3. What is the core operational lesson behind **IAM Policy Evaluation as Layered Authorization**?
**Answer:** Never troubleshoot IAM by broadening privileges until the denying layer is understood.

### Q4. What is the core operational lesson behind **IAM Role Trust Policy vs Permission Policy**?
**Answer:** Debug role assumption before debugging the permissions the role would have after assumption.

### Q5. What is the core operational lesson behind **STS Temporary Credentials and Session Lifetime**?
**Answer:** Use SDK/provider credential chains instead of manually copying STS credentials into files.

### Q6. What is the core operational lesson behind **IAM Identity Center Permission Sets**?
**Answer:** Manage workforce access through groups and permission-set assignments rather than per-user account exceptions.

### Q7. What is the core operational lesson behind **SCPs as Maximum-Permission Guardrails**?
**Answer:** Keep SCPs focused on high-value invariants and test them in lower-risk OUs before broad attachment.

### Q8. What is the core operational lesson behind **VPC as a Regional Routing Domain**?
**Answer:** Start VPC troubleshooting from the source ENI and subnet, not from a generic VPC diagram.

### Q9. What is the core operational lesson behind **Public Subnet Is a Routing Property**?
**Answer:** Do not use the label 'public subnet' as proof that a workload is publicly reachable.

### Q10. What is the core operational lesson behind **NAT Gateway Architecture and AZ Failure**?
**Answer:** For production multi-AZ egress, align NAT failure domains with private subnet AZs.

### Q11. What is the core operational lesson behind **Security Groups as Stateful ENI Policy**?
**Answer:** Prefer security-group references for tier-to-tier access inside AWS where supported.

### Q12. What is the core operational lesson behind **NACLs, Stateless Rules, and Ephemeral Ports**?
**Answer:** Keep NACL rules simple and document why each explicit deny/allow exists.

### Q13. What is the core operational lesson behind **VPC Endpoints and Private AWS Service Access**?
**Answer:** Remember that endpoint policy is an additional authorization layer, not a replacement for IAM.

### Q14. What is the core operational lesson behind **Transit Gateway Route-Table Segmentation**?
**Answer:** Treat TGW route tables as security segmentation boundaries, not just routing tables.

### Q15. What is the core operational lesson behind **Route 53 DNS Routing vs Load Balancing**?
**Answer:** Choose TTL based on change/failover requirements and query cost/behavior.

### Q16. What is the core operational lesson behind **CloudFront Cache Keys and Origin Load**?
**Answer:** Keep cache keys minimal and intentional.

### Q17. What is the core operational lesson behind **CloudFront Origin Access Control**?
**Answer:** Keep private origins private and expose only the delivery layer.

### Q18. What is the core operational lesson behind **Global Accelerator vs CloudFront Decision**?
**Answer:** Choose by primary traffic behavior, not by the word 'global'.

### Q19. What is the core operational lesson behind **EC2 Boot Path and Troubleshooting**?
**Answer:** Use EC2 status checks before assuming SSH or application configuration is the root cause.

### Q20. What is the core operational lesson behind **AMI Lifecycle and Golden Image Pipelines**?
**Answer:** Never make manual production EC2 changes that are not reflected in the image/configuration source of truth.

### Q21. What is the core operational lesson behind **Launch Templates as Fleet Contracts**?
**Answer:** Pin production Auto Scaling groups to a controlled launch-template version or managed default policy.

### Q22. What is the core operational lesson behind **Auto Scaling Group Desired, Minimum, and Maximum Capacity**?
**Answer:** Set minimum capacity from availability requirements, not only average demand.

### Q23. What is the core operational lesson behind **Instance Refresh and Controlled Fleet Replacement**?
**Answer:** Use health-gated rolling replacement for immutable EC2 fleets.

### Q24. What is the core operational lesson behind **EBS Volume Type Selection by Workload**?
**Answer:** Benchmark storage with the actual EC2 instance type and workload pattern.

### Q25. What is the core operational lesson behind **EBS Snapshots and Application Consistency**?
**Answer:** Define whether each backup needs crash consistency or application consistency.

### Q26. What is the core operational lesson behind **S3 Bucket Policy, IAM Policy, and Access Points**?
**Answer:** Troubleshoot S3 authorization as a layered policy evaluation.

### Q27. What is the core operational lesson behind **S3 Versioning, Replication, and Delete Protection**?
**Answer:** Design S3 recovery for accidental and malicious deletion separately.

### Q28. What is the core operational lesson behind **S3 Lifecycle and Cost Without Destroying Recovery**?
**Answer:** Review lifecycle policies like destructive code changes.

### Q29. What is the core operational lesson behind **RDS Multi-AZ Failover Mechanics**?
**Answer:** Never hard-code managed database IP addresses.

### Q30. What is the core operational lesson behind **RDS Read Replicas and Read Scaling**?
**Answer:** Use replicas only for reads that can tolerate their consistency characteristics.

### Q31. What is the core operational lesson behind **Aurora Cluster Endpoint vs Reader Endpoint**?
**Answer:** Use logical service endpoints, not fixed instance addresses, for normal application connectivity.

### Q32. What is the core operational lesson behind **DynamoDB Partition-Key Design**?
**Answer:** Design DynamoDB from query/access patterns and traffic distribution.

### Q33. What is the core operational lesson behind **DynamoDB Conditional Writes and Idempotency**?
**Answer:** Use conditional writes for idempotency and optimistic concurrency instead of read-then-write races.

### Q34. What is the core operational lesson behind **ElastiCache Failure and Cache-Aside Behavior**?
**Answer:** Test the application with the cache unavailable.

### Q35. What is the core operational lesson behind **SQS Visibility Timeout and Duplicate Processing**?
**Answer:** Set visibility timeout from real processing-duration measurements.

### Q36. What is the core operational lesson behind **SQS FIFO Ordering Scope**?
**Answer:** Choose message groups around the smallest domain that truly requires ordering.

### Q37. What is the core operational lesson behind **SNS Fan-Out with Independent Queues**?
**Answer:** Use separate queues when subscribers need independent retry and scaling.

### Q38. What is the core operational lesson behind **EventBridge Event Bus and Schema Boundaries**?
**Answer:** Treat event schemas as versioned APIs.

### Q39. What is the core operational lesson behind **Step Functions Retry and Compensation**?
**Answer:** Design retry, timeout, and compensation per state rather than one global error rule.

### Q40. What is the core operational lesson behind **Lambda Concurrency and Throttling**?
**Answer:** Use concurrency controls as architecture safety limits, not only performance knobs.

### Q41. What is the core operational lesson behind **Lambda Cold Start vs Provisioned Capacity**?
**Answer:** Optimize initialization before paying for permanently warm capacity.

### Q42. What is the core operational lesson behind **API Gateway Throttling and Abuse Protection**?
**Answer:** Return clear retry semantics and use exponential backoff for throttled clients.

### Q43. What is the core operational lesson behind **Athena Cost and Partition Design**?
**Answer:** Design S3 analytical data layout for query patterns.

### Q44. What is the core operational lesson behind **Glue Data Catalog as Shared Metadata**?
**Answer:** Assign ownership to catalog schemas just as you would database schemas.

### Q45. What is the core operational lesson behind **Redshift vs RDS Workload Shape**?
**Answer:** Select database technology from workload behavior, not from query language alone.

### Q46. What is the core operational lesson behind **CloudWatch Metrics, Logs, and Alarms Together**?
**Answer:** Alert on user-impacting symptoms and keep dashboards for diagnostic context.

### Q47. What is the core operational lesson behind **CloudTrail as the Administrative Audit Trail**?
**Answer:** Centralize and protect CloudTrail logs across the organization.

### Q48. What is the core operational lesson behind **AWS Config for State History and Compliance**?
**Answer:** Use Config for state/compliance evidence and CloudTrail for API attribution.

### Q49. What is the core operational lesson behind **Systems Manager Session Manager vs Public SSH**?
**Answer:** Prefer identity-aware managed access over broad public SSH/RDP exposure.

### Q50. What is the core operational lesson behind **GuardDuty, Security Hub, and Detective as a Workflow**?
**Answer:** Learn each service by its primary security-operations role.

### Q51. What is the core operational lesson behind **Inspector vs Macie: Vulnerability vs Sensitive Data**?
**Answer:** Map AWS security services to the asset/risk they inspect.

### Q52. What is the core operational lesson behind **KMS Key Policy and IAM Together**?
**Answer:** Include KMS policy analysis in every encrypted-resource access investigation.

### Q53. What is the core operational lesson behind **Secrets Manager Rotation as a Multi-Step Workflow**?
**Answer:** Test consumer secret-refresh behavior before enabling automatic rotation.

### Q54. What is the core operational lesson behind **AWS Backup Vault Isolation**?
**Answer:** Measure backup quality by successful restores, not by backup-job success alone.

### Q55. What is the core operational lesson behind **Regional DR Patterns on AWS**?
**Answer:** Choose DR pattern per workload tier; do not force one pattern across all systems.

### Q56. What is the core operational lesson behind **Route 53 and Multi-Region Failover**?
**Answer:** Test complete regional recovery, not only DNS failover.

### Q57. What is the core operational lesson behind **AWS Cost Explorer vs Budgets vs Pricing Calculator**?
**Answer:** Memorize cost tools by question type, not by name.

### Q58. What is the core operational lesson behind **Cost Allocation Tags and Ownership**?
**Answer:** Make ownership tags mandatory at resource creation.

### Q59. What is the core operational lesson behind **Savings Plans, RIs, and Capacity Reservations as Different Decisions**?
**Answer:** Separate price optimization from capacity assurance in design reviews.

### Q60. What is the core operational lesson behind **AWS Practitioner Troubleshooting by Evidence Layer**?
**Answer:** Learn AWS services as parts of an end-to-end request path.


## Completion Checklist

- [ ] I understand the CLF-C02 exam structure.
- [ ] I understand AWS Cloud value propositions.
- [ ] I understand Regions/AZs/edge/hybrid infrastructure.
- [ ] I understand shared responsibility.
- [ ] I understand all six Well-Architected pillars.
- [ ] I understand AWS accounts/root-user security.
- [ ] I understand IAM users/groups/roles/policies.
- [ ] I understand IAM Identity Center and federation.
- [ ] I understand Organizations/OUs/SCPs/consolidated billing.
- [ ] I understand Control Tower.
- [ ] I understand VPC/subnets/routes/IGW/NAT.
- [ ] I understand Security Groups/NACLs.
- [ ] I understand peering/Transit Gateway/VPN/Direct Connect/PrivateLink.
- [ ] I understand Route 53/CloudFront/Global Accelerator.
- [ ] I understand EC2/AMI/EBS/ELB/Auto Scaling.
- [ ] I understand EC2 pricing options.
- [ ] I understand ECS/EKS/ECR/Fargate/Lambda.
- [ ] I understand S3 and storage classes.
- [ ] I understand EFS/FSx/Storage Gateway/Snow/Backup/DR.
- [ ] I understand RDS/Aurora/DynamoDB/ElastiCache/DocumentDB/Neptune.
- [ ] I understand DMS/SCT.
- [ ] I understand SQS/SNS/EventBridge/Step Functions/API Gateway.
- [ ] I understand Athena/Glue/Kinesis/EMR/Redshift/OpenSearch/QuickSight.
- [ ] I recognize major AWS AI/ML services in exam scope.
- [ ] I understand CloudWatch/CloudTrail/Config/Systems Manager.
- [ ] I understand Trusted Advisor/Compute Optimizer/Health/Quotas.
- [ ] I understand GuardDuty/Inspector/Macie/Security Hub/Detective.
- [ ] I understand Shield/WAF/Firewall Manager.
- [ ] I understand KMS/Secrets Manager/ACM/Artifact/Audit Manager.
- [ ] I understand CloudFormation.
- [ ] I understand AWS migration services.
- [ ] I understand cost tools and pricing models.
- [ ] I understand AWS Support concepts and the 2026 transition.
- [ ] I can recognize AWS service scenarios quickly.
- [ ] I completed all 30 labs.
- [ ] I completed the AWS Customer Portal Foundation project.
