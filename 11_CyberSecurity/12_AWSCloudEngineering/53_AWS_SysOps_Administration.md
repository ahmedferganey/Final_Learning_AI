# 53. AWS SysOps Administration

> Phase 12 — AWS Cloud Engineering

This course keeps the roadmap title **AWS SysOps Administration**, but uses the **current AWS certification and operations baseline**.

## Current Certification Naming

AWS renamed:

```text
AWS Certified SysOps Administrator – Associate
SOA-C02
```

to:

```text
AWS Certified CloudOps Engineer – Associate
SOA-C03
```

The last day to take SOA-C02 was September 29, 2025. The current exam is **SOA-C03**.

Current official exam format:

```text
Exam duration: 130 minutes
Questions: 65
Question types:
  - Multiple choice
  - Multiple response
Cost: 150 USD
Minimum passing scaled score: 720
Scored questions: 50
Unscored questions: 15
```

Current scored domains:

```text
1. Monitoring, Logging, Analysis,
   Remediation, and Performance Optimization          22%

2. Reliability and Business Continuity                22%

3. Deployment, Provisioning, and Automation           22%

4. Security and Compliance                            16%

5. Networking and Content Delivery                    18%
```

AWS states that the target candidate should have about one year of experience with AWS deployment, management, troubleshooting, networking, and security, plus operations experience.

This course is designed for **actual CloudOps work**, not only the exam.

---

# SysOps / CloudOps Mental Model

A Solutions Architect asks:

```text
"What should we build?"
```

A CloudOps engineer asks:

```text
"Is it healthy?"
"Is it secure?"
"Is it performing?"
"Can it recover?"
"Can it scale?"
"Can I automate the operation?"
"Can I explain exactly why it failed?"
```

The operating loop is:

```text
Provision
   ↓
Configure
   ↓
Monitor
   ↓
Detect
   ↓
Investigate
   ↓
Remediate
   ↓
Verify
   ↓
Automate
   ↓
Improve
```

A production operations stack:

```text
AWS Workloads
     |
     +-- EC2 / ECS / EKS / Lambda
     +-- RDS / DynamoDB
     +-- S3 / EBS / EFS
     +-- ALB / Route 53 / CloudFront
     |
     v
Observability
     |
     +-- CloudWatch Metrics
     +-- CloudWatch Logs
     +-- CloudTrail
     +-- VPC Flow Logs
     +-- X-Ray
     +-- Managed Prometheus
     |
     v
Event / Incident
     |
     +-- EventBridge
     +-- SNS
     +-- Systems Manager
     +-- Lambda
     |
     v
Automated Remediation
```

---

## 1. Topic Title

**AWS SysOps Administration**

Current certification alignment:

**AWS Certified CloudOps Engineer – Associate (SOA-C03)**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain the modern CloudOps operating model.
- Explain the transition from SysOps Administrator to CloudOps Engineer.
- Configure and interpret CloudWatch metrics.
- Configure CloudWatch alarms and composite alarms.
- Use CloudWatch Logs, Logs Insights, metric filters, dashboards, and agents.
- Understand Amazon Managed Service for Prometheus at an operations level.
- Distinguish CloudWatch, CloudTrail, Config, X-Ray, and VPC Flow Logs.
- Build incident-detection and automated-remediation workflows.
- Use EventBridge for event-driven operations.
- Use SNS for operations notifications.
- Use Systems Manager Session Manager, Run Command, Patch Manager, State Manager, Inventory, Automation, Parameter Store, OpsCenter, and Maintenance Windows.
- Use Systems Manager Automation runbooks safely.
- Operate EC2 instances, AMIs, images, launch templates, and Auto Scaling groups.
- Operate ECS/EKS/container workloads at a fundamentals-to-intermediate CloudOps level.
- Monitor and optimize EBS, S3, EFS, FSx, and database services.
- Implement scaling and elasticity.
- Configure and troubleshoot ELB and Route 53 health mechanisms.
- Implement backup/restore with AWS Backup and service-native mechanisms.
- Explain RPO, RTO, PITR, backup/restore, pilot light, warm standby, and active-active.
- Provision resources using CloudFormation and AWS CDK concepts.
- Explain StackSets, AWS RAM, EC2 Image Builder, and deployment strategies.
- Use Git/Terraform in a controlled AWS operations workflow.
- Implement event-driven automation with Lambda, S3 events, and EventBridge.
- Implement IAM, federation, MFA, resource policies, and policy conditions.
- Troubleshoot permissions with CloudTrail, Access Analyzer, and policy simulation concepts.
- Operate multi-account environments with Organizations and IAM Identity Center.
- Use AWS Config and conformance packs.
- Use Security Hub, GuardDuty, Inspector, KMS, ACM, and secret-management services operationally.
- Configure VPC networking, private connectivity, DNS, CloudFront, and Global Accelerator.
- Troubleshoot routes, security groups, NACLs, NAT, Transit Gateway, DNS, and content caching.
- Analyze logs to isolate network faults.
- Optimize costs using operational data.
- Build runbooks and incident procedures.
- Perform safe operations through the AWS CLI.
- Build a production-grade CloudOps operating model.

---

## 3. Prerequisites

Required:

- 49. AWS Cloud Practitioner
- 52. AWS Certified Solutions Architect – Associate
- Linux administration
- networking
- Bash or Python basics
- Git
- configuration management
- basic containers
- basic CI/CD concepts

Recommended lab:

```text
AWS Sandbox
├─ VPC
├─ EC2
├─ ALB
├─ Auto Scaling
├─ S3
├─ RDS
├─ CloudWatch
├─ Systems Manager
└─ AWS Backup
```

Before operations:

```bash
aws sts get-caller-identity
aws configure list
```

Verify account and Region before any write command.

---

## 4. Core Concepts Explanation

# Part 1 — SysOps vs CloudOps

Traditional SysOps focused heavily on servers.

CloudOps operates:

```text
servers
containers
serverless
managed databases
storage
networks
identity
automation
cost
security
```

The current AWS certification rename reflects that broader operating surface.

# Part 2 — Operations as a Feedback Loop

Professional operations is not repeated manual command execution.

```text
Telemetry
  ↓
Decision
  ↓
Action
  ↓
Verification
  ↓
Automation
```

The goal is progressively reducing avoidable manual toil.

# Part 3 — Operational Readiness

Before production launch define:

```text
monitoring
alerts
ownership
runbooks
backup
restore tests
capacity
security logging
change process
rollback
```

A workload without operational readiness is unfinished.

# Part 4 — Runbook vs Playbook

Runbook:

```text
documented operational procedure
```

Playbook:

```text
broader incident-response sequence or automated workflow
```

Teams may use the terms differently; what matters is explicit, tested response procedures.

# Part 5 — AWS Well-Architected for Operations

CloudOps work directly supports:

```text
Operational Excellence
Security
Reliability
Performance Efficiency
Cost Optimization
Sustainability
```

Operations is how architecture promises are maintained after deployment.

# Part 6 — CloudWatch Metrics

Metrics are numerical time series.

Examples:

```text
EC2 CPUUtilization
ALB RequestCount
RDS DatabaseConnections
Lambda Errors
SQS ApproximateNumberOfMessagesVisible
```

Metrics enable dashboards, alarms, autoscaling, and analysis.

# Part 7 — Namespace

CloudWatch organizes metrics by namespace.

Examples:

```text
AWS/EC2
AWS/RDS
AWS/Lambda
custom namespace
```

Namespace prevents unrelated metrics from colliding.

# Part 8 — Dimensions

Dimensions identify a specific resource/context.

Example:

```text
Metric: CPUUtilization
Dimension: InstanceId=i-123
```

A metric with different dimension sets is a distinct time series.

# Part 9 — Statistic

Common statistics:

```text
Average
Minimum
Maximum
Sum
SampleCount
percentiles
```

Choose based on question.

Example:

```text
Average latency
```

can hide a severe p99 tail-latency problem.

# Part 10 — Period

Period controls time aggregation.

```text
1 minute
5 minutes
1 hour
```

Short periods detect changes faster but produce noisier/more granular data.

# Part 11 — Standard vs Detailed Monitoring Concept

Some AWS resources expose monitoring granularity that depends on service/settings.

For EC2, detailed monitoring provides higher-frequency built-in metrics than basic monitoring.

Use when alert/scaling responsiveness justifies it.

# Part 12 — Custom Metrics

Publish application/business metrics such as:

```text
orders_failed
jobs_pending
active_sessions
```

These may be more useful than CPU for application health.

# Part 13 — PutMetricData Example

Conceptual CLI:

```bash
aws cloudwatch put-metric-data   --namespace "Manufacturing/App"   --metric-name FailedJobs   --value 3   --unit Count
```

In production prefer structured application telemetry/agents instead of ad hoc manual publishing.

# Part 14 — CloudWatch Alarm

Alarm evaluates a metric against a threshold.

States:

```text
OK
ALARM
INSUFFICIENT_DATA
```

An alarm should represent an actionable condition.

# Part 15 — Alarm Evaluation Periods

Example:

```text
CPU > 80%
for 3 of 5 periods
```

is more stable than alarming on one brief spike.

# Part 16 — Missing Data

CloudWatch alarms can treat missing data differently.

Choose carefully:

```text
missing = breaching
missing = not breaching
missing = ignore
```

based on what missing telemetry means for that service.

# Part 17 — Composite Alarms

Composite alarms combine alarms:

```text
HighLatency
AND
HighErrorRate
```

This can reduce noisy notifications and focus on service impact.

# Part 18 — Alarm Actions

Alarm actions can trigger:

```text
SNS
Auto Scaling
EC2 actions
Systems Manager / event workflows
```

depending on supported integration.

# Part 19 — CloudWatch Dashboards

A useful dashboard shows:

```text
traffic
errors
latency
saturation
availability
dependencies
```

not only CPU charts.

# Part 20 — Cross-Account / Cross-Region Operations Views

Modern operations often centralize visibility from multiple accounts and Regions.

The architectural goal:

```text
central operations view
without flattening account isolation
```

# Part 21 — CloudWatch Logs

Central log service.

Sources include:

```text
applications
Lambda
CloudWatch Agent
VPC/network services
containers
AWS services
```

Logs should be centralized before ephemeral resources disappear.

# Part 22 — Log Groups and Streams

Simplified:

```text
Log Group
  ├─ Stream A
  ├─ Stream B
  └─ Stream C
```

Retention is configured at log-group level.

# Part 23 — Retention

Do not leave logs forever accidentally.

Set retention based on:

```text
security
operations
compliance
cost
```

Different logs can require different durations.

# Part 24 — CloudWatch Agent

CloudWatch Agent can collect:

```text
OS metrics
application/system logs
```

from EC2 and other supported environments.

Examples:

```text
memory
disk utilization
process logs
```

which are not all native EC2 metrics.

# Part 25 — Agent Configuration

Configuration describes:

```text
metrics to collect
log files
dimensions
intervals
```

Store/manage config centrally where possible.

# Part 26 — Logs Insights

CloudWatch Logs Insights performs interactive queries.

Concept:

```text
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 50
```

Use during incident investigation.

# Part 27 — Metric Filters

Metric filters extract a metric from logs.

Example:

```text
pattern "ERROR"
→ ErrorCount metric
→ CloudWatch Alarm
```

This turns unstructured log events into alertable telemetry.

# Part 28 — Subscription Filters Concept

Log subscription can stream logs to another destination for:

```text
centralization
SIEM
processing
archive
```

depending on integration.

# Part 29 — Amazon Managed Service for Prometheus

Managed Prometheus-compatible monitoring is useful for:

```text
containers
Kubernetes
Prometheus metrics
```

SOA-C03 explicitly brings modern container observability into scope.

# Part 30 — Container Observability

For ECS/EKS inspect:

```text
CPU/memory
task/pod restarts
desired/running count
network
application metrics
logs
cluster/node health
```

Container health requires both platform and application telemetry.

# Part 31 — CloudTrail

CloudTrail records AWS API/control-plane activity.

Operational questions:

```text
Who changed the security group?
Who deleted the instance?
Which role called the API?
From which source IP?
```

# Part 32 — Management Events

Management events represent control-plane operations such as:

```text
CreateBucket
RunInstances
ModifySecurityGroup
```

These are core audit events.

# Part 33 — Data Events

Data events cover high-volume resource operations for supported services.

Examples conceptually:

```text
S3 object access
Lambda invocation
```

Enable intentionally because volume/cost can be significant.

# Part 34 — CloudTrail Lake Concept

CloudTrail Lake supports longer-term event querying/analysis in a managed event data store.

Use when audit investigation needs SQL-like querying across event history.

# Part 35 — CloudWatch vs CloudTrail

```text
CloudWatch:
health/performance/logs

CloudTrail:
API activity/audit
```

During an incident you often need both.

# Part 36 — AWS Config

Config records resource configuration history and evaluates compliance rules.

Questions:

```text
Was this bucket public yesterday?
Which resource changed?
Is encryption enabled?
```

# Part 37 — Config Rule

A rule evaluates desired configuration.

Example:

```text
S3 bucket must not allow public access
```

Result:

```text
COMPLIANT
NON_COMPLIANT
```

# Part 38 — Conformance Pack

Groups Config rules/remediation guidance into a compliance baseline.

SOA-C03 explicitly includes conformance-pack-style continuous compliance.

# Part 39 — Automated Remediation

Pattern:

```text
Config detects violation
 ↓
Systems Manager Automation
 ↓
remediation
 ↓
re-evaluate
```

Automated remediation needs scope controls to avoid damaging legitimate exceptions.

# Part 40 — CloudTrail vs Config

```text
CloudTrail:
who performed API action?

Config:
what configuration existed and whether compliant?
```

# Part 41 — EventBridge

EventBridge routes events.

Example:

```text
EC2 state change
 ↓
EventBridge rule
 ↓
Lambda / SNS / SSM Automation
```

This is a core operations automation pattern.

# Part 42 — Event Pattern

EventBridge filters structured events.

Concept:

```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"]
}
```

# Part 43 — Event Target

Targets can include:

```text
Lambda
SNS
SQS
Step Functions
Systems Manager
API destinations
```

depending on event architecture.

# Part 44 — EventBridge Troubleshooting

Check:

```text
event reaches bus?
pattern matches?
rule enabled?
target permissions?
DLQ/retry?
target throttling?
```

# Part 45 — SNS for Operations

SNS distributes notifications.

Typical:

```text
CloudWatch Alarm
 ↓
SNS Topic
 ├─ email/on-call integration
 └─ automation target
```

Avoid using human email as the only incident mechanism.

# Part 46 — Systems Manager Overview

Systems Manager centralizes operational management.

Important capabilities:

```text
Session Manager
Run Command
Automation
Patch Manager
State Manager
Inventory
Maintenance Windows
Parameter Store
OpsCenter
```

# Part 47 — SSM Managed Node

A managed node needs:

```text
supported SSM agent/integration
network access to Systems Manager endpoints
IAM permissions/instance role
```

Private nodes can use VPC endpoints.

# Part 48 — Session Manager

