# 59. Kubernetes Fundamentals

> Phase 15 — Containers

This course builds from **Application Containers** and **Docker Fundamentals** into the Kubernetes object model, declarative control loops, workload primitives, service networking, storage, configuration, security, observability, and day-to-day `kubectl` use.

The goal is not to memorize YAML. It is to understand why Kubernetes behaves the way it does.

---

# Current Kubernetes Baseline

Current upstream baseline used in this material:

```text
Latest stable Kubernetes minor line: v1.36
Latest stable patch verified for this course: v1.36.2
Kubernetes v1.37 planned release: August 26, 2026
```

This course therefore uses Kubernetes **v1.36-era APIs and behavior** as the practical baseline while avoiding unnecessary dependence on patch-specific details.

Kubernetes describes itself as an open-source platform for managing containerized workloads and services using declarative configuration and automation.

The core mental model is:

```text
You declare desired state
        ↓
Kubernetes API stores it
        ↓
Controllers observe actual state
        ↓
Controllers reconcile differences
        ↓
Cluster continuously moves toward desired state
```

Example:

```text
Desired:
3 web replicas

Actual:
2 web replicas

Controller:
create 1 more Pod
```

This **reconciliation loop** is the foundation of Kubernetes.

---

# Kubernetes Architecture at a Glance

```text
                    kubectl / API Client
                           |
                           v
                    kube-apiserver
                           |
              +------------+------------+
              |                         |
              v                         v
            etcd                  Control Loops
                                 /             \
                      controller-manager      scheduler
                              |                  |
                              +--------+---------+
                                       |
                                       v
                                Worker Nodes
                          +------------+------------+
                          |                         |
                       kubelet                   kube-proxy
                          |                         |
                          v                         v
                    Container Runtime        Service Networking
                          |
                          v
                         Pods
```

A cluster is:

```text
Control Plane
+
Worker Nodes
```

A workload is usually expressed through higher-level objects:

```text
Deployment
   ↓
ReplicaSet
   ↓
Pods
   ↓
Containers
```

Networking commonly looks like:

```text
Client
  ↓
Ingress / Gateway
  ↓
Service
  ↓
Pod IPs
```

Configuration:

```text
ConfigMap / Secret
        ↓
       Pod
```

Persistent data:

```text
PersistentVolumeClaim
        ↓
PersistentVolume / CSI Storage
        ↓
       Pod
```

---

## 1. Topic Title

**Kubernetes Fundamentals**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain why Kubernetes is needed beyond Docker and single-host containers.
- Explain Kubernetes declarative desired-state management.
- Explain reconciliation loops.
- Explain control-plane and node components.
- Explain the Kubernetes API object model.
- Read and write Kubernetes YAML.
- Understand `apiVersion`, `kind`, `metadata`, `spec`, and `status`.
- Use `kubectl` safely and efficiently.
- Manage contexts and namespaces.
- Create and inspect Pods.
- Explain Pod lifecycle and phases.
- Explain multi-container Pod patterns.
- Use init containers and sidecars appropriately.
- Use ephemeral containers for debugging.
- Apply labels, selectors, annotations, and owner references.
- Create ReplicaSets and Deployments.
- Understand rolling updates and rollbacks.
- Understand Deployment strategy settings.
- Create Services and understand ClusterIP, NodePort, LoadBalancer, and ExternalName.
- Explain EndpointSlices.
- Understand Kubernetes DNS.
- Explain Ingress and the modern Gateway API conceptually.
- Use ConfigMaps and Secrets.
- Mount configuration as files and environment variables.
- Explain Secret limitations and safe handling.
- Configure liveness, readiness, and startup probes.
- Configure lifecycle hooks and graceful termination.
- Set resource requests and limits.
- Understand QoS classes.
- Understand CPU throttling and OOM behavior in Kubernetes.
- Understand basic scheduling.
- Use node selectors, affinity, taints, and tolerations at a fundamentals level.
- Explain Jobs and CronJobs.
- Explain DaemonSets and StatefulSets.
- Understand PersistentVolumes, PersistentVolumeClaims, StorageClasses, and CSI.
- Understand access modes and reclaim policies.
- Understand ServiceAccounts and RBAC fundamentals.
- Explain security contexts.
- Explain NetworkPolicy fundamentals.
- Explain Pod Security Standards conceptually.
- Use Horizontal Pod Autoscaler concepts.
- Explain metrics and observability basics.
- Troubleshoot common Pod, Service, DNS, configuration, and scheduling problems.
- Use `kubectl logs`, `exec`, `describe`, `events`, `top`, `port-forward`, and `debug`.
- Explain Helm and Kustomize at a fundamentals level.
- Build a complete multi-tier Kubernetes application.

---

## 3. Prerequisites

Required:

- 57. Application Containers
- 58. Docker Fundamentals
- Linux administration
- Networking fundamentals
- YAML basics
- Git
- Basic HTTP/API knowledge

Recommended lab environments:

```text
kind
minikube
k3d
Docker Desktop Kubernetes
or an authorized managed Kubernetes sandbox
```

Recommended tools:

```text
kubectl
Docker
kind or minikube
curl
jq
yq
Git
```

Verify client:

```bash
kubectl version --client
```

Verify cluster:

```bash
kubectl cluster-info
kubectl get nodes
```

---

## 4. Core Concepts Explanation

# Part 1 — Why Kubernetes Exists

Docker solves:

```text
build image
run container
network container
mount storage
```

A production platform must also solve:

```text
Which host should run it?
What if that host fails?
How many replicas?
How do clients find replicas?
How do we update safely?
How do we attach storage?
How do we manage secrets?
How do we enforce policy?
```

Kubernetes solves these **cluster-level orchestration** problems.

# Part 2 — Declarative Management

Imperative thinking:

```text
Start container A.
Start container B.
Restart A if it fails.
```

Declarative thinking:

```yaml
replicas: 3
```

Kubernetes continuously works to maintain three replicas.

You describe **what should be true**, not every step required to make it true.

# Part 3 — Desired State

Desired state lives in Kubernetes API objects.

Example:

```text
Deployment.spec.replicas = 4
```

The cluster compares this with actual Pods and reconciles the difference.

# Part 4 — Actual State

Actual state comes from current cluster observations:

```text
running Pods
node health
container states
available endpoints
volume attachments
```

Controllers use API state and component reports to decide what to do next.

# Part 5 — Reconciliation Loop

A controller repeatedly performs:

```text
observe
 ↓
compare desired vs actual
 ↓
act
 ↓
observe again
```

This is why deleting a Pod controlled by a Deployment usually causes another Pod to appear.

# Part 6 — Control Plane

The control plane makes cluster-level decisions and stores desired state.

Core components:

```text
kube-apiserver
etcd
kube-scheduler
kube-controller-manager
```

Cloud integrations may add cloud-controller-manager.

# Part 7 — kube-apiserver

The API server is the main front door.

```text
kubectl
controllers
scheduler
kubelets
operators
```

communicate through the Kubernetes API rather than directly editing etcd.

The API server performs authentication, authorization, admission, validation, and persistence.

# Part 8 — etcd

`etcd` is the strongly consistent key-value store containing cluster state.

Think:

```text
desired state
resource metadata
configuration
coordination data
```

Losing etcd without backup can mean losing the cluster's control-plane state.

# Part 9 — kube-scheduler

Scheduler selects a suitable Node for an unscheduled Pod.

It considers:

```text
resource requests
node selectors
affinity
taints/tolerations
topology
constraints
```

It does not start containers itself.

# Part 10 — kube-controller-manager

Runs core controllers such as controllers for:

```text
Deployments/ReplicaSets
Nodes
Jobs
Endpoints
ServiceAccounts
```

Controllers reconcile Kubernetes objects.

# Part 11 — Worker Node

A worker Node runs application Pods.

Important node components:

```text
kubelet
container runtime
kube-proxy
CNI networking
CSI integration where needed
```

# Part 12 — kubelet

The kubelet is the node agent.

It receives Pod specifications assigned to its Node and ensures containers are created and healthy through the container runtime.

It reports node and Pod status back to the API server.

# Part 13 — Container Runtime

Modern Kubernetes uses CRI-compatible runtimes such as:

```text
containerd
CRI-O
```

Kubernetes no longer requires Docker Engine on nodes.

OCI images built with Docker remain usable.

# Part 14 — CRI

The Container Runtime Interface lets kubelet work with compatible runtimes through a standard API.

Concept:

```text
kubelet
 ↓ CRI
containerd / CRI-O
 ↓
OCI runtime
 ↓
Linux containers
```

# Part 15 — kube-proxy

`kube-proxy` implements Service networking behavior on nodes using supported data-plane mechanisms.

The exact implementation can involve Linux packet-processing technologies such as nftables/iptables/IPVS depending on version/configuration.

Some CNI/eBPF solutions can replace parts of traditional kube-proxy behavior.

# Part 16 — CNI Concept

Container Network Interface plugins provide Pod networking.

Kubernetes requires a network model where Pods receive network connectivity.

Examples of CNI ecosystems include:

```text
Calico
Cilium
Flannel
cloud-provider CNIs
```

# Part 17 — CSI Concept

Container Storage Interface standardizes storage-plugin integration.

```text
Pod
 ↓ PVC
StorageClass
 ↓
CSI driver
 ↓
storage system
```

# Part 18 — Cluster DNS

CoreDNS is commonly deployed as cluster DNS.

Pods can resolve Services such as:

```text
db.default.svc.cluster.local
```

instead of hardcoding Service IP addresses.

# Part 19 — Kubernetes Object

Kubernetes resources are API objects.

Examples:

```text
Pod
Deployment
Service
ConfigMap
Secret
PersistentVolumeClaim
Job
```

# Part 20 — API Resource

Discover resources:

```bash
kubectl api-resources
```

This reveals:

```text
kind
short name
API group
namespaced?
verbs
```

# Part 21 — API Version

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
```

`apps` is API group and `v1` version.

Different resource types live in different API groups.

# Part 22 — Core API Group

Core resources use:

```yaml
apiVersion: v1
```

Examples:

```text
Pod
Service
ConfigMap
Secret
Namespace
PersistentVolume
```

# Part 23 — Spec and Status

Most objects separate:

```text
spec   → desired state
status → observed state
```

Users normally edit `spec`.

Controllers update `status`.

# Part 24 — Metadata

Common metadata:

```yaml
metadata:
  name: api
  namespace: production
  labels:
    app: api
```

Metadata identifies and organizes the resource.

# Part 25 — UID

Every created object receives a unique UID.

If you delete and recreate `Pod/api`, it can have the same name but a different UID.

Controllers use UID/owner references to distinguish object identity.

# Part 26 — Generation and ResourceVersion

Kubernetes tracks revisions/versions of API objects.

`resourceVersion` supports concurrency/watch behavior.

Do not manually treat it as a simple sequential version number.

# Part 27 — Finalizers

A finalizer blocks object removal until cleanup occurs.

Example lifecycle:

```text
delete requested
 ↓
deletionTimestamp set
 ↓
controller performs cleanup
 ↓
finalizer removed
 ↓
object disappears
```

# Part 28 — Garbage Collection

Owner references let Kubernetes clean up dependent resources.

Example:

```text
Deployment
 ↓ owns
ReplicaSet
 ↓ owns
Pods
```

# Part 29 — Namespace

Namespaces partition **namespaced API objects** inside one cluster.

Examples:

```text
development
staging
production
```

They are organizational/policy boundaries, not automatically complete security boundaries.

# Part 30 — Cluster-Scoped Resources

Not all objects belong to namespaces.

Examples:

```text
Node
PersistentVolume
Namespace
ClusterRole
StorageClass
```

Always know resource scope before applying permissions or YAML.

# Part 31 — kubectl

`kubectl` is the primary Kubernetes CLI.

General structure:

```bash
kubectl <verb> <resource> <name>
```

Example:

```bash
kubectl get pod api
```

# Part 32 — Kubeconfig

`kubectl` uses kubeconfig containing:

```text
clusters
users/credentials
contexts
current-context
```

Default path is commonly:

```text
~/.kube/config
```

# Part 33 — Context

Context combines:

```text
cluster
user
namespace
```

Inspect:

```bash
kubectl config get-contexts
kubectl config current-context
```

# Part 34 — Switch Context

```bash
kubectl config use-context my-cluster
```

Before destructive operations verify:

```text
context
namespace
resource
```

# Part 35 — Set Namespace in Context

```bash
kubectl config set-context --current \
  --namespace=development
```

This reduces repeated `-n` usage but can also cause mistakes if forgotten.

# Part 36 — kubectl get

```bash
kubectl get pods
kubectl get deployments
kubectl get svc
```

Wide output:

```bash
kubectl get pods -o wide
```

# Part 37 — Output Formats

Useful:

```bash
-o yaml
-o json
-o name
-o wide
-o jsonpath=...
-o custom-columns=...
```

# Part 38 — kubectl describe

`describe` combines object details and related events.

```bash
kubectl describe pod api
```

Excellent first troubleshooting command.

# Part 39 — kubectl explain

Built-in schema documentation:

```bash
kubectl explain deployment
kubectl explain deployment.spec
kubectl explain pod.spec.containers.resources
```

Use it instead of guessing YAML fields.

# Part 40 — Declarative apply

```bash
kubectl apply -f deployment.yaml
```

Declarative files can be version controlled.

Prefer this for repeatable environments.

# Part 41 — Create

Imperative:

```bash
kubectl create namespace dev
```

Useful for labs and some one-time resources.

# Part 42 — Run

Create simple Pod:

```bash
kubectl run nginx \
  --image=nginx:alpine
```

Useful for temporary testing.

# Part 43 — Dry Run

Generate YAML:

```bash
kubectl run web \
  --image=nginx \
  --dry-run=client \
  -o yaml
```

This is valuable for learning and fast object creation.

# Part 44 — Delete

```bash
kubectl delete -f app.yaml
kubectl delete pod api
```

Deleting a controller-managed Pod does not delete the controller.

# Part 45 — Edit

```bash
kubectl edit deployment api
```

Convenient during labs/incidents, but production configuration should normally return to source control/IaC.

# Part 46 — Patch

Patch a resource:

```bash
kubectl patch deployment api \
  -p '{"spec":{"replicas":5}}'
```

Useful for controlled targeted modifications.

# Part 47 — Scale

```bash
kubectl scale deployment api --replicas=5
```

Changes desired replica count.

# Part 48 — Rollout

```bash
kubectl rollout status deployment/api
kubectl rollout history deployment/api
```

Tracks Deployment rollouts.

# Part 49 — Labels via CLI

```bash
kubectl label pod api env=dev
```

Overwrite:

```bash
kubectl label pod api env=prod --overwrite
```

# Part 50 — Annotations via CLI

```bash
kubectl annotate deployment api \
  owner="platform-team"
```

# Part 51 — YAML Indentation

YAML uses indentation.

Incorrect:

```yaml
spec:
containers:
```

Correct:

```yaml
spec:
  containers:
```

Validate before apply.

# Part 52 — Lists in YAML

```yaml
containers:
  - name: api
    image: example/api:1.0
  - name: sidecar
    image: example/helper:1.0
```

# Part 53 — Maps in YAML

```yaml
labels:
  app: api
  tier: backend
```

# Part 54 — Boolean/String Gotchas

Quote values when ambiguity matters.

Kubernetes schemas validate types, but templating/parsing can still produce surprising YAML.

Use `kubectl apply --dry-run=server` when appropriate.

# Part 55 — Multi-Document YAML

Separate documents:

```yaml
apiVersion: v1
kind: Service
...
---
apiVersion: apps/v1
kind: Deployment
...
```

# Part 56 — Server-Side Validation

The API server validates schemas/admission.

A syntactically valid YAML file can still be rejected because:

```text
wrong field
wrong type
policy violation
invalid selector
```

# Part 57 — Apply Diff

Preview:

```bash
kubectl diff -f manifests/
```

Useful before production apply.

# Part 58 — Server-Side Apply Concept

Server-Side Apply tracks field ownership among managers.

Useful for collaborative controllers/tools managing different object fields.

Understand before mixing automation systems.

# Part 59 — Field Manager

Different clients/controllers can own fields.

Conflicts happen when another manager tries to change owned field without resolving ownership.

# Part 60 — Watch

```bash
kubectl get pods -w
```

Observe state transitions in real time.

# Part 61 — Events

```bash
kubectl get events \
  --sort-by=.metadata.creationTimestamp
```

Events reveal scheduling, pull, mount, probe, and controller failures.

# Part 62 — API Discovery

```bash
kubectl api-versions
kubectl api-resources
```

Useful when manifests use unavailable/deprecated APIs.

# Part 63 — Namespace Flag

```bash
kubectl get pods -n production
```

All namespaces:

```bash
kubectl get pods -A
```

# Part 64 — Aliases

Shell shortcuts can improve speed:

```bash
alias k=kubectl
```

But learn full command first and avoid ambiguous production scripts.

# Part 65 — Safe kubectl Workflow

Before write:

```bash
kubectl config current-context
kubectl config view --minify
kubectl get ns
```

Then:

```text
read
describe
diff
apply
verify
```

# Part 66 — Pod

A Pod is Kubernetes' smallest schedulable workload unit.

A Pod contains one or more containers sharing:

```text
network namespace
Pod IP
port space
selected volumes
lifecycle
```

# Part 67 — Why Not Schedule Individual Containers?

Some containers must be colocated.

Example:

```text
application
+
local helper proxy
```

The Pod is the unit Kubernetes schedules together.

# Part 68 — Pod IP

Each Pod normally receives an IP.

All containers in the same Pod share that Pod network namespace and communicate using:

```text
localhost
```

# Part 69 — Pod YAML

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web
spec:
  containers:
    - name: nginx
      image: nginx:alpine
```

# Part 70 — Container Name

Container names must be unique inside one Pod.

Use names that describe roles:

```text
api
metrics-proxy
log-helper
```

# Part 71 — Image Pull

Kubelet/runtime pulls container image if needed according to `imagePullPolicy`.

Failures commonly appear as:

```text
ErrImagePull
ImagePullBackOff
```

# Part 72 — imagePullPolicy

Common values:

```text
Always
IfNotPresent
Never
```

Immutable digests reduce ambiguity.

# Part 73 — Pod Phase

Common phases:

```text
Pending
Running
Succeeded
Failed
Unknown
```

Phase is coarse; inspect individual container states for real troubleshooting.

# Part 74 — Container States

Container state can be:

```text
Waiting
Running
Terminated
```

`Waiting.reason` often reveals startup problems.

# Part 75 — Restart Policy

Pod-level `restartPolicy`:

```text
Always
OnFailure
Never
```

Deployments expect long-running Pods and generally use `Always`.

# Part 76 — CrashLoopBackOff

Means container repeatedly starts and fails, and Kubernetes applies increasing restart backoff.

Investigate:

```bash
kubectl logs POD
kubectl logs POD --previous
kubectl describe pod POD
```

# Part 77 — Previous Logs

```bash
kubectl logs pod-name --previous
```

Critical when current container has restarted and previous crash logs are needed.

# Part 78 — Multi-Container Pod

Use only for tightly coupled processes that must share lifecycle/network/volumes.

Do not put unrelated services in one Pod merely to avoid networking.

# Part 79 — Sidecar Pattern

Sidecar provides supporting capability:

```text
main app
+
proxy/logging/helper
```

Modern Kubernetes includes native sidecar container semantics based on restartable init containers in current versions.

# Part 80 — Init Container

Runs before application containers.

Example uses:

```text
wait for dependency
prepare files
generate configuration
```

Each init container must complete successfully before next proceeds.

# Part 81 — Init Container YAML

```yaml
initContainers:
  - name: init
    image: busybox
    command: ["sh","-c","echo ready > /work/state"]
    volumeMounts:
      - name: work
        mountPath: /work
```

# Part 82 — Native Sidecar Concept

Current Kubernetes supports sidecar semantics through init containers with restart behavior that continues alongside app containers.

Use when lifecycle ordering matters.

# Part 83 — Ephemeral Containers

Ephemeral containers are added to an existing Pod for debugging.

They do not behave like normal app containers and are not automatically restarted.

Useful when production image lacks shell/debug tools.

# Part 84 — kubectl debug

Example:

```bash
kubectl debug pod/api \
  -it \
  --image=busybox
```

Use only in authorized environments and understand namespace/process-sharing options.

# Part 85 — Pod Command and Args

Kubernetes:

```yaml
command:
args:
```

roughly correspond to overriding image ENTRYPOINT/CMD.

Wrong override can cause immediate exit.

# Part 86 — Environment Variables

```yaml
env:
  - name: APP_ENV
    value: production
```

# Part 87 — Container Ports

```yaml
ports:
  - containerPort: 8080
```

This documents port and can support named-port references.

It does not by itself expose the Pod outside cluster.

# Part 88 — Named Ports

```yaml
ports:
  - name: http
    containerPort: 8080
```

Service/probe can reference `http`.

# Part 89 — Working Directory

```yaml
workingDir: /app
```

overrides image working directory.

# Part 90 — Termination Message

Containers can write termination status used by Kubernetes for troubleshooting.

Useful for concise failure reason.

# Part 91 — Pod Hostname

Pod hostname defaults from Pod name in many cases, with configurable hostname/subdomain options.

Do not use Pod hostname as stable service discovery for replaceable replicas.

# Part 92 — Pod Lifecycle

```text
create
 ↓
schedule
 ↓
pull image
 ↓
init
 ↓
start app
 ↓
ready
 ↓
terminate
 ↓
deleted
```

# Part 93 — Termination Grace Period

Kubernetes normally allows a grace period before force killing containers.

Application should handle SIGTERM and drain gracefully.

# Part 94 — preStop Hook

Lifecycle hook can run before termination.

Use carefully:

```text
preStop duration
+
application shutdown
```

must fit grace period.

# Part 95 — postStart Hook

Runs after container starts, but not necessarily before ENTRYPOINT executes.

Do not assume strict sequencing with main process startup.

# Part 96 — Static Pod Concept

Static Pods are managed directly by kubelet from local manifests rather than ordinary controllers.

Control-plane components in kubeadm clusters are often static Pods.

