# 79. Kubernetes Application Deployment

> Phase 19 — Cloud-Native Development

Kubernetes application deployment is the discipline of taking containerized applications and running them reliably on a declarative orchestration platform.

The core mental model is:

```text
Git / CI
   ↓
Container Image
   ↓
Registry
   ↓
Kubernetes Manifests / Helm / GitOps
   ↓
API Server
   ↓
Desired State
   ↓
Controllers
   ↓
Pods
   ↓
Services / Ingress
   ↓
Config / Secrets / Storage
   ↓
Health / Autoscaling / Observability
```

Kubernetes does not merely "run Docker containers." It continuously reconciles declared desired state against actual state.

A production deployment must answer:

```text
Which image version should run?
How many replicas?
What CPU/memory does each replica require?
When is a pod ready?
What happens when a pod crashes?
How does traffic find healthy replicas?
How are configuration and secrets injected?
How is persistent data handled?
How do we roll out safely?
How do we rollback?
How do we autoscale?
How do we prevent one workload from harming another?
How do we observe failures?
```

This course focuses on **deploying applications onto Kubernetes**, not administering the cluster itself.

## 1. Topic Title

**Kubernetes Application Deployment**

## 2. Learning Objectives

- Explain the Kubernetes declarative application model.
- Explain Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs, and CronJobs.
- Design application Deployments with replicas and rollout strategies.
- Use Services for stable networking and discovery.
- Explain ClusterIP, NodePort, and LoadBalancer service exposure.
- Explain Ingress and Gateway-style edge routing concepts.
- Use ConfigMaps and Secrets appropriately.
- Use environment variables and mounted configuration.
- Design liveness, readiness, and startup probes.
- Configure CPU/memory requests and limits.
- Explain scheduling implications of requests and limits.
- Design horizontal autoscaling.
- Explain HPA signals and custom metrics conceptually.
- Explain event-driven autoscaling awareness.
- Use PersistentVolume, PersistentVolumeClaim, and StorageClass concepts.
- Explain ephemeral volumes and emptyDir.
- Design stateless and stateful application deployments.
- Use Jobs and CronJobs for one-off and scheduled workloads.
- Design init containers and sidecar patterns.
- Explain labels, selectors, and annotations.
- Use namespaces for workload organization.
- Understand service accounts and workload identity concepts.
- Apply least privilege through RBAC awareness.
- Explain NetworkPolicy for application isolation.
- Design securityContext settings for non-root workloads.
- Explain pod security principles.
- Use imagePullSecrets and private registries safely.
- Deploy immutable image digests.
- Design rolling updates and rollbacks.
- Explain maxSurge and maxUnavailable concepts.
- Design canary and blue/green patterns on Kubernetes.
- Use PodDisruptionBudget awareness.
- Use affinity, anti-affinity, topology spread, and node selectors conceptually.
- Explain taints/tolerations awareness.
- Design graceful shutdown and preStop behavior.
- Use lifecycle hooks appropriately.
- Explain Service DNS and internal discovery.
- Design application logging, metrics, and tracing in Kubernetes.
- Explain sidecar and DaemonSet observability patterns.
- Use kubectl-style troubleshooting commands conceptually.
- Diagnose CrashLoopBackOff, ImagePullBackOff, Pending, OOMKilled, and readiness failures.
- Explain GitOps deployment flow.
- Explain Helm/Kustomize-style templating/overlays concepts.
- Design environment promotion and configuration separation.
- Design safe database migrations on Kubernetes.
- Explain backup/recovery responsibilities for stateful applications.
- Design HA across nodes/zones.
- Understand resource quotas and noisy-neighbor protection.
- Build a production Kubernetes application deployment architecture.

## 3. Prerequisites

Required:

```text
57–60. Containers / Kubernetes Fundamentals / Administration
77. Cloud-Native Application Development
78. Containerized Application Deployment
Linux
Networking
YAML
CI/CD
```

Recommended:

```text
Helm awareness
GitOps awareness
Cloud load balancers
Observability
Storage fundamentals
```

The focus here is application deployment. Cluster control-plane administration, PKI, etcd operations, and advanced cluster lifecycle belong to Kubernetes administration.

## 4. Core Concepts Explanation

# Part 1 — Kubernetes Desired State

### Core Explanation

You declare what should exist; controllers continuously reconcile actual state toward that declaration.

### Example / Visualization

```text
desired replicas=3 → controller maintains 3
```

### Why It Matters

This is the heart of Kubernetes.

### Practical Use

Think declaratively rather than scripting individual containers.

# Part 2 — Kubernetes API Object

### Core Explanation

Resources such as Deployment, Service, ConfigMap, and Secret are API objects stored and managed by the cluster.

### Example / Visualization

```text
YAML → API Server → object
```

### Why It Matters

Everything is driven through the API.

### Practical Use

Treat manifests as versioned code.

# Part 3 — Manifest

### Core Explanation

A YAML/JSON document describing an API object.

### Example / Visualization

```text
apiVersion/kind/metadata/spec
```

### Why It Matters

Portable declaration of desired state.

### Practical Use

Store in Git.

# Part 4 — metadata

### Core Explanation

Metadata includes name, namespace, labels, and annotations.

### Example / Visualization

```text
metadata.name: orders
```

### Why It Matters

Used for identity and organization.

### Practical Use

Choose stable names.

# Part 5 — spec

### Core Explanation

Spec describes desired configuration.

### Example / Visualization

```text
replicas/image/ports
```

### Why It Matters

Controllers work from spec.

### Practical Use

Avoid manual mutation outside source of truth.

# Part 6 — status

### Core Explanation

Status reports observed/current state.

### Example / Visualization

```text
readyReplicas/currentRevision
```

### Why It Matters

Useful for troubleshooting.

### Practical Use

Do not treat status as configuration.

# Part 7 — Pod

### Core Explanation

Smallest deployable execution unit; one or more containers share network namespace and volumes.

### Example / Visualization

```text
Pod = app container + optional sidecars
```

### Why It Matters

Kubernetes schedules Pods, not individual containers.

### Practical Use

Use one main application concern per Pod.

# Part 8 — Pod Lifecycle

### Core Explanation

Pods move through scheduling, image pull, startup, running, termination, and deletion.

### Example / Visualization

```text
Pending→Running→Terminating
```

### Why It Matters

Understanding lifecycle explains many failures.

### Practical Use

Pods are disposable.

# Part 9 — ReplicaSet

### Core Explanation

Maintains a desired number of identical Pods.

### Example / Visualization

```text
replicas=3
```

### Why It Matters

Usually managed indirectly by Deployments.

### Practical Use

Do not edit ReplicaSets created by Deployment manually.

# Part 10 — Deployment

### Core Explanation

Manages stateless application replicas and rolling updates.

### Example / Visualization

```text
Deployment→ReplicaSets→Pods
```

### Why It Matters

Primary object for stateless services.

### Practical Use

Use for APIs/workers that do not need stable identity.

# Part 11 — StatefulSet

### Core Explanation

Manages stateful Pods with stable identities and ordered behavior.

### Example / Visualization

```text
db-0,db-1,db-2
```

### Why It Matters

Useful for stateful distributed systems.

### Practical Use

Requires careful storage and application semantics.

# Part 12 — DaemonSet

### Core Explanation

Runs one Pod on each or selected node.

### Example / Visualization

```text
node log agent
```

### Why It Matters

Ideal for node-local agents.

### Practical Use

Not for normal horizontally scaled app replicas.

# Part 13 — Job

### Core Explanation

Runs Pods to completion.

### Example / Visualization

```text
migration/import job
```

### Why It Matters

Useful for finite one-off tasks.

### Practical Use

Make jobs idempotent.

# Part 14 — CronJob

### Core Explanation

Creates Jobs on a schedule.

### Example / Visualization

```text
nightly cleanup
```

### Why It Matters

Useful for scheduled workloads.

### Practical Use

Handle overlapping runs and idempotency.

# Part 15 — Controller

### Core Explanation

A control loop watches desired and actual state and acts to reconcile them.

### Example / Visualization

```text
desired 3, actual 2 → create Pod
```

### Why It Matters

Provides self-healing.

### Practical Use

Troubleshooting often means identifying which controller owns the object.

# Part 16 — Owner Reference Awareness

### Core Explanation

Child objects record which controller owns them.

### Example / Visualization

```text
Deployment→ReplicaSet→Pod
```

### Why It Matters

Helps Kubernetes garbage collection and troubleshooting.

### Practical Use

Do not mutate generated children as source of truth.

# Part 17 — Label

### Core Explanation

A key-value identifier attached to objects.

### Example / Visualization

```text
app=orders,version=v2
```

### Why It Matters

Core mechanism for grouping/selecting resources.

### Practical Use

Use consistent taxonomy.

# Part 18 — Selector

### Core Explanation

A selector chooses objects by labels.

### Example / Visualization

```text
app=orders
```

### Why It Matters

Services/controllers depend on selectors.

### Practical Use

Selector mistakes can route traffic incorrectly.

# Part 19 — Annotation

### Core Explanation

Annotations store non-identifying metadata.

### Example / Visualization

```text
owner/team/docs/checksum
```

### Why It Matters

Useful for tools and metadata.

### Practical Use

Do not use annotations for selection.

# Part 20 — Namespace

### Core Explanation

Logical partition for names, quotas, policy, and ownership.

### Example / Visualization

```text
dev/prod/team-a
```

### Why It Matters

Useful organizational boundary.

### Practical Use

Not a hard security boundary by itself.

# Part 21 — Naming Convention

### Core Explanation

Predictable resource names improve operations.

### Example / Visualization

```text
orders-api
```

### Why It Matters

Human debugging depends on readable names.

### Practical Use

Avoid embedding ephemeral IDs.

# Part 22 — Recommended Label Set Awareness

### Core Explanation

Organizations often standardize app name, component, version, environment, and owner labels.

### Example / Visualization

```text
app.kubernetes.io/... awareness
```

### Why It Matters

Improves tooling.

### Practical Use

Use one platform convention.

# Part 23 — Environment Separation

### Core Explanation

Dev, staging, and production can use separate namespaces or clusters depending risk.

### Example / Visualization

```text
dev ns / prod cluster
```

### Why It Matters

Separation reduces blast radius.

### Practical Use

Production often deserves stronger isolation.

# Part 24 — Deployment Replica Count

### Core Explanation

replicas defines desired Pod count.

### Example / Visualization

```text
replicas: 3
```

### Why It Matters

Provides baseline availability/capacity.

### Practical Use

Autoscaling may override replica count dynamically.

# Part 25 — Pod Template

### Core Explanation

Deployment embeds a Pod template defining containers, volumes, labels, probes, resources, etc.

### Example / Visualization

```text
spec.template
```

### Why It Matters

Changing template creates a new ReplicaSet.

### Practical Use

Template changes drive rollout.

# Part 26 — RollingUpdate Strategy

### Core Explanation

Kubernetes gradually replaces old Pods with new ones.

### Example / Visualization

```text
v1/v2 coexist
```

### Why It Matters

Supports low-downtime releases.

### Practical Use

Requires compatibility.

# Part 27 — maxSurge

### Core Explanation

Controls how many extra Pods can exist during rollout.

### Example / Visualization

```text
3 desired + surge 1
```

### Why It Matters

Adds temporary capacity.

### Practical Use

Ensure cluster has headroom.

# Part 28 — maxUnavailable

### Core Explanation

Controls how many desired Pods may be unavailable during rollout.

### Example / Visualization

```text
maxUnavailable=0/1
```

### Why It Matters

Balances speed and availability.

### Practical Use

Choose based on SLO.

# Part 29 — Rollback

### Core Explanation

Deployment can return to a prior ReplicaSet/template revision.

### Example / Visualization

```text
v2 bad→v1
```

### Why It Matters

Fast recovery.

### Practical Use

Database/config changes must remain compatible.

# Part 30 — Rollout Status

### Core Explanation

Observe whether new revision becomes available.

### Example / Visualization

```text
rollout progressing
```

### Why It Matters

Prevents assuming apply=healthy.

### Practical Use

Automate verification.

# Part 31 — Revision History Awareness

### Core Explanation

Old ReplicaSets may be retained for rollback.

### Example / Visualization

```text
revisionHistoryLimit
```

### Why It Matters

Consumes some metadata/resources.

### Practical Use

Keep enough for recovery.

# Part 32 — Canary Deployment Awareness

### Core Explanation

Run a small new-version subset and direct limited traffic.

### Example / Visualization

```text
v1 95%, v2 5%
```

### Why It Matters

Reduces blast radius.

### Practical Use

Requires traffic routing beyond a basic Deployment.

# Part 33 — Blue/Green Awareness

### Core Explanation

Two complete versions run side by side and Service/gateway switches traffic.

### Example / Visualization

```text
blue svc→green svc
```

### Why It Matters

Fast rollback.

### Practical Use

Consumes extra capacity.

# Part 34 — Shadow Traffic Awareness

### Core Explanation

Traffic is mirrored to new version without using response.

### Example / Visualization

```text
prod→v1 + mirror v2
```

### Why It Matters

Useful for validation.

### Practical Use

Avoid duplicate side effects.

# Part 35 — Progressive Delivery

### Core Explanation

Automated traffic shifting based on metrics.

### Example / Visualization

```text
5→25→50→100%
```

### Why It Matters

Combines deployment and observability.

### Practical Use

Often implemented with specialized controllers/service mesh/gateway.

# Part 36 — Backward-Compatible Rollout

### Core Explanation

Old and new versions must coexist safely during rolling updates.

### Example / Visualization

```text
v1+v2
```

### Why It Matters

Critical for API/schema changes.

### Practical Use

Use expand-contract.

# Part 37 — Rollback-Compatible Schema

### Core Explanation

Database changes must allow previous app version to run if rollback occurs.

### Example / Visualization

```text
add column first
```

### Why It Matters

Without this rollback is blocked.

### Practical Use

Delay destructive migrations.

# Part 38 — Service

### Core Explanation

Provides stable virtual IP/DNS and load balancing to selected Pods.

### Example / Visualization

```text
Service→Pods
```

### Why It Matters

Pods are ephemeral; Services provide stable discovery.

### Practical Use

Selectors must match intended Pods.

# Part 39 — ClusterIP

### Core Explanation

Exposes Service only inside cluster.

### Example / Visualization

```text
orders.default.svc
```

### Why It Matters

Default for internal services.

### Practical Use

Prefer for backend-only dependencies.

# Part 40 — NodePort

### Core Explanation

Exposes a port on each node.

### Example / Visualization

```text
nodeIP:nodePort
```

### Why It Matters

Simple external exposure.

### Practical Use

Usually not preferred for polished production ingress.

# Part 41 — LoadBalancer

### Core Explanation

Requests an external load balancer from supporting infrastructure.

### Example / Visualization

```text
Cloud LB→Service
```

### Why It Matters

Common for direct external services.

### Practical Use

Costs and provider behavior vary.

# Part 42 — Headless Service Awareness

### Core Explanation

Service without cluster IP returns Pod endpoints directly.

### Example / Visualization

```text
clusterIP: None concept
```

### Why It Matters

Useful for stateful peer discovery.

### Practical Use

Clients handle endpoints.

# Part 43 — Service Selector

### Core Explanation

Matches Pods by labels.

### Example / Visualization

```text
app=orders
```

### Why It Matters

Determines backend endpoints.

### Practical Use

Wrong labels cause no endpoints.

# Part 44 — EndpointSlice Awareness

### Core Explanation

Kubernetes represents Service backends in scalable endpoint resources.

### Example / Visualization

```text
Service→EndpointSlices
```

### Why It Matters

Modern backend-discovery mechanism.

### Practical Use

Useful in troubleshooting.

# Part 45 — Service DNS

### Core Explanation

Cluster DNS resolves service names.

### Example / Visualization

```text
orders.default.svc.cluster.local
```

### Why It Matters

Primary internal discovery.

### Practical Use

Use logical names, not Pod IPs.

# Part 46 — Pod IP

### Core Explanation

Each Pod receives an IP but it is ephemeral.

### Example / Visualization

```text
Pod restart→new IP
```

### Why It Matters

Do not hardcode Pod addresses.

### Practical Use

Use Service.

# Part 47 — Container Port

### Core Explanation

Documents/listens inside Pod; Service targetPort routes to it.

### Example / Visualization

```text
Service 80→Pod 8080
```

### Why It Matters

Separates client port from app port.

### Practical Use

Ensure app binds correct interface.

# Part 48 — Ingress Awareness

### Core Explanation

Ingress resources describe HTTP routing to Services when supported by an Ingress controller.

### Example / Visualization

```text
Host/path→Service
```

### Why It Matters

Common external web routing model.

### Practical Use

Controller is required.

# Part 49 — Ingress Controller

### Core Explanation

Actual proxy/controller implementing Ingress rules.

### Example / Visualization

```text
NGINX-like/controller
```

### Why It Matters

Resource alone does nothing.

### Practical Use

Operate controller as critical edge component.

# Part 50 — Gateway API Awareness

### Core Explanation

Newer gateway-style APIs model gateways, routes, listeners, and policy with more expressive separation.

### Example / Visualization

```text
Gateway→HTTPRoute→Service
```

### Why It Matters

Improves role separation and routing flexibility.

### Practical Use

