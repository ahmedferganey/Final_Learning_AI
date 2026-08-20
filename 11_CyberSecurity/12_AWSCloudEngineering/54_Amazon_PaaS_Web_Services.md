# 54. Amazon PaaS Web Services

> Phase 12 — AWS Cloud Engineering

This course focuses on **managed AWS application platforms and web-service building blocks**.

The main question is no longer:

```text
How do I create a VM?
```

It becomes:

```text
How much infrastructure do I actually need to manage?
```

AWS offers several levels of abstraction:

```text
More Infrastructure Control
        |
        v
Amazon EC2
        |
Elastic Beanstalk
        |
ECS / EKS on EC2
        |
ECS / EKS on Fargate
        |
AWS App Runner
        |
AWS Lambda
        |
More Managed / Serverless
```

These services are not interchangeable. The correct platform depends on:

```text
application type
runtime
container requirement
request model
execution duration
scaling model
networking
deployment control
operational skill
cost
portability
```

Current AWS documentation describes:

- **Elastic Beanstalk** as a managed application deployment service that provisions EC2, load balancing, health monitoring, and scaling around your code.
- **AWS App Runner** as a managed service that deploys source code or container images directly to scalable web applications.
- **AWS Fargate** as serverless compute for containers used with ECS and EKS.
- **AWS Lambda** as serverless event-driven compute; AWS's current decision guidance characterizes Lambda as suited to short-lived event-driven work and documents a maximum execution duration of 15 minutes.

This course teaches the complete application platform around these compute choices:

```text
DNS
CDN
WAF
API Gateway
AppSync
Application Platform
Queues / Events
Databases
Secrets
Observability
Deployment
Security
Cost
```

---

# Application Platform Mental Model

```text
                         Users
                           |
                       Route 53
                           |
                      CloudFront
                           |
                         AWS WAF
                           |
                    API / Web Entry
                +----------+----------+
                |                     |
          API Gateway               ALB
                |                     |
             Lambda          App Runner / ECS
                |                     |
                +----------+----------+
                           |
                   Application Services
                 /         |          \
              SQS      EventBridge    SNS
                 \         |          /
                           |
                  Database / Storage
                 RDS / DynamoDB / S3
                           |
                 Secrets / Monitoring
```

The core platform-selection decision:

```text
Source Code
   |
   +-- traditional web app?
   |      → Elastic Beanstalk / App Runner
   |
   +-- container?
   |      → App Runner / ECS / EKS / Fargate
   |
   +-- event-driven short task?
   |      → Lambda
   |
   +-- Kubernetes requirement?
   |      → EKS
   |
   +-- maximum OS control?
          → EC2
```

---

## 1. Topic Title

**Amazon PaaS Web Services**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain PaaS, CaaS, serverless containers, and FaaS in AWS.
- Compare EC2, Elastic Beanstalk, App Runner, ECS, EKS, Fargate, and Lambda.
- Select the appropriate AWS application platform from requirements.
- Explain Elastic Beanstalk applications, versions, environments, platforms, web environments, worker environments, deployment policies, configuration, scaling, health, and extensions.
- Explain App Runner source/image services, builds, deployments, autoscaling, health checks, instance roles, VPC connectivity, and observability.
- Explain ECS clusters, task definitions, tasks, services, launch/capacity models, Fargate, load balancing, service discovery, secrets, and deployment.
- Explain EKS at a platform-selection level and know when Kubernetes is justified.
- Explain Lambda functions, runtimes, handlers, layers, versions, aliases, concurrency, event sources, retries, DLQs/destinations, VPC access, environment variables, layers, and observability.
- Explain API Gateway HTTP, REST, and WebSocket API concepts.
- Explain API authentication/authorization and throttling.
- Explain AWS AppSync and GraphQL at a fundamentals level.
- Explain CloudFront, Route 53, WAF, ACM, and load-balancer integration for web platforms.
- Explain SQS, SNS, EventBridge, and Step Functions for application integration.
- Explain asynchronous web architecture.
- Explain RDS, DynamoDB, ElastiCache, S3, EFS, and secrets as application dependencies.
- Explain IAM execution/task/instance roles and workload identity.
- Explain KMS, Secrets Manager, Parameter Store, and ACM for application security.
- Explain CloudWatch, logs, traces, metrics, alarms, and application health.
- Explain rolling, immutable, blue/green, canary, and weighted deployments.
- Explain Route 53 and Lambda alias weighted deployments conceptually.
- Explain application configuration and twelve-factor concepts.
- Explain statelessness, session management, caching, and object storage.
- Explain CI/CD integration concepts.
- Explain CloudFormation/CDK/IaC integration.
- Explain platform cost models and scale-to-zero/idle-cost tradeoffs.
- Troubleshoot common application-platform failures.
- Build a complete production managed web platform.

---

## 3. Prerequisites

Required:

- 49. AWS Cloud Practitioner
- 52. AWS Solutions Architect – Associate
- 53. AWS SysOps Administration / CloudOps
- backend/web fundamentals
- REST APIs
- Linux basics
- containers fundamentals
- databases
- networking
- Git

Useful local tools:

```text
Git
Docker
AWS CLI
Python / Node.js
curl
jq
```

Use a sandbox AWS account and budgets.

---

## 4. Core Concepts Explanation

# Part 1 — What PaaS Means

Platform as a Service removes much of:

```text
OS provisioning
runtime installation
load-balancer plumbing
scaling infrastructure
platform patching
```

so the team focuses on application code/configuration.

AWS has several services with PaaS-like characteristics rather than one universal "PaaS" product.

# Part 2 — Application Abstraction Spectrum

```text
EC2
→ manage OS

Elastic Beanstalk
→ AWS manages application environment around EC2

ECS/EKS
→ manage container orchestration model

Fargate
→ no worker-node management

App Runner
→ source/image to managed web service

Lambda
→ event-driven function
```

Higher abstraction usually reduces control and operations.

# Part 3 — PaaS vs Serverless

PaaS can still maintain provisioned application capacity.

Serverless emphasizes:

```text
no server provisioning
automatic infrastructure management
fine-grained scaling
usage-oriented billing
```

The boundary is not always absolute.

# Part 4 — CaaS

Container as a Service focuses on deploying containers.

AWS examples:

```text
ECS
EKS
Fargate
App Runner
```

They differ in orchestration/control.

# Part 5 — FaaS

Function as a Service:

```text
event
 ↓
function
 ↓
short execution
```

AWS Lambda is the main AWS FaaS example.

# Part 6 — Platform Selection Questions

Ask:

```text
Source or container?
Long-running?
Event-driven?
Kubernetes required?
Need OS access?
Need custom network?
Scale to zero?
Long background jobs?
Team expertise?
```

# Part 7 — Operational Overhead

Relative conceptual overhead:

```text
EC2           high
EKS           high-medium
ECS/EC2       medium
Fargate       medium-low
Beanstalk     medium-low
App Runner    low
Lambda        low
```

Actual complexity depends on application.

# Part 8 — Portability

Containers improve packaging portability, but application dependence on:

```text
IAM
DynamoDB
EventBridge
SQS
Lambda
API Gateway
```

still creates platform coupling.

Portability is an architecture decision, not just a container decision.

# Part 9 — Stateless Web Applications

Best managed-platform web apps externalize state.

```text
Web instance
  |
  +-- session → cache/database
  +-- files → S3/EFS
  +-- data → database
```

Then instances can be replaced safely.

# Part 10 — Twelve-Factor Influence

Useful practices:

```text
config in environment/secret service
stateless processes
logs as streams
disposable instances
dev/prod parity
```

These improve platform portability/scaling.

# Part 11 — Elastic Beanstalk Overview

Elastic Beanstalk accepts application code and creates/manages an environment using AWS resources.

It can provision:

```text
EC2
Auto Scaling
load balancing
health monitoring
security/configuration
```

The resources remain visible in your AWS account.

# Part 12 — Beanstalk Application

Application is a logical container for:

```text
versions
environments
configuration
```

Example:

```text
Application: customer-portal
├─ Version v1
├─ Version v2
├─ Env staging
└─ Env production
```

# Part 13 — Application Version

A version references a deployable source bundle.

Version labels should be immutable/reproducible:

```text
git SHA
release number
```

rather than ambiguous `latest`.

# Part 14 — Beanstalk Environment

Environment is a running deployment.

Examples:

```text
web server environment
worker environment
```

You can maintain separate production/staging environments.

# Part 15 — Web Server Environment

Typical:

```text
User
 ↓
Load Balancer
 ↓
Auto Scaling EC2
 ↓
Application
```

# Part 16 — Worker Environment

Worker environments process SQS messages.

```text
Web App
 ↓
SQS
 ↓
Beanstalk Worker Environment
```

Useful for asynchronous/longer jobs.

# Part 17 — Beanstalk Platforms

Supported platform families include current supported branches for:

```text
Go
Java
.NET
Node.js
PHP
Python
Ruby
Docker
```

Production should use a supported, non-retired platform branch.

# Part 18 — Platform Branch Lifecycle

Platform branch can be:

```text
Supported
Beta
Retired
```

Production should stay on supported branches and plan upgrades before retirement.

# Part 19 — Source Bundle

Bundle contains application source/configuration.

Good practice:

```text
application
dependency manifest
platform configuration
no secrets
```

# Part 20 — EB CLI

Elastic Beanstalk has a dedicated EB CLI.

Typical workflow:

```bash
eb init
eb create
eb deploy
eb status
eb health
```

Exact options depend on current EB CLI version/config.

# Part 21 — Beanstalk Configuration

Environment configuration includes:

```text
instance type
capacity
load balancer
environment variables
VPC
health
deployment policy
```

# Part 22 — Environment Properties

Use for non-secret configuration:

```text
APP_ENV=production
LOG_LEVEL=INFO
```

Do not store sensitive credentials as casual plaintext configuration when Secrets Manager/Parameter Store is appropriate.

# Part 23 — Beanstalk VPC

Production Beanstalk can be placed into controlled VPC architecture:

```text
public ALB
private EC2
private DB
```

instead of public application instances.

# Part 24 — Beanstalk Auto Scaling

Configure:

```text
min
max
instance types
scaling trigger
```

Beanstalk manages underlying Auto Scaling configuration.

# Part 25 — Beanstalk Health

Enhanced health uses environment/instance signals.

Investigate:

```text
health color/status
events
EC2 health
load balancer health
application logs
```

# Part 26 — Beanstalk Logs

Logs can be requested/streamed to CloudWatch depending on settings.

Central logs are essential because instances may be replaced.

# Part 27 — Beanstalk Deployment Policies

Common concepts include:

```text
all-at-once
rolling
rolling with additional batch
immutable
traffic splitting
```

Select by downtime/capacity/risk.

# Part 28 — All-at-Once Deployment

Updates all instances together.

Advantages:

```text
fast
no extra capacity
```

Risk:

```text
service interruption
```

Usually poor for critical production.

# Part 29 — Rolling Deployment

Updates batches.

```text
batch 1
→ batch 2
→ batch 3
```

Temporary capacity reduction/mixed versions may occur.

# Part 30 — Rolling with Additional Batch

Adds capacity before updating batches.

Benefit:

```text
maintain capacity
```

Tradeoff:

```text
temporary extra cost
```

# Part 31 — Immutable Deployment

Creates fresh instances with new version then swaps them into fleet.

Benefits:

```text
clean environment
safer rollback
no in-place contamination
```

Costs more during deployment.

# Part 32 — Traffic Splitting

Send part of traffic to new version.

Use for canary validation with application metrics.

# Part 33 — .ebextensions Concept

Elastic Beanstalk supports configuration files/extensions for environment customization.

Use cautiously: deep host customization can undermine the benefits of managed platform abstraction.

# Part 34 — Platform Hooks Concept

Hooks can execute at deployment/platform lifecycle stages.

Use for controlled application/platform setup, not undocumented snowflake administration.

# Part 35 — Beanstalk Database Separation

Do not couple production database lifecycle to environment lifecycle.

Preferred:

```text
Beanstalk app
 ↓
independent RDS
```

so deleting/rebuilding app environment does not destroy database.

# Part 36 — Beanstalk Blue/Green

Create:

```text
Blue environment = current
Green environment = new
```

validate Green, then swap CNAME/traffic.

Keep rollback path.

# Part 37 — Beanstalk Cost

Elastic Beanstalk itself has no additional service charge; you pay for underlying resources.

Cost drivers:

```text
EC2
ELB
EBS
NAT
RDS
data transfer
logs
```

# Part 38 — Beanstalk Best Fit

Good:

```text
traditional web application
supported runtime
team wants managed infrastructure
still needs EC2-level flexibility
```

# Part 39 — Beanstalk Poor Fit

Less ideal when:

```text
Kubernetes required
fully event-driven function
complex multi-service container platform
need direct custom host orchestration
```

# Part 40 — AWS App Runner Overview

App Runner deploys:

```text
source code
or
container image
```

to a managed scalable web service.

It reduces infrastructure decisions compared with Beanstalk/ECS.

# Part 41 — App Runner Source Deployment

Concept:

```text
Source Repository
 ↓
App Runner build
 ↓
managed service
```

Supported source integration depends on current App Runner capabilities.

# Part 42 — App Runner Image Deployment

```text
ECR image
 ↓
App Runner
 ↓
HTTPS application
```

Good when application already has a container image.

# Part 43 — Automatic Deployment

App Runner can automatically deploy when repository/image changes according to source configuration.

Production teams should still use controlled release governance.

# Part 44 — App Runner Service

Service bundles:

```text
compute
HTTPS endpoint
load balancing
autoscaling
health
deployment
```

into one higher-level resource.

# Part 45 — App Runner Autoscaling

Configure concepts such as:

```text
minimum provisioned instances
maximum instances
concurrency/load per instance
```

App Runner adjusts capacity based on traffic.

# Part 46 — App Runner Health Check

Health checks can determine if app instance is ready.

Application endpoint should be:

```text
fast
stable
representative
```

without overloading dependencies.

# Part 47 — App Runner Instance Role

Application needs IAM role for AWS API access.

```text
App Runner
 ↓ instance role
Secrets Manager / S3 / DynamoDB
```

# Part 48 — App Runner Access Role

A separate role may be required for App Runner to access deployment resources such as private ECR repositories.

Differentiate platform deployment access from runtime application access.

# Part 49 — App Runner VPC Connector

For private outbound connectivity:

```text
App Runner
 ↓ VPC connector
private VPC resources
```

such as RDS.

Understand that ingress/public endpoint behavior is separate.

# Part 50 — App Runner Observability

Use:

```text
service logs
deployment logs
CloudWatch metrics
application logs
```

to troubleshoot build/runtime failures.

# Part 51 — App Runner Best Fit

Good:

```text
HTTP web app/API
source or container
minimal infrastructure operations
automatic scaling
```

# Part 52 — App Runner vs Beanstalk

```text
Beanstalk:
more underlying AWS/EC2 control

App Runner:
more opinionated managed web platform
```

Choose based on customization vs operational simplicity.

# Part 53 — Containers on AWS Layers

AWS decision model:

```text
Compute:
EC2 / Fargate

Orchestration:
ECS / EKS

Higher-level:
App Runner / other managed application services
```

# Part 54 — Amazon ECS

Managed AWS-native container orchestrator.

Core:

```text
cluster
task definition
task
service
```

# Part 55 — ECS Cluster

Logical grouping/capacity context for container workloads.

Can use:

```text
Fargate
EC2 capacity
```

# Part 56 — Task Definition

Blueprint:

```text
image
CPU
memory
ports
environment
secrets
logs
IAM roles
volumes
```

# Part 57 — Task

Running instantiation of task definition.

A task can contain one or more tightly related containers.

# Part 58 — ECS Service

Maintains desired number of long-running tasks.

Supports:

```text
load balancing
service discovery
rolling deployment
autoscaling
```

# Part 59 — Fargate

Serverless container compute.

```text
ECS/EKS
 ↓
Fargate
 ↓
containers
```

No EC2 worker-node administration.

# Part 60 — Fargate Best Fit

Good:

```text
long-running containers
microservices
batch
specific CPU/memory needs
no node management
```

# Part 61 — Fargate vs Lambda

```text
Lambda:
event-driven
short execution
function abstraction

Fargate:
container
long-running service/job
more CPU/memory/runtime control
```

# Part 62 — ECS EC2 Launch Model

Use EC2-backed ECS when:

```text
steady high utilization
special instance/GPU needs
host-level control
custom daemon workloads
```

Accept node-management responsibility.

# Part 63 — ECS Capacity Providers

Capacity providers connect ECS placement/scaling with:

```text
Fargate
Fargate Spot
Auto Scaling group capacity
```

depending on strategy.

# Part 64 — Fargate Spot

Discounted interruptible Fargate capacity.

Use for interruption-tolerant tasks/services with resilient design.

# Part 65 — Task Role

Permissions used by application container.

```text
container
 ↓ task role
AWS API
```

# Part 66 — Task Execution Role