Administration course covers them deeply.

# Part 97 — Mirror Pod

API server shows a mirror object for static Pod, but control remains with node-local manifest/kubelet.

# Part 98 — Pod Immutability

Many Pod spec fields cannot be changed after creation.

Controllers replace Pods rather than mutating them extensively.

# Part 99 — Disposable Pod Principle

Do not rely on a specific Pod identity for stateless workload.

A Deployment can replace it at any time.

# Part 100 — Pod Conditions

Conditions can include concepts such as:

```text
PodScheduled
Initialized
ContainersReady
Ready
```

Use to understand lifecycle.

# Part 101 — Pod Ready

A running Pod is not necessarily Ready.

Readiness determines whether it should receive Service traffic.

# Part 102 — Pod Scheduling Gate Concept

Advanced workflows can intentionally delay scheduling until external orchestration removes scheduling gates.

Know it exists; administration may use it in specialized systems.

# Part 103 — ImagePullSecrets

Private registry credentials can be referenced:

```yaml
imagePullSecrets:
  - name: registry-creds
```

Prefer workload/registry-native identity where available.

# Part 104 — Pod ServiceAccount

```yaml
serviceAccountName: app-sa
```

determines Kubernetes workload identity used for API access.

# Part 105 — Automount Token

If workload does not need Kubernetes API access:

```yaml
automountServiceAccountToken: false
```

can reduce token exposure.

# Part 106 — Pod Security Context Intro

Pod/container security settings include:

```text
runAsNonRoot
runAsUser
capabilities
readOnlyRootFilesystem
seccompProfile
fsGroup
```

# Part 107 — Pod Overhead Concept

Sandboxed runtimes can add overhead accounted in scheduling.

Resource planning must include platform/runtime overhead.

# Part 108 — HostPath Risk

`hostPath` mounts host filesystem into Pod.

This can expose sensitive host data/control.

Avoid for normal applications.

# Part 109 — hostNetwork Risk

`hostNetwork: true` shares node network namespace.

Reduces isolation and introduces port conflicts.

# Part 110 — hostPID Risk

`hostPID: true` exposes host process namespace.

Reserved for tightly controlled infrastructure/debug workloads.

# Part 111 — Privileged Pod Risk

Privileged containers receive broad host privileges.

Do not use to solve routine permission failures.

# Part 112 — Pod Inspection

```bash
kubectl get pod api -o yaml
kubectl describe pod api
```

Inspect both spec and status.

# Part 113 — Pod Exec

```bash
kubectl exec -it api -- sh
```

For multi-container Pod:

```bash
kubectl exec -it api -c app -- sh
```

# Part 114 — Pod Port Forward

```bash
kubectl port-forward pod/api 8080:8080
```

Creates temporary local tunnel for testing.

Not a production exposure mechanism.

# Part 115 — Pod Troubleshooting Tree

```text
Pending?
  → scheduler/resources/volume

Waiting?
  → image/config/mount

Running not Ready?
  → readiness/dependency

Restarting?
  → logs/previous/OOM/probe

No traffic?
  → Service/selector/network/app bind
```

# Part 116 — Labels

Labels are queryable key-value metadata.

```yaml
labels:
  app: orders
  tier: backend
  env: prod
```

They drive selectors.

# Part 117 — Label Design

Use stable dimensions:

```text
app
component
environment
version
managed-by
```

Avoid putting large/unstructured data in labels.

# Part 118 — Selectors

Selector chooses objects by labels.

Example:

```text
app=orders
```

Services and controllers depend heavily on correct selectors.

# Part 119 — Set-Based Selector

Concepts include:

```text
In
NotIn
Exists
DoesNotExist
```

for expressive selection.

# Part 120 — Annotations

Annotations store non-identifying metadata:

```text
build URL
owner notes
checksum
integration configuration
```

They are not used as selector keys.

# Part 121 — OwnerReferences

Controller ownership example:

```text
Deployment
  ↓
ReplicaSet
  ↓
Pod
```

Garbage collector uses owner relationships.

# Part 122 — ReplicaSet

Ensures a specified number of matching Pods exist.

Normally created indirectly by a Deployment rather than authored directly.

# Part 123 — ReplicaSet Selector

ReplicaSet identifies Pods using selector.

Selector must match Pod template labels.

# Part 124 — Deployment

Deployment manages stateless application rollout through ReplicaSets.

```text
Deployment
 ↓
ReplicaSet v2
 ↓
Pods
```

# Part 125 — Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: example/api:1.0
```

# Part 126 — Pod Template

`spec.template` is a Pod template.

Changing it creates a new rollout/revision.

# Part 127 — Desired Replicas

```yaml
replicas: 3
```

Deployment controller ensures appropriate ReplicaSet maintains three Pods.

# Part 128 — RollingUpdate

Default strategy for Deployments.

Old Pods are gradually replaced by new Pods while maintaining availability constraints.

# Part 129 — maxUnavailable

Controls maximum Pods unavailable during rolling update.

Example:

```text
replicas=10
maxUnavailable=2
```

permits temporary available count as low as 8.

# Part 130 — maxSurge

Controls extra Pods above desired replicas during rollout.

Example:

```text
replicas=10
maxSurge=2
```

can temporarily create 12 Pods.

# Part 131 — Recreate Strategy

Stops old Pods before creating new ones.

Useful only when versions cannot coexist or workload requires exclusive access.

Causes downtime.

# Part 132 — Change Image

```bash
kubectl set image deployment/api \
  api=example/api:2.0
```

Then:

```bash
kubectl rollout status deployment/api
```

# Part 133 — Rollout History

```bash
kubectl rollout history deployment/api
```

View revisions.

# Part 134 — Rollback

```bash
kubectl rollout undo deployment/api
```

Can target a previous revision.

Verify application/data compatibility before rollback.

# Part 135 — Pause Rollout

```bash
kubectl rollout pause deployment/api
```

allows multiple template changes before resume in selected workflows.

# Part 136 — Progress Deadline

Deployment can mark rollout failed to progress after configured deadline.

It does not magically rollback unless external automation/operator handles that behavior.

# Part 137 — Revision History Limit

Controls retained old ReplicaSets for rollback/history.

Balance rollback needs vs clutter.

# Part 138 — Deployment Conditions

Inspect:

```bash
kubectl describe deployment api
```

for:

```text
Available
Progressing
ReplicaFailure
```

# Part 139 — Scaling Deployment

```bash
kubectl scale deploy/api --replicas=6
```

Creates/removes Pods through ReplicaSet.

# Part 140 — Self-Healing

Delete one Pod:

```bash
kubectl delete pod API_POD
```

ReplicaSet notices replica deficit and creates replacement.

# Part 141 — Why Not Manage Pods Directly

Direct Pod:

```text
dies → remains gone
```

Deployment-managed Pod:

```text
dies → controller replaces it
```

Production long-running workloads should normally use controllers.

# Part 142 — DaemonSet

Runs a Pod on every matching Node or set of Nodes.

Uses:

```text
log agents
node monitoring
network plugins
storage plugins
```

# Part 143 — DaemonSet Rolling Update

DaemonSets support update strategies for node-level agents.

One bad DaemonSet can impact entire cluster, so rollout carefully.

# Part 144 — StatefulSet

For stateful applications needing:

```text
stable identity
ordered rollout
stable storage
```

Pods receive names such as:

```text
db-0
db-1
db-2
```

# Part 145 — Headless Service

StatefulSet often uses a headless Service:

```yaml
clusterIP: None
```

to provide direct Pod DNS records rather than one virtual Service IP.

# Part 146 — volumeClaimTemplates

StatefulSet can generate one PVC per replica.

```text
db-0 → data-db-0
db-1 → data-db-1
```

storage stays associated with identity.

# Part 147 — StatefulSet Is Not Database HA

Kubernetes can preserve identity/storage, but database replication/election/consistency remain application-specific.

StatefulSet does not automatically make PostgreSQL/MySQL highly available.

# Part 148 — Job

Runs tasks to completion.

Examples:

```text
data migration
batch conversion
one-time report
```

Job controller retries/manages completion.

# Part 149 — Job Completions

A Job can require multiple successful completions.

Useful for batch workloads.

# Part 150 — Parallelism

Controls how many Job Pods run concurrently.

Ensure backend/resource systems can handle concurrency.

# Part 151 — Backoff Limit

Limits Job retry attempts before marking failed.

Avoid infinite failing jobs.

# Part 152 — TTL After Finished

Finished Jobs can be automatically cleaned after time-to-live in supported configuration.

# Part 153 — CronJob

Creates Jobs on schedules.

```yaml
schedule: "0 2 * * *"
```

means daily at 02:00 using cron syntax.

# Part 154 — CronJob Concurrency Policy

Options conceptually:

```text
Allow
Forbid
Replace
```

Choose based on whether overlapping executions are safe.

# Part 155 — CronJob Time Zone

Modern Kubernetes supports explicit time-zone configuration for CronJobs.

Prefer explicit scheduling semantics rather than relying on controller-manager local timezone assumptions.

# Part 156 — Suspend CronJob

Pause scheduling without deleting definition:

```yaml
suspend: true
```

# Part 157 — Controller Selection

Use:

```text
Deployment → stateless service
DaemonSet → one per node
StatefulSet → stable stateful identity
Job → run to completion
CronJob → scheduled Jobs
```

# Part 158 — Custom Controllers Concept

Kubernetes extensibility allows custom controllers/operators to reconcile custom resources.

This is how many databases/platforms automate complex lifecycle.

# Part 159 — Operator Pattern

Operator combines:

```text
Custom Resource
+
Controller
+
domain knowledge
```

Example: database operator can automate backup/failover/upgrade.

# Part 160 — CRD Concept

CustomResourceDefinition adds new resource type to Kubernetes API.

Example:

```text
DatabaseCluster
Certificate
Application
```

# Part 161 — Do Not Abuse CRDs

Use CRDs when you need Kubernetes-style API/reconciliation.

Do not turn every application config field into a cluster API extension.

# Part 162 — Controller Debugging

If desired replicas do not appear:

```text
controller object status
events
selector/template
quota
admission
scheduler
```

may be responsible.

# Part 163 — Ownership Debugging

```bash
kubectl get pod POD -o jsonpath='{.metadata.ownerReferences}'
```

tells which controller owns it.

# Part 164 — Manual Pod Deletion During Incident

Deleting a bad Pod can restore service if controller recreates it, but capture logs/evidence first and fix root cause.

# Part 165 — Workload Controller Mental Model

Controllers make Pods disposable.

You operate **desired workload objects**, not individual container pets.

# Part 166 — Kubernetes Network Model

Fundamental expectation:

```text
Pod → Pod communication
Node → Pod communication
Pod IP unique in cluster network
```

CNI implementation supplies data plane.

# Part 167 — Service

Service provides stable virtual endpoint for dynamic Pods.

```text
Service
 ↓ selector
Pods
```

Pods can change IP while Service identity remains.

# Part 168 — ClusterIP

Default Service type.

Accessible from inside cluster through stable virtual IP/DNS.

```yaml
type: ClusterIP
```

# Part 169 — Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  selector:
    app: api
  ports:
    - port: 80
      targetPort: 8080
```

# Part 170 — port vs targetPort

```text
Service port = 80
Pod targetPort = 8080
```

Clients connect to Service:80; Service routes to Pod:8080.

# Part 171 — NodePort

Exposes Service on a port on each Node.

```text
NodeIP:NodePort
 ↓
Service
 ↓
Pod
```

Useful for some labs/integrations; rarely the preferred public production edge by itself.

# Part 172 — LoadBalancer

Requests an external/internal load balancer from supported cloud/load-balancer integration.

```text
External LB
 ↓
Service
 ↓
Pods
```

# Part 173 — ExternalName

Maps Service DNS name to external DNS CNAME-like target.

No Pod selector/proxying.

# Part 174 — Headless Service

```yaml
clusterIP: None
```

DNS returns backend Pod/endpoint records directly.

Useful for StatefulSets/discovery.

# Part 175 — EndpointSlice

EndpointSlices represent scalable backend endpoint information for Services.

Inspect:

```bash
kubectl get endpointslices
```

Modern Kubernetes uses them rather than relying only on legacy Endpoints object.

# Part 176 — Service Selector Failure

If Service has no endpoints:

```bash
kubectl get svc api
kubectl get endpointslices -l kubernetes.io/service-name=api
kubectl get pods --show-labels
```

Usually selector/labels or readiness.

# Part 177 — Ready Endpoints

Pods failing readiness are generally removed from normal Service endpoint traffic.

This is why readiness directly affects availability.

# Part 178 — Session Affinity

Service can optionally use client-IP affinity.

Do not rely on stickiness when applications should be stateless.

# Part 179 — Internal Traffic Policy Concept

Service traffic policies can influence node-local vs cluster-wide endpoint routing in supported scenarios.

Use only with understanding of availability trade-offs.

# Part 180 — External Traffic Policy Concept

Can influence preservation of client source IP and local endpoint routing for externally exposed Services.

Trade-offs include uneven traffic/availability.

# Part 181 — CoreDNS

CoreDNS watches Kubernetes Service/Pod data and answers cluster DNS.

Service DNS:

```text
api.default.svc.cluster.local
```

# Part 182 — DNS Search Paths

Inside a Pod, resolver search can allow:

```text
api
api.default
api.default.svc
```

depending on namespace/search configuration.

# Part 183 — Cross-Namespace DNS

From namespace `frontend` to Service `db` in `backend`:

```text
db.backend
```

or FQDN.

# Part 184 — DNS Debugging

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  -- nslookup kubernetes.default
```

Then inspect CoreDNS if resolution fails.

# Part 185 — Ingress

Ingress is an API for HTTP/HTTPS routing, implemented by an Ingress controller.

```text
Client
 ↓
Ingress Controller
 ↓
Service
 ↓
Pods
```

# Part 186 — Ingress Resource vs Controller

Creating Ingress YAML alone does not create packet-processing behavior.

A compatible Ingress controller must be installed.

# Part 187 — Ingress Host Routing

```text
api.example.com → api Service
www.example.com → web Service
```

# Part 188 — Ingress Path Routing

```text
/api → api
/static → frontend
```

# Part 189 — Ingress TLS

Ingress can reference TLS Secrets/certificates.

Certificate lifecycle is typically automated through a controller such as cert-manager or cloud integration, but this is external to core Kubernetes.

# Part 190 — Gateway API

Gateway API is the modern, role-oriented, more expressive successor/extension to many Ingress use cases.

Current ecosystem baseline includes Gateway API v1.6-era development.

Core concepts:

```text
GatewayClass
Gateway
HTTPRoute
GRPCRoute
TCPRoute
UDPRoute
```

# Part 191 — GatewayClass

Represents infrastructure/controller class capable of providing Gateways.

Comparable conceptually to choosing implementation.

# Part 192 — Gateway

Defines listener/infrastructure entry point:

```text
80 HTTP
443 HTTPS
```

and attachment policy.

# Part 193 — HTTPRoute

Defines HTTP routing separately from infrastructure Gateway.

This separation supports platform-team and application-team responsibilities.

# Part 194 — Ingress vs Gateway API

Ingress:

```text
simple mature HTTP routing
```

Gateway API:

```text
richer role separation
more expressive routing
broader protocol support
```

Controller support determines practical use.

# Part 195 — NetworkPolicy

NetworkPolicy defines allowed network communication for Pods when CNI supports enforcement.

Without enforcement support, object may exist but have no effect.

# Part 196 — Default Allow

By default, Pods are generally non-isolated for ingress/egress until selected by policy.

A production zero-trust design often starts with default deny.

# Part 197 — Default Deny Ingress

Concept:

```yaml
podSelector: {}
policyTypes:
  - Ingress
```

with no allowed ingress rules isolates matching Pods from ingress.

# Part 198 — Allow API to DB

Use labels:

```text
api Pods → role=api
db Pods  → role=db
```

Policy permits TCP 5432 from API to DB only.

# Part 199 — Egress Policy

Control outbound communication:

```text
DNS
database
external APIs
```

Remember to allow required DNS traffic in restrictive designs.

# Part 200 — NetworkPolicy Scope

Policies are namespaced and select Pods.

Cross-namespace rules can use namespace selectors.

# Part 201 — NetworkPolicy Is Layer 3/4

Core NetworkPolicy works mainly with IP/port/protocol selectors.

Layer-7 policy requires CNI/service-mesh-specific features.

# Part 202 — Service Mesh Concept

A service mesh can add:

```text
mTLS
traffic policy
telemetry
retries
authorization
```

between services.

It adds complexity and is not required for basic Kubernetes.

# Part 203 — Port-Forward Service

```bash
kubectl port-forward svc/api 8080:80
```

temporary local testing tunnel.

# Part 204 — Proxy Environment

Corporate proxy configuration can affect:

```text
image pulls
Pods
nodes
API clients
```

Each layer may need different `NO_PROXY` entries for cluster CIDRs/DNS.

# Part 205 — MTU in Kubernetes

CNI overlays can reduce effective MTU.

Symptoms:

```text
small traffic works
large TLS request hangs
intermittent cross-node failures
```

# Part 206 — Pod CIDR

Many clusters allocate Pod address ranges distinct from Service ranges.

CNI design determines details.

# Part 207 — Service CIDR

Virtual Service IP range is separate from normal Pod addresses in many clusters.

Do not overlap with node/on-prem/VPN networks.

# Part 208 — localhost Misconception

Inside Pod:

```text
localhost
```

reaches containers in same Pod.

It does **not** reach a database Pod in another Pod.

# Part 209 — Service Discovery Principle

Applications should connect:

```text
postgres.database.svc
```

rather than Pod IP.

Service identity survives Pod replacement.

# Part 210 — Network Debug Order

```text
application listener
Pod IP
Service selector/endpoints
DNS
NetworkPolicy
CNI path
node routing/firewall
Ingress/Gateway
external LB
```

# Part 211 — Service Without Selector

A Service can be defined without selector and paired with manually/controller-managed EndpointSlices for external/backends.

Useful for advanced integration.

# Part 212 — External Service Discovery

Use:

```text
ExternalName
Service without selector
external DNS/service discovery
```

depending on integration.

Avoid hardcoded IP inside application image.

# Part 213 — Topology-Aware Routing Concept

Kubernetes can use topology hints/policies in supported features to prefer nearby endpoints.

Use only after measuring latency/availability trade-offs.

# Part 214 — Network Abstraction Stack

```text
Pod IP
 ↓
Service
 ↓
Ingress/Gateway
 ↓
external DNS/load balancer
```

Each layer solves a different stability/exposure problem.

# Part 215 — Networking Mental Model

When traffic fails, ask:

```text
Can source resolve name?
Does Service have endpoints?
Is target Ready?
Is target listening?
Does policy allow it?
Does CNI route it?
```

# Part 216 — ConfigMap

Stores non-secret configuration.

Examples:

```text
feature flags
URLs
logging configuration
application files
```

# Part 217 — ConfigMap Literal

```bash
kubectl create configmap app-config \
  --from-literal=APP_ENV=production
```

# Part 218 — ConfigMap File

```bash
kubectl create configmap nginx-config \
  --from-file=nginx.conf
```

# Part 219 — ConfigMap envFrom

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

Injects keys as environment variables.

# Part 220 — ConfigMap Key Reference

```yaml
env:
  - name: APP_ENV
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: APP_ENV
```

# Part 221 — ConfigMap Volume

Mount configuration as files.

Updates to projected volumes may propagate eventually, but applications may need reload/restart.

# Part 222 — Secret

Stores sensitive data in Kubernetes API.

Important:

```text
Secret is not magically safe merely because it is kind: Secret.
```

Base64 representation is encoding, not encryption.

# Part 223 — Secret Base64

```bash
printf '%s' 'password' | base64
```

Anyone with Secret read permission can normally recover plaintext.

Protect RBAC and etcd encryption.

# Part 224 — Secret stringData

Manifest can use:

```yaml
stringData:
  password: example
```

API server converts to encoded `data`.

Do not commit real secrets to Git.

# Part 225 — Secret Environment

Can inject Secret into environment.

Risk:

```text
process env
debug dumps
logs
```

File/projected secret or external secret system may be preferable.

# Part 226 — Secret Volume

Mounted Secret files are often safer for applications that can read credentials from filesystem.

Set least permissions.

# Part 227 — External Secret Management Concept

Production clusters often integrate:

```text
cloud secret managers
Vault
external-secrets controllers
CSI secret stores
```

to avoid manually managing static Kubernetes Secret manifests.

# Part 228 — Immutable ConfigMap/Secret

Objects can be marked immutable in supported APIs.

This can reduce accidental mutation and watch load for stable config.

# Part 229 — Config Reload Pattern

Configuration changes require application behavior:

```text
watch file
SIGHUP reload
restart rollout
```

Kubernetes does not automatically teach application how to reload.

# Part 230 — Config Checksum Rollout Pattern

Helm/Kustomize workflows often annotate Pod template with config hash so config change triggers new Pods.

Concept:

```text
config hash changes
→ Deployment template changes
→ rollout
```

# Part 231 — Liveness Probe

Answers:

```text
Should kubelet restart this container?
```

Do not point liveness at fragile external dependency.

# Part 232 — Readiness Probe

Answers:

```text
Should this Pod receive traffic?
```

Failure removes Pod from ready Service endpoints without necessarily restarting it.

# Part 233 — Startup Probe

Protects slow-starting app from premature liveness failures.

Once startup succeeds, liveness/readiness operate normally.

# Part 234 — HTTP Probe

```yaml
httpGet:
  path: /health
  port: 8080
```

# Part 235 — TCP Probe

Checks whether TCP port can accept connection.

It cannot prove application-level correctness.

# Part 236 — Exec Probe

Runs command inside container.

Use sparingly because expensive commands can add load.

# Part 237 — Probe Timing

Important:

```text
initialDelaySeconds
periodSeconds
timeoutSeconds
failureThreshold
successThreshold
```

Tune based on application behavior.

# Part 238 — Probe Storm

Hundreds of Pods probing dependency every second can create load.

Health endpoints should be lightweight.

# Part 239 — Resource Request

Request is scheduler's resource planning amount.

Example:

```yaml
resources:
  requests:
    cpu: 250m
    memory: 256Mi