Use platform-supported implementation.

# Part 51 — TLS Termination

### Core Explanation

Ingress/Gateway can terminate TLS.

### Example / Visualization

```text
Client TLS→Gateway→Service
```

### Why It Matters

Centralizes certificate handling.

### Practical Use

Internal TLS depends on threat model.

# Part 52 — ExternalDNS Awareness

### Core Explanation

Automation can create DNS records from Kubernetes resources.

### Example / Visualization

```text
Service/Ingress→DNS
```

### Why It Matters

Reduces manual DNS.

### Practical Use

Requires scoped cloud DNS permissions.

# Part 53 — NetworkPolicy

### Core Explanation

Controls allowed Pod ingress/egress based on labels/namespaces/IPs where supported.

### Example / Visualization

```text
default deny + allow rules
```

### Why It Matters

Reduces lateral movement.

### Practical Use

Requires compatible network plugin.

# Part 54 — Default-Deny Policy

### Core Explanation

Block traffic unless explicitly allowed.

### Example / Visualization

```text
deny all→specific allow
```

### Why It Matters

Good security baseline.

### Practical Use

Roll out carefully to avoid outages.

# Part 55 — Egress Policy

### Core Explanation

Restricts outbound destinations.

### Example / Visualization

```text
orders→payment/db only
```

### Why It Matters

Limits compromised workload movement.

### Practical Use

DNS and cloud endpoints require planning.

# Part 56 — ConfigMap

### Core Explanation

Stores non-secret configuration data.

### Example / Visualization

```text
LOG_LEVEL, feature config
```

### Why It Matters

Decouples config from image.

### Practical Use

Do not put credentials inside.

# Part 57 — Config as Environment

### Core Explanation

ConfigMap keys can populate environment variables.

### Example / Visualization

```text
envFrom ConfigMap
```

### Why It Matters

Simple for small config.

### Practical Use

Updates usually require restart to affect process env.

# Part 58 — Config as Volume

### Core Explanation

ConfigMap can be mounted as files.

### Example / Visualization

```text
/etc/app/config.yaml
```

### Why It Matters

Useful for structured files.

### Practical Use

Applications may need reload logic.

# Part 59 — Secret

### Core Explanation

Stores sensitive values for injection into Pods.

### Example / Visualization

```text
DB password/token
```

### Why It Matters

Separates secret objects from ordinary config.

### Practical Use

Base64 representation is not encryption by itself.

# Part 60 — Secret as Environment

### Core Explanation

Secret value can become environment variable.

### Example / Visualization

```text
DB_PASSWORD
```

### Why It Matters

Convenient.

### Practical Use

May be exposed through process/debug tooling.

# Part 61 — Secret as Volume

### Core Explanation

Secret can be mounted as files.

### Example / Visualization

```text
/run/secrets/...
```

### Why It Matters

Good for certs/keys.

### Practical Use

Handle file permissions and rotation.

# Part 62 — External Secret Manager Awareness

### Core Explanation

Controllers/CSI integrations can project secrets from cloud/vault systems.

### Example / Visualization

```text
external secret store→Pod
```

### Why It Matters

Reduces static secrets in cluster.

### Practical Use

Adds external dependency.

# Part 63 — Secret Rotation

### Core Explanation

Pods/apps need a strategy for updated credentials.

### Example / Visualization

```text
rotate secret→reload/restart
```

### Why It Matters

Long-lived connections may need reconnect.

### Practical Use

Test rotation.

# Part 64 — Configuration Checksum Pattern Awareness

### Core Explanation

Deployment template annotation can include config hash so config change triggers rollout.

### Example / Visualization

```text
checksum/config
```

### Why It Matters

Useful when app reads config only at startup.

### Practical Use

Automate through templating.

# Part 65 — Immutable Config Awareness

### Core Explanation

Some config can be treated as immutable and versioned.

### Example / Visualization

```text
config-v3
```

### Why It Matters

Reduces surprise mutation.

### Practical Use

Roll forward via new object/version.

# Part 66 — Liveness Probe

### Core Explanation

Determines whether a container is stuck and should be restarted.

### Example / Visualization

```text
/live
```

### Why It Matters

Restart is destructive; use carefully.

### Practical Use

Do not depend on external DB.

# Part 67 — Readiness Probe

### Core Explanation

Determines whether Pod should receive Service traffic.

### Example / Visualization

```text
/ready
```

### Why It Matters

Protects clients from unready instances.

### Practical Use

Include only essential serving dependencies.

# Part 68 — Startup Probe

### Core Explanation

Allows slow-starting app time to initialize before liveness takes effect.

### Example / Visualization

```text
/startup
```

### Why It Matters

Prevents premature restart loops.

### Practical Use

Use for legitimately slow startup.

# Part 69 — HTTP Probe

### Core Explanation

Kubelet performs HTTP request.

### Example / Visualization

```text
GET /ready
```

### Why It Matters

Good for web apps.

### Practical Use

Keep endpoint cheap.

# Part 70 — TCP Probe

### Core Explanation

Checks whether a port accepts connection.

### Example / Visualization

```text
tcpSocket
```

### Why It Matters

Useful when HTTP endpoint unavailable.

### Practical Use

Does not verify full application semantics.

# Part 71 — Exec Probe

### Core Explanation

Runs a command in container.

### Example / Visualization

```text
exec health command
```

### Why It Matters

Flexible but adds process overhead.

### Practical Use

Avoid expensive probes.

# Part 72 — Probe Initial Delay

### Core Explanation

Wait before starting checks.

### Example / Visualization

```text
initialDelaySeconds
```

### Why It Matters

Can hide poor startup if overused.

### Practical Use

Prefer startup probes.

# Part 73 — Probe Period

### Core Explanation

Frequency of checks.

### Example / Visualization

```text
periodSeconds
```

### Why It Matters

Trade-off detection speed vs load.

### Practical Use

Avoid too aggressive intervals.

# Part 74 — Failure Threshold

### Core Explanation

Number of failures before action.

### Example / Visualization

```text
failureThreshold
```

### Why It Matters

Controls sensitivity.

### Practical Use

Tune to realistic transient behavior.

# Part 75 — preStop Hook

### Core Explanation

Runs action before container termination.

### Example / Visualization

```text
preStop sleep/drain
```

### Why It Matters

Can assist connection draining.

### Practical Use

Still handle SIGTERM in app.

# Part 76 — Termination Grace Period

### Core Explanation

Time allowed for graceful shutdown before force kill.

### Example / Visualization

```text
30s concept
```

### Why It Matters

Must exceed realistic drain time.

### Practical Use

Avoid huge values.

# Part 77 — Graceful Shutdown Sequence

### Core Explanation

Remove readiness, stop new work, drain, close dependencies, exit.

### Example / Visualization

```text
NotReady→drain→exit
```

### Why It Matters

Prevents dropped requests.

### Practical Use

Coordinate app and platform.

# Part 78 — Resource Request

### Core Explanation

Amount of CPU/memory scheduler reserves for Pod.

### Example / Visualization

```text
cpu 250m, memory 256Mi
```

### Why It Matters

Influences scheduling and capacity.

### Practical Use

Set from measurements.

# Part 79 — Resource Limit

### Core Explanation

Maximum allowed CPU/memory usage behavior.

### Example / Visualization

```text
cpu 1, memory 512Mi
```

### Why It Matters

Protects cluster.

### Practical Use

CPU throttles; memory may OOM.

# Part 80 — CPU Unit

### Core Explanation

CPU can be expressed as cores or millicores.

### Example / Visualization

```text
500m=0.5 CPU
```

### Why It Matters

Supports precise requests.

### Practical Use

Profile application.

# Part 81 — Memory Unit

### Core Explanation

Memory expressed in bytes/Ki/Mi/Gi.

### Example / Visualization

```text
512Mi
```

### Why It Matters

Hard limit can cause OOM kill.

### Practical Use

Leave headroom.

# Part 82 — QoS Awareness

### Core Explanation

Kubernetes classifies Pods based on requests/limits and may use this under pressure.

### Example / Visualization

```text
Guaranteed/Burstable/BestEffort awareness
```

### Why It Matters

Affects eviction behavior.

### Practical Use

Critical apps should have sensible requests/limits.

# Part 83 — OOMKilled

### Core Explanation

Container exceeded memory or host pressure triggered kill.

### Example / Visualization

```text
OOMKilled
```

### Why It Matters

Common deployment failure.

### Practical Use

Inspect memory use and limits.

# Part 84 — CPU Throttling

### Core Explanation

Container exceeds CPU quota and gets throttled.

### Example / Visualization

```text
latency↑ while CPU capped
```

### Why It Matters

Can look like app slowness.

### Practical Use

Monitor throttling.

# Part 85 — Pending Pod

### Core Explanation

Scheduler cannot place Pod due to insufficient resources/constraints.

### Example / Visualization

```text
Pending
```

### Why It Matters

Usually scheduling issue.

### Practical Use

Inspect events.

# Part 86 — Node Selector

### Core Explanation

Constrains Pods to nodes with labels.

### Example / Visualization

```text
disk=ssd
```

### Why It Matters

Simple placement rule.

### Practical Use

Avoid unnecessary hard constraints.

# Part 87 — Node Affinity Awareness

### Core Explanation

Expresses richer scheduling preference/requirements.

### Example / Visualization

```text
zone/type rules
```

### Why It Matters

Useful for specialized workloads.

### Practical Use

Hard affinity can cause Pending.

# Part 88 — Pod Anti-Affinity Awareness

### Core Explanation

Avoid placing replicas together.

### Example / Visualization

```text
spread replicas
```

### Why It Matters

Improves HA.

### Practical Use

Topology spread may scale better.

# Part 89 — Topology Spread Constraints

### Core Explanation

Distribute Pods across zones/nodes.

### Example / Visualization

```text
maxSkew
```

### Why It Matters

Improves fault tolerance.

### Practical Use

Requires enough eligible nodes.

# Part 90 — Taint

### Core Explanation

Marks nodes to repel Pods unless tolerated.

### Example / Visualization

```text
dedicated=gpu:NoSchedule
```

### Why It Matters

Protects specialized nodes.

### Practical Use

Use tolerations intentionally.

# Part 91 — Toleration

### Core Explanation

Allows Pod onto matching tainted node.

### Example / Visualization

```text
tolerate dedicated node
```

### Why It Matters

Placement control.

### Practical Use

Does not force placement.

# Part 92 — PriorityClass Awareness

### Core Explanation

Higher-priority workloads can be scheduled/preempt lower ones.

### Example / Visualization

```text
critical service priority
```

### Why It Matters

Useful under resource pressure.

### Practical Use

Use sparingly.

# Part 93 — ResourceQuota

### Core Explanation

Namespace-level limits on resources/object counts.

### Example / Visualization

```text
CPU/memory/PVC quotas
```

### Why It Matters

Controls noisy neighbors and cost.

### Practical Use

Pair with LimitRange.

# Part 94 — LimitRange Awareness

### Core Explanation

Provides default/min/max requests/limits in namespace.

### Example / Visualization

```text
default CPU/mem
```

### Why It Matters

Improves hygiene.

### Practical Use

Document expectations.

# Part 95 — Horizontal Pod Autoscaler

### Core Explanation

HPA changes replica count based on observed metrics.

### Example / Visualization

```text
replicas↑/↓
```

### Why It Matters

Automates elasticity.

### Practical Use

App must be horizontally scalable.

# Part 96 — CPU HPA

### Core Explanation

Scale based on CPU utilization relative to request.

### Example / Visualization

```text
CPU target 70%
```

### Why It Matters

Simple for CPU-correlated workloads.

### Practical Use

Requests must be set correctly.

# Part 97 — Memory HPA Awareness

### Core Explanation

Memory can be used for scaling in some scenarios.

### Example / Visualization

```text
memory target
```

### Why It Matters

Useful for memory-proportional workloads.

### Practical Use

Leaks can cause runaway scaling.

# Part 98 — Custom Metrics

### Core Explanation

HPA can use application/external metrics through metrics adapters.

### Example / Visualization

```text
RPS, queue lag
```

### Why It Matters

Better signal for some workloads.

### Practical Use

Avoid noisy unstable metrics.

# Part 99 — Queue-Lag Autoscaling

### Core Explanation

Consumer replicas scale with backlog.

### Example / Visualization

```text
lag↑→workers↑
```

### Why It Matters

Strong fit for async workloads.

### Practical Use

Protect downstream DB/API.

# Part 100 — Event-Driven Autoscaling Awareness

### Core Explanation

Specialized controllers can scale from event sources.

### Example / Visualization

```text
queue depth→0..N
```

### Why It Matters

Supports scale-to-zero in some designs.

### Practical Use

Understand cold-start and dependency impact.

# Part 101 — Scale-Up Policy

### Core Explanation

Controls how quickly replicas increase.

### Example / Visualization

```text
+100% per interval
```

### Why It Matters

Prevents extreme jumps.

### Practical Use

Balance responsiveness and dependency limits.

# Part 102 — Scale-Down Stabilization

### Core Explanation

Avoid rapid oscillation after short traffic drops.

### Example / Visualization

```text
stabilization window
```

### Why It Matters

Prevents thrashing.

### Practical Use

Use realistic cooldown.

# Part 103 — Autoscaling Dependency Risk

### Core Explanation

More Pods multiply DB connections, broker consumers, and outbound calls.

### Example / Visualization

```text
10→100 Pods
```

### Why It Matters

Can overload shared systems.

### Practical Use

Capacity-plan end-to-end.

# Part 104 — Minimum Replicas

### Core Explanation

Keeps baseline capacity warm.

### Example / Visualization

```text
minReplicas=2
```

### Why It Matters

Improves availability/cold-start.

### Practical Use

Costs more.

# Part 105 — Maximum Replicas

### Core Explanation

Caps scale-out.

### Example / Visualization

```text
maxReplicas=50
```

### Why It Matters

Protects downstream/cost.

### Practical Use

Set intentionally.

# Part 106 — PersistentVolume

### Core Explanation

Cluster storage resource representing provisioned durable storage.

### Example / Visualization

```text
PV
```

### Why It Matters

Decouples storage lifecycle from Pod.

### Practical Use

Provision statically or dynamically.

# Part 107 — PersistentVolumeClaim

### Core Explanation

Application request for storage.

### Example / Visualization

```text
PVC→PV
```

### Why It Matters

Pods consume claims rather than provider-specific volumes.

### Practical Use

Specify size/access mode.

# Part 108 — StorageClass

### Core Explanation

Defines a class/provisioner/policy for dynamic storage.

### Example / Visualization

```text
fast-ssd / standard
```

### Why It Matters

Abstracts storage implementation.

### Practical Use

Understand reclaim/expansion policy.

# Part 109 — Dynamic Provisioning

### Core Explanation

PVC automatically triggers storage creation.

### Example / Visualization

```text
PVC→StorageClass→volume
```

### Why It Matters

Simplifies deployment.

### Practical Use

Cloud quotas/cost still apply.

# Part 110 — Access Mode Awareness

### Core Explanation

Volumes may support single-node or multi-node read/write modes depending backend.

### Example / Visualization

```text
RWO/RWX concepts
```

### Why It Matters

Application design depends on it.

### Practical Use

Do not assume shared-write support.

# Part 111 — Reclaim Policy Awareness

### Core Explanation

Storage may be retained or deleted after claim release.

### Example / Visualization

```text
Retain/Delete
```

### Why It Matters

Critical for data safety.

### Practical Use

Use retention for important data.

# Part 112 — Volume Expansion Awareness

### Core Explanation

Some storage classes support increasing PVC size.

### Example / Visualization

```text
10Gi→20Gi
```

### Why It Matters

Useful for growth.

### Practical Use

Filesystem/app may require action.

# Part 113 — emptyDir

### Core Explanation

Ephemeral volume shared by containers in one Pod; lost when Pod is removed.

### Example / Visualization

```text
emptyDir
```

### Why It Matters

Useful for temp/cache/inter-container files.

### Practical Use

Not durable.

# Part 114 — ConfigMap Volume

### Core Explanation

Projects config files into Pod.

### Example / Visualization

```text
ConfigMap→volume
```

### Why It Matters

Useful for read-only config.

### Practical Use

Not for secrets.

# Part 115 — Secret Volume

### Core Explanation

Projects secrets/certs into Pod.

### Example / Visualization

```text
Secret→volume
```

### Why It Matters

Useful for credentials.

### Practical Use

Protect file permissions.

# Part 116 — CSI Awareness

### Core Explanation

Container Storage Interface allows pluggable storage drivers.

### Example / Visualization

```text
K8s↔CSI driver↔storage
```

### Why It Matters

Standard storage integration.

### Practical Use

Driver availability matters.

# Part 117 — StatefulSet VolumeClaimTemplate Awareness

### Core Explanation

StatefulSet can create one PVC per replica.

### Example / Visualization

```text
db-0→pvc0
```

### Why It Matters

Supports stable per-Pod storage.

### Practical Use

Data replication still application responsibility.

# Part 118 — Backup Responsibility

### Core Explanation

Kubernetes does not automatically back up application data.

### Example / Visualization

```text
PVC != backup
```

### Why It Matters

Data recovery must be designed.

### Practical Use

Use storage snapshots/DB backups.

# Part 119 — Volume Snapshot Awareness