Secure administrative shell without requiring public SSH/RDP.

```text
Operator
 ↓ IAM
Session Manager
 ↓
Private EC2
```

Benefits:

```text
no inbound port 22
central authorization
session logging options
```

# Part 49 — Session Manager CLI

Concept:

```bash
aws ssm start-session   --target i-0123456789abcdef0
```

Use least-privilege IAM and audit session activity.

# Part 50 — Run Command

Execute commands across managed nodes.

Useful for:

```text
diagnostics
service restart
config inspection
controlled operational action
```

Use targeting/tags and concurrency/error thresholds to limit blast radius.

# Part 51 — Run Command Safety

Before fleet-wide command:

```text
target canary
review command
set max concurrency
set max errors
capture output
```

Remote execution is powerful and dangerous.

# Part 52 — State Manager

Maintains desired node state through associations.

Examples:

```text
ensure agent installed
ensure configuration applied
run scheduled compliance task
```

# Part 53 — Patch Manager

Automates patching for supported operating systems.

Operations design needs:

```text
patch baseline/policy
maintenance window
reboot behavior
test ring
production ring
compliance reporting
```

# Part 54 — Maintenance Windows

Schedule disruptive operations during controlled periods.

```text
Saturday 02:00
→ patch noncritical fleet
```

Use target groups and task priority/concurrency.

# Part 55 — Inventory

Collects managed-node metadata:

```text
applications
OS
network
files/config metadata
```

depending on configuration.

Useful for fleet visibility.

# Part 56 — Automation Runbooks

Automation runbooks orchestrate multi-step operations.

Example:

```text
create snapshot
stop instance
change configuration
start instance
verify
```

# Part 57 — Automation Documents

Runbooks are Systems Manager documents with steps/actions and parameters.

Treat them as code:

```text
version
review
test
least privilege
```

# Part 58 — Parameter Store

Stores configuration values and secure strings.

Use for:

```text
application configuration
feature/config parameters
some encrypted secrets
```

Secrets Manager is stronger for dedicated secret lifecycle/rotation scenarios.

# Part 59 — OpsCenter

Aggregates operational issues (OpsItems) from supported services/events.

Use to:

```text
centralize incident context
track remediation
link related resources
```

# Part 60 — Fleet Manager Concept

Provides centralized GUI-oriented node management for supported tasks.

Still use automation for repeatable fleet operations.

# Part 61 — Automated Remediation Pattern

Example:

```text
CloudWatch alarm
 ↓
EventBridge
 ↓
SSM Automation
 ↓
restart service / replace resource
 ↓
health check
```

Only automate remediation you understand and can verify.

# Part 62 — Human-in-the-Loop Automation

For high-risk actions:

```text
detect
 ↓
collect evidence
 ↓
approval
 ↓
automation
```

is safer than fully autonomous remediation.

# Part 63 — Toil

Toil is repetitive manual operational work that:

```text
is automatable
does not create enduring value
scales with workload
```

CloudOps should reduce toil with runbooks and automation.

# Part 64 — EC2 Operations

Operate:

```text
state
status checks
AMI
EBS
network
IAM role
patching
monitoring
Auto Scaling
```

A running instance can still be unhealthy.

# Part 65 — EC2 Status Checks

Separate checks reflect:

```text
system/infrastructure reachability
instance/guest reachability
```

This helps distinguish AWS host-level issues from guest OS problems.

# Part 66 — EC2 Recovery Actions

For supported failures, CloudWatch/EC2 recovery mechanisms can recover an instance onto healthy infrastructure while preserving appropriate identity/storage characteristics.

Use service-supported recovery rather than manual reboot loops.

# Part 67 — AMI Operations

AMIs provide repeatable server images.

Operations process:

```text
base
→ patch
→ test
→ publish
→ deploy
→ retire old image
```

# Part 68 — EC2 Image Builder

Automates image pipelines.

SOA-C03 explicitly includes creating/managing AMIs and container images.

Pipeline:

```text
source image
 ↓
components
 ↓
test
 ↓
AMI/container image
```

# Part 69 — Golden AMI

Include controlled:

```text
OS patch level
security baseline
monitoring agent
SSM agent
dependencies
```

Avoid embedding secrets.

# Part 70 — Launch Templates

Version reusable EC2 launch settings.

Use with:

```text
Auto Scaling
EC2 fleet
Spot
```

A change should usually create a new template version.

# Part 71 — Auto Scaling Group Operations

Monitor:

```text
DesiredCapacity
MinSize
MaxSize
InService instances
Pending/Terminating
health status
scaling activities
```

# Part 72 — Scaling Activity Troubleshooting

If ASG does not launch:

```text
quota?
capacity?
AMI?
instance type?
subnet IP?
launch template?
IAM?
KMS?
```

Read scaling activity messages.

# Part 73 — Instance Refresh

Rolls updated launch-template/AMI configuration through an ASG.

Use:

```text
minimum healthy percentage
checkpoints
warm-up
rollback strategy
```

to control risk.

# Part 74 — Lifecycle Hooks

Pause launch/termination to perform operations.

Examples:

```text
bootstrap
register agent
drain workload
archive logs
```

# Part 75 — Warm Pools Concept

Pre-initialized instances can reduce scale-out latency for applications with slow startup.

Tradeoff:

```text
faster scale
vs
additional resource cost
```

# Part 76 — ECS Operations

Monitor:

```text
desired tasks
running tasks
task failures
service events
CPU/memory
container logs
load-balancer health
```

# Part 77 — ECS Task Failure

Check:

```text
image pull
IAM task execution role
secrets
CPU/memory
health check
network
ports
CloudWatch Logs
```

# Part 78 — EKS Operations

At associate operations level understand:

```text
control plane
nodes
pods
services
RBAC
CloudWatch/container metrics
cluster networking
```

# Part 79 — Container Image Operations

Images should be:

```text
versioned
scanned
reproducible
minimal
signed/controlled where required
```

ECR lifecycle policies prevent unbounded image accumulation.

# Part 80 — ECR Operations

Monitor/manage:

```text
repositories
permissions
image tags
scan findings
lifecycle
replication
```

# Part 81 — EBS Monitoring

Important metrics/conditions include:

```text
IOPS
throughput
queue
latency indicators
burst/credits where applicable
volume status
instance EBS limits
```

Performance is limited by both volume and instance.

# Part 82 — EBS Type Optimization

Use:

```text
gp3 → general SSD
io2 → high IOPS/durability
st1 → sequential throughput HDD
sc1 → cold throughput HDD
```

Choose from measured access pattern.

# Part 83 — EBS Volume Modification

Many EBS properties can be modified online for supported volume types.

Operational process:

```text
measure
modify
monitor optimization state
verify application
```

# Part 84 — EBS Snapshot Operations

Use snapshots for:

```text
backup
restore
AMI
cross-Region/cross-account copy
```

Test restores; snapshot existence alone does not prove recoverability.

# Part 85 — S3 Operations

Operate:

```text
access
versioning
lifecycle
replication
encryption
performance
logging
inventory
cost
```

# Part 86 — S3 Multipart Upload

Use multipart upload for large objects.

Operations should monitor/clean incomplete multipart uploads using lifecycle rules to avoid cost waste.

# Part 87 — S3 Transfer Acceleration

Can improve long-distance transfer by using AWS edge path.

Measure before enabling because it adds cost.

# Part 88 — S3 Lifecycle Operations

Lifecycle reduces cost automatically.

Example:

```text
30d → IA
180d → archive
7y → delete
```

Validate legal/retention requirements first.

# Part 89 — S3 Replication Monitoring

For replication-sensitive workloads monitor:

```text
replication status
failed replication
permissions
KMS
destination policy
```

# Part 90 — S3 Files

The current SOA-C03 guide explicitly mentions **Amazon S3 Files** as a shared-storage option.

Treat current product capabilities and availability as version-sensitive and verify the current AWS storage documentation before production use.

# Part 91 — EFS Operations

Monitor:

```text
throughput
client connections
I/O
storage classes
mount target health
```

Use lifecycle policies to move cold files where appropriate.

# Part 92 — FSx Operations

FSx operations depend on filesystem:

```text
Windows
Lustre
ONTAP
OpenZFS
```

Monitor capacity, throughput, backups, replication, and service-specific metrics.

# Part 93 — RDS Operations

Monitor:

```text
CPU
FreeableMemory
DatabaseConnections
FreeStorageSpace
Read/WriteLatency
IOPS
replica lag
events
```

plus database-native metrics.

# Part 94 — RDS Performance Insights

Helps identify database load and top waits/SQL dimensions.

Use to answer:

```text
What is consuming database time?
```

rather than only looking at CPU.

# Part 95 — RDS Proxy

Connection pooling improves:

```text
Lambda/high-concurrency applications
connection storm handling
failover behavior
```

where supported.

# Part 96 — RDS Storage Full

If FreeStorageSpace falls:

```text
identify growth
logs/temp
storage autoscaling settings
increase storage
fix application/data retention
```

Do not only add disk repeatedly.

# Part 97 — DynamoDB Operations

Monitor:

```text
throttled requests
consumed capacity
latency
system errors
hot partitions
GSI behavior
```

# Part 98 — DynamoDB Scaling

Use:

```text
on-demand
provisioned + autoscaling
```

based on traffic.

Hot partition problems may remain even if total table capacity is high.

# Part 99 — Elasticity Operations

Elasticity needs:

```text
metric
threshold/target
minimum
maximum
warm-up
downstream capacity
```

Scaling compute alone can overload a database.

# Part 100 — Caching for Scalability

CloudOps can reduce backend load through:

```text
CloudFront
ElastiCache
application cache
```

Monitor hit ratio and eviction/miss behavior.

# Part 101 — ELB Operations

Monitor:

```text
healthy targets
request count
latency
5xx
connection errors
target response
```

and access logs where enabled.

# Part 102 — ALB Unhealthy Target

Check:

```text
health path
target port
SG
application listening
timeout
response code
dependency health
```

# Part 103 — ELB 502/504

Common paths:

```text
502 → invalid/reset backend response
504 → backend timeout
```

Inspect target logs and target-response metrics rather than blaming ELB blindly.

# Part 104 — Route 53 Health Checks

Use for:

```text
endpoint monitoring
failover routing
calculated health
```

DNS failover also depends on TTL and application readiness.

# Part 105 — Route 53 Resolver

Resolver supports:

```text
VPC DNS
inbound/outbound endpoints
hybrid DNS forwarding
rules
```

SOA-C03 explicitly includes Route 53 Resolver operations.

# Part 106 — DNS Firewall

Route 53 Resolver DNS Firewall can filter DNS queries by domain lists/rules.

Use for centralized DNS security controls.

# Part 107 — AWS Backup

Central backup management for supported resources.

Core objects:

```text
backup plan
vault
rule
selection
recovery point
```

# Part 108 — Backup Plan

Defines:

```text
schedule
retention
lifecycle
copy
vault
```

Use tags/resource selection for scale.

# Part 109 — Backup Vault

Logical container for recovery points.

Use:

```text
vault access policy
KMS
Vault Lock where appropriate
```

to protect backups.

# Part 110 — Backup Vault Lock

Can enforce WORM-style retention controls.

Important for ransomware-resistant/cyber-resilient backup patterns.

# Part 111 — Cross-Account Backup

Pattern:

```text
Workload Account
 ↓
Central Backup Account
```

reduces blast radius.

# Part 112 — Cross-Region Backup

Supports DR:

```text
Primary Region
 ↓ copy
DR Region
```

Consider RPO, transfer, KMS, and restoration dependencies.

# Part 113 — Point-in-Time Restore

PITR restores data to a chosen time inside supported retention window.

Useful after:

```text
accidental delete
bad application write
logical corruption
```

# Part 114 — Backup Testing

A backup is not proven until restored.

Test:

```text
restore
boot/connect
application consistency
data validation
RTO timing
```

# Part 115 — DR Procedures

SOA-C03 expects operational execution of:

```text
backup/restore
pilot light
warm standby
active-active
```

not only architectural recognition.

# Part 116 — Pilot Light Operations

During failover:

```text
validate replicated data
scale compute
restore missing services
switch DNS
verify
```

# Part 117 — Warm Standby Operations

DR environment is already functional at reduced scale.

Failover:

```text
scale
promote data if required
shift traffic
validate
```

# Part 118 — Active-Active Operations

Requires continuous:

```text
health monitoring
routing
replication
conflict handling
capacity
```

Operations complexity is highest.

# Part 119 — CloudFormation Operations

CloudFormation manages infrastructure stacks.

Operations include:

```text
create
update
change set
rollback
drift detection
delete
```

# Part 120 — Change Sets

Preview proposed stack changes.

Use before high-impact updates:

```text
template change
 ↓
change set
 ↓ review
execute
```

# Part 121 — CloudFormation Rollback

Failed update can trigger rollback.

Investigate:

```text
Events
resource failure
IAM
quota
dependency
```

rather than repeatedly retrying.

# Part 122 — CloudFormation Drift

Drift occurs when live resource differs from stack-defined state.

Example:

```text
engineer manually edits SG
```

Use drift detection and eliminate uncontrolled manual changes.

# Part 123 — StackSets

Deploy stacks across:

```text
multiple accounts
multiple Regions
```

Useful for:

```text
baseline roles
logging
security
operations resources
```

# Part 124 — AWS RAM

Share supported resources across accounts.

Operations must understand:

```text
owner
consumer
share
permission
lifecycle
```

# Part 125 — AWS CDK Concept

CDK defines infrastructure in programming languages and synthesizes CloudFormation.

SOA-C03 includes CDK awareness.

Operational source of truth is still version-controlled IaC.

# Part 126 — Terraform in AWS Operations

The current exam explicitly acknowledges third-party deployment automation such as Terraform and Git.

Operations rule:

```text
define ownership
avoid manual drift
review plan
manage state securely
```

# Part 127 — Deployment Strategies

Common:

```text
all-at-once
rolling
rolling with extra batch
immutable
blue/green
canary
```

Select by availability and rollback requirements.

# Part 128 — Blue/Green

```text
Blue = current
Green = new
```

Validate Green then shift traffic.

Rollback can be quick if Blue remains intact.

# Part 129 — Canary

Send small traffic subset to new version.

```text
5% new
95% old
```

Observe metrics before expanding.

# Part 130 — Rolling Deployment

Update subset at a time.

Tradeoff:

```text
less extra capacity
but temporary mixed versions
```

# Part 131 — Security Operations

CloudOps implements controls designed by security/governance teams.

Daily tasks:

```text
review findings
rotate credentials
patch
enforce encryption
investigate access
remediate drift
```

# Part 132 — IAM Access Troubleshooting

For AccessDenied inspect:

```text
identity
role session
IAM policy
resource policy
SCP
boundary
session policy
KMS policy
condition
```

# Part 133 — IAM Access Analyzer

Helps analyze external/public/cross-account access and policy access paths.

Use to identify unintended resource exposure.

# Part 134 — Policy Simulator Concept

Evaluate whether a policy permits/denies an action under modeled conditions.