```

# Part 240 — Resource Limit

Limit constrains maximum behavior.

```yaml
limits:
  cpu: "1"
  memory: 512Mi
```

# Part 241 — CPU Units

```text
1000m = 1 CPU
250m = 0.25 CPU
```

# Part 242 — Memory Units

Use binary suffix:

```text
Mi
Gi
```

Example:

```text
512Mi
2Gi
```

# Part 243 — Memory Limit and OOM

Exceeding memory limit can cause container OOM kill.

Inspect:

```bash
kubectl describe pod
kubectl get pod -o yaml
```

for termination reason such as `OOMKilled`.

# Part 244 — CPU Limit and Throttling

CPU over limit is throttled rather than usually killed.

Symptoms:

```text
latency
timeouts
queue buildup
```

# Part 245 — QoS Classes

Pods are categorized based on resource request/limit configuration:

```text
Guaranteed
Burstable
BestEffort
```

This affects eviction priority under node pressure.

# Part 246 — Guaranteed QoS

Generally requires each container to have CPU/memory requests equal limits.

Useful for predictable critical workloads, but may reduce scheduling flexibility.

# Part 247 — Burstable QoS

At least some requests/limits exist, but not all meet Guaranteed criteria.

Common production class.

# Part 248 — BestEffort QoS

No CPU/memory requests/limits.

Most vulnerable to eviction under resource pressure and difficult to capacity-plan.

# Part 249 — LimitRange Concept

Namespace policy can set:

```text
default requests
default limits
minimum/maximum
```

Administration course covers configuration deeply.

# Part 250 — ResourceQuota Concept

Namespace can limit aggregate:

```text
CPU
memory
Pods
PVCs
Services
object counts
```

# Part 251 — Right-Sizing

Start from observed:

```text
p50
p95
peak
startup
failure behavior
```

Too-low requests cause poor scheduling; too-high waste capacity.

# Part 252 — Requests Drive Scheduling

Scheduler compares Pod requests to Node allocatable resources.

It does not schedule based only on live current CPU/memory usage.

# Part 253 — Limits Are Not Reservations

A memory/CPU limit is not the same as guaranteed physical reservation.

Requests are key to placement.

# Part 254 — Overcommit

If requests are lower than limits, cluster can overcommit.

Good for utilization, but node pressure becomes possible when many Pods burst simultaneously.

# Part 255 — Node Pressure

Kubelet may report:

```text
MemoryPressure
DiskPressure
PIDPressure
```

and evict Pods according to policies/priorities.

# Part 256 — Ephemeral Storage

Pods also consume node-local ephemeral storage through:

```text
writable layers
emptyDir
logs
```

Requests/limits can be configured.

# Part 257 — emptyDir

Temporary volume exists for Pod lifetime.

```text
Pod deleted
→ emptyDir data deleted
```

Containers in same Pod can share it.

# Part 258 — emptyDir Memory

`emptyDir` can use memory-backed storage.

Counts against memory behavior and should be sized carefully.

# Part 259 — Configuration and Resource Debugging

If app starts but fails:

```text
env/config
secret key
mount path
probe
CPU throttle
memory OOM
ephemeral disk
```

are common causes.

# Part 260 — Operational Contract

A good Pod definition tells platform:

```text
what to run
what it needs
how much it needs
when it is healthy
how to stop it
which identity it uses
```

# Part 261 — Basic Scheduling

Scheduler filters and scores Nodes.

Simple placement controls:

```text
nodeSelector
node affinity
taints/tolerations
resource requests
```

# Part 262 — nodeSelector

```yaml
nodeSelector:
  disktype: ssd
```

Pod runs only on Nodes with matching label.

# Part 263 — Node Labels

```bash
kubectl label node worker1 disktype=ssd
```

Avoid trusting unprotected labels for high-security placement unless label is protected by node restriction mechanisms.

# Part 264 — Node Affinity

More expressive than `nodeSelector`.

Can express:

```text
required
preferred
In
NotIn
Exists
```

# Part 265 — Pod Affinity

Place Pods near matching Pods.

Example:

```text
frontend near cache
```

Can increase scheduling complexity.

# Part 266 — Pod Anti-Affinity

Spread replicas apart.

Example:

```text
do not place two critical replicas on same Node
```

# Part 267 — Taint

Taint repels Pods unless they tolerate it.

```text
node role/special hardware/dedicated workloads
```

# Part 268 — Toleration

Toleration allows Pod to schedule/remain on tainted Node but does not guarantee placement there.

# Part 269 — Topology Spread Constraints

Spread replicas across:

```text
zones
nodes
racks
```

using topology domains.

Often more flexible than strict anti-affinity.

# Part 270 — PersistentVolume

PV represents cluster storage resource.

It is cluster-scoped and has lifecycle independent from a particular Pod.

# Part 271 — PersistentVolumeClaim

PVC is a namespaced request for storage.

```text
Pod
 ↓
PVC
 ↓
PV
```

# Part 272 — StorageClass

Describes storage provisioning class.

Examples:

```text
fast SSD
standard disk
NFS-backed
cloud block
```

# Part 273 — Dynamic Provisioning

PVC requests storage and StorageClass/CSI provisioner creates volume automatically.

This is standard production pattern.

# Part 274 — Access Modes

Common:

```text
ReadWriteOnce
ReadOnlyMany
ReadWriteMany
ReadWriteOncePod
```

Actual support depends on storage driver.

# Part 275 — Reclaim Policy

PV/storage can use:

```text
Retain
Delete
```

depending on class/volume.

Understand before deleting PVC.

# Part 276 — Volume Binding Mode

StorageClass can delay binding until Pod scheduling so volume is created in compatible topology/zone.

Important for zonal block storage.

# Part 277 — CSI

CSI driver handles:

```text
provision
attach
mount
resize
snapshot integrations
```

depending on driver/features.

# Part 278 — ServiceAccount

Kubernetes workload identity object.

Default ServiceAccount exists in namespace, but production apps should often have dedicated identity.

# Part 279 — RBAC

Role-based access control uses:

```text
Role / ClusterRole
RoleBinding / ClusterRoleBinding
```

to grant API permissions.

# Part 280 — Role

Namespaced permission set.

Example:

```text
get/list/watch ConfigMaps in namespace
```

# Part 281 — ClusterRole

Can contain permissions for cluster-scoped resources or reusable namespaced permissions.

# Part 282 — RoleBinding

Binds a Role or ClusterRole to subjects within a namespace.

# Part 283 — ClusterRoleBinding

Grants ClusterRole at cluster scope.

Use very carefully.

# Part 284 — can-i

Check authorization:

```bash
kubectl auth can-i get pods
kubectl auth can-i delete secrets -n prod
```

# Part 285 — SecurityContext

Example:

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
```

Container-level settings can drop capabilities/read-only root.

# Part 286 — Pod Security Standards

Kubernetes defines security profiles conceptually:

```text
Privileged
Baseline
Restricted
```

Pod Security Admission can enforce namespace policy in current clusters.

# Part 287 — Horizontal Pod Autoscaler

HPA changes replicas based on metrics.

```text
CPU high
→ increase replicas
```

Requires appropriate metrics pipeline and resource requests for common CPU behavior.

# Part 288 — HPA Is Not Instant

Autoscaling has:

```text
metric collection delay
control loop interval
Pod startup time
```

Applications must survive bursts using capacity, queues, or other designs.

# Part 289 — Vertical Pod Autoscaler Concept

VPA recommends/adjusts requests in supporting environments.

It is not core controller installed in every cluster by default.

# Part 290 — Metrics Server

Common lightweight metrics source enabling:

```bash
kubectl top nodes
kubectl top pods
```

and HPA resource metrics.

It is an add-on, not core durable monitoring system.

# Part 291 — kubectl top

```bash
kubectl top pods
kubectl top nodes
```

Useful for quick resource view, not full observability.

# Part 292 — Helm

Helm packages Kubernetes manifests into charts.

Concept:

```text
Chart templates
+
values
 ↓
rendered Kubernetes objects
```

# Part 293 — Helm Values

Parameterize:

```text
image
replicas
resources
ingress
configuration
```

without copying YAML per environment.

# Part 294 — Helm Release

Installing chart creates a release with revision history.

Helm manages rendered Kubernetes resources and release metadata.

# Part 295 — Kustomize

Kustomize transforms base YAML without templates.

```text
base
+
overlay dev
+
overlay prod
```

`kubectl` includes Kustomize support.

# Part 296 — kubectl apply -k

```bash
kubectl apply -k overlays/dev
```

renders/applies Kustomization.

# Part 297 — Helm vs Kustomize

```text
Helm:
package + template + release manager

Kustomize:
patch/overlay native YAML
```

Many teams use both in different layers.

# Part 298 — Fundamental Troubleshooting Method

Start from desired object and walk down:

```text
Deployment
 ↓ ReplicaSet
Pods
 ↓
Container
 ↓
Service endpoint
 ↓
Network/DNS
 ↓
Dependency
```

Use status/events/logs at every layer.

# Part 299 — Kubernetes Fundamentals Architecture

A healthy application typically combines:

```text
Deployment/StatefulSet
Service
ConfigMap/Secret
probes
resource requests/limits
ServiceAccount/RBAC
NetworkPolicy
PVC if stateful
Ingress/Gateway if exposed
```

# Part 300 — Kubernetes Fundamentals Final Mental Model

Kubernetes is a **declarative distributed control system**.

You do not manage individual containers as pets.

You define objects, and controllers continuously reconcile the cluster toward desired state while networking, storage, identity, policy, and scheduling provide the operating platform.

---

# Supplemental Deep-Study Layer — Kubernetes Fundamentals

> **Source distinction:** The complete uploaded Course 59 remains preserved in this enhanced file. The material below expands the original with deeper API-object behavior, controller evidence, workload lifecycle, rollout engineering, Service/EndpointSlice/DNS behavior, NetworkPolicy, storage, identity, security, autoscaling, packaging, GitOps concepts, resilience patterns, and structured troubleshooting. Version-specific Kubernetes/Gateway API/CKA statements in the original source remain source-derived and should be checked against live upstream documentation when exact release behavior matters.

Preferred study flow:

```text
Concept
  ↓
Detailed explanation
  ↓
Kubernetes mental model
  ↓
kubectl / YAML / code
  ↓
Expected evidence
  ↓
Why it works
  ↓
Production use
  ↓
Troubleshooting
  ↓
Best practice
```


## Advanced Deep Dive 1 — API Object Lifecycle

### Concept

Kubernetes objects move through API validation, persistence, watch delivery, reconciliation, and garbage collection. Understanding the lifecycle explains why a successful `kubectl apply` does not guarantee a healthy workload.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl apply -f app.yaml
kubectl get deploy api -o yaml
kubectl get rs,pods -l app=api
kubectl get events --sort-by=.metadata.creationTimestamp
```

### Expected Evidence

The API object exists, controllers create dependents, and events explain downstream failures.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Verify both API acceptance and reconciled runtime state.

---

## Advanced Deep Dive 2 — Desired State vs Observed State

### Concept

Most resources expose desired intent in `.spec` and controller-reported reality in `.status`. Operational decisions should compare the two instead of reading only one.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get deployment api -o jsonpath='{.spec.replicas}{" desired / "}{.status.availableReplicas}{" available\n"}'
```

### Expected Evidence

Desired replicas and observed availability can be compared directly.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Treat status conditions as controller evidence, not decorative metadata.

---

## Advanced Deep Dive 3 — Generation and ObservedGeneration

### Concept

Controllers can report which generation they have processed. A spec update can be newer than the status a controller has reconciled.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get deployment api -o jsonpath='{.metadata.generation}{" spec generation / "}{.status.observedGeneration}{" observed\n"}'
```

### Expected Evidence

When equal, status normally reflects the latest spec generation.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use generation checks when debugging slow or stuck controllers.

---

## Advanced Deep Dive 4 — resourceVersion and Optimistic Concurrency

### Concept

`resourceVersion` identifies the API object's current storage/watch version and helps prevent lost updates. It is not a user-facing semantic version.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get configmap app-config -o jsonpath='{.metadata.resourceVersion}{"\n"}'
```

### Expected Evidence

The resource version changes as the object is modified.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Do not build business logic around numeric ordering of resourceVersion.

---

## Advanced Deep Dive 5 — Finalizers

### Concept

A finalizer keeps an object in terminating state until cleanup logic completes. Stuck deletion often means the responsible controller cannot finish cleanup.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pvc data -o yaml | sed -n '/finalizers:/,/spec:/p'
```

### Expected Evidence

Finalizer names and deletionTimestamp reveal why the object still exists.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Investigate the controller and dependent infrastructure before manually removing finalizers.

---

## Advanced Deep Dive 6 — Owner References

### Concept

Owner references let garbage collection and controllers model dependency relationships. Workload troubleshooting should identify the top-level owner instead of treating each Pod as independent.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pod <POD> -o jsonpath='{.metadata.ownerReferences}'
```

### Expected Evidence

The Pod points to its ReplicaSet or another controller owner.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Operate the highest-level controller that expresses intent.

---

## Advanced Deep Dive 7 — Server-Side Apply Field Ownership

### Concept

Server-Side Apply tracks which manager owns which fields. Conflicts appear when multiple tools attempt to own the same field.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get deployment api -o yaml | sed -n '/managedFields:/,$p' | head -80
```

### Expected Evidence

Managed fields show different field managers and operations.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Give each automation system clear field ownership.

---

## Advanced Deep Dive 8 — kubectl Diff as Change Review

### Concept

`kubectl diff` compares desired manifests with live objects before mutation, reducing accidental production changes.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl diff -f manifests/
```

### Expected Evidence

Pending additions, deletions, and modifications are visible before apply.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use diff plus context/namespace verification before production writes.

---

## Advanced Deep Dive 9 — Server Dry-Run

### Concept

Client dry-run only validates local generation; server dry-run also exercises API validation/admission without persistence.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl apply --server-side --dry-run=server -f app.yaml
```

### Expected Evidence

The request is validated by the API server without creating the object.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use server dry-run when admission policy matters.

---

## Advanced Deep Dive 10 — kubectl Explain as Schema Discovery

### Concept

`kubectl explain` provides live schema documentation matching cluster API discovery, reducing stale YAML guessing.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl explain deployment.spec.strategy
kubectl explain pod.spec.securityContext
```

### Expected Evidence

Fields, types, and descriptions match the connected cluster.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Prefer schema discovery over copying old manifests from blogs.

---

## Advanced Deep Dive 11 — Namespace Boundary

### Concept

Namespaces organize namespaced resources and become scopes for RBAC, quotas, policies, and tenancy controls, but they do not automatically isolate network, nodes, or kernel resources.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl api-resources --namespaced=true
kubectl api-resources --namespaced=false
```

### Expected Evidence

Namespaced and cluster-scoped resources are clearly distinguished.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Combine namespaces with RBAC, quotas, Pod security, and network policy.

---

## Advanced Deep Dive 12 — Labels as Control Inputs

### Concept

Labels are not merely metadata; selectors drive Services, Deployments, NetworkPolicies, scheduling, and automation. A label change can alter traffic or ownership behavior.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pods --show-labels
kubectl get pods -l 'app=api,env=prod'
```

### Expected Evidence

Selector membership can be inspected before changing labels.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Treat selector-driving labels as API contract.

---

## Advanced Deep Dive 13 — Recommended Label Taxonomy

### Concept

Stable label conventions make queries, ownership, policy, and observability predictable across teams.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
metadata:
  labels:
    app.kubernetes.io/name: orders
    app.kubernetes.io/component: api
    app.kubernetes.io/part-of: commerce
    app.kubernetes.io/version: "1.8.4"
```

### Expected Evidence

Objects share consistent machine-readable dimensions.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Standardize labels centrally and avoid ad hoc synonyms.

---

## Advanced Deep Dive 14 — Annotations for Non-Selector Metadata

### Concept

Annotations can store owner references, checksums, documentation links, or integration hints without affecting selector membership.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl annotate deployment api owner=platform-team change-ticket=CHG-123
```

### Expected Evidence

Metadata is attached without changing workload selection.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Keep large/unstructured data out of labels when it is not used for selection.

---

## Advanced Deep Dive 15 — Pod Sandbox Mental Model

### Concept

A Pod is a schedulable group sharing network identity and selected namespaces/volumes. The runtime creates a sandbox before application containers start.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
Pod
  ├─ shared network namespace
  ├─ shared Pod IP
  ├─ shared volumes
  ├─ app container
  └─ helper container
```

### Expected Evidence

Containers in one Pod can communicate over localhost and share mounted volumes.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use one Pod only for tightly coupled lifecycle/network requirements.

---

## Advanced Deep Dive 16 — Pod Conditions

### Concept

Pod phase is coarse. Conditions such as PodScheduled, Initialized, ContainersReady, and Ready reveal where lifecycle progression stopped.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pod <POD> -o jsonpath='{range .status.conditions[*]}{.type}={.status}{" reason="}{.reason}{"\n"}{end}'
```

### Expected Evidence

The exact condition blocking readiness is visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use conditions before assuming `Running` means healthy.

---

## Advanced Deep Dive 17 — Container State and LastState

### Concept

Each container has current state and previous termination state. Crash loops often require looking at `lastState.terminated` for reason, exit code, and timestamps.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pod <POD> -o jsonpath='{range .status.containerStatuses[*]}{.name}{" restart="}{.restartCount}{" last="}{.lastState.terminated.reason}{" exit="}{.lastState.terminated.exitCode}{"\n"}{end}'
```

### Expected Evidence

Restart count and previous termination reason are shown per container.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Correlate lastState with `kubectl logs --previous`.

---

## Advanced Deep Dive 18 — Image Digest Runtime Evidence

### Concept

Tags can move. The actual pulled image identity is exposed as an imageID/digest in container status.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pod <POD> -o jsonpath='{range .status.containerStatuses[*]}{.name}{" "}{.imageID}{"\n"}{end}'
```

### Expected Evidence

The running artifact can be tied to an immutable digest.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Record imageID during incidents and deployments.

---

## Advanced Deep Dive 19 — Init Container Contract

### Concept

Init containers run sequentially before ordinary app containers. They should be bounded, deterministic, and idempotent.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pod <POD> -o jsonpath='{range .status.initContainerStatuses[*]}{.name}{" "}{.state}{"\n"}{end}'
```

### Expected Evidence

Initialization state reveals which step is blocking app startup.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Avoid embedding long-running business workflows in init containers.

---

## Advanced Deep Dive 20 — Native Sidecar Semantics

### Concept

Modern Kubernetes supports restartable init-container semantics for native sidecars, providing explicit startup/termination ordering with main containers.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
initContainers:
  - name: proxy
    image: example/proxy:1.0
    restartPolicy: Always
```

### Expected Evidence

The helper starts as an init-style sidecar and remains running with app containers where supported by the cluster version.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use sidecars only when tight Pod-level lifecycle coupling is needed.

---

## Advanced Deep Dive 21 — Ephemeral Debug Container

### Concept

Ephemeral containers let operators add a debug toolset to an existing Pod without rebuilding the production image.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl debug pod/<POD> -it --image=busybox --target=<CONTAINER>
```

### Expected Evidence

A temporary debug container joins selected namespaces for investigation.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use ephemeral debugging instead of shipping shells/tools in every production image.

---

## Advanced Deep Dive 22 — Termination Grace Sequence

### Concept

Pod termination coordinates endpoint removal, preStop, SIGTERM, grace period, and final SIGKILL if the process does not exit.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
deletion requested
  ↓ endpoint/readiness removal
  ↓ preStop (if any)
  ↓ SIGTERM
  ↓ grace period
  ↓ SIGKILL if still running
```

### Expected Evidence

Application logs show graceful drain before process exit.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Set terminationGracePeriodSeconds from measured drain requirements.

---

## Advanced Deep Dive 23 — preStop Timing

### Concept

The preStop hook consumes the same termination grace period as application shutdown; long hooks can leave no time for the app to drain.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
lifecycle:
  preStop:
    exec:
      command: ["sh","-c","sleep 5"]
terminationGracePeriodSeconds: 30
```

### Expected Evidence

Hook duration and application shutdown fit within the total grace budget.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Prefer the application to handle SIGTERM directly when possible.

---

## Advanced Deep Dive 24 — Liveness Scope

### Concept

Liveness should answer whether the local process is irrecoverably stuck. Tying it to remote dependencies can create restart storms.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
DB outage
  ↓ bad liveness checks DB
many Pods restart
  ↓ reconnect storm
incident worsens
```

### Expected Evidence

The probe does not restart healthy processes merely because a remote dependency is unavailable.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Keep liveness local and conservative.

---

## Advanced Deep Dive 25 — Readiness Scope

### Concept

Readiness controls traffic eligibility. It can depend on required downstream services when the instance truly cannot serve without them.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
process running
DB unavailable
  ↓ readiness false
Service removes endpoint
```

### Expected Evidence

The Pod remains alive but stops receiving new Service traffic.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use readiness to protect users from partially initialized or dependency-broken instances.

---

## Advanced Deep Dive 26 — Startup Probe

### Concept

Startup probes prevent liveness from killing slow-start applications before initialization completes.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
startupProbe:
  httpGet:
    path: /health/startup
    port: 8080
  periodSeconds: 5
  failureThreshold: 24
```

### Expected Evidence

The application receives a bounded startup window before liveness begins.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use startup probes instead of extreme liveness initial delays for slow apps.

---

## Advanced Deep Dive 27 — Probe Budget Math

### Concept

Probe failure time is approximately period × failureThreshold plus timeout/processing effects. Operators should calculate it deliberately.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```python
period = 5
failure_threshold = 6
print("Approx failure detection seconds:", period * failure_threshold)
```

### Expected Evidence

The effective detection window is explicit.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Tune probes from failure-detection and recovery objectives.

---

## Advanced Deep Dive 28 — Deployment Rollout Capacity

### Concept