### Core Explanation

Storage providers may support point-in-time snapshots.

### Example / Visualization

```text
PVC→snapshot
```

### Why It Matters

Useful for backup/clone.

### Practical Use

Application consistency may require quiescing.

# Part 120 — Init Container

### Core Explanation

Runs to completion before application containers start.

### Example / Visualization

```text
init→app
```

### Why It Matters

Useful for setup/checks.

### Practical Use

Avoid long fragile dependency waiting.

# Part 121 — Migration Init Container Caution

### Core Explanation

Running DB migration from every replica init can race.

### Example / Visualization

```text
N Pods→same migration
```

### Why It Matters

Can cause conflicts.

### Practical Use

Prefer one Job for schema migration.

# Part 122 — Sidecar

### Core Explanation

A helper container shares Pod lifecycle/network/volumes.

### Example / Visualization

```text
app + proxy/agent
```

### Why It Matters

Useful for tightly coupled helper function.

### Practical Use

Adds resource/lifecycle complexity.

# Part 123 — Log Sidecar Awareness

### Core Explanation

Sidecar can tail/transform file logs.

### Example / Visualization

```text
app file→sidecar
```

### Why It Matters

Sometimes useful for legacy apps.

### Practical Use

Prefer stdout where possible.

# Part 124 — Proxy Sidecar Awareness

### Core Explanation

Service mesh/data-plane proxy can run alongside app.

### Example / Visualization

```text
app↔proxy
```

### Why It Matters

Provides mTLS/traffic telemetry.

### Practical Use

Operational overhead.

# Part 125 — Ambassador Pattern Awareness

### Core Explanation

Sidecar proxy handles outbound/inbound communication to external systems.

### Example / Visualization

```text
app→ambassador→external
```

### Why It Matters

Encapsulates protocol/auth.

### Practical Use

Use when platform supports/needs it.

# Part 126 — Adapter Sidecar Awareness

### Core Explanation

Sidecar transforms app output/interface for platform consumption.

### Example / Visualization

```text
legacy app→adapter
```

### Why It Matters

Useful for legacy integration.

### Practical Use

Avoid if app can be modified cleanly.

# Part 127 — Job Retry

### Core Explanation

Job controller can retry failed Pods.

### Example / Visualization

```text
backoffLimit awareness
```

### Why It Matters

Useful for finite work.

### Practical Use

Make job idempotent.

# Part 128 — CronJob Concurrency

### Core Explanation

Scheduled jobs may overlap if previous run is slow.

### Example / Visualization

```text
Allow/Forbid/Replace concepts
```

### Why It Matters

Overlap can corrupt or duplicate work.

### Practical Use

Choose concurrency policy.

# Part 129 — Job TTL Awareness

### Core Explanation

Finished Jobs can be cleaned after a retention period.

### Example / Visualization

```text
ttlSecondsAfterFinished awareness
```

### Why It Matters

Reduces clutter.

### Practical Use

Keep enough history for debugging.

# Part 130 — ServiceAccount

### Core Explanation

Identity assigned to Pods for Kubernetes/API or external workload integrations.

### Example / Visualization

```text
Pod→ServiceAccount
```

### Why It Matters

Avoid default shared identity.

### Practical Use

Use one per workload when needed.

# Part 131 — Default ServiceAccount Caution

### Core Explanation

All Pods in a namespace may otherwise share default identity.

### Example / Visualization

```text
default SA
```

### Why It Matters

Weakens least privilege.

### Practical Use

Create scoped accounts.

# Part 132 — RBAC Awareness

### Core Explanation

Role/ClusterRole and bindings authorize Kubernetes API actions.

### Example / Visualization

```text
SA→RoleBinding→permissions
```

### Why It Matters

Controls what workloads/operators can do.

### Practical Use

Apps often need no Kubernetes API access.

# Part 133 — Automount Token Caution

### Core Explanation

Service-account token need not be mounted into Pods that do not use Kubernetes API.

### Example / Visualization

```text
automount off
```

### Why It Matters

Reduces credential exposure.

### Practical Use

Disable where unnecessary.

# Part 134 — Pod Security Context

### Core Explanation

Defines UID/GID, fsGroup, privilege controls, seccomp, etc.

### Example / Visualization

```text
runAsNonRoot
```

### Why It Matters

Important runtime hardening.

### Practical Use

Align with image user.

# Part 135 — runAsNonRoot

### Core Explanation

Requires container to run non-root.

### Example / Visualization

```text
securityContext
```

### Why It Matters

Prevents accidental root image execution.

### Practical Use

Set explicitly.

# Part 136 — readOnlyRootFilesystem

### Core Explanation

Mounts root filesystem read-only.

### Example / Visualization

```text
read-only root
```

### Why It Matters

Limits persistence/tampering.

### Practical Use

Provide writable temp mounts.

# Part 137 — allowPrivilegeEscalation

### Core Explanation

Can prevent processes gaining more privileges.

### Example / Visualization

```text
false
```

### Why It Matters

Defense in depth.

### Practical Use

Use for normal apps.

# Part 138 — Capabilities

### Core Explanation

Drop Linux capabilities not required.

### Example / Visualization

```text
drop: ALL
```

### Why It Matters

Reduces kernel attack surface.

### Practical Use

Add only specific required capabilities.

# Part 139 — seccompProfile Awareness

### Core Explanation

Apply restricted/default syscall profile.

### Example / Visualization

```text
RuntimeDefault
```

### Why It Matters

Strong default hardening.

### Practical Use

Test app compatibility.

# Part 140 — ImagePullSecret

### Core Explanation

Credential used to pull from private registry.

### Example / Visualization

```text
Pod→registry
```

### Why It Matters

Needed if workload identity/native registry auth unavailable.

### Practical Use

Scope and rotate.

# Part 141 — Registry Digest Pinning

### Core Explanation

Reference image by immutable digest.

### Example / Visualization

```text
image@sha256:...
```

### Why It Matters

Prevents tag drift.

### Practical Use

Use in production promotion.

# Part 142 — Admission Policy Awareness

### Core Explanation

Cluster can enforce image/security/resource policies at admission.

### Example / Visualization

```text
manifest→policy→accept/deny
```

### Why It Matters

Automates guardrails.

### Practical Use

Platform topic but app teams must satisfy it.

# Part 143 — NetworkPolicy Security

### Core Explanation

Restrict app ingress/egress.

### Example / Visualization

```text
default deny + allow
```

### Why It Matters

Limits lateral movement.

### Practical Use

Test DNS/monitoring paths.

# Part 144 — Secret Encryption Awareness

### Core Explanation

Secret objects should be protected by cluster-at-rest encryption and access controls.

### Example / Visualization

```text
etcd encryption awareness
```

### Why It Matters

Base64 alone is not protection.

### Practical Use

Platform operators configure it.

# Part 145 — Pod Logs

### Core Explanation

Container stdout/stderr can be retrieved/collected.

### Example / Visualization

```text
kubectl logs
```

### Why It Matters

First-line application diagnostics.

### Practical Use

Centralize for production.

# Part 146 — Previous Container Logs

### Core Explanation

After restart, previous container logs may reveal crash reason.

### Example / Visualization

```text
logs --previous concept
```

### Why It Matters

Useful for CrashLoopBackOff.

### Practical Use

Collect centrally before loss.

# Part 147 — kubectl get

### Core Explanation

Lists object state at a glance.

### Example / Visualization

```text
get pods/deploy/svc
```

### Why It Matters

Useful first step.

### Practical Use

Check namespace.

# Part 148 — kubectl describe

### Core Explanation

Shows spec, status, conditions, and events.

### Example / Visualization

```text
describe pod
```

### Why It Matters

Critical for scheduling/image/probe issues.

### Practical Use

Events often explain root cause.

# Part 149 — kubectl logs

### Core Explanation

Shows container application logs.

### Example / Visualization

```text
logs pod -c app
```

### Why It Matters

Diagnoses runtime behavior.

### Practical Use

Choose correct container.

# Part 150 — kubectl exec Awareness

### Core Explanation

Runs a command inside a container for authorized debugging.

### Example / Visualization

```text
exec shell/command
```

### Why It Matters

Useful but minimal images may lack shell.

### Practical Use

Do not modify production state manually.

# Part 151 — kubectl port-forward Awareness

### Core Explanation

Temporarily forwards local port to Pod/Service for debugging.

### Example / Visualization

```text
localhost→Pod
```

### Why It Matters

Useful in labs/debug.

### Practical Use

Not a production exposure mechanism.

# Part 152 — Events

### Core Explanation

Kubernetes emits scheduling, image, probe, volume, and lifecycle events.

### Example / Visualization

```text
FailedScheduling/ImagePull
```

### Why It Matters

High-value troubleshooting source.

### Practical Use

Events may have limited retention.

# Part 153 — CrashLoopBackOff

### Core Explanation

Container repeatedly exits and kubelet backs off restarting.

### Example / Visualization

```text
start→crash→backoff
```

### Why It Matters

Usually app/config/secret/startup failure.

### Practical Use

Inspect logs and exit code.

# Part 154 — ImagePullBackOff

### Core Explanation

Image pull repeatedly fails.

### Example / Visualization

```text
bad image/auth/registry
```

### Why It Matters

Occurs before app starts.

### Practical Use

Check image reference and credentials.

# Part 155 — ErrImagePull Awareness

### Core Explanation

Initial image pull failure state.

### Example / Visualization

```text
pull failed
```

### Why It Matters

Often precedes backoff.

### Practical Use

Inspect events.

# Part 156 — Pending

### Core Explanation

Pod cannot be scheduled or volume not ready.

### Example / Visualization

```text
Pending
```

### Why It Matters

Could be resources, selectors, taints, PVC.

### Practical Use

Describe Pod.

# Part 157 — ContainerCreating

### Core Explanation

Pod scheduled but runtime is creating containers/volumes/network.

### Example / Visualization

```text
ContainerCreating
```

### Why It Matters

May wait on image/volume/CNI.

### Practical Use

Inspect events.

# Part 158 — OOMKilled

### Core Explanation

Container terminated due to memory limit/pressure.

### Example / Visualization

```text
OOMKilled
```

### Why It Matters

Common resource problem.

### Practical Use

Inspect memory metrics and limit.

# Part 159 — Readiness Failure

### Core Explanation

Pod runs but Service has not included it as ready endpoint.

### Example / Visualization

```text
Running 1/1? readiness false
```

### Why It Matters

Traffic issue without crash.

### Practical Use

Test readiness endpoint.

# Part 160 — Liveness Failure

### Core Explanation

Repeated liveness failures restart container.

### Example / Visualization

```text
Unhealthy→restart
```

### Why It Matters

Bad probe can create outage.

### Practical Use

Keep liveness minimal.

# Part 161 — Service Has No Endpoints

### Core Explanation

Selectors do not match ready Pods.

### Example / Visualization

```text
svc→0 endpoints
```

### Why It Matters

Common routing failure.

### Practical Use

Compare labels/selectors/readiness.

# Part 162 — DNS Failure

### Core Explanation

Pod cannot resolve Service names.

### Example / Visualization

```text
DNS error
```

### Why It Matters

Could be cluster DNS or policy.

### Practical Use

Test resolver and Service existence.

# Part 163 — Connection Refused

### Core Explanation

DNS works but target port has no listener.

### Example / Visualization

```text
ECONNREFUSED
```

### Why It Matters

Different layer from DNS.

### Practical Use

Check targetPort/app bind.

# Part 164 — Ingress 404

### Core Explanation

Ingress controller cannot match host/path or backend.

### Example / Visualization

```text
404 at edge
```

### Why It Matters

Routing config issue.

### Practical Use

Inspect rule and controller.

# Part 165 — Ingress 502/503

### Core Explanation

Ingress matched route but backend endpoints unhealthy/unreachable.

### Example / Visualization

```text
edge→service failure
```

### Why It Matters

Check Service endpoints/readiness/network policy.

### Practical Use

Trace from edge inward.

# Part 166 — PVC Pending

### Core Explanation

Claim cannot bind/provision storage.

### Example / Visualization

```text
PVC Pending
```

### Why It Matters

StorageClass/quota/provisioner issue.

### Practical Use

Describe PVC.

# Part 167 — Permission Denied on Volume

### Core Explanation

Container UID/GID cannot access mounted filesystem.

### Example / Visualization

```text
EACCES
```

### Why It Matters

Common with non-root images.

### Practical Use

Use fsGroup/ownership appropriately.

# Part 168 — Scheduling Failure

### Core Explanation

Requests exceed available capacity or affinity/taint rules block placement.

### Example / Visualization

```text
FailedScheduling
```

### Why It Matters

Not an application code problem.

### Practical Use

Inspect scheduler event.

# Part 169 — Noisy Neighbor

### Core Explanation

Another workload consumes shared node resources.

### Example / Visualization

```text
latency/evictions
```

### Why It Matters

Requests/limits/quotas matter.

### Practical Use

Use resource governance.

# Part 170 — Eviction Awareness

### Core Explanation

Pods may be evicted under node pressure.

### Example / Visualization

```text
MemoryPressure/DiskPressure
```

### Why It Matters

Different from app crash.

### Practical Use

Inspect node conditions.

# Part 171 — Rollout Stuck

### Core Explanation

New Pods fail readiness, pull, schedule, or crash so Deployment cannot progress.

### Example / Visualization

```text
rollout timeout
```

### Why It Matters

Do not keep applying repeatedly.

### Practical Use

Inspect new ReplicaSet/Pods.

# Part 172 — Rollback Decision

### Core Explanation

If new revision is unhealthy and cause is not quickly reversible, restore last known good.

### Example / Visualization

```text
v2→v1
```

### Why It Matters

Minimizes incident time.

### Practical Use

Ensure migration compatibility.

# Part 173 — Telemetry Correlation

### Core Explanation

Include pod, namespace, node, version, trace ID, and request ID in observability where useful.

### Example / Visualization

```text
logs/metrics/traces
```

### Why It Matters

Connects app failures to deployment state.

### Practical Use

Avoid high-cardinality metric labels.

# Part 174 — Final Kubernetes Deployment Mental Model

### Core Explanation

Kubernetes application deployment is declarative reconciliation of Pods, networking, config, secrets, storage, health, resources, scaling, and rollout behavior around immutable application images.

### Example / Visualization

```text
Image+Manifest→Controllers→Healthy Service
```

### Why It Matters

Success depends on designing the application for replacement, scaling, and coexistence.

### Practical Use

Treat manifests and image digests as release artifacts.

# Part 175 — Helm Awareness

### Core Explanation

Helm packages Kubernetes manifests using charts, values, templates, and releases.

### Example / Visualization

```text
Chart + values → manifests
```

### Why It Matters

Useful for reusable application packaging.

### Practical Use

Avoid excessive template logic.

# Part 176 — Helm Values

### Core Explanation

Values customize chart parameters.

### Example / Visualization

```text
replicas/image/resources
```

### Why It Matters

Separates defaults from environment config.

### Practical Use

Version values per environment.

# Part 177 — Kustomize Awareness

### Core Explanation

Kustomize composes base manifests with overlays/patches.

### Example / Visualization

```text
base + prod overlay
```

### Why It Matters

Useful without templating language.

### Practical Use

Keep overlays small.

# Part 178 — Base/Overlay Pattern

### Core Explanation

Shared manifests live in base; environment changes live in overlays.

### Example / Visualization

```text
base→dev/prod
```

### Why It Matters

Reduces duplication.

### Practical Use

Do not fork whole manifests.

# Part 179 — GitOps

### Core Explanation

Git stores desired deployment state; a controller reconciles it to cluster.

### Example / Visualization

```text
Git→GitOps Controller→Cluster
```

### Why It Matters

Provides audit and drift correction.

### Practical Use

Separate app code repo and environment repo as appropriate.

# Part 180 — Drift

### Core Explanation

Runtime state differs from declared source of truth.

### Example / Visualization

```text
manual kubectl edit
```

### Why It Matters

Drift makes environments unpredictable.

### Practical Use

Let controller reconcile.

# Part 181 — Promotion via Pull Request

### Core Explanation

Promote a known image digest/config by changing Git and reviewing PR.

### Example / Visualization

```text
digest v2→prod PR
```

### Why It Matters

Provides audit trail.

### Practical Use

Do not rebuild image.

# Part 182 — Environment Repository Awareness

### Core Explanation

Deployment config may live in dedicated Git repo.

### Example / Visualization

```text
env repo
```

### Why It Matters

Separates application build from environment promotion.

### Practical Use

Define ownership.

# Supplemental Deep-Study Layer — Kubernetes Application Deployment

> The original uploaded course is preserved in full. This enhancement adds deeper architecture, implementation, operational, security, troubleshooting, cost, resilience, and recovery coverage.

Recommended study sequence:

```text
Concept
  ↓
Architecture / Platform Contract
  ↓
Code / Manifest / Diagram
  ↓
Normal Behavior
  ↓
Failure / Overload
  ↓
Security + Observability
  ↓
Recovery / Rollback
```


## Advanced Deep Dive 1 — Desired-State Ownership

### Concept

Treat Git/manifests as the source of desired application state and avoid using generated Pods/ReplicaSets as configuration.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Desired-State Ownership**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Treat Git/manifests as the source of desired application state and avoid using generated Pods/ReplicaSets as configuration. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 2 — Controller Reconciliation