Useful before changing production policies.

# Part 135 — MFA Operations

Enforce MFA for privileged humans.

Monitor:

```text
unused identities
old access keys
root activity
MFA coverage
```

# Part 136 — IAM Identity Center Operations

Manage:

```text
permission sets
account assignments
identity-source integration
session duration
```

and audit access regularly.

# Part 137 — KMS Operations

Operate:

```text
key policies
grants
rotation
aliases
usage
deletion schedule
CloudTrail logs
```

KMS access failures often involve both IAM and key policy.

# Part 138 — KMS Key Deletion

Deletion is deliberately delayed.

Operations should:

```text
disable first
observe dependency
schedule deletion
```

to avoid irrecoverable encrypted-data loss.

# Part 139 — ACM

Certificate Manager automates certificate lifecycle for supported AWS-integrated services.

Monitor renewal eligibility and DNS/email validation requirements.

# Part 140 — Secrets Manager

Use for secrets needing:

```text
secure storage
rotation
application retrieval
versioning
```

Audit access and rotation failures.

# Part 141 — Parameter Store SecureString

Appropriate for many secure configuration values.

Choose Secrets Manager when dedicated rotation/integration functionality is required.

# Part 142 — Security Hub

Centralizes security findings/posture from AWS security services and integrations.

Operations:

```text
triage
assign severity
remediate
suppress with reason
track
```

# Part 143 — GuardDuty

Threat detection findings may indicate:

```text
credential misuse
malicious network behavior
compromised workloads
```

Investigate context before remediation.

# Part 144 — Inspector

Vulnerability management for supported compute/container/serverless workloads.

Operations should prioritize by:

```text
exploitability
internet exposure
business criticality
fix availability
```

# Part 145 — AWS Config Compliance

Continuous compliance:

```text
Config
 ↓ rule/conformance pack
NON_COMPLIANT
 ↓
remediation
```

# Part 146 — Trusted Advisor Security Checks

SOA-C03 includes remediation based on Trusted Advisor security recommendations.

Treat recommendations as input, not blind automation.

# Part 147 — VPC Operations

Operate:

```text
CIDRs
subnets
route tables
SG
NACL
NAT
IGW
IPv6 egress
endpoints
peering
TGW
```

# Part 148 — Subnet Exhaustion

If deployment fails because subnet lacks IP addresses:

```text
inspect AvailableIpAddressCount
CIDR size
ENI consumers
load balancers
containers
endpoints
```

Subnet sizing is an operational capacity concern.

# Part 149 — NAT Troubleshooting

Private host Internet failure:

```text
private route → NAT?
NAT available?
NAT public subnet?
public route → IGW?
SG egress?
NACL?
DNS?
```

# Part 150 — Egress-Only Internet Gateway

IPv6 outbound-only Internet path for VPC workloads.

Conceptually similar objective to blocking unsolicited inbound while allowing outbound IPv6.

# Part 151 — VPC Endpoint Troubleshooting

Check:

```text
endpoint state
subnet/route
private DNS
SG for interface endpoint
endpoint policy
IAM/resource policy
```

# Part 152 — VPC Peering Troubleshooting

Check:

```text
peering active
routes both sides
non-overlapping CIDRs
SG/NACL
DNS options
transitivity assumption
```

# Part 153 — Transit Gateway Troubleshooting

Inspect:

```text
attachments
TGW route tables
associations
propagations
VPC subnet routes
security
```

# Part 154 — Network Logs

Useful:

```text
VPC Flow Logs
ELB access logs
WAF logs
CloudFront logs
container logs
```

Correlate timestamp and request identifiers.

# Part 155 — VPC Flow Logs

Fields expose:

```text
source/destination
port
protocol
ACCEPT/REJECT
bytes
packets
```

No packet payload.

# Part 156 — Flow Log REJECT

A reject can point toward:

```text
NACL
security control
route/path context
```

But absence of reject does not prove application health.

# Part 157 — Reachability Analyzer Concept

Analyzes network path configuration between supported source/destination.

Useful for configuration-level connectivity diagnosis without generating traffic.

# Part 158 — CloudFront Operations

Monitor:

```text
cache hit ratio
origin latency
4xx/5xx
requests
bytes
invalidations
```

# Part 159 — CloudFront Stale Cache

Check:

```text
TTL
Cache-Control
cache key
origin headers
invalidation
versioned object names
```

# Part 160 — Global Accelerator Operations

Monitor endpoint health and traffic distribution across AWS Regions/endpoints.

Use when network acceleration/static anycast architecture is required.

# Part 161 — Cost Operations

CloudOps should monitor cost continuously.

```text
resource telemetry
+
billing telemetry
=
operational efficiency
```

# Part 162 — Cost Explorer

Analyze:

```text
service
account
Region
usage type
tag
time
```

Use to locate cost changes.

# Part 163 — AWS Budgets

Create:

```text
monthly budget
forecast threshold
actual threshold
```

and route notifications to accountable owners.

# Part 164 — Compute Optimizer

Provides sizing recommendations for supported resources.

Validate with business context before applying.

# Part 165 — Savings Plans / Reservations Operations

Track:

```text
coverage
utilization
expiration
```

A discount commitment that is unused is waste.

# Part 166 — Idle Resource Detection

Common waste:

```text
unattached EBS
unused Elastic IP/public IPv4
idle load balancer
stopped resources with disks
old snapshots
idle RDS
NAT traffic inefficiency
```

# Part 167 — Tagging for Operations

Mandatory tags can include:

```text
Owner
Environment
Application
CostCenter
Criticality
BackupPolicy
PatchGroup
```

Tags support automation and accountability.

# Part 168 — Incident Severity

Define severity by business impact.

Example:

```text
SEV1 → critical customer outage
SEV2 → degraded major function
SEV3 → limited impact
```

Avoid classifying severity only by technical component.

# Part 169 — Incident Timeline

Record:

```text
detect
acknowledge
mitigate
recover
root cause
follow-up
```

Accurate timeline improves post-incident learning.

# Part 170 — Containment vs Remediation

Containment:

```text
stop damage now
```

Remediation:

```text
remove root cause
```

Example credential compromise:

```text
revoke key = containment
fix unsafe secret process = remediation
```

# Part 171 — Post-Incident Review

Blameless technical review should identify:

```text
trigger
contributing factors
detection gap
response gap
architecture gap
actions
owners
deadlines
```

# Part 172 — CloudOps CLI Safety

Before write commands:

```bash
aws sts get-caller-identity
aws configure get region
```

Then prefer:

```text
describe/get/list
```

for investigation first.

# Part 173 — Read-Only EC2 Discovery

```bash
aws ec2 describe-instances   --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,AZ:Placement.AvailabilityZone,Type:InstanceType}'   --output table
```

# Part 174 — CloudWatch Alarm Discovery

```bash
aws cloudwatch describe-alarms   --query 'MetricAlarms[].{Alarm:AlarmName,State:StateValue,Metric:MetricName}'   --output table
```

# Part 175 — ASG Discovery

```bash
aws autoscaling describe-auto-scaling-groups   --query 'AutoScalingGroups[].{Name:AutoScalingGroupName,Desired:DesiredCapacity,Min:MinSize,Max:MaxSize}'   --output table
```

# Part 176 — SSM Managed Nodes

```bash
aws ssm describe-instance-information   --query 'InstanceInformationList[].{Id:InstanceId,Ping:PingStatus,Platform:PlatformName}'   --output table
```

# Part 177 — RDS Discovery

```bash
aws rds describe-db-instances   --query 'DBInstances[].{DB:DBInstanceIdentifier,Status:DBInstanceStatus,MultiAZ:MultiAZ,Engine:Engine}'   --output table
```

# Part 178 — Backup Discovery

```bash
aws backup list-backup-vaults
aws backup list-backup-plans
```

Inspect recovery-point coverage before assuming backup is complete.

# Part 179 — VPC Flow Discovery

```bash
aws ec2 describe-flow-logs   --query 'FlowLogs[].{Id:FlowLogId,Resource:ResourceId,Status:FlowLogStatus}'   --output table
```

# Part 180 — CloudOps Final Mental Model

Professional AWS operations means:

```text
observe
understand
automate
limit blast radius
verify recovery
secure access
control cost
learn from failure
```

The objective is not keeping servers alive manually. It is operating reliable cloud services predictably.

---

# Supplemental Deep-Study Layer — AWS SysOps Administration / CloudOps Engineering

> **Source distinction:** The complete uploaded course remains preserved. The sections below are supplemental engineering expansion added for deeper architecture, operations, CLI/configuration, failure analysis, labs, and production troubleshooting.

Focus: SLO-driven operations, telemetry quality, Systems Manager safety, fleet/image/patch operations, backup validation, incident response, security investigation, network troubleshooting, cost anomalies, and auditable operations.

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

## Advanced Deep Dive 1 — Service Ownership and Operational Catalog

### Concept and Detailed Explanation

Every production service needs an owner, SLO, dashboard, runbooks, backup class, dependencies, escalation path, and cost center. Operations fail quickly when alerts cannot be mapped to accountable teams.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Service
 ├─ owner/on-call
 ├─ SLO
 ├─ dashboard
 ├─ runbooks
 ├─ backup
 └─ dependencies
```

### CLI / Configuration / Calculation

```bash
aws resourcegroupstaggingapi get-resources --output table 2>/dev/null || true
```

### Expected Behavior

Critical resources can be mapped to accountable service owners.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

An alarm includes service owner and runbook link so incident routing is immediate.

### Troubleshooting Workflow

```text
alert has no owner
 ↓ tags/catalog
 ↓ service mapping
 ↓ assign owner
 ↓ update alert/runbook
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Make service ownership mandatory production metadata.

---

## Advanced Deep Dive 2 — SLI/SLO/Error Budget

### Concept and Detailed Explanation

CloudOps should distinguish measurement (SLI), engineering target (SLO), and contractual commitment (SLA). Error budget turns reliability into operational decision data.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
SLI measured
 ↓
SLO target
 ↓
SLA promise
 ↓
error budget
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
m=30*24*60
slo=.999
print('allowed minutes',m*(1-slo))
PY
```

### Expected Behavior

Dashboards calculate the exact SLI used for operational decisions.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

An API with 99.9% SLO has roughly 43 minutes of monthly error budget.

### Troubleshooting Workflow

```text
reliability dispute
 ↓ SLI formula
 ↓ time window
 ↓ SLO
 ↓ burn rate
 ↓ action policy
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Define SLI math and error-budget policy before incidents.

---

## Advanced Deep Dive 3 — Burn-Rate Alerting

### Concept and Detailed Explanation

Monthly error budget can be consumed in hours. Multi-window burn-rate alerts identify rapid degradation while reducing noise from brief events.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Error budget
 ↓ actual failures
 ↓ fast burn + slow burn
 ↓ page / ticket
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Fast: 5m + 1h
Slow: 6h + 3d
Thresholds depend on SLO.
EOF
```

### Expected Behavior

Paging correlates with risk of exhausting the SLO rather than isolated CPU spikes.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Sustained failed-checkout burn pages the team while a harmless CPU burst does not.

### Troubleshooting Workflow

```text
too many pages
 ↓ SLI quality
 ↓ burn threshold
 ↓ windows
 ↓ actionability
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Page on user-impact burn; use component alarms for diagnosis.

---

## Advanced Deep Dive 4 — Golden Signals Dashboard

### Concept and Detailed Explanation

Start with latency, traffic, errors, and saturation, then drill into compute/database/network. CPU alone cannot represent service health.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
User service
 ↓ latency
 ↓ traffic
 ↓ errors
 ↓ saturation
 ↓ dependencies
```

### CLI / Configuration / Calculation

```bash
aws cloudwatch list-metrics --output table 2>/dev/null | head -40
```

### Expected Behavior

Operators see whether users are affected and which dependency is saturated.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

CPU is low but API latency rises because DB connections are exhausted.

### Troubleshooting Workflow

```text
service slow
 ↓ traffic?
 ↓ errors?
 ↓ latency percentile
 ↓ saturation
 ↓ dependency
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Lead dashboards with service/user signals.

---

## Advanced Deep Dive 5 — Percentiles Instead of Averages

### Concept and Detailed Explanation

Average latency can hide severe tail behavior. p95/p99 better represent the experience of slower requests while averages remain useful for broad capacity trends.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Many fast requests
 + few very slow
 ↓ average looks fine
 p99 exposes tail
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
p50 typical
p95 most users
p99 tail
EOF
```

### Expected Behavior

Latency SLO and alerts use percentiles appropriate to business need.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Average 150 ms hides p99 4 seconds.

### Troubleshooting Workflow

```text
latency complaint
 ↓ p50/p95/p99
 ↓ route/dependency
 ↓ trace slow requests
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Do not use only average latency for interactive services.

---

## Advanced Deep Dive 6 — Metric Math for Operational Ratios

### Concept and Detailed Explanation

Derived metrics such as error rate, availability, backlog per worker, and saturation ratios often answer operational questions better than raw counters.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
raw metrics
 ↓ expression
 ↓ derived SLI/operational metric
 ↓ alarm/dashboard
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
error_rate = 100 * errors / requests
backlog_per_worker = queue_depth / max(workers,1)
EOF
```

### Expected Behavior

Dashboards show ratios that map directly to operations decisions.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Workers scale from backlog per worker instead of absolute queue depth.

### Troubleshooting Workflow

```text
derived metric wrong
 ↓ period/statistics
 ↓ dimensions
 ↓ missing data
 ↓ zero denominator
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use metric math to encode operational meaning.

---

## Advanced Deep Dive 7 — Missing Telemetry Semantics

### Concept and Detailed Explanation

No data may mean idle service, deleted resource, failed agent, or monitoring outage. Configure alarm missing-data behavior according to what absence means.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Metric stops
 ↓ expected idle?
 or telemetry failure?
 ↓ alarm semantics
```

### CLI / Configuration / Calculation

```bash
aws cloudwatch describe-alarms --output json 2>/dev/null || true
```

### Expected Behavior

Heartbeat absence pages; sparse business-event metrics do not create false alerts.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

CloudWatch Agent heartbeat stops and is treated as breaching.

### Troubleshooting Workflow

```text
INSUFFICIENT_DATA
 ↓ metric emitted?
 ↓ agent/service
 ↓ dimensions/period
 ↓ expected sparse?
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Define missing-data meaning for every critical alarm.

---

## Advanced Deep Dive 8 — Structured Logging Schema

### Concept and Detailed Explanation

Stable JSON fields make incident queries reliable. Standardize service, environment, deployment version, request ID, trace ID, error code, and resource identity while excluding secrets and unnecessary PII.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
App
 ↓ structured JSON
CloudWatch Logs
 ↓ Logs Insights
 ↓ incident query
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
{"level":"ERROR","service":"orders","request_id":"abc","version":"v42","error_code":"DB_TIMEOUT"}
EOF
```

### Expected Behavior

Logs can be grouped and filtered by fields without fragile parsing.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Errors are grouped by deployment version in seconds.

### Troubleshooting Workflow

```text
logs hard to query
 ↓ structured?
 ↓ consistent field names?
 ↓ PII/secrets?
 ↓ retention
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Define a logging schema and prohibit secret values in logs.