Rolling updates consume temporary capacity according to replicas, maxSurge, maxUnavailable, startup time, and readiness behavior.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
replicas=10
maxSurge=2
maxUnavailable=1
→ up to 12 Pods
→ at least 9 desired available during rollout
```

### Expected Evidence

The cluster has enough headroom for the configured overlap.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Capacity-plan rollout surge before production deployment.

---

## Advanced Deep Dive 29 — Deployment Availability Condition

### Concept

Deployment availability reflects minimum ready replicas after readiness and minReadySeconds. A rollout can be Running while not Available.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get deploy api
kubectl describe deploy api
```

### Expected Evidence

Available/Progressing conditions explain rollout state.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Watch controller conditions, not only Pod phase.

---

## Advanced Deep Dive 30 — ProgressDeadlineSeconds

### Concept

A Deployment can report ProgressDeadlineExceeded when rollout does not make progress. Kubernetes does not inherently perform an application-safe rollback for every failure.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get deploy api -o jsonpath='{range .status.conditions[*]}{.type}{" "}{.reason}{" "}{.message}{"\n"}{end}'
```

### Expected Evidence

The controller identifies stalled rollout progress.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Connect rollout failure to explicit rollback automation/runbooks.

---

## Advanced Deep Dive 31 — Revision History and Rollback

### Concept

Deployment revisions preserve previous ReplicaSet templates, but rollback safety also depends on database/schema/config compatibility.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl rollout history deploy/api
kubectl rollout undo deploy/api --to-revision=<N>
```

### Expected Evidence

The workload template can revert to a known prior revision.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Pair application rollback with expand/contract schema practices.

---

## Advanced Deep Dive 32 — Recreate Strategy

### Concept

Recreate eliminates overlap between versions but introduces downtime and should be reserved for workloads that cannot coexist safely.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
strategy:
  type: Recreate
```

### Expected Evidence

Old Pods terminate before new Pods are started.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Choose Recreate only from an explicit exclusivity requirement.

---

## Advanced Deep Dive 33 — StatefulSet Identity

### Concept

StatefulSet Pods receive stable ordinal identity and can retain per-replica storage. This solves identity/lifecycle mechanics, not database replication logic.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pods -l app=db
kubectl get pvc
```

### Expected Evidence

Stable Pod names and PVC names map predictably by ordinal.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use an operator/application protocol for database HA, not StatefulSet alone.

---

## Advanced Deep Dive 34 — StatefulSet Ordered vs Parallel Management

### Concept

StatefulSets can use ordered or parallel Pod management behavior depending on workload needs.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
podManagementPolicy: Parallel
```

### Expected Evidence

Pod creation/deletion ordering matches the chosen policy.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use ordered behavior only when the application genuinely depends on ordinal sequencing.

---

## Advanced Deep Dive 35 — Headless Service Discovery

### Concept

A headless Service returns backend endpoint records rather than a single virtual ClusterIP, allowing direct replica discovery.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get svc db-headless -o yaml
kubectl get endpointslices -l kubernetes.io/service-name=db-headless
```

### Expected Evidence

EndpointSlice records represent individual StatefulSet Pod endpoints.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use headless Services when clients need direct replica identity.

---

## Advanced Deep Dive 36 — Job Completion Semantics

### Concept

Jobs track successful completions and retries. Batch design must distinguish retryable infrastructure failure from non-idempotent business side effects.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get jobs
kubectl describe job <JOB>
```

### Expected Evidence

Completions, failures, and retry behavior are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Make Job actions idempotent or checkpointed before allowing retries.

---

## Advanced Deep Dive 37 — Indexed Jobs

### Concept

Indexed Jobs assign stable completion indexes, useful for sharded batch work where each Pod processes a distinct partition.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
completion index 0 → shard 0
completion index 1 → shard 1
...
```

### Expected Evidence

Each Pod can derive its work partition from the completion index.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use indexed Jobs for deterministic partitioned batch workloads.

---

## Advanced Deep Dive 38 — CronJob Missed/Overlapping Runs

### Concept

CronJobs may face controller downtime, long execution, or overlapping runs. concurrencyPolicy and startingDeadlineSeconds should match business semantics.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
concurrencyPolicy: Forbid
startingDeadlineSeconds: 300
```

### Expected Evidence

A late or overlapping schedule behaves according to an explicit policy.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Design CronJobs for duplicate/missed execution scenarios.

---

## Advanced Deep Dive 39 — DaemonSet Node Agent Blast Radius

### Concept

A DaemonSet can deploy one Pod to many or all nodes. A bad image or configuration can therefore impact the whole cluster quickly.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl rollout status daemonset/<DS> -n kube-system
```

### Expected Evidence

Node-agent rollout progress is visible cluster-wide.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Canary infrastructure DaemonSet changes before broad rollout.

---

## Advanced Deep Dive 40 — Service Virtual IP

### Concept

ClusterIP is a virtual Service identity implemented by the Service data plane; no ordinary process needs to bind the Service IP directly.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get svc api -o wide
kubectl get endpointslices -l kubernetes.io/service-name=api
```

### Expected Evidence

Service VIP and backend endpoints are distinct.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Debug Service data plane separately from the application listener.

---

## Advanced Deep Dive 41 — EndpointSlice Readiness

### Concept

EndpointSlices contain endpoint conditions such as ready/serving/terminating. Readiness changes directly influence Service traffic.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get endpointslices -l kubernetes.io/service-name=api -o yaml
```

### Expected Evidence

Backend addresses and readiness conditions are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

When a Service has no traffic, inspect EndpointSlices before DNS.

---

## Advanced Deep Dive 42 — Named Ports

### Concept

Named container/Service ports reduce duplicated numeric configuration and allow probes/services to reference a logical port name.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
ports:
  - name: http
    containerPort: 8080
```

### Expected Evidence

Service targetPort can reference `http` instead of repeating 8080.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use stable named ports for application protocols.

---

## Advanced Deep Dive 43 — ClusterIP vs NodePort vs LoadBalancer

### Concept

Service types represent different exposure layers: cluster-only VIP, node-wide port, and external/internal load balancer integration.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
ClusterIP    → inside cluster
NodePort     → node IP:port
LoadBalancer → external/internal LB + Service
```

### Expected Evidence

The exposure level is explicit.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use the narrowest exposure type that meets the requirement.

---

## Advanced Deep Dive 44 — ExternalName Limitations

### Concept

ExternalName creates DNS indirection to another hostname; it does not proxy traffic, create health checks, or rewrite application-layer hostnames.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
type: ExternalName
externalName: database.example.internal
```

### Expected Evidence

DNS resolves the Service name to the external target.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use ExternalName only when DNS indirection matches protocol expectations.

---

## Advanced Deep Dive 45 — Service Session Affinity

### Concept

ClientIP session affinity can retain client-to-backend stickiness but may produce uneven load and should not replace correct stateless session design.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
sessionAffinity: ClientIP
```

### Expected Evidence

Repeat requests from one client tend toward the same backend while affinity is active.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Externalize session state instead of depending on stickiness whenever possible.

---

## Advanced Deep Dive 46 — CoreDNS Search Path

### Concept

Pod resolv.conf normally includes namespace/service search domains, enabling short names such as `api` to resolve within the current namespace.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl exec <POD> -- cat /etc/resolv.conf
```

### Expected Evidence

nameserver, search, and options reveal cluster DNS behavior.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use FQDN or namespace-qualified names when cross-namespace ambiguity matters.

---

## Advanced Deep Dive 47 — DNS ndots Behavior

### Concept

Resolver `ndots` can cause multiple search-domain queries before an external name is attempted, affecting latency for dotted names.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl exec <POD> -- cat /etc/resolv.conf
```

### Expected Evidence

The `options ndots:` value can be inspected.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Measure DNS behavior before changing cluster-wide resolver settings.

---

## Advanced Deep Dive 48 — Service Selector Failure

### Concept

A Service with a selector but no matching Ready Pods produces no useful ready endpoints.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get svc api -o jsonpath='{.spec.selector}'
kubectl get pods --show-labels
kubectl get endpointslices -l kubernetes.io/service-name=api
```

### Expected Evidence

The selector/label mismatch is visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Debug selector → Pod label → readiness in that order.

---

## Advanced Deep Dive 49 — Ingress Controller Dependency

### Concept

Ingress resources are configuration objects; a compatible Ingress controller must actually implement packet handling.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get ingressclass
kubectl get ingress -A
```

### Expected Evidence

The cluster has a controller/class capable of processing the resource.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Do not expect Ingress YAML alone to expose traffic.

---

## Advanced Deep Dive 50 — Gateway API Role Separation

### Concept

Gateway API separates infrastructure ownership from route ownership so platform teams can manage listeners while app teams attach Routes.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
platform team:
GatewayClass + Gateway

application team:
HTTPRoute / GRPCRoute
```

### Expected Evidence

Route attachment status shows whether policy/listeners accept the route.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use role separation to reduce shared ingress configuration conflicts.

---

## Advanced Deep Dive 51 — Gateway Route Status

### Concept

Gateway API resources expose status conditions explaining whether a Route was accepted and whether backend references resolved.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get httproute <ROUTE> -o yaml
```

### Expected Evidence

Accepted/ResolvedRefs-style conditions explain attachment problems.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Read status conditions before changing listener or backend configuration.

---

## Advanced Deep Dive 52 — NetworkPolicy Default Deny

### Concept

A default-deny policy changes the namespace from implicit connectivity to explicit allow-listing when the CNI enforces NetworkPolicy.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Expected Evidence

Selected Pods become isolated except for separately allowed flows.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Add DNS and required service egress before enabling deny-all in production.

---

## Advanced Deep Dive 53 — NetworkPolicy DNS Allow

### Concept

Egress-restricted Pods often need explicit access to cluster DNS; forgetting UDP/TCP 53 is a common self-inflicted outage.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
app Pod
  ↓ DNS UDP/TCP 53
CoreDNS Service/Pods
```

### Expected Evidence

Name resolution succeeds while other unauthorized egress remains blocked.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Treat DNS as an explicit dependency in default-deny designs.

---

## Advanced Deep Dive 54 — NetworkPolicy Namespace Selectors

### Concept

Cross-namespace policy depends on namespace labels. Security-sensitive namespace labels must be governed because changing them can alter access.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get ns --show-labels
```

### Expected Evidence

Namespace labels used by policies are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Protect security-significant namespace labels through governance/admission.

---

## Advanced Deep Dive 55 — ConfigMap Env vs Volume Update

### Concept

Environment variables are fixed at process start; mounted ConfigMap projections may update eventually, but applications must reload or restart to consume them.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get configmap app-config -o yaml
kubectl exec <POD> -- env | grep APP_
```

### Expected Evidence

The live process environment can differ from the latest ConfigMap object.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use explicit rollout/reload strategy for configuration changes.

---

## Advanced Deep Dive 56 — Secret Encoding vs Encryption

### Concept

Kubernetes Secret data is base64-encoded in API representation; confidentiality depends on RBAC, etcd encryption, transport security, and workflow.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get secret demo -o jsonpath='{.data.password}' | base64 -d; echo
```

### Expected Evidence

Anyone with Secret read permission can recover the value.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Treat Secret read permission as access to plaintext secret material.

---

## Advanced Deep Dive 57 — Projected ServiceAccount Tokens

### Concept

Modern ServiceAccount token projection provides short-lived, audience-bound credentials rather than relying on indefinitely valid Secret tokens.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl create token <SERVICEACCOUNT> --duration=10m
```

### Expected Evidence

A short-lived token is issued for the workload identity.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Disable token automount for workloads that do not call the Kubernetes API.

---

## Advanced Deep Dive 58 — Resource Requests as Scheduling Contract

### Concept

Scheduler uses resource requests, not instantaneous utilization, when determining whether a Pod fits a node.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe node <NODE> | sed -n '/Allocated resources:/,$p' | head -30
```

### Expected Evidence

Requested CPU/memory allocations are visible independently of current usage.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Right-size requests from measured workload demand.

---

## Advanced Deep Dive 59 — CPU Limit Throttling

### Concept

CPU limits enforce cgroup quota and can cause latency even when the node has spare CPU.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl top pod <POD>
kubectl get pod <POD> -o jsonpath='{.spec.containers[*].resources}'
```

### Expected Evidence

Configured limits and current usage can be compared.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Investigate throttling before assuming the application needs more replicas.

---

## Advanced Deep Dive 60 — Memory Limit OOM

### Concept

Memory limit is a hard boundary; exceeding it can cause OOMKill and restart while the Pod may remain scheduled on the same node.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe pod <POD> | grep -A5 -E 'Last State|OOMKilled'
```

### Expected Evidence

Termination reason indicates OOMKilled when applicable.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Size memory for startup, steady state, and peak behavior.

---

## Advanced Deep Dive 61 — QoS Classes

### Concept

Guaranteed, Burstable, and BestEffort reflect request/limit configuration and influence eviction behavior under node pressure.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pod <POD> -o jsonpath='{.status.qosClass}{"\n"}'
```

### Expected Evidence

The Pod's QoS class is explicit.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Avoid accidental BestEffort for important workloads.

---

## Advanced Deep Dive 62 — Ephemeral Storage Requests

### Concept

Writable layers, logs, and emptyDir consume node-local ephemeral storage. Requests/limits help prevent one Pod from filling the node.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
resources:
  requests:
    ephemeral-storage: 500Mi
  limits:
    ephemeral-storage: 2Gi
```

### Expected Evidence

Pod resource policy includes local storage consumption.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Treat node disk as a schedulable/limited resource.

---

## Advanced Deep Dive 63 — emptyDir Medium Memory

### Concept

Memory-backed emptyDir stores data in tmpfs and consumes memory; it can be fast but increases memory pressure.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
volumes:
  - name: scratch
    emptyDir:
      medium: Memory
      sizeLimit: 256Mi
```

### Expected Evidence

The temporary volume is bounded and disappears with the Pod.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use memory-backed emptyDir only for bounded scratch data.

---

## Advanced Deep Dive 64 — NodeSelector Hard Constraint

### Concept

nodeSelector restricts placement to nodes carrying exact labels; missing labels create Pending Pods.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get nodes --show-labels
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Evidence

Scheduling events report unmatched node selectors.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use nodeSelector only for durable infrastructure capabilities.

---

## Advanced Deep Dive 65 — Node Affinity Required vs Preferred

### Concept

Required affinity is a hard scheduling rule; preferred affinity influences scoring but allows fallback.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
requiredDuringScheduling... → hard filter
preferredDuringScheduling... → scoring preference
```

### Expected Evidence

A workload can fall back only when the policy is preferred.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use preferences for performance/locality and hard rules for true constraints.

---

## Advanced Deep Dive 66 — Taints and Tolerations

### Concept

Taints repel workloads; tolerations permit scheduling but do not actively attract Pods to the node.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe node <NODE> | grep -i Taints
```

### Expected Evidence

The node's taints are visible alongside Pod tolerations.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Combine taints with affinity/selectors for dedicated-node placement.

---

## Advanced Deep Dive 67 — Topology Spread Constraints

### Concept

Topology spread distributes replicas across failure domains with a controlled skew, often providing better resilience than strict anti-affinity.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app: api
```

### Expected Evidence

Replicas are spread across nodes with bounded skew.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Design for node/zone failure capacity, not only normal balance.

---

## Advanced Deep Dive 68 — Pod Anti-Affinity Trade-Off

### Concept

Strict anti-affinity improves failure-domain spread but can make replacement Pods unschedulable during capacity loss.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
3 replicas
3 nodes
strict one-per-node
1 node fails
→ replacement needs a fourth eligible node
```

### Expected Evidence

The trade-off between resilience and schedulability is explicit.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Prefer topology spread unless strict separation is required.

---

## Advanced Deep Dive 69 — PVC Binding

### Concept

PVC binding depends on StorageClass, access mode, capacity, topology, and provisioner health. Pending PVCs often block Pod scheduling.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe pvc <PVC>
kubectl get storageclass
kubectl get pv
```

### Expected Evidence

PVC events identify provisioning or compatibility failures.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Troubleshoot PVC before changing the Pod when storage is unbound.

---

## Advanced Deep Dive 70 — WaitForFirstConsumer

### Concept

Delayed volume binding lets scheduling choose a node/zone before provisioning zonal storage, avoiding volumes created in unusable topology.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get storageclass <SC> -o jsonpath='{.volumeBindingMode}{"\n"}'
```

### Expected Evidence

The class reports WaitForFirstConsumer where configured.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use topology-aware binding for zonal block storage.

---

## Advanced Deep Dive 71 — Reclaim Policy

### Concept

Delete and Retain determine what happens to backing storage after PV/PVC lifecycle ends. This is a data-governance decision.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pv -o custom-columns=NAME:.metadata.name,RECLAIM:.spec.persistentVolumeReclaimPolicy,STATUS:.status.phase
```

### Expected Evidence

Each persistent volume's reclaim behavior is visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use Retain for data requiring deliberate recovery/cleanup.

---

## Advanced Deep Dive 72 — VolumeSnapshot Is Not Backup

### Concept

A CSI snapshot may live in the same storage/account/failure domain. Backups need independent retention, isolation, and restore testing.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
PVC
  ↓ snapshot
same storage domain
  ↓
backup copy
separate failure domain
```

### Expected Evidence

Recovery design distinguishes fast snapshot from durable backup.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Test restore paths rather than equating snapshot creation with backup.

---

## Advanced Deep Dive 73 — ServiceAccount Least Privilege

### Concept

Dedicated ServiceAccounts provide workload identity. Default ServiceAccount should not automatically receive broad API access.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl auth can-i get pods --as=system:serviceaccount:<NS>:<SA> -n <NS>
```

### Expected Evidence

The workload's effective API permission is verifiable.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Create one identity per application capability and grant only required verbs/resources.

---

## Advanced Deep Dive 74 — RoleBinding Scope

### Concept

A RoleBinding grants a Role or ClusterRole within one namespace; ClusterRoleBinding grants cluster-wide scope.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get rolebindings,clusterrolebindings -A
```

### Expected Evidence

Namespaced versus cluster-wide bindings are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Prefer RoleBinding when access only needs one namespace.

---

## Advanced Deep Dive 75 — kubectl auth can-i

### Concept

Authorization questions should be tested using exact identity, verb, resource, API group, namespace, and subresource.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl auth can-i create pods/exec   --as=system:serviceaccount:app:reader   -n app
```

### Expected Evidence

The API server returns an explicit yes/no authorization decision.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use can-i before changing RBAC.

---

## Advanced Deep Dive 76 — SecurityContext Restricted Baseline

### Concept

Ordinary workloads should run non-root, deny privilege escalation, drop capabilities, use RuntimeDefault seccomp, and make root filesystem read-only when possible.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: api
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
      readOnlyRootFilesystem: true
```

### Expected Evidence

The manifest expresses least privilege instead of relying on runtime defaults.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Start from restricted posture and add narrow exceptions.

---

## Advanced Deep Dive 77 — Pod Security Admission

### Concept

Namespace labels can enforce/warn/audit Pod Security Standards, creating a practical guardrail for multi-team clusters.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl label ns app   pod-security.kubernetes.io/enforce=restricted   --overwrite
```

### Expected Evidence

Non-compliant Pods are rejected in the protected namespace.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Roll out PSA with warn/audit before enforce in existing namespaces.

---

## Advanced Deep Dive 78 — HostPath Risk

### Concept

hostPath exposes node filesystem paths directly to a Pod and can bypass many isolation expectations.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pods -A -o json | jq -r '..|.hostPath? // empty' 2>/dev/null | head
```

### Expected Evidence

Host-mounted paths can be inventoried.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Avoid hostPath for ordinary apps and isolate infrastructure Pods that require it.

---

## Advanced Deep Dive 79 — hostNetwork and hostPID

### Concept

Sharing host network or PID namespaces reduces isolation and can expose node services/processes.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get pod <POD> -o jsonpath='{.spec.hostNetwork}{" hostNetwork "}{.spec.hostPID}{" hostPID\n"}'
```

### Expected Evidence

Host namespace sharing is explicitly visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Require a documented infrastructure use case for host namespace access.

---

## Advanced Deep Dive 80 — HPA Control Loop

### Concept

HPA adjusts replicas from observed metrics relative to target, but response includes metric delay, control-loop interval, Pod startup, and stabilization.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get hpa
kubectl describe hpa <HPA>
```

### Expected Evidence

Current metric, target, desired replicas, and scaling events are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Do not rely on HPA alone for sudden burst absorption.

---

## Advanced Deep Dive 81 — HPA + Requests

### Concept

CPU utilization-based HPA depends on CPU requests because utilization is measured relative to requested CPU.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
usage 200m
request 400m
→ 50% utilization
```

### Expected Evidence

Scaling targets can be interpreted correctly.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Define realistic requests before enabling CPU-based HPA.

---

## Advanced Deep Dive 82 — Queue-Length Autoscaling Concept

### Concept

Workers often scale better on backlog or event rate than CPU, because queue depth represents actual work waiting.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
queue depth
  ↓ metrics adapter/event scaler
HPA/controller
  ↓ worker replicas
```

### Expected Evidence

Replica count follows work backlog rather than incidental CPU.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Choose a scaling metric causally related to workload demand.

---

## Advanced Deep Dive 83 — Metrics Server Limits

### Concept

metrics-server provides short-term resource metrics for `kubectl top` and HPA but is not a historical observability platform.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl top nodes
kubectl top pods -A
```

### Expected Evidence

Current CPU/memory metrics are available.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use Prometheus/managed monitoring for durable metrics and SLOs.

---

## Advanced Deep Dive 84 — Events as Ephemeral Evidence

### Concept

Kubernetes Events are useful diagnostic breadcrumbs but have limited retention and are not a replacement for audit logs or centralized observability.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get events -A --sort-by=.metadata.creationTimestamp | tail -50
```

### Expected Evidence

Recent scheduling, probe, mount, and pull failures are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Forward important operational events if longer history is required.

---

## Advanced Deep Dive 85 — Structured Logs and Pod Identity

### Concept

Container logs should include service/version/correlation fields; the platform should enrich them with namespace, Pod, container, node, and image metadata.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```json
{"service":"orders","version":"1.8.4","request_id":"r-42","level":"ERROR","message":"db timeout"}
```

### Expected Evidence

Application and Kubernetes metadata can be correlated in a central log system.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use immutable image/version fields in logs for incident reconstruction.

---

## Advanced Deep Dive 86 — OpenTelemetry in Kubernetes

### Concept

OpenTelemetry collectors can receive traces, metrics, and logs from workloads and export to monitoring backends; deployment can use DaemonSet, gateway, or sidecar patterns.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
apps
  ↓ OTel SDK
collector agent/gateway
  ↓
trace/metric/log backends
```