Permissions used by ECS/Fargate agent/platform actions such as:

```text
pull ECR image
send logs
retrieve configured secrets
```

Do not confuse with app task role.

# Part 67 — ECS Networking

`awsvpc`-style networking gives task ENIs/security groups.

Design:

```text
ALB
 ↓
private ECS tasks
 ↓
private database
```

# Part 68 — ECS Load Balancing

Use ALB for HTTP/path/host routing.

```text
/api → service A
/orders → service B
```

# Part 69 — ECS Service Auto Scaling

Scale desired task count by:

```text
CPU
memory
ALB requests
custom metrics
```

# Part 70 — ECS Deployment

Rolling ECS service deployment gradually replaces tasks.

Configure:

```text
minimum healthy
maximum percent
health checks
deployment circuit breaker
```

# Part 71 — ECS Deployment Circuit Breaker

Can detect failed service deployment and stop/rollback according to configuration.

Still inspect root cause:

```text
image
health
IAM
network
secret
```

# Part 72 — ECS Blue/Green

Can integrate deployment tooling for blue/green traffic shifting.

Use when fast rollback and validation justify complexity.

# Part 73 — ECS Service Discovery

Service discovery allows services to find each other using DNS/service registry patterns.

Avoid hardcoded container IPs.

# Part 74 — ECS Secrets

Inject references from:

```text
Secrets Manager
Parameter Store
```

rather than embedding credentials in images/task definitions.

# Part 75 — ECS Logs

Configure application containers to send logs centrally.

Do not depend on ephemeral container filesystem for operational logs.

# Part 76 — ECR

Managed container registry.

Use:

```text
immutable/versioned image tags
scanning
lifecycle
replication where needed
```

# Part 77 — ECR Lifecycle

Delete old/unreferenced images automatically.

Preserve images required for rollback/reproducibility.

# Part 78 — Amazon EKS

Managed Kubernetes.

Use when requirement includes:

```text
Kubernetes API
Helm/operators
Kubernetes portability/ecosystem
```

Do not choose Kubernetes only because containers are used.

# Part 79 — EKS Control Plane

AWS manages Kubernetes control-plane service.

Customer still manages substantial:

```text
workloads
RBAC
networking
nodes/Fargate choice
add-ons
security
```

# Part 80 — EKS Managed Nodes

AWS-managed node groups simplify worker lifecycle relative to self-managed node groups, but EC2/node patching and workload scheduling concerns remain.

# Part 81 — EKS on Fargate

Run supported Kubernetes pods without managing EC2 worker nodes.

Use when workload fits Fargate/Kubernetes constraints.

# Part 82 — ECS vs EKS

```text
ECS:
AWS-native, simpler

EKS:
Kubernetes standard/ecosystem, more complexity
```

Choose EKS only when Kubernetes value exceeds operational cost.

# Part 83 — Lambda Overview

Lambda runs code in response to events without server management.

AWS manages:

```text
capacity
infrastructure
scaling
patching
```

You manage code, dependencies, permissions, configuration, and application behavior.

# Part 84 — Lambda Runtime

AWS provides managed runtimes for supported languages and supports custom runtime/container image patterns.

Track runtime deprecation and upgrade before production retirement.

# Part 85 — Handler

Handler is function entry point.

Python example:

```python
def handler(event, context):
    return {"statusCode": 200, "body": "ok"}
```

# Part 86 — Event

Lambda receives event payload.

Example S3/SQS/API events have different JSON schemas.

Do not assume every trigger produces the same structure.

# Part 87 — Execution Environment Reuse

Lambda may reuse execution environments.

Initialize expensive clients outside handler where safe:

```python
import boto3
s3 = boto3.client("s3")

def handler(event, context):
    ...
```

Never rely on reuse for correctness.

# Part 88 — Lambda Statelessness

Local `/tmp` or memory can persist briefly across warm invocations but is not durable application state.

Persist durable state in:

```text
S3
DynamoDB
RDS
EFS
```

# Part 89 — Lambda Timeout

Current AWS guidance documents a maximum Lambda execution duration of 15 minutes.

Long jobs may fit:

```text
Fargate
Batch
Step Functions orchestration
```

better.

# Part 90 — Lambda Memory

Memory selection affects available compute resources.

Benchmark:

```text
duration
memory
cost
```

rather than choosing minimum memory automatically.

# Part 91 — Lambda Concurrency

Concurrency:

```text
simultaneous function executions
```

High concurrency can overwhelm:

```text
RDS
external API
downstream service
```

# Part 92 — Reserved Concurrency

Can:

```text
reserve capacity for function
limit maximum concurrency
```

Useful for downstream protection and tenant isolation.

# Part 93 — Provisioned Concurrency

Pre-initializes execution environments to reduce cold-start latency.

Tradeoff:

```text
lower latency
higher idle cost
```

# Part 94 — Cold Start

A new execution environment must initialize:

```text
runtime
code
dependencies
initialization logic
```

Keep initialization efficient.

# Part 95 — Lambda Versions

Published versions are immutable snapshots.

Use versions for controlled releases.

# Part 96 — Lambda Aliases

Alias points to version.

```text
prod → v12
```

Can support weighted traffic between versions for canary release.

# Part 97 — Lambda Layers

Package reusable dependencies separately.

Use carefully: too many/larger layers can complicate dependency/version management.

# Part 98 — Environment Variables

Use for non-secret configuration.

Secrets should be referenced from protected secret services.

# Part 99 — Lambda Execution Role

Grant only needed AWS permissions.

Example:

```text
GetObject one bucket
PutItem one table
```

# Part 100 — Lambda Resource Policy

Controls who/services can invoke function.

Example:

```text
API Gateway
S3
SNS
cross-account principal
```

# Part 101 — Synchronous Invocation

Caller waits for result.

Examples:

```text
API Gateway
direct SDK invoke
```

Caller sees errors directly.

# Part 102 — Asynchronous Invocation

Lambda queues event internally and retries according to service behavior.

Configure:

```text
destinations
DLQ
retry/age controls
```

as supported.

# Part 103 — Poll-Based Event Sources

For sources such as:

```text
SQS
Kinesis
DynamoDB Streams
```

Lambda event source mapping polls and invokes function batches.

# Part 104 — SQS + Lambda

```text
Producer
 ↓
SQS
 ↓
Lambda workers
```

Good for buffering and asynchronous scaling.

# Part 105 — Partial Batch Failure Concept

For batch sources, design failure handling so one bad item does not force unnecessary reprocessing when supported response modes can identify failed records.

# Part 106 — Lambda DLQ

Failed asynchronous events can be routed to durable failure handling.

DLQ is not a substitute for monitoring and replay tooling.

# Part 107 — Lambda Destinations

Can route successful/failed asynchronous invocation results to supported destinations.

Useful for event workflows and observability.

# Part 108 — Lambda VPC Connectivity

Attach function to VPC when it needs private VPC resources.

For AWS public APIs, consider service endpoints/private connectivity rather than unnecessary VPC complexity.

# Part 109 — Lambda + RDS

High Lambda concurrency can create connection storms.

Use:

```text
RDS Proxy
connection pooling
concurrency limits
```

# Part 110 — Lambda + EFS

Lambda can mount EFS for supported use cases needing shared filesystem/dependency/data access.

Consider startup/performance and access-point security.

# Part 111 — Lambda Observability

Monitor:

```text
Invocations
Errors
Duration
Throttles
ConcurrentExecutions
IteratorAge for streams
logs
traces
```

# Part 112 — API Gateway

Managed API front door.

Supports API types including:

```text
HTTP APIs
REST APIs
WebSocket APIs
```

with different feature/cost profiles.

# Part 113 — HTTP API

Lower-cost/lighter-weight choice for many HTTP backends.

Use when advanced REST API features are unnecessary.

# Part 114 — REST API

Feature-rich API Gateway model supporting advanced:

```text
request/response transforms
API keys/usage plans
caching and other capabilities
```

depending on requirements.

# Part 115 — WebSocket API

Persistent bidirectional communication.

Use for:

```text
chat
realtime dashboards
notifications
```

# Part 116 — API Gateway Integration

Backends can include:

```text
Lambda
HTTP endpoint
AWS service integrations
private integrations
```

# Part 117 — Lambda Proxy Integration

API request largely passes to Lambda event and Lambda returns HTTP response structure.

Simple for serverless APIs.

# Part 118 — API Authentication

Options include:

```text
IAM
Cognito/user identity
JWT authorizers
Lambda authorizers
```

depending on API type/features.

# Part 119 — API Authorization

Authenticate caller then enforce:

```text
resource/action
tenant
scope
business rule
```

Application authorization remains necessary.

# Part 120 — API Throttling

Protect:

```text
backend
cost
fairness
```

with rate/burst controls where supported.

# Part 121 — API Caching

Caching can reduce backend latency/load for cacheable REST responses.

Do not cache personalized/sensitive data with incorrect keys.

# Part 122 — API Gateway Access Logs

Log:

```text
request ID
status
latency
caller context
route
```

while avoiding sensitive payload leakage.

# Part 123 — Custom Domain

Use ACM certificate + API Gateway custom domain + Route 53 DNS.

```text
api.example.com
```

instead of provider-generated endpoint.

# Part 124 — AWS AppSync

Managed GraphQL service.

Use when application benefits from:

```text
GraphQL schema
multiple data sources
real-time subscriptions
client data synchronization patterns
```

# Part 125 — GraphQL

Clients request exact fields:

```graphql
query {
  order(id: "123") {
    id
    status
  }
}
```

Useful for frontend/mobile APIs.

# Part 126 — AppSync Data Sources

Can integrate with supported:

```text
DynamoDB
Lambda
HTTP
relational/service integrations
```

depending on resolver model.

# Part 127 — Route 53 for Applications

Use DNS for:

```text
custom domains
health/failover
weighted release
latency/global routing
```

# Part 128 — CloudFront for Web Apps

Use for:

```text
edge caching
TLS
global delivery
WAF
S3/ALB/API origins
```

# Part 129 — Static + Dynamic CloudFront

Example cache behaviors:

```text
/static/* → S3
/api/*    → API Gateway/ALB
```

One distribution can front multiple origins.

# Part 130 — AWS WAF

Protect web entry points with:

```text
managed rules
rate limits
IP rules
application attack filters
```

WAF complements secure code.

# Part 131 — ACM

Use managed certificates with supported AWS web services.

Automated renewal depends on validation/integration remaining valid.

# Part 132 — ALB for Managed Platforms

ALB is common for:

```text
Beanstalk
ECS
EKS
EC2
```

when layer-7 routing is needed.

# Part 133 — SQS

Queue decouples application components.

Use for:

```text
background work
burst buffering
retry
worker scaling
```

# Part 134 — SNS

Fan-out:

```text
event
 ↓
SNS
 ├─ SQS
 ├─ Lambda
 └─ notification
```

# Part 135 — EventBridge

Event routing:

```text
source
 ↓
event bus
 ↓ rules
targets
```

Excellent for loosely coupled domain/infrastructure events.

# Part 136 — Step Functions

Workflow orchestration:

```text
validate
 ↓
charge
 ↓
reserve inventory
 ↓
ship
```

with retries/branches/parallel steps.

# Part 137 — Async Request Pattern

```text
Client
 ↓ POST /jobs
API
 ↓
SQS
 ↓
Worker
 ↓
Result Store
```

API returns job ID quickly instead of holding HTTP request open.

# Part 138 — Long-Running Work

If job exceeds Lambda's execution model:

```text
API Gateway
 ↓
SQS
 ↓
Fargate / Batch
```

is often better.

# Part 139 — RDS as Web Dependency

Use managed relational DB for:

```text
transactions
SQL
relationships
```

Keep DB private and credentials in Secrets Manager.

# Part 140 — DynamoDB as Web Dependency

Use for:

```text
key-value/document
high scale
serverless workloads
low operational overhead
```

Design access patterns first.

# Part 141 — ElastiCache

Use for:

```text
sessions
hot objects
query cache
rate limits
```

Cache should normally not be only durable copy.

# Part 142 — S3

Use for:

```text
uploads
static assets
documents
media
logs
```

Use presigned URLs to avoid proxying large files through app servers.

# Part 143 — EFS

Shared file storage can support legacy/shared-content requirements for compatible platforms/compute.

Prefer object storage when true filesystem semantics are unnecessary.

# Part 144 — Secrets Manager

Store:

```text
database passwords
API credentials
application secrets
```

Retrieve using workload IAM roles.

# Part 145 — Parameter Store

Store:

```text
configuration
secure strings
feature/environment parameters
```

according to application needs.

# Part 146 — Application Configuration

Separate:

```text
code
config
secret
```

Example:

```text
code → Git/image
config → environment/Parameter Store
secret → Secrets Manager
```

# Part 147 — Feature Flags

Deploy code independent of feature activation.

Useful for:

```text
gradual release
rollback
A/B
emergency disable
```

Use controlled configuration system.

# Part 148 — Session Management

For horizontally scaled web apps:

```text
do not keep session only in local RAM
```

Use:

```text
signed token
ElastiCache
DynamoDB/database
```

depending on application.

# Part 149 — Health Endpoint

Good `/health`:

```text
fast
stable
does not mutate
```

Separate:

```text
liveness
readiness
deep dependency health
```

where platform supports.

# Part 150 — Graceful Shutdown

On termination/deployment:

```text
stop new traffic
drain connections
finish work
close resources
exit
```

This prevents dropped requests.

# Part 151 — CloudWatch Application Metrics

Monitor:

```text
requests
errors
latency
saturation
business outcomes
```

Platform CPU alone is insufficient.

# Part 152 — Structured Logging

Use JSON-style logs:

```json
{
  "level": "ERROR",
  "request_id": "abc",
  "service": "orders",
  "message": "payment failed"
}
```

Avoid secrets/PII.

# Part 153 — Correlation ID

Propagate request identifier:

```text
client
→ API
→ service
→ queue
→ worker
```

for end-to-end investigation.

# Part 154 — AWS X-Ray Concept

Distributed tracing helps locate latency/errors across services.

Use trace context across supported integrations.

# Part 155 — Alarms

Alert on:

```text
error rate
latency
failed deployment
queue backlog
throttling
DB saturation
```

not every normal scaling event.

# Part 156 — CI/CD Pipeline Concept

```text
Git push
 ↓
test
 ↓
build
 ↓
artifact/image
 ↓
deploy staging
 ↓
verify
 ↓
production
```

Platform choice determines deployment mechanism.

# Part 157 — Artifact Immutability

Deploy same tested artifact:

```text
staging
→ production
```

Do not rebuild differently at each environment.

# Part 158 — Container Build Pipeline

```text
Dockerfile
 ↓
build
 ↓
scan
 ↓
ECR
 ↓
ECS/App Runner
```

# Part 159 — Lambda Deployment Package

Use:

```text
ZIP
or
container image
```

according to Lambda-supported packaging.

Keep dependencies reproducible.

# Part 160 — CloudFormation Integration

Model:

```text
API Gateway
Lambda
IAM
DynamoDB
alarms
```

as IaC for repeatability.

# Part 161 — AWS CDK Concept

Define infrastructure with programming language and synthesize CloudFormation.

Useful for application teams comfortable with software abstractions.

# Part 162 — Platform Cost Model

Compare:

```text
idle capacity
request volume
execution duration
memory/CPU
load balancer
NAT
logs
database
data transfer
```

Do not compare only compute unit price.

# Part 163 — Beanstalk Cost Model

Cost resembles underlying:

```text
EC2
ALB
EBS
Auto Scaling
network
```

because Beanstalk orchestrates those resources.

# Part 164 — App Runner Cost Model

Cost is based on service resources/usage according to current pricing.

Low traffic can scale down, but understand minimum/provisioned capacity behavior and data/network dependencies.

# Part 165 — Fargate Cost Model

Pay for provisioned task CPU/memory/resources over task runtime.

Good operational simplicity; steady high-utilization fleets may warrant EC2 comparison.

# Part 166 — Lambda Cost Model

Main dimensions:

```text
requests
execution duration/resources
provisioned concurrency if used
data/services
```

Bursty workloads can be very efficient.

# Part 167 — API Gateway Cost Model

Cost includes request volume and API type/features/data transfer.

HTTP API can be more cost-efficient when REST API advanced features are unnecessary.

# Part 168 — Platform Troubleshooting Method

Trace:

```text
DNS
 ↓
CDN/WAF
 ↓
API/LB
 ↓
platform service
 ↓
application
 ↓
IAM
 ↓
network
 ↓
database/queue
```

# Part 169 — Beanstalk Deployment Failure

Check:

```text
Events
deployment logs
source bundle
runtime/dependencies
platform version
instance role
health
```

# Part 170 — App Runner Deployment Failure

Check:

```text
source/image access
build command
start command
port
health check
IAM
deployment logs
```

# Part 171 — ECS Task Won't Start

Check:

```text
ECR image
execution role
CPU/memory
subnet IP
security group
secret
log driver
entrypoint
```

# Part 172 — ECS Service Unhealthy