---

## Advanced Deep Dive 9 — Log Retention by Data Class

### Concept and Detailed Explanation

Application debug, security audit, compliance, and network logs have different retention needs. Explicit retention controls cost and governance.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Debug → short
Operational → medium
Security/compliance → longer/protected
```

### CLI / Configuration / Calculation

```bash
aws logs describe-log-groups --query 'logGroups[].{Group:logGroupName,Retention:retentionInDays,Bytes:storedBytes}' --output table
```

### Expected Behavior

Every production log group has an intentional retention period.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Verbose debug logs keep 30 days while audit logs archive longer.

### Troubleshooting Workflow

```text
log cost high
 ↓ largest groups
 ↓ retention
 ↓ verbosity
 ↓ archive requirement
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Set retention explicitly; never-expire should be rare and justified.

---

## Advanced Deep Dive 10 — CloudTrail Session Reconstruction

### Concept and Detailed Explanation

Investigate the assumed-role session, source identity/session name, source IP, user agent, request ID, and related API calls—not only the role name.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Human/CI
 ↓ STS role session
 ↓ API calls
 ↓ CloudTrail timeline
```

### CLI / Configuration / Calculation

```bash
aws cloudtrail lookup-events --max-results 20 --output table 2>/dev/null || true
```

### Expected Behavior

Investigators can map a shared role session back to a human or pipeline.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A production role action is traced to a specific CI run using session metadata.

### Troubleshooting Workflow

```text
unexpected API
 ↓ event/session
 ↓ source identity
 ↓ source IP/user agent
 ↓ related actions
 ↓ contain
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Preserve source identity in federation and automation sessions.

---

## Advanced Deep Dive 11 — CloudTrail + Config Incident Reconstruction

### Concept and Detailed Explanation

CloudTrail explains who called APIs; Config explains resource state before and after. Together they reconstruct configuration incidents.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Config state v1
 ↓ API call
Config state v2
 ↓ noncompliant
 + CloudTrail actor
```

### CLI / Configuration / Calculation

```bash
aws configservice get-resource-config-history --resource-type AWS::EC2::SecurityGroup --resource-id <ID> 2>/dev/null || true
```

### Expected Behavior

Before/after configuration and actor are attributable.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A public SSH rule is traced to one API call/session.

### Troubleshooting Workflow

```text
resource changed
 ↓ Config timeline
 ↓ exact time
 ↓ CloudTrail lookup
 ↓ actor/action
 ↓ remediate
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use Config and CloudTrail together.

---

## Advanced Deep Dive 12 — EventBridge Retry/DLQ Operations

### Concept and Detailed Explanation

Event-driven automation needs retry limits, target permissions, DLQs, and replay ownership. A failed target must not silently lose remediation events.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Event
 ↓ rule
 ↓ target
 failure
 ↓ retry
 ↓ DLQ
 ↓ replay
```

### CLI / Configuration / Calculation

```bash
aws events list-rules --output table 2>/dev/null || true
aws events list-targets-by-rule --rule <RULE> 2>/dev/null || true
```

### Expected Behavior

Failed deliveries become visible and recoverable.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Automation Lambda loses permission; events land in DLQ until repaired.

### Troubleshooting Workflow

```text
event missing
 ↓ pattern match
 ↓ target permission
 ↓ target errors/throttling
 ↓ DLQ
 ↓ replay
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Every automation event path needs explicit failure handling.

---

## Advanced Deep Dive 13 — Automated Remediation Guardrails

### Concept and Detailed Explanation

Automated remediation should be narrow, idempotent, tagged/opt-in, canaried where possible, rate-limited, verified, and stopped on unexpected errors.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Detect
 ↓ verify preconditions
 ↓ remediate canary
 ↓ health check
 ↓ continue/stop
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
AutoRemediate=true
maxConcurrency=1
maxErrors=1
verifyAfter=true
EOF
```

### Expected Behavior

Automation fixes known issues without touching unrelated resources.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

SSM runbook restarts only tagged services and verifies health.

### Troubleshooting Workflow

```text
automation harmful
 ↓ stop rule
 ↓ scope
 ↓ preconditions
 ↓ rollback
 ↓ review
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Automate only well-understood failure modes with bounded blast radius.

---

## Advanced Deep Dive 14 — Session Manager Audit

### Concept and Detailed Explanation

Session Manager reduces public SSH exposure, but privileged shell access still needs IAM control, session attribution, and protected logging according to policy.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Operator
 ↓ IAM/SSO
Session Manager
 ↓ private EC2
 ↓ audit destination
```

### CLI / Configuration / Calculation

```bash
aws ssm describe-instance-information --output table 2>/dev/null || true
```

### Expected Behavior

Privileged sessions are attributable to federated identities.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Production servers have no public SSH and are managed through SSM.

### Troubleshooting Workflow

```text
session unavailable
 ↓ managed-node status
 ↓ IAM
 ↓ endpoints/network
 ↓ session preferences
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use identity-aware administration and protect session logs.

---

## Advanced Deep Dive 15 — Run Command Blast Radius

### Concept and Detailed Explanation

Fleet-wide Run Command is production deployment. Use tag targeting, canaries, MaxConcurrency, MaxErrors, timeouts, and output capture.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
command
 ↓ canary
 ↓ small batch
 ↓ verify
 ↓ wider fleet
 stop on errors
```

### CLI / Configuration / Calculation

```bash
aws ssm list-command-invocations --details --max-results 20 2>/dev/null || true
```

### Expected Behavior

A bad command stops before affecting the entire fleet.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Read-only diagnostics run on 5% of servers before expansion.

### Troubleshooting Workflow

```text
command failure
 ↓ affected targets
 ↓ command output
 ↓ error threshold
 ↓ stop/correct
 ↓ reconcile
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat remote execution like production change.

---

## Advanced Deep Dive 16 — Patch Rings

### Concept and Detailed Explanation

Patch deployment should move through development, staging, production canary, and production fleet with application validation at each step.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Dev → Stage → Prod Canary → Prod Fleet
          ↑ validation gates
```

### CLI / Configuration / Calculation

```bash
aws ssm describe-patch-baselines --output table 2>/dev/null || true
```

### Expected Behavior

Production receives patches only after lower rings pass.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Kernel patch breaks a driver in staging and is blocked from production.

### Troubleshooting Workflow

```text
patch failure
 ↓ package/kernel
 ↓ reboot/service
 ↓ rollback possible?
 ↓ image replacement/forward fix
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use patch rings and know the recovery path before approval.

---

## Advanced Deep Dive 17 — Maintenance Window Capacity

### Concept and Detailed Explanation

Maintenance removes service capacity. Plan batches from minimum healthy instances, quorum, restart time, load-balancer drain, and rollback deadline.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Window start
 ↓ batch
 ↓ verify
 ↓ next batch
 ↓ rollback deadline
 ↓ end
```

### CLI / Configuration / Calculation

```bash
aws ssm describe-maintenance-windows --output table 2>/dev/null || true
```

### Expected Behavior

Service remains above minimum capacity throughout maintenance.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Only one quorum member is maintained at once.

### Troubleshooting Workflow

```text
maintenance outage
 ↓ batch size
 ↓ remaining capacity
 ↓ health
 ↓ rollback deadline
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Calculate maintenance concurrency from surviving capacity.

---

## Advanced Deep Dive 18 — Golden AMI Provenance

### Concept and Detailed Explanation

A production AMI should map to source image, patch baseline, build commit, security scans, tests, owner, and deprecation date.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Trusted base
 ↓ patch/harden
 ↓ test/scan
 ↓ AMI ID
 ↓ launch template
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-images --owners self --query 'Images[].{ImageId:ImageId,Name:Name,CreationDate:CreationDate}' --output table
```

### Expected Behavior

Every running instance can be mapped to a known approved image.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A vulnerable AMI version is identified across the fleet quickly.

### Troubleshooting Workflow

```text
unknown image
 ↓ instance ImageId
 ↓ AMI metadata
 ↓ build pipeline
 ↓ source/scan
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Tag images with provenance and retire obsolete versions.

---

## Advanced Deep Dive 19 — ASG Scaling Activity Diagnosis

### Concept and Detailed Explanation

Scaling activity history often explains why capacity did not launch: quota, subnet IP, KMS, AMI, launch template, health, or capacity errors.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
scaling policy
 ↓ desired change
 ↓ launch
   └─ failure reason in activity
```

### CLI / Configuration / Calculation

```bash
aws autoscaling describe-scaling-activities --auto-scaling-group-name <ASG> --max-items 20 2>/dev/null || true
```

### Expected Behavior

The exact launch failure is identified before thresholds are changed.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

KMS permission blocks launch of encrypted AMI instances.

### Troubleshooting Workflow

```text
ASG not scaling
 ↓ activity message
 ↓ quota/capacity
 ↓ template/AMI
 ↓ subnet IP
 ↓ KMS/IAM
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Read scaling activity evidence first.

---

## Advanced Deep Dive 20 — Instance Refresh Safety

### Concept and Detailed Explanation

Instance Refresh needs minimum healthy percentage, warm-up, checkpoints, and application-level health. EC2 running state is not enough.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
old fleet
 ↓ replace batch
new instances
 ↓ warm up
 ↓ ALB/app health
 ↓ continue/rollback
```

### CLI / Configuration / Calculation

```bash
aws autoscaling describe-instance-refreshes --auto-scaling-group-name <ASG> 2>/dev/null || true
```

### Expected Behavior

A bad AMI stops before healthy capacity is exhausted.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

New instances boot but fail readiness, so refresh halts.

### Troubleshooting Workflow

```text
refresh stuck
 ↓ launch
 ↓ warmup
 ↓ target health
 ↓ capacity
 ↓ image/config
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Gate refresh on workload readiness.

---

## Advanced Deep Dive 21 — Container Exit-Code Triage

### Concept and Detailed Explanation

ECS task failure can be image pull, scheduling, OOM, application crash, health failure, IAM, network, or secret. Start with stopped reason and exit code.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
schedule
 ↓ image pull
 ↓ start
 ↓ exit code
 ↓ health
 ↓ service stability
```

### CLI / Configuration / Calculation

```bash
aws ecs list-tasks --cluster <CLUSTER> 2>/dev/null || true
aws ecs describe-tasks --cluster <CLUSTER> --tasks <TASK> 2>/dev/null || true
```

### Expected Behavior

Exit/stopped evidence points to the right layer.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Exit 137 suggests memory pressure rather than routing.

### Troubleshooting Workflow

```text
task stopped
 ↓ stoppedReason
 ↓ exit code
 ↓ logs
 ↓ CPU/memory
 ↓ IAM/network/secret
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Start from task/container termination evidence.

---

## Advanced Deep Dive 22 — EBS End-to-End Performance

### Concept and Detailed Explanation

Storage latency can be constrained by application access pattern, filesystem, volume IOPS/throughput, or EC2 EBS bandwidth. Increasing volume performance may not fix instance-level bottlenecks.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
App
 ↓ filesystem
 ↓ EBS volume
 ↓ instance EBS channel
 ↓ backend
```

### CLI / Configuration / Calculation

```bash
iostat -xz 1 5 2>/dev/null || true
aws ec2 describe-volumes --volume-ids <VOL> 2>/dev/null || true
```

### Expected Behavior

Operators can identify whether bottleneck is volume, instance, or app.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

High-IOPS volume remains slow because instance EBS bandwidth is saturated.

### Troubleshooting Workflow

```text
disk slow
 ↓ queue/latency
 ↓ volume IOPS/throughput
 ↓ instance limit
 ↓ app pattern
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Check the whole I/O path before resizing.

---

## Advanced Deep Dive 23 — S3 Replication Monitoring

### Concept and Detailed Explanation

Replication used for DR/compliance must be monitored. Role permissions, destination policy, KMS, object eligibility, and replication configuration can cause silent lag/failure.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
source
 ↓ replication rule/role/KMS
 ↓ destination
 ↓ status monitoring
```

### CLI / Configuration / Calculation

```bash
aws s3api get-bucket-replication --bucket <BUCKET> 2>/dev/null || true
```

### Expected Behavior

Replication failures are detected before DR data silently falls behind.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

KMS policy change breaks CRR and monitoring catches it.

### Troubleshooting Workflow

```text
replication fail
 ↓ rule
 ↓ object eligible
 ↓ role
 ↓ destination policy
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

Alert on replication health when it is a recovery control.

---

## Advanced Deep Dive 24 — Incomplete Multipart Upload Cleanup

### Concept and Detailed Explanation

Abandoned multipart uploads continue consuming storage. Lifecycle cleanup should abort incomplete uploads after a defined period.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
multipart upload
 ↓ abandoned parts
 ↓ hidden storage cost
 ↓ lifecycle abort
```

### CLI / Configuration / Calculation

```bash
aws s3api list-multipart-uploads --bucket <BUCKET> 2>/dev/null || true
```

### Expected Behavior

Old incomplete uploads do not accumulate.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Failed migration leaves partial uploads that lifecycle removes.

### Troubleshooting Workflow

```text
storage unexplained
 ↓ multipart uploads
 ↓ age/client failures
 ↓ lifecycle rule
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Add multipart cleanup to large-upload buckets.

---

## Advanced Deep Dive 25 — RDS Wait Analysis

### Concept and Detailed Explanation

Database CPU can be low while queries wait on locks, I/O, or concurrency. Use database load/wait evidence rather than CPU alone.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
DB load
 ├─ CPU
 ├─ I/O waits
 ├─ locks
 └─ connection waits
```

### CLI / Configuration / Calculation

```bash
aws rds describe-db-instances --output table 2>/dev/null || true
aws cloudwatch list-metrics --namespace AWS/RDS 2>/dev/null | head -40
```

### Expected Behavior

Operators identify the dominant wait before resizing.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Low CPU but lock waits cause application latency.

### Troubleshooting Workflow

```text
DB slow
 ↓ load/waits
 ↓ top SQL
 ↓ locks
 ↓ connections
 ↓ storage
 ↓ CPU
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use database-native load evidence before scaling.

---

## Advanced Deep Dive 26 — DynamoDB Throttle vs Hot Key

### Concept and Detailed Explanation

Adding total capacity does not necessarily fix a hot partition. Inspect request distribution, key design, GSIs, and workload skew.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
table aggregate OK
but hot key
 ↓ throttling
```

### CLI / Configuration / Calculation

```bash
aws cloudwatch list-metrics --namespace AWS/DynamoDB 2>/dev/null | head -60
```

### Expected Behavior

Aggregate capacity and partition-distribution failures are distinguished.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

One tenant generates most writes and remains throttled after capacity increase.

### Troubleshooting Workflow

```text
throttle
 ↓ capacity mode
 ↓ consumed/throttled
 ↓ key distribution
 ↓ GSI
 ↓ redesign
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat hot-key failures as data-model problems.

---

## Advanced Deep Dive 27 — ALB 5xx Ownership

### Concept and Detailed Explanation