### Expected Evidence

Application telemetry complements Kubernetes object/runtime metrics.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Instrument the application, not only the cluster.

---

## Advanced Deep Dive 87 — Helm Template vs Release State

### Concept

Helm renders templates from values and also maintains release history. Troubleshooting should inspect both rendered manifests and live Kubernetes resources.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
helm get values <RELEASE>
helm get manifest <RELEASE> | head -80
helm history <RELEASE>
```

### Expected Evidence

Release inputs, rendered output, and history are available.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Do not debug Helm values without inspecting the rendered manifest.

---

## Advanced Deep Dive 88 — Helm Values Schema

### Concept

Charts can define JSON schema for values validation, catching invalid configuration before resources reach the API.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
values.yaml
  ↓ values.schema.json validation
templates
  ↓ Kubernetes objects
```

### Expected Evidence

Invalid values fail early during Helm rendering/install.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use chart schemas for shared production charts.

---

## Advanced Deep Dive 89 — Kustomize Overlay Discipline

### Concept

Kustomize keeps a common base and applies patches/transformations for environments without duplicating full YAML.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
base/
overlays/dev/
overlays/prod/
```

### Expected Evidence

Rendered dev/prod manifests differ only where intended.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Keep overlays small and review `kubectl kustomize` output in CI.

---

## Advanced Deep Dive 90 — Immutable Image Promotion

### Concept

Production should deploy the same image digest tested in earlier environments rather than rebuilding per environment.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
build digest D
  ↓ dev test D
  ↓ staging test D
  ↓ prod deploy D
```

### Expected Evidence

All environments use the same artifact bytes.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Promote digests; change configuration separately.

---

## Advanced Deep Dive 91 — Config Rollout Checksum

### Concept

When a workload cannot reload mounted configuration automatically, a Pod-template checksum annotation can force a controlled rollout on config changes.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
metadata:
  annotations:
    checksum/config: "<rendered-config-hash>"
```

### Expected Evidence

Config changes alter Pod template and create a new rollout.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Make configuration update semantics explicit.

---

## Advanced Deep Dive 92 — GitOps Mental Model

### Concept

GitOps controllers continuously reconcile cluster state toward version-controlled desired manifests, extending the same Kubernetes reconciliation model to deployment operations.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
Git desired state
  ↓ GitOps controller
Kubernetes API
  ↓ controllers
runtime state
```

### Expected Evidence

Drift is visible and can be corrected by reconciliation.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Avoid manual changes that conflict with the authoritative Git owner.

---

## Advanced Deep Dive 93 — Admission Policy Preview

### Concept

Policy engines and built-in validating policy can reject manifests violating organizational rules such as privileged workloads, missing limits, or unapproved registries.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
kubectl apply
  ↓ authn/authz
admission policy
  ├─ allow
  └─ reject
```

### Expected Evidence

Unsafe configuration is blocked before persistence.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Convert repeatable review rules into admission policy.

---

## Advanced Deep Dive 94 — Application SLO

### Concept

Kubernetes health should be connected to user-facing SLOs such as availability and latency; a cluster can be green while users experience failure.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
SLI = successful valid requests / valid requests
SLO = 99.95% monthly
latency p95 < 500 ms
```

### Expected Evidence

Application dashboards show whether users receive the intended service.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use Kubernetes metrics for diagnosis and SLOs for outcome.

---

## Advanced Deep Dive 95 — PodDisruptionBudget Preview

### Concept

PDB limits voluntary disruptions so maintenance does not remove too many healthy replicas at once.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: api
```

### Expected Evidence

Node drain respects the disruption budget for matching Pods.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Set PDBs from real replica count and failure capacity.

---

## Advanced Deep Dive 96 — Graceful Degradation

### Concept

Applications should classify dependencies as critical or optional so readiness, retries, and fallbacks do not turn optional failures into full outages.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
critical DB down → readiness false
optional analytics down → continue core API with degraded feature
```

### Expected Evidence

The service retains useful behavior when noncritical dependencies fail.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Design dependency failure semantics before writing probes.

---

## Advanced Deep Dive 97 — Retry Backoff and Jitter

### Concept

Pod replacement and service discovery do not eliminate transient dependency failures. Clients should use bounded retries, exponential backoff, jitter, and idempotency.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```python
import random
for n in range(5):
    print(round(min(30, 2**n) + random.random(), 2))
```

### Expected Evidence

Retry intervals spread instead of synchronizing across replicas.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Retry only transient failures and cap total retry time.

---

## Advanced Deep Dive 98 — Circuit Breaker Concept

### Concept

If a dependency is persistently failing, failing fast can protect worker threads/connections and reduce cascading load.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
CLOSED → normal
failures rise
OPEN → fail fast/fallback
after cooldown
HALF-OPEN → test recovery
```

### Expected Evidence

The app stops flooding an unhealthy dependency.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use circuit breaking for remote dependencies where repeated calls amplify incidents.

---

## Advanced Deep Dive 99 — Bulkhead Isolation

### Concept

Separate worker pools, queues, database pools, or services keep one workload class from consuming all shared resources.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
interactive API pool
batch/report pool
notification pool
```

### Expected Evidence

Noncritical overload cannot starve critical paths.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Partition scarce resources by business criticality.

---

## Advanced Deep Dive 100 — Deployment Canary Concept

### Concept

A canary release exposes a small portion of traffic/users to a new version before broad rollout. Kubernetes needs an ingress/service mesh or multiple Services/Deployments to implement traffic splitting.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
stable v1 95%
canary v2 5%
  ↓ observe
promote or rollback
```

### Expected Evidence

The new version is evaluated against objective metrics before full promotion.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Define canary success/rollback criteria before rollout.

---

## Advanced Deep Dive 101 — Blue-Green Concept

### Concept

Blue-green keeps old and new environments running side by side and switches the Service/route when the new one is verified.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
Service selector
  ↓
blue v1

switch selector
  ↓
green v2
```

### Expected Evidence

Rollback can switch traffic back quickly if data/schema compatibility allows.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use immutable labels and tested switch/rollback procedure.

---

## Advanced Deep Dive 102 — Pod Priority Preview

### Concept

Priority affects scheduling/preemption and should be reserved for genuinely critical workloads and platform components.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get priorityclasses
```

### Expected Evidence

Available priority classes can be reviewed.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Do not mark ordinary apps system-critical.

---

## Advanced Deep Dive 103 — ResourceQuota Preview

### Concept

Namespaces can enforce aggregate CPU, memory, Pod, PVC, and object limits to control multi-team consumption.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get resourcequota -A
```

### Expected Evidence

Team-level resource ceilings are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use quota to prevent one namespace from exhausting shared cluster capacity.

---

## Advanced Deep Dive 104 — LimitRange Preview

### Concept

LimitRange can default or bound per-container requests/limits inside a namespace.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get limitrange -A
```

### Expected Evidence

Default/min/max resource policies are visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Use LimitRange to avoid accidental BestEffort workloads.

---

## Advanced Deep Dive 105 — Node Pressure Awareness

### Concept

Node conditions such as MemoryPressure, DiskPressure, and PIDPressure can cause evictions or scheduling avoidance even when individual Pods look healthy.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe node <NODE> | sed -n '/Conditions:/,/Addresses:/p'
```

### Expected Evidence

Pressure conditions show node-level resource health.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Troubleshoot the node when many unrelated Pods fail together.

---

## Advanced Deep Dive 106 — Service Account Token Exposure

### Concept

Mounting the Kubernetes API token into every Pod increases credential exposure. If the application never calls the API, disable automount.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```yaml
automountServiceAccountToken: false
```

### Expected Evidence

The Pod no longer receives an unnecessary API bearer token.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Remove unused credentials from workloads.

---

## Advanced Deep Dive 107 — ImagePullSecret vs Workload Identity

### Concept

Static registry Secrets work broadly, but cloud-native workload/node identity can reduce long-lived pull credentials where supported.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
static imagePullSecret
vs
node/workload identity → short-lived registry token
```

### Expected Evidence

Registry authentication is tied to managed identity rather than reusable passwords.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Prefer short-lived identity-based registry auth where available.

---

## Advanced Deep Dive 108 — Debugging Minimal Images

### Concept

Production images may lack shell/curl/dig. `kubectl debug`, temporary diagnostic Pods, and port-forwarding provide safer troubleshooting options.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl run net-debug --rm -it --image=nicolaka/netshoot -- bash
```

### Expected Evidence

A disposable diagnostic environment can test DNS/network without modifying production images.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Keep debug tooling ephemeral and access-controlled.

---

## Advanced Deep Dive 109 — Pod Pending Diagnostic Tree

### Concept

Pending normally means the Pod has not started. Events reveal whether the blocker is scheduling, PVC binding, image, or sandbox setup.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe pod <POD>
kubectl get events --field-selector involvedObject.name=<POD> --sort-by=.metadata.creationTimestamp
```

### Expected Evidence

Scheduler/storage/sandbox messages identify the blocked layer.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Read the event message literally before changing resources.

---

## Advanced Deep Dive 110 — CrashLoopBackOff Diagnostic Tree

### Concept

CrashLoopBackOff is a restart backoff symptom, not a root cause. Inspect current/previous logs, exit reason, probes, config, and OOM evidence.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl logs <POD> -c <CONTAINER> --previous
kubectl describe pod <POD>
```

### Expected Evidence

The previous container's actual failure reason is preserved.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Capture evidence before deleting the Pod.

---

## Advanced Deep Dive 111 — ImagePullBackOff Diagnostic Tree

### Concept

Image pull failures can come from name/tag, registry auth, DNS, TLS, proxy, architecture, or rate limits.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Evidence

Events include the runtime/registry error string.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Fix registry/reference cause rather than repeatedly deleting the Pod.

---

## Advanced Deep Dive 112 — Service No Endpoints Diagnostic Tree

### Concept

If DNS resolves but Service has no ready EndpointSlices, focus on selector, Pod labels, readiness, and namespace.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get svc <SVC> -o yaml
kubectl get endpointslices -l kubernetes.io/service-name=<SVC> -o wide
kubectl get pods --show-labels
```

### Expected Evidence

The backend selection failure is visible.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Debug endpoint production before kube-proxy/CNI.

---

## Advanced Deep Dive 113 — DNS Diagnostic Tree

### Concept

DNS failures can originate in the Pod resolver, kube-dns Service, CoreDNS endpoints, CoreDNS config, NetworkPolicy, or upstream DNS.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl run dns-debug --rm -it --image=busybox -- nslookup kubernetes.default
```

### Expected Evidence

The cluster-local resolver path can be tested independently.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Separate cluster-local DNS from external-upstream DNS.

---

## Advanced Deep Dive 114 — NetworkPolicy Diagnostic Tree

### Concept

A policy object has effect only when the CNI enforces it. Troubleshooting needs source Pod labels, destination labels, namespace labels, ports, policyTypes, and DNS egress.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl get networkpolicy -A
kubectl get pod <POD> --show-labels
```

### Expected Evidence

The exact policy selection can be reconstructed.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Test one allowed and one denied flow after every policy change.

---

## Advanced Deep Dive 115 — PVC Pending Diagnostic Tree

### Concept

PVC Pending usually means the storage request has not been provisioned/bound due to StorageClass, provisioner, topology, capacity, quota, or parameters.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl describe pvc <PVC>
kubectl get storageclass
```

### Expected Evidence

PVC events show the provisioning decision and error.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Start with the claim and provisioner before changing application YAML.

---

## Advanced Deep Dive 116 — RBAC Forbidden Diagnostic Tree

### Concept

A Forbidden response already proves authentication succeeded; investigate effective authorization instead of credentials.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl auth can-i <VERB> <RESOURCE>   --as=<SUBJECT> -n <NAMESPACE>
```

### Expected Evidence

The exact action is allowed or denied for the identity.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Do not grant cluster-admin to make a single verb work.

---

## Advanced Deep Dive 117 — Context Safety

### Concept

The same manifest applied to the wrong context or namespace can be a production incident. Context verification is an operational control.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```bash
kubectl config current-context
kubectl config view --minify
kubectl get ns
```

### Expected Evidence

Cluster, user, and default namespace are visible before writes.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Make context/namespace verification habitual before destructive operations.

---

## Advanced Deep Dive 118 — Evidence-First Troubleshooting

### Concept

A reliable sequence is: desired object, controller status, Pod/container state, Service/endpoints, DNS/network policy, storage/config, node/resource pressure, then external dependencies.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
Deployment/StatefulSet
  ↓ ReplicaSet/Pod
  ↓ container
  ↓ Service/EndpointSlice
  ↓ DNS/NetworkPolicy
  ↓ PVC/Config/Secret
  ↓ node/runtime
```

### Expected Evidence

The failing layer is isolated before remediation.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Change one layer at a time and preserve the evidence that justified it.

---

## Advanced Deep Dive 119 — Operational Readiness Review

### Concept

A production Kubernetes workload needs ownership, immutable image, resources, probes, graceful stop, RBAC, Pod security, network policy, storage recovery, telemetry, rollout, and rollback.

### Architecture / Mental Model

```text
Desired Kubernetes object
        ↓
API validation + persistence
        ↓
Controller / Scheduler / Kubelet
        ↓
Pod + Service + Storage + Policy
        ↓
Observed status + events + telemetry
```

### kubectl / YAML / Code

```text
[ ] owner/on-call
[ ] image digest
[ ] resources
[ ] startup/readiness/liveness
[ ] graceful termination
[ ] ServiceAccount/RBAC
[ ] restricted security context
[ ] NetworkPolicy
[ ] backup/restore
[ ] logs/metrics/traces
[ ] rollout/rollback
```

### Expected Evidence

The workload can be operated and recovered before launch.

### Why It Works

Kubernetes is a distributed declarative control system. The API stores intent, controllers reconcile dependent resources, the scheduler chooses placement, kubelet drives container runtime state, and networking/storage/policy components complete the data plane. A command succeeding at one layer does not prove the lower layers converged successfully.

### Production Example

For a production service, record the top-level controller, immutable image digest, Service/route, ServiceAccount, resource requests/limits, security context, probes, network policy, persistent-data strategy, configuration source, observability, and rollback method.

### Troubleshooting Workflow

```text
Verify context + namespace
   ↓
Inspect desired object
   ↓
Inspect status + conditions + events
   ↓
Walk ownership to Pod/container
   ↓
Check Service/EndpointSlice/DNS/policy
   ↓
Check config/secret/PVC
   ↓
Check node/resource pressure
   ↓
Make one controlled correction
   ↓
Verify user-facing behavior
```

### Common Mistakes

- Treating Pods as permanent servers.
- Reading only `Running` and ignoring readiness/conditions.
- Hardcoding Pod IPs.
- Using `localhost` for another Pod.
- Granting broad RBAC or privilege to solve narrow failures.
- Assuming a Secret is encrypted because it is base64.
- Deploying without resource requests, health semantics, or rollback.

### Best Practice

Make operational readiness a deployment gate.

---

# Supplemental Hands-on Lab Series — Kubernetes Fundamentals

## Enhanced Lab 1 — API Object Lifecycle

### Objective

Turn **API Object Lifecycle** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl apply -f app.yaml
kubectl get deploy api -o yaml
kubectl get rs,pods -l app=api
kubectl get events --sort-by=.metadata.creationTimestamp
```

### Expected Result

The API object exists, controllers create dependents, and events explain downstream failures.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Verify both API acceptance and reconciled runtime state.

---

## Enhanced Lab 2 — Desired State vs Observed State

### Objective

Turn **Desired State vs Observed State** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get deployment api -o jsonpath='{.spec.replicas}{" desired / "}{.status.availableReplicas}{" available\n"}'
```

### Expected Result

Desired replicas and observed availability can be compared directly.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat status conditions as controller evidence, not decorative metadata.

---

## Enhanced Lab 3 — Generation and ObservedGeneration

### Objective

Turn **Generation and ObservedGeneration** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get deployment api -o jsonpath='{.metadata.generation}{" spec generation / "}{.status.observedGeneration}{" observed\n"}'
```

### Expected Result

When equal, status normally reflects the latest spec generation.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use generation checks when debugging slow or stuck controllers.

---

## Enhanced Lab 4 — resourceVersion and Optimistic Concurrency

### Objective

Turn **resourceVersion and Optimistic Concurrency** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get configmap app-config -o jsonpath='{.metadata.resourceVersion}{"\n"}'
```

### Expected Result

The resource version changes as the object is modified.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not build business logic around numeric ordering of resourceVersion.

---

## Enhanced Lab 5 — Finalizers

### Objective

Turn **Finalizers** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pvc data -o yaml | sed -n '/finalizers:/,/spec:/p'
```

### Expected Result

Finalizer names and deletionTimestamp reveal why the object still exists.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Investigate the controller and dependent infrastructure before manually removing finalizers.

---

## Enhanced Lab 6 — Owner References

### Objective

Turn **Owner References** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pod <POD> -o jsonpath='{.metadata.ownerReferences}'
```

### Expected Result

The Pod points to its ReplicaSet or another controller owner.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Operate the highest-level controller that expresses intent.

---

## Enhanced Lab 7 — Server-Side Apply Field Ownership

### Objective

Turn **Server-Side Apply Field Ownership** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get deployment api -o yaml | sed -n '/managedFields:/,$p' | head -80
```

### Expected Result

Managed fields show different field managers and operations.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Give each automation system clear field ownership.

---

## Enhanced Lab 8 — kubectl Diff as Change Review

### Objective

Turn **kubectl Diff as Change Review** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl diff -f manifests/
```

### Expected Result

Pending additions, deletions, and modifications are visible before apply.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use diff plus context/namespace verification before production writes.

---

## Enhanced Lab 9 — Server Dry-Run

### Objective

Turn **Server Dry-Run** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl apply --server-side --dry-run=server -f app.yaml
```

### Expected Result

The request is validated by the API server without creating the object.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use server dry-run when admission policy matters.

---

## Enhanced Lab 10 — kubectl Explain as Schema Discovery

### Objective

Turn **kubectl Explain as Schema Discovery** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl explain deployment.spec.strategy
kubectl explain pod.spec.securityContext
```

### Expected Result

Fields, types, and descriptions match the connected cluster.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer schema discovery over copying old manifests from blogs.

---

## Enhanced Lab 11 — Namespace Boundary

### Objective

Turn **Namespace Boundary** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl api-resources --namespaced=true
kubectl api-resources --namespaced=false
```

### Expected Result

Namespaced and cluster-scoped resources are clearly distinguished.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Combine namespaces with RBAC, quotas, Pod security, and network policy.

---

## Enhanced Lab 12 — Labels as Control Inputs

### Objective

Turn **Labels as Control Inputs** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pods --show-labels
kubectl get pods -l 'app=api,env=prod'
```

### Expected Result

Selector membership can be inspected before changing labels.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat selector-driving labels as API contract.

---

## Enhanced Lab 13 — Recommended Label Taxonomy

### Objective

Turn **Recommended Label Taxonomy** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
metadata:
  labels:
    app.kubernetes.io/name: orders
    app.kubernetes.io/component: api
    app.kubernetes.io/part-of: commerce
    app.kubernetes.io/version: "1.8.4"
```

### Expected Result

Objects share consistent machine-readable dimensions.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Standardize labels centrally and avoid ad hoc synonyms.

---

## Enhanced Lab 14 — Annotations for Non-Selector Metadata

### Objective

Turn **Annotations for Non-Selector Metadata** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl annotate deployment api owner=platform-team change-ticket=CHG-123
```

### Expected Result

Metadata is attached without changing workload selection.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep large/unstructured data out of labels when it is not used for selection.

---

## Enhanced Lab 15 — Pod Sandbox Mental Model

### Objective

Turn **Pod Sandbox Mental Model** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
Pod
  ├─ shared network namespace
  ├─ shared Pod IP
  ├─ shared volumes
  ├─ app container
  └─ helper container
```

### Expected Result

Containers in one Pod can communicate over localhost and share mounted volumes.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use one Pod only for tightly coupled lifecycle/network requirements.

---

## Enhanced Lab 16 — Pod Conditions

### Objective

Turn **Pod Conditions** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pod <POD> -o jsonpath='{range .status.conditions[*]}{.type}={.status}{" reason="}{.reason}{"\n"}{end}'
```

### Expected Result

The exact condition blocking readiness is visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use conditions before assuming `Running` means healthy.

---

## Enhanced Lab 17 — Container State and LastState

### Objective

Turn **Container State and LastState** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pod <POD> -o jsonpath='{range .status.containerStatuses[*]}{.name}{" restart="}{.restartCount}{" last="}{.lastState.terminated.reason}{" exit="}{.lastState.terminated.exitCode}{"\n"}{end}'
```

### Expected Result

Restart count and previous termination reason are shown per container.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Correlate lastState with `kubectl logs --previous`.

---

## Enhanced Lab 18 — Image Digest Runtime Evidence

### Objective

Turn **Image Digest Runtime Evidence** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pod <POD> -o jsonpath='{range .status.containerStatuses[*]}{.name}{" "}{.imageID}{"\n"}{end}'
```

### Expected Result

The running artifact can be tied to an immutable digest.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Record imageID during incidents and deployments.

---

## Enhanced Lab 19 — Init Container Contract

### Objective

Turn **Init Container Contract** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pod <POD> -o jsonpath='{range .status.initContainerStatuses[*]}{.name}{" "}{.state}{"\n"}{end}'
```

### Expected Result

Initialization state reveals which step is blocking app startup.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Avoid embedding long-running business workflows in init containers.

---

## Enhanced Lab 20 — Native Sidecar Semantics

### Objective

Turn **Native Sidecar Semantics** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
initContainers:
  - name: proxy
    image: example/proxy:1.0
    restartPolicy: Always
```