Check:

```text
container process
port mapping
ALB target
health path
SG
startup time
deployment configuration
```

# Part 173 — Lambda Timeout

Check:

```text
slow dependency
network/VPC
DB query
external API
large data
memory/CPU
```

Increasing timeout without root-cause analysis hides problems.

# Part 174 — Lambda AccessDenied

Check:

```text
execution role
resource policy
KMS
S3/DynamoDB policy
VPC endpoint policy
SCP
```

# Part 175 — API Gateway 5xx

Check:

```text
integration error
Lambda exception
timeout
permission
mapping
backend response format
```

# Part 176 — API Gateway 4xx

Check:

```text
route
authentication
authorization
request validation
throttling
resource path
```

# Part 177 — Queue Backlog

Check:

```text
message arrival rate
worker count
processing duration
errors
DLQ
visibility timeout
downstream bottleneck
```

# Part 178 — Secret Rotation Failure

Check:

```text
rotation function/workflow
IAM
network
database permission
application compatibility
staged versions
```

# Part 179 — Deployment Rollback Decision

Rollback when:

```text
customer impact
error budget burn
security issue
data risk
```

and rollback is safer than forward repair.

Have objective thresholds.

# Part 180 — PaaS Final Mental Model

The objective is not choosing the most managed service.

Choose the **lowest operational complexity that still satisfies**:

```text
runtime
control
networking
performance
deployment
security
portability
cost
```

That is sound application-platform engineering.

---

# Supplemental Deep-Study Layer — Amazon PaaS Web Services

> **Source distinction:** The complete uploaded course remains preserved. The sections below are supplemental engineering expansion added for deeper architecture, operations, CLI/configuration, failure analysis, labs, and production troubleshooting.

Focus: platform-selection discipline, stateless application design, Beanstalk/App Runner/ECS/Lambda/API Gateway engineering, async/event patterns, deployment safety, observability, secrets, application resilience, and platform cost.

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

## Advanced Deep Dive 1 — Platform Selection by Hard Constraints

### Concept and Detailed Explanation

Select the lowest operational complexity that still satisfies execution duration, runtime, container/Kubernetes needs, OS control, networking, storage, latency, deployment, security, and cost.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Need OS → EC2
Need K8s → EKS
Container service → ECS/Fargate/App Runner
Short event → Lambda
Traditional app → Beanstalk
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
runtime=
long_running=
container=
kubernetes=
private_network=
OS_control=
scale_to_zero=
EOF
```

### Expected Behavior

Platform choice can be explained from hard requirements.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A 45-minute job uses Fargate/Batch instead of Lambda.

### Troubleshooting Workflow

```text
platform mismatch
 ↓ violated requirement
 ↓ execution model
 ↓ network/storage
 ↓ operations/cost
 ↓ reselect
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Eliminate platforms that violate hard constraints first.

---

## Advanced Deep Dive 2 — Code / Config / Secret Separation

### Concept and Detailed Explanation

Code, ordinary configuration, and secrets require different lifecycle and access control. Build once, inject config, retrieve secrets by workload identity.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Git/image → code
Parameter/env → nonsecret config
Secrets Manager → credentials
IAM role → retrieval
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
APP_ENV=prod
LOG_LEVEL=INFO
DB_SECRET_ARN=arn:aws:secretsmanager:...
EOF
```

### Expected Behavior

Production uses the same artifact as staging while secrets never enter Git.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

One container digest is promoted across environments with different runtime config references.

### Troubleshooting Workflow

```text
wrong config/secret leak
 ↓ where stored?
 ↓ image/Git?
 ↓ environment?
 ↓ secret manager?
 ↓ rotate/fix
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Promote one artifact and inject environment-specific configuration.

---

## Advanced Deep Dive 3 — Stateless Compute

### Concept and Detailed Explanation

Managed platforms replace tasks, instances, and functions. Durable state must live in S3, databases, queues, or appropriate shared storage; local process memory and writable layers are disposable.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Compute
 ├─ session → token/cache
 ├─ files → S3/EFS
 ├─ data → DB
 └─ jobs → SQS
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Do not store unique durable state in:
container layer
instance local disk
process memory
Lambda /tmp
EOF
```

### Expected Behavior

Any compute unit can terminate without data loss.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

App Runner deployment replaces every instance while sessions survive in cache/token store.

### Troubleshooting Workflow

```text
replacement loses state
 ↓ identify local state
 ↓ durable vs cache
 ↓ move externally
 ↓ termination test
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design compute as replaceable.

---

## Advanced Deep Dive 4 — Liveness vs Readiness

### Concept and Detailed Explanation

Liveness says the process exists; readiness says it can serve traffic. Deep health can test more dependencies separately. Load balancer health checks should be fast and deterministic.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
liveness → process
readiness → serve traffic
deep health → full dependency/business path
```

### CLI / Configuration / Calculation

```bash
curl -fsS http://127.0.0.1:8080/health
curl -fsS http://127.0.0.1:8080/ready
```

### Expected Behavior

Unready instances drain while healthy capacity stays available.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

DB initialization failure makes readiness fail even though process is alive.

### Troubleshooting Workflow

```text
health flaps
 ↓ endpoint speed
 ↓ dependency choices
 ↓ timeout/threshold
 ↓ startup grace
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Keep readiness fast; test deep dependencies with synthetic monitoring.

---

## Advanced Deep Dive 5 — Graceful Shutdown

### Concept and Detailed Explanation

Deployments and scale-in terminate compute. Applications should stop new work, drain connections, finish or release jobs, close resources, and exit within a bounded deadline.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
termination signal
 ↓ mark not ready
 ↓ drain
 ↓ finish/hand off
 ↓ close connections
 ↓ exit
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
SIGTERM:
stop polling
stop accepting
wait bounded
close DB
exit
EOF
```

### Expected Behavior

In-flight requests/jobs survive normal deployments.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

ECS worker stops polling SQS before task termination.

### Troubleshooting Workflow

```text
dropped work
 ↓ signal handled?
 ↓ ALB deregistration
 ↓ queue ack
 ↓ shutdown deadline
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Test graceful termination during deployment tests.

---

## Advanced Deep Dive 6 — Beanstalk Blue/Green

### Concept and Detailed Explanation

Blue/green creates a separate environment and shifts application endpoint/traffic after validation. This reduces in-place risk but requires database/schema compatibility and temporary double capacity.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Blue current
Green new
 ↓ validate
 ↓ swap traffic
 ↓ monitor
 ↓ retire Blue later
```

### CLI / Configuration / Calculation

```bash
eb status 2>/dev/null || true
eb health 2>/dev/null || true
```

### Expected Behavior

Green passes business/health checks before production traffic moves.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Green is swapped in while Blue remains available for rollback.

### Troubleshooting Workflow

```text
post-swap errors
 ↓ green health
 ↓ schema compatibility
 ↓ config/secrets
 ↓ swap back if safe
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Keep Blue until Green is stable and data compatibility is confirmed.

---

## Advanced Deep Dive 7 — Beanstalk Platform Lifecycle

### Concept and Detailed Explanation

Managed runtimes still have supported/retired platform branches. Runtime upgrades can break native dependencies and should be tested like application releases.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
supported branch
 ↓ new platform
 ↓ staging tests
 ↓ production safe deployment
```

### CLI / Configuration / Calculation

```bash
eb platform list 2>/dev/null || true
```

### Expected Behavior

Production remains on supported platform versions.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Python platform upgrade reveals a native dependency issue in staging.

### Troubleshooting Workflow

```text
upgrade fail
 ↓ runtime version
 ↓ dependencies
 ↓ hooks/config
 ↓ health
 ↓ rollback/fix
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat managed platform upgrades as code/runtime changes.

---

## Advanced Deep Dive 8 — App Runner Build vs Runtime Identity

### Concept and Detailed Explanation

Deployment-plane access and runtime application permissions are different. App Runner may need access to source/ECR while runtime needs only business AWS APIs.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Source/ECR
 ↓ access role
App Runner
 ↓ runtime role
S3/Secrets/DB API
```

### CLI / Configuration / Calculation

```bash
aws apprunner list-services 2>/dev/null || true
```

### Expected Behavior

Build/deploy and runtime use separate least-privilege roles.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Image pull works through access role; app reads one S3 prefix through instance role.

### Troubleshooting Workflow

```text
AccessDenied
 ↓ build or runtime?
 ↓ ECR/source role
 ↓ instance role
 ↓ resource/KMS policy
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Separate deployment-plane and runtime permissions.

---

## Advanced Deep Dive 9 — App Runner VPC Connector

### Concept and Detailed Explanation

Adding VPC connectivity changes outbound networking. Private DB access may work while Internet/SaaS access fails if NAT, DNS, or endpoints are missing.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
User → App Runner public ingress
          ↓ outbound
      VPC connector
          ↓
      private RDS / endpoints / NAT
```

### CLI / Configuration / Calculation

```bash
aws apprunner list-vpc-connectors 2>/dev/null || true
```

### Expected Behavior

App reaches private dependencies without exposing them publicly.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

After connector enablement, private DB works but SaaS API fails because egress was not designed.

### Troubleshooting Workflow

```text
outbound fail
 ↓ connector subnets
 ↓ SG
 ↓ route
 ↓ NAT/endpoints
 ↓ DNS
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat VPC connector as a network architecture change.

---

## Advanced Deep Dive 10 — ECS Task Definition Immutability

### Concept and Detailed Explanation

Task definitions are versioned revisions. Deploy specific image digests and configuration revisions so rollback is reproducible.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Git SHA
 ↓ image digest
 ↓ task definition revision
 ↓ ECS deployment
```

### CLI / Configuration / Calculation

```bash
aws ecs list-task-definitions --sort DESC --max-items 20 2>/dev/null || true
```

### Expected Behavior

Every running task maps to an exact artifact and configuration revision.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Rollback points service to prior task-definition revision.

### Troubleshooting Workflow

```text
unknown version
 ↓ task revision
 ↓ image digest
 ↓ build metadata
 ↓ correct deployment
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use immutable artifacts and versioned task definitions.

---

## Advanced Deep Dive 11 — Task Role vs Execution Role

### Concept and Detailed Explanation

ECS execution role supports platform startup actions such as ECR pulls/logs/secret retrieval, while task role authorizes application code. Diagnose based on when the failure occurs.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
ECS platform → execution role → ECR/Logs/startup
Container app → task role → S3/DynamoDB/business APIs
```

### CLI / Configuration / Calculation

```bash
aws ecs describe-task-definition --task-definition <TASKDEF> 2>/dev/null || true
```

### Expected Behavior

Image/startup failures and application API failures are separated.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Task starts, then DynamoDB access fails: task role is the relevant layer.

### Troubleshooting Workflow

```text
permission failure
 ↓ before start? execution role
 ↓ after app start? task role
 ↓ resource/KMS/SCP
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Grant each role only its layer's permissions.

---

## Advanced Deep Dive 12 — ECS awsvpc Subnet Capacity

### Concept and Detailed Explanation

Fargate/awsvpc tasks consume ENIs and private addresses. Deployment surge and autoscaling therefore depend on subnet capacity.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
ECS tasks
 ↓ ENIs
 ↓ subnet IP pool
 ↓ scale/deployment ceiling
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-subnets --query 'Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone,Free:AvailableIpAddressCount}' --output table
```

### Expected Behavior

Task subnets support maximum scale plus rolling/blue-green overlap.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Service cannot double capacity for deployment because /27 subnets are full.

### Troubleshooting Workflow

```text
placement fail
 ↓ free IPs
 ↓ AZ
 ↓ other ENIs/endpoints
 ↓ new/larger subnet
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Capacity-plan subnet IPs for task count and deployment headroom.

---

## Advanced Deep Dive 13 — ECS Deployment Surge

### Concept and Detailed Explanation

Minimum/maximum healthy percentages determine how many old/new tasks coexist. These values trade capacity, rollout speed, and required headroom.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
desired=10
min healthy=100%
max=200%
 ↓ up to 20 during rollout
```

### CLI / Configuration / Calculation

```bash
aws ecs describe-services --cluster <CLUSTER> --services <SERVICE> 2>/dev/null || true
```

### Expected Behavior

Deployment preserves serving capacity without exhausting IP/quota/DB headroom.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

100/200 rollout cannot launch because subnet has room for only 14 tasks.

### Troubleshooting Workflow

```text
deployment stuck
 ↓ desired/running/pending
 ↓ min/max
 ↓ IP/quota
 ↓ health
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Size deployment surge from real headroom.

---

## Advanced Deep Dive 14 — EKS Selection Gate

### Concept and Detailed Explanation

Kubernetes adds flexibility and ecosystem value but also RBAC, cluster/network/add-on, upgrade, and operational complexity. Require an explicit Kubernetes need.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Need Kubernetes API/operators/Helm portability?
 yes → EKS
 no → ECS/App Runner/Lambda may be simpler
```

### CLI / Configuration / Calculation

```bash
aws eks list-clusters --output table 2>/dev/null || true
```

### Expected Behavior

Kubernetes is chosen because a concrete capability requires it.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Custom operators and cross-cloud Kubernetes standards justify EKS.

### Troubleshooting Workflow

```text
platform too complex
 ↓ which K8s capability used?
 ↓ simpler service possible?
 ↓ team skill/ops
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use EKS only when Kubernetes value exceeds complexity.

---

## Advanced Deep Dive 15 — Lambda Initialization Reuse

### Concept and Detailed Explanation

Initialize expensive SDK clients outside the handler when safe because warm execution environments may reuse them. Correctness must not depend on reuse and stale connections need recovery.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
cold start
 ↓ module init
 ↓ handler
warm call
 ↓ reuse client if environment survives
```

### CLI / Configuration / Calculation

```bash
cat <<'PY'
import boto3
s3=boto3.client("s3")
def handler(event,context):
    return {"ok":True}
PY
```

### Expected Behavior

Cold initialization is reduced while function remains correct on every fresh environment.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

HTTP/SDK client is reused but reconnects after stale socket.

### Troubleshooting Workflow

```text
intermittent connection
 ↓ init location
 ↓ warm reuse?
 ↓ stale client
 ↓ retry/recreate
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Reuse clients for performance, never for correctness.

---

## Advanced Deep Dive 16 — Lambda /tmp Semantics

### Concept and Detailed Explanation

Temporary storage is scratch space, not durable state. Warm reuse may preserve files briefly, but the environment can disappear at any time.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Invocation
 ↓ /tmp scratch
 may persist warm
 but disposable
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
from pathlib import Path
p=Path('/tmp/demo.txt');p.write_text('scratch');print(p.read_text())
PY
```

### Expected Behavior

Function remains correct even when `/tmp` starts empty.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Image transform downloads to `/tmp` and persists result to S3.

### Troubleshooting Workflow

```text
file missing
 ↓ assumed warm reuse?
 ↓ retrieve source from durable store
 ↓ persist output externally
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use `/tmp` only for ephemeral working data.

---

## Advanced Deep Dive 17 — Lambda Concurrency Protects RDS

### Concept and Detailed Explanation

Lambda can scale faster than a relational DB can accept sessions. Concurrency limits, RDS Proxy, pooling, and queues protect the database.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
burst
 ↓ Lambda
 ↓ reserved concurrency
 ↓ RDS Proxy
 ↓ DB
```

### CLI / Configuration / Calculation

```bash
aws lambda get-function-concurrency --function-name <FUNCTION> 2>/dev/null || true
aws rds describe-db-proxies --output table 2>/dev/null || true
```

### Expected Behavior

Serverless burst does not exhaust DB connections.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

DB-using function is capped while stateless functions remain elastic.

### Troubleshooting Workflow

```text
DB connections exhausted
 ↓ Lambda concurrency
 ↓ proxy/pool
 ↓ transaction duration
 ↓ DB max
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Set concurrency from downstream capacity.

---

## Advanced Deep Dive 18 — Lambda Idempotency

### Concept and Detailed Explanation

Retries and duplicate delivery are normal. Use idempotency keys and atomic conditional records before irreversible effects.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
request/event ID
 ↓ conditional record
 first → process
 duplicate → return/no-op
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
DynamoDB condition:
attribute_not_exists(request_id)
EOF
```

### Expected Behavior

Duplicate events create one business effect.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Payment callback retry returns the existing result.

### Troubleshooting Workflow

```text
duplicate effect
 ↓ event ID
 ↓ idempotency store
 ↓ transaction boundary
 ↓ acknowledgement
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Assume events can repeat.

---

## Advanced Deep Dive 19 — Lambda Batch Failure Isolation

### Concept and Detailed Explanation

Batch event sources can reprocess successful records when one item fails. Use supported partial-batch response patterns and DLQ/redrive to isolate poison records.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
batch A B C D
 ↓ C fails
report C
 ↓ retry C only
```

### CLI / Configuration / Calculation

```bash
aws lambda list-event-source-mappings --function-name <FUNCTION> 2>/dev/null || true
```

### Expected Behavior

One bad record does not repeatedly process an entire successful batch.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Nine valid SQS messages succeed while one invalid record retries.

### Troubleshooting Workflow

```text
batch loops
 ↓ failed record
 ↓ partial response
 ↓ DLQ
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