Differentiate load-balancer-generated 5xx from target-generated 5xx. The correct evidence source depends on where the error originates.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Client
 ↓ ALB
 ├─ ALB error
 └─ target → target 5xx
```

### CLI / Configuration / Calculation

```bash
aws cloudwatch list-metrics --namespace AWS/ApplicationELB 2>/dev/null | head -60
aws elbv2 describe-target-health --target-group-arn <TG> 2>/dev/null || true
```

### Expected Behavior

Incident triage identifies the component generating errors.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

ALB connection reset metrics rise while application logs show process crashes.

### Troubleshooting Workflow

```text
ALB 5xx
 ↓ ELB vs Target 5xx
 ↓ target health
 ↓ app logs
 ↓ timeout/reset/dependency
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Separate front-door, target, and dependency errors.

---

## Advanced Deep Dive 28 — NAT Connection Capacity

### Concept and Detailed Explanation

Large fan-out through NAT can produce connection exhaustion symptoms. Monitor NAT metrics and connection reuse, especially when many private clients call one destination.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
many private clients
 ↓ NAT
 ↓ same external endpoint
 ↓ connection pressure
```

### CLI / Configuration / Calculation

```bash
aws cloudwatch list-metrics --namespace AWS/NATGateway 2>/dev/null | head -50
```

### Expected Behavior

NAT capacity is observable for high-scale egress workloads.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Container fleet opens many short connections to one SaaS API and sees intermittent failures.

### Troubleshooting Workflow

```text
egress intermittent
 ↓ NAT metrics
 ↓ connection count
 ↓ destination concentration
 ↓ pooling/additional egress design
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Monitor NAT for high fan-out egress patterns.

---

## Advanced Deep Dive 29 — Flow Logs Limitations

### Concept and Detailed Explanation

VPC Flow Logs contain network metadata, not payload. ACCEPT proves network controls allowed a flow; it does not prove TLS, authentication, or application success.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
packet
 ↓ flow metadata
 src/dst/port/bytes
 ACCEPT/REJECT
 no payload
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-flow-logs --output table 2>/dev/null || true
```

### Expected Behavior

Operators escalate to application/TLS evidence when flow is accepted.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Flow is ACCEPT on 443, so investigation moves to certificate/application layer.

### Troubleshooting Workflow

```text
connection fails
 ↓ flow ACCEPT/REJECT
 ↓ if REJECT → network policy
 ↓ if ACCEPT → transport/TLS/app
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use the lowest evidence layer that can answer the question.

---

## Advanced Deep Dive 30 — Restore Testing and RTO

### Concept and Detailed Explanation

Backup success is not recovery success. Restore a disposable copy, connect, validate application/data consistency, and measure the full recovery time.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
backup
 ↓ recovery point
 ↓ restore
 ↓ boot/connect
 ↓ validate
 ↓ measured RTO
```

### CLI / Configuration / Calculation

```bash
aws backup list-backup-vaults --output table 2>/dev/null || true
```

### Expected Behavior

Restore drills prove recovery points are usable.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

RDS backup exists but DR restore fails because KMS permissions were never tested.

### Troubleshooting Workflow

```text
restore fail
 ↓ recovery point
 ↓ KMS/IAM
 ↓ network
 ↓ app validation
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Track restore success and restore time as KPIs.

---

## Advanced Deep Dive 31 — PITR for Logical Corruption

### Concept and Detailed Explanation

Replication can copy bad writes. Point-in-time recovery protects against logical corruption such as accidental DELETE or bad application writes.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
bad write at 14:03
 ↓ replicated
PITR to 14:02:59
 ↓ clean restore
```

### CLI / Configuration / Calculation

```bash
aws dynamodb describe-continuous-backups --table-name <TABLE> 2>/dev/null || true
```

### Expected Behavior

Runbooks distinguish infrastructure outage from logical-data corruption.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Bad deployment deletes rows; Multi-AZ cannot help, so PITR is used.

### Troubleshooting Workflow

```text
logical corruption
 ↓ stop bad writer
 ↓ identify timestamp
 ↓ restore PITR
 ↓ validate
 ↓ reconcile newer valid data
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design for logical corruption, not only hardware failure.

---

## Advanced Deep Dive 32 — CloudFormation Drift Ownership

### Concept and Detailed Explanation

Drift often means unclear ownership. If humans and multiple automation tools edit the same resource, desired state becomes unreliable.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
IaC desired state
 ↓ manual/other tool
 live resource differs
 ↓ drift
```

### CLI / Configuration / Calculation

```bash
aws cloudformation detect-stack-drift --stack-name <STACK> 2>/dev/null || true
```

### Expected Behavior

Drift is corrected in the authoritative source or ownership is intentionally changed.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Manual SG rule is removed because CloudFormation owns the resource.

### Troubleshooting Workflow

```text
drift
 ↓ who changed?
 ↓ CloudTrail
 ↓ resource owner/tool
 ↓ reconcile/import
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Give each resource one authoritative writer.

---

## Advanced Deep Dive 33 — StackSets Progressive Rollout

### Concept and Detailed Explanation

Organization-wide deployment can amplify mistakes. Use canary accounts/OUs, concurrency limits, and failure tolerance before expanding.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
StackSet
 ↓ Canary OU
 ↓ Stage OU
 ↓ Prod OU
```

### CLI / Configuration / Calculation

```bash
aws cloudformation list-stack-sets --status ACTIVE 2>/dev/null || true
```

### Expected Behavior

A bad baseline stops before organization-wide impact.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

New Config baseline is tested in a security OU first.

### Troubleshooting Workflow

```text
StackSet failure
 ↓ account/Region
 ↓ operation result
 ↓ failure tolerance
 ↓ stop/fix/retry
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat multi-account deployment like progressive release.

---

## Advanced Deep Dive 34 — IAM AccessDenied Ladder

### Concept and Detailed Explanation

AccessDenied can come from identity policy, permission boundary, session policy, SCP, resource policy, endpoint policy, KMS, or conditions. Follow a fixed evaluation ladder.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Caller
 ↓ identity
 ↓ boundary/session
 ↓ SCP
 ↓ resource policy
 ↓ KMS/endpoint
 ↓ conditions
```

### CLI / Configuration / Calculation

```bash
aws sts get-caller-identity
aws iam simulate-principal-policy --policy-source-arn <ARN> --action-names <ACTION> 2>/dev/null || true
```

### Expected Behavior

The denying layer is identified before permissions are broadened.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Role allows S3 but SCP denies the Region.

### Troubleshooting Workflow

```text
AccessDenied
 ↓ caller/action/resource
 ↓ IAM
 ↓ boundary/session
 ↓ SCP
 ↓ resource/KMS/endpoint
 ↓ conditions
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Never use admin access as the first troubleshooting step.

---

## Advanced Deep Dive 35 — Credential Compromise Containment

### Concept and Detailed Explanation

Containment should revoke/disable compromised access, preserve audit evidence, enumerate affected actions/resources, rotate downstream secrets, and rebuild trust.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
detect
 ↓ revoke/deny
 ↓ preserve CloudTrail
 ↓ scope impact
 ↓ rotate/repair
 ↓ verify
```

### CLI / Configuration / Calculation

```bash
aws cloudtrail lookup-events --max-results 50 2>/dev/null || true
```

### Expected Behavior

Compromised credentials stop working and impact is bounded.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Leaked key is disabled while CloudTrail timeline is reviewed.

### Troubleshooting Workflow

```text
credential incident
 ↓ principal/session
 ↓ revoke
 ↓ API timeline
 ↓ affected resources
 ↓ rotate
 ↓ validate
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Contain first, then eradicate root cause.

---

## Advanced Deep Dive 36 — KMS Dependency Inventory

### Concept and Detailed Explanation

Disabling or deleting a KMS key can make many resources unreadable. Track which EBS, RDS, S3, backups, and secrets depend on each critical key.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
KMS key
 ├─ EBS
 ├─ RDS
 ├─ S3
 ├─ backup
 └─ secret
```

### CLI / Configuration / Calculation

```bash
aws kms list-aliases --output table 2>/dev/null || true
```

### Expected Behavior

Key changes are reviewed with a known blast radius.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Key retirement is delayed because old snapshots still depend on it.

### Troubleshooting Workflow

```text
KMS change
 ↓ dependent resources
 ↓ backups/DR
 ↓ migrate/re-encrypt
 ↓ disable before delete
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Never delete a key without dependency evidence.

---

## Advanced Deep Dive 37 — Cost Anomaly as Incident Signal

### Concept and Detailed Explanation

Unexpected cost can reveal retry loops, runaway scaling, logging storms, bad routing, data-scan growth, or abuse. Cost telemetry belongs in operational review.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
behavior change
 ↓ resource usage
 ↓ cost anomaly
 ↓ operational investigation
```

### CLI / Configuration / Calculation

```bash
aws ce get-cost-and-usage --time-period Start=2026-08-01,End=2026-08-20 --granularity DAILY --metrics UnblendedCost 2>/dev/null || true
```

### Expected Behavior

Cost changes are correlated with deployments, traffic, and usage type.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

NAT cost doubles after routing change sends S3 traffic through NAT.

### Troubleshooting Workflow

```text
bill spike
 ↓ account/service
 ↓ usage type
 ↓ tag/resource
 ↓ deployment/traffic
 ↓ root cause
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat cost anomalies as possible system-health signals.

---

## Advanced Deep Dive 38 — Incident Command Roles

### Concept and Detailed Explanation

Large incidents need explicit coordination roles so technical work, communication, and timeline recording proceed in parallel.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Incident Commander
 ├─ Ops lead
 ├─ Communications
 ├─ Scribe
 └─ SMEs
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
IC:
Ops:
Comms:
Scribe:
Impact:
Current mitigation:
Next update:
EOF
```

### Expected Behavior

Responders know who decides, who troubleshoots, and who communicates.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

During regional incident the IC coordinates while DB and network SMEs investigate.

### Troubleshooting Workflow

```text
incident chaotic
 ↓ assign IC
 ↓ define objective
 ↓ parallel workstreams
 ↓ update cadence
 ↓ decision log
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Separate incident coordination from hands-on debugging.

---

## Advanced Deep Dive 39 — Mitigation Before Root Cause

### Concept and Detailed Explanation

During active outage, restoring acceptable service often matters more than immediately proving exact root cause. Use safe known mitigations first while preserving evidence.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
detect
 ↓ mitigate/restore
 ↓ stabilize
 ↓ evidence
 ↓ root cause
 ↓ prevention
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Mitigation: shift traffic to healthy Region.
Root-cause analysis continues after service stabilizes.
EOF
```

### Expected Behavior

MTTR is reduced without losing diagnostic evidence.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Traffic fails over before deep database analysis.

### Troubleshooting Workflow

```text
outage ongoing
 ↓ safe mitigation?
 ↓ execute/verify
 ↓ preserve logs
 ↓ root cause later
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Restore service first when a safe mitigation exists.

---

## Advanced Deep Dive 40 — Post-Incident Action Quality

### Concept and Detailed Explanation

Good action items change systems—tests, policies, automation, architecture, alerts, ownership, or runbooks. 'Be more careful' is not an engineering control.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
incident
 ↓ contributing factor
 ↓ control gap
 ↓ specific action
 ↓ owner/date
 ↓ verification
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Bad: Be more careful.
Good: CI policy blocks public RDS endpoints; owner=platform; due=2026-09-15.
EOF
```

### Expected Behavior

Follow-up items measurably reduce recurrence or impact.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Public SG incident leads to CI policy and Config rule.

### Troubleshooting Workflow

```text
same incident repeats
 ↓ old actions
 ↓ systemic?
 ↓ completed?
 ↓ verified effective?
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Write actions that modify the system, not human intention.

---

## Advanced Deep Dive 41 — Operational Readiness Review

### Concept and Detailed Explanation

Before production, require owner/on-call, SLO, dashboard, alerts, backup/restore, capacity/quota, security logging, deployment/rollback, and runbooks.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Build complete
 ↓ ORR
 pass → launch
 gaps → remediate
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
[ ] SLO
[ ] dashboard
[ ] paging
[ ] runbook
[ ] backup restore test
[ ] quota
[ ] rollback
[ ] owner/on-call
EOF
```

### Expected Behavior

Production launch has explicit operations acceptance.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Release is delayed until restore test and on-call runbook are ready.

### Troubleshooting Workflow

```text
service not supportable
 ↓ missing ORR item
 ↓ assign owner
 ↓ close gap
 ↓ re-review
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Make operational readiness a launch gate.

---

## Advanced Deep Dive 42 — Runbook Stop Conditions

### Concept and Detailed Explanation

A runbook needs prerequisites, evidence, actions, expected output, stop conditions, rollback/forward-fix, escalation, and verification.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
symptom
 ↓ preconditions
 ↓ evidence
 ↓ action
 ↓ verify
 pass/fail
 ↓ close or stop/escalate
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Stop if:
- >1 production host fails
- backup not current
- customer errors increase
EOF
```

### Expected Behavior

Operators know when not to continue a dangerous procedure.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

ALB runbook defines when to drain one target and when to stop.

### Troubleshooting Workflow

```text
runbook harmful
 ↓ scope?
 ↓ preconditions?
 ↓ stop condition?
 ↓ verification?
 ↓ update/test
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Write stop conditions as carefully as commands.

---

## Advanced Deep Dive 43 — Multi-Region Readiness

### Concept and Detailed Explanation

Standby Region must maintain deployment parity, data freshness, quotas, keys, secrets, artifacts, DNS, certificates, and monitoring—not merely a replicated database.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Region A active
 ↕ replication/health
Region B standby
 ↓ readiness checks
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-regions --output table 2>/dev/null || true
```

### Expected Behavior

Operations can prove DR Region is ready before disaster.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Standby app image is one release behind and readiness check detects it.

### Troubleshooting Workflow

```text
DR not ready
 ↓ app version
 ↓ data lag
 ↓ quota
 ↓ keys/secrets
 ↓ routing
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Continuously monitor standby readiness.

---

## Advanced Deep Dive 44 — Failback Procedure

### Concept and Detailed Explanation

Failback is distinct from failover. Data created in DR must be synchronized, write ownership must be clear, primary capacity validated, and split-brain prevented.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
failover to B
 ↓ writes occur in B
A recovers
 ↓ resync
 ↓ validate A
 ↓ shift traffic
 ↓ monitor
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Failback prerequisites:
single write owner
data sync complete
version parity
capacity healthy
rollback path
EOF
```

### Expected Behavior

Failback preserves all data created during the disaster interval.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Database replication is re-established before DNS returns to primary.

### Troubleshooting Workflow

```text
failback risk
 ↓ current writer
 ↓ data delta
 ↓ resync
 ↓ validate
 ↓ traffic shift
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design and test failback separately.

---

## Advanced Deep Dive 45 — Capacity Forecasting

### Concept and Detailed Explanation