### Expected Result

The helper starts as an init-style sidecar and remains running with app containers where supported by the cluster version.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use sidecars only when tight Pod-level lifecycle coupling is needed.

---

## Enhanced Lab 21 — Ephemeral Debug Container

### Objective

Turn **Ephemeral Debug Container** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl debug pod/<POD> -it --image=busybox --target=<CONTAINER>
```

### Expected Result

A temporary debug container joins selected namespaces for investigation.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use ephemeral debugging instead of shipping shells/tools in every production image.

---

## Enhanced Lab 22 — Termination Grace Sequence

### Objective

Turn **Termination Grace Sequence** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
deletion requested
  ↓ endpoint/readiness removal
  ↓ preStop (if any)
  ↓ SIGTERM
  ↓ grace period
  ↓ SIGKILL if still running
```

### Expected Result

Application logs show graceful drain before process exit.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set terminationGracePeriodSeconds from measured drain requirements.

---

## Enhanced Lab 23 — preStop Timing

### Objective

Turn **preStop Timing** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
lifecycle:
  preStop:
    exec:
      command: ["sh","-c","sleep 5"]
terminationGracePeriodSeconds: 30
```

### Expected Result

Hook duration and application shutdown fit within the total grace budget.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer the application to handle SIGTERM directly when possible.

---

## Enhanced Lab 24 — Liveness Scope

### Objective

Turn **Liveness Scope** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
DB outage
  ↓ bad liveness checks DB
many Pods restart
  ↓ reconnect storm
incident worsens
```

### Expected Result

The probe does not restart healthy processes merely because a remote dependency is unavailable.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep liveness local and conservative.

---

## Enhanced Lab 25 — Readiness Scope

### Objective

Turn **Readiness Scope** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
process running
DB unavailable
  ↓ readiness false
Service removes endpoint
```

### Expected Result

The Pod remains alive but stops receiving new Service traffic.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use readiness to protect users from partially initialized or dependency-broken instances.

---

## Enhanced Lab 26 — Startup Probe

### Objective

Turn **Startup Probe** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
startupProbe:
  httpGet:
    path: /health/startup
    port: 8080
  periodSeconds: 5
  failureThreshold: 24
```

### Expected Result

The application receives a bounded startup window before liveness begins.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use startup probes instead of extreme liveness initial delays for slow apps.

---

## Enhanced Lab 27 — Probe Budget Math

### Objective

Turn **Probe Budget Math** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```python
period = 5
failure_threshold = 6
print("Approx failure detection seconds:", period * failure_threshold)
```

### Expected Result

The effective detection window is explicit.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Tune probes from failure-detection and recovery objectives.

---

## Enhanced Lab 28 — Deployment Rollout Capacity

### Objective

Turn **Deployment Rollout Capacity** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
replicas=10
maxSurge=2
maxUnavailable=1
→ up to 12 Pods
→ at least 9 desired available during rollout
```

### Expected Result

The cluster has enough headroom for the configured overlap.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Capacity-plan rollout surge before production deployment.

---

## Enhanced Lab 29 — Deployment Availability Condition

### Objective

Turn **Deployment Availability Condition** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get deploy api
kubectl describe deploy api
```

### Expected Result

Available/Progressing conditions explain rollout state.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Watch controller conditions, not only Pod phase.

---

## Enhanced Lab 30 — ProgressDeadlineSeconds

### Objective

Turn **ProgressDeadlineSeconds** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get deploy api -o jsonpath='{range .status.conditions[*]}{.type}{" "}{.reason}{" "}{.message}{"\n"}{end}'
```

### Expected Result

The controller identifies stalled rollout progress.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Connect rollout failure to explicit rollback automation/runbooks.

---

## Enhanced Lab 31 — Revision History and Rollback

### Objective

Turn **Revision History and Rollback** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl rollout history deploy/api
kubectl rollout undo deploy/api --to-revision=<N>
```

### Expected Result

The workload template can revert to a known prior revision.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Pair application rollback with expand/contract schema practices.

---

## Enhanced Lab 32 — Recreate Strategy

### Objective

Turn **Recreate Strategy** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
strategy:
  type: Recreate
```

### Expected Result

Old Pods terminate before new Pods are started.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Choose Recreate only from an explicit exclusivity requirement.

---

## Enhanced Lab 33 — StatefulSet Identity

### Objective

Turn **StatefulSet Identity** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pods -l app=db
kubectl get pvc
```

### Expected Result

Stable Pod names and PVC names map predictably by ordinal.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use an operator/application protocol for database HA, not StatefulSet alone.

---

## Enhanced Lab 34 — StatefulSet Ordered vs Parallel Management

### Objective

Turn **StatefulSet Ordered vs Parallel Management** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
podManagementPolicy: Parallel
```

### Expected Result

Pod creation/deletion ordering matches the chosen policy.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use ordered behavior only when the application genuinely depends on ordinal sequencing.

---

## Enhanced Lab 35 — Headless Service Discovery

### Objective

Turn **Headless Service Discovery** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get svc db-headless -o yaml
kubectl get endpointslices -l kubernetes.io/service-name=db-headless
```

### Expected Result

EndpointSlice records represent individual StatefulSet Pod endpoints.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use headless Services when clients need direct replica identity.

---

## Enhanced Lab 36 — Job Completion Semantics

### Objective

Turn **Job Completion Semantics** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get jobs
kubectl describe job <JOB>
```

### Expected Result

Completions, failures, and retry behavior are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make Job actions idempotent or checkpointed before allowing retries.

---

## Enhanced Lab 37 — Indexed Jobs

### Objective

Turn **Indexed Jobs** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
completion index 0 → shard 0
completion index 1 → shard 1
...
```

### Expected Result

Each Pod can derive its work partition from the completion index.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use indexed Jobs for deterministic partitioned batch workloads.

---

## Enhanced Lab 38 — CronJob Missed/Overlapping Runs

### Objective

Turn **CronJob Missed/Overlapping Runs** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
concurrencyPolicy: Forbid
startingDeadlineSeconds: 300
```

### Expected Result

A late or overlapping schedule behaves according to an explicit policy.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Design CronJobs for duplicate/missed execution scenarios.

---

## Enhanced Lab 39 — DaemonSet Node Agent Blast Radius

### Objective

Turn **DaemonSet Node Agent Blast Radius** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl rollout status daemonset/<DS> -n kube-system
```

### Expected Result

Node-agent rollout progress is visible cluster-wide.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Canary infrastructure DaemonSet changes before broad rollout.

---

## Enhanced Lab 40 — Service Virtual IP

### Objective

Turn **Service Virtual IP** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get svc api -o wide
kubectl get endpointslices -l kubernetes.io/service-name=api
```

### Expected Result

Service VIP and backend endpoints are distinct.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Debug Service data plane separately from the application listener.

---

## Enhanced Lab 41 — EndpointSlice Readiness

### Objective

Turn **EndpointSlice Readiness** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get endpointslices -l kubernetes.io/service-name=api -o yaml
```

### Expected Result

Backend addresses and readiness conditions are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

When a Service has no traffic, inspect EndpointSlices before DNS.

---

## Enhanced Lab 42 — Named Ports

### Objective

Turn **Named Ports** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
ports:
  - name: http
    containerPort: 8080
```

### Expected Result

Service targetPort can reference `http` instead of repeating 8080.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use stable named ports for application protocols.

---

## Enhanced Lab 43 — ClusterIP vs NodePort vs LoadBalancer

### Objective

Turn **ClusterIP vs NodePort vs LoadBalancer** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
ClusterIP    → inside cluster
NodePort     → node IP:port
LoadBalancer → external/internal LB + Service
```

### Expected Result

The exposure level is explicit.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use the narrowest exposure type that meets the requirement.

---

## Enhanced Lab 44 — ExternalName Limitations

### Objective

Turn **ExternalName Limitations** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
type: ExternalName
externalName: database.example.internal
```

### Expected Result

DNS resolves the Service name to the external target.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use ExternalName only when DNS indirection matches protocol expectations.

---

## Enhanced Lab 45 — Service Session Affinity

### Objective

Turn **Service Session Affinity** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
sessionAffinity: ClientIP
```

### Expected Result

Repeat requests from one client tend toward the same backend while affinity is active.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Externalize session state instead of depending on stickiness whenever possible.

---

## Enhanced Lab 46 — CoreDNS Search Path

### Objective

Turn **CoreDNS Search Path** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl exec <POD> -- cat /etc/resolv.conf
```

### Expected Result

nameserver, search, and options reveal cluster DNS behavior.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use FQDN or namespace-qualified names when cross-namespace ambiguity matters.

---

## Enhanced Lab 47 — DNS ndots Behavior

### Objective

Turn **DNS ndots Behavior** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl exec <POD> -- cat /etc/resolv.conf
```

### Expected Result

The `options ndots:` value can be inspected.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Measure DNS behavior before changing cluster-wide resolver settings.

---

## Enhanced Lab 48 — Service Selector Failure

### Objective

Turn **Service Selector Failure** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get svc api -o jsonpath='{.spec.selector}'
kubectl get pods --show-labels
kubectl get endpointslices -l kubernetes.io/service-name=api
```

### Expected Result

The selector/label mismatch is visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Debug selector → Pod label → readiness in that order.

---

## Enhanced Lab 49 — Ingress Controller Dependency

### Objective

Turn **Ingress Controller Dependency** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get ingressclass
kubectl get ingress -A
```

### Expected Result

The cluster has a controller/class capable of processing the resource.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not expect Ingress YAML alone to expose traffic.

---

## Enhanced Lab 50 — Gateway API Role Separation

### Objective

Turn **Gateway API Role Separation** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
platform team:
GatewayClass + Gateway

application team:
HTTPRoute / GRPCRoute
```

### Expected Result

Route attachment status shows whether policy/listeners accept the route.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use role separation to reduce shared ingress configuration conflicts.

---

## Enhanced Lab 51 — Gateway Route Status

### Objective

Turn **Gateway Route Status** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get httproute <ROUTE> -o yaml
```

### Expected Result

Accepted/ResolvedRefs-style conditions explain attachment problems.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Read status conditions before changing listener or backend configuration.

---

## Enhanced Lab 52 — NetworkPolicy Default Deny

### Objective

Turn **NetworkPolicy Default Deny** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Expected Result

Selected Pods become isolated except for separately allowed flows.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Add DNS and required service egress before enabling deny-all in production.

---

## Enhanced Lab 53 — NetworkPolicy DNS Allow

### Objective

Turn **NetworkPolicy DNS Allow** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
app Pod
  ↓ DNS UDP/TCP 53
CoreDNS Service/Pods
```

### Expected Result

Name resolution succeeds while other unauthorized egress remains blocked.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat DNS as an explicit dependency in default-deny designs.

---

## Enhanced Lab 54 — NetworkPolicy Namespace Selectors

### Objective

Turn **NetworkPolicy Namespace Selectors** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get ns --show-labels
```

### Expected Result

Namespace labels used by policies are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Protect security-significant namespace labels through governance/admission.

---

## Enhanced Lab 55 — ConfigMap Env vs Volume Update

### Objective

Turn **ConfigMap Env vs Volume Update** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get configmap app-config -o yaml
kubectl exec <POD> -- env | grep APP_
```

### Expected Result

The live process environment can differ from the latest ConfigMap object.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use explicit rollout/reload strategy for configuration changes.

---

## Enhanced Lab 56 — Secret Encoding vs Encryption

### Objective

Turn **Secret Encoding vs Encryption** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get secret demo -o jsonpath='{.data.password}' | base64 -d; echo
```

### Expected Result

Anyone with Secret read permission can recover the value.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat Secret read permission as access to plaintext secret material.

---

## Enhanced Lab 57 — Projected ServiceAccount Tokens

### Objective

Turn **Projected ServiceAccount Tokens** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl create token <SERVICEACCOUNT> --duration=10m
```

### Expected Result

A short-lived token is issued for the workload identity.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Disable token automount for workloads that do not call the Kubernetes API.

---

## Enhanced Lab 58 — Resource Requests as Scheduling Contract

### Objective

Turn **Resource Requests as Scheduling Contract** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe node <NODE> | sed -n '/Allocated resources:/,$p' | head -30
```

### Expected Result

Requested CPU/memory allocations are visible independently of current usage.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Right-size requests from measured workload demand.

---

## Enhanced Lab 59 — CPU Limit Throttling

### Objective

Turn **CPU Limit Throttling** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl top pod <POD>
kubectl get pod <POD> -o jsonpath='{.spec.containers[*].resources}'
```

### Expected Result

Configured limits and current usage can be compared.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Investigate throttling before assuming the application needs more replicas.

---

## Enhanced Lab 60 — Memory Limit OOM

### Objective

Turn **Memory Limit OOM** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe pod <POD> | grep -A5 -E 'Last State|OOMKilled'
```

### Expected Result

Termination reason indicates OOMKilled when applicable.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Size memory for startup, steady state, and peak behavior.

---

## Enhanced Lab 61 — QoS Classes

### Objective

Turn **QoS Classes** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pod <POD> -o jsonpath='{.status.qosClass}{"\n"}'
```

### Expected Result

The Pod's QoS class is explicit.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Avoid accidental BestEffort for important workloads.

---

## Enhanced Lab 62 — Ephemeral Storage Requests

### Objective

Turn **Ephemeral Storage Requests** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
resources:
  requests:
    ephemeral-storage: 500Mi
  limits:
    ephemeral-storage: 2Gi
```

### Expected Result

Pod resource policy includes local storage consumption.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat node disk as a schedulable/limited resource.

---

## Enhanced Lab 63 — emptyDir Medium Memory

### Objective

Turn **emptyDir Medium Memory** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
volumes:
  - name: scratch
    emptyDir:
      medium: Memory
      sizeLimit: 256Mi
```

### Expected Result

The temporary volume is bounded and disappears with the Pod.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use memory-backed emptyDir only for bounded scratch data.

---

## Enhanced Lab 64 — NodeSelector Hard Constraint

### Objective

Turn **NodeSelector Hard Constraint** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get nodes --show-labels
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Result

Scheduling events report unmatched node selectors.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use nodeSelector only for durable infrastructure capabilities.

---

## Enhanced Lab 65 — Node Affinity Required vs Preferred

### Objective

Turn **Node Affinity Required vs Preferred** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
requiredDuringScheduling... → hard filter
preferredDuringScheduling... → scoring preference
```

### Expected Result

A workload can fall back only when the policy is preferred.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use preferences for performance/locality and hard rules for true constraints.

---

## Enhanced Lab 66 — Taints and Tolerations

### Objective

Turn **Taints and Tolerations** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe node <NODE> | grep -i Taints
```

### Expected Result

The node's taints are visible alongside Pod tolerations.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Combine taints with affinity/selectors for dedicated-node placement.

---

## Enhanced Lab 67 — Topology Spread Constraints

### Objective

Turn **Topology Spread Constraints** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app: api
```

### Expected Result

Replicas are spread across nodes with bounded skew.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Design for node/zone failure capacity, not only normal balance.

---

## Enhanced Lab 68 — Pod Anti-Affinity Trade-Off

### Objective

Turn **Pod Anti-Affinity Trade-Off** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
3 replicas
3 nodes
strict one-per-node
1 node fails
→ replacement needs a fourth eligible node
```

### Expected Result

The trade-off between resilience and schedulability is explicit.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer topology spread unless strict separation is required.

---

## Enhanced Lab 69 — PVC Binding

### Objective

Turn **PVC Binding** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe pvc <PVC>
kubectl get storageclass
kubectl get pv
```

### Expected Result

PVC events identify provisioning or compatibility failures.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Troubleshoot PVC before changing the Pod when storage is unbound.

---

## Enhanced Lab 70 — WaitForFirstConsumer

### Objective

Turn **WaitForFirstConsumer** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get storageclass <SC> -o jsonpath='{.volumeBindingMode}{"\n"}'
```

### Expected Result

The class reports WaitForFirstConsumer where configured.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use topology-aware binding for zonal block storage.

---

## Enhanced Lab 71 — Reclaim Policy

### Objective

Turn **Reclaim Policy** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pv -o custom-columns=NAME:.metadata.name,RECLAIM:.spec.persistentVolumeReclaimPolicy,STATUS:.status.phase
```

### Expected Result

Each persistent volume's reclaim behavior is visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use Retain for data requiring deliberate recovery/cleanup.

---

## Enhanced Lab 72 — VolumeSnapshot Is Not Backup

### Objective

Turn **VolumeSnapshot Is Not Backup** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
PVC
  ↓ snapshot
same storage domain
  ↓
backup copy
separate failure domain
```

### Expected Result

Recovery design distinguishes fast snapshot from durable backup.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Test restore paths rather than equating snapshot creation with backup.

---

## Enhanced Lab 73 — ServiceAccount Least Privilege

### Objective

Turn **ServiceAccount Least Privilege** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl auth can-i get pods --as=system:serviceaccount:<NS>:<SA> -n <NS>
```

### Expected Result

The workload's effective API permission is verifiable.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Create one identity per application capability and grant only required verbs/resources.

---

## Enhanced Lab 74 — RoleBinding Scope

### Objective

Turn **RoleBinding Scope** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get rolebindings,clusterrolebindings -A
```

### Expected Result

Namespaced versus cluster-wide bindings are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer RoleBinding when access only needs one namespace.

---

## Enhanced Lab 75 — kubectl auth can-i

### Objective

Turn **kubectl auth can-i** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl auth can-i create pods/exec   --as=system:serviceaccount:app:reader   -n app
```

### Expected Result

The API server returns an explicit yes/no authorization decision.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use can-i before changing RBAC.

---

## Enhanced Lab 76 — SecurityContext Restricted Baseline

### Objective

Turn **SecurityContext Restricted Baseline** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: api
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
      readOnlyRootFilesystem: true
```

### Expected Result

The manifest expresses least privilege instead of relying on runtime defaults.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Start from restricted posture and add narrow exceptions.

---

## Enhanced Lab 77 — Pod Security Admission

### Objective

Turn **Pod Security Admission** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl label ns app   pod-security.kubernetes.io/enforce=restricted   --overwrite
```

### Expected Result

Non-compliant Pods are rejected in the protected namespace.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Roll out PSA with warn/audit before enforce in existing namespaces.

---

## Enhanced Lab 78 — HostPath Risk

### Objective

Turn **HostPath Risk** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pods -A -o json | jq -r '..|.hostPath? // empty' 2>/dev/null | head
```

### Expected Result

Host-mounted paths can be inventoried.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Avoid hostPath for ordinary apps and isolate infrastructure Pods that require it.

---

## Enhanced Lab 79 — hostNetwork and hostPID

### Objective

Turn **hostNetwork and hostPID** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get pod <POD> -o jsonpath='{.spec.hostNetwork}{" hostNetwork "}{.spec.hostPID}{" hostPID\n"}'
```

### Expected Result

Host namespace sharing is explicitly visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Require a documented infrastructure use case for host namespace access.

---

## Enhanced Lab 80 — HPA Control Loop

### Objective

Turn **HPA Control Loop** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get hpa
kubectl describe hpa <HPA>
```

### Expected Result

Current metric, target, desired replicas, and scaling events are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not rely on HPA alone for sudden burst absorption.

---

## Enhanced Lab 81 — HPA + Requests

### Objective

Turn **HPA + Requests** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
usage 200m
request 400m
→ 50% utilization
```

### Expected Result

Scaling targets can be interpreted correctly.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Define realistic requests before enabling CPU-based HPA.

---

## Enhanced Lab 82 — Queue-Length Autoscaling Concept

### Objective

Turn **Queue-Length Autoscaling Concept** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
queue depth
  ↓ metrics adapter/event scaler
HPA/controller
  ↓ worker replicas
```

### Expected Result

Replica count follows work backlog rather than incidental CPU.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Choose a scaling metric causally related to workload demand.

---

## Enhanced Lab 83 — Metrics Server Limits

### Objective

Turn **Metrics Server Limits** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl top nodes
kubectl top pods -A
```

### Expected Result

Current CPU/memory metrics are available.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use Prometheus/managed monitoring for durable metrics and SLOs.

---

## Enhanced Lab 84 — Events as Ephemeral Evidence

### Objective

Turn **Events as Ephemeral Evidence** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get events -A --sort-by=.metadata.creationTimestamp | tail -50
```

### Expected Result

Recent scheduling, probe, mount, and pull failures are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Forward important operational events if longer history is required.

---

## Enhanced Lab 85 — Structured Logs and Pod Identity

### Objective

Turn **Structured Logs and Pod Identity** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```json
{"service":"orders","version":"1.8.4","request_id":"r-42","level":"ERROR","message":"db timeout"}
```

### Expected Result

Application and Kubernetes metadata can be correlated in a central log system.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use immutable image/version fields in logs for incident reconstruction.

---

## Enhanced Lab 86 — OpenTelemetry in Kubernetes

### Objective

Turn **OpenTelemetry in Kubernetes** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
apps
  ↓ OTel SDK
collector agent/gateway
  ↓
trace/metric/log backends
```

### Expected Result

Application telemetry complements Kubernetes object/runtime metrics.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Instrument the application, not only the cluster.

---

## Enhanced Lab 87 — Helm Template vs Release State

### Objective

Turn **Helm Template vs Release State** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
helm get values <RELEASE>
helm get manifest <RELEASE> | head -80
helm history <RELEASE>
```

### Expected Result

Release inputs, rendered output, and history are available.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not debug Helm values without inspecting the rendered manifest.

---

## Enhanced Lab 88 — Helm Values Schema

### Objective

Turn **Helm Values Schema** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
values.yaml
  ↓ values.schema.json validation
templates
  ↓ Kubernetes objects
```

### Expected Result

Invalid values fail early during Helm rendering/install.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use chart schemas for shared production charts.

---

## Enhanced Lab 89 — Kustomize Overlay Discipline

### Objective

Turn **Kustomize Overlay Discipline** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
base/
overlays/dev/
overlays/prod/
```

### Expected Result

Rendered dev/prod manifests differ only where intended.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep overlays small and review `kubectl kustomize` output in CI.

---

## Enhanced Lab 90 — Immutable Image Promotion

### Objective

Turn **Immutable Image Promotion** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
build digest D
  ↓ dev test D
  ↓ staging test D
  ↓ prod deploy D
```