Isolate poison records and keep handlers idempotent.

---

## Advanced Deep Dive 20 — Lambda Alias Canary

### Concept and Detailed Explanation

Published Lambda versions and aliases support controlled weighted release. Rollback is a fast alias change if data/schema remains compatible.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
prod alias
 95% → v10
 5% → v11
 ↓ observe
 expand or rollback
```

### CLI / Configuration / Calculation

```bash
aws lambda get-alias --function-name <FUNCTION> --name prod 2>/dev/null || true
```

### Expected Behavior

New version receives bounded traffic and is promoted only after gates pass.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Latency regression in v11 returns all traffic to v10.

### Troubleshooting Workflow

```text
canary bad
 ↓ version metrics/logs
 ↓ alias weight
 ↓ rollback
 ↓ fix
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Define canary thresholds before traffic shift.

---

## Advanced Deep Dive 21 — API Gateway HTTP vs REST

### Concept and Detailed Explanation

Choose API type based on required features and economics. A simple JWT/API integration may fit HTTP API; advanced REST-specific features may justify REST API.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
requirements
 ↓ simple modern HTTP?
 → HTTP API
 ↓ advanced REST features?
 → REST API
```

### CLI / Configuration / Calculation

```bash
aws apigatewayv2 get-apis --output table 2>/dev/null || true
aws apigateway get-rest-apis --output table 2>/dev/null || true
```

### Expected Behavior

API type provides necessary features without unnecessary complexity.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

JWT Lambda API uses HTTP API; legacy API with advanced usage/caching requirements stays REST.

### Troubleshooting Workflow

```text
feature missing
 ↓ API type
 ↓ required capability
 ↓ auth/integration
 ↓ migrate if needed
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use the simplest API type that satisfies requirements.

---

## Advanced Deep Dive 22 — API Private Integration

### Concept and Detailed Explanation

Managed API ingress can still reach private backends without making them public. Private integrations/VPC links should preserve backend isolation.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Client
 ↓ API Gateway
 ↓ VPC link/private integration
 ↓ internal LB
 ↓ private ECS/EC2
```

### CLI / Configuration / Calculation

```bash
aws apigatewayv2 get-vpc-links --output table 2>/dev/null || true
```

### Expected Behavior

Public API front door reaches private services without direct backend Internet exposure.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

API Gateway routes to private ECS behind internal load balancer.

### Troubleshooting Workflow

```text
private integration 5xx
 ↓ VPC link
 ↓ LB target health
 ↓ SG/route
 ↓ app port
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Keep backend private when public exposure is unnecessary.

---

## Advanced Deep Dive 23 — API Authentication vs Object Authorization

### Concept and Detailed Explanation

Authenticating a caller does not prove the caller may access every object. Enforce route/scope authorization and business-object ownership using trusted identity claims.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Client
 ↓ JWT/IAM auth
 ↓ route scope
 ↓ backend
 ↓ tenant/object authorization
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
trusted claim: tenant_id
request path: /orders/{id}
backend verifies order.tenant_id == token.tenant_id
EOF
```

### Expected Behavior

One tenant cannot read another tenant's resource by changing URL IDs.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

JWT scope allows read-orders; backend still validates ownership.

### Troubleshooting Workflow

```text
403/possible data leak
 ↓ token valid
 ↓ scope
 ↓ object ownership
 ↓ tenant context
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Enforce authorization at capability and object levels.

---

## Advanced Deep Dive 24 — Idempotent POST

### Concept and Detailed Explanation

Client timeouts cause POST retries. Accept an idempotency key and store the outcome so retry returns the original result rather than repeating the side effect.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
POST + idempotency key
 ↓ conditional record
 first → execute/store
 retry → return previous result
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Idempotency-Key: unique request UUID
Scope: caller + operation
TTL: business-defined
EOF
```

### Expected Behavior

Repeated client retries create one order/charge.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Mobile client retries after timeout and receives original order ID.

### Troubleshooting Workflow

```text
duplicate POST
 ↓ same key?
 ↓ stored payload/result
 ↓ payload mismatch?
 ↓ return prior/conflict
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Require idempotency for retry-prone irreversible operations.

---

## Advanced Deep Dive 25 — API Backpressure

### Concept and Detailed Explanation

Throttle ingress before the slowest dependency is overloaded. Rate/burst controls and async queues turn uncontrolled overload into predictable 429/queued behavior.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
clients
 ↓ WAF/API throttle
 ↓ allowed traffic
 backend finite capacity
```

### CLI / Configuration / Calculation

```bash
aws apigateway get-usage-plans --output table 2>/dev/null || true
```

### Expected Behavior

Excess demand is rejected/buffered before DB or Lambda collapse.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

API throttling prevents database connection storm.

### Troubleshooting Workflow

```text
429/5xx
 ↓ edge throttle
 ↓ compute concurrency
 ↓ DB/API limits
 ↓ client retry
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Set ingress capacity from end-to-end dependency capacity.

---

## Advanced Deep Dive 26 — WebSocket Connection Lifecycle

### Concept and Detailed Explanation

WebSocket connections are ephemeral. Track connection IDs with TTL, handle disconnects and stale entries, and remove IDs when sends report Gone.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
connect
 ↓ store connection
 ↓ messages
 ↓ disconnect/stale cleanup
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
connection_id
user_id
connected_at
expires_at
EOF
```

### Expected Behavior

Disconnected clients do not produce repeated failed sends.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Dashboard removes stale connection IDs after failed post-to-connection.

### Troubleshooting Workflow

```text
send fails
 ↓ connection exists?
 ↓ client gone?
 ↓ delete stale state
 ↓ reconnect
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat connection IDs as temporary resources.

---

## Advanced Deep Dive 27 — CloudFront Multi-Origin

### Concept and Detailed Explanation