Autoscaling handles short-term demand but not every long-term ceiling. Forecast subnet IPs, quotas, database storage, connections, egress, and budget.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
historical demand
 ↓ trend
 ↓ forecast
 ↓ quota/capacity action
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Forecast:
peak RPS
DB growth GB/day
subnet free IP
SQS peak depth
monthly egress
EOF
```

### Expected Behavior

Teams act before hard limits are reached.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

DB growth forecast triggers archive work months before full storage.

### Troubleshooting Workflow

```text
capacity surprise
 ↓ missing leading metric
 ↓ trend
 ↓ hard limit
 ↓ forecast horizon
 ↓ action
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Monitor headroom and growth rate, not only current utilization.

---

## Advanced Deep Dive 46 — Evidence Chain for Operations

### Concept and Detailed Explanation

A mature operation can link Git/IaC version, deployment execution, resource state, runtime telemetry, incident timeline, remediation, and corrective change.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Git commit
 ↓ deployment run
 ↓ resource state
 ↓ telemetry
 ↓ incident
 ↓ remediation
 ↓ verification
 ↓ follow-up PR
```

### CLI / Configuration / Calculation

```bash
aws cloudtrail lookup-events --max-results 10 2>/dev/null || true
aws cloudwatch describe-alarms --state-value ALARM --output table 2>/dev/null || true
```

### Expected Behavior

Incidents and changes can be reconstructed from durable evidence.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Postmortem links CloudFormation commit, pipeline, CloudTrail event, alarm, SSM runbook, and corrective PR.

### Troubleshooting Workflow

```text
missing evidence
 ↓ which link absent?
 ↓ logging/deploy metadata
 ↓ correlation/run IDs
 ↓ retention
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design intent, execution, and outcome to be auditable.

---

# Supplemental Hands-on Lab Series — AWS SysOps Administration / CloudOps Engineering

## Enhanced Lab 1 — Service Ownership and Operational Catalog

### Objective

Turn **Service Ownership and Operational Catalog** into an evidence-based AWS exercise.

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

Critical resources can be mapped to accountable service owners.

### Troubleshooting Path

```text
alert has no owner
 ↓ tags/catalog
 ↓ service mapping
 ↓ assign owner
 ↓ update alert/runbook
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

## Enhanced Lab 2 — SLI/SLO/Error Budget

### Objective

Turn **SLI/SLO/Error Budget** into an evidence-based AWS exercise.

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
m=30*24*60
slo=.999
print('allowed minutes',m*(1-slo))
PY
```

### Expected Result

Dashboards calculate the exact SLI used for operational decisions.

### Troubleshooting Path

```text
reliability dispute
 ↓ SLI formula
 ↓ time window
 ↓ SLO
 ↓ burn rate
 ↓ action policy
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

## Enhanced Lab 3 — Burn-Rate Alerting

### Objective

Turn **Burn-Rate Alerting** into an evidence-based AWS exercise.

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
Fast: 5m + 1h
Slow: 6h + 3d
Thresholds depend on SLO.
EOF
```

### Expected Result

Paging correlates with risk of exhausting the SLO rather than isolated CPU spikes.

### Troubleshooting Path

```text
too many pages
 ↓ SLI quality
 ↓ burn threshold
 ↓ windows
 ↓ actionability
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

## Enhanced Lab 4 — Golden Signals Dashboard

### Objective

Turn **Golden Signals Dashboard** into an evidence-based AWS exercise.

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
aws cloudwatch list-metrics --output table 2>/dev/null | head -40
```

### Expected Result

Operators see whether users are affected and which dependency is saturated.

### Troubleshooting Path

```text
service slow
 ↓ traffic?
 ↓ errors?
 ↓ latency percentile
 ↓ saturation
 ↓ dependency
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

## Enhanced Lab 5 — Percentiles Instead of Averages

### Objective

Turn **Percentiles Instead of Averages** into an evidence-based AWS exercise.

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
p50 typical
p95 most users
p99 tail
EOF
```

### Expected Result

Latency SLO and alerts use percentiles appropriate to business need.

### Troubleshooting Path

```text
latency complaint
 ↓ p50/p95/p99
 ↓ route/dependency
 ↓ trace slow requests
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

## Enhanced Lab 6 — Metric Math for Operational Ratios

### Objective

Turn **Metric Math for Operational Ratios** into an evidence-based AWS exercise.

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
error_rate = 100 * errors / requests
backlog_per_worker = queue_depth / max(workers,1)
EOF
```

### Expected Result

Dashboards show ratios that map directly to operations decisions.

### Troubleshooting Path

```text
derived metric wrong
 ↓ period/statistics
 ↓ dimensions
 ↓ missing data
 ↓ zero denominator
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

## Enhanced Lab 7 — Missing Telemetry Semantics

### Objective

Turn **Missing Telemetry Semantics** into an evidence-based AWS exercise.

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
aws cloudwatch describe-alarms --output json 2>/dev/null || true
```

### Expected Result

Heartbeat absence pages; sparse business-event metrics do not create false alerts.

### Troubleshooting Path

```text
INSUFFICIENT_DATA
 ↓ metric emitted?
 ↓ agent/service
 ↓ dimensions/period
 ↓ expected sparse?
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

## Enhanced Lab 8 — Structured Logging Schema

### Objective

Turn **Structured Logging Schema** into an evidence-based AWS exercise.

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
{"level":"ERROR","service":"orders","request_id":"abc","version":"v42","error_code":"DB_TIMEOUT"}
EOF
```

### Expected Result

Logs can be grouped and filtered by fields without fragile parsing.

### Troubleshooting Path

```text
logs hard to query
 ↓ structured?
 ↓ consistent field names?
 ↓ PII/secrets?
 ↓ retention
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

## Enhanced Lab 9 — Log Retention by Data Class

### Objective

Turn **Log Retention by Data Class** into an evidence-based AWS exercise.

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
aws logs describe-log-groups --query 'logGroups[].{Group:logGroupName,Retention:retentionInDays,Bytes:storedBytes}' --output table
```

### Expected Result

Every production log group has an intentional retention period.

### Troubleshooting Path

```text
log cost high
 ↓ largest groups
 ↓ retention
 ↓ verbosity
 ↓ archive requirement
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

## Enhanced Lab 10 — CloudTrail Session Reconstruction

### Objective

Turn **CloudTrail Session Reconstruction** into an evidence-based AWS exercise.

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
aws cloudtrail lookup-events --max-results 20 --output table 2>/dev/null || true
```

### Expected Result

Investigators can map a shared role session back to a human or pipeline.

### Troubleshooting Path

```text
unexpected API
 ↓ event/session
 ↓ source identity
 ↓ source IP/user agent
 ↓ related actions
 ↓ contain
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

## Enhanced Lab 11 — CloudTrail + Config Incident Reconstruction

### Objective

Turn **CloudTrail + Config Incident Reconstruction** into an evidence-based AWS exercise.

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
aws configservice get-resource-config-history --resource-type AWS::EC2::SecurityGroup --resource-id <ID> 2>/dev/null || true
```

### Expected Result

Before/after configuration and actor are attributable.

### Troubleshooting Path

```text
resource changed
 ↓ Config timeline
 ↓ exact time
 ↓ CloudTrail lookup
 ↓ actor/action
 ↓ remediate
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

## Enhanced Lab 12 — EventBridge Retry/DLQ Operations

### Objective

Turn **EventBridge Retry/DLQ Operations** into an evidence-based AWS exercise.

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
aws events list-rules --output table 2>/dev/null || true
aws events list-targets-by-rule --rule <RULE> 2>/dev/null || true
```

### Expected Result

Failed deliveries become visible and recoverable.

### Troubleshooting Path

```text
event missing
 ↓ pattern match
 ↓ target permission
 ↓ target errors/throttling
 ↓ DLQ
 ↓ replay
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

## Enhanced Lab 13 — Automated Remediation Guardrails

### Objective

Turn **Automated Remediation Guardrails** into an evidence-based AWS exercise.

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
AutoRemediate=true
maxConcurrency=1
maxErrors=1
verifyAfter=true
EOF
```

### Expected Result

Automation fixes known issues without touching unrelated resources.

### Troubleshooting Path

```text
automation harmful
 ↓ stop rule
 ↓ scope
 ↓ preconditions
 ↓ rollback
 ↓ review
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

## Enhanced Lab 14 — Session Manager Audit

### Objective

Turn **Session Manager Audit** into an evidence-based AWS exercise.

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
aws ssm describe-instance-information --output table 2>/dev/null || true
```

### Expected Result

Privileged sessions are attributable to federated identities.

### Troubleshooting Path

```text
session unavailable
 ↓ managed-node status
 ↓ IAM
 ↓ endpoints/network
 ↓ session preferences
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

## Enhanced Lab 15 — Run Command Blast Radius

### Objective

Turn **Run Command Blast Radius** into an evidence-based AWS exercise.

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
aws ssm list-command-invocations --details --max-results 20 2>/dev/null || true
```

### Expected Result

A bad command stops before affecting the entire fleet.

### Troubleshooting Path

```text
command failure
 ↓ affected targets
 ↓ command output
 ↓ error threshold
 ↓ stop/correct
 ↓ reconcile
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

## Enhanced Lab 16 — Patch Rings

### Objective

Turn **Patch Rings** into an evidence-based AWS exercise.

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
aws ssm describe-patch-baselines --output table 2>/dev/null || true
```

### Expected Result

Production receives patches only after lower rings pass.

### Troubleshooting Path

```text
patch failure
 ↓ package/kernel
 ↓ reboot/service
 ↓ rollback possible?
 ↓ image replacement/forward fix
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

## Enhanced Lab 17 — Maintenance Window Capacity

### Objective

Turn **Maintenance Window Capacity** into an evidence-based AWS exercise.

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
aws ssm describe-maintenance-windows --output table 2>/dev/null || true
```

### Expected Result

Service remains above minimum capacity throughout maintenance.

### Troubleshooting Path

```text
maintenance outage
 ↓ batch size
 ↓ remaining capacity
 ↓ health
 ↓ rollback deadline
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

## Enhanced Lab 18 — Golden AMI Provenance

### Objective

Turn **Golden AMI Provenance** into an evidence-based AWS exercise.

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
aws ec2 describe-images --owners self --query 'Images[].{ImageId:ImageId,Name:Name,CreationDate:CreationDate}' --output table
```

### Expected Result

Every running instance can be mapped to a known approved image.

### Troubleshooting Path

```text
unknown image
 ↓ instance ImageId
 ↓ AMI metadata
 ↓ build pipeline
 ↓ source/scan
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

## Enhanced Lab 19 — ASG Scaling Activity Diagnosis

### Objective

Turn **ASG Scaling Activity Diagnosis** into an evidence-based AWS exercise.

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
aws autoscaling describe-scaling-activities --auto-scaling-group-name <ASG> --max-items 20 2>/dev/null || true
```

### Expected Result

The exact launch failure is identified before thresholds are changed.

### Troubleshooting Path

```text
ASG not scaling
 ↓ activity message
 ↓ quota/capacity
 ↓ template/AMI
 ↓ subnet IP
 ↓ KMS/IAM
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

## Enhanced Lab 20 — Instance Refresh Safety

### Objective

Turn **Instance Refresh Safety** into an evidence-based AWS exercise.

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
aws autoscaling describe-instance-refreshes --auto-scaling-group-name <ASG> 2>/dev/null || true
```

### Expected Result

A bad AMI stops before healthy capacity is exhausted.

### Troubleshooting Path

```text
refresh stuck
 ↓ launch
 ↓ warmup
 ↓ target health
 ↓ capacity
 ↓ image/config
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

## Enhanced Lab 21 — Container Exit-Code Triage

### Objective

Turn **Container Exit-Code Triage** into an evidence-based AWS exercise.

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
aws ecs list-tasks --cluster <CLUSTER> 2>/dev/null || true
aws ecs describe-tasks --cluster <CLUSTER> --tasks <TASK> 2>/dev/null || true
```

### Expected Result

Exit/stopped evidence points to the right layer.

### Troubleshooting Path

```text
task stopped
 ↓ stoppedReason
 ↓ exit code
 ↓ logs
 ↓ CPU/memory
 ↓ IAM/network/secret
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

## Enhanced Lab 22 — EBS End-to-End Performance

### Objective

Turn **EBS End-to-End Performance** into an evidence-based AWS exercise.

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
iostat -xz 1 5 2>/dev/null || true
aws ec2 describe-volumes --volume-ids <VOL> 2>/dev/null || true
```

### Expected Result

Operators can identify whether bottleneck is volume, instance, or app.

### Troubleshooting Path

```text
disk slow
 ↓ queue/latency
 ↓ volume IOPS/throughput
 ↓ instance limit
 ↓ app pattern
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

## Enhanced Lab 23 — S3 Replication Monitoring

### Objective

Turn **S3 Replication Monitoring** into an evidence-based AWS exercise.

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
aws s3api get-bucket-replication --bucket <BUCKET> 2>/dev/null || true
```

### Expected Result

Replication failures are detected before DR data silently falls behind.

### Troubleshooting Path

```text
replication fail
 ↓ rule
 ↓ object eligible
 ↓ role
 ↓ destination policy
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

## Enhanced Lab 24 — Incomplete Multipart Upload Cleanup

### Objective

Turn **Incomplete Multipart Upload Cleanup** into an evidence-based AWS exercise.

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
aws s3api list-multipart-uploads --bucket <BUCKET> 2>/dev/null || true
```

### Expected Result

Old incomplete uploads do not accumulate.

### Troubleshooting Path

```text
storage unexplained
 ↓ multipart uploads
 ↓ age/client failures
 ↓ lifecycle rule
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

## Enhanced Lab 25 — RDS Wait Analysis

### Objective

Turn **RDS Wait Analysis** into an evidence-based AWS exercise.

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
aws rds describe-db-instances --output table 2>/dev/null || true
aws cloudwatch list-metrics --namespace AWS/RDS 2>/dev/null | head -40
```

### Expected Result

Operators identify the dominant wait before resizing.

### Troubleshooting Path

```text
DB slow
 ↓ load/waits
 ↓ top SQL
 ↓ locks
 ↓ connections
 ↓ storage
 ↓ CPU
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

## Enhanced Lab 26 — DynamoDB Throttle vs Hot Key

### Objective

Turn **DynamoDB Throttle vs Hot Key** into an evidence-based AWS exercise.

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
aws cloudwatch list-metrics --namespace AWS/DynamoDB 2>/dev/null | head -60
```

### Expected Result

Aggregate capacity and partition-distribution failures are distinguished.

### Troubleshooting Path

```text
throttle
 ↓ capacity mode
 ↓ consumed/throttled
 ↓ key distribution
 ↓ GSI
 ↓ redesign
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

## Enhanced Lab 27 — ALB 5xx Ownership

### Objective

Turn **ALB 5xx Ownership** into an evidence-based AWS exercise.

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
aws cloudwatch list-metrics --namespace AWS/ApplicationELB 2>/dev/null | head -60
aws elbv2 describe-target-health --target-group-arn <TG> 2>/dev/null || true
```

### Expected Result

Incident triage identifies the component generating errors.

### Troubleshooting Path