### Expected Result

All environments use the same artifact bytes.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Promote digests; change configuration separately.

---

## Enhanced Lab 91 — Config Rollout Checksum

### Objective

Turn **Config Rollout Checksum** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
metadata:
  annotations:
    checksum/config: "<rendered-config-hash>"
```

### Expected Result

Config changes alter Pod template and create a new rollout.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make configuration update semantics explicit.

---

## Enhanced Lab 92 — GitOps Mental Model

### Objective

Turn **GitOps Mental Model** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
Git desired state
  ↓ GitOps controller
Kubernetes API
  ↓ controllers
runtime state
```

### Expected Result

Drift is visible and can be corrected by reconciliation.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Avoid manual changes that conflict with the authoritative Git owner.

---

## Enhanced Lab 93 — Admission Policy Preview

### Objective

Turn **Admission Policy Preview** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
kubectl apply
  ↓ authn/authz
admission policy
  ├─ allow
  └─ reject
```

### Expected Result

Unsafe configuration is blocked before persistence.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Convert repeatable review rules into admission policy.

---

## Enhanced Lab 94 — Application SLO

### Objective

Turn **Application SLO** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
SLI = successful valid requests / valid requests
SLO = 99.95% monthly
latency p95 < 500 ms
```

### Expected Result

Application dashboards show whether users receive the intended service.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use Kubernetes metrics for diagnosis and SLOs for outcome.

---

## Enhanced Lab 95 — PodDisruptionBudget Preview

### Objective

Turn **PodDisruptionBudget Preview** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: api
```

### Expected Result

Node drain respects the disruption budget for matching Pods.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set PDBs from real replica count and failure capacity.

---

## Enhanced Lab 96 — Graceful Degradation

### Objective

Turn **Graceful Degradation** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
critical DB down → readiness false
optional analytics down → continue core API with degraded feature
```

### Expected Result

The service retains useful behavior when noncritical dependencies fail.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Design dependency failure semantics before writing probes.

---

## Enhanced Lab 97 — Retry Backoff and Jitter

### Objective

Turn **Retry Backoff and Jitter** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```python
import random
for n in range(5):
    print(round(min(30, 2**n) + random.random(), 2))
```

### Expected Result

Retry intervals spread instead of synchronizing across replicas.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Retry only transient failures and cap total retry time.

---

## Enhanced Lab 98 — Circuit Breaker Concept

### Objective

Turn **Circuit Breaker Concept** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
CLOSED → normal
failures rise
OPEN → fail fast/fallback
after cooldown
HALF-OPEN → test recovery
```

### Expected Result

The app stops flooding an unhealthy dependency.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use circuit breaking for remote dependencies where repeated calls amplify incidents.

---

## Enhanced Lab 99 — Bulkhead Isolation

### Objective

Turn **Bulkhead Isolation** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
interactive API pool
batch/report pool
notification pool
```

### Expected Result

Noncritical overload cannot starve critical paths.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Partition scarce resources by business criticality.

---

## Enhanced Lab 100 — Deployment Canary Concept

### Objective

Turn **Deployment Canary Concept** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
stable v1 95%
canary v2 5%
  ↓ observe
promote or rollback
```

### Expected Result

The new version is evaluated against objective metrics before full promotion.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Define canary success/rollback criteria before rollout.

---

## Enhanced Lab 101 — Blue-Green Concept

### Objective

Turn **Blue-Green Concept** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
Service selector
  ↓
blue v1

switch selector
  ↓
green v2
```

### Expected Result

Rollback can switch traffic back quickly if data/schema compatibility allows.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use immutable labels and tested switch/rollback procedure.

---

## Enhanced Lab 102 — Pod Priority Preview

### Objective

Turn **Pod Priority Preview** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get priorityclasses
```

### Expected Result

Available priority classes can be reviewed.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not mark ordinary apps system-critical.

---

## Enhanced Lab 103 — ResourceQuota Preview

### Objective

Turn **ResourceQuota Preview** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get resourcequota -A
```

### Expected Result

Team-level resource ceilings are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use quota to prevent one namespace from exhausting shared cluster capacity.

---

## Enhanced Lab 104 — LimitRange Preview

### Objective

Turn **LimitRange Preview** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get limitrange -A
```

### Expected Result

Default/min/max resource policies are visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use LimitRange to avoid accidental BestEffort workloads.

---

## Enhanced Lab 105 — Node Pressure Awareness

### Objective

Turn **Node Pressure Awareness** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe node <NODE> | sed -n '/Conditions:/,/Addresses:/p'
```

### Expected Result

Pressure conditions show node-level resource health.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Troubleshoot the node when many unrelated Pods fail together.

---

## Enhanced Lab 106 — Service Account Token Exposure

### Objective

Turn **Service Account Token Exposure** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```yaml
automountServiceAccountToken: false
```

### Expected Result

The Pod no longer receives an unnecessary API bearer token.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Remove unused credentials from workloads.

---

## Enhanced Lab 107 — ImagePullSecret vs Workload Identity

### Objective

Turn **ImagePullSecret vs Workload Identity** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
static imagePullSecret
vs
node/workload identity → short-lived registry token
```

### Expected Result

Registry authentication is tied to managed identity rather than reusable passwords.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer short-lived identity-based registry auth where available.

---

## Enhanced Lab 108 — Debugging Minimal Images

### Objective

Turn **Debugging Minimal Images** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl run net-debug --rm -it --image=nicolaka/netshoot -- bash
```

### Expected Result

A disposable diagnostic environment can test DNS/network without modifying production images.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep debug tooling ephemeral and access-controlled.

---

## Enhanced Lab 109 — Pod Pending Diagnostic Tree

### Objective

Turn **Pod Pending Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe pod <POD>
kubectl get events --field-selector involvedObject.name=<POD> --sort-by=.metadata.creationTimestamp
```

### Expected Result

Scheduler/storage/sandbox messages identify the blocked layer.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Read the event message literally before changing resources.

---

## Enhanced Lab 110 — CrashLoopBackOff Diagnostic Tree

### Objective

Turn **CrashLoopBackOff Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl logs <POD> -c <CONTAINER> --previous
kubectl describe pod <POD>
```

### Expected Result

The previous container's actual failure reason is preserved.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Capture evidence before deleting the Pod.

---

## Enhanced Lab 111 — ImagePullBackOff Diagnostic Tree

### Objective

Turn **ImagePullBackOff Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Result

Events include the runtime/registry error string.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix registry/reference cause rather than repeatedly deleting the Pod.

---

## Enhanced Lab 112 — Service No Endpoints Diagnostic Tree

### Objective

Turn **Service No Endpoints Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get svc <SVC> -o yaml
kubectl get endpointslices -l kubernetes.io/service-name=<SVC> -o wide
kubectl get pods --show-labels
```

### Expected Result

The backend selection failure is visible.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Debug endpoint production before kube-proxy/CNI.

---

## Enhanced Lab 113 — DNS Diagnostic Tree

### Objective

Turn **DNS Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl run dns-debug --rm -it --image=busybox -- nslookup kubernetes.default
```

### Expected Result

The cluster-local resolver path can be tested independently.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate cluster-local DNS from external-upstream DNS.

---

## Enhanced Lab 114 — NetworkPolicy Diagnostic Tree

### Objective

Turn **NetworkPolicy Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl get networkpolicy -A
kubectl get pod <POD> --show-labels
```

### Expected Result

The exact policy selection can be reconstructed.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Test one allowed and one denied flow after every policy change.

---

## Enhanced Lab 115 — PVC Pending Diagnostic Tree

### Objective

Turn **PVC Pending Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl describe pvc <PVC>
kubectl get storageclass
```

### Expected Result

PVC events show the provisioning decision and error.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Start with the claim and provisioner before changing application YAML.

---

## Enhanced Lab 116 — RBAC Forbidden Diagnostic Tree

### Objective

Turn **RBAC Forbidden Diagnostic Tree** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl auth can-i <VERB> <RESOURCE>   --as=<SUBJECT> -n <NAMESPACE>
```

### Expected Result

The exact action is allowed or denied for the identity.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not grant cluster-admin to make a single verb work.

---

## Enhanced Lab 117 — Context Safety

### Objective

Turn **Context Safety** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```bash
kubectl config current-context
kubectl config view --minify
kubectl get ns
```

### Expected Result

Cluster, user, and default namespace are visible before writes.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make context/namespace verification habitual before destructive operations.

---

## Enhanced Lab 118 — Evidence-First Troubleshooting

### Objective

Turn **Evidence-First Troubleshooting** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
Deployment/StatefulSet
  ↓ ReplicaSet/Pod
  ↓ container
  ↓ Service/EndpointSlice
  ↓ DNS/NetworkPolicy
  ↓ PVC/Config/Secret
  ↓ node/runtime
```

### Expected Result

The failing layer is isolated before remediation.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Change one layer at a time and preserve the evidence that justified it.

---

## Enhanced Lab 119 — Operational Readiness Review

### Objective

Turn **Operational Readiness Review** into a repeatable Kubernetes engineering and troubleshooting exercise.

### Safety Boundary

Use a disposable kind/minikube/k3d cluster or another authorized lab. Use fake credentials and non-production data. Avoid intentionally destabilizing shared clusters.

### Procedure

1. Verify current context and namespace.
2. Draw the expected object/controller/data path.
3. Apply or inspect the relevant object.
4. Run the command/query below and record baseline evidence.
5. Introduce one reversible failure where safe.
6. Diagnose using status, conditions, events, logs, and dependent objects.
7. Restore the intended state.
8. Verify application behavior, not just object existence.
9. Record the security/reliability impact.
10. Convert the finding into a reusable check/runbook.

### Command / Configuration

```text
[ ] owner/on-call
[ ] image digest
[ ] resources
[ ] startup/readiness/liveness
[ ] graceful termination
[ ] ServiceAccount/RBAC
[ ] restricted security context
[ ] NetworkPolicy
[ ] backup/restore
[ ] logs/metrics/traces
[ ] rollout/rollback
```

### Expected Result

The workload can be operated and recovered before launch.

### Evidence Record

```text
Context / namespace
Top-level object
Desired state
Observed status
Owner chain
Pod/container state
Service/EndpointSlice
DNS/NetworkPolicy
Config/Secret/PVC
Node/resources
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make operational readiness a deployment gate.

---

## 5. Hands-on Lab / Practical Exercises

> Use your own lab cluster or an authorized training environment.

### Lab 1 — Create a Local Cluster

Using `kind` or `minikube`, create a disposable cluster.

Verify:

```bash
kubectl cluster-info
kubectl get nodes
kubectl get pods -A
```

Identify control-plane and system Pods.

### Lab 2 — Explore API Resources

```bash
kubectl api-resources
kubectl api-versions
kubectl explain pod
kubectl explain deployment.spec
```

Create a table of 20 resources and whether each is namespaced.

### Lab 3 — Contexts and Namespaces

Create:

```text
development
staging
production
```

Set current context namespace to `development`.

Practice switching safely.

### Lab 4 — First Pod

Create an nginx Pod with YAML.

Inspect:

```bash
kubectl get pod -o wide
kubectl describe pod
kubectl get pod -o yaml
```

Locate spec and status.

### Lab 5 — Pod Lifecycle

Delete and recreate Pod while running:

```bash
kubectl get pod -w
```

Record lifecycle state changes.

### Lab 6 — CrashLoopBackOff

Deploy a container with invalid command.

Use:

```bash
kubectl logs
kubectl logs --previous
kubectl describe pod
kubectl get events
```

Identify root cause.

### Lab 7 — Init Container

Create init container that writes a file into `emptyDir`.

Main container reads the file.

Explain shared-volume lifecycle.

### Lab 8 — Multi-Container Pod

Create app + helper container sharing:

```text
localhost
emptyDir
```

Prove they share Pod network.

### Lab 9 — Ephemeral Debug Container

Use `kubectl debug` on a minimal Pod that has no shell.

Inspect DNS/network from debug image.

### Lab 10 — Labels and Selectors

Create five Pods with labels:

```text
app
tier
env
version
```

Query:

```bash
kubectl get pods -l app=api
kubectl get pods -l 'env in (dev,test)'
```

### Lab 11 — Deployment

Create:

```text
api Deployment
replicas: 3
```

Delete one Pod and watch self-healing.

### Lab 12 — Rolling Update

Change image version.

Watch:

```bash
kubectl rollout status
kubectl get rs
kubectl get pods -w
```

Explain old/new ReplicaSets.

### Lab 13 — Rollback

Deploy broken image.

Rollback:

```bash
kubectl rollout undo deployment/api
```

Verify recovery.

### Lab 14 — DaemonSet

Deploy a lightweight DaemonSet.

Verify one Pod per matching Node.

### Lab 15 — Job

Create a Job that calculates or processes a file then exits successfully.

Inspect completion and logs.

### Lab 16 — CronJob

Create a CronJob every few minutes in lab.

Observe Jobs/Pods created.

Suspend it afterward.

### Lab 17 — StatefulSet

Create simple three-replica StatefulSet with headless Service.

Observe:

```text
app-0
app-1
app-2
```

and DNS identities.

### Lab 18 — ClusterIP Service

Expose Deployment internally.

From temporary client Pod:

```bash
curl http://api
```

### Lab 19 — Service Selector Failure

Intentionally mismatch selector.

Observe empty EndpointSlices.

Fix labels/selector.

### Lab 20 — Service Types

Compare:

```text
ClusterIP
NodePort
LoadBalancer concept
ExternalName
```

Use local cluster capabilities safely.

### Lab 21 — DNS

From a Pod:

```bash
nslookup kubernetes.default
nslookup api
nslookup api.NAMESPACE
```

Inspect `/etc/resolv.conf`.

### Lab 22 — Ingress

Install/use local Ingress controller if lab supports it.

Route:

```text
/app → frontend
/api → api
```

### Lab 23 — Gateway API Tabletop

Design:

```text
GatewayClass
Gateway
HTTPRoute
```

for two teams:

```text
platform team owns Gateway
app team owns HTTPRoute
```

### Lab 24 — ConfigMap

Inject config both ways:

```text
environment
mounted file
```

Update ConfigMap and observe different update behavior.

### Lab 25 — Secret

Create a lab-only Secret.

Mount as file.

Demonstrate that base64 is reversible and discuss RBAC/encryption requirements.

### Lab 26 — Probes

Add:

```text
startup
readiness
liveness
```

probes.

Break readiness only and observe Service endpoint behavior.

### Lab 27 — Graceful Shutdown

Deploy app that handles SIGTERM.

Delete Pod and observe grace period/logs.

### Lab 28 — Resources and OOM

Set a low memory limit for a controlled memory workload.

Observe `OOMKilled`.

Increase appropriately.

### Lab 29 — CPU Throttling

Set:

```text
request: 100m
limit: 200m
```

on CPU workload.

Observe `kubectl top` and application performance.

### Lab 30 — Scheduling

Label a Node:

```text
disktype=ssd
```

Use `nodeSelector`.

Then remove label and observe Pending scheduling behavior.

### Lab 31 — Taints/Tolerations

Taint a lab worker.

Create Pod without toleration, then with toleration.

Explain that toleration permits but does not force placement.

### Lab 32 — Topology Spread Tabletop

Design three replicas across:

```text
zone
node
```

with topology spread constraints.

### Lab 33 — PVC

Create PVC using lab StorageClass.

Mount into Pod.

Write file, replace Pod, verify persistence.

### Lab 34 — Reclaim Policy

Inspect:

```bash
kubectl get storageclass
kubectl get pv
kubectl get pvc
```

Explain what happens if PVC is deleted.

### Lab 35 — RBAC

Create ServiceAccount `reader`.

Grant only:

```text
get/list Pods
```

Test:

```bash
kubectl auth can-i ...
```

### Lab 36 — Security Context

Run container:

```text
non-root
drop ALL capabilities
RuntimeDefault seccomp
read-only root
```

Add only required writable `emptyDir`.

### Lab 37 — NetworkPolicy

If CNI supports it:

```text
default deny
allow frontend → api
allow api → db
```

Test permitted and denied paths.

### Lab 38 — HPA

Install/use metrics-server if lab supports it.

Create CPU-based HPA and generate safe load.

Observe replica changes.

### Lab 39 — Kustomize

Create:

```text
base/
overlays/dev/
overlays/prod/
```

change replicas/image tags without copying full manifests.

### Lab 40 — Helm

Install a simple chart.

Inspect:

```bash
helm list
helm get manifest RELEASE
helm history RELEASE
```

Upgrade and rollback.

### Lab 41 — Full Application

Deploy:

```text
frontend
api
redis
postgres
```

with Services, ConfigMaps, Secrets, PVC, probes, and resource requests.

### Lab 42 — Failure Game Day

Simulate:

1. ImagePullBackOff
2. CrashLoopBackOff
3. OOMKilled
4. Pod Pending
5. bad readiness
6. Service no endpoints
7. DNS failure
8. NetworkPolicy deny
9. PVC Pending
10. bad ConfigMap key

For each record:

```text
Symptom
Evidence
Root Cause
Fix
Verification
Prevention
```

### Lab 43 — kubectl Speed Drill

Without copying commands from history, perform:

```text
create namespace
generate Pod YAML
create Deployment
scale
expose
inspect
logs
exec
rollout
rollback
delete
```

Focus on accuracy before speed.

### Lab 44 — Architecture Review

Review your application for:

```text
statelessness
identity
health
resources
network exposure
secret handling
storage
rollout
observability
```

### Lab 45 — Docker-to-Kubernetes Mapping

Document:

```text
Dockerfile          → image
docker run          → Pod
Compose service     → Deployment/StatefulSet + Service
Docker volume       → PVC/PV
Docker healthcheck  → probes
Docker network DNS  → Service/CoreDNS
Docker resource cap → requests/limits
```

---

## 6. Mini Project

# Mini Project — Kubernetes Production Fundamentals Platform

Deploy a customer-order application.

Architecture:

```text
                       Client
                         |
                  Ingress / Gateway
                         |
              +----------+----------+
              |                     |
          Frontend                API Service
              |                     |
              +----------+----------+
                         |
                    API Deployment
                    /           \
                 Redis        PostgreSQL
                                  |
                                  PVC
```

Background processing:

```text
API
 ↓
Queue
 ↓