### Concept

Understand that controllers repeatedly compare desired and actual state; troubleshooting begins by identifying the owning controller.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Controller Reconciliation**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Understand that controllers repeatedly compare desired and actual state; troubleshooting begins by identifying the owning controller. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 3 — Server-Side Apply Awareness

### Concept

Field ownership matters when multiple tools manage one object; avoid uncoordinated writers that fight over the same fields.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Server-Side Apply Awareness**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Field ownership matters when multiple tools manage one object; avoid uncoordinated writers that fight over the same fields. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 4 — Manifest Schema Validation

### Concept

Validate apiVersion, kind, required fields, selectors, resources, probes, and policy before deployment reaches the cluster.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Manifest Schema Validation**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Validate apiVersion, kind, required fields, selectors, resources, probes, and policy before deployment reaches the cluster. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 5 — Immutable Image Reference

### Concept

Deploy by immutable digest for deterministic promotion, rollback, and incident traceability.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Immutable Image Reference**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Deploy by immutable digest for deterministic promotion, rollback, and incident traceability. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 6 — Label Taxonomy

### Concept

Standardize application, component, version, environment, and owner labels so Services, policies, telemetry, and tooling agree.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Label Taxonomy**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Standardize application, component, version, environment, and owner labels so Services, policies, telemetry, and tooling agree. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 7 — Selector Immutability Awareness

### Concept

Treat controller selectors as stable identity because changing them can be restricted or can orphan workloads.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Selector Immutability Awareness**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Treat controller selectors as stable identity because changing them can be restricted or can orphan workloads. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 8 — Service Selector Safety

### Concept

Verify Service selectors match only the intended ready Pods so traffic cannot reach the wrong component/version.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Service Selector Safety**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Verify Service selectors match only the intended ready Pods so traffic cannot reach the wrong component/version. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 9 — Namespace Ownership

### Concept

Use namespaces for organization, quota, policy, and ownership while remembering they are not a complete hard security boundary by themselves.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Namespace Ownership**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use namespaces for organization, quota, policy, and ownership while remembering they are not a complete hard security boundary by themselves. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 10 — Namespace Production Isolation

### Concept

Use stronger isolation for production when risk requires it, potentially including separate clusters/accounts/projects.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Namespace Production Isolation**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use stronger isolation for production when risk requires it, potentially including separate clusters/accounts/projects. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 11 — Deployment Failure-State Capacity

### Concept

Choose replicas and rollout settings so the service remains above minimum capacity during node/zone loss and deployment.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Deployment Failure-State Capacity**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Choose replicas and rollout settings so the service remains above minimum capacity during node/zone loss and deployment. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 12 — maxSurge Capacity Budget

### Concept

Ensure the cluster has enough headroom for temporary surge Pods during rollout.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **maxSurge Capacity Budget**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Ensure the cluster has enough headroom for temporary surge Pods during rollout. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 13 — maxUnavailable SLO Mapping

### Concept

Choose allowed unavailability from the service SLO rather than defaulting blindly.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **maxUnavailable SLO Mapping**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Choose allowed unavailability from the service SLO rather than defaulting blindly. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 14 — Progress Deadline

### Concept

Use rollout progress limits/automation so a new revision that never becomes ready fails visibly instead of hanging indefinitely.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Progress Deadline**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use rollout progress limits/automation so a new revision that never becomes ready fails visibly instead of hanging indefinitely. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 15 — Revision Retention

### Concept

Keep enough previous ReplicaSets/releases for recovery without retaining unlimited history.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Revision Retention**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Keep enough previous ReplicaSets/releases for recovery without retaining unlimited history. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 16 — Rollback Compatibility

### Concept

Ensure old application versions can still run against current schema/config when rollback is part of the recovery plan.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Rollback Compatibility**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Ensure old application versions can still run against current schema/config when rollback is part of the recovery plan. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 17 — Canary Workload Separation

### Concept

Represent stable and canary versions with labels/services/routes that make traffic percentage and telemetry distinguishable.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Canary Workload Separation**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Represent stable and canary versions with labels/services/routes that make traffic percentage and telemetry distinguishable. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 18 — Canary Baseline Comparison

### Concept

Compare candidate error, latency, saturation, and business outcomes against stable version before increasing traffic.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Canary Baseline Comparison**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Compare candidate error, latency, saturation, and business outcomes against stable version before increasing traffic. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 19 — Unknown Canary Telemetry

### Concept

Treat missing or stale analysis data as UNKNOWN and halt promotion.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Unknown Canary Telemetry**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Treat missing or stale analysis data as UNKNOWN and halt promotion. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 20 — Blue-Green Switch Safety

### Concept

Validate green environment and shared data compatibility before moving the Service/Gateway selector or route.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Blue-Green Switch Safety**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Validate green environment and shared data compatibility before moving the Service/Gateway selector or route. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 21 — Shadow Traffic Side-Effect Control

### Concept

Ensure mirrored traffic cannot execute real writes or duplicate irreversible actions.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Shadow Traffic Side-Effect Control**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Ensure mirrored traffic cannot execute real writes or duplicate irreversible actions. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 22 — ClusterIP Default

### Concept

Use ClusterIP for internal services unless an external exposure requirement exists.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **ClusterIP Default**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use ClusterIP for internal services unless an external exposure requirement exists. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 23 — Headless Service

### Concept

Use headless discovery only when the application needs direct endpoint identity and can handle endpoint churn.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Headless Service**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use headless discovery only when the application needs direct endpoint identity and can handle endpoint churn. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 24 — EndpointSlice Diagnosis

### Concept

Inspect EndpointSlices when Service traffic fails even though Pods appear healthy.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **EndpointSlice Diagnosis**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Inspect EndpointSlices when Service traffic fails even though Pods appear healthy. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 25 — Readiness and Service Membership

### Concept

Remember that an unready Pod can exist and run while being removed from normal Service traffic.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Readiness and Service Membership**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Remember that an unready Pod can exist and run while being removed from normal Service traffic. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 26 — Ingress Controller Dependency

### Concept

An Ingress object requires a compatible controller; include controller health and configuration in the edge dependency model.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Ingress Controller Dependency**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

An Ingress object requires a compatible controller; include controller health and configuration in the edge dependency model. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 27 — Gateway API Role Separation

### Concept

Use Gateway/Route separation to distinguish infrastructure ownership from application routing ownership when supported.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Gateway API Role Separation**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use Gateway/Route separation to distinguish infrastructure ownership from application routing ownership when supported. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 28 — TLS Certificate Lifecycle

### Concept

Automate certificate issuance, renewal, rotation, and expiry monitoring for ingress/gateway endpoints.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **TLS Certificate Lifecycle**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Automate certificate issuance, renewal, rotation, and expiry monitoring for ingress/gateway endpoints. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 29 — ExternalDNS Permission Scope

### Concept

Give DNS automation narrowly scoped permissions to only the zones/records it owns.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **ExternalDNS Permission Scope**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Give DNS automation narrowly scoped permissions to only the zones/records it owns. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 30 — Default-Deny NetworkPolicy

### Concept

Start from deny-by-default where supported, then add explicit application flows.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Default-Deny NetworkPolicy**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Start from deny-by-default where supported, then add explicit application flows. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 31 — DNS Egress with NetworkPolicy

### Concept

Allow required DNS resolution when enforcing egress policy; otherwise workloads can fail before reaching services.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **DNS Egress with NetworkPolicy**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Allow required DNS resolution when enforcing egress policy; otherwise workloads can fail before reaching services. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 32 — NetworkPolicy Dependency Matrix

### Concept

Document every legitimate service-to-service and egress path before enforcing restrictive policy.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **NetworkPolicy Dependency Matrix**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Document every legitimate service-to-service and egress path before enforcing restrictive policy. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 33 — ConfigMap Update Semantics

### Concept

Understand whether the application reads environment variables once or mounted files dynamically and choose rollout/reload behavior accordingly.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **ConfigMap Update Semantics**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Understand whether the application reads environment variables once or mounted files dynamically and choose rollout/reload behavior accordingly. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 34 — Secret Delivery Choice

### Concept

Choose environment, mounted volume, CSI/external secret projection, or workload identity based on exposure and rotation needs.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Secret Delivery Choice**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Choose environment, mounted volume, CSI/external secret projection, or workload identity based on exposure and rotation needs. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 35 — Secret Rotation Test

### Concept

Verify that applications reload files or reconnect after secret changes instead of assuming rotation is automatic.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Secret Rotation Test**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Verify that applications reload files or reconnect after secret changes instead of assuming rotation is automatic. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 36 — Config Checksum Rollout

### Concept

Use a deterministic config hash annotation or version change to trigger Pod replacement when startup-only configuration changes.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Config Checksum Rollout**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use a deterministic config hash annotation or version change to trigger Pod replacement when startup-only configuration changes. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 37 — Liveness Minimalism

### Concept

Keep liveness local to process progress so external dependency outages do not create restart storms.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Liveness Minimalism**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Keep liveness local to process progress so external dependency outages do not create restart storms. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 38 — Readiness Dependency Classification

### Concept

Only mark not-ready for dependencies required to serve that Pod's intended traffic.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Readiness Dependency Classification**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Only mark not-ready for dependencies required to serve that Pod's intended traffic. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 39 — Startup Probe Budget

### Concept

Use startup probes for legitimately slow initialization instead of inflating liveness delays.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Startup Probe Budget**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use startup probes for legitimately slow initialization instead of inflating liveness delays. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 40 — Probe Cost Budget

### Concept

Keep probes cheap and independent of expensive database queries or remote SaaS calls.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Probe Cost Budget**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Keep probes cheap and independent of expensive database queries or remote SaaS calls. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 41 — Probe Failure Threshold

### Concept

Tune probe period/timeout/failure threshold to distinguish real failure from brief jitter.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Probe Failure Threshold**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Tune probe period/timeout/failure threshold to distinguish real failure from brief jitter. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 42 — Graceful Shutdown Order

### Concept

Make readiness false, stop new work, drain, close clients, flush telemetry, then exit before grace period.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
SIGTERM / termination starts
   ↓
readiness becomes false
   ↓
Service stops new traffic
   ↓
finish in-flight requests/jobs
   ↓
close DB/broker/HTTP clients
   ↓
exit before grace period ends
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Graceful Shutdown Order**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Make readiness false, stop new work, drain, close clients, flush telemetry, then exit before grace period. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 43 — preStop Caution

### Concept

Use preStop only as a supplement; the application must still handle SIGTERM correctly.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
SIGTERM / termination starts
   ↓
readiness becomes false
   ↓
Service stops new traffic
   ↓
finish in-flight requests/jobs
   ↓
close DB/broker/HTTP clients
   ↓
exit before grace period ends
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **preStop Caution**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use preStop only as a supplement; the application must still handle SIGTERM correctly. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 44 — Termination Grace Sizing

### Concept

Measure worst-case drain time and set terminationGracePeriodSeconds with explicit buffer.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
SIGTERM / termination starts
   ↓
readiness becomes false
   ↓
Service stops new traffic
   ↓
finish in-flight requests/jobs
   ↓
close DB/broker/HTTP clients
   ↓
exit before grace period ends
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Termination Grace Sizing**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Measure worst-case drain time and set terminationGracePeriodSeconds with explicit buffer. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 45 — Connection Draining

### Concept

Coordinate load balancer/Service removal with process shutdown so old Pods finish in-flight connections.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Connection Draining**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Coordinate load balancer/Service removal with process shutdown so old Pods finish in-flight connections. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 46 — Resource Requests from Measurements

### Concept

Set CPU/memory requests from observed normal demand because requests control scheduling and HPA utilization calculations.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Resource Requests from Measurements**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Set CPU/memory requests from observed normal demand because requests control scheduling and HPA utilization calculations. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 47 — Memory Limit Headroom

### Concept

Set memory limits with realistic peak headroom and investigate leaks rather than continuously raising limits.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Memory Limit Headroom**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Set memory limits with realistic peak headroom and investigate leaks rather than continuously raising limits. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 48 — CPU Throttling Observability

### Concept

Track throttled CPU time because a CPU-capped Pod can have high tail latency without obvious crash.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **CPU Throttling Observability**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Track throttled CPU time because a CPU-capped Pod can have high tail latency without obvious crash. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 49 — OOMKilled Root Cause

### Concept

Distinguish too-low limits, traffic spikes, memory leaks, cache growth, allocator behavior, and node pressure.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **OOMKilled Root Cause**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Distinguish too-low limits, traffic spikes, memory leaks, cache growth, allocator behavior, and node pressure. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 50 — QoS Class Awareness

### Concept

Understand how requests/limits influence QoS and eviction behavior under node pressure.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **QoS Class Awareness**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Understand how requests/limits influence QoS and eviction behavior under node pressure. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 51 — LimitRange Defaults

### Concept

Use namespace defaults carefully so developers understand the resources automatically applied to Pods.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **LimitRange Defaults**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use namespace defaults carefully so developers understand the resources automatically applied to Pods. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 52 — ResourceQuota Capacity

### Concept

Use quotas to bound namespace resource/cost impact without making legitimate deployments permanently unschedulable.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **ResourceQuota Capacity**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use quotas to bound namespace resource/cost impact without making legitimate deployments permanently unschedulable. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 53 — Pending Pod Evidence

### Concept