Use separate cache behaviors for static and dynamic content. Static assets can be aggressively cached; personalized API paths often need auth forwarding and little/no shared caching.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
CloudFront
 ├─ /static/* → private S3
 └─ /api/* → API Gateway/ALB
```

### CLI / Configuration / Calculation

```bash
aws cloudfront list-distributions --output table 2>/dev/null || true
```

### Expected Behavior

Static content achieves high cache hit ratio without caching private API responses incorrectly.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Hashed assets cache for a year; `/api/orders` is not shared-cached.

### Troubleshooting Workflow

```text
wrong content cached
 ↓ path behavior
 ↓ cache policy
 ↓ headers/cookies/query
 ↓ TTL
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design cache behavior by data sensitivity and variability.

---

## Advanced Deep Dive 28 — CloudFront Origin Access

### Concept and Detailed Explanation

Private S3 origin should stay nonpublic while CloudFront has controlled access. Users should not bypass the edge layer directly.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Users
 ↓ CloudFront/WAF
 ↓ signed origin access
 ↓ private S3
```

### CLI / Configuration / Calculation

```bash
aws s3api get-public-access-block --bucket <BUCKET> 2>/dev/null || true
```

### Expected Behavior

CloudFront serves objects but direct unauthenticated S3 URLs fail.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Static assets are protected behind CloudFront.

### Troubleshooting Workflow

```text
CloudFront 403
 ↓ object
 ↓ origin access config
 ↓ bucket policy
 ↓ KMS
 ↓ cache
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Expose the delivery layer, not the origin bucket.

---

## Advanced Deep Dive 29 — WAF Rate Rules

### Concept and Detailed Explanation

Rate-based rules can block abusive patterns before expensive application compute. Tune thresholds using observed legitimate traffic and endpoint sensitivity.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Internet
 ↓ WAF
 normal → app
 abusive → count/block/challenge
```

### CLI / Configuration / Calculation

```bash
aws wafv2 list-web-acls --scope REGIONAL --region <REGION> 2>/dev/null || true
```

### Expected Behavior

Abusive sources are limited before consuming app/database capacity.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Login endpoint uses tighter rate control than static content.

### Troubleshooting Workflow

```text
valid users blocked
 ↓ WAF logs
 ↓ scope-down
 ↓ threshold
 ↓ proxy/IP behavior
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Observe/count before blocking complex traffic patterns.

---

## Advanced Deep Dive 30 — SQS Backpressure for Long Jobs

### Concept and Detailed Explanation

Long or bursty work should be queued and processed asynchronously rather than keeping HTTP requests open.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
POST job
 ↓ return job ID
 ↓ SQS
 ↓ worker
 ↓ result store
 ↓ poll/notification
```

### CLI / Configuration / Calculation

```bash
aws sqs get-queue-attributes --queue-url <URL> --attribute-names ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible 2>/dev/null || true
```

### Expected Behavior

User-facing request returns quickly while workers scale independently.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Report generation returns 202 and processes for 20 minutes in Fargate.

### Troubleshooting Workflow

```text
job latency
 ↓ arrival rate
 ↓ queue age/depth
 ↓ worker throughput
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

Decouple request latency from long-running work.

---

## Advanced Deep Dive 31 — DLQ as Operational Workflow

### Concept and Detailed Explanation

A DLQ needs alarms, retention, secure access, diagnosis, repair, and controlled replay. It is not permanent storage for ignored failures.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
main queue
 ↓ repeated fail
DLQ
 ↓ alert
 ↓ investigate/fix
 ↓ replay
```

### CLI / Configuration / Calculation

```bash
aws sqs get-queue-attributes --queue-url <DLQ> --attribute-names ApproximateNumberOfMessages 2>/dev/null || true
```

### Expected Behavior

Poison messages stop consuming main workers and create actionable incidents.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Malformed event moves to DLQ and is replayed after consumer fix.

### Troubleshooting Workflow

```text
DLQ growing
 ↓ sample safely
 ↓ schema/error class
 ↓ producer/consumer fix
 ↓ redrive
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Alert on DLQ depth for critical workflows.

---

## Advanced Deep Dive 32 — Event Schema Versioning

### Concept and Detailed Explanation

Event-driven services deploy independently, so event contracts need schema versioning and backward-compatibility rules.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
producer
 ↓ event v1/v2
EventBridge/SNS
 ↓ consumers at different versions
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
event_id
event_type
schema_version
aggregate_id
occurred_at
EOF
```

### Expected Behavior

Consumers tolerate compatible additions and migrate deliberately for breaking changes.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Analytics remains on v1 while billing adopts v2.

### Troubleshooting Workflow

```text
consumer parser fails
 ↓ schema version
 ↓ producer release
 ↓ compatibility
 ↓ adapter/replay
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat event schemas like public APIs.

---

## Advanced Deep Dive 33 — Step Functions Retry Classification

### Concept and Detailed Explanation

Retries should address transient faults. Validation/business failures should branch, and side-effect failures may need compensation.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
task
 ├─ timeout/5xx → retry/backoff
 ├─ invalid input → reject
 └─ partial side effect → compensate
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Retry transient only:
IntervalSeconds=2
BackoffRate=2
MaxAttempts=4
EOF
```

### Expected Behavior

Invalid requests do not loop and transient faults recover safely.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Payment 503 retries; insufficient funds does not.

### Troubleshooting Workflow

```text
workflow loops
 ↓ error class
 ↓ retry policy
 ↓ idempotency
 ↓ catch/compensate
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Classify errors before defining retries.

---

## Advanced Deep Dive 34 — Saga Compensation

### Concept and Detailed Explanation

Payment, inventory, shipping, and notification cannot share one ACID transaction. Track side effects and define compensating operations.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
reserve
 ↓ charge
 ↓ shipping fail
 ↓ refund
 ↓ release inventory
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
operation_id
step_status
compensation_status
idempotency_key
EOF
```

### Expected Behavior

Partial failure ends in a known compensated or resumable state.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Payment is refunded if stock finalization fails.

### Troubleshooting Workflow

```text
partial state
 ↓ committed steps
 ↓ idempotency records
 ↓ compensate
 ↓ verify
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design compensation before orchestrating irreversible steps.

---

## Advanced Deep Dive 35 — RDS Connection Pool Math

### Concept and Detailed Explanation

Total DB sessions equal pool size per compute unit multiplied by maximum compute scale. A reasonable pool on one task can become disastrous at 100 tasks.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
N app tasks
 × pool P
 = potential connections
 ↓
DB max - admin headroom
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
tasks=50; pool=20
print(tasks*pool)
PY
```

### Expected Behavior

Maximum possible connections remain below safe DB capacity.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

ECS service scaling would create 1,000 sessions, so pool/proxy settings are reduced.

### Troubleshooting Workflow

```text
DB connections exhausted
 ↓ task/function count
 ↓ pool each
 ↓ RDS Proxy
 ↓ transaction duration
 ↓ max connections
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Capacity-plan DB sessions across maximum compute scale.

---

## Advanced Deep Dive 36 — Backward-Compatible Schema Deployment

### Concept and Detailed Explanation

Rolling, canary, and blue/green releases run old and new code together. Database schema changes must support both until rollback window ends.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
add compatible schema
 ↓ old+new apps run
 ↓ migrate/backfill
 ↓ retire old
 ↓ remove old fields later
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Prefer:
ADD nullable/new column
deploy compatible code
backfill
drop old field later
EOF
```

### Expected Behavior

Blue and Green can coexist and rollback remains possible.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Column rename is implemented through additive migration first.

### Troubleshooting Workflow

```text
rollback breaks
 ↓ schema compatible?
 ↓ mixed versions?
 ↓ data transformed?
 ↓ forward fix/PITR
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Use expand/migrate/contract schema changes.

---

## Advanced Deep Dive 37 — Cache Stampede Protection

### Concept and Detailed Explanation

When a hot key expires, many requests can miss simultaneously and overload the DB. TTL jitter, single-flight refresh, prewarming, or stale-while-revalidate reduce the spike.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
many clients
 ↓ same cache miss
 ↓ DB storm

protected:
one refresh / jitter / stale response
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
TTL = base + random_jitter
single refresher per key
EOF
```

### Expected Behavior

Popular cache expiry does not cause synchronized backend overload.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Product catalog randomizes TTLs and refreshes hot keys in background.

### Troubleshooting Workflow

```text
DB spike after expiry
 ↓ hit ratio
 ↓ same-key expiry
 ↓ TTL
 ↓ refresh strategy
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design cache-miss behavior, not only cache-hit behavior.

---

## Advanced Deep Dive 38 — Multi-Tenant Cache Keys

### Concept and Detailed Explanation

If response varies by tenant or user, cache keys must include trusted tenant context. Missing tenant identity can create a serious data-leak vulnerability.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Tenant A request
 ↓ cache key includes A
Tenant B request
 ↓ different key
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Bad: /orders/123
Better: tenant/acme/orders/123
EOF
```

### Expected Behavior

Cached private data cannot cross tenant boundaries.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Redis keys include tenant ID derived from verified token claims.

### Troubleshooting Workflow

```text
cross-tenant leak
 ↓ cache key
 ↓ auth context
 ↓ purge
 ↓ incident scope
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Treat cache-key design as authorization.

---

## Advanced Deep Dive 39 — Sensitive CDN Caching

### Concept and Detailed Explanation

Authenticated/personalized content should normally avoid shared caching unless the cache key safely varies by user/tenant. Respect Cache-Control and origin policy.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
authenticated request
 ↓ private response
 ↓ no shared cache
or safe user-scoped cache
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Cache-Control: private, no-store
EOF
```

### Expected Behavior

One user's response is never served to another user.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Order history path passes through CloudFront but caching is disabled.

### Troubleshooting Workflow

```text
data leak
 ↓ cache behavior
 ↓ key
 ↓ headers/cookies
 ↓ invalidate/disable
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Default to no shared cache for sensitive personalized APIs.

---

## Advanced Deep Dive 40 — CORS Is Not Authentication

### Concept and Detailed Explanation

CORS is a browser enforcement mechanism. It does not stop curl, scripts, or non-browser clients and cannot protect an API without real authentication/authorization.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Browser
 ↓ CORS response
browser enforces

Non-browser client
 → CORS not a security boundary
```

### CLI / Configuration / Calculation

```bash
curl -i -H 'Origin: https://example.com' https://api.example.com/ 2>/dev/null || true
```

### Expected Behavior

API security remains based on auth, not allowed-origin headers.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

A public endpoint cannot rely on CORS to protect customer data.

### Troubleshooting Workflow

```text
browser CORS error
 ↓ preflight
 ↓ origin/method/header
 ↓ auth separately
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Configure CORS narrowly but secure APIs with identity and authorization.

---

## Advanced Deep Dive 41 — Webhook Signature Verification

### Concept and Detailed Explanation

Inbound webhooks should validate provider-supported signatures, timestamp freshness, raw-body integrity, source context, and event ID deduplication.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
provider
 ↓ signed webhook
API
 ↓ verify
 ↓ idempotency
 ↓ queue/process
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
verify:
signature
timestamp
event_id
expected account/source
EOF
```

### Expected Behavior

Forged and replayed webhook events are rejected.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Payment callback verifies signature before enqueuing update.

### Troubleshooting Workflow

```text
suspicious webhook
 ↓ signature
 ↓ timestamp
 ↓ duplicate event?
 ↓ provider audit
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Never trust a webhook because its URL is secret.

---

## Advanced Deep Dive 42 — Outbound Webhook Queue

### Concept and Detailed Explanation

Your application should not block core transactions on customer webhook availability. Queue delivery, retry with backoff, sign payloads, and DLQ failures.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
business event
 ↓ delivery queue
 ↓ webhook worker
 ↓ customer endpoint
 fail → retry/DLQ
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
event_id
attempt_count
next_attempt
last_status
signature_version
EOF
```

### Expected Behavior

Customer endpoint outage does not break the core transaction.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Order creation succeeds while partner webhook retries asynchronously.

### Troubleshooting Workflow

```text
webhook backlog
 ↓ recipient status
 ↓ retry
 ↓ DLQ
 ↓ disable toxic endpoint
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Decouple outbound webhook delivery from business transactions.

---

## Advanced Deep Dive 43 — Container Resource Sizing

### Concept and Detailed Explanation

CPU/memory requests affect Fargate cost, ECS scheduling, and stability. OOM and CPU throttling require measured right-sizing, not guesswork.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
task CPU/memory
 ↓ scheduler/runtime
 ↓ actual usage
 ↓ right-size
```

### CLI / Configuration / Calculation

```bash
aws ecs describe-task-definition --task-definition <TASKDEF> 2>/dev/null || true
```

### Expected Behavior

Task size covers realistic peak needs with reasonable headroom.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Exit 137 is traced to memory pressure instead of network.

### Troubleshooting Workflow

```text
task crashes
 ↓ exit code
 ↓ memory/CPU metrics
 ↓ leak vs sizing
 ↓ new task size
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Right-size from measured usage and investigate leaks.

---

## Advanced Deep Dive 44 — Fargate vs EC2 Total Economics

### Concept and Detailed Explanation

Fargate reduces node operations; ECS/EC2 can be economical for steady high utilization but adds patching, scaling, bin packing, and node lifecycle. Compare total economics.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
same container
 ├─ Fargate → task billing + low node ops
 └─ EC2 → instance billing + node management
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Compare:
duty cycle
utilization
Spot
special hardware
node ops
engineering labor
EOF
```

### Expected Behavior

Platform choice reflects workload shape and team capacity.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Steady high-density service moves to EC2; burst workers remain Fargate.

### Troubleshooting Workflow

```text
cost high
 ↓ steady/bursty?
 ↓ utilization
 ↓ bin packing
 ↓ ops burden
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Compare operational labor with cloud price.

---

## Advanced Deep Dive 45 — Lambda Memory Price/Performance

### Concept and Detailed Explanation

More Lambda memory can provide more CPU and shorten execution. The cheapest configuration is not necessarily the smallest memory size.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
memory ↑
 CPU ↑
 duration may ↓
 cost per request may ↑ or ↓
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Benchmark:
memory
p50/p95 duration
cost / 1M calls
errors
cold start
EOF
```

### Expected Behavior

Memory is chosen from measured price/performance.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

CPU-heavy parser runs much faster at higher memory and lowers cost/request.

### Troubleshooting Workflow

```text
Lambda slow/expensive
 ↓ duration profile
 ↓ CPU vs I/O wait
 ↓ memory
 ↓ benchmark
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Benchmark memory settings with real workloads.

---

## Advanced Deep Dive 46 — Provisioned Concurrency Economics

### Concept and Detailed Explanation

Provisioned concurrency reduces cold-start latency but adds idle cost. Use only where latency SLO and measured cold-start impact justify it.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
requests
 ↓ preinitialized capacity
 ↓ lower cold start
 but idle cost
```

### CLI / Configuration / Calculation

```bash
aws lambda get-provisioned-concurrency-config --function-name <FUNCTION> --qualifier <ALIAS> 2>/dev/null || true
```

### Expected Behavior

Strict-latency functions have stable startup without warming everything.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Auth callback uses provisioned concurrency; overnight jobs do not.

### Troubleshooting Workflow

```text
cost high
 ↓ provisioned amount
 ↓ actual concurrency
 ↓ cold-start impact
 ↓ resize/schedule
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Pay for warm capacity only where SLO needs it.

---

## Advanced Deep Dive 47 — NAT and Endpoint Cost for Managed Compute

### Concept and Detailed Explanation

Private Lambda/ECS/App Runner can generate significant NAT traffic for S3, ECR, logs, secrets, APIs, and Internet dependencies. VPC endpoints can reduce public/NAT dependency but have their own cost.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
private compute
 ↓ NAT → AWS services/Internet
or
 ↓ endpoints → AWS services
```

### CLI / Configuration / Calculation

```bash
aws ec2 describe-nat-gateways --output table 2>/dev/null || true
aws ec2 describe-vpc-endpoints --output table 2>/dev/null || true
```

### Expected Behavior

Network path cost/security is intentional and measurable.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Fargate tasks use endpoints for ECR/S3/logs/secrets while SaaS traffic uses NAT.

### Troubleshooting Workflow

```text
NAT cost high
 ↓ traffic destination
 ↓ endpoint support
 ↓ cross-AZ
 ↓ interface endpoint cost
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

Model network cost, not only compute cost.

---

## Advanced Deep Dive 48 — Container Image Supply Chain

### Concept and Detailed Explanation

Managed runtime does not make an untrusted image safe. Use controlled base images, pinned dependencies, scanning, provenance/signing where required, and immutable deployment digests.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
source
 ↓ build
 ↓ scan/test
 ↓ ECR digest
 ↓ deployment
```

### CLI / Configuration / Calculation

```bash
aws ecr describe-images --repository-name <REPO> --max-results 20 2>/dev/null || true
```

### Expected Behavior

Every deployed image maps to a source commit and security/test evidence.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Vulnerable base image is rebuilt and all running digests are identified.

### Troubleshooting Workflow

```text
unknown image
 ↓ running digest
 ↓ ECR metadata
 ↓ build provenance
 ↓ base/deps
 ↓ rebuild
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Deploy immutable, traceable artifacts.

---

## Advanced Deep Dive 49 — Application Secret Refresh

### Concept and Detailed Explanation

Long-running tasks should not cache rotated secrets forever. Design refresh TTL/version handling so rotation does not require emergency restart of every process.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Secrets Manager rotates
 ↓ app cache TTL
 ↓ refresh new
 ↓ old retires
```

### CLI / Configuration / Calculation

```bash
aws secretsmanager describe-secret --secret-id <SECRET> 2>/dev/null || true
```

### Expected Behavior

Rotated credentials propagate predictably to long-running services.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

ECS API refreshes DB secret periodically.

### Troubleshooting Workflow

```text
auth fails after rotation
 ↓ current secret
 ↓ provider credential
 ↓ app cache
 ↓ rotation logs
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Design secret refresh before enabling rotation.

---

## Advanced Deep Dive 50 — Structured Logging Correlation

### Concept and Detailed Explanation

Ephemeral managed compute requires centralized logs with request ID, trace ID, service, tenant, deployment version, and error code. Propagate correlation through queues/events.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
client ID
 ↓ API
 ↓ service
 ↓ queue
 ↓ worker
same correlation context
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
{"service":"orders","request_id":"r1","trace_id":"t1","version":"v42","level":"ERROR"}
EOF
```

### Expected Behavior

One request can be followed through synchronous and asynchronous components.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

API and worker logs share the same correlation ID.

### Troubleshooting Workflow

```text
cannot trace
 ↓ ID generated?
 ↓ propagated into events?
 ↓ structured logs?
 ↓ trace context
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Create correlation at ingress and propagate it everywhere.

---

## Advanced Deep Dive 51 — Logging PII and Secret Controls

### Concept and Detailed Explanation

Logs are data stores. Redact authorization headers, cookies, passwords, keys, full payment data, and unnecessary PII.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
request
 ↓ logging middleware
 ↓ redact/drop
 ↓ CloudWatch Logs
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Never log:
Authorization
session cookie
password
private key
secret value
full card data
EOF
```

### Expected Behavior

Logs support diagnosis without becoming a credential/PII leak.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Request ID and customer ID are logged, but bearer token is not.

### Troubleshooting Workflow

```text
secret in logs
 ↓ rotate
 ↓ restrict affected logs
 ↓ fix redaction
 ↓ audit access
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Classify and protect logs like production data.

---

## Advanced Deep Dive 52 — Deployment Version in Telemetry

### Concept and Detailed Explanation

Every release should expose commit/version in logs, traces, health endpoints, and deployment events so regressions correlate immediately.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Git SHA
 ↓ artifact
 ↓ deploy
 ↓ runtime version field
 ↓ logs/metrics/traces
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
APP_VERSION=git-abc123
EOF
```

### Expected Behavior

Errors and latency can be compared by application version.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

5xx begins when canary version reaches 25%.

### Troubleshooting Workflow

```text
regression
 ↓ deployment timeline
 ↓ version-specific metrics
 ↓ rollback/fix
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Make release version a first-class telemetry field.

---

## Advanced Deep Dive 53 — Backward-Compatible Rollback

### Concept and Detailed Explanation

Compute rollback works only if schema, data, secret, and configuration changes remain compatible. Classify rollback feasibility before release.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
new deploy fails
 ↓ old version still compatible?
 yes → rollback
 no → forward fix/PITR
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Rollback checklist:
old artifact retained
schema compatible
config retained
secret versions available
feature flags reversible
EOF
```

### Expected Behavior

Operators know whether rollback is safe.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Old task cannot read new schema, so compute rollback alone is rejected.

### Troubleshooting Workflow

```text
rollback fails
 ↓ schema/data?
 ↓ config/secret?
 ↓ artifact?
 ↓ forward fix/recovery
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Prove reversibility before calling something rollback.

---

## Advanced Deep Dive 54 — Build Once, Promote

### Concept and Detailed Explanation

Rebuilding separately for production creates untested differences. Build one immutable artifact and promote the same digest through environments.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Git commit
 ↓ build once
 ↓ digest
 ↓ staging
 ↓ production
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
staging=sha256:abc
production=sha256:abc
EOF
```

### Expected Behavior

Production runs exactly the artifact tested in staging.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Container digest is promoted, not rebuilt.

### Troubleshooting Workflow

```text
prod differs
 ↓ compare digest/hash
 ↓ pipeline rebuilt?
 ↓ fix promotion
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Build once and promote immutable artifacts.

---

## Advanced Deep Dive 55 — Blue/Green Headroom

### Concept and Detailed Explanation

Blue/green doubles resources temporarily. Quotas, subnet IPs, DB connections, target limits, and cost must support overlap.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Blue full
 + Green full
 ↓ validate
 ↓ shift
 ↓ retire Blue
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
Check:
subnet IP
Fargate/EC2 quota
DB connections
ALB target capacity
temporary cost
EOF
```

### Expected Behavior

Both environments coexist without exhausting dependencies.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Green cannot start because subnet IPs are exhausted.

### Troubleshooting Workflow

```text
blue/green stuck
 ↓ quota
 ↓ subnet IP
 ↓ DB connections
 ↓ target capacity
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Capacity-plan the overlap period.

---

## Advanced Deep Dive 56 — Canary Sample Sufficiency

### Concept and Detailed Explanation

A small traffic percentage is useful only if enough representative requests occur to detect regression. Low-volume services need longer windows or synthetic tests.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
total requests × canary %
 = sample size
 ↓ enough evidence?
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
rph=200; pct=.05
print(rph*pct)
PY
```

### Expected Behavior

Canary observation provides enough sample volume for release metrics.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Low-volume admin API uses synthetic tests and longer canary duration.

### Troubleshooting Workflow

```text
canary looks clean
 ↓ sample size
 ↓ route coverage
 ↓ observation time
 ↓ synthetic validation
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Set canary duration from traffic and risk.

---

## Advanced Deep Dive 57 — Synthetic User Journey

### Concept and Detailed Explanation

Managed platform metrics can be healthy while real login/checkout fails. Synthetic tests validate DNS, TLS, auth, routing, app, and dependencies end-to-end.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
synthetic client
 ↓ Route53/CloudFront/WAF
 ↓ API/app
 ↓ DB/dependency
 ↓ business assertion
```

### CLI / Configuration / Calculation

```bash
curl -fsS -o /dev/null -w '%{http_code} %{time_total}
' https://example.com/health 2>/dev/null || true
```

### Expected Behavior

Critical user paths have external-style monitoring.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Login canary fails after authorizer config change while ECS tasks stay healthy.

### Troubleshooting Workflow

```text
synthetic fail
 ↓ DNS/TLS
 ↓ edge/WAF
 ↓ API/LB
 ↓ app
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

Monitor at least one real business journey.

---

## Advanced Deep Dive 58 — Queue Age as Async SLO

### Concept and Detailed Explanation

For async systems, age of the oldest message often maps more directly to user wait time than queue depth alone.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
job arrives
 ↓ queue wait
 ↓ process
 ↓ result
total async latency
```

### CLI / Configuration / Calculation

```bash
aws sqs get-queue-attributes --queue-url <URL> --attribute-names ApproximateNumberOfMessages 2>/dev/null || true
```

### Expected Behavior

Alerts detect growing user delay before async SLO is breached.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Queue depth is modest but jobs are 20 minutes old because workers are stuck.

### Troubleshooting Workflow

```text
async latency
 ↓ oldest message age
 ↓ worker throughput
 ↓ errors
 ↓ downstream
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Monitor backlog age as well as depth.

---

## Advanced Deep Dive 59 — Managed Platform Quotas

### Concept and Detailed Explanation

PaaS/serverless removes server provisioning but not limits. Lambda concurrency, Fargate capacity, ENIs, API quotas, database connections, and subnet IPs can constrain scale.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
demand
 ↓ managed autoscale
 ↓ platform quota
 ↓ downstream quota
 ↓ real ceiling
```

### CLI / Configuration / Calculation

```bash
aws service-quotas list-services --output table 2>/dev/null | head -50
```

### Expected Behavior

Peak capacity plans include platform and downstream limits.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Lambda hits concurrency quota before DB becomes saturated.

### Troubleshooting Workflow

```text
scale stops
 ↓ service quota
 ↓ subnet IP
 ↓ downstream limit
 ↓ raise/redesign
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Serverless is elastic, not unlimited.

---

## Advanced Deep Dive 60 — Managed Platform DR

### Concept and Detailed Explanation

Regional managed services still require DR when regional outage tolerance is needed. Replicate code/images, IaC, data, secrets, KMS access, certificates, DNS, and quotas.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
Primary Region
 ↓ artifacts/data replicate
DR Region
 ↓ deploy/activate
 ↓ DNS failover
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
DR:
artifact
IaC
data
secret/KMS
certificate
quota
DNS
monitoring
EOF
```

### Expected Behavior

Application platform can activate within business RTO.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Lambda code is in Git but DR fails because secret/KMS/cert were not prepared.

### Troubleshooting Workflow

```text
regional outage
 ↓ platform deploy
 ↓ data
 ↓ keys/secrets
 ↓ DNS/cert
 ↓ business test
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Include every platform dependency in DR.

---

## Advanced Deep Dive 61 — Platform Unit Economics

### Concept and Detailed Explanation

Compare EC2, Fargate, App Runner, Lambda, and Beanstalk using workload shape and cost per business unit plus operational labor.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
platform cost
 ÷ requests/jobs/orders
 = unit cost
 + operations burden
```

### CLI / Configuration / Calculation

```bash
python3 - <<'PY'
monthly=12000
requests=80_000_000
print(monthly/(requests/1_000_000))
PY
```

### Expected Behavior

Platform selection is revisited as traffic shape changes.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

Bursty API remains Lambda while steady 24/7 worker moves to ECS.

### Troubleshooting Workflow

```text
cost high
 ↓ duty cycle
 ↓ unit cost
 ↓ idle
 ↓ network/logging
 ↓ alternate platform
```

### Common Problems

- The architecture satisfies the happy path but not the failure path.
- A broad IAM/network change is used before the failed layer is identified.
- Capacity or service quota is ignored.
- Monitoring proves resource health but not user/business health.
- The recovery procedure is documented but never tested.
- Cost is estimated from one service price instead of the whole request/data path.

### Best Practice

Measure cost per workload unit and total operational effort.

---

## Advanced Deep Dive 62 — Operational Readiness for Managed Services

### Concept and Detailed Explanation

Managed infrastructure still needs ownership, SLOs, dashboards, alarms, tracing, secret rotation, backup/restore, deployment/rollback, quotas, cost controls, and runbooks.

This is a supplemental engineering expansion beyond the uploaded source. Treat the AWS service as an implementation mechanism, not as the requirement itself. For every production decision, record the requirement, assumptions, blast radius, failure mode, validation evidence, recovery path, and cost/security trade-off.

### Architecture / Mental Model

```text
service built
 ↓ operational readiness review
 ↓ production
```

### CLI / Configuration / Calculation

```bash
cat <<'EOF'
[ ] owner/on-call
[ ] SLO
[ ] logs/traces
[ ] alarms
[ ] rollback
[ ] backup/restore
[ ] secret rotation
[ ] quota
[ ] budget
EOF
```

### Expected Behavior

Team can operate the service before customer traffic.

### Why It Works

AWS is built around API-driven control planes and distributed data planes. A successful API call proves that the requested control-plane change was accepted; production validation must still verify routing, identity, resource health, application behavior, data consistency, and observability.

### Production Example

App Runner launch waits until DB restore runbook is complete.

### Troubleshooting Workflow

```text
incident exposes gap
 ↓ which readiness item?
 ↓ assign/fix
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

Managed means less infrastructure toil, not less operational responsibility.

---

# Supplemental Hands-on Lab Series — Amazon PaaS Web Services

## Enhanced Lab 1 — Platform Selection by Hard Constraints

### Objective

Turn **Platform Selection by Hard Constraints** into an evidence-based AWS exercise.

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
runtime=
long_running=
container=
kubernetes=
private_network=
OS_control=
scale_to_zero=
EOF
```

### Expected Result

Platform choice can be explained from hard requirements.

### Troubleshooting Path

```text
platform mismatch
 ↓ violated requirement
 ↓ execution model
 ↓ network/storage
 ↓ operations/cost
 ↓ reselect
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

## Enhanced Lab 2 — Code / Config / Secret Separation

### Objective

Turn **Code / Config / Secret Separation** into an evidence-based AWS exercise.

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
APP_ENV=prod
LOG_LEVEL=INFO
DB_SECRET_ARN=arn:aws:secretsmanager:...
EOF
```

### Expected Result

Production uses the same artifact as staging while secrets never enter Git.

### Troubleshooting Path

```text
wrong config/secret leak
 ↓ where stored?
 ↓ image/Git?
 ↓ environment?
 ↓ secret manager?
 ↓ rotate/fix
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

## Enhanced Lab 3 — Stateless Compute

### Objective

Turn **Stateless Compute** into an evidence-based AWS exercise.

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
Do not store unique durable state in:
container layer
instance local disk
process memory
Lambda /tmp
EOF
```

### Expected Result

Any compute unit can terminate without data loss.

### Troubleshooting Path

```text
replacement loses state
 ↓ identify local state
 ↓ durable vs cache
 ↓ move externally
 ↓ termination test
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

## Enhanced Lab 4 — Liveness vs Readiness

### Objective

Turn **Liveness vs Readiness** into an evidence-based AWS exercise.

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
curl -fsS http://127.0.0.1:8080/health
curl -fsS http://127.0.0.1:8080/ready
```

### Expected Result

Unready instances drain while healthy capacity stays available.

### Troubleshooting Path

```text
health flaps
 ↓ endpoint speed
 ↓ dependency choices
 ↓ timeout/threshold
 ↓ startup grace
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

## Enhanced Lab 5 — Graceful Shutdown

### Objective

Turn **Graceful Shutdown** into an evidence-based AWS exercise.

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
SIGTERM:
stop polling
stop accepting
wait bounded
close DB
exit
EOF
```

### Expected Result

In-flight requests/jobs survive normal deployments.

### Troubleshooting Path

```text
dropped work
 ↓ signal handled?
 ↓ ALB deregistration
 ↓ queue ack
 ↓ shutdown deadline
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

## Enhanced Lab 6 — Beanstalk Blue/Green

### Objective

Turn **Beanstalk Blue/Green** into an evidence-based AWS exercise.

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
eb status 2>/dev/null || true
eb health 2>/dev/null || true
```

### Expected Result

Green passes business/health checks before production traffic moves.

### Troubleshooting Path

```text
post-swap errors
 ↓ green health
 ↓ schema compatibility
 ↓ config/secrets
 ↓ swap back if safe
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

## Enhanced Lab 7 — Beanstalk Platform Lifecycle

### Objective

Turn **Beanstalk Platform Lifecycle** into an evidence-based AWS exercise.

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
eb platform list 2>/dev/null || true
```

### Expected Result

Production remains on supported platform versions.

### Troubleshooting Path

```text
upgrade fail
 ↓ runtime version
 ↓ dependencies
 ↓ hooks/config
 ↓ health
 ↓ rollback/fix
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

## Enhanced Lab 8 — App Runner Build vs Runtime Identity

### Objective

Turn **App Runner Build vs Runtime Identity** into an evidence-based AWS exercise.

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
aws apprunner list-services 2>/dev/null || true
```

### Expected Result

Build/deploy and runtime use separate least-privilege roles.

### Troubleshooting Path

```text
AccessDenied
 ↓ build or runtime?
 ↓ ECR/source role
 ↓ instance role
 ↓ resource/KMS policy
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

## Enhanced Lab 9 — App Runner VPC Connector

### Objective

Turn **App Runner VPC Connector** into an evidence-based AWS exercise.

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
aws apprunner list-vpc-connectors 2>/dev/null || true
```

### Expected Result

App reaches private dependencies without exposing them publicly.

### Troubleshooting Path

```text
outbound fail
 ↓ connector subnets
 ↓ SG
 ↓ route
 ↓ NAT/endpoints
 ↓ DNS
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

## Enhanced Lab 10 — ECS Task Definition Immutability

### Objective

Turn **ECS Task Definition Immutability** into an evidence-based AWS exercise.

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
aws ecs list-task-definitions --sort DESC --max-items 20 2>/dev/null || true
```

### Expected Result

Every running task maps to an exact artifact and configuration revision.

### Troubleshooting Path

```text
unknown version
 ↓ task revision
 ↓ image digest
 ↓ build metadata
 ↓ correct deployment
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

## Enhanced Lab 11 — Task Role vs Execution Role

### Objective

Turn **Task Role vs Execution Role** into an evidence-based AWS exercise.

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
aws ecs describe-task-definition --task-definition <TASKDEF> 2>/dev/null || true
```

### Expected Result

Image/startup failures and application API failures are separated.

### Troubleshooting Path

```text
permission failure
 ↓ before start? execution role
 ↓ after app start? task role
 ↓ resource/KMS/SCP
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

## Enhanced Lab 12 — ECS awsvpc Subnet Capacity

### Objective

Turn **ECS awsvpc Subnet Capacity** into an evidence-based AWS exercise.

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
aws ec2 describe-subnets --query 'Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone,Free:AvailableIpAddressCount}' --output table
```

### Expected Result

Task subnets support maximum scale plus rolling/blue-green overlap.

### Troubleshooting Path

```text
placement fail
 ↓ free IPs
 ↓ AZ
 ↓ other ENIs/endpoints
 ↓ new/larger subnet
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

## Enhanced Lab 13 — ECS Deployment Surge

### Objective

Turn **ECS Deployment Surge** into an evidence-based AWS exercise.

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
aws ecs describe-services --cluster <CLUSTER> --services <SERVICE> 2>/dev/null || true
```

### Expected Result

Deployment preserves serving capacity without exhausting IP/quota/DB headroom.

### Troubleshooting Path

```text
deployment stuck
 ↓ desired/running/pending
 ↓ min/max
 ↓ IP/quota
 ↓ health
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

## Enhanced Lab 14 — EKS Selection Gate

### Objective

Turn **EKS Selection Gate** into an evidence-based AWS exercise.

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
aws eks list-clusters --output table 2>/dev/null || true
```

### Expected Result

Kubernetes is chosen because a concrete capability requires it.

### Troubleshooting Path

```text
platform too complex
 ↓ which K8s capability used?
 ↓ simpler service possible?
 ↓ team skill/ops
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

## Enhanced Lab 15 — Lambda Initialization Reuse

### Objective

Turn **Lambda Initialization Reuse** into an evidence-based AWS exercise.

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
cat <<'PY'
import boto3
s3=boto3.client("s3")
def handler(event,context):
    return {"ok":True}
PY
```

### Expected Result

Cold initialization is reduced while function remains correct on every fresh environment.

### Troubleshooting Path

```text
intermittent connection
 ↓ init location
 ↓ warm reuse?
 ↓ stale client
 ↓ retry/recreate
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

## Enhanced Lab 16 — Lambda /tmp Semantics

### Objective

Turn **Lambda /tmp Semantics** into an evidence-based AWS exercise.

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
from pathlib import Path
p=Path('/tmp/demo.txt');p.write_text('scratch');print(p.read_text())
PY
```

### Expected Result

Function remains correct even when `/tmp` starts empty.

### Troubleshooting Path

```text
file missing
 ↓ assumed warm reuse?
 ↓ retrieve source from durable store
 ↓ persist output externally
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

## Enhanced Lab 17 — Lambda Concurrency Protects RDS

### Objective

Turn **Lambda Concurrency Protects RDS** into an evidence-based AWS exercise.

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
aws lambda get-function-concurrency --function-name <FUNCTION> 2>/dev/null || true
aws rds describe-db-proxies --output table 2>/dev/null || true
```

### Expected Result

Serverless burst does not exhaust DB connections.

### Troubleshooting Path

```text
DB connections exhausted
 ↓ Lambda concurrency
 ↓ proxy/pool
 ↓ transaction duration
 ↓ DB max
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

## Enhanced Lab 18 — Lambda Idempotency

### Objective

Turn **Lambda Idempotency** into an evidence-based AWS exercise.

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
DynamoDB condition:
attribute_not_exists(request_id)
EOF
```

### Expected Result

Duplicate events create one business effect.

### Troubleshooting Path

```text
duplicate effect
 ↓ event ID
 ↓ idempotency store
 ↓ transaction boundary
 ↓ acknowledgement
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

## Enhanced Lab 19 — Lambda Batch Failure Isolation

### Objective

Turn **Lambda Batch Failure Isolation** into an evidence-based AWS exercise.

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
aws lambda list-event-source-mappings --function-name <FUNCTION> 2>/dev/null || true
```

### Expected Result

One bad record does not repeatedly process an entire successful batch.

### Troubleshooting Path

```text
batch loops
 ↓ failed record
 ↓ partial response
 ↓ DLQ
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

## Enhanced Lab 20 — Lambda Alias Canary

### Objective

Turn **Lambda Alias Canary** into an evidence-based AWS exercise.

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
aws lambda get-alias --function-name <FUNCTION> --name prod 2>/dev/null || true
```

### Expected Result

New version receives bounded traffic and is promoted only after gates pass.

### Troubleshooting Path

```text
canary bad
 ↓ version metrics/logs
 ↓ alias weight
 ↓ rollback
 ↓ fix
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

## Enhanced Lab 21 — API Gateway HTTP vs REST

### Objective

Turn **API Gateway HTTP vs REST** into an evidence-based AWS exercise.

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
aws apigatewayv2 get-apis --output table 2>/dev/null || true
aws apigateway get-rest-apis --output table 2>/dev/null || true
```

### Expected Result

API type provides necessary features without unnecessary complexity.

### Troubleshooting Path

```text
feature missing
 ↓ API type
 ↓ required capability
 ↓ auth/integration
 ↓ migrate if needed
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

## Enhanced Lab 22 — API Private Integration

### Objective

Turn **API Private Integration** into an evidence-based AWS exercise.

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
aws apigatewayv2 get-vpc-links --output table 2>/dev/null || true
```

### Expected Result

Public API front door reaches private services without direct backend Internet exposure.

### Troubleshooting Path

```text
private integration 5xx
 ↓ VPC link
 ↓ LB target health
 ↓ SG/route
 ↓ app port
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

## Enhanced Lab 23 — API Authentication vs Object Authorization

### Objective

Turn **API Authentication vs Object Authorization** into an evidence-based AWS exercise.

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
trusted claim: tenant_id
request path: /orders/{id}
backend verifies order.tenant_id == token.tenant_id
EOF
```

### Expected Result

One tenant cannot read another tenant's resource by changing URL IDs.

### Troubleshooting Path

```text
403/possible data leak
 ↓ token valid
 ↓ scope
 ↓ object ownership
 ↓ tenant context
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

## Enhanced Lab 24 — Idempotent POST

### Objective

Turn **Idempotent POST** into an evidence-based AWS exercise.

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
Idempotency-Key: unique request UUID
Scope: caller + operation
TTL: business-defined
EOF
```

### Expected Result

Repeated client retries create one order/charge.

### Troubleshooting Path

```text
duplicate POST
 ↓ same key?
 ↓ stored payload/result
 ↓ payload mismatch?
 ↓ return prior/conflict
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

## Enhanced Lab 25 — API Backpressure

### Objective

Turn **API Backpressure** into an evidence-based AWS exercise.

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
aws apigateway get-usage-plans --output table 2>/dev/null || true
```

### Expected Result

Excess demand is rejected/buffered before DB or Lambda collapse.

### Troubleshooting Path

```text
429/5xx
 ↓ edge throttle
 ↓ compute concurrency
 ↓ DB/API limits
 ↓ client retry
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

## Enhanced Lab 26 — WebSocket Connection Lifecycle

### Objective

Turn **WebSocket Connection Lifecycle** into an evidence-based AWS exercise.

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
connection_id
user_id
connected_at
expires_at
EOF
```

### Expected Result

Disconnected clients do not produce repeated failed sends.

### Troubleshooting Path

```text
send fails
 ↓ connection exists?
 ↓ client gone?
 ↓ delete stale state
 ↓ reconnect
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

## Enhanced Lab 27 — CloudFront Multi-Origin

### Objective

Turn **CloudFront Multi-Origin** into an evidence-based AWS exercise.

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

Static content achieves high cache hit ratio without caching private API responses incorrectly.

### Troubleshooting Path

```text
wrong content cached
 ↓ path behavior
 ↓ cache policy
 ↓ headers/cookies/query
 ↓ TTL
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

## Enhanced Lab 28 — CloudFront Origin Access

### Objective

Turn **CloudFront Origin Access** into an evidence-based AWS exercise.

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
```

### Expected Result

CloudFront serves objects but direct unauthenticated S3 URLs fail.

### Troubleshooting Path

```text
CloudFront 403
 ↓ object
 ↓ origin access config
 ↓ bucket policy
 ↓ KMS
 ↓ cache
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

## Enhanced Lab 29 — WAF Rate Rules

### Objective

Turn **WAF Rate Rules** into an evidence-based AWS exercise.

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
aws wafv2 list-web-acls --scope REGIONAL --region <REGION> 2>/dev/null || true
```

### Expected Result

Abusive sources are limited before consuming app/database capacity.

### Troubleshooting Path

```text
valid users blocked
 ↓ WAF logs
 ↓ scope-down
 ↓ threshold
 ↓ proxy/IP behavior
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

## Enhanced Lab 30 — SQS Backpressure for Long Jobs

### Objective

Turn **SQS Backpressure for Long Jobs** into an evidence-based AWS exercise.

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
aws sqs get-queue-attributes --queue-url <URL> --attribute-names ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible 2>/dev/null || true
```

### Expected Result

User-facing request returns quickly while workers scale independently.

### Troubleshooting Path

```text
job latency
 ↓ arrival rate
 ↓ queue age/depth
 ↓ worker throughput
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

## Enhanced Lab 31 — DLQ as Operational Workflow

### Objective

Turn **DLQ as Operational Workflow** into an evidence-based AWS exercise.

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
aws sqs get-queue-attributes --queue-url <DLQ> --attribute-names ApproximateNumberOfMessages 2>/dev/null || true
```

### Expected Result

Poison messages stop consuming main workers and create actionable incidents.

### Troubleshooting Path

```text
DLQ growing
 ↓ sample safely
 ↓ schema/error class
 ↓ producer/consumer fix
 ↓ redrive
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

## Enhanced Lab 32 — Event Schema Versioning

### Objective

Turn **Event Schema Versioning** into an evidence-based AWS exercise.

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
event_id
event_type
schema_version
aggregate_id
occurred_at
EOF
```

### Expected Result

Consumers tolerate compatible additions and migrate deliberately for breaking changes.

### Troubleshooting Path

```text
consumer parser fails
 ↓ schema version
 ↓ producer release
 ↓ compatibility
 ↓ adapter/replay
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

## Enhanced Lab 33 — Step Functions Retry Classification

### Objective

Turn **Step Functions Retry Classification** into an evidence-based AWS exercise.

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
Retry transient only:
IntervalSeconds=2
BackoffRate=2
MaxAttempts=4
EOF
```

### Expected Result

Invalid requests do not loop and transient faults recover safely.

### Troubleshooting Path

```text
workflow loops
 ↓ error class
 ↓ retry policy
 ↓ idempotency
 ↓ catch/compensate
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

## Enhanced Lab 34 — Saga Compensation

### Objective

Turn **Saga Compensation** into an evidence-based AWS exercise.

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
operation_id
step_status
compensation_status
idempotency_key
EOF
```

### Expected Result

Partial failure ends in a known compensated or resumable state.

### Troubleshooting Path

```text
partial state
 ↓ committed steps
 ↓ idempotency records
 ↓ compensate
 ↓ verify
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

## Enhanced Lab 35 — RDS Connection Pool Math

### Objective

Turn **RDS Connection Pool Math** into an evidence-based AWS exercise.

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
tasks=50; pool=20
print(tasks*pool)
PY
```

### Expected Result

Maximum possible connections remain below safe DB capacity.

### Troubleshooting Path

```text
DB connections exhausted
 ↓ task/function count
 ↓ pool each
 ↓ RDS Proxy
 ↓ transaction duration
 ↓ max connections
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

## Enhanced Lab 36 — Backward-Compatible Schema Deployment

### Objective

Turn **Backward-Compatible Schema Deployment** into an evidence-based AWS exercise.

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
Prefer:
ADD nullable/new column
deploy compatible code
backfill
drop old field later
EOF
```

### Expected Result

Blue and Green can coexist and rollback remains possible.

### Troubleshooting Path

```text
rollback breaks
 ↓ schema compatible?
 ↓ mixed versions?
 ↓ data transformed?
 ↓ forward fix/PITR
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

## Enhanced Lab 37 — Cache Stampede Protection

### Objective

Turn **Cache Stampede Protection** into an evidence-based AWS exercise.

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
TTL = base + random_jitter
single refresher per key
EOF
```

### Expected Result

Popular cache expiry does not cause synchronized backend overload.

### Troubleshooting Path

```text
DB spike after expiry
 ↓ hit ratio
 ↓ same-key expiry
 ↓ TTL
 ↓ refresh strategy
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

## Enhanced Lab 38 — Multi-Tenant Cache Keys

### Objective

Turn **Multi-Tenant Cache Keys** into an evidence-based AWS exercise.

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
Bad: /orders/123
Better: tenant/acme/orders/123
EOF
```

### Expected Result

Cached private data cannot cross tenant boundaries.

### Troubleshooting Path

```text
cross-tenant leak
 ↓ cache key
 ↓ auth context
 ↓ purge
 ↓ incident scope
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

## Enhanced Lab 39 — Sensitive CDN Caching

### Objective

Turn **Sensitive CDN Caching** into an evidence-based AWS exercise.

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
Cache-Control: private, no-store
EOF
```

### Expected Result

One user's response is never served to another user.

### Troubleshooting Path

```text
data leak
 ↓ cache behavior
 ↓ key
 ↓ headers/cookies
 ↓ invalidate/disable
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

## Enhanced Lab 40 — CORS Is Not Authentication

### Objective

Turn **CORS Is Not Authentication** into an evidence-based AWS exercise.

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
curl -i -H 'Origin: https://example.com' https://api.example.com/ 2>/dev/null || true
```

### Expected Result

API security remains based on auth, not allowed-origin headers.

### Troubleshooting Path

```text
browser CORS error
 ↓ preflight
 ↓ origin/method/header
 ↓ auth separately
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

## Enhanced Lab 41 — Webhook Signature Verification

### Objective

Turn **Webhook Signature Verification** into an evidence-based AWS exercise.

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
verify:
signature
timestamp
event_id
expected account/source
EOF
```

### Expected Result

Forged and replayed webhook events are rejected.

### Troubleshooting Path

```text
suspicious webhook
 ↓ signature
 ↓ timestamp
 ↓ duplicate event?
 ↓ provider audit
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

## Enhanced Lab 42 — Outbound Webhook Queue

### Objective

Turn **Outbound Webhook Queue** into an evidence-based AWS exercise.

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
event_id
attempt_count
next_attempt
last_status
signature_version
EOF
```

### Expected Result

Customer endpoint outage does not break the core transaction.

### Troubleshooting Path

```text
webhook backlog
 ↓ recipient status
 ↓ retry
 ↓ DLQ
 ↓ disable toxic endpoint
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

## Enhanced Lab 43 — Container Resource Sizing

### Objective

Turn **Container Resource Sizing** into an evidence-based AWS exercise.

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
aws ecs describe-task-definition --task-definition <TASKDEF> 2>/dev/null || true
```

### Expected Result

Task size covers realistic peak needs with reasonable headroom.

### Troubleshooting Path

```text
task crashes
 ↓ exit code
 ↓ memory/CPU metrics
 ↓ leak vs sizing
 ↓ new task size
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

## Enhanced Lab 44 — Fargate vs EC2 Total Economics

### Objective

Turn **Fargate vs EC2 Total Economics** into an evidence-based AWS exercise.

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
Compare:
duty cycle
utilization
Spot
special hardware
node ops
engineering labor
EOF
```

### Expected Result

Platform choice reflects workload shape and team capacity.

### Troubleshooting Path

```text
cost high
 ↓ steady/bursty?
 ↓ utilization
 ↓ bin packing
 ↓ ops burden
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

## Enhanced Lab 45 — Lambda Memory Price/Performance

### Objective

Turn **Lambda Memory Price/Performance** into an evidence-based AWS exercise.

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
Benchmark:
memory
p50/p95 duration
cost / 1M calls
errors
cold start
EOF
```

### Expected Result

Memory is chosen from measured price/performance.

### Troubleshooting Path

```text
Lambda slow/expensive
 ↓ duration profile
 ↓ CPU vs I/O wait
 ↓ memory
 ↓ benchmark
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

## Enhanced Lab 46 — Provisioned Concurrency Economics

### Objective

Turn **Provisioned Concurrency Economics** into an evidence-based AWS exercise.

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
aws lambda get-provisioned-concurrency-config --function-name <FUNCTION> --qualifier <ALIAS> 2>/dev/null || true
```

### Expected Result

Strict-latency functions have stable startup without warming everything.

### Troubleshooting Path

```text
cost high
 ↓ provisioned amount
 ↓ actual concurrency
 ↓ cold-start impact
 ↓ resize/schedule
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

## Enhanced Lab 47 — NAT and Endpoint Cost for Managed Compute

### Objective

Turn **NAT and Endpoint Cost for Managed Compute** into an evidence-based AWS exercise.

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
aws ec2 describe-nat-gateways --output table 2>/dev/null || true
aws ec2 describe-vpc-endpoints --output table 2>/dev/null || true
```

### Expected Result

Network path cost/security is intentional and measurable.

### Troubleshooting Path

```text
NAT cost high
 ↓ traffic destination
 ↓ endpoint support
 ↓ cross-AZ
 ↓ interface endpoint cost
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

## Enhanced Lab 48 — Container Image Supply Chain

### Objective

Turn **Container Image Supply Chain** into an evidence-based AWS exercise.

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
aws ecr describe-images --repository-name <REPO> --max-results 20 2>/dev/null || true
```

### Expected Result

Every deployed image maps to a source commit and security/test evidence.

### Troubleshooting Path

```text
unknown image
 ↓ running digest
 ↓ ECR metadata
 ↓ build provenance
 ↓ base/deps
 ↓ rebuild
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

## Enhanced Lab 49 — Application Secret Refresh

### Objective

Turn **Application Secret Refresh** into an evidence-based AWS exercise.

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
aws secretsmanager describe-secret --secret-id <SECRET> 2>/dev/null || true
```

### Expected Result

Rotated credentials propagate predictably to long-running services.

### Troubleshooting Path

```text
auth fails after rotation
 ↓ current secret
 ↓ provider credential
 ↓ app cache
 ↓ rotation logs
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

## Enhanced Lab 50 — Structured Logging Correlation

### Objective

Turn **Structured Logging Correlation** into an evidence-based AWS exercise.

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
{"service":"orders","request_id":"r1","trace_id":"t1","version":"v42","level":"ERROR"}
EOF
```

### Expected Result

One request can be followed through synchronous and asynchronous components.

### Troubleshooting Path

```text
cannot trace
 ↓ ID generated?
 ↓ propagated into events?
 ↓ structured logs?
 ↓ trace context
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

## Enhanced Lab 51 — Logging PII and Secret Controls

### Objective

Turn **Logging PII and Secret Controls** into an evidence-based AWS exercise.

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
Never log:
Authorization
session cookie
password
private key
secret value
full card data
EOF
```

### Expected Result

Logs support diagnosis without becoming a credential/PII leak.

### Troubleshooting Path

```text
secret in logs
 ↓ rotate
 ↓ restrict affected logs
 ↓ fix redaction
 ↓ audit access
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

## Enhanced Lab 52 — Deployment Version in Telemetry

### Objective

Turn **Deployment Version in Telemetry** into an evidence-based AWS exercise.

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
APP_VERSION=git-abc123
EOF
```

### Expected Result

Errors and latency can be compared by application version.

### Troubleshooting Path

```text
regression
 ↓ deployment timeline
 ↓ version-specific metrics
 ↓ rollback/fix
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

## Enhanced Lab 53 — Backward-Compatible Rollback

### Objective

Turn **Backward-Compatible Rollback** into an evidence-based AWS exercise.

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
Rollback checklist:
old artifact retained
schema compatible
config retained
secret versions available
feature flags reversible
EOF
```

### Expected Result

Operators know whether rollback is safe.

### Troubleshooting Path

```text
rollback fails
 ↓ schema/data?
 ↓ config/secret?
 ↓ artifact?
 ↓ forward fix/recovery
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

## Enhanced Lab 54 — Build Once, Promote

### Objective

Turn **Build Once, Promote** into an evidence-based AWS exercise.

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
staging=sha256:abc
production=sha256:abc
EOF
```

### Expected Result

Production runs exactly the artifact tested in staging.

### Troubleshooting Path

```text
prod differs
 ↓ compare digest/hash
 ↓ pipeline rebuilt?
 ↓ fix promotion
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

## Enhanced Lab 55 — Blue/Green Headroom

### Objective

Turn **Blue/Green Headroom** into an evidence-based AWS exercise.

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
Check:
subnet IP
Fargate/EC2 quota
DB connections
ALB target capacity
temporary cost
EOF
```

### Expected Result

Both environments coexist without exhausting dependencies.

### Troubleshooting Path

```text
blue/green stuck
 ↓ quota
 ↓ subnet IP
 ↓ DB connections
 ↓ target capacity
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

## Enhanced Lab 56 — Canary Sample Sufficiency

### Objective

Turn **Canary Sample Sufficiency** into an evidence-based AWS exercise.

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
rph=200; pct=.05
print(rph*pct)
PY
```

### Expected Result

Canary observation provides enough sample volume for release metrics.

### Troubleshooting Path

```text
canary looks clean
 ↓ sample size
 ↓ route coverage
 ↓ observation time
 ↓ synthetic validation
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

## Enhanced Lab 57 — Synthetic User Journey

### Objective

Turn **Synthetic User Journey** into an evidence-based AWS exercise.

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
curl -fsS -o /dev/null -w '%{http_code} %{time_total}
' https://example.com/health 2>/dev/null || true
```

### Expected Result

Critical user paths have external-style monitoring.

### Troubleshooting Path

```text
synthetic fail
 ↓ DNS/TLS
 ↓ edge/WAF
 ↓ API/LB
 ↓ app
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

## Enhanced Lab 58 — Queue Age as Async SLO

### Objective

Turn **Queue Age as Async SLO** into an evidence-based AWS exercise.

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
aws sqs get-queue-attributes --queue-url <URL> --attribute-names ApproximateNumberOfMessages 2>/dev/null || true
```

### Expected Result

Alerts detect growing user delay before async SLO is breached.

### Troubleshooting Path

```text
async latency
 ↓ oldest message age
 ↓ worker throughput
 ↓ errors
 ↓ downstream
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

## Enhanced Lab 59 — Managed Platform Quotas

### Objective

Turn **Managed Platform Quotas** into an evidence-based AWS exercise.

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
aws service-quotas list-services --output table 2>/dev/null | head -50
```

### Expected Result

Peak capacity plans include platform and downstream limits.

### Troubleshooting Path

```text
scale stops
 ↓ service quota
 ↓ subnet IP
 ↓ downstream limit
 ↓ raise/redesign
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

## Enhanced Lab 60 — Managed Platform DR

### Objective

Turn **Managed Platform DR** into an evidence-based AWS exercise.

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
DR:
artifact
IaC
data
secret/KMS
certificate
quota
DNS
monitoring
EOF
```

### Expected Result

Application platform can activate within business RTO.

### Troubleshooting Path

```text
regional outage
 ↓ platform deploy
 ↓ data
 ↓ keys/secrets
 ↓ DNS/cert
 ↓ business test
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

## Enhanced Lab 61 — Platform Unit Economics

### Objective

Turn **Platform Unit Economics** into an evidence-based AWS exercise.

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
monthly=12000
requests=80_000_000
print(monthly/(requests/1_000_000))
PY
```

### Expected Result

Platform selection is revisited as traffic shape changes.

### Troubleshooting Path

```text
cost high
 ↓ duty cycle
 ↓ unit cost
 ↓ idle
 ↓ network/logging
 ↓ alternate platform
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

## Enhanced Lab 62 — Operational Readiness for Managed Services

### Objective

Turn **Operational Readiness for Managed Services** into an evidence-based AWS exercise.

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
[ ] owner/on-call
[ ] SLO
[ ] logs/traces
[ ] alarms
[ ] rollback
[ ] backup/restore
[ ] secret rotation
[ ] quota
[ ] budget
EOF
```

### Expected Result

Team can operate the service before customer traffic.

### Troubleshooting Path

```text
incident exposes gap
 ↓ which readiness item?
 ↓ assign/fix
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

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Platform Selection Matrix

Compare:

```text
EC2
Elastic Beanstalk
App Runner
ECS/EC2
ECS/Fargate
EKS
Lambda
```

Columns:

```text
OS control
container
Kubernetes
server management
autoscaling
event-driven
long-running
operational overhead
```

### Lab 2 — Simple Web Application

Create a small Python Flask or FastAPI app:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "web-platform-lab"}

@app.get("/health")
def health():
    return {"status": "ok"}
```

Add `requirements.txt`.

### Lab 3 — Twelve-Factor Configuration

Move:

```text
APP_ENV
LOG_LEVEL
DATABASE_URL reference
```

out of source code.

Do not store secrets in Git.

### Lab 4 — Elastic Beanstalk Architecture

Draw:

```text
Route53
 ↓
ALB
 ↓
Beanstalk ASG EC2
 ↓
RDS
```

Place EC2/RDS in private subnets.

### Lab 5 — EB CLI Workflow

In a sandbox:

```bash
eb init
eb create
eb status
eb health
eb deploy
```

Record which AWS resources Beanstalk created.

Clean up.

### Lab 6 — Beanstalk Deployment Policies

Tabletop:

```text
all-at-once
rolling
rolling + extra batch
immutable
traffic splitting
```

Choose for dev vs critical production.

### Lab 7 — Beanstalk Blue/Green

Design:

```text
blue-prod
green-prod
```

Define:

```text
deployment
validation
CNAME swap
rollback
```

### Lab 8 — App Runner Source Deployment

Deploy a simple web app from a supported source repository or tabletop the workflow:

```text
repository
 ↓
build
 ↓
App Runner
 ↓
HTTPS endpoint
```

### Lab 9 — App Runner Container

Containerize the lab app:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

Push to ECR and design App Runner deployment.

### Lab 10 — App Runner Private Database

Design:

```text
App Runner
 ↓ VPC Connector
Private RDS
```

Include security groups and secret retrieval.

### Lab 11 — ECS Task Definition

Create conceptual task:

```text
image
CPU
memory
port 8080
execution role
task role
CloudWatch Logs
secret reference
```

### Lab 12 — ECS Fargate Service

Design:

```text
ALB
 ↓
ECS Service
├─ Fargate Task A
└─ Fargate Task B
```

across two AZs.

### Lab 13 — ECS Task Role vs Execution Role

Create permission table:

```text
pull ECR → execution role
write logs → execution role
read app S3 → task role
read DynamoDB → task role
```

### Lab 14 — ECS Auto Scaling

Scale from:

```text
2 → 20 tasks
```

using:

```text
CPU
or
ALB requests per target
```

Explain downstream database capacity.

### Lab 15 — ECS Failed Deployment

Intentionally use incorrect health path in a sandbox/tabletop.

Trace:

```text
ECS event
ALB target
container log
health response
```

### Lab 16 — EKS Decision

For five workloads decide:

```text
ECS
EKS
App Runner
```

Use Kubernetes only where requirements justify it.

### Lab 17 — Lambda Function

Create:

```python
import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "hello"})
    }
```

Deploy in sandbox or package locally.

### Lab 18 — Lambda Environment and Secret

Use:

```text
APP_ENV → environment variable
DB_PASSWORD → Secrets Manager reference
```

Explain why they differ.

### Lab 19 — Lambda Concurrency

Scenario:

```text
10,000 API requests
DB max connections 200
```

Design:

```text
reserved concurrency
RDS Proxy
queue
```

to protect database.

### Lab 20 — SQS + Lambda

Architecture:

```text
API
 ↓
SQS
 ↓
Lambda
```

Configure conceptual:

```text
batch
visibility timeout
DLQ
retry
```

### Lab 21 — API Gateway + Lambda

Build:

```text
GET /orders/{id}
 ↓
API Gateway
 ↓
Lambda
 ↓
DynamoDB
```

Define authentication and logging.

### Lab 22 — HTTP API vs REST API

Create requirements:

```text
simple JWT API
advanced API keys/caching/transforms
```

Choose the appropriate API type.

### Lab 23 — WebSocket Design

Create:

```text
client
 ↔
API Gateway WebSocket
 ↓
Lambda
 ↓
DynamoDB connections
```

for a status dashboard.

### Lab 24 — CloudFront Multi-Origin

Design:

```text
/static/* → S3
/api/* → API Gateway
```

Add WAF and ACM.

### Lab 25 — Async Long Job

Requirement:

```text
video-processing job = 45 minutes
```

Do not use one Lambda.

Design:

```text
API Gateway
 ↓
SQS
 ↓
Fargate/Batch
 ↓
S3
```

### Lab 26 — Step Functions Workflow

Model:

```text
validate order
 ↓
charge
 ↓
reserve stock
 ↓
notify
```

Add retries and compensation path.

### Lab 27 — Observability

For each platform create:

```text
5 metrics
5 logs
3 alarms
1 trace path
1 dashboard
```

### Lab 28 — Deployment Strategy

For:

```text
Beanstalk
ECS
Lambda
```

design:

```text
canary
blue/green
rollback
health threshold
```

### Lab 29 — Cost Comparison

Using fictional unit prices, compare:

```text
EC2
Fargate
App Runner
Lambda
```

for:

```text
constant high traffic
bursty traffic
long-running worker
rare event function
```

### Lab 30 — Platform Troubleshooting Challenge

Diagnose:

```text
Beanstalk red health
App Runner build failed
ECS image pull failed
ECS target unhealthy
Lambda timeout
Lambda throttle
API 403
API 502
SQS backlog
secret access denied
```

For each:

```text
Evidence
Layer
Root Cause
Fix
Verification
Prevention
```

---

## 6. Mini Project

# Mini Project — Managed AWS Web Platform

Build/design an online customer portal.

Requirements:

```text
10,000 daily users
1,000 concurrent peak
REST API
background report generation
file uploads
customer login
relational orders database
global static assets
production + staging
zero-downtime deployments
```

## Front Door

```text
Route 53
 ↓
CloudFront
 ↓
AWS WAF
```

## Web/API Platform

Compare and select:

```text
Elastic Beanstalk
App Runner
ECS/Fargate
Lambda/API Gateway
```

You may intentionally use more than one:

```text
Web app → App Runner/ECS
API → API Gateway/Lambda
Worker → Fargate
```

## Data

```text
RDS/Aurora → orders
DynamoDB → optional high-scale metadata
ElastiCache → sessions/cache
S3 → files/static assets
```

## Async

```text
API
 ↓
SQS
 ↓
Worker
```

and:

```text
Domain Event
 ↓
EventBridge/SNS
 ↓
Consumers
```

## Security

```text
IAM roles
Cognito/user auth if justified
Secrets Manager
KMS
ACM
WAF
private database
least privilege
```

## Deployment

Required:

```text
Git
 ↓
test
 ↓
build
 ↓
artifact/image
 ↓
staging
 ↓
health validation
 ↓
canary/blue-green production
```

## Observability

```text
CloudWatch
structured logs
alarms
X-Ray/tracing
deployment events
```

## Required ADRs

```text
ADR-001-Web-Platform.md
ADR-002-API-Platform.md
ADR-003-Worker-Platform.md
ADR-004-Database.md
ADR-005-Deployment-Strategy.md
```

## Required Runbooks

```text
RUNBOOK_DEPLOYMENT_FAILURE.md
RUNBOOK_PLATFORM_UNHEALTHY.md
RUNBOOK_API_5XX.md
RUNBOOK_LAMBDA_THROTTLE.md
RUNBOOK_QUEUE_BACKLOG.md
RUNBOOK_DB_CONNECTIONS.md
RUNBOOK_SECRET_FAILURE.md
RUNBOOK_ROLLBACK.md
```

---

## 7. Recommended Resources

This Markdown is designed to be self-contained.

For current production implementation, use official AWS documentation:

```text
AWS Elastic Beanstalk Developer Guide
AWS App Runner Developer Guide
Amazon ECS Developer Guide
Amazon EKS User Guide
AWS Fargate documentation
AWS Lambda Developer Guide
Amazon API Gateway Developer Guide
AWS AppSync Developer Guide
Amazon EventBridge
Amazon SQS
Amazon SNS
AWS Step Functions
AWS CloudFormation
Amazon CloudWatch
```

---

## 8. Certification Relevance

This course is primarily **platform engineering / application deployment training**, not a one-to-one certification course.

It reinforces skills relevant to:

```text
AWS Solutions Architect – Associate
AWS CloudOps Engineer – Associate
AWS Developer – Associate
AWS DevOps Engineer – Professional
```

and prepares for later:

```text
Containers
Kubernetes
Infrastructure as Code
DevOps
CI/CD
Cloud-Native Development
DevSecOps
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** EC2 for every web workload.  
  **Best practice:** choose the lowest suitable abstraction.

- **Mistake:** Kubernetes because "containers".  
  **Best practice:** use EKS only when Kubernetes capabilities justify complexity.

- **Mistake:** Lambda for a 45-minute job.  
  **Best practice:** Fargate/Batch/workflow.

- **Mistake:** Store session in local app memory.  
  **Best practice:** external shared state.

- **Mistake:** Store uploaded files on ephemeral instance/container filesystem.  
  **Best practice:** S3/EFS where appropriate.

- **Mistake:** Put secrets in environment source files/Git.  
  **Best practice:** Secrets Manager/Parameter Store + IAM roles.

- **Mistake:** Confuse ECS task role and execution role.  
  **Best practice:** runtime app permissions vs platform task-start permissions.

- **Mistake:** Make production deployment all-at-once.  
  **Best practice:** canary/rolling/immutable/blue-green according to risk.

- **Mistake:** Health check only tests port.  
  **Best practice:** meaningful readiness endpoint.

- **Mistake:** Scale frontend without protecting database.  
  **Best practice:** pools/proxy/cache/queue/concurrency limits.

- **Mistake:** No centralized logs because platform is managed.  
  **Best practice:** management does not remove application observability.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Elastic Beanstalk?

**Answer:** Managed web application environment that provisions and manages underlying AWS resources such as EC2, scaling, load balancing, and health.

### Q2. App Runner?

**Answer:** Managed source/container-to-scalable-web-service platform.

### Q3. ECS?

**Answer:** AWS-native container orchestration.

### Q4. EKS?

**Answer:** Managed Kubernetes.

### Q5. Fargate?

**Answer:** Serverless compute for ECS/EKS containers.

### Q6. Lambda?

**Answer:** Serverless event-driven function compute.

### Q7. Maximum Lambda execution duration in current AWS guidance?

**Answer:** 15 minutes.

### Q8. Beanstalk worker environment?

**Answer:** SQS-backed asynchronous worker application environment.

### Q9. App Runner best fit?

**Answer:** Managed HTTP web app/API from source or container with minimal infrastructure operations.

### Q10. Task role vs execution role?

**Answer:** Task role is application AWS permissions; execution role supports ECS/Fargate platform actions such as image/log/secret operations.

### Q11. ECS service?

**Answer:** Maintains desired number of long-running tasks.

### Q12. Lambda reserved concurrency?

**Answer:** Reserves/limits concurrent function executions.

### Q13. Provisioned concurrency?

**Answer:** Pre-initialized Lambda execution capacity to reduce cold-start latency.

### Q14. API Gateway?

**Answer:** Managed API front door.

### Q15. AppSync?

**Answer:** Managed GraphQL API service.

### Q16. SQS?

**Answer:** Durable work queue.

### Q17. SNS?

**Answer:** Pub/sub fan-out.

### Q18. EventBridge?

**Answer:** Event bus/routing.

### Q19. Step Functions?

**Answer:** Workflow/state orchestration.

### Q20. Core platform-selection principle?

**Answer:** Choose the lowest operational complexity that satisfies runtime, control, network, performance, security, portability, deployment, and cost requirements.

---

# Expanded Self-Assessment Bank — Amazon PaaS Web Services

### Q1. What is the key lesson from **Platform Selection by Hard Constraints**?
**Answer:** Eliminate platforms that violate hard constraints first.

### Q2. What is the key lesson from **Code / Config / Secret Separation**?
**Answer:** Promote one artifact and inject environment-specific configuration.

### Q3. What is the key lesson from **Stateless Compute**?
**Answer:** Design compute as replaceable.

### Q4. What is the key lesson from **Liveness vs Readiness**?
**Answer:** Keep readiness fast; test deep dependencies with synthetic monitoring.

### Q5. What is the key lesson from **Graceful Shutdown**?
**Answer:** Test graceful termination during deployment tests.

### Q6. What is the key lesson from **Beanstalk Blue/Green**?
**Answer:** Keep Blue until Green is stable and data compatibility is confirmed.

### Q7. What is the key lesson from **Beanstalk Platform Lifecycle**?
**Answer:** Treat managed platform upgrades as code/runtime changes.

### Q8. What is the key lesson from **App Runner Build vs Runtime Identity**?
**Answer:** Separate deployment-plane and runtime permissions.

### Q9. What is the key lesson from **App Runner VPC Connector**?
**Answer:** Treat VPC connector as a network architecture change.

### Q10. What is the key lesson from **ECS Task Definition Immutability**?
**Answer:** Use immutable artifacts and versioned task definitions.

### Q11. What is the key lesson from **Task Role vs Execution Role**?
**Answer:** Grant each role only its layer's permissions.

### Q12. What is the key lesson from **ECS awsvpc Subnet Capacity**?
**Answer:** Capacity-plan subnet IPs for task count and deployment headroom.

### Q13. What is the key lesson from **ECS Deployment Surge**?
**Answer:** Size deployment surge from real headroom.

### Q14. What is the key lesson from **EKS Selection Gate**?
**Answer:** Use EKS only when Kubernetes value exceeds complexity.

### Q15. What is the key lesson from **Lambda Initialization Reuse**?
**Answer:** Reuse clients for performance, never for correctness.

### Q16. What is the key lesson from **Lambda /tmp Semantics**?
**Answer:** Use `/tmp` only for ephemeral working data.

### Q17. What is the key lesson from **Lambda Concurrency Protects RDS**?
**Answer:** Set concurrency from downstream capacity.

### Q18. What is the key lesson from **Lambda Idempotency**?
**Answer:** Assume events can repeat.

### Q19. What is the key lesson from **Lambda Batch Failure Isolation**?
**Answer:** Isolate poison records and keep handlers idempotent.

### Q20. What is the key lesson from **Lambda Alias Canary**?
**Answer:** Define canary thresholds before traffic shift.

### Q21. What is the key lesson from **API Gateway HTTP vs REST**?
**Answer:** Use the simplest API type that satisfies requirements.

### Q22. What is the key lesson from **API Private Integration**?
**Answer:** Keep backend private when public exposure is unnecessary.

### Q23. What is the key lesson from **API Authentication vs Object Authorization**?
**Answer:** Enforce authorization at capability and object levels.

### Q24. What is the key lesson from **Idempotent POST**?
**Answer:** Require idempotency for retry-prone irreversible operations.

### Q25. What is the key lesson from **API Backpressure**?
**Answer:** Set ingress capacity from end-to-end dependency capacity.

### Q26. What is the key lesson from **WebSocket Connection Lifecycle**?
**Answer:** Treat connection IDs as temporary resources.

### Q27. What is the key lesson from **CloudFront Multi-Origin**?
**Answer:** Design cache behavior by data sensitivity and variability.

### Q28. What is the key lesson from **CloudFront Origin Access**?
**Answer:** Expose the delivery layer, not the origin bucket.

### Q29. What is the key lesson from **WAF Rate Rules**?
**Answer:** Observe/count before blocking complex traffic patterns.

### Q30. What is the key lesson from **SQS Backpressure for Long Jobs**?
**Answer:** Decouple request latency from long-running work.

### Q31. What is the key lesson from **DLQ as Operational Workflow**?
**Answer:** Alert on DLQ depth for critical workflows.

### Q32. What is the key lesson from **Event Schema Versioning**?
**Answer:** Treat event schemas like public APIs.

### Q33. What is the key lesson from **Step Functions Retry Classification**?
**Answer:** Classify errors before defining retries.

### Q34. What is the key lesson from **Saga Compensation**?
**Answer:** Design compensation before orchestrating irreversible steps.

### Q35. What is the key lesson from **RDS Connection Pool Math**?
**Answer:** Capacity-plan DB sessions across maximum compute scale.

### Q36. What is the key lesson from **Backward-Compatible Schema Deployment**?
**Answer:** Use expand/migrate/contract schema changes.

### Q37. What is the key lesson from **Cache Stampede Protection**?
**Answer:** Design cache-miss behavior, not only cache-hit behavior.

### Q38. What is the key lesson from **Multi-Tenant Cache Keys**?
**Answer:** Treat cache-key design as authorization.

### Q39. What is the key lesson from **Sensitive CDN Caching**?
**Answer:** Default to no shared cache for sensitive personalized APIs.

### Q40. What is the key lesson from **CORS Is Not Authentication**?
**Answer:** Configure CORS narrowly but secure APIs with identity and authorization.

### Q41. What is the key lesson from **Webhook Signature Verification**?
**Answer:** Never trust a webhook because its URL is secret.

### Q42. What is the key lesson from **Outbound Webhook Queue**?
**Answer:** Decouple outbound webhook delivery from business transactions.

### Q43. What is the key lesson from **Container Resource Sizing**?
**Answer:** Right-size from measured usage and investigate leaks.

### Q44. What is the key lesson from **Fargate vs EC2 Total Economics**?
**Answer:** Compare operational labor with cloud price.

### Q45. What is the key lesson from **Lambda Memory Price/Performance**?
**Answer:** Benchmark memory settings with real workloads.

### Q46. What is the key lesson from **Provisioned Concurrency Economics**?
**Answer:** Pay for warm capacity only where SLO needs it.

### Q47. What is the key lesson from **NAT and Endpoint Cost for Managed Compute**?
**Answer:** Model network cost, not only compute cost.

### Q48. What is the key lesson from **Container Image Supply Chain**?
**Answer:** Deploy immutable, traceable artifacts.

### Q49. What is the key lesson from **Application Secret Refresh**?
**Answer:** Design secret refresh before enabling rotation.

### Q50. What is the key lesson from **Structured Logging Correlation**?
**Answer:** Create correlation at ingress and propagate it everywhere.

### Q51. What is the key lesson from **Logging PII and Secret Controls**?
**Answer:** Classify and protect logs like production data.

### Q52. What is the key lesson from **Deployment Version in Telemetry**?
**Answer:** Make release version a first-class telemetry field.

### Q53. What is the key lesson from **Backward-Compatible Rollback**?
**Answer:** Prove reversibility before calling something rollback.

### Q54. What is the key lesson from **Build Once, Promote**?
**Answer:** Build once and promote immutable artifacts.

### Q55. What is the key lesson from **Blue/Green Headroom**?
**Answer:** Capacity-plan the overlap period.

### Q56. What is the key lesson from **Canary Sample Sufficiency**?
**Answer:** Set canary duration from traffic and risk.

### Q57. What is the key lesson from **Synthetic User Journey**?
**Answer:** Monitor at least one real business journey.

### Q58. What is the key lesson from **Queue Age as Async SLO**?
**Answer:** Monitor backlog age as well as depth.

### Q59. What is the key lesson from **Managed Platform Quotas**?
**Answer:** Serverless is elastic, not unlimited.

### Q60. What is the key lesson from **Managed Platform DR**?
**Answer:** Include every platform dependency in DR.

### Q61. What is the key lesson from **Platform Unit Economics**?
**Answer:** Measure cost per workload unit and total operational effort.

### Q62. What is the key lesson from **Operational Readiness for Managed Services**?
**Answer:** Managed means less infrastructure toil, not less operational responsibility.


## Completion Checklist

- [ ] I understand PaaS/CaaS/FaaS.
- [ ] I can compare EC2/Beanstalk/App Runner/ECS/EKS/Fargate/Lambda.
- [ ] I understand Elastic Beanstalk deeply.
- [ ] I understand App Runner.
- [ ] I understand ECS task/service/roles/networking.
- [ ] I understand EKS selection.
- [ ] I understand Lambda execution/scaling/events.
- [ ] I understand API Gateway.
- [ ] I understand AppSync fundamentals.
- [ ] I understand CloudFront/WAF/Route53 web entry.
- [ ] I understand queues/events/workflows.
- [ ] I understand application state/storage/data dependencies.
- [ ] I understand secrets and workload IAM.
- [ ] I understand observability/tracing.
- [ ] I understand deployment strategies.
- [ ] I understand CI/CD/IaC integration.
- [ ] I understand platform cost models.
- [ ] I can troubleshoot managed application platforms.
- [ ] I completed all 30 labs.
- [ ] I completed the Managed AWS Web Platform project.