Worker Deployment
```

Required Kubernetes objects:

```text
Namespaces
Deployments
Services
StatefulSet or DB Deployment for lab
ConfigMaps
Secrets
ServiceAccounts
Roles / RoleBindings
PVCs
StorageClass usage
Ingress or Gateway design
NetworkPolicies
HPA
Jobs
CronJob
```

## Workload Requirements

Frontend:

```text
2 replicas
readiness/liveness
non-root
CPU/memory requests
ClusterIP Service
```

API:

```text
3 replicas
startup/readiness/liveness
graceful shutdown
non-root
read-only rootfs
ConfigMap
Secret
HPA
```

Worker:

```text
2 replicas
queue-based workload
resource limits
graceful termination
```

Database:

```text
persistent PVC
backup Job/CronJob concept
not publicly exposed
```

## Network Policy

Enforce:

```text
Ingress → Frontend/API
Frontend → API
API → PostgreSQL/Redis
Worker → PostgreSQL/Redis
No direct Frontend → PostgreSQL
```

## Security

Require:

```text
dedicated ServiceAccounts
least privilege RBAC
runAsNonRoot
drop capabilities
RuntimeDefault seccomp
read-only rootfs where possible
no privileged
no hostPath
no hostNetwork
```

## Observability

Define:

```text
logs
events
health
CPU
memory
restarts
HPA
PVC usage
Service endpoints
application latency/error rate
```

## Git Structure

```text
k8s-platform/
├── base/
│   ├── frontend/
│   ├── api/
│   ├── worker/
│   ├── database/
│   └── networking/
├── overlays/
│   ├── dev/
│   └── prod/
├── helm/
├── docs/
└── README.md
```

## Required Runbooks

```text
RUNBOOK_POD_PENDING.md
RUNBOOK_CRASHLOOP.md
RUNBOOK_IMAGE_PULL.md
RUNBOOK_OOM.md
RUNBOOK_SERVICE_NO_ENDPOINTS.md
RUNBOOK_DNS.md
RUNBOOK_NETWORK_POLICY.md
RUNBOOK_PVC_PENDING.md
RUNBOOK_ROLLOUT.md
RUNBOOK_ROLLBACK.md
```

---

## 7. Recommended Resources

This Markdown is designed to be self-contained for the course.

For current production syntax and behavior, use official upstream documentation:

```text
Kubernetes Documentation
Kubernetes Concepts
Kubernetes API Reference
kubectl Reference
Kubernetes Release Notes
Gateway API Documentation
OCI Specifications
```

Current baseline for this course:

```text
Kubernetes v1.36
Latest stable patch verified: v1.36.2
```

---

## 8. Certification Relevance

This course prepares directly for:

```text
60. Kubernetes Administration
CKA
CKAD
CKS
Kubernetes operations
Platform Engineering
Cloud-native development
DevSecOps
```

The current CKA remains a **performance-based, command-line exam**. The current Linux Foundation page reports the exam environment as Kubernetes **v1.35** and states that exam environments typically align with the newest Kubernetes minor release within approximately **4–8 weeks** after upstream release.

This course deliberately teaches v1.36-era fundamentals so the concepts remain ahead of the current CKA environment without relying on experimental v1.37 behavior.

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Manage individual Pods as permanent servers.  
  **Best practice:** use controllers.

- **Mistake:** Hardcode Pod IPs.  
  **Best practice:** Services and DNS.

- **Mistake:** `localhost` for another Pod.  
  **Best practice:** Service DNS.

- **Mistake:** Treat Running as healthy.  
  **Best practice:** readiness/liveness/startup probes.

- **Mistake:** No resource requests.  
  **Best practice:** size requests from real usage.

- **Mistake:** Huge CPU/memory limits without measurement.  
  **Best practice:** balance utilization and safety.

- **Mistake:** Put secrets directly into Git YAML.  
  **Best practice:** protected secret workflow/external secret manager.

- **Mistake:** Assume Secret base64 is encryption.  
  **Best practice:** RBAC + etcd encryption + external KMS/secret controls.

- **Mistake:** Publish database externally.  
  **Best practice:** internal Service/network policy.

- **Mistake:** Use privileged/hostPath to solve normal permissions.  
  **Best practice:** least privilege.

- **Mistake:** Deploy without rollback path.  
  **Best practice:** rollout status/history and immutable images.

- **Mistake:** Use strict liveness dependent on database.  
  **Best practice:** separate liveness from readiness.

- **Mistake:** Write directly to container filesystem for durable data.  
  **Best practice:** PVC or external data service.

- **Mistake:** Treat namespace alone as strong security isolation.  
  **Best practice:** RBAC, policy, network controls, quotas, Pod security.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Kubernetes core operating model?

**Answer:** Declarative desired state plus reconciliation controllers.

### Q2. Control-plane components?

**Answer:** API server, etcd, scheduler, controller manager; cloud integrations may add cloud-controller-manager.

### Q3. Node components?

**Answer:** kubelet, container runtime, kube-proxy/networking components.

### Q4. Smallest schedulable unit?

**Answer:** Pod.

### Q5. `spec` vs `status`?

**Answer:** Desired state vs observed state.

### Q6. Deployment manages?

**Answer:** ReplicaSets that manage Pods.

### Q7. Service purpose?

**Answer:** Stable network identity/load-balancing abstraction for dynamic Pod endpoints.

### Q8. Default Service type?

**Answer:** ClusterIP.

### Q9. EndpointSlice?

**Answer:** Scalable representation of Service backend endpoints.

### Q10. Core cluster DNS commonly?

**Answer:** CoreDNS.

### Q11. Ingress requires?

**Answer:** An Ingress controller.

### Q12. Gateway API?

**Answer:** Modern role-oriented service-networking API with GatewayClass/Gateway/Routes.

### Q13. ConfigMap?

**Answer:** Non-secret configuration.

### Q14. Secret base64 means encrypted?

**Answer:** No.

### Q15. Liveness?

**Answer:** Whether container should be restarted.

### Q16. Readiness?

**Answer:** Whether Pod should receive traffic.

### Q17. Startup probe?

**Answer:** Protects slow startup before liveness takes effect.

### Q18. Request?

**Answer:** Resource amount used for scheduling/planning.

### Q19. Limit?

**Answer:** Maximum resource constraint.

### Q20. Memory over limit?

**Answer:** Can cause OOM kill.

### Q21. CPU over limit?

**Answer:** Usually throttling.

### Q22. QoS classes?

**Answer:** Guaranteed, Burstable, BestEffort.

### Q23. PVC?

**Answer:** Namespaced request for persistent storage.

### Q24. StorageClass?

**Answer:** Defines dynamic storage provisioning class/parameters.

### Q25. StatefulSet?

**Answer:** Controller for workloads needing stable identity/storage/ordered behavior.

### Q26. DaemonSet?

**Answer:** Runs Pods on matching Nodes.

### Q27. Job?

**Answer:** Runs work to completion.

### Q28. CronJob?

**Answer:** Schedules Jobs.

### Q29. ServiceAccount?

**Answer:** Kubernetes workload identity.

### Q30. RBAC objects?

**Answer:** Role/ClusterRole and RoleBinding/ClusterRoleBinding.

### Q31. Taint vs toleration?

**Answer:** Taint repels Pods; toleration permits matching Pod to schedule/remain.

### Q32. HPA?

**Answer:** Scales replicas based on metrics.

### Q33. Helm?

**Answer:** Kubernetes package/template/release manager.

### Q34. Kustomize?

**Answer:** Declarative YAML overlays/patching without template syntax.

### Q35. First steps for Pod failure?

**Answer:** `get`, `describe`, `logs`, `events`, inspect spec/status.

---

# Expanded Self-Assessment Bank — Kubernetes Fundamentals

### Q1. What is the key engineering lesson from **API Object Lifecycle**?

**Answer:** Verify both API acceptance and reconciled runtime state.

### Q2. What is the key engineering lesson from **Desired State vs Observed State**?

**Answer:** Treat status conditions as controller evidence, not decorative metadata.

### Q3. What is the key engineering lesson from **Generation and ObservedGeneration**?

**Answer:** Use generation checks when debugging slow or stuck controllers.

### Q4. What is the key engineering lesson from **resourceVersion and Optimistic Concurrency**?

**Answer:** Do not build business logic around numeric ordering of resourceVersion.

### Q5. What is the key engineering lesson from **Finalizers**?

**Answer:** Investigate the controller and dependent infrastructure before manually removing finalizers.

### Q6. What is the key engineering lesson from **Owner References**?

**Answer:** Operate the highest-level controller that expresses intent.

### Q7. What is the key engineering lesson from **Server-Side Apply Field Ownership**?

**Answer:** Give each automation system clear field ownership.

### Q8. What is the key engineering lesson from **kubectl Diff as Change Review**?

**Answer:** Use diff plus context/namespace verification before production writes.

### Q9. What is the key engineering lesson from **Server Dry-Run**?

**Answer:** Use server dry-run when admission policy matters.

### Q10. What is the key engineering lesson from **kubectl Explain as Schema Discovery**?

**Answer:** Prefer schema discovery over copying old manifests from blogs.

### Q11. What is the key engineering lesson from **Namespace Boundary**?

**Answer:** Combine namespaces with RBAC, quotas, Pod security, and network policy.

### Q12. What is the key engineering lesson from **Labels as Control Inputs**?

**Answer:** Treat selector-driving labels as API contract.

### Q13. What is the key engineering lesson from **Recommended Label Taxonomy**?

**Answer:** Standardize labels centrally and avoid ad hoc synonyms.

### Q14. What is the key engineering lesson from **Annotations for Non-Selector Metadata**?

**Answer:** Keep large/unstructured data out of labels when it is not used for selection.

### Q15. What is the key engineering lesson from **Pod Sandbox Mental Model**?

**Answer:** Use one Pod only for tightly coupled lifecycle/network requirements.

### Q16. What is the key engineering lesson from **Pod Conditions**?

**Answer:** Use conditions before assuming `Running` means healthy.

### Q17. What is the key engineering lesson from **Container State and LastState**?

**Answer:** Correlate lastState with `kubectl logs --previous`.

### Q18. What is the key engineering lesson from **Image Digest Runtime Evidence**?

**Answer:** Record imageID during incidents and deployments.

### Q19. What is the key engineering lesson from **Init Container Contract**?

**Answer:** Avoid embedding long-running business workflows in init containers.

### Q20. What is the key engineering lesson from **Native Sidecar Semantics**?

**Answer:** Use sidecars only when tight Pod-level lifecycle coupling is needed.

### Q21. What is the key engineering lesson from **Ephemeral Debug Container**?

**Answer:** Use ephemeral debugging instead of shipping shells/tools in every production image.

### Q22. What is the key engineering lesson from **Termination Grace Sequence**?

**Answer:** Set terminationGracePeriodSeconds from measured drain requirements.

### Q23. What is the key engineering lesson from **preStop Timing**?

**Answer:** Prefer the application to handle SIGTERM directly when possible.

### Q24. What is the key engineering lesson from **Liveness Scope**?

**Answer:** Keep liveness local and conservative.

### Q25. What is the key engineering lesson from **Readiness Scope**?

**Answer:** Use readiness to protect users from partially initialized or dependency-broken instances.

### Q26. What is the key engineering lesson from **Startup Probe**?

**Answer:** Use startup probes instead of extreme liveness initial delays for slow apps.

### Q27. What is the key engineering lesson from **Probe Budget Math**?

**Answer:** Tune probes from failure-detection and recovery objectives.

### Q28. What is the key engineering lesson from **Deployment Rollout Capacity**?

**Answer:** Capacity-plan rollout surge before production deployment.

### Q29. What is the key engineering lesson from **Deployment Availability Condition**?

**Answer:** Watch controller conditions, not only Pod phase.

### Q30. What is the key engineering lesson from **ProgressDeadlineSeconds**?

**Answer:** Connect rollout failure to explicit rollback automation/runbooks.

### Q31. What is the key engineering lesson from **Revision History and Rollback**?

**Answer:** Pair application rollback with expand/contract schema practices.

### Q32. What is the key engineering lesson from **Recreate Strategy**?

**Answer:** Choose Recreate only from an explicit exclusivity requirement.

### Q33. What is the key engineering lesson from **StatefulSet Identity**?

**Answer:** Use an operator/application protocol for database HA, not StatefulSet alone.

### Q34. What is the key engineering lesson from **StatefulSet Ordered vs Parallel Management**?

**Answer:** Use ordered behavior only when the application genuinely depends on ordinal sequencing.

### Q35. What is the key engineering lesson from **Headless Service Discovery**?

**Answer:** Use headless Services when clients need direct replica identity.

### Q36. What is the key engineering lesson from **Job Completion Semantics**?

**Answer:** Make Job actions idempotent or checkpointed before allowing retries.

### Q37. What is the key engineering lesson from **Indexed Jobs**?

**Answer:** Use indexed Jobs for deterministic partitioned batch workloads.

### Q38. What is the key engineering lesson from **CronJob Missed/Overlapping Runs**?

**Answer:** Design CronJobs for duplicate/missed execution scenarios.

### Q39. What is the key engineering lesson from **DaemonSet Node Agent Blast Radius**?

**Answer:** Canary infrastructure DaemonSet changes before broad rollout.

### Q40. What is the key engineering lesson from **Service Virtual IP**?

**Answer:** Debug Service data plane separately from the application listener.

### Q41. What is the key engineering lesson from **EndpointSlice Readiness**?

**Answer:** When a Service has no traffic, inspect EndpointSlices before DNS.

### Q42. What is the key engineering lesson from **Named Ports**?

**Answer:** Use stable named ports for application protocols.

### Q43. What is the key engineering lesson from **ClusterIP vs NodePort vs LoadBalancer**?

**Answer:** Use the narrowest exposure type that meets the requirement.

### Q44. What is the key engineering lesson from **ExternalName Limitations**?

**Answer:** Use ExternalName only when DNS indirection matches protocol expectations.

### Q45. What is the key engineering lesson from **Service Session Affinity**?

**Answer:** Externalize session state instead of depending on stickiness whenever possible.

### Q46. What is the key engineering lesson from **CoreDNS Search Path**?

**Answer:** Use FQDN or namespace-qualified names when cross-namespace ambiguity matters.

### Q47. What is the key engineering lesson from **DNS ndots Behavior**?

**Answer:** Measure DNS behavior before changing cluster-wide resolver settings.

### Q48. What is the key engineering lesson from **Service Selector Failure**?

**Answer:** Debug selector → Pod label → readiness in that order.

### Q49. What is the key engineering lesson from **Ingress Controller Dependency**?

**Answer:** Do not expect Ingress YAML alone to expose traffic.

### Q50. What is the key engineering lesson from **Gateway API Role Separation**?

**Answer:** Use role separation to reduce shared ingress configuration conflicts.

### Q51. What is the key engineering lesson from **Gateway Route Status**?

**Answer:** Read status conditions before changing listener or backend configuration.

### Q52. What is the key engineering lesson from **NetworkPolicy Default Deny**?

**Answer:** Add DNS and required service egress before enabling deny-all in production.

### Q53. What is the key engineering lesson from **NetworkPolicy DNS Allow**?

**Answer:** Treat DNS as an explicit dependency in default-deny designs.

### Q54. What is the key engineering lesson from **NetworkPolicy Namespace Selectors**?

**Answer:** Protect security-significant namespace labels through governance/admission.

### Q55. What is the key engineering lesson from **ConfigMap Env vs Volume Update**?

**Answer:** Use explicit rollout/reload strategy for configuration changes.

### Q56. What is the key engineering lesson from **Secret Encoding vs Encryption**?

**Answer:** Treat Secret read permission as access to plaintext secret material.

### Q57. What is the key engineering lesson from **Projected ServiceAccount Tokens**?

**Answer:** Disable token automount for workloads that do not call the Kubernetes API.

### Q58. What is the key engineering lesson from **Resource Requests as Scheduling Contract**?

**Answer:** Right-size requests from measured workload demand.

### Q59. What is the key engineering lesson from **CPU Limit Throttling**?

**Answer:** Investigate throttling before assuming the application needs more replicas.

### Q60. What is the key engineering lesson from **Memory Limit OOM**?

**Answer:** Size memory for startup, steady state, and peak behavior.

### Q61. What is the key engineering lesson from **QoS Classes**?

**Answer:** Avoid accidental BestEffort for important workloads.

### Q62. What is the key engineering lesson from **Ephemeral Storage Requests**?

**Answer:** Treat node disk as a schedulable/limited resource.

### Q63. What is the key engineering lesson from **emptyDir Medium Memory**?

**Answer:** Use memory-backed emptyDir only for bounded scratch data.

### Q64. What is the key engineering lesson from **NodeSelector Hard Constraint**?

**Answer:** Use nodeSelector only for durable infrastructure capabilities.

### Q65. What is the key engineering lesson from **Node Affinity Required vs Preferred**?

**Answer:** Use preferences for performance/locality and hard rules for true constraints.

### Q66. What is the key engineering lesson from **Taints and Tolerations**?

**Answer:** Combine taints with affinity/selectors for dedicated-node placement.

### Q67. What is the key engineering lesson from **Topology Spread Constraints**?

**Answer:** Design for node/zone failure capacity, not only normal balance.

### Q68. What is the key engineering lesson from **Pod Anti-Affinity Trade-Off**?

**Answer:** Prefer topology spread unless strict separation is required.

### Q69. What is the key engineering lesson from **PVC Binding**?

**Answer:** Troubleshoot PVC before changing the Pod when storage is unbound.

### Q70. What is the key engineering lesson from **WaitForFirstConsumer**?

**Answer:** Use topology-aware binding for zonal block storage.

### Q71. What is the key engineering lesson from **Reclaim Policy**?

**Answer:** Use Retain for data requiring deliberate recovery/cleanup.

### Q72. What is the key engineering lesson from **VolumeSnapshot Is Not Backup**?

**Answer:** Test restore paths rather than equating snapshot creation with backup.

### Q73. What is the key engineering lesson from **ServiceAccount Least Privilege**?

**Answer:** Create one identity per application capability and grant only required verbs/resources.

### Q74. What is the key engineering lesson from **RoleBinding Scope**?

**Answer:** Prefer RoleBinding when access only needs one namespace.

### Q75. What is the key engineering lesson from **kubectl auth can-i**?

**Answer:** Use can-i before changing RBAC.

### Q76. What is the key engineering lesson from **SecurityContext Restricted Baseline**?

**Answer:** Start from restricted posture and add narrow exceptions.

### Q77. What is the key engineering lesson from **Pod Security Admission**?

**Answer:** Roll out PSA with warn/audit before enforce in existing namespaces.

### Q78. What is the key engineering lesson from **HostPath Risk**?

**Answer:** Avoid hostPath for ordinary apps and isolate infrastructure Pods that require it.

### Q79. What is the key engineering lesson from **hostNetwork and hostPID**?

**Answer:** Require a documented infrastructure use case for host namespace access.

### Q80. What is the key engineering lesson from **HPA Control Loop**?

**Answer:** Do not rely on HPA alone for sudden burst absorption.

### Q81. What is the key engineering lesson from **HPA + Requests**?

**Answer:** Define realistic requests before enabling CPU-based HPA.

### Q82. What is the key engineering lesson from **Queue-Length Autoscaling Concept**?

**Answer:** Choose a scaling metric causally related to workload demand.

### Q83. What is the key engineering lesson from **Metrics Server Limits**?

**Answer:** Use Prometheus/managed monitoring for durable metrics and SLOs.

### Q84. What is the key engineering lesson from **Events as Ephemeral Evidence**?

**Answer:** Forward important operational events if longer history is required.

### Q85. What is the key engineering lesson from **Structured Logs and Pod Identity**?

**Answer:** Use immutable image/version fields in logs for incident reconstruction.

### Q86. What is the key engineering lesson from **OpenTelemetry in Kubernetes**?

**Answer:** Instrument the application, not only the cluster.

### Q87. What is the key engineering lesson from **Helm Template vs Release State**?

**Answer:** Do not debug Helm values without inspecting the rendered manifest.

### Q88. What is the key engineering lesson from **Helm Values Schema**?

**Answer:** Use chart schemas for shared production charts.

### Q89. What is the key engineering lesson from **Kustomize Overlay Discipline**?

**Answer:** Keep overlays small and review `kubectl kustomize` output in CI.

### Q90. What is the key engineering lesson from **Immutable Image Promotion**?

**Answer:** Promote digests; change configuration separately.

### Q91. What is the key engineering lesson from **Config Rollout Checksum**?

**Answer:** Make configuration update semantics explicit.

### Q92. What is the key engineering lesson from **GitOps Mental Model**?

**Answer:** Avoid manual changes that conflict with the authoritative Git owner.

### Q93. What is the key engineering lesson from **Admission Policy Preview**?

**Answer:** Convert repeatable review rules into admission policy.

### Q94. What is the key engineering lesson from **Application SLO**?

**Answer:** Use Kubernetes metrics for diagnosis and SLOs for outcome.

### Q95. What is the key engineering lesson from **PodDisruptionBudget Preview**?

**Answer:** Set PDBs from real replica count and failure capacity.

### Q96. What is the key engineering lesson from **Graceful Degradation**?

**Answer:** Design dependency failure semantics before writing probes.

### Q97. What is the key engineering lesson from **Retry Backoff and Jitter**?

**Answer:** Retry only transient failures and cap total retry time.

### Q98. What is the key engineering lesson from **Circuit Breaker Concept**?

**Answer:** Use circuit breaking for remote dependencies where repeated calls amplify incidents.

### Q99. What is the key engineering lesson from **Bulkhead Isolation**?

**Answer:** Partition scarce resources by business criticality.

### Q100. What is the key engineering lesson from **Deployment Canary Concept**?

**Answer:** Define canary success/rollback criteria before rollout.

### Q101. What is the key engineering lesson from **Blue-Green Concept**?

**Answer:** Use immutable labels and tested switch/rollback procedure.

### Q102. What is the key engineering lesson from **Pod Priority Preview**?

**Answer:** Do not mark ordinary apps system-critical.

### Q103. What is the key engineering lesson from **ResourceQuota Preview**?

**Answer:** Use quota to prevent one namespace from exhausting shared cluster capacity.

### Q104. What is the key engineering lesson from **LimitRange Preview**?

**Answer:** Use LimitRange to avoid accidental BestEffort workloads.

### Q105. What is the key engineering lesson from **Node Pressure Awareness**?

**Answer:** Troubleshoot the node when many unrelated Pods fail together.

### Q106. What is the key engineering lesson from **Service Account Token Exposure**?

**Answer:** Remove unused credentials from workloads.

### Q107. What is the key engineering lesson from **ImagePullSecret vs Workload Identity**?

**Answer:** Prefer short-lived identity-based registry auth where available.

### Q108. What is the key engineering lesson from **Debugging Minimal Images**?

**Answer:** Keep debug tooling ephemeral and access-controlled.

### Q109. What is the key engineering lesson from **Pod Pending Diagnostic Tree**?

**Answer:** Read the event message literally before changing resources.

### Q110. What is the key engineering lesson from **CrashLoopBackOff Diagnostic Tree**?

**Answer:** Capture evidence before deleting the Pod.

### Q111. What is the key engineering lesson from **ImagePullBackOff Diagnostic Tree**?

**Answer:** Fix registry/reference cause rather than repeatedly deleting the Pod.

### Q112. What is the key engineering lesson from **Service No Endpoints Diagnostic Tree**?

**Answer:** Debug endpoint production before kube-proxy/CNI.

### Q113. What is the key engineering lesson from **DNS Diagnostic Tree**?

**Answer:** Separate cluster-local DNS from external-upstream DNS.

### Q114. What is the key engineering lesson from **NetworkPolicy Diagnostic Tree**?

**Answer:** Test one allowed and one denied flow after every policy change.

### Q115. What is the key engineering lesson from **PVC Pending Diagnostic Tree**?

**Answer:** Start with the claim and provisioner before changing application YAML.

### Q116. What is the key engineering lesson from **RBAC Forbidden Diagnostic Tree**?

**Answer:** Do not grant cluster-admin to make a single verb work.

### Q117. What is the key engineering lesson from **Context Safety**?

**Answer:** Make context/namespace verification habitual before destructive operations.

### Q118. What is the key engineering lesson from **Evidence-First Troubleshooting**?

**Answer:** Change one layer at a time and preserve the evidence that justified it.

### Q119. What is the key engineering lesson from **Operational Readiness Review**?

**Answer:** Make operational readiness a deployment gate.

## Completion Checklist

- [ ] I understand declarative reconciliation.
- [ ] I understand control-plane/node components.
- [ ] I can read/write Kubernetes YAML.
- [ ] I can use kubectl contexts/namespaces.
- [ ] I understand Pods and lifecycle.
- [ ] I understand init/sidecar/ephemeral containers.
- [ ] I understand labels/selectors/annotations.
- [ ] I can operate Deployments and rollouts.
- [ ] I understand DaemonSets/StatefulSets/Jobs/CronJobs.
- [ ] I understand Services/EndpointSlices/DNS.
- [ ] I understand Ingress/Gateway API fundamentals.
- [ ] I understand ConfigMaps/Secrets.
- [ ] I can configure probes/graceful shutdown.
- [ ] I understand requests/limits/QoS.
- [ ] I understand basic scheduling.
- [ ] I understand PV/PVC/StorageClass/CSI.
- [ ] I understand ServiceAccounts/RBAC.
- [ ] I understand security contexts/Pod Security.
- [ ] I understand NetworkPolicy.
- [ ] I understand HPA/metrics-server.
- [ ] I understand Helm/Kustomize fundamentals.
- [ ] I can troubleshoot common Kubernetes failures.
- [ ] I completed all 45 labs.
- [ ] I completed the Kubernetes Production Fundamentals Platform project.