Use scheduler events to distinguish insufficient resources, node constraints, taints, or unbound storage.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```bash
kubectl get pods -n app
kubectl describe pod <pod> -n app
kubectl logs <pod> -c app -n app
kubectl logs <pod> -c app -n app --previous
kubectl get events -n app --sort-by=.lastTimestamp
kubectl get endpointslices -n app
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Pending Pod Evidence**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use scheduler events to distinguish insufficient resources, node constraints, taints, or unbound storage. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 54 — Topology Spread

### Concept

Spread replicas across nodes/zones without making placement so strict that Pods become Pending.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Topology Spread**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Spread replicas across nodes/zones without making placement so strict that Pods become Pending. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 55 — Anti-Affinity Trade-Off

### Concept

Use required anti-affinity only where strict separation is worth the scheduling risk; prefer flexible spread for many workloads.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Anti-Affinity Trade-Off**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use required anti-affinity only where strict separation is worth the scheduling risk; prefer flexible spread for many workloads. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 56 — Node Affinity

### Concept

Use node affinity when hardware/location requirements are genuine, not as a substitute for good platform labels.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Node Affinity**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use node affinity when hardware/location requirements are genuine, not as a substitute for good platform labels. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 57 — Taints and Tolerations

### Concept

Use taints to protect specialized nodes and tolerations only for workloads intentionally allowed there.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Taints and Tolerations**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use taints to protect specialized nodes and tolerations only for workloads intentionally allowed there. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 58 — PriorityClass Governance

### Concept

Reserve high priorities for genuinely critical workloads to avoid starvation/preemption chaos.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **PriorityClass Governance**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Reserve high priorities for genuinely critical workloads to avoid starvation/preemption chaos. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 59 — PodDisruptionBudget

### Concept

Protect availability from voluntary disruptions while allowing enough flexibility for node maintenance.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **PodDisruptionBudget**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Protect availability from voluntary disruptions while allowing enough flexibility for node maintenance. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 60 — PDB vs Involuntary Failure

### Concept

Remember PDBs constrain voluntary eviction but cannot prevent node crashes or all failure modes.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **PDB vs Involuntary Failure**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Remember PDBs constrain voluntary eviction but cannot prevent node crashes or all failure modes. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 61 — HPA Prerequisite Requests

### Concept

CPU/memory HPA depends on meaningful resource requests; bad requests produce misleading scaling.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **HPA Prerequisite Requests**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

CPU/memory HPA depends on meaningful resource requests; bad requests produce misleading scaling. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 62 — HPA Stabilization

### Concept

Use scale-up/down policies and stabilization to avoid oscillation and sudden dependency overload.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **HPA Stabilization**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use scale-up/down policies and stabilization to avoid oscillation and sudden dependency overload. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 63 — Queue-Lag Worker Scaling

### Concept

Scale asynchronous workers from queue age/lag when that better represents work demand than CPU.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Queue-Lag Worker Scaling**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Scale asynchronous workers from queue age/lag when that better represents work demand than CPU. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 64 — Autoscaling Downstream Ceiling

### Concept

Set maxReplicas and concurrency so scale-out cannot exceed database, broker, or partner capacity.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Autoscaling Downstream Ceiling**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Set maxReplicas and concurrency so scale-out cannot exceed database, broker, or partner capacity. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 65 — Scale-to-Zero Cold Start

### Concept

Use event-driven scale-to-zero only when startup and backlog delay fit the business SLO.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Scale-to-Zero Cold Start**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use event-driven scale-to-zero only when startup and backlog delay fit the business SLO. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 66 — Cluster Autoscaler Interaction

### Concept

Application Pods can remain Pending while node capacity grows; startup and PDB/topology rules affect the eventual scheduling outcome.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Cluster Autoscaler Interaction**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Application Pods can remain Pending while node capacity grows; startup and PDB/topology rules affect the eventual scheduling outcome. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 67 — PVC as Durable Boundary

### Concept

Treat PVC-backed data as independent from Pod lifetime and include backup/recovery explicitly.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **PVC as Durable Boundary**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Treat PVC-backed data as independent from Pod lifetime and include backup/recovery explicitly. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 68 — StorageClass Policy

### Concept

Understand performance, zone binding, reclaim, encryption, expansion, and snapshot behavior of the selected StorageClass.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **StorageClass Policy**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Understand performance, zone binding, reclaim, encryption, expansion, and snapshot behavior of the selected StorageClass. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 69 — Reclaim Policy

### Concept

Use Retain/Delete according to data criticality and decommission workflow; deletion can be irreversible.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Manifest
   ↓
Admission policy
   ├─ image digest pinned?
   ├─ runAsNonRoot?
   ├─ resource requests present?
   └─ approved registry?
   ↓
accept / reject
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Reclaim Policy**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use Retain/Delete according to data criticality and decommission workflow; deletion can be irreversible. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 70 — Volume Binding Topology

### Concept

Storage provisioning may be zone-aware; schedule and storage topology must be compatible.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Volume Binding Topology**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Storage provisioning may be zone-aware; schedule and storage topology must be compatible. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 71 — Access Mode Reality

### Concept

Do not assume ReadWriteMany is available or performant on every backend.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Access Mode Reality**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Do not assume ReadWriteMany is available or performant on every backend. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 72 — Volume Expansion

### Concept

Plan filesystem/application actions and monitoring after PVC size increases.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Volume Expansion**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Plan filesystem/application actions and monitoring after PVC size increases. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 73 — Volume Snapshot Consistency

### Concept

A storage snapshot is not automatically application-consistent; quiesce/DB-native backup may be required.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Volume Snapshot Consistency**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

A storage snapshot is not automatically application-consistent; quiesce/DB-native backup may be required. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 74 — StatefulSet Identity

### Concept

Stable Pod names and per-replica PVCs do not solve database replication or consensus by themselves.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **StatefulSet Identity**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Stable Pod names and per-replica PVCs do not solve database replication or consensus by themselves. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 75 — StatefulSet Rolling Risk

### Concept

Stateful systems may require ordered upgrade/health semantics more specific than a generic Deployment.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **StatefulSet Rolling Risk**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Stateful systems may require ordered upgrade/health semantics more specific than a generic Deployment. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 76 — Init Container Failure

### Concept

An init container that loops/fails prevents the application from starting; keep setup bounded and observable.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Init Container Failure**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

An init container that loops/fails prevents the application from starting; keep setup bounded and observable. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 77 — Migration Job Singleton

### Concept

Run schema migration as one controlled Job rather than from every application Pod.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Migration Job Singleton**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Run schema migration as one controlled Job rather than from every application Pod. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 78 — Migration Locking / Idempotency

### Concept

Make migration jobs restartable, concurrency-safe, and able to report exactly which migration step failed.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Migration Locking / Idempotency**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Make migration jobs restartable, concurrency-safe, and able to report exactly which migration step failed. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 79 — CronJob Concurrency

### Concept

Set Allow/Forbid/Replace according to whether overlapping scheduled executions are safe.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **CronJob Concurrency**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Set Allow/Forbid/Replace according to whether overlapping scheduled executions are safe. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 80 — CronJob Missed Schedule

### Concept

Decide how delayed/missed jobs behave after controller downtime or long suspension.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **CronJob Missed Schedule**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Decide how delayed/missed jobs behave after controller downtime or long suspension. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 81 — Job Idempotency

### Concept

A retried Job must not duplicate irreversible business effects.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Job Idempotency**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

A retried Job must not duplicate irreversible business effects. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 82 — Sidecar Lifecycle Cost

### Concept

Account for sidecar CPU/memory/startup/shutdown because every Pod replica multiplies the helper cost.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Sidecar Lifecycle Cost**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Account for sidecar CPU/memory/startup/shutdown because every Pod replica multiplies the helper cost. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 83 — Service Mesh Sidecar Readiness

### Concept

Proxy readiness and application readiness can interact; verify traffic is not sent before both are usable.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Service Mesh Sidecar Readiness**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Proxy readiness and application readiness can interact; verify traffic is not sent before both are usable. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 84 — ServiceAccount Per Workload

### Concept

Use dedicated identities for workloads that need Kubernetes/cloud APIs; avoid shared default identity.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **ServiceAccount Per Workload**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use dedicated identities for workloads that need Kubernetes/cloud APIs; avoid shared default identity. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 85 — Disable Token Automount

### Concept

Disable service-account token mounting when the workload does not call Kubernetes API.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: orders-api
automountServiceAccountToken: false
```

```text
Pod -> ServiceAccount / workload identity
      ↓
least-privilege authorization
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Disable Token Automount**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Disable service-account token mounting when the workload does not call Kubernetes API. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 86 — RBAC Least Privilege

### Concept

Grant only specific verbs/resources/namespaces required by the workload or automation.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
  seccompProfile:
    type: RuntimeDefault
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **RBAC Least Privilege**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Grant only specific verbs/resources/namespaces required by the workload or automation. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 87 — Workload Identity Federation

### Concept

Prefer platform/cloud workload identity mappings to long-lived cloud keys stored in Kubernetes Secrets.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: orders-api
automountServiceAccountToken: false
```

```text
Pod -> ServiceAccount / workload identity
      ↓
least-privilege authorization
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Workload Identity Federation**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Prefer platform/cloud workload identity mappings to long-lived cloud keys stored in Kubernetes Secrets. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 88 — Pod Security Context

### Concept

Enforce non-root, no privilege escalation, dropped capabilities, and default seccomp for ordinary application Pods.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Pod Security Context**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Enforce non-root, no privilege escalation, dropped capabilities, and default seccomp for ordinary application Pods. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 89 — Read-Only Root Filesystem

### Concept

Pair readOnlyRootFilesystem with explicit tmpfs/emptyDir mounts for legitimate temporary writes.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Read-Only Root Filesystem**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Pair readOnlyRootFilesystem with explicit tmpfs/emptyDir mounts for legitimate temporary writes. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 90 — Capability Add-Back

### Concept

After dropping ALL capabilities, add only the exact capability the process genuinely requires.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
  seccompProfile:
    type: RuntimeDefault
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Capability Add-Back**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

After dropping ALL capabilities, add only the exact capability the process genuinely requires. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 91 — Admission Policy

### Concept

Use admission guardrails for approved registries, digest pinning, resources, labels, and security context.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Manifest
   ↓
Admission policy
   ├─ image digest pinned?
   ├─ runAsNonRoot?
   ├─ resource requests present?
   └─ approved registry?
   ↓
accept / reject
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Admission Policy**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use admission guardrails for approved registries, digest pinning, resources, labels, and security context. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 92 — ImagePullSecret Scope

### Concept

Keep registry pull credentials namespace/repository scoped and rotate them if workload identity/native auth is unavailable.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **ImagePullSecret Scope**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Keep registry pull credentials namespace/repository scoped and rotate them if workload identity/native auth is unavailable. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 93 — Secret at Rest Awareness

### Concept

Kubernetes Secret objects require API/RBAC protection and platform encryption-at-rest; base64 is not encryption.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Secret at Rest Awareness**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Kubernetes Secret objects require API/RBAC protection and platform encryption-at-rest; base64 is not encryption. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 94 — GitOps Source of Truth

### Concept

Let GitOps controllers reconcile desired state and treat manual kubectl changes as temporary debugging only.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **GitOps Source of Truth**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Let GitOps controllers reconcile desired state and treat manual kubectl changes as temporary debugging only. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 95 — Drift Detection

### Concept

Use GitOps status/diff to detect manual or automated divergence from declared configuration.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Drift Detection**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use GitOps status/diff to detect manual or automated divergence from declared configuration. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 96 — Environment Repository

### Concept

Separate artifact build from environment promotion so one immutable image can move through dev/stage/prod.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Environment Repository**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Separate artifact build from environment promotion so one immutable image can move through dev/stage/prod. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 97 — Helm Values Governance

### Concept

Keep values files small, typed/documented where possible, and avoid embedding secret values.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Helm Values Governance**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Keep values files small, typed/documented where possible, and avoid embedding secret values. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 98 — Helm Template Complexity

### Concept

Avoid turning Helm templates into a programming language full of hidden conditional behavior.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Helm Template Complexity**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Avoid turning Helm templates into a programming language full of hidden conditional behavior. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 99 — Kustomize Overlay Discipline

### Concept

Keep a common base and small overlays instead of duplicating entire manifest trees per environment.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Kustomize Overlay Discipline**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Keep a common base and small overlays instead of duplicating entire manifest trees per environment. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 100 — Promotion Pull Request

### Concept

Promote by changing the immutable digest and reviewed configuration in the environment repository.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Promotion Pull Request**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Promote by changing the immutable digest and reviewed configuration in the environment repository. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 101 — Policy Before Apply

### Concept

Run manifest schema, security, compatibility, and policy checks before the GitOps controller sees the change.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Manifest
   ↓
Admission policy
   ├─ image digest pinned?
   ├─ runAsNonRoot?
   ├─ resource requests present?
   └─ approved registry?
   ↓
accept / reject
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Policy Before Apply**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Run manifest schema, security, compatibility, and policy checks before the GitOps controller sees the change. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 102 — Smoke Test After Rollout

### Concept

Verify readiness plus at least one critical business path before declaring deployment complete.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Smoke Test After Rollout**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Verify readiness plus at least one critical business path before declaring deployment complete. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 103 — Deployment Marker

### Concept

Record image digest/revision and deploy time in logs/metrics/tracing dashboards.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Deployment Marker**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Record image digest/revision and deploy time in logs/metrics/tracing dashboards. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 104 — Kubernetes Metric Cardinality

### Concept

Use bounded labels like namespace/workload/route/version; avoid Pod UID/request ID as metric labels.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Kubernetes Metric Cardinality**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Use bounded labels like namespace/workload/route/version; avoid Pod UID/request ID as metric labels. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 105 — Pod-Level Tracing Context

### Concept

Preserve standard distributed trace context across ingress, services, workers, and messaging.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Pod-Level Tracing Context**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Preserve standard distributed trace context across ingress, services, workers, and messaging. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 106 — CrashLoopBackOff Diagnosis

### Concept

Inspect current/previous logs, exit code, config/secret changes, probes, and dependency initialization.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```bash
kubectl get pods -n app
kubectl describe pod <pod> -n app
kubectl logs <pod> -c app -n app
kubectl logs <pod> -c app -n app --previous
kubectl get events -n app --sort-by=.lastTimestamp
kubectl get endpointslices -n app
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **CrashLoopBackOff Diagnosis**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Inspect current/previous logs, exit code, config/secret changes, probes, and dependency initialization. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 107 — ImagePullBackOff Diagnosis

### Concept

Check image reference/digest, registry credentials, node egress/DNS, platform architecture, and registry health.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```bash
kubectl get pods -n app
kubectl describe pod <pod> -n app
kubectl logs <pod> -c app -n app
kubectl logs <pod> -c app -n app --previous
kubectl get events -n app --sort-by=.lastTimestamp
kubectl get endpointslices -n app
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **ImagePullBackOff Diagnosis**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Check image reference/digest, registry credentials, node egress/DNS, platform architecture, and registry health. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 108 — Service No Endpoints

### Concept

Compare Service selector, Pod labels, readiness, namespace, and EndpointSlices.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Service No Endpoints**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Compare Service selector, Pod labels, readiness, namespace, and EndpointSlices. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 109 — Ingress 502/503 Path

### Concept

Trace controller -> Service -> EndpointSlice -> Pod readiness -> NetworkPolicy -> targetPort/listener.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Ingress 502/503 Path**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Trace controller -> Service -> EndpointSlice -> Pod readiness -> NetworkPolicy -> targetPort/listener. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 110 — DNS Failure Path

### Concept

Check Service existence, cluster DNS, Pod resolver config, NetworkPolicy egress, and namespace/name correctness.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **DNS Failure Path**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Check Service existence, cluster DNS, Pod resolver config, NetworkPolicy egress, and namespace/name correctness. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 111 — PVC Pending Path

### Concept

Check StorageClass, provisioner, quota, access mode, zone constraints, and events.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **PVC Pending Path**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Check StorageClass, provisioner, quota, access mode, zone constraints, and events. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 112 — FailedScheduling Path

### Concept

Read scheduler events before changing application code; identify resources, affinity, taints, topology, or volumes.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **FailedScheduling Path**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Read scheduler events before changing application code; identify resources, affinity, taints, topology, or volumes. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 113 — Eviction Diagnosis

### Concept

Differentiate application crash from node MemoryPressure/DiskPressure/PIDPressure eviction.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Eviction Diagnosis**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Differentiate application crash from node MemoryPressure/DiskPressure/PIDPressure eviction. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 114 — Rollout Stuck

### Concept

Inspect the new ReplicaSet and Pods rather than repeatedly reapplying the same manifest.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Rollout Stuck**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Inspect the new ReplicaSet and Pods rather than repeatedly reapplying the same manifest. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 115 — Rollback Decision Rule

### Concept

Rollback quickly when the new revision is clearly unhealthy and the fix is not safer/faster than returning to known-good.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Rollback Decision Rule**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Rollback quickly when the new revision is clearly unhealthy and the fix is not safer/faster than returning to known-good. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 116 — Backup Responsibility

### Concept

Kubernetes objects can be recreated from Git, but application data, external secrets, and stateful dependencies need separate recovery.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Backup Responsibility**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Kubernetes objects can be recreated from Git, but application data, external secrets, and stateful dependencies need separate recovery. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 117 — Restore Drill

### Concept

Restore manifests/config plus durable data and validate a real business workflow in an isolated environment.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Restore Drill**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Restore manifests/config plus durable data and validate a real business workflow in an isolated environment. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 118 — Kubernetes RPO

### Concept

Define recoverable state across PVCs, databases, object storage, and messaging rather than treating cluster state as business backup.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Kubernetes RPO**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Define recoverable state across PVCs, databases, object storage, and messaging rather than treating cluster state as business backup. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 119 — Kubernetes RTO

### Concept

Measure cluster/runtime availability, storage restore, application rollout, DNS/edge, and validation time end-to-end.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Kubernetes RTO**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Measure cluster/runtime availability, storage restore, application rollout, DNS/edge, and validation time end-to-end. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 120 — Node Failure Game Day

### Concept

Terminate one lab node and verify replica rescheduling, PDB/topology behavior, capacity, and service continuity.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Node Failure Game Day**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Terminate one lab node and verify replica rescheduling, PDB/topology behavior, capacity, and service continuity. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 121 — Zone Failure Game Day

### Concept

Model loss of an entire zone and verify remaining capacity plus data-layer survivability.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Zone Failure Game Day**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Model loss of an entire zone and verify remaining capacity plus data-layer survivability. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 122 — Production Kubernetes Readiness Review

### Concept

Review source of truth, immutable image, probes, resources, security, policy, autoscaling, storage, rollout, observability, backup, and DR.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Production Kubernetes Readiness Review**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Review source of truth, immutable image, probes, resources, security, policy, autoscaling, storage, rollout, observability, backup, and DR. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

## Advanced Deep Dive 123 — Kubernetes Deployment Final Operating Model

### Concept

Treat image digest plus declarative application objects, policy, identity, state, and telemetry as one versioned production release.

### Detailed Explanation

This topic should be treated as part of an **operating contract**, not as an isolated feature. The design must make ownership, identity, resource limits, dependency assumptions, failure behavior, observability, and recovery explicit.

### Mental Model / Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Behavior

A correct design remains understandable during normal operation, rollout, restart, dependency degradation, overload, and recovery. An operator should be able to identify the current desired state, running artifact/configuration, failed boundary, and safe next action from evidence.

### Why It Works

Reliable cloud-native systems reduce hidden state and hidden coupling. Desired state, immutable artifacts, explicit identity, bounded resource use, compatibility rules, and observable failure transitions make replacement and automation safe.

### Production Scenario

For **Kubernetes Deployment Final Operating Model**, document:

```text
Owner:
Source of truth:
Runtime / platform:
Identity:
Data / state:
Dependencies:
Resource budget:
Failure behavior:
Retry / rollback:
Telemetry:
Recovery:
Security assumption:
```

### Common Problems

- Platform automation is expected to fix an application-level correctness bug.
- Failure behavior is undefined until the first incident.
- Scaling one tier overloads the next tier.
- A rollout succeeds technically but violates a business SLO.
- Security policy is based only on network location.
- Runtime state drifts from Git/IaC.
- Recovery steps depend on undocumented manual changes.

### Troubleshooting Method

```text
1. Start from the user-visible symptom.
2. Identify the current desired state and running version.
3. Check controller/runtime/edge status.
4. Validate identity, configuration, and policy.
5. Inspect resource pressure and dependency latency.
6. Correlate logs, metrics, traces, and deployment events.
7. Determine the last durable business state.
8. Roll back or recover using a tested procedure.
```

### Best Practice

Treat image digest plus declarative application objects, policy, identity, state, and telemetry as one versioned production release. Encode the rule in version-controlled configuration, automated tests/policy, observability, and a runbook.

---

# Supplemental Hands-on Lab Series

## Enhanced Practical Lab 1 — Desired-State Ownership

### Objective

Practice **Desired-State Ownership** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 2 — Controller Reconciliation

### Objective

Practice **Controller Reconciliation** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 3 — Server-Side Apply Awareness

### Objective

Practice **Server-Side Apply Awareness** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 4 — Manifest Schema Validation

### Objective

Practice **Manifest Schema Validation** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 5 — Immutable Image Reference

### Objective

Practice **Immutable Image Reference** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 6 — Label Taxonomy

### Objective

Practice **Label Taxonomy** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 7 — Selector Immutability Awareness

### Objective

Practice **Selector Immutability Awareness** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 8 — Service Selector Safety

### Objective

Practice **Service Selector Safety** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 9 — Namespace Ownership

### Objective

Practice **Namespace Ownership** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 10 — Namespace Production Isolation

### Objective

Practice **Namespace Production Isolation** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 11 — Deployment Failure-State Capacity

### Objective

Practice **Deployment Failure-State Capacity** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 12 — maxSurge Capacity Budget

### Objective

Practice **maxSurge Capacity Budget** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 13 — maxUnavailable SLO Mapping

### Objective

Practice **maxUnavailable SLO Mapping** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 14 — Progress Deadline

### Objective

Practice **Progress Deadline** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 15 — Revision Retention

### Objective

Practice **Revision Retention** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 16 — Rollback Compatibility

### Objective

Practice **Rollback Compatibility** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 17 — Canary Workload Separation

### Objective

Practice **Canary Workload Separation** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 18 — Canary Baseline Comparison

### Objective

Practice **Canary Baseline Comparison** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 19 — Unknown Canary Telemetry

### Objective

Practice **Unknown Canary Telemetry** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 20 — Blue-Green Switch Safety

### Objective

Practice **Blue-Green Switch Safety** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 21 — Shadow Traffic Side-Effect Control

### Objective

Practice **Shadow Traffic Side-Effect Control** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 22 — ClusterIP Default

### Objective

Practice **ClusterIP Default** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 23 — Headless Service

### Objective

Practice **Headless Service** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 24 — EndpointSlice Diagnosis

### Objective

Practice **EndpointSlice Diagnosis** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 25 — Readiness and Service Membership

### Objective

Practice **Readiness and Service Membership** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 26 — Ingress Controller Dependency

### Objective

Practice **Ingress Controller Dependency** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 27 — Gateway API Role Separation

### Objective

Practice **Gateway API Role Separation** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 28 — TLS Certificate Lifecycle

### Objective

Practice **TLS Certificate Lifecycle** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 29 — ExternalDNS Permission Scope

### Objective

Practice **ExternalDNS Permission Scope** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 30 — Default-Deny NetworkPolicy

### Objective

Practice **Default-Deny NetworkPolicy** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 31 — DNS Egress with NetworkPolicy

### Objective

Practice **DNS Egress with NetworkPolicy** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 32 — NetworkPolicy Dependency Matrix

### Objective

Practice **NetworkPolicy Dependency Matrix** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 33 — ConfigMap Update Semantics

### Objective

Practice **ConfigMap Update Semantics** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 34 — Secret Delivery Choice

### Objective

Practice **Secret Delivery Choice** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 35 — Secret Rotation Test

### Objective

Practice **Secret Rotation Test** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 36 — Config Checksum Rollout

### Objective

Practice **Config Checksum Rollout** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 37 — Liveness Minimalism

### Objective

Practice **Liveness Minimalism** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 38 — Readiness Dependency Classification

### Objective

Practice **Readiness Dependency Classification** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 39 — Startup Probe Budget

### Objective

Practice **Startup Probe Budget** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 40 — Probe Cost Budget

### Objective

Practice **Probe Cost Budget** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 41 — Probe Failure Threshold

### Objective

Practice **Probe Failure Threshold** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 42 — Graceful Shutdown Order

### Objective

Practice **Graceful Shutdown Order** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
SIGTERM / termination starts
   ↓
readiness becomes false
   ↓
Service stops new traffic
   ↓
finish in-flight requests/jobs
   ↓
close DB/broker/HTTP clients
   ↓
exit before grace period ends
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 43 — preStop Caution

### Objective

Practice **preStop Caution** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
SIGTERM / termination starts
   ↓
readiness becomes false
   ↓
Service stops new traffic
   ↓
finish in-flight requests/jobs
   ↓
close DB/broker/HTTP clients
   ↓
exit before grace period ends
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 44 — Termination Grace Sizing

### Objective

Practice **Termination Grace Sizing** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
SIGTERM / termination starts
   ↓
readiness becomes false
   ↓
Service stops new traffic
   ↓
finish in-flight requests/jobs
   ↓
close DB/broker/HTTP clients
   ↓
exit before grace period ends
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 45 — Connection Draining

### Objective

Practice **Connection Draining** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 46 — Resource Requests from Measurements

### Objective

Practice **Resource Requests from Measurements** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 47 — Memory Limit Headroom

### Objective

Practice **Memory Limit Headroom** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 48 — CPU Throttling Observability

### Objective

Practice **CPU Throttling Observability** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 49 — OOMKilled Root Cause

### Objective

Practice **OOMKilled Root Cause** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 50 — QoS Class Awareness

### Objective

Practice **QoS Class Awareness** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 51 — LimitRange Defaults

### Objective

Practice **LimitRange Defaults** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 52 — ResourceQuota Capacity

### Objective

Practice **ResourceQuota Capacity** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

```text
requests -> scheduling capacity
limits   -> runtime enforcement
CPU limit hit -> throttling
memory limit hit -> OOM termination
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 53 — Pending Pod Evidence