```text
ALB 5xx
 ↓ ELB vs Target 5xx
 ↓ target health
 ↓ app logs
 ↓ timeout/reset/dependency
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

## Enhanced Lab 28 — NAT Connection Capacity

### Objective

Turn **NAT Connection Capacity** into an evidence-based AWS exercise.

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
aws cloudwatch list-metrics --namespace AWS/NATGateway 2>/dev/null | head -50
```

### Expected Result

NAT capacity is observable for high-scale egress workloads.

### Troubleshooting Path

```text
egress intermittent
 ↓ NAT metrics
 ↓ connection count
 ↓ destination concentration
 ↓ pooling/additional egress design
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

## Enhanced Lab 29 — Flow Logs Limitations

### Objective

Turn **Flow Logs Limitations** into an evidence-based AWS exercise.

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
aws ec2 describe-flow-logs --output table 2>/dev/null || true
```

### Expected Result

Operators escalate to application/TLS evidence when flow is accepted.

### Troubleshooting Path

```text
connection fails
 ↓ flow ACCEPT/REJECT
 ↓ if REJECT → network policy
 ↓ if ACCEPT → transport/TLS/app
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

## Enhanced Lab 30 — Restore Testing and RTO

### Objective

Turn **Restore Testing and RTO** into an evidence-based AWS exercise.

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

Restore drills prove recovery points are usable.

### Troubleshooting Path

```text
restore fail
 ↓ recovery point
 ↓ KMS/IAM
 ↓ network
 ↓ app validation
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

## Enhanced Lab 31 — PITR for Logical Corruption

### Objective

Turn **PITR for Logical Corruption** into an evidence-based AWS exercise.

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
aws dynamodb describe-continuous-backups --table-name <TABLE> 2>/dev/null || true
```

### Expected Result

Runbooks distinguish infrastructure outage from logical-data corruption.

### Troubleshooting Path

```text
logical corruption
 ↓ stop bad writer
 ↓ identify timestamp
 ↓ restore PITR
 ↓ validate
 ↓ reconcile newer valid data
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

## Enhanced Lab 32 — CloudFormation Drift Ownership

### Objective

Turn **CloudFormation Drift Ownership** into an evidence-based AWS exercise.

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
aws cloudformation detect-stack-drift --stack-name <STACK> 2>/dev/null || true
```

### Expected Result

Drift is corrected in the authoritative source or ownership is intentionally changed.

### Troubleshooting Path

```text
drift
 ↓ who changed?
 ↓ CloudTrail
 ↓ resource owner/tool
 ↓ reconcile/import
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

## Enhanced Lab 33 — StackSets Progressive Rollout

### Objective

Turn **StackSets Progressive Rollout** into an evidence-based AWS exercise.

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
aws cloudformation list-stack-sets --status ACTIVE 2>/dev/null || true
```

### Expected Result

A bad baseline stops before organization-wide impact.

### Troubleshooting Path

```text
StackSet failure
 ↓ account/Region
 ↓ operation result
 ↓ failure tolerance
 ↓ stop/fix/retry
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

## Enhanced Lab 34 — IAM AccessDenied Ladder

### Objective

Turn **IAM AccessDenied Ladder** into an evidence-based AWS exercise.

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
aws sts get-caller-identity
aws iam simulate-principal-policy --policy-source-arn <ARN> --action-names <ACTION> 2>/dev/null || true
```

### Expected Result

The denying layer is identified before permissions are broadened.

### Troubleshooting Path

```text
AccessDenied
 ↓ caller/action/resource
 ↓ IAM
 ↓ boundary/session
 ↓ SCP
 ↓ resource/KMS/endpoint
 ↓ conditions
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

## Enhanced Lab 35 — Credential Compromise Containment

### Objective

Turn **Credential Compromise Containment** into an evidence-based AWS exercise.

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
aws cloudtrail lookup-events --max-results 50 2>/dev/null || true
```

### Expected Result

Compromised credentials stop working and impact is bounded.

### Troubleshooting Path

```text
credential incident
 ↓ principal/session
 ↓ revoke
 ↓ API timeline
 ↓ affected resources
 ↓ rotate
 ↓ validate
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

## Enhanced Lab 36 — KMS Dependency Inventory

### Objective

Turn **KMS Dependency Inventory** into an evidence-based AWS exercise.

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
```

### Expected Result

Key changes are reviewed with a known blast radius.

### Troubleshooting Path

```text
KMS change
 ↓ dependent resources
 ↓ backups/DR
 ↓ migrate/re-encrypt
 ↓ disable before delete
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

## Enhanced Lab 37 — Cost Anomaly as Incident Signal

### Objective

Turn **Cost Anomaly as Incident Signal** into an evidence-based AWS exercise.

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
aws ce get-cost-and-usage --time-period Start=2026-08-01,End=2026-08-20 --granularity DAILY --metrics UnblendedCost 2>/dev/null || true
```

### Expected Result

Cost changes are correlated with deployments, traffic, and usage type.

### Troubleshooting Path

```text
bill spike
 ↓ account/service
 ↓ usage type
 ↓ tag/resource
 ↓ deployment/traffic
 ↓ root cause
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

## Enhanced Lab 38 — Incident Command Roles

### Objective

Turn **Incident Command Roles** into an evidence-based AWS exercise.

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
IC:
Ops:
Comms:
Scribe:
Impact:
Current mitigation:
Next update:
EOF
```

### Expected Result

Responders know who decides, who troubleshoots, and who communicates.

### Troubleshooting Path

```text
incident chaotic
 ↓ assign IC
 ↓ define objective
 ↓ parallel workstreams
 ↓ update cadence
 ↓ decision log
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

## Enhanced Lab 39 — Mitigation Before Root Cause

### Objective

Turn **Mitigation Before Root Cause** into an evidence-based AWS exercise.

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
Mitigation: shift traffic to healthy Region.
Root-cause analysis continues after service stabilizes.
EOF
```

### Expected Result

MTTR is reduced without losing diagnostic evidence.

### Troubleshooting Path

```text
outage ongoing
 ↓ safe mitigation?
 ↓ execute/verify
 ↓ preserve logs
 ↓ root cause later
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

## Enhanced Lab 40 — Post-Incident Action Quality

### Objective

Turn **Post-Incident Action Quality** into an evidence-based AWS exercise.

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
Bad: Be more careful.
Good: CI policy blocks public RDS endpoints; owner=platform; due=2026-09-15.
EOF
```

### Expected Result

Follow-up items measurably reduce recurrence or impact.

### Troubleshooting Path

```text
same incident repeats
 ↓ old actions
 ↓ systemic?
 ↓ completed?
 ↓ verified effective?
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

## Enhanced Lab 41 — Operational Readiness Review

### Objective

Turn **Operational Readiness Review** into an evidence-based AWS exercise.

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
[ ] SLO
[ ] dashboard
[ ] paging
[ ] runbook
[ ] backup restore test
[ ] quota
[ ] rollback
[ ] owner/on-call
EOF
```

### Expected Result

Production launch has explicit operations acceptance.

### Troubleshooting Path

```text
service not supportable
 ↓ missing ORR item
 ↓ assign owner
 ↓ close gap
 ↓ re-review
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

## Enhanced Lab 42 — Runbook Stop Conditions

### Objective

Turn **Runbook Stop Conditions** into an evidence-based AWS exercise.

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
Stop if:
- >1 production host fails
- backup not current
- customer errors increase
EOF
```

### Expected Result

Operators know when not to continue a dangerous procedure.

### Troubleshooting Path

```text
runbook harmful
 ↓ scope?
 ↓ preconditions?
 ↓ stop condition?
 ↓ verification?
 ↓ update/test
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

## Enhanced Lab 43 — Multi-Region Readiness

### Objective

Turn **Multi-Region Readiness** into an evidence-based AWS exercise.

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
aws ec2 describe-regions --output table 2>/dev/null || true
```

### Expected Result

Operations can prove DR Region is ready before disaster.

### Troubleshooting Path

```text
DR not ready
 ↓ app version
 ↓ data lag
 ↓ quota
 ↓ keys/secrets
 ↓ routing
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

## Enhanced Lab 44 — Failback Procedure

### Objective

Turn **Failback Procedure** into an evidence-based AWS exercise.

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
Failback prerequisites:
single write owner
data sync complete
version parity
capacity healthy
rollback path
EOF
```

### Expected Result

Failback preserves all data created during the disaster interval.

### Troubleshooting Path

```text
failback risk
 ↓ current writer
 ↓ data delta
 ↓ resync
 ↓ validate
 ↓ traffic shift
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

## Enhanced Lab 45 — Capacity Forecasting

### Objective

Turn **Capacity Forecasting** into an evidence-based AWS exercise.

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
Forecast:
peak RPS
DB growth GB/day
subnet free IP
SQS peak depth
monthly egress
EOF
```

### Expected Result

Teams act before hard limits are reached.

### Troubleshooting Path

```text
capacity surprise
 ↓ missing leading metric
 ↓ trend
 ↓ hard limit
 ↓ forecast horizon
 ↓ action
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

## Enhanced Lab 46 — Evidence Chain for Operations

### Objective

Turn **Evidence Chain for Operations** into an evidence-based AWS exercise.

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
aws cloudtrail lookup-events --max-results 10 2>/dev/null || true
aws cloudwatch describe-alarms --state-value ALARM --output table 2>/dev/null || true
```

### Expected Result

Incidents and changes can be reconstructed from durable evidence.

### Troubleshooting Path

```text
missing evidence
 ↓ which link absent?
 ↓ logging/deploy metadata
 ↓ correlation/run IDs
 ↓ retention
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

### Lab 1 — Current CloudOps Exam Mapping

Create a table:

```text
Domain 1 22%
Domain 2 22%
Domain 3 22%
Domain 4 16%
Domain 5 18%
```

Map every lab in this course to at least one domain.

### Lab 2 — CloudWatch Metrics Baseline

Choose one EC2 instance.

Record:

```text
CPUUtilization
NetworkIn
NetworkOut
StatusCheckFailed
```

Explain what each metric can and cannot prove.

### Lab 3 — Install CloudWatch Agent

On a disposable EC2 instance, configure collection for:

```text
memory
disk usage
/var/log/messages or syslog
application log
```

Verify data appears centrally.

### Lab 4 — Create an Alarm

Create an alarm:

```text
CPU > 80%
for 3 evaluation periods
```

Send to a lab SNS topic.

Test and clean up.

### Lab 5 — Composite Alarm Design

Create conceptual alarms:

```text
HighLatency
High5xx
```

Then:

```text
ServiceImpact = HighLatency AND High5xx
```

Explain noise reduction.

### Lab 6 — Logs Insights

Run a query against lab logs:

```text
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 50
```

Document the operational question answered.

### Lab 7 — Metric Filter

Create a metric from a test log line:

```text
"PAYMENT_FAILED"
```

Build an alarm on the derived metric.

### Lab 8 — CloudTrail Investigation

Find a recent lab API action.

Record:

```text
eventTime
eventName
userIdentity
sourceIPAddress
resources
```

### Lab 9 — AWS Config Tabletop

Define five compliance rules:

```text
S3 public access blocked
EBS encrypted
approved instance types
required tags
CloudTrail enabled
```

### Lab 10 — EventBridge Remediation

Design:

```text
EC2 stops
 ↓
EventBridge
 ↓
SNS
```

Then extend conceptually to an SSM Automation action.

### Lab 11 — Session Manager

Connect to a private EC2 instance using Session Manager.

Requirements:

```text
no public IP
no inbound SSH
SSM role
SSM connectivity
```

### Lab 12 — Run Command

Run a safe read-only command across tagged lab instances:

```text
uname -a
df -h
```

Limit concurrency.

### Lab 13 — Patch Ring Design

Create:

```text
Ring 0 Dev
Ring 1 Staging
Ring 2 Production Canary
Ring 3 Production Fleet
```

Define maintenance windows and rollback criteria.

### Lab 14 — SSM Automation Runbook

Design a runbook:

```text
create EBS snapshot
restart application
health check
if failed → restore/escalate
```

### Lab 15 — AMI Pipeline

Design:

```text
base AMI
 ↓
Image Builder
 ↓
patch
 ↓
agents
 ↓
tests
 ↓
golden AMI
 ↓
ASG instance refresh
```

### Lab 16 — Auto Scaling Troubleshooting

Create ten failure scenarios:

```text
subnet IP exhaustion
quota
bad AMI
bad user data
KMS denied
capacity unavailable
health check fail
```

Write evidence and fix.

### Lab 17 — ECS Task Failure Tabletop

Diagnose:

```text
CannotPullContainerError
task exits 137
health check fail
secret denied
```

### Lab 18 — EBS Performance Review

Given fictional metrics:

```text
IOPS high
queue growing
latency rising
EC2 bandwidth maxed
```

identify whether the bottleneck is volume or instance.

### Lab 19 — S3 Lifecycle

Design rules for:

```text
logs
backup
application files
incomplete multipart uploads
old versions
```

### Lab 20 — EFS/FSx Selection

Select storage and operations metrics for:

```text
Linux web share
Windows share
HPC
ONTAP migration
```

### Lab 21 — RDS Performance Investigation

Use CloudWatch/Performance Insights conceptually to investigate:

```text
CPU 35%
DB load high
connections high
latency rising
```

Explain why CPU alone is insufficient.

### Lab 22 — DynamoDB Throttling

Given:

```text
high throttles
one partition key receives 80% writes
```

identify hot partition and propose redesign.

### Lab 23 — ELB Health Troubleshooting

Break a health path intentionally in a lab.

Trace:

```text
ALB
SG
target
port
application
health response
```

### Lab 24 — Route 53 Failover Tabletop

Design:

```text
Primary Region
Secondary Region
health check
failover record
```

Specify TTL and recovery validation.

### Lab 25 — AWS Backup Plan

Create a plan for:

```text
daily 35d
monthly 12m
cross-account
cross-Region
```

using a fictional compliance requirement.

### Lab 26 — Restore Test

Restore one disposable recovery point.

Measure:

```text
start time
available time
application validation time
```

Compare with RTO.

### Lab 27 — CloudFormation Change Set

Create a simple lab stack.

Modify a tag or low-risk property.

Generate a change set and inspect before execution.

### Lab 28 — CloudFormation Failure

Create a controlled template error.

Read stack Events.

Record:

```text
failed resource
status reason
rollback
```

### Lab 29 — StackSets Architecture

Design organization-wide deployment of:

```text
CloudWatch role
security baseline
Config resource
```

to multiple accounts/Regions.

### Lab 30 — IAM Denied Troubleshooting

Create five scenarios involving:

```text
IAM deny
SCP
resource policy
KMS policy
permission boundary
```

For each identify evidence.

### Lab 31 — Security Finding Workflow

Design:

```text
GuardDuty
 ↓
Security Hub
 ↓
EventBridge
 ↓
SNS/automation
 ↓
Ops ticket
```

### Lab 32 — NAT Failure

Trace a private EC2 Internet outage:

```text
route
NAT
public subnet
IGW
NACL
SG
DNS
```