### Objective

Practice **Pending Pod Evidence** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```bash
kubectl get pods -n app
kubectl describe pod <pod> -n app
kubectl logs <pod> -c app -n app
kubectl logs <pod> -c app -n app --previous
kubectl get events -n app --sort-by=.lastTimestamp
kubectl get endpointslices -n app
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 54 — Topology Spread

### Objective

Practice **Topology Spread** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 55 — Anti-Affinity Trade-Off

### Objective

Practice **Anti-Affinity Trade-Off** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 56 — Node Affinity

### Objective

Practice **Node Affinity** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 57 — Taints and Tolerations

### Objective

Practice **Taints and Tolerations** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 58 — PriorityClass Governance

### Objective

Practice **PriorityClass Governance** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 59 — PodDisruptionBudget

### Objective

Practice **PodDisruptionBudget** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 60 — PDB vs Involuntary Failure

### Objective

Practice **PDB vs Involuntary Failure** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 61 — HPA Prerequisite Requests

### Objective

Practice **HPA Prerequisite Requests** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 62 — HPA Stabilization

### Objective

Practice **HPA Stabilization** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 63 — Queue-Lag Worker Scaling

### Objective

Practice **Queue-Lag Worker Scaling** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 64 — Autoscaling Downstream Ceiling

### Objective

Practice **Autoscaling Downstream Ceiling** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 65 — Scale-to-Zero Cold Start

### Objective

Practice **Scale-to-Zero Cold Start** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 66 — Cluster Autoscaler Interaction

### Objective

Practice **Cluster Autoscaler Interaction** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders-api
spec:
  minReplicas: 3
  maxReplicas: 20
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders-api
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 67 — PVC as Durable Boundary

### Objective

Practice **PVC as Durable Boundary** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 68 — StorageClass Policy

### Objective

Practice **StorageClass Policy** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 69 — Reclaim Policy

### Objective

Practice **Reclaim Policy** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Manifest
   ↓
Admission policy
   ├─ image digest pinned?
   ├─ runAsNonRoot?
   ├─ resource requests present?
   └─ approved registry?
   ↓
accept / reject
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 70 — Volume Binding Topology

### Objective

Practice **Volume Binding Topology** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders-api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: orders-api
```

```text
Replica A -> zone-a
Replica B -> zone-b
Replica C -> zone-c
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 71 — Access Mode Reality

### Objective

Practice **Access Mode Reality** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 72 — Volume Expansion

### Objective

Practice **Volume Expansion** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 73 — Volume Snapshot Consistency

### Objective

Practice **Volume Snapshot Consistency** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 74 — StatefulSet Identity

### Objective

Practice **StatefulSet Identity** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 75 — StatefulSet Rolling Risk

### Objective

Practice **StatefulSet Rolling Risk** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 76 — Init Container Failure

### Objective

Practice **Init Container Failure** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 77 — Migration Job Singleton

### Objective

Practice **Migration Job Singleton** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 78 — Migration Locking / Idempotency

### Objective

Practice **Migration Locking / Idempotency** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 79 — CronJob Concurrency

### Objective

Practice **CronJob Concurrency** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 80 — CronJob Missed Schedule

### Objective

Practice **CronJob Missed Schedule** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 81 — Job Idempotency

### Objective

Practice **Job Idempotency** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migration
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: registry.example/orders@sha256:DEMO
          args: ["migrate"]
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 82 — Sidecar Lifecycle Cost

### Objective

Practice **Sidecar Lifecycle Cost** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 83 — Service Mesh Sidecar Readiness

### Objective

Practice **Service Mesh Sidecar Readiness** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 84 — ServiceAccount Per Workload

### Objective

Practice **ServiceAccount Per Workload** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 85 — Disable Token Automount

### Objective

Practice **Disable Token Automount** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: orders-api
automountServiceAccountToken: false
```

```text
Pod -> ServiceAccount / workload identity
      ↓
least-privilege authorization
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 86 — RBAC Least Privilege

### Objective

Practice **RBAC Least Privilege** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
  seccompProfile:
    type: RuntimeDefault
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 87 — Workload Identity Federation

### Objective

Practice **Workload Identity Federation** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: orders-api
automountServiceAccountToken: false
```

```text
Pod -> ServiceAccount / workload identity
      ↓
least-privilege authorization
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 88 — Pod Security Context

### Objective

Practice **Pod Security Context** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 89 — Read-Only Root Filesystem

### Objective

Practice **Read-Only Root Filesystem** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 90 — Capability Add-Back

### Objective

Practice **Capability Add-Back** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
  seccompProfile:
    type: RuntimeDefault
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 91 — Admission Policy

### Objective

Practice **Admission Policy** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Manifest
   ↓
Admission policy
   ├─ image digest pinned?
   ├─ runAsNonRoot?
   ├─ resource requests present?
   └─ approved registry?
   ↓
accept / reject
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 92 — ImagePullSecret Scope

### Objective

Practice **ImagePullSecret Scope** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 93 — Secret at Rest Awareness

### Objective

Practice **Secret at Rest Awareness** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: orders-config
        key: LOG_LEVEL
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: orders-db-secret
        key: password
```

```text
ConfigMap -> non-secret config
Secret / external secret store -> sensitive config
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 94 — GitOps Source of Truth

### Objective

Practice **GitOps Source of Truth** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 95 — Drift Detection

### Objective

Practice **Drift Detection** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 96 — Environment Repository

### Objective

Practice **Environment Repository** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 97 — Helm Values Governance

### Objective

Practice **Helm Values Governance** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 98 — Helm Template Complexity

### Objective

Practice **Helm Template Complexity** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 99 — Kustomize Overlay Discipline

### Objective

Practice **Kustomize Overlay Discipline** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 100 — Promotion Pull Request

### Objective

Practice **Promotion Pull Request** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Application CI
   ↓ builds immutable digest
Environment Git repository
   ↓ pull request updates digest/config
GitOps controller
   ↓ reconciles
Cluster
   ↓
rollout + readiness + verification
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 101 — Policy Before Apply

### Objective

Practice **Policy Before Apply** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Manifest
   ↓
Admission policy
   ├─ image digest pinned?
   ├─ runAsNonRoot?
   ├─ resource requests present?
   └─ approved registry?
   ↓
accept / reject
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 102 — Smoke Test After Rollout

### Objective

Practice **Smoke Test After Rollout** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 103 — Deployment Marker

### Objective

Practice **Deployment Marker** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 104 — Kubernetes Metric Cardinality

### Objective

Practice **Kubernetes Metric Cardinality** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 105 — Pod-Level Tracing Context

### Objective

Practice **Pod-Level Tracing Context** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 106 — CrashLoopBackOff Diagnosis

### Objective

Practice **CrashLoopBackOff Diagnosis** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```bash
kubectl get pods -n app
kubectl describe pod <pod> -n app
kubectl logs <pod> -c app -n app
kubectl logs <pod> -c app -n app --previous
kubectl get events -n app --sort-by=.lastTimestamp
kubectl get endpointslices -n app
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 107 — ImagePullBackOff Diagnosis

### Objective

Practice **ImagePullBackOff Diagnosis** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```bash
kubectl get pods -n app
kubectl describe pod <pod> -n app
kubectl logs <pod> -c app -n app
kubectl logs <pod> -c app -n app --previous
kubectl get events -n app --sort-by=.lastTimestamp
kubectl get endpointslices -n app
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 108 — Service No Endpoints

### Objective

Practice **Service No Endpoints** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 109 — Ingress 502/503 Path

### Objective

Practice **Ingress 502/503 Path** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 110 — DNS Failure Path

### Objective

Practice **DNS Failure Path** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector:
    app: orders-api
  ports:
    - port: 80
      targetPort: 8080
```

```text
orders.default.svc.cluster.local
        ↓
Service
        ↓
ready Pod endpoints
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 111 — PVC Pending Path

### Objective

Practice **PVC Pending Path** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
```

```text
Pod lifecycle != data lifecycle
PVC / managed data service owns durable state
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 112 — FailedScheduling Path

### Objective

Practice **FailedScheduling Path** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 113 — Eviction Diagnosis

### Objective

Practice **Eviction Diagnosis** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 114 — Rollout Stuck

### Objective

Practice **Rollout Stuck** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 115 — Rollback Decision Rule

### Objective

Practice **Rollback Decision Rule** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 116 — Backup Responsibility

### Objective

Practice **Backup Responsibility** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 117 — Restore Drill

### Objective

Practice **Restore Drill** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 118 — Kubernetes RPO

### Objective

Practice **Kubernetes RPO** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 119 — Kubernetes RTO

### Objective

Practice **Kubernetes RTO** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 120 — Node Failure Game Day

### Objective

Practice **Node Failure Game Day** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 121 — Zone Failure Game Day

### Objective

Practice **Zone Failure Game Day** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```text
Git / CI
   ↓
Manifest + immutable image
   ↓
Kubernetes API
   ↓
Controller reconciliation
   ↓
Pod / Service / Policy / Storage
   ↓
Telemetry
   ↓
Rollback / recovery
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 122 — Production Kubernetes Readiness Review

### Objective

Practice **Production Kubernetes Readiness Review** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  periodSeconds: 10
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 2
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## Enhanced Practical Lab 123 — Kubernetes Deployment Final Operating Model

### Objective

Practice **Kubernetes Deployment Final Operating Model** in a local, disposable, or explicitly authorized environment.

### Procedure

1. Draw the relevant request/data/runtime path.
2. State the desired behavior and one failure scenario.
3. Implement or model the configuration.
4. Record the exact artifact/configuration version.
5. Execute the normal case.
6. Inject one safe failure, incompatibility, or resource constraint where appropriate.
7. Capture status, events, logs, metrics, traces, and durable state.
8. Write the recovery/rollback action.

### Starter Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
        - name: app
          image: registry.example/orders@sha256:DEMO
```

### Expected Result

You can explain the happy path, one failure path, the platform/controller behavior, the security boundary, and the evidence required to recover safely.

### Evidence Template

```text
Scenario:
Artifact / manifest / architecture version:
Expected state:
Actual state:
Identity:
Resource state:
Failure injected:
Observed events:
Logs / metrics / traces:
Recovery action:
Final validation:
```

### Review Questions

- What owns desired state?
- What can fail together?
- Can old/new versions coexist?
- What is the first shared bottleneck?
- Is identity least-privileged?
- What is durable state?
- Can the failure be diagnosed without random restart/manual mutation?
- What is the rollback or DR path?

---

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — First Deployment

Create a Deployment manifest for a simple HTTP API with 2 replicas.

### Lab 2 — Labels and Selectors

Add labels and verify Deployment/Service selectors match.

### Lab 3 — ClusterIP Service

Expose API internally using ClusterIP.

### Lab 4 — Service DNS

Resolve and call Service by DNS name from another Pod.

### Lab 5 — Rolling Update

Change image version and observe ReplicaSet transition.

### Lab 6 — Rollback

Rollback to previous revision after a simulated bad release.

### Lab 7 — maxSurge/maxUnavailable

Compare rollout behavior under two strategies.

### Lab 8 — Readiness Probe

Add `/ready` and observe traffic exclusion until ready.

### Lab 9 — Liveness Probe

Add `/live` and verify restart after controlled failure.

### Lab 10 — Startup Probe

Protect a deliberately slow-starting app.

### Lab 11 — Graceful Shutdown

Terminate a Pod and verify app drains requests.

### Lab 12 — preStop

Add a preStop delay/hook and compare shutdown behavior.

### Lab 13 — ConfigMap Environment

Inject LOG_LEVEL and FEATURE_FLAG.

### Lab 14 — ConfigMap Volume

Mount a YAML configuration file.

### Lab 15 — Secret Environment

Inject a lab secret and discuss exposure trade-offs.

### Lab 16 — Secret Volume

Mount a secret file with read-only permissions.

### Lab 17 — Config Rollout

Use config checksum/version change to trigger new Pods.

### Lab 18 — Resource Requests

Set CPU/memory requests and observe scheduling.

### Lab 19 — Resource Limits

Set CPU/memory limits and test controlled load.

### Lab 20 — OOMKilled Lab

Trigger safe memory overuse and inspect termination reason.

### Lab 21 — Pending Pod

Set impossible resource request and inspect scheduler events.

### Lab 22 — Node Selector

Schedule Pod to a labeled node in a lab cluster.

### Lab 23 — Topology Spread Design

Design replicas across zones/nodes.

### Lab 24 — NetworkPolicy Default Deny

Create default-deny namespace policy in a lab.

### Lab 25 — NetworkPolicy Allow

Allow API→DB traffic only.

### Lab 26 — ServiceAccount

Create dedicated ServiceAccount for application.

### Lab 27 — Disable Token Automount

Run a Pod without Kubernetes API token when not needed.

### Lab 28 — SecurityContext

Set runAsNonRoot, readOnlyRootFilesystem, drop capabilities.

### Lab 29 — Private Registry

Configure image pull from an authorized private registry.

### Lab 30 — Digest Pinning

Deploy image by digest.

### Lab 31 — PVC

Create PVC and mount it into a Pod.

### Lab 32 — emptyDir

Use shared ephemeral volume between app and helper container.

### Lab 33 — StatefulSet Awareness

Create simple StatefulSet and inspect stable Pod names.

### Lab 34 — Job

Run one-off migration Job.

### Lab 35 — CronJob

Schedule a cleanup task and set concurrency policy.

### Lab 36 — Init Container

Use init container to prepare a config artifact.

### Lab 37 — Sidecar

Run a helper sidecar sharing a volume.

### Lab 38 — HPA

Configure CPU-based horizontal scaling in a lab.

### Lab 39 — Queue Scaling Design

Design lag-based autoscaling for a worker.

### Lab 40 — Ingress

Route `/api` host/path to Service using available controller.

### Lab 41 — TLS Edge Design

Design Ingress/Gateway TLS termination.

### Lab 42 — Helm

Package simple Deployment+Service as a chart.

### Lab 43 — Kustomize

Create base plus dev/prod overlays.

### Lab 44 — GitOps Flow

Design Git PR→controller→cluster deployment.

### Lab 45 — Migration Strategy

Design expand-contract DB migration plus one migration Job.

### Lab 46 — PDB

Create/discuss disruption budget for a 3-replica API.

### Lab 47 — Observability

Define logs, metrics, traces, pod/version labels, and dashboards.

### Lab 48 — Troubleshooting Game Day

Diagnose CrashLoopBackOff, ImagePullBackOff, Pending, OOMKilled, and no Service endpoints.

### Lab 49 — Rollout Failure Game Day

Deploy bad image, observe stuck rollout, rollback.

### Lab 50 — Capstone Review

Review manifests for networking, config, security, resources, probes, autoscaling, storage, rollout, and observability.

## 6. Mini Project

# Mini Project — Production Kubernetes Order Platform

Deploy:

```text
Ingress / Gateway
Orders API Deployment
Worker Deployment
Cache Service
Managed Database connection
Object Storage integration
Message Queue integration
Migration Job
Telemetry
```

## Required Kubernetes Objects

```text
Namespace
Deployment
Service
ConfigMap
Secret
ServiceAccount
NetworkPolicy
HorizontalPodAutoscaler
PodDisruptionBudget
Job
CronJob
Ingress or Gateway-style route
PVC only where justified
```

## API Deployment

```text
replicas >= 3
readiness
liveness
startup probe where needed
CPU/memory requests
CPU/memory limits
runAsNonRoot
readOnlyRootFilesystem
drop capabilities
graceful shutdown
immutable image digest
```

## Worker Deployment

```text
queue-driven workload
idempotent consumer
bounded concurrency
lag-based autoscaling design
graceful message drain
```

## Networking

```text
Internet
  ↓
Ingress/Gateway
  ↓
Orders Service
  ↓
Orders Pods

Orders Pods
  ↓
private dependencies
```

Use default-deny NetworkPolicy plus explicit allowances.

## Configuration

```text
ConfigMap for non-secret config
Secret/external secret for credentials
config version/checksum rollout
```

## Storage

```text
managed DB preferred
object storage for files
PVC only for workloads that truly need filesystem persistence
```

## Delivery

```text
CI builds image
 ↓
scan / SBOM
 ↓
push by digest
 ↓
Git deployment update
 ↓
GitOps/Apply
 ↓
rolling rollout
 ↓
readiness
 ↓
smoke test
 ↓