### Lab 33 — VPC Endpoint

Move S3 traffic from:

```text
Private EC2 → NAT → S3
```

to:

```text
Private EC2 → Gateway Endpoint → S3
```

Explain security and cost impact.

### Lab 34 — Flow Logs Investigation

Given accepted/rejected entries, determine:

```text
source
destination
port
action
```

and identify likely layer.

### Lab 35 — Cost Incident

Monthly cost doubles.

Investigate conceptually:

```text
Cost Explorer
service
Region
usage type
tag
time
```

Create root-cause hypotheses.

### Lab 36 — CloudOps Game Day

Simulate:

```text
EC2 failure
AZ failure
RDS failover
SQS backlog
IAM lockout
NAT outage
CloudFront stale cache
```

For each:

```text
Detection
Evidence
Mitigation
Recovery
Automation Opportunity
```

---

## 6. Mini Project

# Mini Project — AWS CloudOps Operating Platform

Operate a production-style environment:

```text
Organizations
├─ Security
├─ Log Archive
├─ Network
├─ Production
└─ NonProduction
```

Workload:

```text
Route 53
 ↓
CloudFront
 ↓
ALB
 ↓
Auto Scaling EC2 / ECS
 ↓
RDS
 ↓
S3
```

Required operational components:

```text
CloudWatch dashboards
CloudWatch alarms
CloudWatch Agent
CloudTrail
AWS Config
VPC Flow Logs
Systems Manager
AWS Backup
Security Hub
GuardDuty
Inspector
Cost Explorer/Budgets
```

Required automation:

```text
EventBridge
Systems Manager Automation
Lambda where justified
CloudFormation
StackSets concept
```

Required runbooks:

```text
RUNBOOK_EC2_UNHEALTHY.md
RUNBOOK_ASG_LAUNCH_FAILURE.md
RUNBOOK_ALB_5XX.md
RUNBOOK_RDS_PERFORMANCE.md
RUNBOOK_RDS_FAILOVER.md
RUNBOOK_S3_ACCESS_DENIED.md
RUNBOOK_IAM_DENIED.md
RUNBOOK_NAT_FAILURE.md
RUNBOOK_SUBNET_EXHAUSTION.md
RUNBOOK_BACKUP_RESTORE.md
RUNBOOK_COST_SPIKE.md
RUNBOOK_SECURITY_FINDING.md
RUNBOOK_REGION_INCIDENT.md
```

Required dashboards:

```text
Service Health
Application Performance
Database
Network
Backup
Security
Cost
```

Required operational KPIs:

```text
availability
MTTD
MTTR
error rate
latency
backup success
restore success
patch compliance
security findings age
cost variance
automation coverage
```

---

## 7. Recommended Resources

This Markdown is self-contained for the course.

For current implementation details, use official AWS documentation:

```text
AWS Certified CloudOps Engineer – Associate SOA-C03 Exam Guide
Amazon CloudWatch
AWS CloudTrail
AWS Config
AWS Systems Manager
Amazon EC2
Amazon ECS
Amazon EKS
AWS Backup
AWS CloudFormation
AWS IAM
AWS KMS
AWS Security Hub
Amazon GuardDuty
Amazon VPC
Amazon Route 53
Amazon CloudFront
AWS Cost Management
```

Use CLI help for exact syntax:

```bash
aws cloudwatch help
aws logs help
aws ssm help
aws backup help
aws cloudformation help
```

---

## 8. Certification Relevance

Roadmap course name:

```text
AWS SysOps Administration
```

Current certification:

```text
AWS Certified CloudOps Engineer – Associate
SOA-C03
```

Current domain weights:

```text
Monitoring / Logging / Analysis / Remediation / Performance 22%
Reliability / Business Continuity                           22%
Deployment / Provisioning / Automation                      22%
Security / Compliance                                       16%
Networking / Content Delivery                               18%
```

Current exam format:

```text
130 minutes
65 questions
50 scored
15 unscored
720 passing scaled score
```

This course prepares for:

```text
AWS CloudOps roles
AWS DevOps Engineer – Professional
AWS Security
Terraform
CI/CD
DevSecOps
SRE
Platform Engineering
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Alarm on every metric spike.  
  **Best practice:** alert on actionable service-impact conditions.

- **Mistake:** Use CPU as the only health signal.  
  **Best practice:** combine traffic, errors, latency, saturation, and business metrics.

- **Mistake:** Keep logs indefinitely by default.  
  **Best practice:** explicit retention by use case.

- **Mistake:** Public SSH for every instance.  
  **Best practice:** Session Manager/private administration where suitable.

- **Mistake:** Fleet-wide Run Command immediately.  
  **Best practice:** canary, concurrency limits, error thresholds.

- **Mistake:** Patch production first.  
  **Best practice:** patch rings.

- **Mistake:** Repeatedly increase resources without root-cause analysis.  
  **Best practice:** metrics + performance analysis.

- **Mistake:** Backup exists, therefore recovery works.  
  **Best practice:** restore testing.

- **Mistake:** Manual console edits outside CloudFormation.  
  **Best practice:** IaC and drift control.

- **Mistake:** Grant admin to fix AccessDenied.  
  **Best practice:** inspect the full permission-evaluation path.

- **Mistake:** Treat GuardDuty finding as proof of compromise.  
  **Best practice:** investigate context and evidence.

- **Mistake:** Ignore NAT/network transfer cost.  
  **Best practice:** endpoints/topology/cost analysis.

- **Mistake:** Incident resolved means work finished.  
  **Best practice:** post-incident review and preventive actions.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What replaced AWS Certified SysOps Administrator – Associate?

**Answer:** AWS Certified CloudOps Engineer – Associate, SOA-C03.

### Q2. Current exam duration?

**Answer:** 130 minutes.

### Q3. Current question count?

**Answer:** 65.

### Q4. Passing score?

**Answer:** 720 scaled score.

### Q5. Domain 1 weight?

**Answer:** 22%.

### Q6. CloudWatch vs CloudTrail?

**Answer:** Operational telemetry vs AWS API/audit activity.

### Q7. Config?

**Answer:** Resource configuration history and compliance evaluation.

### Q8. Logs Insights?

**Answer:** Query CloudWatch log data interactively.

### Q9. Composite alarm?

**Answer:** Alarm based on states of multiple other alarms.

### Q10. Systems Manager Session Manager?

**Answer:** IAM-controlled interactive access to managed nodes without normal inbound SSH/RDP exposure.

### Q11. Run Command?

**Answer:** Execute commands remotely across Systems Manager managed nodes.

### Q12. Patch Manager?

**Answer:** Automates patching/compliance for supported systems.

### Q13. Automation runbook?

**Answer:** Multi-step Systems Manager automation procedure.

### Q14. EC2 Image Builder?

**Answer:** Automated AMI/container image pipeline service.

### Q15. Instance Refresh?

**Answer:** Controlled replacement/update of ASG instances from new configuration.

### Q16. RDS Performance Insights?

**Answer:** Database load/wait/SQL performance analysis capability.

### Q17. AWS Backup?

**Answer:** Central backup policy and recovery management for supported AWS services.

### Q18. StackSets?

**Answer:** Deploy CloudFormation stacks across multiple accounts and Regions.

### Q19. IAM Access Analyzer?

**Answer:** Helps analyze resource access and unintended external/cross-account access.

### Q20. VPC Flow Logs?

**Answer:** Metadata records about IP flows, including ACCEPT/REJECT.

### Q21. Gateway endpoint?

**Answer:** Private VPC routing endpoint for S3/DynamoDB.

### Q22. CloudFront stale content first checks?

**Answer:** TTL, cache headers/key, invalidation, origin version.

### Q23. MTTD?

**Answer:** Mean Time To Detect.

### Q24. MTTR?

**Answer:** Mean Time To Restore/Recover/Resolve depending on organization definition.

### Q25. Core CloudOps loop?

**Answer:** Monitor → detect → investigate → remediate → verify → automate → improve.

---

# Expanded Self-Assessment Bank — AWS SysOps Administration / CloudOps Engineering

### Q1. What is the key lesson from **Service Ownership and Operational Catalog**?
**Answer:** Make service ownership mandatory production metadata.

### Q2. What is the key lesson from **SLI/SLO/Error Budget**?
**Answer:** Define SLI math and error-budget policy before incidents.

### Q3. What is the key lesson from **Burn-Rate Alerting**?
**Answer:** Page on user-impact burn; use component alarms for diagnosis.

### Q4. What is the key lesson from **Golden Signals Dashboard**?
**Answer:** Lead dashboards with service/user signals.

### Q5. What is the key lesson from **Percentiles Instead of Averages**?
**Answer:** Do not use only average latency for interactive services.

### Q6. What is the key lesson from **Metric Math for Operational Ratios**?
**Answer:** Use metric math to encode operational meaning.

### Q7. What is the key lesson from **Missing Telemetry Semantics**?
**Answer:** Define missing-data meaning for every critical alarm.

### Q8. What is the key lesson from **Structured Logging Schema**?
**Answer:** Define a logging schema and prohibit secret values in logs.

### Q9. What is the key lesson from **Log Retention by Data Class**?
**Answer:** Set retention explicitly; never-expire should be rare and justified.

### Q10. What is the key lesson from **CloudTrail Session Reconstruction**?
**Answer:** Preserve source identity in federation and automation sessions.

### Q11. What is the key lesson from **CloudTrail + Config Incident Reconstruction**?
**Answer:** Use Config and CloudTrail together.

### Q12. What is the key lesson from **EventBridge Retry/DLQ Operations**?
**Answer:** Every automation event path needs explicit failure handling.

### Q13. What is the key lesson from **Automated Remediation Guardrails**?
**Answer:** Automate only well-understood failure modes with bounded blast radius.

### Q14. What is the key lesson from **Session Manager Audit**?
**Answer:** Use identity-aware administration and protect session logs.

### Q15. What is the key lesson from **Run Command Blast Radius**?
**Answer:** Treat remote execution like production change.

### Q16. What is the key lesson from **Patch Rings**?
**Answer:** Use patch rings and know the recovery path before approval.

### Q17. What is the key lesson from **Maintenance Window Capacity**?
**Answer:** Calculate maintenance concurrency from surviving capacity.

### Q18. What is the key lesson from **Golden AMI Provenance**?
**Answer:** Tag images with provenance and retire obsolete versions.

### Q19. What is the key lesson from **ASG Scaling Activity Diagnosis**?
**Answer:** Read scaling activity evidence first.

### Q20. What is the key lesson from **Instance Refresh Safety**?
**Answer:** Gate refresh on workload readiness.

### Q21. What is the key lesson from **Container Exit-Code Triage**?
**Answer:** Start from task/container termination evidence.

### Q22. What is the key lesson from **EBS End-to-End Performance**?
**Answer:** Check the whole I/O path before resizing.

### Q23. What is the key lesson from **S3 Replication Monitoring**?
**Answer:** Alert on replication health when it is a recovery control.

### Q24. What is the key lesson from **Incomplete Multipart Upload Cleanup**?
**Answer:** Add multipart cleanup to large-upload buckets.

### Q25. What is the key lesson from **RDS Wait Analysis**?
**Answer:** Use database-native load evidence before scaling.

### Q26. What is the key lesson from **DynamoDB Throttle vs Hot Key**?
**Answer:** Treat hot-key failures as data-model problems.

### Q27. What is the key lesson from **ALB 5xx Ownership**?
**Answer:** Separate front-door, target, and dependency errors.

### Q28. What is the key lesson from **NAT Connection Capacity**?
**Answer:** Monitor NAT for high fan-out egress patterns.

### Q29. What is the key lesson from **Flow Logs Limitations**?
**Answer:** Use the lowest evidence layer that can answer the question.

### Q30. What is the key lesson from **Restore Testing and RTO**?
**Answer:** Track restore success and restore time as KPIs.

### Q31. What is the key lesson from **PITR for Logical Corruption**?
**Answer:** Design for logical corruption, not only hardware failure.

### Q32. What is the key lesson from **CloudFormation Drift Ownership**?
**Answer:** Give each resource one authoritative writer.

### Q33. What is the key lesson from **StackSets Progressive Rollout**?
**Answer:** Treat multi-account deployment like progressive release.

### Q34. What is the key lesson from **IAM AccessDenied Ladder**?
**Answer:** Never use admin access as the first troubleshooting step.

### Q35. What is the key lesson from **Credential Compromise Containment**?
**Answer:** Contain first, then eradicate root cause.

### Q36. What is the key lesson from **KMS Dependency Inventory**?
**Answer:** Never delete a key without dependency evidence.

### Q37. What is the key lesson from **Cost Anomaly as Incident Signal**?
**Answer:** Treat cost anomalies as possible system-health signals.

### Q38. What is the key lesson from **Incident Command Roles**?
**Answer:** Separate incident coordination from hands-on debugging.

### Q39. What is the key lesson from **Mitigation Before Root Cause**?
**Answer:** Restore service first when a safe mitigation exists.

### Q40. What is the key lesson from **Post-Incident Action Quality**?
**Answer:** Write actions that modify the system, not human intention.

### Q41. What is the key lesson from **Operational Readiness Review**?
**Answer:** Make operational readiness a launch gate.

### Q42. What is the key lesson from **Runbook Stop Conditions**?
**Answer:** Write stop conditions as carefully as commands.

### Q43. What is the key lesson from **Multi-Region Readiness**?
**Answer:** Continuously monitor standby readiness.

### Q44. What is the key lesson from **Failback Procedure**?
**Answer:** Design and test failback separately.

### Q45. What is the key lesson from **Capacity Forecasting**?
**Answer:** Monitor headroom and growth rate, not only current utilization.

### Q46. What is the key lesson from **Evidence Chain for Operations**?
**Answer:** Design intent, execution, and outcome to be auditable.


## Completion Checklist

- [ ] I understand the SysOps → CloudOps certification transition.
- [ ] I understand SOA-C03 domains.
- [ ] I can operate CloudWatch metrics/alarms/logs.
- [ ] I understand CloudTrail/Config.
- [ ] I can query logs.
- [ ] I understand EventBridge/SNS operations.
- [ ] I can use Systems Manager concepts.
- [ ] I understand Session Manager and Run Command.
- [ ] I understand patching and maintenance windows.
- [ ] I understand Automation runbooks.
- [ ] I can operate EC2/ASG/images.
- [ ] I understand container operations.
- [ ] I can analyze EBS/S3/EFS/FSx performance.
- [ ] I can analyze RDS/DynamoDB.
- [ ] I understand ELB/Route 53 operational health.
- [ ] I understand AWS Backup and restore.
- [ ] I understand DR operational procedures.
- [ ] I understand CloudFormation/StackSets/RAM/CDK.
- [ ] I understand IAM troubleshooting.
- [ ] I understand security/compliance operations.
- [ ] I can troubleshoot VPC networking.
- [ ] I understand Flow Logs and network logs.
- [ ] I understand cost operations.
- [ ] I can run a structured incident process.
- [ ] I completed all 36 labs.
- [ ] I completed the AWS CloudOps Operating Platform project.