metrics verification
```

## Required Rollout Designs

```text
Rolling
Canary
Blue/Green
Rollback
```

## Required Documentation

```text
K8S_ARCHITECTURE.md
MANIFESTS.md
NETWORKING.md
CONFIG_SECRETS.md
SECURITY_CONTEXT.md
STORAGE.md
AUTOSCALING.md
ROLLOUTS.md
MIGRATIONS.md
OBSERVABILITY.md
TROUBLESHOOTING.md
HA_DR.md
```

## 7. Recommended Resources

This Markdown is designed to be self-contained.

For implementation specifics, consult current official Kubernetes documentation for:

```text
Deployments
Services
ConfigMaps
Secrets
Probes
Resources
HPA
Storage
Jobs/CronJobs
NetworkPolicy
SecurityContext
ServiceAccounts
Ingress / Gateway APIs
kubectl
```

Use the official documentation of your chosen Ingress controller, CSI driver, autoscaling add-on, Helm, Kustomize, and GitOps controller when implementing vendor-specific behavior.

## 8. Certification Relevance

Relevant to:

```text
Cloud Application Developer
Kubernetes Application Developer
DevOps Engineer
Platform Engineer
SRE
Cloud Engineer
Container Engineer
Application Security Engineer
```

It reinforces practical deployment knowledge complementary to Kubernetes administration and prepares directly for Course 80 — Cloud Application Architecture.

## 9. Common Mistakes & Best Practices

- **Mistake:** Editing Pods directly.  
  **Best practice:** Change the owning controller/manifests.
- **Mistake:** Using mutable image tags.  
  **Best practice:** Deploy immutable digests.
- **Mistake:** No requests/limits.  
  **Best practice:** Set measured values.
- **Mistake:** Liveness depends on DB.  
  **Best practice:** Keep liveness local; use readiness for serving readiness.
- **Mistake:** Service selector does not match Pods.  
  **Best practice:** Standardize labels and verify endpoints.
- **Mistake:** Using Pod IPs directly.  
  **Best practice:** Use Services/DNS.
- **Mistake:** Putting secrets in ConfigMaps.  
  **Best practice:** Use Secrets or external secret managers.
- **Mistake:** Treating base64 as encryption.  
  **Best practice:** Use RBAC, encryption at rest, and external secret management.
- **Mistake:** Running as root by default.  
  **Best practice:** Use securityContext and non-root image.
- **Mistake:** Mounting service-account token unnecessarily.  
  **Best practice:** Disable automount when app does not need API.
- **Mistake:** No NetworkPolicy.  
  **Best practice:** Use default deny plus explicit allow where supported.
- **Mistake:** Autoscaling without DB capacity planning.  
  **Best practice:** Scale dependency chain.
- **Mistake:** Running DB migration in every replica.  
  **Best practice:** Use one controlled Job.
- **Mistake:** Destroying DB schema before rollback window closes.  
  **Best practice:** Use expand-contract.
- **Mistake:** Using PVC for data better suited to managed/object storage.  
  **Best practice:** Match storage to workload.
- **Mistake:** No graceful shutdown.  
  **Best practice:** Drain before termination.
- **Mistake:** No PDB/topology spread for critical replicas.  
  **Best practice:** Design maintenance and zone failure tolerance.
- **Mistake:** Applying manifests manually outside Git.  
  **Best practice:** Use a declared source of truth.
- **Mistake:** Assuming apply success means application healthy.  
  **Best practice:** Check rollout, readiness, smoke tests, and telemetry.
- **Mistake:** Troubleshooting by deleting Pods repeatedly.  
  **Best practice:** Inspect status, events, logs, and controller state first.

## 10. Self-Assessment Questions (with short answers)

### Q1. Kubernetes desired state?

**Answer:** Declared resource spec that controllers reconcile toward.

### Q2. Pod?

**Answer:** Smallest deployable execution unit.

### Q3. Deployment?

**Answer:** Controller for replicated stateless Pods and rolling updates.

### Q4. ReplicaSet?

**Answer:** Maintains a desired number of matching Pods.

### Q5. StatefulSet?

**Answer:** Controller for stateful Pods with stable identity/storage behavior.

### Q6. DaemonSet?

**Answer:** Runs Pods on each/selected node.

### Q7. Job?

**Answer:** Runs work to completion.

### Q8. CronJob?

**Answer:** Schedules Jobs.

### Q9. Label?

**Answer:** Key-value metadata used for selection/grouping.

### Q10. Selector?

**Answer:** Rule matching resources by labels.

### Q11. ConfigMap?

**Answer:** Non-secret configuration object.

### Q12. Secret?

**Answer:** Object for sensitive configuration/credentials.

### Q13. Service?

**Answer:** Stable network identity/load-balancing abstraction for Pods.

### Q14. ClusterIP?

**Answer:** Internal-only Service type.

### Q15. LoadBalancer?

**Answer:** Service type integrating external load balancer where supported.

### Q16. Ingress?

**Answer:** HTTP routing resource implemented by an Ingress controller.

### Q17. Gateway API awareness?

**Answer:** More expressive gateway/route model supported by implementations.

### Q18. Readiness probe?

**Answer:** Determines whether Pod receives traffic.

### Q19. Liveness probe?

**Answer:** Determines whether container should be restarted.

### Q20. Startup probe?

**Answer:** Protects slow startup before liveness begins.

### Q21. Resource request?

**Answer:** Amount reserved/used for scheduling.

### Q22. Resource limit?

**Answer:** Maximum resource usage policy.

### Q23. OOMKilled?

**Answer:** Container terminated due to memory exhaustion/limit.

### Q24. HPA?

**Answer:** Controller that adjusts replica count from metrics.

### Q25. Queue-lag scaling?

**Answer:** Scale workers based on backlog/lag.

### Q26. PVC?

**Answer:** Application request for persistent storage.

### Q27. StorageClass?

**Answer:** Defines dynamic storage provisioning class/policy.

### Q28. emptyDir?

**Answer:** Ephemeral Pod-scoped shared volume.

### Q29. ServiceAccount?

**Answer:** Workload identity inside Kubernetes.

### Q30. RBAC?

**Answer:** Authorization model for Kubernetes API actions.

### Q31. NetworkPolicy?

**Answer:** Rules controlling Pod network connectivity.

### Q32. runAsNonRoot?

**Answer:** Security setting requiring non-root user.

### Q33. readOnlyRootFilesystem?

**Answer:** Prevents writes to container root filesystem.

### Q34. ImagePullSecret?

**Answer:** Credential for private image registry pulls.

### Q35. Rolling update?

**Answer:** Gradually replace old Pods with new revision.

### Q36. maxSurge?

**Answer:** Extra Pods permitted during rollout.

### Q37. maxUnavailable?

**Answer:** Desired Pods allowed unavailable during rollout.

### Q38. PDB?

**Answer:** Controls voluntary disruption availability for Pods.

### Q39. Topology spread?

**Answer:** Distribute replicas across failure domains.

### Q40. Init container?

**Answer:** Runs before app containers.

### Q41. Sidecar?

**Answer:** Helper container sharing Pod lifecycle/network/volumes.

### Q42. CrashLoopBackOff?

**Answer:** Repeated container crashes with restart backoff.

### Q43. ImagePullBackOff?

**Answer:** Repeated failure pulling image.

### Q44. Pending Pod?

**Answer:** Pod not yet scheduled/started, often due to constraints/resources.

### Q45. Service no endpoints?

**Answer:** Usually selector mismatch or all matching Pods unready.

### Q46. GitOps?

**Answer:** Git is desired-state source and controller reconciles cluster.

### Q47. Helm?

**Answer:** Package/template system for Kubernetes resources.

### Q48. Kustomize?

**Answer:** Base-plus-overlay customization approach.

### Q49. Why migrate DB with Job?

**Answer:** Avoid multiple replica races and control migration lifecycle.

### Q50. Final principle?

**Answer:** Deploy immutable images through declarative manifests with health, resources, security, networking, scaling, and safe rollout behavior.

# Expanded Self-Assessment Bank — Kubernetes Application Deployment


### Q1. What is the central engineering lesson from **Desired-State Ownership**?

**Answer:** Treat Git/manifests as the source of desired application state and avoid using generated Pods/ReplicaSets as configuration.

### Q2. What is the central engineering lesson from **Controller Reconciliation**?

**Answer:** Understand that controllers repeatedly compare desired and actual state; troubleshooting begins by identifying the owning controller.

### Q3. What is the central engineering lesson from **Server-Side Apply Awareness**?

**Answer:** Field ownership matters when multiple tools manage one object; avoid uncoordinated writers that fight over the same fields.

### Q4. What is the central engineering lesson from **Manifest Schema Validation**?

**Answer:** Validate apiVersion, kind, required fields, selectors, resources, probes, and policy before deployment reaches the cluster.

### Q5. What is the central engineering lesson from **Immutable Image Reference**?

**Answer:** Deploy by immutable digest for deterministic promotion, rollback, and incident traceability.

### Q6. What is the central engineering lesson from **Label Taxonomy**?

**Answer:** Standardize application, component, version, environment, and owner labels so Services, policies, telemetry, and tooling agree.

### Q7. What is the central engineering lesson from **Selector Immutability Awareness**?

**Answer:** Treat controller selectors as stable identity because changing them can be restricted or can orphan workloads.

### Q8. What is the central engineering lesson from **Service Selector Safety**?

**Answer:** Verify Service selectors match only the intended ready Pods so traffic cannot reach the wrong component/version.

### Q9. What is the central engineering lesson from **Namespace Ownership**?

**Answer:** Use namespaces for organization, quota, policy, and ownership while remembering they are not a complete hard security boundary by themselves.

### Q10. What is the central engineering lesson from **Namespace Production Isolation**?

**Answer:** Use stronger isolation for production when risk requires it, potentially including separate clusters/accounts/projects.

### Q11. What is the central engineering lesson from **Deployment Failure-State Capacity**?

**Answer:** Choose replicas and rollout settings so the service remains above minimum capacity during node/zone loss and deployment.

### Q12. What is the central engineering lesson from **maxSurge Capacity Budget**?

**Answer:** Ensure the cluster has enough headroom for temporary surge Pods during rollout.

### Q13. What is the central engineering lesson from **maxUnavailable SLO Mapping**?

**Answer:** Choose allowed unavailability from the service SLO rather than defaulting blindly.

### Q14. What is the central engineering lesson from **Progress Deadline**?

**Answer:** Use rollout progress limits/automation so a new revision that never becomes ready fails visibly instead of hanging indefinitely.

### Q15. What is the central engineering lesson from **Revision Retention**?

**Answer:** Keep enough previous ReplicaSets/releases for recovery without retaining unlimited history.

### Q16. What is the central engineering lesson from **Rollback Compatibility**?

**Answer:** Ensure old application versions can still run against current schema/config when rollback is part of the recovery plan.

### Q17. What is the central engineering lesson from **Canary Workload Separation**?

**Answer:** Represent stable and canary versions with labels/services/routes that make traffic percentage and telemetry distinguishable.

### Q18. What is the central engineering lesson from **Canary Baseline Comparison**?

**Answer:** Compare candidate error, latency, saturation, and business outcomes against stable version before increasing traffic.

### Q19. What is the central engineering lesson from **Unknown Canary Telemetry**?

**Answer:** Treat missing or stale analysis data as UNKNOWN and halt promotion.

### Q20. What is the central engineering lesson from **Blue-Green Switch Safety**?

**Answer:** Validate green environment and shared data compatibility before moving the Service/Gateway selector or route.

### Q21. What is the central engineering lesson from **Shadow Traffic Side-Effect Control**?

**Answer:** Ensure mirrored traffic cannot execute real writes or duplicate irreversible actions.

### Q22. What is the central engineering lesson from **ClusterIP Default**?

**Answer:** Use ClusterIP for internal services unless an external exposure requirement exists.

### Q23. What is the central engineering lesson from **Headless Service**?

**Answer:** Use headless discovery only when the application needs direct endpoint identity and can handle endpoint churn.

### Q24. What is the central engineering lesson from **EndpointSlice Diagnosis**?

**Answer:** Inspect EndpointSlices when Service traffic fails even though Pods appear healthy.

### Q25. What is the central engineering lesson from **Readiness and Service Membership**?

**Answer:** Remember that an unready Pod can exist and run while being removed from normal Service traffic.

### Q26. What is the central engineering lesson from **Ingress Controller Dependency**?

**Answer:** An Ingress object requires a compatible controller; include controller health and configuration in the edge dependency model.

### Q27. What is the central engineering lesson from **Gateway API Role Separation**?

**Answer:** Use Gateway/Route separation to distinguish infrastructure ownership from application routing ownership when supported.

### Q28. What is the central engineering lesson from **TLS Certificate Lifecycle**?

**Answer:** Automate certificate issuance, renewal, rotation, and expiry monitoring for ingress/gateway endpoints.

### Q29. What is the central engineering lesson from **ExternalDNS Permission Scope**?

**Answer:** Give DNS automation narrowly scoped permissions to only the zones/records it owns.

### Q30. What is the central engineering lesson from **Default-Deny NetworkPolicy**?

**Answer:** Start from deny-by-default where supported, then add explicit application flows.

### Q31. What is the central engineering lesson from **DNS Egress with NetworkPolicy**?

**Answer:** Allow required DNS resolution when enforcing egress policy; otherwise workloads can fail before reaching services.

### Q32. What is the central engineering lesson from **NetworkPolicy Dependency Matrix**?

**Answer:** Document every legitimate service-to-service and egress path before enforcing restrictive policy.

### Q33. What is the central engineering lesson from **ConfigMap Update Semantics**?

**Answer:** Understand whether the application reads environment variables once or mounted files dynamically and choose rollout/reload behavior accordingly.

### Q34. What is the central engineering lesson from **Secret Delivery Choice**?

**Answer:** Choose environment, mounted volume, CSI/external secret projection, or workload identity based on exposure and rotation needs.

### Q35. What is the central engineering lesson from **Secret Rotation Test**?

**Answer:** Verify that applications reload files or reconnect after secret changes instead of assuming rotation is automatic.

### Q36. What is the central engineering lesson from **Config Checksum Rollout**?

**Answer:** Use a deterministic config hash annotation or version change to trigger Pod replacement when startup-only configuration changes.

### Q37. What is the central engineering lesson from **Liveness Minimalism**?

**Answer:** Keep liveness local to process progress so external dependency outages do not create restart storms.

### Q38. What is the central engineering lesson from **Readiness Dependency Classification**?

**Answer:** Only mark not-ready for dependencies required to serve that Pod's intended traffic.

### Q39. What is the central engineering lesson from **Startup Probe Budget**?

**Answer:** Use startup probes for legitimately slow initialization instead of inflating liveness delays.

### Q40. What is the central engineering lesson from **Probe Cost Budget**?

**Answer:** Keep probes cheap and independent of expensive database queries or remote SaaS calls.

### Q41. What is the central engineering lesson from **Probe Failure Threshold**?

**Answer:** Tune probe period/timeout/failure threshold to distinguish real failure from brief jitter.

### Q42. What is the central engineering lesson from **Graceful Shutdown Order**?

**Answer:** Make readiness false, stop new work, drain, close clients, flush telemetry, then exit before grace period.

### Q43. What is the central engineering lesson from **preStop Caution**?

**Answer:** Use preStop only as a supplement; the application must still handle SIGTERM correctly.

### Q44. What is the central engineering lesson from **Termination Grace Sizing**?

**Answer:** Measure worst-case drain time and set terminationGracePeriodSeconds with explicit buffer.

### Q45. What is the central engineering lesson from **Connection Draining**?

**Answer:** Coordinate load balancer/Service removal with process shutdown so old Pods finish in-flight connections.

### Q46. What is the central engineering lesson from **Resource Requests from Measurements**?

**Answer:** Set CPU/memory requests from observed normal demand because requests control scheduling and HPA utilization calculations.

### Q47. What is the central engineering lesson from **Memory Limit Headroom**?

**Answer:** Set memory limits with realistic peak headroom and investigate leaks rather than continuously raising limits.

### Q48. What is the central engineering lesson from **CPU Throttling Observability**?

**Answer:** Track throttled CPU time because a CPU-capped Pod can have high tail latency without obvious crash.

### Q49. What is the central engineering lesson from **OOMKilled Root Cause**?

**Answer:** Distinguish too-low limits, traffic spikes, memory leaks, cache growth, allocator behavior, and node pressure.

### Q50. What is the central engineering lesson from **QoS Class Awareness**?

**Answer:** Understand how requests/limits influence QoS and eviction behavior under node pressure.

### Q51. What is the central engineering lesson from **LimitRange Defaults**?

**Answer:** Use namespace defaults carefully so developers understand the resources automatically applied to Pods.

### Q52. What is the central engineering lesson from **ResourceQuota Capacity**?

**Answer:** Use quotas to bound namespace resource/cost impact without making legitimate deployments permanently unschedulable.

### Q53. What is the central engineering lesson from **Pending Pod Evidence**?

**Answer:** Use scheduler events to distinguish insufficient resources, node constraints, taints, or unbound storage.

### Q54. What is the central engineering lesson from **Topology Spread**?

**Answer:** Spread replicas across nodes/zones without making placement so strict that Pods become Pending.

### Q55. What is the central engineering lesson from **Anti-Affinity Trade-Off**?

**Answer:** Use required anti-affinity only where strict separation is worth the scheduling risk; prefer flexible spread for many workloads.

### Q56. What is the central engineering lesson from **Node Affinity**?

**Answer:** Use node affinity when hardware/location requirements are genuine, not as a substitute for good platform labels.

### Q57. What is the central engineering lesson from **Taints and Tolerations**?

**Answer:** Use taints to protect specialized nodes and tolerations only for workloads intentionally allowed there.

### Q58. What is the central engineering lesson from **PriorityClass Governance**?

**Answer:** Reserve high priorities for genuinely critical workloads to avoid starvation/preemption chaos.

### Q59. What is the central engineering lesson from **PodDisruptionBudget**?

**Answer:** Protect availability from voluntary disruptions while allowing enough flexibility for node maintenance.

### Q60. What is the central engineering lesson from **PDB vs Involuntary Failure**?

**Answer:** Remember PDBs constrain voluntary eviction but cannot prevent node crashes or all failure modes.

### Q61. What is the central engineering lesson from **HPA Prerequisite Requests**?

**Answer:** CPU/memory HPA depends on meaningful resource requests; bad requests produce misleading scaling.

### Q62. What is the central engineering lesson from **HPA Stabilization**?

**Answer:** Use scale-up/down policies and stabilization to avoid oscillation and sudden dependency overload.

### Q63. What is the central engineering lesson from **Queue-Lag Worker Scaling**?

**Answer:** Scale asynchronous workers from queue age/lag when that better represents work demand than CPU.

### Q64. What is the central engineering lesson from **Autoscaling Downstream Ceiling**?

**Answer:** Set maxReplicas and concurrency so scale-out cannot exceed database, broker, or partner capacity.

### Q65. What is the central engineering lesson from **Scale-to-Zero Cold Start**?

**Answer:** Use event-driven scale-to-zero only when startup and backlog delay fit the business SLO.

### Q66. What is the central engineering lesson from **Cluster Autoscaler Interaction**?

**Answer:** Application Pods can remain Pending while node capacity grows; startup and PDB/topology rules affect the eventual scheduling outcome.

### Q67. What is the central engineering lesson from **PVC as Durable Boundary**?

**Answer:** Treat PVC-backed data as independent from Pod lifetime and include backup/recovery explicitly.

### Q68. What is the central engineering lesson from **StorageClass Policy**?

**Answer:** Understand performance, zone binding, reclaim, encryption, expansion, and snapshot behavior of the selected StorageClass.

### Q69. What is the central engineering lesson from **Reclaim Policy**?

**Answer:** Use Retain/Delete according to data criticality and decommission workflow; deletion can be irreversible.

### Q70. What is the central engineering lesson from **Volume Binding Topology**?

**Answer:** Storage provisioning may be zone-aware; schedule and storage topology must be compatible.

### Q71. What is the central engineering lesson from **Access Mode Reality**?

**Answer:** Do not assume ReadWriteMany is available or performant on every backend.

### Q72. What is the central engineering lesson from **Volume Expansion**?

**Answer:** Plan filesystem/application actions and monitoring after PVC size increases.

### Q73. What is the central engineering lesson from **Volume Snapshot Consistency**?

**Answer:** A storage snapshot is not automatically application-consistent; quiesce/DB-native backup may be required.

### Q74. What is the central engineering lesson from **StatefulSet Identity**?

**Answer:** Stable Pod names and per-replica PVCs do not solve database replication or consensus by themselves.

### Q75. What is the central engineering lesson from **StatefulSet Rolling Risk**?

**Answer:** Stateful systems may require ordered upgrade/health semantics more specific than a generic Deployment.

### Q76. What is the central engineering lesson from **Init Container Failure**?

**Answer:** An init container that loops/fails prevents the application from starting; keep setup bounded and observable.

### Q77. What is the central engineering lesson from **Migration Job Singleton**?

**Answer:** Run schema migration as one controlled Job rather than from every application Pod.

### Q78. What is the central engineering lesson from **Migration Locking / Idempotency**?

**Answer:** Make migration jobs restartable, concurrency-safe, and able to report exactly which migration step failed.

### Q79. What is the central engineering lesson from **CronJob Concurrency**?

**Answer:** Set Allow/Forbid/Replace according to whether overlapping scheduled executions are safe.

### Q80. What is the central engineering lesson from **CronJob Missed Schedule**?

**Answer:** Decide how delayed/missed jobs behave after controller downtime or long suspension.

### Q81. What is the central engineering lesson from **Job Idempotency**?

**Answer:** A retried Job must not duplicate irreversible business effects.

### Q82. What is the central engineering lesson from **Sidecar Lifecycle Cost**?

**Answer:** Account for sidecar CPU/memory/startup/shutdown because every Pod replica multiplies the helper cost.

### Q83. What is the central engineering lesson from **Service Mesh Sidecar Readiness**?

**Answer:** Proxy readiness and application readiness can interact; verify traffic is not sent before both are usable.

### Q84. What is the central engineering lesson from **ServiceAccount Per Workload**?

**Answer:** Use dedicated identities for workloads that need Kubernetes/cloud APIs; avoid shared default identity.

### Q85. What is the central engineering lesson from **Disable Token Automount**?

**Answer:** Disable service-account token mounting when the workload does not call Kubernetes API.

### Q86. What is the central engineering lesson from **RBAC Least Privilege**?

**Answer:** Grant only specific verbs/resources/namespaces required by the workload or automation.

### Q87. What is the central engineering lesson from **Workload Identity Federation**?

**Answer:** Prefer platform/cloud workload identity mappings to long-lived cloud keys stored in Kubernetes Secrets.

### Q88. What is the central engineering lesson from **Pod Security Context**?

**Answer:** Enforce non-root, no privilege escalation, dropped capabilities, and default seccomp for ordinary application Pods.

### Q89. What is the central engineering lesson from **Read-Only Root Filesystem**?

**Answer:** Pair readOnlyRootFilesystem with explicit tmpfs/emptyDir mounts for legitimate temporary writes.

### Q90. What is the central engineering lesson from **Capability Add-Back**?

**Answer:** After dropping ALL capabilities, add only the exact capability the process genuinely requires.

### Q91. What is the central engineering lesson from **Admission Policy**?

**Answer:** Use admission guardrails for approved registries, digest pinning, resources, labels, and security context.

### Q92. What is the central engineering lesson from **ImagePullSecret Scope**?

**Answer:** Keep registry pull credentials namespace/repository scoped and rotate them if workload identity/native auth is unavailable.

### Q93. What is the central engineering lesson from **Secret at Rest Awareness**?

**Answer:** Kubernetes Secret objects require API/RBAC protection and platform encryption-at-rest; base64 is not encryption.

### Q94. What is the central engineering lesson from **GitOps Source of Truth**?

**Answer:** Let GitOps controllers reconcile desired state and treat manual kubectl changes as temporary debugging only.

### Q95. What is the central engineering lesson from **Drift Detection**?

**Answer:** Use GitOps status/diff to detect manual or automated divergence from declared configuration.

### Q96. What is the central engineering lesson from **Environment Repository**?

**Answer:** Separate artifact build from environment promotion so one immutable image can move through dev/stage/prod.

### Q97. What is the central engineering lesson from **Helm Values Governance**?

**Answer:** Keep values files small, typed/documented where possible, and avoid embedding secret values.

### Q98. What is the central engineering lesson from **Helm Template Complexity**?

**Answer:** Avoid turning Helm templates into a programming language full of hidden conditional behavior.

### Q99. What is the central engineering lesson from **Kustomize Overlay Discipline**?

**Answer:** Keep a common base and small overlays instead of duplicating entire manifest trees per environment.

### Q100. What is the central engineering lesson from **Promotion Pull Request**?

**Answer:** Promote by changing the immutable digest and reviewed configuration in the environment repository.

### Q101. What is the central engineering lesson from **Policy Before Apply**?

**Answer:** Run manifest schema, security, compatibility, and policy checks before the GitOps controller sees the change.

### Q102. What is the central engineering lesson from **Smoke Test After Rollout**?

**Answer:** Verify readiness plus at least one critical business path before declaring deployment complete.

### Q103. What is the central engineering lesson from **Deployment Marker**?

**Answer:** Record image digest/revision and deploy time in logs/metrics/tracing dashboards.

### Q104. What is the central engineering lesson from **Kubernetes Metric Cardinality**?

**Answer:** Use bounded labels like namespace/workload/route/version; avoid Pod UID/request ID as metric labels.

### Q105. What is the central engineering lesson from **Pod-Level Tracing Context**?

**Answer:** Preserve standard distributed trace context across ingress, services, workers, and messaging.

### Q106. What is the central engineering lesson from **CrashLoopBackOff Diagnosis**?

**Answer:** Inspect current/previous logs, exit code, config/secret changes, probes, and dependency initialization.

### Q107. What is the central engineering lesson from **ImagePullBackOff Diagnosis**?

**Answer:** Check image reference/digest, registry credentials, node egress/DNS, platform architecture, and registry health.

### Q108. What is the central engineering lesson from **Service No Endpoints**?

**Answer:** Compare Service selector, Pod labels, readiness, namespace, and EndpointSlices.

### Q109. What is the central engineering lesson from **Ingress 502/503 Path**?

**Answer:** Trace controller -> Service -> EndpointSlice -> Pod readiness -> NetworkPolicy -> targetPort/listener.

### Q110. What is the central engineering lesson from **DNS Failure Path**?

**Answer:** Check Service existence, cluster DNS, Pod resolver config, NetworkPolicy egress, and namespace/name correctness.

### Q111. What is the central engineering lesson from **PVC Pending Path**?

**Answer:** Check StorageClass, provisioner, quota, access mode, zone constraints, and events.

### Q112. What is the central engineering lesson from **FailedScheduling Path**?

**Answer:** Read scheduler events before changing application code; identify resources, affinity, taints, topology, or volumes.

### Q113. What is the central engineering lesson from **Eviction Diagnosis**?

**Answer:** Differentiate application crash from node MemoryPressure/DiskPressure/PIDPressure eviction.

### Q114. What is the central engineering lesson from **Rollout Stuck**?

**Answer:** Inspect the new ReplicaSet and Pods rather than repeatedly reapplying the same manifest.

### Q115. What is the central engineering lesson from **Rollback Decision Rule**?

**Answer:** Rollback quickly when the new revision is clearly unhealthy and the fix is not safer/faster than returning to known-good.

### Q116. What is the central engineering lesson from **Backup Responsibility**?

**Answer:** Kubernetes objects can be recreated from Git, but application data, external secrets, and stateful dependencies need separate recovery.

### Q117. What is the central engineering lesson from **Restore Drill**?

**Answer:** Restore manifests/config plus durable data and validate a real business workflow in an isolated environment.

### Q118. What is the central engineering lesson from **Kubernetes RPO**?

**Answer:** Define recoverable state across PVCs, databases, object storage, and messaging rather than treating cluster state as business backup.

### Q119. What is the central engineering lesson from **Kubernetes RTO**?

**Answer:** Measure cluster/runtime availability, storage restore, application rollout, DNS/edge, and validation time end-to-end.

### Q120. What is the central engineering lesson from **Node Failure Game Day**?

**Answer:** Terminate one lab node and verify replica rescheduling, PDB/topology behavior, capacity, and service continuity.

### Q121. What is the central engineering lesson from **Zone Failure Game Day**?

**Answer:** Model loss of an entire zone and verify remaining capacity plus data-layer survivability.

### Q122. What is the central engineering lesson from **Production Kubernetes Readiness Review**?

**Answer:** Review source of truth, immutable image, probes, resources, security, policy, autoscaling, storage, rollout, observability, backup, and DR.

### Q123. What is the central engineering lesson from **Kubernetes Deployment Final Operating Model**?

**Answer:** Treat image digest plus declarative application objects, policy, identity, state, and telemetry as one versioned production release.

## Completion Checklist

- [ ] I understand core application-oriented Kubernetes objects.
- [ ] I can deploy stateless applications with Deployments.
- [ ] I can expose applications through Services and Ingress/Gateway concepts.
- [ ] I can use ConfigMaps and Secrets.
- [ ] I can design probes and graceful shutdown.
- [ ] I can set requests/limits and understand OOM/throttling.
- [ ] I can design HPA and queue-based scaling.
- [ ] I understand PVC/StorageClass/emptyDir.
- [ ] I can use Jobs, CronJobs, init containers, and sidecars.
- [ ] I understand ServiceAccounts, securityContext, RBAC awareness, and NetworkPolicy.
- [ ] I can design rolling/canary/blue-green deployments.
- [ ] I understand GitOps, Helm, and Kustomize concepts.
- [ ] I can design migration and rollback compatibility.
- [ ] I can troubleshoot common Pod/deployment failures.
- [ ] I completed all labs.
- [ ] I completed the Kubernetes application capstone.
