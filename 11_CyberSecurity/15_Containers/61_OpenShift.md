# 61. OpenShift

> Phase 15 — Containers

This course completes Phase 15 by moving from upstream Kubernetes administration into **Red Hat OpenShift Container Platform (OCP)**.

The course is intentionally in depth. OpenShift is not treated as "Kubernetes with a web UI." The material explains the additional platform layers that make OpenShift an enterprise application platform:

```text
Kubernetes
+
Red Hat Enterprise Linux CoreOS
+
CRI-O
+
Cluster Operators
+
Cluster Version Operator
+
Machine Config Operator
+
OVN-Kubernetes
+
Ingress / Routes
+
Integrated Registry
+
OAuth / RBAC
+
Security Context Constraints
+
Operator Lifecycle Management
+
Monitoring / Observability
+
Update / Lifecycle Automation
+
Developer Self-Service
+
Red Hat Support Tooling
```

---

# Current Platform Baseline

Current production documentation baseline used for this material:

```text
Red Hat OpenShift Container Platform: 4.22
Current z-stream verified: 4.22.9
4.22.9 advisory date: August 11, 2026
Underlying Kubernetes: 1.35
Container runtime: CRI-O
Node operating system baseline: RHCOS
```

Red Hat's current 4.22 release notes state that OpenShift Container Platform 4.22 uses **Kubernetes 1.35 with CRI-O**. The same release documentation states that OCP 4.22 uses **Red Hat Enterprise Linux CoreOS (RHCOS)** machines for control-plane and compute machines.

Do not confuse the current platform version with the current certification exam baseline.

---

# Current Certification Baseline

The current Red Hat exam is:

```text
Red Hat Certified System Administrator in OpenShift
Exam: EX280
```

Red Hat currently states that **EX280 is based on OpenShift Container Platform 4.18**.

Therefore this course teaches two layers:

```text
Layer 1 — Current OpenShift operations
          OCP 4.22

Layer 2 — EX280 objective compatibility
          OCP 4.18 exam baseline
```

The core administrative concepts overlap strongly, but exam tasks should always be practiced against the exam's stated OpenShift version.

Current EX280 skill areas include:

```text
Manage OpenShift Container Platform
Work with resource manifests
Deploy applications
Manage authentication and authorization
Configure network security
Expose non-HTTP/SNI applications
Enable developer self-service
Manage OpenShift Operators
Configure application security
```

---

# OpenShift Mental Model

Upstream Kubernetes:

```text
Kubernetes API
Controllers
Scheduler
Kubelet
CNI
CSI
```

OpenShift adds an opinionated supported platform:

```text
                         Users / Developers
                         /              \
                    Web Console          oc
                         \              /
                           OpenShift APIs
                                |
                     Kubernetes APIs + APIs
                                |
        +-----------------------+-----------------------+
        |                       |                       |
 Cluster Operators        Platform Operators       User Workloads
        |                       |                       |
        +-----------------------+-----------------------+
                                |
                          RHCOS Nodes
                                |
                              CRI-O
                                |
                              Pods
```

Cluster lifecycle:

```text
ClusterVersion
      ↓
Cluster Version Operator
      ↓
Release Payload
      ↓
Cluster Operators
      ↓
Platform Components
```

Node operating system lifecycle:

```text
MachineConfig
      ↓
Machine Config Operator
      ↓
MachineConfigPool
      ↓
RHCOS Nodes
```

Application exposure:

```text
Internet
   ↓
OpenShift Ingress Controller
   ↓
Route
   ↓
Service
   ↓
Pods
```

Application image lifecycle:

```text
Source
 ↓
Build / CI
 ↓
Image
 ↓
Image Registry
 ↓
ImageStream / image reference
 ↓
Deployment
```

---

## 1. Topic Title

**OpenShift**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain OpenShift architecture and how it extends Kubernetes.
- Explain the relationship among OCP, Kubernetes, RHCOS, CRI-O, and Operators.
- Explain OpenShift Cluster Operators.
- Inspect ClusterVersion and ClusterOperator status.
- Explain the Cluster Version Operator.
- Explain the Machine Config Operator.
- Explain MachineConfigPools.
- Explain RHCOS lifecycle and immutable-node principles.
- Explain OpenShift installation models.
- Distinguish installer-provisioned and user-provisioned infrastructure.
- Explain Assisted and Agent-based installation concepts.
- Use the OpenShift CLI (`oc`) effectively.
- Use the web console for administration and developer workflows.
- Manage OpenShift projects.
- Explain the difference between Project and Kubernetes Namespace.
- Configure project templates, quotas, and LimitRanges.
- Manage users, groups, ServiceAccounts, and RBAC.
- Configure identity-provider concepts.
- Explain OAuth and OIDC integration concepts.
- Use `oc adm policy`.
- Understand Security Context Constraints.
- Understand the relationship between SCC and Kubernetes Pod Security Admission.
- Run ordinary workloads under restrictive OpenShift security defaults.
- Troubleshoot UID, SELinux, capability, and SCC failures.
- Explain OpenShift Routes.
- Configure edge, passthrough, and re-encrypt TLS routes.
- Understand wildcard routes and route admission.
- Explain OpenShift Ingress Controller architecture.
- Expose HTTP/SNI and non-HTTP applications.
- Understand Service type LoadBalancer and NodePort usage.
- Explain OVN-Kubernetes.
- Configure and troubleshoot NetworkPolicy.
- Understand EgressFirewall and EgressIP concepts.
- Understand secondary networks and Multus.
- Understand Kubernetes NMState in OpenShift.
- Understand SR-IOV at a platform level.
- Manage DNS and ingress-related operators.
- Explain OpenShift image registry architecture.
- Work with ImageStreams and ImageStreamTags.
- Import and inspect images by tag and digest.
- Understand OpenShift BuildConfig.
- Understand Source-to-Image.
- Understand Shipwright-based builds.
- Build applications from source.
- Explain OpenShift Templates and modern alternatives.
- Deploy applications from YAML, Helm, and Kustomize.
- Understand OpenShift Pipelines and GitOps integration.
- Explain Operators and the Operator pattern.
- Use OperatorHub.
- Understand Operator Lifecycle Manager.
- Understand current OLM v1 concepts and the classic OLM model encountered in existing clusters/exam material.
- Install, update, inspect, and uninstall Operators safely.
- Explain OperatorGroups, Subscriptions, InstallPlans, CatalogSources, ClusterServiceVersions, and modern extension concepts.
- Manage persistent storage through StorageClasses, PVCs, and CSI.
- Understand OpenShift Data Foundation conceptually.
- Manage nodes, Machines, MachineSets, and MachineHealthChecks.
- Understand control-plane, worker, infrastructure, and specialized node roles.
- Use labels, taints, tolerations, and node placement.
- Understand MachineConfig and node configuration.
- Understand the Node Tuning Operator.
- Understand cluster and machine autoscaling concepts.
- Configure integrated monitoring concepts.
- Understand Prometheus, Alertmanager, Thanos, and user-workload monitoring.
- Understand OpenShift Logging and Loki-based logging concepts.
- Understand OpenTelemetry and distributed tracing integrations.
- Use Network Observability concepts.
- Inspect events, alerts, ClusterOperators, and cluster health.
- Use `oc debug` and node debugging safely.
- Use `oc adm inspect` and `oc adm must-gather`.
- Understand OpenShift update channels and update graphs.
- Plan and perform OpenShift updates safely.
- Understand Extended Update Support at a conceptual level.
- Understand disconnected/mirrored registry environments and `oc-mirror`.
- Back up and restore OpenShift cluster state conceptually.
- Understand etcd backup/restore in OpenShift.
- Troubleshoot degraded Operators, failed Routes, image pulls, SCC denials, networking, registry, storage, MachineConfig, and updates.
- Prepare for the current EX280 objectives while understanding that the live platform is newer than the exam baseline.
- Design an enterprise OpenShift platform.

---

## 3. Prerequisites

Required:

- 57. Application Containers
- 58. Docker Fundamentals
- 59. Kubernetes Fundamentals
- 60. Kubernetes Administration
- Red Hat Linux administration
- Networking
- Storage fundamentals
- Git
- YAML
- Bash
- Basic PKI and TLS
- Kubernetes RBAC and security contexts

Recommended lab options:

```text
Red Hat Developer Sandbox
OpenShift Local where currently supported
a training-provided OpenShift cluster
an authorized cloud/on-prem OpenShift lab
```

For full cluster-administration exercises, use a disposable or authorized OpenShift environment. Do not experiment with ClusterVersion, MachineConfig, SCC, ingress, or cluster Operators on a production cluster without change control.

Recommended tools:

```text
oc
kubectl
podman
curl
jq
yq
git
helm
```

Verify:

```bash
oc version
oc whoami
oc project
oc get clusterversion
oc get clusteroperators
```

---

## 4. Core Concepts Explanation

# Part 1 — What OpenShift Is

OpenShift Container Platform is Red Hat's enterprise Kubernetes application platform.

It provides Kubernetes APIs plus supported platform services for:

```text
installation
node OS lifecycle
networking
ingress
registry
authentication
security
monitoring
updates
Operators
developer workflows
```

The value is the integrated supported platform, not one isolated feature.

# Part 2 — OpenShift vs Kubernetes

Kubernetes gives core orchestration primitives.

OpenShift adds opinionated supported implementations and APIs.

Example:

```text
Kubernetes Ingress
OpenShift Route

generic CNI
OVN-Kubernetes platform networking

Linux worker
RHCOS-managed node

manual add-ons
Cluster Operators
```

# Part 3 — OpenShift APIs

OpenShift exposes normal Kubernetes resources plus OpenShift-specific resources such as:

```text
Route
Project
ImageStream
BuildConfig
SecurityContextConstraints
ClusterVersion
MachineConfig
MachineConfigPool
```

Some OpenShift features are implemented by Operators and CRDs.

# Part 4 — Current OCP 4.22 Foundation

Current OCP 4.22 uses:

```text
Kubernetes 1.35
CRI-O
RHCOS
```

Treat these as a validated platform combination rather than independently upgrading components.

# Part 5 — CRI-O

CRI-O is the OpenShift container runtime.

Flow:

```text
kubelet
 ↓ CRI
CRI-O
 ↓ OCI runtime
Linux container
```

Administrators should troubleshoot CRI-O rather than expecting Docker Engine on nodes.

# Part 6 — RHCOS

Red Hat Enterprise Linux CoreOS is the purpose-built operating system used by modern OpenShift nodes.

It is managed declaratively as part of the cluster.

Avoid ad hoc package/manual node changes.

# Part 7 — Immutable Node Principle

OpenShift node configuration should come from supported cluster mechanisms:

```text
MachineConfig
Operators
supported node configuration APIs
```

not repeated SSH edits.

The objective is reproducible node state.

# Part 8 — Cluster Operator

Cluster Operators manage major platform components.

Examples include operators for:

```text
authentication
network
DNS
ingress
image registry
kube-apiserver
monitoring
machine configuration
```

# Part 9 — Inspect Cluster Operators

```bash
oc get clusteroperators
```

Key conditions:

```text
Available
Progressing
Degraded
Upgradeable
```

# Part 10 — Available Condition

`Available=True` generally means the Operator's managed component is operational according to its health criteria.

Always inspect detailed message when status is unexpected.

# Part 11 — Progressing Condition

`Progressing=True` can mean:

```text
upgrade
rollout
reconciliation
configuration change
```

It is not automatically an error.

# Part 12 — Degraded Condition

`Degraded=True` indicates the Operator detected a problem.

Inspect:

```bash
oc describe clusteroperator NAME
```

and the Operator's namespace/logs.

# Part 13 — Upgradeable Condition

`Upgradeable=False` can block or warn against cluster update because a component/precondition is incompatible.

Resolve before forcing updates.

# Part 14 — ClusterVersion

ClusterVersion represents OpenShift release state.

```bash
oc get clusterversion
oc describe clusterversion version
```

It shows desired/current versions and update history.

# Part 15 — Cluster Version Operator

CVO manages the OpenShift release payload.

```text
release image
 ↓
CVO
 ↓
manifests/components
 ↓
Cluster Operators
```

Do not manually version individual core components outside supported lifecycle.

# Part 16 — Release Payload

An OpenShift release is distributed as a versioned payload containing component images/manifests.

This creates a tested platform composition.

# Part 17 — Payload Digest

Release payloads are content-addressed/signature-verified in supported update processes.

Cluster upgrades consume validated release images rather than random component versions.

# Part 18 — Machine Config Operator

MCO manages operating-system and node-level configuration.

Examples:

```text
files
systemd units
kernel arguments
CRI-O configuration
OS updates
```

through MachineConfig and related APIs.

# Part 19 — MachineConfig

Declarative node configuration object.

A MachineConfig can define Ignition-formatted changes such as:

```text
files
systemd
kernel arguments
users in limited supported scenarios
```

# Part 20 — MachineConfigPool

Groups nodes that should receive a rendered machine configuration.

Common pools:

```text
master
worker
```

custom pools can support specialized nodes.

# Part 21 — Rendered MachineConfig

MCO merges applicable MachineConfigs into rendered configuration.

```text
00-base
+ custom config
+ operator config
→ rendered-worker-...
```

# Part 22 — MCP Update

Applying MachineConfig can cause:

```text
drain
node reboot
configuration apply
uncordon
next node
```

depending on change.

Plan cluster capacity before MCO changes.

# Part 23 — MCP Status

```bash
oc get mcp
oc describe mcp worker
```

Important:

```text
UPDATED
UPDATING
DEGRADED
machine counts
```

# Part 24 — Machine Config Degraded

A degraded pool can block cluster updates.

Investigate:

```text
MCO/MCD logs
node state
rendered config
filesystem drift
reboot
```

# Part 25 — Machine Config Daemon

Runs on nodes and applies rendered machine configuration.

Manual node drift can cause MCD validation/degradation.

# Part 26 — Machine Config Server

Supports early node provisioning/bootstrapping by serving Ignition configuration in installation architecture.

# Part 27 — Operators Everywhere

OpenShift follows Operator model for platform lifecycle.

Instead of:

```text
manually edit component Deployment
```

you typically configure:

```text
Operator API / custom resource
```

and let Operator reconcile implementation.

# Part 28 — Operator-Owned Resources

Do not edit lower-level resources if Operator will revert them.

Find source of truth:

```text
IngressController
Network
ImageRegistry
Console
APIServer
```

rather than editing generated Deployment directly.

# Part 29 — Platform Namespaces

OpenShift system namespaces commonly use:

```text
openshift-*
```

Examples:

```text
openshift-ingress
openshift-monitoring
openshift-authentication
openshift-image-registry
openshift-machine-config-operator
```

# Part 30 — kube-system vs openshift-*

Core Kubernetes components may exist in `kube-system`, while OpenShift platform operators/components use OpenShift namespaces.

Do not assume all platform Pods are in one namespace.

# Part 31 — Infrastructure Nodes

Organizations can dedicate worker-class nodes for platform workloads such as:

```text
ingress
registry
monitoring
logging
```

using labels/taints/placement.

This separates application and platform capacity.

# Part 32 — Control Plane Nodes

Control-plane nodes run Kubernetes/OpenShift control plane and etcd.

Ordinary application workloads are generally kept off them.

# Part 33 — Worker Nodes

Run normal application workloads.

Worker configuration is managed through machine/node APIs rather than unmanaged host configuration.

# Part 34 — OpenShift Editions Concept

Red Hat provides self-managed and managed OpenShift offerings.

Core administration concepts apply across:

```text
OpenShift Container Platform
ROSA
Azure Red Hat OpenShift
OpenShift Dedicated
```

but customer/provider responsibilities differ.

# Part 35 — Self-Managed Responsibility

With OCP you may own:

```text
installation
infra
control plane
nodes
updates
backup
network
storage
```

depending on hosting model.

# Part 36 — Managed Service Responsibility

Managed offerings shift parts of:

```text
control-plane operations
updates
infrastructure
support
```

to provider/Red Hat.

Application, RBAC, network policy, and workload security still matter.

# Part 37 — OpenShift Web Console

Provides Administrator and Developer perspectives for:

```text
cluster status
workloads
Operators
storage
network
builds
topology
monitoring
```

The CLI remains essential for automation/troubleshooting.

# Part 38 — Developer Perspective

Focuses on application workflows:

```text
add application
topology
build/deploy
routes
logs
metrics
```

# Part 39 — Administrator Perspective

Focuses on:

```text
cluster operators
nodes
machines
networking
storage
users
updates
Operators
monitoring
```

# Part 40 — OpenShift Platform Mental Model

OpenShift is Kubernetes operated by a hierarchy of **platform Operators**.

Before editing anything, ask:

```text
Which Operator owns this component?
Which custom resource is its source of truth?
```

# Part 41 — Installation Program

`openshift-install` creates installation assets and drives supported cluster installation workflows.

Installation method depends on platform and infrastructure ownership.

# Part 42 — Installer-Provisioned Infrastructure

IPI:

```text
installer creates cloud/infrastructure resources
+
installs OpenShift
```

Simplifies supported platforms where permissions allow.

# Part 43 — User-Provisioned Infrastructure

UPI:

```text
administrator provisions infrastructure
installer-generated assets/bootstrap install cluster
```

Used where infrastructure must be created separately/customized.

# Part 44 — Assisted Installer

Guided service/workflow for discovering hosts, validating prerequisites, and installing OpenShift.

Common in bare-metal/on-prem environments.

# Part 45 — Agent-Based Installer

Creates bootable/disconnected-friendly assets for agent-based cluster discovery and installation.

Useful for constrained or disconnected environments.

# Part 46 — Bootstrap Node

During classic installation:

```text
bootstrap
 ↓
temporary control-plane bootstrap
 ↓
control-plane becomes self-hosted
 ↓
bootstrap removed
```

# Part 47 — Bootstrap Complete

Never remove bootstrap infrastructure until installer reports bootstrap completion and control plane has taken over required services.

# Part 48 — install-config.yaml

Defines installation intent:

```text
baseDomain
metadata.name
platform
networking
controlPlane
compute
pullSecret
sshKey
```

structure depends on platform/version.

# Part 49 — Pull Secret

Installation pull secret enables access to required Red Hat registries/services.

Treat it as sensitive credential.

# Part 50 — Cluster ID and DNS

OpenShift installation depends heavily on:

```text
API DNS
API-int DNS
apps wildcard DNS
load balancers
node DNS
```

Incorrect DNS is a major install failure source.

# Part 51 — API DNS

Typical:

```text
api.<cluster>.<baseDomain>
```

points to control-plane API load balancer.

# Part 52 — Apps Wildcard DNS

Typical:

```text
*.apps.<cluster>.<baseDomain>
```

routes application hostnames to ingress.

# Part 53 — API Load Balancer

Balances:

```text
TCP 6443
```

to control-plane API endpoints.

Bootstrap participates during installation where architecture requires.

# Part 54 — Ingress Load Balancer

Routes:

```text
80
443
```

to OpenShift ingress router nodes/endpoints.

Architecture varies by platform.

# Part 55 — RHCOS Ignition

RHCOS nodes consume Ignition configuration at first boot.

Installation/MCO workflows create desired OS configuration.

Do not hand-edit ignition-generated state after cluster is established.

# Part 56 — Installation Validation

Use installer logs plus:

```text
DNS
load balancers
host reachability
bootstrap journal
control-plane journal
certificate/time
```

when installation stalls.

# Part 57 — Installer Log Levels

Run installation with appropriate log level to capture diagnostic details.

Preserve logs before destroying failed installation.

# Part 58 — Cluster Completion

Installation success should be followed by:

```bash
oc get nodes
oc get co
oc get clusterversion
```

plus application/route/storage smoke tests.

# Part 59 — Day 2 Operations

After install configure:

```text
identity provider
RBAC
storage
ingress
registry
monitoring
logging
node roles
quotas
backup
updates
```

# Part 60 — kubeadmin

Installer may provide temporary `kubeadmin` administrative account.

After configuring durable identity provider and admin access, remove temporary kubeadmin according to Red Hat guidance.

# Part 61 — Cluster Update Service

OpenShift uses update graph/channel to identify supported upgrade paths.

CVO performs cluster update.

# Part 62 — Update Channel

Channels represent release streams.

Examples vary by version/lifecycle:

```text
stable
fast
candidate
EUS-related paths
```

Use support policy appropriate to production.

# Part 63 — Update Graph

Not every version can update directly to every later version.

The graph accounts for supported upgrade edges and known risks.

# Part 64 — Check Available Updates

```bash
oc adm upgrade
oc get clusterversion
```

shows available/recommended state according to connected update service and cluster conditions.

# Part 65 — Update Preconditions

Before upgrade:

```text
all ClusterOperators healthy
MCP updated
no blocking Upgradeable=False
backup
capacity
deprecated API/add-on compatibility
release notes
```

# Part 66 — OpenShift Update Scope

Cluster update can update:

```text
Kubernetes/OpenShift control plane
Operators
RHCOS
CRI-O
platform components
```

as an integrated payload.

# Part 67 — Update Progress

Monitor:

```bash
oc get clusterversion
oc get clusteroperators
oc get mcp
```

Do not panic because Operators temporarily show Progressing.

# Part 68 — Update Failure

Find first degraded component.

```text
ClusterVersion history
ClusterOperator message
MCP
events/logs
```

Avoid forcing through without support rationale.

# Part 69 — EUS Concept

Even-numbered OpenShift releases have Extended Update Support under Red Hat lifecycle policy.

Current 4.22 is an even-numbered release; exact entitlement/lifecycle dates should be checked against the current product lifecycle.

# Part 70 — Lifecycle Planning

Enterprise policy should track:

```text
OCP minor
z-stream
EUS status
add-on compatibility
upgrade deadline
maintenance windows
```

# Part 71 — Disconnected Cluster

No direct Internet registry/update access.

Requires mirrors for:

```text
OpenShift releases
Operators/catalogs
application images
Helm/artifacts as needed
```

# Part 72 — oc-mirror

OpenShift mirroring tool helps mirror release and Operator content into disconnected registries.

Current implementation/version behavior changes across releases; use 4.22 docs for live environments.

# Part 73 — Mirror Registry

Internal registry must provide:

```text
TLS
capacity
availability
access control
backup
DNS
```

because cluster lifecycle depends on it.

# Part 74 — ImageDigestMirrorSet Concept

OpenShift APIs can redirect image digest sources toward mirrors.

Use current mirror configuration APIs rather than obsolete ImageContentSourcePolicy-only tutorials.

# Part 75 — ImageTagMirrorSet Concept

Can support tag-based mirror behavior where applicable.

Digest pinning remains stronger for immutable platform content.

# Part 76 — Disconnected Update

Workflow:

```text
mirror target release
verify content
configure mirror
update cluster to mirrored release
monitor CVO/operators
```

# Part 77 — Backup Before Update

Capture:

```text
etcd backup
cluster configuration
critical application data
update baseline
```

according to DR policy.

# Part 78 — Update Is Not App Backup

CVO protects/reconciles platform desired state; it does not back up application databases/PVC data.

Application backup remains separate.

# Part 79 — Supportability

OpenShift support assumes supported configurations and documented upgrade paths.

Unsupported manual changes can make incidents harder to resolve.

# Part 80 — Lifecycle Mental Model

OpenShift lifecycle is **release-payload driven**:

```text
tested release
→ CVO
→ Operators
→ node OS/runtime
```

rather than independent package upgrades.

# Part 81 — oc CLI

`oc` includes Kubernetes-compatible commands plus OpenShift-specific features.

Red Hat describes `oc` as supporting development, build, deployment, application runtime, and administrative commands under `oc adm`.

# Part 82 — oc Login

```bash
oc login https://api.cluster.example:6443
```

authenticate with configured cluster identity.

Avoid storing tokens in unsafe shell history/scripts.

# Part 83 — oc whoami

```bash
oc whoami
oc whoami --show-server
oc whoami --show-token
```

The token output is sensitive.

# Part 84 — oc Project

```bash
oc project
oc project development
```

switches current project/namespace context.

# Part 85 — Project

OpenShift Project is a Kubernetes Namespace plus additional OpenShift metadata/self-service behavior.

It organizes:

```text
resources
access
quota
limits
team ownership
```

# Part 86 — Create Project

```bash
oc new-project orders-dev
```

may invoke project request/template policies.

# Part 87 — Project Request

Non-admin users can be allowed to request projects.

Cluster admin can customize template/default roles/quotas.

# Part 88 — Delete Project

```bash
oc delete project orders-dev
```

deletes namespaced resources.

Treat as high-impact operation.

# Part 89 — Project Finalization

A project stuck Terminating often has:

```text
finalizers
unavailable API extension
Operator cleanup
```

Fix cause instead of blindly removing finalizers.

# Part 90 — Project Template

Administrators can define template used for new projects to apply:

```text
RoleBindings
ResourceQuota
LimitRange
NetworkPolicy
labels
```

# Part 91 — ClusterResourceQuota

OpenShift adds ClusterResourceQuota to apply aggregate quota across selected projects.

Useful across teams/projects.

# Part 92 — ResourceQuota

Namespace/project quota:

```text
CPU
memory
Pods
PVC
Services
object counts
```

# Part 93 — LimitRange

Provides default/min/max requests and limits.

Prevents unbounded BestEffort workloads.

# Part 94 — Developer Self-Service

A good OpenShift platform lets developers create permitted resources without cluster-admin.

Controls:

```text
RBAC
quota
LimitRange
SCC
NetworkPolicy
templates/catalog
```

# Part 95 — oc new-app

Can create application resources from:

```text
image
source repository
template
```

depending on available builders/resources.

Useful for quick developer workflows.

# Part 96 — new-app Result

Always inspect generated objects:

```bash
oc get all
oc describe ...
```

Do not treat `oc new-app` as magic.

# Part 97 — oc expose

Can expose Service through Route:

```bash
oc expose service api
```

then:

```bash
oc get route
```

# Part 98 — oc status

```bash
oc status
```

summarizes project resources and possible warnings.

Useful quick view.

# Part 99 — oc get

Same Kubernetes style:

```bash
oc get pods
oc get deploy
oc get route
oc get is
```

# Part 100 — oc describe

Use for events/status and OpenShift resources:

```bash
oc describe route api
oc describe clusteroperator network
```

# Part 101 — oc explain

```bash
oc explain route.spec
oc explain securitycontextconstraints
```

helps inspect schema.

# Part 102 — oc set

Useful subcommands manipulate:

```text
env
image
resources
volume
probe
```

in workload resources.

# Part 103 — oc set resources

```bash
oc set resources deployment/api \
  --requests=cpu=200m,memory=256Mi \
  --limits=cpu=1,memory=512Mi
```

# Part 104 — oc set probe

Can configure probes from CLI in supported workload forms.

Understand generated YAML and persist in Git.

# Part 105 — oc set volume

Can attach:

```text
PVC
ConfigMap
Secret
emptyDir
```

to workloads.

Review mount/security result.

# Part 106 — oc create route

Provides route-specific CLI:

```bash
oc create route edge ...
oc create route passthrough ...
oc create route reencrypt ...
```

# Part 107 — oc adm

Administrative commands include:

```text
policy
cordon/drain
must-gather
inspect
top
node logs/debug tools
upgrade operations
```

depending on version.

# Part 108 — oc adm policy

Manage RBAC:

```bash
oc adm policy add-role-to-user edit alice -n project
oc adm policy add-cluster-role-to-user cluster-admin admin
```

Use least privilege.

# Part 109 — oc adm groups

Administer groups:

```bash
oc adm groups new developers
oc adm groups add-users developers alice bob
```

where appropriate.

# Part 110 — oc adm top

Quick resource usage:

```bash
oc adm top nodes
oc adm top pods
```

based on monitoring/metrics APIs.

# Part 111 — oc debug

Creates debug Pod/environment to inspect a node/workload.

Node example concept:

```bash
oc debug node/worker1
```

# Part 112 — chroot /host

Inside node debug Pod:

```bash
chroot /host
```

gives host filesystem/process environment access.

This is highly privileged; use only as cluster administrator in authorized troubleshooting.

# Part 113 — Node Debug vs SSH

OpenShift encourages cluster-integrated debug workflows rather than unmanaged SSH.

Node debug is auditable/ephemeral but still privileged.

# Part 114 — oc adm inspect

Collects diagnostic data for specified resources.

Example concept:

```bash
oc adm inspect clusteroperator/network
```

# Part 115 — oc adm must-gather

Collects broad cluster diagnostic information for troubleshooting/support.

```bash
oc adm must-gather
```

May contain sensitive cluster data; protect archive.

# Part 116 — Targeted Must-Gather

Current support tooling can target resources/namespaces to reduce output.

Useful when full cluster gather is large.

# Part 117 — Web Console + CLI

Use console for visualization and CLI for:

```text
repeatability
exact output
automation
fast troubleshooting
```

Strong administrators use both.

# Part 118 — API Compatibility

Because OpenShift builds on Kubernetes, many:

```bash
kubectl
```

commands work, but `oc` understands OpenShift-specific resources/administrative workflows.

# Part 119 — Context Safety

Before write:

```bash
oc whoami
oc whoami --show-server
oc project
```

especially when managing multiple clusters.

# Part 120 — CLI Mental Model

`oc` is your primary operating interface:

```text
read
describe
logs
events
edit/apply
adm
debug
must-gather
```

Always verify source cluster/project first.

# Part 121 — Deployments in OpenShift

Modern OpenShift supports normal Kubernetes Deployment resources.

Prefer Deployment for stateless applications unless an OpenShift-specific workflow requires another controller.

# Part 122 — DeploymentConfig Legacy Context

Older OpenShift clusters/training may include `DeploymentConfig`.

Modern application design generally favors Kubernetes Deployment.

Know DeploymentConfig for legacy/exam environments without choosing it automatically for new apps.

# Part 123 — ImageStream

OpenShift-specific abstraction that tracks image references/tags.

```text
ImageStream
 ├─ :dev
 ├─ :stage
 └─ :prod
```

can decouple workload/build workflows from raw registry path.

# Part 124 — ImageStreamTag

Reference:

```text
orders:1.2
orders:latest
```

within ImageStream.

Tags can point to image digests/imported images.

# Part 125 — ImageStreamImage

Represents a particular image by digest within ImageStream.

Useful for immutable identity.

# Part 126 — Import Image

```bash
oc import-image myapp:latest \
  --from=registry.example/myapp:latest \
  --confirm
```

exact options depend on source/security.

# Part 127 — Image Trigger

OpenShift workflows can trigger builds/deployments based on ImageStream changes.

Understand before changing tags in production.

# Part 128 — Integrated Image Registry

OpenShift includes an image registry managed by Image Registry Operator.

It stores cluster images/build outputs.

# Part 129 — Image Registry Operator

Configure registry through its Operator/custom resource rather than manually editing generated Deployment.

# Part 130 — Registry Storage

Production registry requires persistent/object storage suitable to platform.

Ephemeral storage is not acceptable for durable production image history.

# Part 131 — Registry Route

Internal registry can be exposed externally when required, with TLS/auth controls.

Do not expose by default without need.

# Part 132 — Registry Authentication

Users/service accounts can obtain tokens for registry access.

RBAC controls image push/pull by project/repository.

# Part 133 — Podman Login

Concept:

```bash
podman login \
  -u USER \
  -p "$(oc whoami -t)" \
  REGISTRY
```

Avoid leaking token in process/history; use safer stdin/token handling where supported.

# Part 134 — BuildConfig

OpenShift BuildConfig defines build process.

Strategies historically include:

```text
Source
Docker/Containerfile
Custom
Pipeline legacy context
```

current platform increasingly promotes modern build frameworks.

# Part 135 — Source-to-Image

S2I combines:

```text
application source
+
builder image
↓
runnable application image
```

without developer writing full container build manually.

# Part 136 — S2I Builder Image

Contains:

```text
language runtime
assemble script
run script
```

and conventions for building source.

# Part 137 — Build Trigger

BuildConfig can trigger on:

```text
image change
config change
webhook
manual request
```

depending on configuration.

# Part 138 — Start Build

```bash
oc start-build myapp
oc logs -f build/myapp-1
```

# Part 139 — Build Logs

Troubleshoot:

```text
source clone
builder pull
dependency fetch
permissions
output push
```

# Part 140 — Shipwright Builds

Current OpenShift documentation includes Shipwright-based builds as an extensible modern image build framework.

Concepts differ from legacy BuildConfig; learn both if operating mixed environments.

# Part 141 — Build Security

Builds can access:

```text
source credentials
registry credentials
dependencies
cluster network
```

Treat builder ServiceAccounts and secrets as privileged supply-chain components.

# Part 142 — Binary Build Concept

Can provide local source/binary content to build without Git checkout.

Useful for controlled CI, but reproducibility requires source/version metadata.

# Part 143 — Build Output

Output generally pushes image to:

```text
ImageStream
internal registry
external registry
```

depending on build configuration.

# Part 144 — Template

OpenShift Template parameterizes a set of objects.

Legacy/common exam concept:

```text
parameters
objects
labels
```

Modern teams also use Helm/Kustomize/Operators/GitOps.

# Part 145 — Process Template

```bash
oc process -f template.yaml \
  -p APP_NAME=orders
```

renders objects.

Review before apply.

# Part 146 — Helm on OpenShift

OpenShift supports Helm workflows.

Current OCP 4.22 also offers a supported Helm CLI v4 binary for evaluation/use, while integrated console flows still use Helm v3 at that release.

Know chart compatibility before relying on Helm 4-only features.

# Part 147 — Kustomize

EX280 objectives explicitly include deploying using Kustomize and overlays.

Example:

```bash
oc apply -k overlays/prod
```

# Part 148 — Route

OpenShift Route exposes a Service using hostname.

```text
Client
 ↓
Route hostname
 ↓
Ingress Controller/router
 ↓
Service
 ↓
Pods
```

# Part 149 — Route API

OpenShift-specific:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
```

# Part 150 — Simple Route

```bash
oc expose service api
oc get route api
```

creates default route behavior if ingress domain permits.

# Part 151 — Route Host

Can be generated under cluster apps domain or explicitly specified:

```text
api.apps.cluster.example
```

subject to admission/DNS.

# Part 152 — Edge TLS Termination

TLS terminates at OpenShift router.

```text
Client HTTPS
 ↓ decrypt at router
Router HTTP/HTTPS backend depending config
 ↓
Service
```

# Part 153 — Passthrough TLS

Router uses SNI to select backend but does not terminate TLS.

```text
Client TLS
 ↓
Router
 ↓ unchanged TLS
Pod/backend
```

Backend owns certificate.

# Part 154 — Re-encrypt TLS

```text
Client TLS
 ↓ terminate router
router establishes new TLS
 ↓
backend
```

router validates backend certificate using destination CA.

# Part 155 — Route Certificate

Edge/reencrypt Route can provide:

```text
certificate
private key
CA chain
destination CA
```

depending on termination mode.

# Part 156 — Route Redirect

Insecure traffic policy can:

```text
allow
disable
redirect
```

depending on route configuration.

# Part 157 — Wildcard Route

Can admit wildcard subdomains in supported configuration.

Admin policy may restrict wildcard use.

# Part 158 — Route Admission

Ingress controller/router decides whether Route is admitted.

Inspect:

```bash
oc describe route ROUTE
```

status ingress conditions.

# Part 159 — IngressController Resource

OpenShift Ingress Operator manages routers through `IngressController` resources.

Configure source-of-truth CR rather than generated router Deployment.

# Part 160 — Default IngressController

Usually named:

```text
default
```

in:

```text
openshift-ingress-operator
```

and router workloads run in `openshift-ingress`.

# Part 161 — Ingress Placement

Configure node placement for routers:

```text
nodeSelector
tolerations
replicas
```

to dedicated infra nodes if needed.

# Part 162 — Ingress Domain

Cluster apps domain determines default Route host suffix.

DNS wildcard must resolve to ingress.

# Part 163 — Ingress Certificates

Default ingress certificate can be replaced with trusted custom certificate.

Certificate chain/hostname/rotation must be managed.

# Part 164 — Route 503

Typical causes:

```text
Service no endpoints
Pods not Ready
wrong targetPort
router cannot reach backend
TLS backend error
```

# Part 165 — Route TLS Failure

Check:

```text
termination mode
certificate/key
SNI/host
destination CA
backend certificate
router logs
```

# Part 166 — Non-HTTP Exposure

EX280 includes exposing non-HTTP/SNI applications.

Use supported Service `LoadBalancer` or other network integration rather than HTTP Route when protocol does not fit Route semantics.

# Part 167 — LoadBalancer Service

On supported cloud/on-prem load-balancer integration:

```yaml
type: LoadBalancer
```

provisions/exposes external IP.

# Part 168 — NodePort

Can expose TCP/UDP through node ports, but is low-level and usually placed behind external LB/firewall.

Avoid uncontrolled public NodePort exposure.

# Part 169 — Application Topology

Developer console topology can visualize:

```text
Deployments
Builds
Services
Routes
Pipelines
```

but YAML/API remains source of truth.

# Part 170 — Application Delivery Mental Model

```text
source
→ build
→ image
→ registry/ImageStream
→ Deployment
→ Service
→ Route/LoadBalancer
```

Troubleshoot along this chain.

# Part 171 — OpenShift Authentication

OpenShift includes OAuth-based authentication integration and supports configured identity providers.

Authentication creates user identity; RBAC authorizes actions.

# Part 172 — OAuth Server

OpenShift OAuth integrates identity providers and issues cluster tokens used by `oc`/console.

Current OCP also supports direct external OIDC identity-provider patterns in supported versions.

# Part 173 — Identity Provider Types

Common concepts include:

```text
HTPasswd
LDAP
GitHub/GitLab-like providers
OpenID Connect
external enterprise IdP
```

availability/config details depend on version.

# Part 174 — HTPasswd Provider

Useful for:

```text
labs
small local users
break-glass patterns in limited designs
```

not usually primary enterprise identity source.

# Part 175 — LDAP Integration

Can authenticate/sync enterprise identities/groups.

Plan:

```text
TLS
bind credential
user filter
group sync
mapping
```

# Part 176 — OIDC

Modern enterprise identity federation can use OIDC.

Validate:

```text
issuer
client
audience
claims
groups
CA
```

# Part 177 — User Object

OpenShift User represents authenticated user recognized by cluster.

Identity provider mapping links external identity to user.

# Part 178 — Identity Object

Tracks identity-provider identity linked to User in OAuth model.

Avoid manual changes unless following supported identity management workflow.

# Part 179 — Group

OpenShift/Kubernetes Group can be used in RBAC bindings.

```text
developers
platform-admins
auditors
```

# Part 180 — Group Sync

LDAP/group sync can align cluster groups with external directories.

Automation must handle removals, rename, scope, and least privilege.

# Part 181 — ClusterRole

Built-in examples:

```text
cluster-admin
admin
edit
view
```

Use smallest role needed.

# Part 182 — admin Role

Project-level `admin` manages project resources/access broadly without full cluster admin.

# Part 183 — edit Role

Can create/change most application resources but has important security implications through workload identity/Secrets.

Do not treat as harmless.

# Part 184 — view Role

Read-only application-resource access with restrictions around sensitive data.

Check actual permissions using `oc auth can-i`.

# Part 185 — RoleBinding

Namespaced/project grant:

```bash
oc adm policy add-role-to-user edit alice -n orders
```

# Part 186 — ClusterRoleBinding

Cluster-wide grant.

`cluster-admin` is extremely powerful.

Audit regularly.

# Part 187 — oc auth can-i

```bash
oc auth can-i create routes
oc auth can-i get secrets -n project
```

Can impersonate when authorized.

# Part 188 — ServiceAccount

Workload identity.

OpenShift projects commonly include default service accounts such as:

```text
default
builder
deployer legacy contexts
```

roles evolve by release/workflow.

# Part 189 — Dedicated ServiceAccount

Create one per application privilege boundary.

```bash
oc create sa orders-api
```

then bind only required roles.

# Part 190 — ServiceAccount Token

Modern bound tokens are short-lived/projected.

Avoid old long-lived token Secret patterns.

# Part 191 — SCC

Security Context Constraints are OpenShift-specific controls that determine whether a Pod security configuration is allowed and may apply defaults.

They constrain:

```text
UID
SELinux
privileged
capabilities
host namespaces
host volumes
FSGroup
supplemental groups
```

# Part 192 — SCC Admission

At Pod creation:

```text
requested Pod security context
+
user/service account authorized SCCs
↓
admission evaluates
↓
admitted with selected SCC or rejected
```

# Part 193 — Default SCCs

OpenShift installs default SCCs.

Red Hat explicitly advises **not to modify default SCCs**.

Create custom SCC when necessary because defaults can be reset/relied upon by platform.

# Part 194 — restricted SCC Family

Ordinary apps are intended to run under restrictive SCC behavior.

Design images to tolerate:

```text
arbitrary non-root UID
SELinux
dropped capabilities
no privileged mode
```

# Part 195 — Arbitrary UID

OpenShift commonly assigns Pod an arbitrary UID from project range.

Container image must not require fixed root/user ownership.

Good image pattern:

```text
group-writable application directories
non-root compatible
```

# Part 196 — Why chmod 777 Is Wrong

Arbitrary UID compatibility does not mean world-writable everything.

Prefer:

```text
correct group ownership
g=u permissions where appropriate
read-only image
explicit writable volume
```

# Part 197 — SELinux

OpenShift strongly integrates SELinux confinement.

A Pod can receive MCS/SELinux labels isolating volume/process access.

Unix mode bits alone do not determine access.

# Part 198 — SCC and RBAC

Users/ServiceAccounts gain ability to use SCC through authorization.

Do not broadly grant powerful SCC such as privileged.

# Part 199 — Who Can Use SCC

```bash
oc adm policy who-can use scc/privileged
```

is useful security audit.

# Part 200 — Add SCC to ServiceAccount

Administrative workflows can grant an SCC/use capability to specific ServiceAccount.

Do this only after proving why restrictive SCC cannot support workload.

# Part 201 — Custom SCC

If needed, create a new custom SCC matching narrow requirement.

Never modify default SCC just to satisfy one vendor application.

# Part 202 — SCC Priority

When multiple SCCs are authorized, admission prioritizes according to rules/priority/restrictiveness behavior.

Inspect selected SCC on admitted Pod annotations/status according to version.

# Part 203 — Pod Security Admission

OpenShift also supports Kubernetes Pod Security Admission.

SCC and PSA are related but different controls.

OpenShift automatically manages some namespace labels/synchronization behavior to keep platform compatibility.

# Part 204 — SCC vs PSA

```text
SCC:
OpenShift admission/defaulting + authorization model

PSA:
Kubernetes namespace-level Privileged/Baseline/Restricted standards
```

Do not assume one replaces the other in OpenShift.

# Part 205 — Privilege Escalation

Ordinary apps should use:

```text
allowPrivilegeEscalation=false
drop capabilities
RuntimeDefault seccomp
non-root
```

when compatible.

# Part 206 — Privileged Workload

Some infrastructure Operators legitimately require privileged SCC.

Keep in protected namespace and dedicated ServiceAccount.

# Part 207 — HostPath

SCC can restrict host directory volume access.

Ordinary applications should not mount host filesystem.

# Part 208 — hostNetwork / hostPID

SCC controls access to host namespace features.

Grant only infrastructure workloads that truly require them.

# Part 209 — Seccomp

OpenShift supports seccomp profiles.

Prefer RuntimeDefault or carefully reviewed profiles rather than unconfined.

# Part 210 — Security Profiles Operator

Can manage seccomp/SELinux security profiles in supported workflows.

Useful for advanced workload hardening.

# Part 211 — Compliance Operator

Automates compliance scans/remediation guidance against supported profiles.

Use results as compliance evidence/input, not blind remediation.

# Part 212 — File Integrity Operator

Monitors file integrity on nodes using supported tooling.

Helps detect unexpected host changes.

# Part 213 — External Secrets Operator

Current OpenShift includes Red Hat-supported External Secrets Operator capabilities for integrating external secret stores.

Use workload identity/least privilege.

# Part 214 — cert-manager Operator

Provides automated certificate issuance/lifecycle integrations.

Do not confuse application certs, ingress certs, and platform PKI.

# Part 215 — Cluster PKI

OpenShift manages many internal certificates automatically through Operators.

Manual replacement can conflict with operator reconciliation.

# Part 216 — Ingress Certificates

Custom ingress default certificate is administrator-managed through supported ingress configuration.

Track renewal.

# Part 217 — API Certificate

Custom API serving certificate can be configured through supported API server/ingress mechanisms.

Maintain SAN/chain/rotation.

# Part 218 — Audit Logs

OpenShift exposes Kubernetes/OpenShift API audit logs according to policy.

Use for:

```text
RBAC changes
Secret access
Pod exec
SCC/security changes
```

# Part 219 — Audit Profiles

OpenShift provides configurable audit policy/profile behavior through supported APIs.

Balance visibility and sensitive-data/log volume.

# Part 220 — Network Isolation

Security combines:

```text
SCC/PSA
RBAC
NetworkPolicy
egress controls
node separation
TLS
secret management
```

# Part 221 — Image Security

Control:

```text
trusted registry
image digest
signature/provenance
vulnerability scanning
build identity
```

OpenShift security is not only runtime SCC.

# Part 222 — Image Policy

Cluster image configuration can restrict/allow registries and mirror sources.

Misconfiguration can prevent all image pulls.

# Part 223 — Cluster Admin Separation

Separate:

```text
platform admins
security admins
developer admins
auditors
```

through groups/RBAC rather than shared cluster-admin tokens.

# Part 224 — Break-Glass

Maintain emergency access:

```text
strongly protected
rarely used
audited
tested
```

not daily account.

# Part 225 — OpenShift Security Mental Model

OpenShift security is intentionally restrictive:

```text
arbitrary UID
SELinux
SCC
RBAC
NetworkPolicy
Operator-managed PKI
```

Applications should adapt to platform security rather than disabling it.

# Part 226 — OVN-Kubernetes

Current OpenShift uses OVN-Kubernetes as primary cluster network implementation.

It provides:

```text
Pod networking
Service integration
NetworkPolicy
egress features
network segmentation capabilities
```

# Part 227 — Cluster Network Operator

CNO manages cluster networking components/configuration.

Inspect:

```bash
oc get co network
oc -n openshift-network-operator get pods
```

# Part 228 — Network Configuration

Cluster `Network` configuration defines high-level:

```text
clusterNetwork
serviceNetwork
network type
MTU/migration settings
```

Changing core network after install is high risk.

# Part 229 — ClusterNetwork

Pod address ranges.

Plan with:

```text
node count
Pods per node
on-prem/cloud CIDRs
VPN
secondary networks
```

# Part 230 — ServiceNetwork

Virtual Service IP CIDR(s).

Must not overlap with cluster/node/external ranges.

# Part 231 — OVN Logical Networking

OVN implements logical switches/routers/policies translated into node data plane.

Admins usually operate through OpenShift/Kubernetes APIs rather than manually editing OVN DB.

# Part 232 — NetworkPolicy

Standard Kubernetes NetworkPolicy is enforced by OVN-Kubernetes.

Use default-deny plus explicit flows for sensitive projects.

# Part 233 — Default Deny

Start:

```text
deny ingress
deny egress
allow DNS
allow required application dependencies
```

only after dependency mapping.

# Part 234 — NetworkPolicy Project Boundary

Policies select Pods in a namespace/project.

Namespace selectors allow cross-project rules using trusted labels.

# Part 235 — EgressFirewall

OpenShift-specific egress control can restrict outbound destinations from a namespace/project.

Use for:

```text
deny Internet
allow selected CIDRs/domains where supported
```

behavior depends on OVN feature/version.

# Part 236 — EgressIP

Assign predictable source egress IPs for selected workloads/namespaces.

Useful when external systems allowlist fixed source IP.

# Part 237 — EgressService Concept

OVN-Kubernetes can support stable egress behavior for Service traffic in selected patterns.

Verify current use cases before deployment.

# Part 238 — AdminNetworkPolicy Concept

Newer Kubernetes/OVN network policy capabilities can provide administrator-level policies above tenant NetworkPolicy.

Check current 4.22 support/maturity before production use.

# Part 239 — Multus

OpenShift supports additional Pod network interfaces using Multus.

```text
default OVN network
+
secondary network
```

# Part 240 — NetworkAttachmentDefinition

Defines secondary network attachment.

Pods request through annotations/API.

Examples:

```text
macvlan
bridge
SR-IOV
```

depending on plugins.

# Part 241 — Secondary Network Use Cases

Examples:

```text
telco data plane
storage network
legacy L2 attachment
high-performance network
```

adds routing/security complexity.

# Part 242 — SR-IOV

SR-IOV Network Operator manages high-performance NIC virtual functions and related resources.

Common in telecom/NFV/HPC workloads.

# Part 243 — SR-IOV Security

Direct NIC capabilities reduce abstraction and increase hardware/placement dependency.

Use dedicated nodes and resource policy.

# Part 244 — Kubernetes NMState

NMState Operator manages node network configuration declaratively.

Use for:

```text
bonds
VLANs
bridges
interfaces
routes
```

in supported on-prem scenarios.

# Part 245 — NodeNetworkConfigurationPolicy

Describes desired node network state.

A bad network policy can disconnect nodes; use staged safe changes.

# Part 246 — Ingress Operator

Manages OpenShift ingress controllers/router.

Inspect:

```bash
oc get co ingress
oc -n openshift-ingress-operator get pods
```

# Part 247 — Ingress Controller

OpenShift router implementation commonly uses HAProxy.

Operator manages replicas/configuration/certificates/placement.

# Part 248 — Route Sharding

Multiple IngressControllers can select Routes/namespaces using labels.

Use for:

```text
internal vs external
different certificates
teams
network zones
```

# Part 249 — Internal Ingress

Create ingress controller with internal load balancer/domain for internal-only applications.

DNS/route selectors must align.

# Part 250 — Route Selector

IngressController can select Routes based on labels.

Unselected Route is not admitted by that router.

# Part 251 — Namespace Selector

Ingress controller can select namespaces/projects, enabling tenant/zone separation.

# Part 252 — Router Replicas

Production routers should have enough replicas and node/failure-domain spread.

Capacity depends on connection rate/TLS/traffic.

# Part 253 — Router Metrics

Monitor:

```text
HTTP response codes
connection rates
TLS errors
backend availability
latency
```

# Part 254 — Route Timeouts

Long-running applications might need route-specific timeout annotations/config.

Changing timeout can hide backend design issues; use deliberately.

# Part 255 — Route Whitelisting Concept

Ingress/router annotations can restrict source IP in supported patterns.

Prefer centralized network policy/WAF where requirements are broader.

# Part 256 — DNS Operator

Manages cluster DNS components.

Inspect:

```bash
oc get co dns
```

# Part 257 — DNS Operator Source of Truth

Configure supported DNS API rather than editing CoreDNS/daemon resources directly.

# Part 258 — OpenShift DNS

Internal Service DNS remains Kubernetes/CoreDNS-style.

OpenShift adds operator-managed lifecycle.

# Part 259 — External DNS

ExternalDNS Operator can automate DNS records in supported providers.

Use scoped credentials and ownership markers.

# Part 260 — LoadBalancer Service

Cloud/platform LoadBalancer integration may be managed by cloud controller/network Operators.

Inspect Service events and provider resources.

# Part 261 — MetalLB Operator

On supported bare-metal environments, MetalLB Operator provides LoadBalancer Services through L2/BGP advertisement.

# Part 262 — BGP

MetalLB/advanced OVN integrations may exchange routes using BGP.

Network team must coordinate ASN/peering/prefix policy.

# Part 263 — Ingress Node Firewall Operator

Can manage node-level ingress firewall rules in supported use cases.

This is separate from Pod NetworkPolicy.

# Part 264 — Network Observability Operator

Provides flow-level network visibility.

Use to analyze:

```text
who talks to whom
bytes/packets
DNS/network behavior
policy impact
```

# Part 265 — Flow Collection

Flow telemetry can be large.

Tune:

```text
sampling
retention
storage
tenant access
```

# Part 266 — Network Observability DNS Analysis

Can correlate DNS/network flows to help identify resolution or suspicious traffic patterns in supported configurations.

# Part 267 — Network Troubleshooting

Layer order:

```text
Pod
Service
EndpointSlice
NetworkPolicy
OVN
node
Route/Ingress
external LB
DNS
```

# Part 268 — Pod-to-Pod Failure

Check:

```text
same/cross node?
Pod IP
policy
OVN node
MTU
routes
```

# Part 269 — Service Failure

Check:

```bash
oc get svc
oc get endpointslices
oc get pods -o wide
```

then test Pod IP directly.

# Part 270 — Route Failure

Check:

```text
Route admitted?
router?
Service endpoints?
backend readiness?
TLS?
DNS?
```

# Part 271 — DNS Failure

Check:

```text
Pod resolv.conf
DNS Operator
DNS Pods
Service
NetworkPolicy
upstream resolver
```

# Part 272 — OVN Node Failure

If one Node's Pods lose network:

```text
ovnkube node components
node interfaces/routes
MTU
OVS/OVN health
CNO
```

# Part 273 — CNO Degraded

`network` ClusterOperator Degraded is high priority because new/ongoing networking can fail.

Inspect operator condition message first.

# Part 274 — Multiple Networks Failure

Secondary-network Pod failure:

```text
NAD
Multus
plugin binary/config
device resource
node interface
IPAM
```

# Part 275 — SR-IOV Scheduling

Pod needs resource exposed by device plugin.

If unavailable:

```text
Pending insufficient resource
```

or attachment error.

# Part 276 — NMState Failure

Inspect policy/enactment status.

Never apply wide node-network changes without rollback/out-of-band access plan.

# Part 277 — Network MTU

Cloud/VLAN/VXLAN/Geneve overhead can create path MTU issues.

Symptoms:

```text
small packets work
large TLS hangs
```

# Part 278 — North-South Traffic

External ↔ cluster:

```text
DNS
LB
Ingress
Route
Service
Pod
```

# Part 279 — East-West Traffic

Within cluster:

```text
Pod
OVN
NetworkPolicy
Service
Pod
```

# Part 280 — Egress Traffic

```text
Pod
OVN policy
egress IP/NAT
node/cloud firewall
external service
```

# Part 281 — Network Segmentation Design

Separate:

```text
tenant projects
platform namespaces
infra nodes
external/internal ingress
egress policy
secondary data networks
```

# Part 282 — Network Runbooks

Maintain runbooks for:

```text
Route 503
DNS failure
OVN degradation
EgressIP failure
NetworkPolicy deny
LoadBalancer pending
```

# Part 283 — Packet Capture

Use `oc debug node` + authorized node tools when needed.

Protect payload data and minimize capture scope.

# Part 284 — Network Change Safety

Changes to:

```text
clusterNetwork
MTU
node routes
NMState
Ingress LB
```

have large blast radius.

Use staged supported procedures.

# Part 285 — OpenShift Networking Mental Model

OpenShift networking is:

```text
OVN-Kubernetes
+
Operators
+
Routes/Ingress
+
NetworkPolicy
+
egress controls
+
secondary networks
+
external infrastructure
```

# Part 286 — Operator Pattern

An Operator encodes domain-specific operational knowledge into Kubernetes controllers.

It can automate:

```text
install
configure
upgrade
backup
failover
scale
```

# Part 287 — OperatorHub

OpenShift console/catalog experience for discovering installable Operators from configured catalogs.

# Part 288 — OLM

Operator Lifecycle Manager manages Operator installation/update/lifecycle.

OpenShift 4.22 documentation includes current **OLM v1 extensions** alongside established Operator workflows.

# Part 289 — Why Learn Classic OLM

Existing OpenShift clusters and EX280 4.18 material commonly use classic OLM resources:

```text
CatalogSource
Subscription
InstallPlan
ClusterServiceVersion
OperatorGroup
```

You need these operationally even as newer OLM evolves.

# Part 290 — CatalogSource

Classic OLM resource pointing to Operator catalog content.

Catalog health affects installation/update resolution.

# Part 291 — OperatorGroup

Defines Operator installation/target namespace scope.

An Operator's supported install modes must match target scope.

# Part 292 — Subscription

Declares desired Operator/channel/source.

OLM resolves install/update.

# Part 293 — Channel

Operator channels represent update streams such as:

```text
stable
fast
version-specific
```

names vary by Operator.

# Part 294 — InstallPlan

Resolved set of resources to install/upgrade Operator.

Approval can be:

```text
Automatic
Manual
```

# Part 295 — Manual Approval

Provides change-control checkpoint.

```text
new update available
↓
InstallPlan Pending approval
↓
admin reviews
↓
approve
```

# Part 296 — ClusterServiceVersion

Classic OLM CSV describes installed Operator version/metadata/permissions/CRDs/status.

Inspect when Operator install fails.

# Part 297 — CSV Status

Possible phases include success/failure/pending behaviors.

`oc describe csv` reveals missing requirements or permissions.

# Part 298 — Operator Namespace

Operators can install:

```text
single namespace
own namespace
multiple namespaces
all namespaces
```

depending on install mode.

# Part 299 — Operator Permissions

Operator may receive powerful cluster roles.

Review:

```text
ServiceAccount
Roles
ClusterRoles
CRDs
webhooks
SCC
```

before installation.

# Part 300 — Operator CRD

Operator often creates CRD defining managed application.

Example:

```text
DatabaseCluster
LokiStack
Pipeline
```

# Part 301 — Operator Custom Resource

User creates CR:

```text
desired app config
```

Operator reconciles lower-level resources.

# Part 302 — Operator Upgrade

Review:

```text
channel
version
InstallPlan
CRD conversion
breaking changes
operand version
backup
```

# Part 303 — Operand

The actual software managed by Operator.

Operator version and operand version may differ.

# Part 304 — Operator Uninstall

Uninstalling Operator may not delete custom resources/data automatically.

Read product uninstall procedure.

# Part 305 — CRD Deletion Risk

Deleting CRD deletes API representation of all custom resources and can orphan/destroy managed state.

Never delete just to "clean up."

# Part 306 — Subscription Troubleshooting

Check:

```text
CatalogSource healthy
channel exists
package
Subscription status
InstallPlan
CSV
resolution errors
```

# Part 307 — Catalog Troubleshooting

If catalog unavailable:

```text
catalog Pod
registry image
network/DNS
certificate
proxy
disk
```

# Part 308 — Dependency Resolution

OLM resolves required packages/version constraints.

Conflicts can block upgrades/install.

# Part 309 — OLM v1 Concept

Current OpenShift extends lifecycle management through newer OLM v1 APIs/extension model.

Treat it as an evolving modern path and follow 4.22 docs when implementing.

# Part 310 — OLM v1 vs Classic

Do not assume classic objects map one-to-one.

Operational teams need migration/version awareness and should know which lifecycle system a specific Operator uses.

# Part 311 — Cluster Operator vs Installed Operator

Cluster Operator:

```text
core OpenShift platform component managed as part of release
```

Installed Operator:

```text
optional/additional lifecycle-managed application/operator
```

Do not confuse them.

# Part 312 — Operator Status

For installed Operator inspect:

```text
Subscription/extension
CSV if classic
Operator Pods
CR status
events
logs
```

# Part 313 — Operator Health vs Operand Health

Operator Pod can be Running while managed database/application is degraded.

Inspect custom resource conditions.

# Part 314 — Operator Webhooks

Operators often install admission/conversion webhooks.

Certificate/service outage can block API requests.

# Part 315 — Operator SCC

Some Operators install custom SCCs.

Red Hat docs note additional SCCs might be installed by Operators/components.

Review privilege.

# Part 316 — Operator Upgrade Blast Radius

An Operator controlling all namespaces/storage/networking can have cluster-wide impact.

Use manual approval/change windows when appropriate.

# Part 317 — OperatorHub Security

Restrict which catalogs/operators are available in regulated clusters.

Third-party Operator is privileged software supply chain.

# Part 318 — Disconnected Operator Catalog

Mirror catalog/index/operator images into internal registry.

Update CatalogSource/modern catalog configuration accordingly.

# Part 319 — Operator Licensing

Catalog availability does not automatically mean no commercial license/subscription requirement.

Review vendor terms/support.

# Part 320 — Operator Backup

Before upgrading stateful Operator:

```text
managed data backup
CR export
version
Operator configuration
```

# Part 321 — Operator CR Finalizers

Custom resources can stick terminating when Operator unavailable and finalizer cleanup cannot complete.

Restore Operator/controller first when possible.

# Part 322 — Operator Permissions Audit

```bash
oc get clusterrolebindings
oc get clusterroles
oc get scc
```

identify privileged installed Operators.

# Part 323 — Operator Resource Ownership

Do not manually scale/edit Operator-owned Deployments if Operator will reconcile them.

Edit custom resource.

# Part 324 — Operator Upgrade Channel Governance

Pin approved channels and monitor automatic upgrade behavior.

Do not let critical database Operators change unexpectedly.

# Part 325 — OLM Upgrade During OCP Update

Check third-party Operator compatibility before OCP minor upgrade.

An unsupported Operator can block `Upgradeable` or fail after API changes.

# Part 326 — Operator Lifecycle Documentation

For each production Operator record:

```text
owner
catalog/source
channel
version
upgrade policy
backup
CRDs
permissions
support contact
```

# Part 327 — EX280 Operator Scope

Current EX280 objectives explicitly require:

```text
install Operator
uninstall Operator
delete Operator
```

Practice against exam OCP 4.18 lifecycle model.

# Part 328 — Modern OCP Operator Scope

Current 4.22 administrators also need OLM v1 awareness, even if exam environment is older.

# Part 329 — Operator Incident Workflow

```text
CR condition
Operator logs
events
catalog/lifecycle object
RBAC/SCC
webhook
dependency
```

# Part 330 — Operator Mental Model

Operator is software with cluster permissions that continuously changes your platform.

Treat installation as production code deployment, not a marketplace click.

# Part 331 — OpenShift Storage

Uses Kubernetes CSI/PV/PVC model with Red Hat-supported storage integrations.

Administrators manage:

```text
StorageClass
CSI Operator/driver
PVC
snapshots
capacity
topology
```

# Part 332 — Default StorageClass

Know which class is default.

Unexpected defaults can create wrong:

```text
cost
performance
availability zone
reclaim behavior
```

# Part 333 — CSI Operators

Cloud/platform CSI drivers may be managed by OpenShift Cluster Operators or add-on Operators.

Do not upgrade independently unless supported.

# Part 334 — PersistentVolumeClaim

Application requests storage normally through PVC.

```text
Pod
 ↓
PVC
 ↓
StorageClass/CSI
 ↓
backend
```

# Part 335 — Volume Expansion

If class/driver supports it, increase PVC request.

Monitor backend/filesystem resize.

# Part 336 — VolumeSnapshot

CSI snapshot APIs/controllers can provide snapshot functionality where supported.

Snapshot remains different from full backup.

# Part 337 — OpenShift Data Foundation

Optional Red Hat storage platform providing software-defined block/file/object storage and data services for OpenShift.

It is Operator-managed and requires dedicated capacity planning.

# Part 338 — Registry Storage

Integrated image registry storage requirement differs from application PVC.

Choose supported highly available storage for production.

# Part 339 — Monitoring Storage

OpenShift monitoring time-series retention needs persistent storage if configured for durable metrics.

Capacity/IOPS matter.

# Part 340 — Machine API

On supported infrastructures, OpenShift manages infrastructure machines through Machine API.

Objects:

```text
Machine
MachineSet
MachineHealthCheck
ControlPlaneMachineSet in supported platforms
```

# Part 341 — Machine

Represents underlying host/VM lifecycle.

Machine is not same as Kubernetes Node:

```text
Machine → infrastructure
Node → Kubernetes registered compute
```

# Part 342 — MachineSet

Desired replicas of similar worker Machines.

Comparable to infrastructure-level replica controller.

# Part 343 — Scale MachineSet

```bash
oc scale machineset NAME \
  -n openshift-machine-api \
  --replicas=5
```

only in appropriate supported environments.

# Part 344 — MachineHealthCheck

Detects unhealthy Machines/Nodes and can remediate/replace under supported conditions.

Incorrect MHC can remove too many nodes; protect with limits.

# Part 345 — Machine Autoscaler

Scales individual MachineSet within min/max based on capacity needs when cluster autoscaling configured.

# Part 346 — Cluster Autoscaler

Controls cluster-wide autoscaling policy.

Works with MachineAutoscalers.

# Part 347 — Infrastructure Node

Label worker as infra role and configure platform components to schedule there.

May affect subscription/licensing treatment depending on workload/use—verify Red Hat subscription rules.

# Part 348 — Node Roles

Labels typically:

```text
node-role.kubernetes.io/master/control-plane
node-role.kubernetes.io/worker
node-role.kubernetes.io/infra
```

exact role behavior derives from labels/taints/placement.

# Part 349 — Node Label

Use for:

```text
workload placement
hardware
zone
role
```

protect security-sensitive labels.

# Part 350 — Taints/Tolerations

Dedicated infra/special nodes use taints to repel ordinary workloads.

Platform components receive tolerations.

# Part 351 — MachineConfig Custom Pool

Create custom MCP for specialized worker group to apply:

```text
kernel args
systemd
CRI-O config
files
```

without changing all workers.

# Part 352 — Performance Profile Concept

Performance Addon/Tuned capabilities can configure:

```text
CPU isolation
hugepages
NUMA
real-time kernel
```

for latency-sensitive workloads.

# Part 353 — Node Tuning Operator

Manages Tuned profiles and node-level performance settings.

Prefer supported profiles over manual sysctl edits.

# Part 354 — Specialized Hardware

Operators can manage:

```text
GPU
SR-IOV
device plugins
Node Feature Discovery
```

and node labels/resources.

# Part 355 — Node Feature Discovery

Detects hardware/features and labels nodes for scheduling/operator use.

Do not blindly trust arbitrary workload-controlled labels for security.

# Part 356 — Node Maintenance

Use Kubernetes/OpenShift:

```text
cordon
drain
Machine API/MCO
```

depending on operation.

Account for PDB/local state.

# Part 357 — RHCOS Updates

RHCOS updates are integrated into OpenShift release/MCO lifecycle.

Do not `dnf update` nodes manually.

# Part 358 — Node Debug

```bash
oc debug node/NODE
chroot /host
```

then:

```text
journalctl
crictl
ip
ss
filesystem
```

as needed.

# Part 359 — CRI-O Service

On node:

```bash
systemctl status crio
journalctl -u crio
```

inside `chroot /host` debug context.

# Part 360 — Kubelet Service

```bash
systemctl status kubelet
journalctl -u kubelet
```

to diagnose node NotReady/runtime/CNI.

# Part 361 — Node NotReady

Check:

```text
kubelet
CRI-O
CNI/OVN
disk/memory/PID
certificate
network/API
MCO
```

# Part 362 — MCP Degraded Node

Check MachineConfigDaemon logs and node current/desiredConfig annotations/status.

Manual drift is common cause.

# Part 363 — Storage Node Failure

For stateful workload:

```text
PVC
VolumeAttachment
CSI
zone
node failure
backend
```

must be traced separately from Machine replacement.

# Part 364 — Capacity Planning

Reserve resources for:

```text
platform Operators
monitoring
logging
ingress
registry
DaemonSets
application failover
```

not just app requests.

# Part 365 — Nodes and Storage Mental Model

OpenShift tries to make infrastructure declarative:

```text
Machine → Node
MachineConfig → OS
CSI → storage
Operators → lifecycle
```

# Part 366 — OpenShift Monitoring

Includes integrated monitoring for platform components based on Prometheus ecosystem.

Cluster admins receive default dashboards/alerts.

# Part 367 — openshift-monitoring

Namespace contains core cluster monitoring components.

Do not edit Operator-owned Deployments manually.

# Part 368 — Prometheus

Scrapes metrics from OpenShift components and targets.

OpenShift manages configuration through supported monitoring APIs/ConfigMaps/Operators.

# Part 369 — Alertmanager

Groups/routes alerts to notification integrations.

Configure receivers carefully and protect credentials.

# Part 370 — Thanos Concept

OpenShift monitoring architecture uses Thanos components for query/federation/storage-related functionality depending on configuration.

# Part 371 — User Workload Monitoring

Can enable monitoring for user projects.

Applications expose metrics and create:

```text
ServiceMonitor
PodMonitor
PrometheusRule
```

according to supported APIs.

# Part 372 — ServiceMonitor

Defines how Prometheus discovers/scrapes Service endpoints.

Incorrect label selector is common cause of missing metrics.

# Part 373 — PrometheusRule

Defines alerting/recording rules.

Alerts require:

```text
useful threshold
duration
severity
owner
runbook
```

# Part 374 — Alerts UI

Console shows active alerts and cluster health.

Never silence alerts permanently without resolving cause.

# Part 375 — ClusterOperator Alerts

Degraded Operators often generate alerts.

Correlate:

```text
alert
CO condition
events
Operator logs
```

# Part 376 — OpenShift Logging

Modern OpenShift logging stack is Operator-managed and commonly uses Loki-based log storage/collection integrations.

Exact components evolve across versions.

# Part 377 — Loki Operator

Manages LokiStack/log storage in supported logging architecture.

Object storage is important for scalable production logging.

# Part 378 — Log Collector

Collectors such as Vector-based components gather container/platform logs in modern OpenShift logging stacks.

Configure filtering/forwarding/retention intentionally.

# Part 379 — ClusterLogForwarder Concept

Routes logs to:

```text
Loki
external SIEM
syslog
cloud logging
other supported outputs
```

depending on logging Operator version.

# Part 380 — Audit Log Forwarding

Security audit logs can be forwarded to SIEM.

Protect sensitive content and retention.

# Part 381 — Cluster Observability Operator

Current OpenShift includes Cluster Observability Operator documentation for deploying/configuring observability components.

It supplements evolving observability architecture.

# Part 382 — OpenTelemetry

Red Hat build of OpenTelemetry supports telemetry collection/export:

```text
traces
metrics
logs
```

depending on integration.

# Part 383 — Distributed Tracing

Trace request path across microservices.

Useful when Route/Service/Pod appear healthy but latency is high.

# Part 384 — Network Observability

Adds network flow dashboards/metrics beyond normal Prometheus component monitoring.

# Part 385 — Power Monitoring

OpenShift includes power-monitoring integration for energy-related telemetry in supported environments.

Useful for sustainability/capacity analysis.

# Part 386 — Events

```bash
oc get events \
  --sort-by=.metadata.creationTimestamp
```

important for:

```text
scheduling
image pull
SCC
mount
route/operator events
```

# Part 387 — Container Logs

```bash
oc logs pod/POD
oc logs deployment/API
oc logs POD --previous
```

# Part 388 — Operator Logs

Find operator namespace/pod then inspect logs.

Operator's condition message often identifies exact component.

# Part 389 — Metrics vs Logs vs Events

```text
metrics → how much/how often
logs → detailed records
events → Kubernetes lifecycle notices
traces → request path
```

Use together.

# Part 390 — OpenShift Pipelines

Red Hat OpenShift Pipelines is Tekton-based CI/CD.

Objects:

```text
Task
Pipeline
PipelineRun
TaskRun
```

installed/managed as Operator.

# Part 391 — Pipeline Security

CI Pods can access:

```text
source
registry
secrets
cluster deploy permissions
```

separate build/deploy ServiceAccounts and least privilege.

# Part 392 — OpenShift GitOps

Argo CD-based GitOps product.

```text
Git desired state
 ↓
Argo CD
 ↓
OpenShift resources
```

supports declarative continuous delivery.

# Part 393 — GitOps Drift

Manual cluster edit can be reverted by GitOps controller.

Identify source of truth before emergency edits.

# Part 394 — GitOps Admin

Platform team manages:

```text
Argo instance
RBAC
projects
repositories
credentials
cluster targets
resource exclusions
```

# Part 395 — OpenShift Serverless

Knative-based platform for serverless services/events.

Installed as Operators, not mandatory core OCP.

# Part 396 — OpenShift Service Mesh

Provides service-mesh capabilities such as:

```text
mTLS
traffic management
telemetry
authorization
```

through supported product stack.

# Part 397 — OpenShift Virtualization

KubeVirt-based VM platform on OpenShift.

Allows VMs and containers under Kubernetes-style management.

Separate deep course would be required for production administration.

# Part 398 — Sandboxed Containers

Optional stronger-isolation runtime technology for selected workloads.

Useful where shared-kernel isolation is insufficient.

# Part 399 — OpenShift Lightspeed

Current OpenShift integration includes AI-assisted operations/documentation capabilities.

Treat generated advice as assistant input, not unreviewed production change.

# Part 400 — Jenkins Legacy Context

OpenShift historically integrated Jenkins images/templates.

Current CI/CD direction favors OpenShift Pipelines/GitOps; maintain Jenkins only where business requirements justify it.

# Part 401 — BuildConfig vs Shipwright

```text
BuildConfig:
established OpenShift-native legacy/current supported build API

Shipwright:
newer extensible Kubernetes build framework
```

Know what your cluster/application uses.

# Part 402 — Template vs Helm/Kustomize

```text
Template → OpenShift parameterized objects
Helm → templates/package/release
Kustomize → overlays/patches
GitOps → continuous reconciliation
```

# Part 403 — Developer Catalog

Console catalog can surface:

```text
Operators
Helm charts
templates
samples
developer services
```

content governance matters.

# Part 404 — Observability Retention

Plan:

```text
metrics retention
log retention
trace retention
object storage
PII/security
cost
```

# Part 405 — Observability Mental Model

OpenShift platform should answer:

```text
Is cluster healthy?
Which Operator is degraded?
Are users affected?
Which node/network/storage layer?
What changed?
```

# Part 406 — Cluster Health Quick Check

```bash
oc get clusterversion
oc get clusteroperators
oc get nodes
oc get mcp
oc get pods -A
```

This creates first platform-wide health picture.

# Part 407 — Degraded ClusterOperator Workflow

```text
read condition message
↓
identify managed namespace/component
↓
events
↓
operator logs
↓
operand logs/status
↓
dependency
```

# Part 408 — Authentication Degraded

Users may fail login while existing ServiceAccount workloads continue.

Check:

```text
authentication Operator
OAuth Pods
IdP configuration
certificates
routes
```

# Part 409 — Console Degraded

Console can fail while API/CLI works.

Check Console Operator, Route, console Pods, OAuth/auth dependencies.

# Part 410 — Ingress Degraded

Check:

```text
Ingress Operator
IngressController status
router Pods
LoadBalancer
DNS
certificate
node placement
```

# Part 411 — Image Registry Degraded

Check:

```text
Image Registry Operator
registry config
storage
registry Pods
route
credentials
```

# Part 412 — Monitoring Degraded

Check:

```text
monitoring Operator/components
PVC/storage
memory
rules/config
certificates
```

# Part 413 — MachineConfig Degraded

Check:

```text
MCP
MCD logs
node desired/current config
manual drift
disk
reboot
```

# Part 414 — Network Degraded

Check CNO and OVN components before application-level workarounds.

Networking degradation can affect every namespace.

# Part 415 — DNS Degraded

Check DNS Operator and DNS Pods, then upstream resolver/network.

# Part 416 — SCC Denied Pod

Symptoms in events:

```text
unable to validate against any security context constraint
```

Investigate requested:

```text
UID
privileged
capability
hostPath
hostNetwork
SELinux
```

then fix image/Pod or grant narrow custom SCC.

# Part 417 — Arbitrary UID Failure

Typical:

```text
Permission denied writing /app
```

because image expects fixed UID/root.

Fix image ownership/group permissions; do not grant `anyuid` immediately.

# Part 418 — ImagePullBackOff

Check:

```text
image reference
ImageStream trigger
registry auth
mirror
proxy
TLS
pull secret
digest
```

# Part 419 — Build Failure

Check:

```text
source clone
builder image
build ServiceAccount
secret
dependency network
output registry
quota
```

# Part 420 — Route 503

Trace:

```text
DNS
Route admission
router
Service
EndpointSlice
readiness
Pod listener
```

# Part 421 — Route TLS Error

Trace:

```text
host/SNI
termination
route cert
router cert
destination CA
backend TLS
```

# Part 422 — LoadBalancer Pending

Check:

```text
cloud/network provider Operator
Service events
quota
address pool
MetalLB
permissions
```

# Part 423 — PVC Pending

Check:

```text
PVC events
StorageClass
CSI
backend capacity
zone/topology
quota
```

# Part 424 — Node NotReady

Use:

```bash
oc describe node NODE
oc debug node/NODE
chroot /host
journalctl -u kubelet
journalctl -u crio
```

then network/disk/MCO.

# Part 425 — MCP Updating Too Long

Check:

```text
drain blocked
PDB
reboot
node Ready
MCD
rendered config
```

# Part 426 — Operator Install Failure

Classic OLM:

```text
CatalogSource
Subscription
InstallPlan
CSV
Operator Pod
CRD/webhook
```

modern OLM v1 uses different extension APIs; identify model first.

# Part 427 — Webhook Failure

Can block all resource creation matching webhook.

Check:

```text
Service endpoints
certificate
Operator
failurePolicy
DNS/network
```

# Part 428 — Update Blocked

Check:

```text
Upgradeable=False
ClusterVersion conditions
degraded Operators
MCP
available update graph
```

Do not bypass unless Red Hat-supported procedure.

# Part 429 — Update Stalled

Find first component not reaching desired version.

```bash
oc get co
oc get mcp
oc describe clusterversion
```

# Part 430 — Disconnected Pull Failure

Check:

```text
mirror content present
IDMS/ITMS
pull secret
registry TLS
DNS
proxy
release signature/content
```

# Part 431 — oc adm must-gather Use

Collect after initial evidence when issue is broad or support case likely.

Archive can be large and sensitive.

# Part 432 — Must-Gather Plugins

Operators/products can provide custom must-gather images to collect domain-specific diagnostics.

Use correct image/version.

# Part 433 — Must-Gather Targeting

Current support tooling can use targeted `oc adm inspect` through must-gather to reduce data volume.

Useful for one Operator/project.

# Part 434 — Support Case Preparation

Provide:

```text
cluster ID/version
time window
symptoms
impact
recent changes
must-gather
reproduction
```

without exposing unrelated secrets outside approved support workflow.

# Part 435 — etcd Backup Concept

OpenShift provides supported cluster backup/restore procedures around etcd and static resources.

Use documented scripts/procedures for exact OCP version.

# Part 436 — etcd Snapshot Sensitivity

Contains:

```text
Secrets
RBAC
routes
projects
Operator CRs
cluster state
```

encrypt/protect off-cluster.

# Part 437 — Restore Scope

etcd restore recovers control-plane API state, not automatically external:

```text
PVC data
object storage
external DB
cloud resources
registry backups
```

# Part 438 — Application Backup

Separate from cluster backup:

```text
database backups
PVC snapshots/backups
object storage versioning
external service backup
```

# Part 439 — Disaster Recovery

Define:

```text
cluster rebuild/restore
DNS/LB
registry/mirrors
PKI
GitOps
storage
identity provider
application data
```

# Part 440 — EX280 Current Title

Current Red Hat certification:

```text
Red Hat Certified System Administrator in OpenShift
EX280
```

Red Hat states the exam is performance-based.

# Part 441 — EX280 Version

Current Red Hat EX280 page states:

```text
Exam based on OCP 4.18
```

This is older than the live OCP 4.22 baseline of this course.

Practice exam-specific tasks in 4.18-compatible lab when possible.

# Part 442 — EX280 Manage OCP Objectives

Includes:

```text
web console
CLI
projects
images/tags/digests
resource queries
manifests
events/alerts/logs
cluster health
troubleshooting
```

# Part 443 — EX280 Resource Manifests

Includes:

```text
YAML
deployment updates
Kustomize
overlays
```

# Part 444 — EX280 Authentication/Authorization

Includes managing:

```text
users
groups
permissions
```

plus application security/service accounts.

# Part 445 — EX280 Networking

Includes:

```text
networking components
SDN troubleshooting
Routes
TLS
NetworkPolicy
external access
non-HTTP/SNI LoadBalancer
```

# Part 446 — EX280 Developer Self-Service

Includes:

```text
cluster/project quota
resource requirements
LimitRange
project templates
```

# Part 447 — EX280 Operators

Includes installing/uninstalling/deleting Operators.

Practice classic OLM resources for 4.18 context.

# Part 448 — EX280 Persistence Requirement

Red Hat explicitly states exam configurations must persist after reboot without intervention.

Do not solve tasks with temporary command-only state.

# Part 449 — After EX280

Current Red Hat recommends advanced OpenShift administration training/exam path such as:

```text
DO380
EX380
```

for large-scale enterprise operations.

# Part 450 — OpenShift Final Mental Model

Professional OpenShift administration means operating **a supported Kubernetes distribution as an integrated product**.

Think:

```text
ClusterVersion
ClusterOperators
RHCOS/MCO
CRI-O
OVN
Routes
Registry
OAuth/RBAC/SCC
OLM
Monitoring
Updates
Support
```

The strongest administrator knows both Kubernetes internals and OpenShift's Operator-managed sources of truth.

---

# Supplemental Deep-Study Layer — OpenShift

> **Source distinction:** The complete uploaded Course 61 remains preserved in this enhanced file. The material below adds deeper platform-operator reasoning, CVO/MCO/RHCOS lifecycle, installation dependencies, project self-service, enterprise identity/RBAC, SCC/PSA/SELinux, Routes/Ingress/OVN, image/build supply chain, OLM governance, storage/Machine API, observability, GitOps/Pipelines, upgrades/disconnected mirroring, DR/support, and evidence-first incident response. Exact OCP/EX280/Operator version statements in the original source remain source-derived; verify the documentation matching the live OpenShift release before version-specific production changes.

Preferred study flow:

```text
Concept
  ↓
Detailed explanation
  ↓
OpenShift Operator mental model
  ↓
oc / YAML / configuration
  ↓
Expected evidence
  ↓
Why it works
  ↓
Production scenario
  ↓
Troubleshooting / recovery
  ↓
Best practice
```


## Advanced Deep Dive 1 — Operator Ownership and Source of Truth

### Concept

OpenShift platform components are reconciled by Cluster Operators. When an Operator owns a Deployment, ConfigMap, DaemonSet, or Secret, editing the generated object can be temporary or harmful because the Operator will reconcile it back.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get clusteroperators
oc get deploy -A | grep -i operator
oc describe clusteroperator ingress
```

### Expected Evidence

The owning Operator and its status/message are identified before any change is made.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Change the supported Operator custom resource or configuration API, not generated operands.

---

## Advanced Deep Dive 2 — ClusterVersion as Platform Desired State

### Concept

The ClusterVersion resource records the desired OpenShift release and the history of update attempts. It is the main platform-level desired-state object for OpenShift lifecycle.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get clusterversion
oc describe clusterversion version
```

### Expected Evidence

Desired version, history, channel, available updates, and conditions are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use ClusterVersion/CVO as the supported release lifecycle instead of upgrading core components individually.

---

## Advanced Deep Dive 3 — ClusterOperator Condition Interpretation

### Concept

Available, Progressing, Degraded, and Upgradeable describe different aspects of platform health. Progressing is normal during rollout, while Degraded indicates an Operator-detected fault and Upgradeable can intentionally block a cluster update.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co
oc get co network -o jsonpath='{range .status.conditions[*]}{.type}={.status}{" reason="}{.reason}{"\n"}{end}'
```

### Expected Evidence

The exact condition reason is visible instead of relying on a green/red summary.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Read Operator conditions and messages before restarting operands.

---

## Advanced Deep Dive 4 — Release Payload Mental Model

### Concept

An OpenShift release is an integrated tested payload of platform images and manifests. CVO reconciles this payload across Cluster Operators, which is why arbitrary component version mixing is unsupported.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
release image
  ↓ verified payload
Cluster Version Operator
  ↓
Cluster Operators
  ↓
platform operands + RHCOS rollout
```

### Expected Evidence

The platform version is treated as one tested composition rather than independent package versions.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Upgrade through supported release graph edges.

---

## Advanced Deep Dive 5 — CVO Failure Decomposition

### Concept

A stalled update should be reduced to the first component that is not converging: ClusterVersion history, a degraded ClusterOperator, an updating/degraded MachineConfigPool, or an Operator dependency.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get clusterversion
oc get co
oc get mcp
oc get events -A --sort-by=.metadata.creationTimestamp | tail -60
```

### Expected Evidence

The first non-converged layer is identified.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not force past upgrade blockers without understanding the reported risk.

---

## Advanced Deep Dive 6 — RHCOS Immutable Node Model

### Concept

RHCOS is intended to be managed declaratively. Manual package installation or persistent host edits create configuration drift that can conflict with MCO validation and future upgrades.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get nodes -o wide
oc debug node/<NODE> -- chroot /host rpm-ostree status 2>/dev/null || true
```

### Expected Evidence

The node OS image/state can be inspected without treating the node as a traditional mutable server.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use MachineConfig and supported Operators for persistent node changes.

---

## Advanced Deep Dive 7 — MachineConfig Merge

### Concept

Multiple MachineConfig objects matching one MachineConfigPool are rendered into one effective configuration. The rendered config, not any single MachineConfig, is what a node converges toward.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get mc
oc get mcp worker -o jsonpath='{.status.configuration.name}{"\n"}'
```

### Expected Evidence

The current rendered configuration name is visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Review all matching MachineConfigs before assuming which object caused a node change.

---

## Advanced Deep Dive 8 — MachineConfigPool Rollout

### Concept

MachineConfigPool changes can cordon, drain, reboot, and update nodes sequentially. Capacity and disruption budgets must tolerate the rollout.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get mcp
oc describe mcp worker
```

### Expected Evidence

Updated, updating, degraded, ready, and unavailable machine counts are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Treat MCO changes like node-maintenance events with N-1 capacity.

---

## Advanced Deep Dive 9 — MCP Degraded Diagnosis

### Concept

A degraded MachineConfigPool can result from filesystem drift, failed reboot, unavailable node, invalid MachineConfig, or MachineConfigDaemon failure.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get mcp
oc -n openshift-machine-config-operator get pods -o wide
oc -n openshift-machine-config-operator logs ds/machine-config-daemon --tail=100
```

### Expected Evidence

The affected pool/node and MCD error can be correlated.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Fix the actual node/config drift instead of deleting the pool or rendered config.

---

## Advanced Deep Dive 10 — MCD Current vs Desired Configuration

### Concept

Nodes carry annotations/status describing their current and desired rendered MachineConfig. A mismatch explains why a pool remains Updating.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get node <NODE> -o jsonpath='{.metadata.annotations.machineconfiguration\.openshift\.io/currentConfig}{" current\n"}{.metadata.annotations.machineconfiguration\.openshift\.io/desiredConfig}{" desired\n"}'
```

### Expected Evidence

Current and desired rendered configurations can be compared.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use node annotations plus MCD logs to isolate rollout failures.

---

## Advanced Deep Dive 11 — Control Plane vs Worker Pools

### Concept

Master/control-plane and worker pools normally have separate rendered configurations and rollout semantics. Control-plane MCO changes carry larger blast radius because they can affect API/etcd availability.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get mcp master worker
```

### Expected Evidence

Each pool's rollout state is independent and visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Apply the strictest change control to control-plane MachineConfig changes.

---

## Advanced Deep Dive 12 — Custom MachineConfigPool

### Concept

Specialized node groups can use custom pools to receive specific kernel arguments, files, systemd units, CRI-O settings, or performance configuration without changing all workers.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
worker pool
  ├─ general nodes
custom infra pool
  ├─ ingress/registry nodes
custom performance pool
  └─ low-latency nodes
```

### Expected Evidence

Specialized configuration is isolated to intended nodes.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use custom pools only when the operational need justifies extra lifecycle complexity.

---

## Advanced Deep Dive 13 — MachineConfig Rollback

### Concept

Rollback generally means removing/reverting the offending MachineConfig and allowing MCO to render a new desired state, not manually undoing files on every node.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
bad MC applied
  ↓ MCP rolls out
problem detected
  ↓ revert/delete custom MC
MCO renders corrected config
  ↓ nodes converge
```

### Expected Evidence

The rollback returns nodes to a supported rendered configuration.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Keep a version-controlled copy of every custom MachineConfig.

---

## Advanced Deep Dive 14 — Installation Dependency Graph

### Concept

OpenShift installation is a dependency graph across DNS, load balancers, RHCOS/Ignition, bootstrap, control-plane, certificates, networking, and Operators. A failure in any prerequisite can stall the installer.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
DNS + LB + hosts
  ↓
bootstrap
  ↓
control-plane
  ↓
CNI/network
  ↓
operators
  ↓
cluster complete
```

### Expected Evidence

The failed installation stage can be placed in the dependency graph.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Troubleshoot the earliest failed dependency instead of repeatedly rerunning the installer.

---

## Advanced Deep Dive 15 — IPI vs UPI Responsibility

### Concept

Installer-provisioned infrastructure creates supported infrastructure automatically; user-provisioned infrastructure shifts more responsibility for DNS, LBs, compute, networking, and lifecycle to administrators.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
IPI: installer → infra + cluster
UPI: admin → infra, installer/assets → cluster
```

### Expected Evidence

Ownership of infrastructure creation and failure diagnosis is explicit.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Choose the model based on platform support and organizational infrastructure control.

---

## Advanced Deep Dive 16 — Assisted Installation

### Concept

Assisted Installer discovers hosts, validates readiness, and coordinates installation. It reduces manual bootstrap complexity but still depends on correct networking, DNS, storage, firmware, and host inventory.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
hosts boot discovery
  ↓ inventory/validation
assisted service
  ↓ install config
  ↓ cluster bootstrap
```

### Expected Evidence

Host validation failures are visible before cluster installation begins.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Resolve discovery validation errors rather than bypassing them.

---

## Advanced Deep Dive 17 — Agent-Based Installation

### Concept

Agent-based installation packages discovery and installation intent into bootable assets, useful for disconnected or constrained on-prem environments.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
install-config + agent-config
  ↓ generate ISO
hosts boot
  ↓ agent discovery
  ↓ bootstrap/install
```

### Expected Evidence

Cluster intent and host mapping are predeclared and reproducible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Keep generated assets protected because they can contain cluster credentials/configuration.

---

## Advanced Deep Dive 18 — Bootstrap Completion

### Concept

The temporary bootstrap host participates only until the permanent control plane can host the required bootstrap services. Removing it early can break installation.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
openshift-install wait-for bootstrap-complete --dir=<DIR> --log-level=debug
```

### Expected Evidence

The installer explicitly reports bootstrap completion.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Remove bootstrap infrastructure only after the supported completion signal.

---

## Advanced Deep Dive 19 — Install Config Security

### Concept

`install-config.yaml` can contain pull secrets, SSH keys, cluster identity, platform details, and network configuration. It should be protected and intentionally archived or destroyed.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
chmod 600 install-config.yaml
```

### Expected Evidence

The file is readable only by the intended operator account.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Treat installation assets as sensitive cluster-bootstrap material.

---

## Advanced Deep Dive 20 — OpenShift DNS Prerequisites

### Concept

API, API-int, wildcard apps, host forward/reverse resolution, and upstream resolver behavior are foundational. Incorrect DNS can appear as bootstrap, TLS, ingress, or node-registration failure.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
dig api.<cluster>.<baseDomain>
dig api-int.<cluster>.<baseDomain>
dig test.apps.<cluster>.<baseDomain>
```

### Expected Evidence

Each critical name resolves to the intended load-balancer/address.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Validate DNS from bootstrap/control-plane/worker network paths before install.

---

## Advanced Deep Dive 21 — API Load Balancer

### Concept

The API load balancer provides a stable control-plane endpoint and must route only to healthy API servers while preserving TLS.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
curl -k https://api.<cluster>.<baseDomain>:6443/readyz 2>/dev/null || true
```

### Expected Evidence

The API endpoint responds through the load balancer when the backend is ready.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Make API LB itself highly available and monitor backend readiness.

---

## Advanced Deep Dive 22 — Ingress Load Balancer

### Concept

The ingress load balancer sends 80/443 traffic toward the OpenShift router/IngressController infrastructure. Wildcard apps DNS must point to it.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
*.apps DNS
  ↓ external/internal LB
router Pods
  ↓ Route
Service
```

### Expected Evidence

North-south traffic has a documented LB→router path.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Keep ingress LB and API LB roles separate.

---

## Advanced Deep Dive 23 — Pull Secret Lifecycle

### Concept

The installation/global pull secret grants registry access for Red Hat and configured registries. It is sensitive and can affect cluster-wide image pulls.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get secret pull-secret -n openshift-config -o jsonpath='{.data.\.dockerconfigjson}' >/dev/null
```

### Expected Evidence

The secret exists at the expected cluster location without printing its value.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Never paste the pull secret into tickets or shell history.

---

## Advanced Deep Dive 24 — kubeadmin Retirement

### Concept

The installer-created kubeadmin account is bootstrap access. A production cluster should configure durable enterprise identity and then remove temporary bootstrap admin access according to supported guidance.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get secret kubeadmin -n kube-system 2>/dev/null || true
```

### Expected Evidence

The team can verify whether temporary bootstrap credentials still exist.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Retire bootstrap identities after enterprise admin access is proven.

---

## Advanced Deep Dive 25 — oc Context Safety

### Concept

`oc` can target multiple clusters/projects. High-impact commands must begin with verification of user, server, and current project.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc whoami
oc whoami --show-server
oc project
```

### Expected Evidence

Operator identity, API endpoint, and project are visible before a write.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Make context verification part of every change runbook.

---

## Advanced Deep Dive 26 — Projects as Policy Boundaries

### Concept

An OpenShift Project is a Kubernetes Namespace plus OpenShift metadata/self-service behavior. Its real isolation comes from RBAC, quota, SCC/PSA, NetworkPolicy, and platform policy.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get project <PROJECT> -o yaml
oc get rolebinding,resourcequota,limitrange,networkpolicy -n <PROJECT>
```

### Expected Evidence

The project's policy controls can be inspected together.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Provision projects from a standard baseline, not as empty namespaces.

---

## Advanced Deep Dive 27 — Project Request Template

### Concept

A customized project request template can automatically apply baseline quota, LimitRange, labels, RoleBindings, and NetworkPolicies whenever developers create projects.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
new project request
  ↓ project template
namespace/project
  + quota
  + limits
  + RBAC
  + network policy
```

### Expected Evidence

New projects begin compliant by default.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use templates/automation to eliminate repetitive manual tenant setup.

---

## Advanced Deep Dive 28 — ClusterResourceQuota

### Concept

ClusterResourceQuota can enforce aggregate quota across multiple projects selected by labels or annotations, useful when one team owns several environments.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get clusterresourcequota
```

### Expected Evidence

Cross-project quota policy and usage are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use aggregate quota for team-level governance while retaining per-project quotas where useful.

---

## Advanced Deep Dive 29 — LimitRange Defaults

### Concept

LimitRange can default CPU/memory requests and limits for Pods that omit them, preventing unbounded BestEffort workloads.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get limitrange -A
oc describe limitrange -n <PROJECT>
```

### Expected Evidence

Default/min/max constraints are explicit.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Pair LimitRange defaults with measurement-driven right-sizing.

---

## Advanced Deep Dive 30 — ResourceQuota Admission

### Concept

Quota rejection happens during API admission before scheduling. It is distinct from a Pod remaining Pending due insufficient node resources.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc describe resourcequota -n <PROJECT>
```

### Expected Evidence

Used vs hard quota identifies whether admission is blocking creation.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Read the API error before changing node capacity.

---

## Advanced Deep Dive 31 — Developer Self-Service Guardrails

### Concept

Self-service is successful when developers can create permitted applications without cluster-admin while platform controls automatically enforce quota, networking, identity, security, and observability.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
developer
  ↓ project-scoped RBAC
create workload
  ↓ quota / SCC / PSA / NetworkPolicy / policy
safe platform execution
```

### Expected Evidence

Developers can move quickly without bypassing platform governance.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Design guardrails rather than ticket-driven manual approvals for routine work.

---

## Advanced Deep Dive 32 — OAuth Authentication Flow

### Concept

OpenShift OAuth authenticates users through configured identity providers and issues tokens consumed by `oc` and the console. Authentication and RBAC authorization remain separate stages.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
user
  ↓ IdP
OAuth
  ↓ token
OpenShift API
  ↓ RBAC
allowed / denied
```

### Expected Evidence

Login success can be separated from authorization failure.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Troubleshoot identity provider, OAuth route/certs, and RBAC independently.

---

## Advanced Deep Dive 33 — OIDC Federation

### Concept

External OIDC integration depends on issuer trust, client/audience, redirect URIs, claims, groups, CA trust, and token lifetime.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
enterprise IdP
  ↓ signed ID token
OpenShift authentication
  ↓ user/groups
RBAC
```

### Expected Evidence

Identity claims map predictably to cluster users/groups.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use short-lived IdP-managed identities and MFA for human access.

---

## Advanced Deep Dive 34 — LDAP Integration

### Concept

LDAP-backed identity requires secure TLS, scoped bind credentials, filters, attribute mapping, and often separate group synchronization.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
OpenShift OAuth
  ↓ LDAPS
directory
  ↓ user DN/attributes
mapped OpenShift user
```

### Expected Evidence

User lookup and TLS trust can be tested independently of RBAC.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Avoid broad directory searches and plaintext LDAP.

---

## Advanced Deep Dive 35 — Group-Centric RBAC

### Concept

Enterprise access scales better when RoleBindings target groups rather than individual users.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc adm groups new app-devs
oc adm policy add-role-to-group edit app-devs -n orders-dev
```

### Expected Evidence

Project access follows group membership.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Bind roles to identity-provider groups where possible.

---

## Advanced Deep Dive 36 — admin vs edit vs view

### Concept

Project-level `admin`, `edit`, and `view` have significantly different capabilities. `edit` can often indirectly access application secrets through workload manipulation, so it is not a harmless role.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc auth can-i --list -n <PROJECT>
```

### Expected Evidence

Effective verbs/resources can be reviewed rather than assumed from role name.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Test actual permissions before assigning broad roles.

---

## Advanced Deep Dive 37 — Cluster-Admin Audit

### Concept

Cluster-admin grants full control and should be limited to a small, audited administrator group.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get clusterrolebindings -o json | jq -r '.items[] | select(.roleRef.name=="cluster-admin") | .metadata.name'
```

### Expected Evidence

Cluster-admin bindings can be enumerated.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use project-scoped roles for application teams and break-glass for emergency access.

---

## Advanced Deep Dive 38 — ServiceAccount Identity

### Concept

Workloads should use dedicated ServiceAccounts per privilege boundary rather than default project identity.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc create sa orders-api -n orders
oc auth can-i get configmaps --as=system:serviceaccount:orders:orders-api -n orders
```

### Expected Evidence

The exact workload identity and its effective access are verifiable.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

One ServiceAccount should represent one coherent application capability.

---

## Advanced Deep Dive 39 — Bound ServiceAccount Tokens

### Concept

Modern ServiceAccount tokens are projected, short-lived, and audience-bound. Avoid manually creating legacy long-lived token Secrets.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc create token orders-api -n orders --duration=10m
```

### Expected Evidence

A temporary token is issued without creating a permanent Secret.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Disable automount for workloads that never call the cluster API.

---

## Advanced Deep Dive 40 — SCC Admission Mental Model

### Concept

SCC admission evaluates the requested Pod security context against SCCs the requesting user/ServiceAccount is authorized to use. It can reject or default security settings.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
Pod spec
  + caller identity
  + authorized SCCs
  ↓ SCC admission
selected SCC / rejection
```

### Expected Evidence

A denial can be traced to one requested privilege that no allowed SCC permits.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Fix the workload first; grant a broader SCC only when the requirement is justified.

---

## Advanced Deep Dive 41 — Default SCC Immutability

### Concept

Default SCCs are platform-managed policy objects. Modifying them creates upgrade/supportability risk and can affect many workloads.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get scc
```

### Expected Evidence

Default and custom SCCs can be distinguished.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Create a narrowly scoped custom SCC instead of modifying built-ins.

---

## Advanced Deep Dive 42 — Arbitrary UID Image Design

### Concept

OpenShift commonly runs workloads with a project-assigned arbitrary non-root UID. Images should avoid fixed UID ownership assumptions and keep writable directories group-compatible.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```dockerfile
RUN mkdir -p /opt/app/data  && chgrp -R 0 /opt/app  && chmod -R g=u /opt/app
```

### Expected Evidence

A random non-root UID can read/write required paths without world-writable permissions.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Design images for arbitrary UID rather than granting anyuid.

---

## Advanced Deep Dive 43 — SCC Denial Diagnostics

### Concept

SCC denial errors usually identify privileged mode, fixed UID, hostPath, hostNetwork/hostPID, capabilities, SELinux, fsGroup, or volume type conflicts.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc describe pod <POD> -n <PROJECT> | sed -n '/Events:/,$p'
```

### Expected Evidence

Admission error text identifies which requested security settings are incompatible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Read the denial before assigning a more permissive SCC.

---

## Advanced Deep Dive 44 — SCC Use Authorization

### Concept

Ability to use an SCC is itself an RBAC-authorized privilege. Auditing who can use privileged or anyuid SCCs is an important cluster security control.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc adm policy who-can use scc/privileged
oc adm policy who-can use scc/anyuid
```

### Expected Evidence

Users/groups/ServiceAccounts with powerful SCC access are enumerated.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Review powerful SCC usage regularly.

---

## Advanced Deep Dive 45 — Custom SCC Governance

### Concept

A custom SCC should encode the narrow exception required by one workload and be bound only to its dedicated ServiceAccount.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
legacy app requirement
  ↓ identify exact missing permission
custom SCC
  ↓ bind only serviceaccount X
```

### Expected Evidence

The exception has limited blast radius.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Document each custom SCC as a security exception ADR.

---

## Advanced Deep Dive 46 — SCC and PSA Together

### Concept

OpenShift SCC and Kubernetes Pod Security Admission solve overlapping but different problems. SCC authorizes/defaults detailed security settings; PSA enforces namespace-level Pod Security Standards.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
namespace PSA labels
  ↓ baseline/restricted policy
Pod create
  ↓ SCC authorization/defaulting
admitted only if both paths allow it
```

### Expected Evidence

Policy behavior is understood as layered admission.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Test both controls when a hardened Pod is unexpectedly rejected.

---

## Advanced Deep Dive 47 — SELinux Confinement

### Concept

OpenShift uses SELinux/MCS labels to isolate processes and volumes. POSIX mode bits alone do not explain permission failures.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc debug node/<NODE> -- chroot /host ls -Z /var/lib/kubelet 2>/dev/null | head
```

### Expected Evidence

SELinux labels are visible on the host.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Fix supported labels/policies rather than disabling SELinux.

---

## Advanced Deep Dive 48 — allowPrivilegeEscalation

### Concept

Ordinary applications should generally deny privilege escalation even when running as non-root.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```yaml
securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop: ["ALL"]
```

### Expected Evidence

The Pod requests a restricted runtime privilege set.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use the smallest security context that still allows the application to function.

---

## Advanced Deep Dive 49 — Seccomp RuntimeDefault

### Concept

RuntimeDefault seccomp reduces available syscalls while preserving broad compatibility with ordinary applications.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```yaml
securityContext:
  seccompProfile:
    type: RuntimeDefault
```

### Expected Evidence

The workload explicitly requests the runtime's default seccomp confinement.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Prefer RuntimeDefault over Unconfined.

---

## Advanced Deep Dive 50 — Security Profiles Operator

### Concept

The Security Profiles Operator can manage seccomp/SELinux profiles declaratively for workloads needing tighter control than the runtime default.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
profile CR
  ↓ Security Profiles Operator
node profile installation
  ↓ workload references profile
```

### Expected Evidence

Custom profile lifecycle is cluster-managed rather than manually copied to nodes.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use custom profiles only after measuring the workload's required behavior.

---

## Advanced Deep Dive 51 — Compliance Operator

### Concept

The Compliance Operator automates scans against supported compliance profiles and produces findings/remediation objects.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get compliancesuites,compliancescans -A 2>/dev/null || true
```

### Expected Evidence

Scan state/findings are visible when the Operator is installed.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Treat automated remediation as change input, not something to apply blindly.

---

## Advanced Deep Dive 52 — External Secret Integration

### Concept

External secret workflows reduce manually managed static Kubernetes Secrets by synchronizing or mounting values from enterprise secret stores.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
workload identity
  ↓ external secret store
operator/CSI integration
  ↓ projected/synced secret
application
```

### Expected Evidence

Secret lifecycle is tied to an external source of truth.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use least-privilege workload identity and rotation.

---

## Advanced Deep Dive 53 — Route vs Ingress

### Concept

OpenShift Route is a first-class supported application exposure API with edge, passthrough, and re-encrypt TLS semantics. Standard Kubernetes Ingress remains available but Route is central to OpenShift operations.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get routes -A
oc get ingress -A
```

### Expected Evidence

The exposure resource used by each application is clear.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Choose one supported edge model and document TLS termination.

---

## Advanced Deep Dive 54 — Edge Route TLS

### Concept

Edge termination ends client TLS at the router. Backend traffic can be HTTP or separately secured depending on configuration.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
client HTTPS
  ↓ TLS terminates
OpenShift router
  ↓ HTTP/backend
Service
```

### Expected Evidence

The router owns the public certificate/private key.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use edge termination only when plaintext or alternate backend protection is acceptable.

---

## Advanced Deep Dive 55 — Passthrough Route TLS

### Concept

Passthrough uses SNI to select a backend while the router does not decrypt application traffic.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
client TLS
  ↓ router selects by SNI
unchanged TLS
  ↓ backend Pod
```

### Expected Evidence

The backend presents and owns the TLS certificate.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use passthrough when end-to-end application TLS ownership is required.

---

## Advanced Deep Dive 56 — Re-encrypt Route TLS

### Concept

Re-encrypt terminates client TLS at the router and establishes a second verified TLS connection to the backend.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
client TLS
  ↓ terminate
router
  ↓ new TLS validated with destination CA
backend
```

### Expected Evidence

Both frontend and backend trust chains can be validated separately.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Maintain destination CA and backend certificate rotation carefully.

---

## Advanced Deep Dive 57 — Route Admission Status

### Concept

A Route object can exist but not be admitted. Its status reports router acceptance and assigned host behavior.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get route <ROUTE> -o yaml | sed -n '/status:/,$p'
```

### Expected Evidence

Admitted/host conditions explain whether a router accepted the Route.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Check admission before debugging the backend application.

---

## Advanced Deep Dive 58 — Route 503 Decomposition

### Concept

A router 503 usually means the edge is reachable but there is no usable backend because of readiness, selector, targetPort, or backend/TLS connectivity.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get route <ROUTE>
oc get svc <SVC>
oc get endpointslices -l kubernetes.io/service-name=<SVC>
oc get pods -o wide
```

### Expected Evidence

The failure is narrowed from Route to Service to endpoint to Pod.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Trace north-south traffic one hop at a time.

---

## Advanced Deep Dive 59 — IngressController Source of Truth

### Concept

Router Deployments are managed by Ingress Operator. Placement, replicas, domain, certificates, and publishing strategy should be configured on IngressController.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc -n openshift-ingress-operator get ingresscontroller
oc -n openshift-ingress get pods -o wide
```

### Expected Evidence

The supported source-of-truth resource and generated router Pods are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Never make persistent changes directly to router Deployments.

---

## Advanced Deep Dive 60 — Ingress Sharding

### Concept

Multiple IngressControllers can select namespaces or Routes to create public/internal or tenant-specific ingress planes.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
public IngressController
  ↓ routeSelector=public

internal IngressController
  ↓ namespaceSelector=internal
```

### Expected Evidence

Routes are admitted only by the intended router set.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use sharding for real network/certificate/tenancy boundaries, not cosmetic separation.

---

## Advanced Deep Dive 61 — Ingress Certificate Lifecycle

### Concept

The default apps certificate is platform edge identity and should be monitored, rotated, and distributed through supported Ingress configuration.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc -n openshift-ingress-operator get ingresscontroller default -o yaml
```

### Expected Evidence

The configured certificate reference and ingress status can be inspected.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Monitor certificate expiry and chain validity.

---

## Advanced Deep Dive 62 — OVN-Kubernetes Mental Model

### Concept

OVN-Kubernetes creates logical networking constructs for Pods, Services, policy, and egress features while programming node-level data paths.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
Pod
  ↓ veth/interface
OVN logical switch/router
  ↓ node dataplane
underlay
  ↓ remote node/Pod
```

### Expected Evidence

Packet failures can be localized to Pod, OVN, node, or external network.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Troubleshoot through OpenShift/OVN APIs and supported tooling instead of manually editing OVN databases.

---

## Advanced Deep Dive 63 — Cluster Network Operator

### Concept

CNO owns the cluster networking stack. `network` ClusterOperator condition is the first platform-level health signal when OVN or network configuration fails.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co network
oc -n openshift-network-operator get pods
```

### Expected Evidence

Operator health and namespace workloads are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Start at CNO conditions before application-specific workarounds.

---

## Advanced Deep Dive 64 — Pod/Service CIDR Governance

### Concept

ClusterNetwork and ServiceNetwork are foundational address spaces. Overlap with datacenter, VPC, VPN, or secondary networks causes difficult routing failures.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get network.config.openshift.io cluster -o yaml
```

### Expected Evidence

Cluster and Service CIDRs can be inspected from the supported config API.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Document IPAM before installation and reserve growth capacity.

---

## Advanced Deep Dive 65 — OVN MTU

### Concept

Encapsulation reduces usable Pod MTU. A mismatch can produce successful pings/small requests but failed large TLS/data transfers.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc debug node/<NODE> -- chroot /host ip link
```

### Expected Evidence

Node/interface MTUs are visible for comparison with overlay requirements.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Plan MTU from the real underlay and encapsulation overhead.

---

## Advanced Deep Dive 66 — NetworkPolicy Default Deny

### Concept

Standard NetworkPolicy is enforced by OVN-Kubernetes. A default-deny model turns implicit connectivity into explicit application dependency rules.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```yaml
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Expected Evidence

Selected Pods are isolated except for separately allowed flows.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Allow DNS and required dependencies before enabling egress deny.

---

## Advanced Deep Dive 67 — NetworkPolicy Project Labels

### Concept

Cross-project policies can use namespace selectors, making namespace labels security-relevant configuration.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get ns --show-labels
```

### Expected Evidence

Labels referenced by policy can be audited.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Govern security-significant labels so tenant users cannot self-escalate network access.

---

## Advanced Deep Dive 68 — EgressFirewall

### Concept

EgressFirewall provides OpenShift-specific namespace/project outbound controls beyond basic Pod selectors.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get egressfirewall -A 2>/dev/null || true
```

### Expected Evidence

Existing egress firewall objects and scope are visible where supported.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Treat DNS, proxies, registries, APIs, and update endpoints as explicit dependencies.

---

## Advanced Deep Dive 69 — EgressIP

### Concept

EgressIP can assign predictable source IPs to selected namespaces/workloads for external firewall allowlists.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get egressips.k8s.ovn.org -A 2>/dev/null || true
```

### Expected Evidence

Configured egress identities can be inspected.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Provide redundancy so one node failure does not remove all egress IP capacity.

---

## Advanced Deep Dive 70 — Admin Network Policy Concept

### Concept

Administrator-level network policy can enforce cluster/tenant baseline controls above application-owned policies in supported environments.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
admin baseline policy
  ↓
tenant NetworkPolicy
  ↓
OVN enforcement
```

### Expected Evidence

Platform and tenant policy responsibilities are separated.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Verify exact OCP support/maturity before production adoption.

---

## Advanced Deep Dive 71 — Multus Secondary Networks

### Concept

Multus allows Pods to attach additional interfaces beyond the default OVN network, useful for storage, telco, or legacy L2 integration.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get network-attachment-definitions -A
```

### Expected Evidence

Secondary network definitions can be inventoried.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Document routing, IPAM, security, and failure behavior for every secondary interface.

---

## Advanced Deep Dive 72 — NetworkAttachmentDefinition

### Concept

A NAD describes how Multus should attach a secondary network using a plugin such as macvlan, bridge, or SR-IOV.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: storage-net
```

### Expected Evidence

The secondary network exists as an API object.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Keep plugin configuration and IPAM version-controlled.

---

## Advanced Deep Dive 73 — SR-IOV Scheduling

### Concept

SR-IOV exposes hardware-backed virtual functions through device resources. Scheduling depends on node hardware, operator policy, and available VF resources.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get node -o json | jq -r '.items[] | [.metadata.name,.status.allocatable] | @json' | head
```

### Expected Evidence

Specialized allocatable resources can be inspected.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use dedicated node pools and capacity planning for SR-IOV workloads.

---

## Advanced Deep Dive 74 — NMState Change Safety

### Concept

NodeNetworkConfigurationPolicy can change bonds, VLANs, bridges, routes, and interfaces. A bad policy can disconnect many nodes simultaneously.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get nncp,nnce 2>/dev/null || true
```

### Expected Evidence

Desired policies and per-node enactment status are visible where NMState is installed.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Canary node network changes and maintain out-of-band recovery access.

---

## Advanced Deep Dive 75 — LoadBalancer Service on Bare Metal

### Concept

Bare-metal clusters need an implementation such as MetalLB or external network integration to allocate and advertise LoadBalancer addresses.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get svc -A | grep LoadBalancer
oc get metallb -A 2>/dev/null || true
```

### Expected Evidence

Pending external IPs can be correlated with the installed LB implementation.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not assume cloud-provider behavior exists on-premises.

---

## Advanced Deep Dive 76 — MetalLB BGP/L2 Trade-Off

### Concept

MetalLB can advertise addresses using L2 or BGP. BGP integrates with routed networks but requires ASN/peering/prefix governance.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
L2 mode → ARP/NDP advertisement
BGP mode → route advertisement to peers
```

### Expected Evidence

The external path is documented and owned jointly with the network team.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Treat address pools and BGP policy as production network configuration.

---

## Advanced Deep Dive 77 — DNS Operator Source of Truth

### Concept

OpenShift DNS is Operator-managed. Custom forwarding/upstream behavior should use supported DNS Operator configuration, not edits to generated DNS Pods.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co dns
oc get dns.operator/default -o yaml
```

### Expected Evidence

The supported DNS configuration object is visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Avoid editing generated CoreDNS workloads directly.

---

## Advanced Deep Dive 78 — Route/DNS End-to-End Test

### Concept

An application hostname depends on wildcard/external DNS, LB, router admission, Service endpoints, and Pod readiness.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
curl -vk https://<ROUTE_HOST>/ 2>&1 | head -30
oc get route,svc,endpointslices -n <PROJECT>
```

### Expected Evidence

External TLS/HTTP behavior can be correlated with cluster resources.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Verify the whole north-south path after ingress changes.

---

## Advanced Deep Dive 79 — Integrated Registry Operator

### Concept

OpenShift's image registry is managed by the Image Registry Operator. Storage, replicas, routing, and configuration should be changed through its supported config.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co image-registry
oc get configs.imageregistry.operator.openshift.io cluster -o yaml
```

### Expected Evidence

Registry health and source-of-truth configuration are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Never persistently edit the generated registry Deployment.

---

## Advanced Deep Dive 80 — Registry Storage Durability

### Concept

Production registry storage must survive Pod/node replacement and provide capacity/availability appropriate to image history and builds.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
registry Pods
  ↓ durable object/file storage
  ↓ image layers/manifests
```

### Expected Evidence

Registry persistence is separate from the registry Deployment lifecycle.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Monitor storage capacity and backup/recovery requirements.

---

## Advanced Deep Dive 81 — ImageStream Tag vs Digest

### Concept

ImageStreams provide OpenShift tag workflows, while digests identify immutable image content. Production releases should preserve digest identity even when tags drive promotion.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get is <NAME> -o yaml
oc get istag <NAME>:<TAG> -o yaml
```

### Expected Evidence

Tag history and resolved image digest can be inspected.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Promote immutable digests through environments.

---

## Advanced Deep Dive 82 — Image Change Triggers

### Concept

ImageStream updates can automatically trigger builds or deployment changes in workflows that enable image triggers.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc set triggers deployment/<DEPLOYMENT>
```

### Expected Evidence

Configured image/config triggers can be reviewed.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Know whether changing a tag automatically changes production workloads.

---

## Advanced Deep Dive 83 — BuildConfig Supply-Chain Boundary

### Concept

BuildConfig jobs can access source credentials, dependency networks, internal registry, and output repositories. The builder identity is therefore a privileged supply-chain actor.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get bc,builds
oc describe bc <BUILD>
```

### Expected Evidence

Build strategy, ServiceAccount, triggers, and output target are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Separate build and deploy permissions.

---

## Advanced Deep Dive 84 — S2I Builder Contract

### Concept

S2I builder images define assemble/run conventions that transform source into a runnable image while reducing Dockerfile maintenance for supported language stacks.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
source
  ↓ assemble
builder image runtime
  ↓ output image
  ↓ run script
```

### Expected Evidence

The build can be reproduced from source revision and builder image.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Pin builder image/version and record source commit.

---

## Advanced Deep Dive 85 — Build Failure Decomposition

### Concept

Build failures should be separated into source clone, builder pull, dependency resolution, build script, resource quota, output push, and registry authentication.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get builds
oc describe build <BUILD>
oc logs build/<BUILD>
```

### Expected Evidence

The failed build phase and exact log error are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Fix the failed supply-chain step instead of rerunning blindly.

---

## Advanced Deep Dive 86 — Shipwright Build Model

### Concept

Shipwright provides a Kubernetes-native build abstraction using Build, BuildRun, and strategies. It is distinct from BuildConfig and should be operated according to the installed Operator/API version.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc api-resources | grep -i shipwright
```

### Expected Evidence

The installed build API model can be identified.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not mix BuildConfig and Shipwright assumptions in one troubleshooting path.

---

## Advanced Deep Dive 87 — Build Provenance

### Concept

A production image release should link source commit, builder identity, dependencies, SBOM, scan, signature/provenance, and output digest.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
source commit
  ↓ trusted build
SBOM + scan + provenance
  ↓ signed image digest
```

### Expected Evidence

Incident responders can prove exactly how an image was created.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Promote artifacts, not source rebuilds, between environments.

---

## Advanced Deep Dive 88 — Registry Mirror Trust

### Concept

Disconnected or controlled clusters depend on internal mirrors for release, Operator, and application images. The mirror becomes critical supply-chain infrastructure.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
approved upstream
  ↓ mirror workflow
internal registry
  ↓ cluster pulls
```

### Expected Evidence

The internal mirror has TLS, auth, storage, backup, and monitoring ownership.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Treat mirror compromise/outage as platform-severity risk.

---

## Advanced Deep Dive 89 — Image Mirror Policy

### Concept

OpenShift mirror APIs redirect digest/tag sources toward internal registries. Incorrect mirror policy can break cluster-wide image pulls.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get imagedigestmirrorsets,imagetagmirrorsets 2>/dev/null || true
```

### Expected Evidence

Configured source-to-mirror relationships are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Test platform and workload pulls before broad mirror changes.

---

## Advanced Deep Dive 90 — Classic OLM Control Flow

### Concept

Classic OLM resolves CatalogSource + Subscription + OperatorGroup into an InstallPlan and ClusterServiceVersion, then deploys the Operator and CRDs/RBAC.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
CatalogSource
  ↓ package/channel
Subscription
  ↓ resolver
InstallPlan
  ↓
CSV + CRDs + RBAC + Operator
```

### Expected Evidence

A failed install can be placed at catalog, resolution, approval, CSV, or Operator-runtime stage.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Inspect lifecycle objects before deleting/reinstalling the Operator.

---

## Advanced Deep Dive 91 — CatalogSource Health

### Concept

Catalog failures block Operator discovery and upgrades. Diagnose catalog Pod/image, registry, DNS, TLS, proxy, and storage before touching Subscriptions.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get catalogsource -A
oc describe catalogsource <NAME> -n <NS>
```

### Expected Evidence

Catalog connection/status errors are explicit.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Secure and monitor catalogs as software supply-chain inputs.

---

## Advanced Deep Dive 92 — OperatorGroup Scope

### Concept

OperatorGroup determines where an Operator is expected to watch/manage resources. Install-mode mismatch can make CSV installation fail.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get operatorgroup -A
```

### Expected Evidence

Target namespaces/scope are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Match the Operator's supported install modes to the intended tenancy scope.

---

## Advanced Deep Dive 93 — Subscription Channel Governance

### Concept

Subscriptions select package/channel/source and optionally automatic or manual approval behavior. Automatic upgrades can be too risky for stateful or highly privileged Operators.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get subscription -A
oc describe subscription <SUB> -n <NS>
```

### Expected Evidence

Current channel, source, installed CSV, and upgrade state are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use manual approval when business change control requires review.

---

## Advanced Deep Dive 94 — InstallPlan Approval

### Concept

Manual InstallPlan approval creates an explicit checkpoint before OLM applies new CRDs/RBAC/webhooks/operator versions.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get installplan -A
```

### Expected Evidence

Pending plans can be reviewed before approval.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Inspect permissions, release notes, CRD changes, and backup readiness first.

---

## Advanced Deep Dive 95 — CSV Failure

### Concept

A CSV can remain Pending/Failed because prerequisites, APIs, permissions, webhooks, deployments, or install modes are unsatisfied.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get csv -A
oc describe csv <CSV> -n <NS>
```

### Expected Evidence

Requirements and failure reasons are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Resolve the missing requirement instead of deleting the namespace.

---

## Advanced Deep Dive 96 — Operator Permission Review

### Concept

Operators can create CRDs, webhooks, ClusterRoles, SCCs, privileged workloads, and storage/network resources. Installing one can equal deploying cluster-admin-grade software.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get clusterrolebindings,clusterroles | grep -i <OPERATOR_NAME>
```

### Expected Evidence

The Operator's privilege footprint is reviewable.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Perform security review before installing third-party Operators.

---

## Advanced Deep Dive 97 — Operator CR Status

### Concept

The Operator Deployment can be Running while the managed operand is unhealthy. The custom resource status/conditions are the authoritative application-level signal.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get <CRD_KIND> <NAME> -o yaml | sed -n '/status:/,$p'
```

### Expected Evidence

Managed resource conditions explain operand health.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Troubleshoot Operator and operand separately.

---

## Advanced Deep Dive 98 — Operator Finalizers

### Concept

Custom resources can stay Terminating when the Operator that owns cleanup is absent or broken.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get <RESOURCE> <NAME> -o jsonpath='{.metadata.finalizers}{"\n"}'
```

### Expected Evidence

Finalizer ownership explains the stuck deletion.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Restore the Operator/cleanup path before manually removing finalizers.

---

## Advanced Deep Dive 99 — CRD Deletion Risk

### Concept

Deleting a CRD removes the API definition and can remove all CR instances, potentially orphaning or destroying managed state.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get crd | grep -i <OPERATOR>
```

### Expected Evidence

CRD inventory is known before uninstall.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Follow the Operator's documented uninstall procedure.

---

## Advanced Deep Dive 100 — OLM v1 vs Classic

### Concept

Newer OpenShift versions may use newer OLM extension APIs alongside classic OLM. Operators must first identify which lifecycle model governs a particular package.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc api-resources | grep -Ei 'subscription|installplan|clusterserviceversion|catalog|extension'
```

### Expected Evidence

Installed lifecycle APIs reveal which model is available.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not assume one-to-one object mapping between classic and newer OLM.

---

## Advanced Deep Dive 101 — Operator Compatibility Before OCP Update

### Concept

Third-party Operators can depend on Kubernetes APIs, CRDs, webhook behavior, and operand versions. An OCP update should include an Operator compatibility matrix.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
OCP target
  ↕ supported
Operator version/channel
  ↕
operand version + CRDs
```

### Expected Evidence

Every production Operator has a validated supported path.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Block cluster upgrade until critical Operator compatibility is confirmed.

---

## Advanced Deep Dive 102 — CSI StorageClass Governance

### Concept

Default StorageClass determines backend, topology, encryption, reclaim policy, expansion, and cost for claims without an explicit class.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get storageclass
```

### Expected Evidence

The default class and parameters are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Document each StorageClass as a service tier.

---

## Advanced Deep Dive 103 — PVC Pending

### Concept

A Pending PVC is a storage control-plane problem until proven otherwise: no class, provisioner failure, quota, topology, capacity, or invalid parameters.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc describe pvc <PVC> -n <PROJECT>
oc get storageclass
```

### Expected Evidence

PVC events identify the provisioning failure.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Fix claim/provisioner before modifying application containers.

---

## Advanced Deep Dive 104 — VolumeAttachment Failure

### Concept

Attachable block volumes create VolumeAttachment objects. Old node attachment can block failover to a replacement node.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get volumeattachments
```

### Expected Evidence

The volume's target node/attachment status is visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use storage fencing/driver-supported detach procedures for stateful recovery.

---

## Advanced Deep Dive 105 — Snapshot vs Backup

### Concept

CSI snapshots are useful recovery points but may share the same storage account/region/failure domain. A backup should provide independent retention and restore validation.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
PVC → snapshot → fast recovery
PVC/app → backup copy → independent failure domain
```

### Expected Evidence

Recovery architecture distinguishes snapshot from durable backup.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Test application-consistent restores.

---

## Advanced Deep Dive 106 — ODF as Data Platform

### Concept

OpenShift Data Foundation is an Operator-managed storage platform providing block/file/object capabilities. It adds dedicated capacity, network, failure-domain, and upgrade requirements.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
ODF Operators
  ↓ Ceph/data services
StorageClasses / object APIs
  ↓ applications
```

### Expected Evidence

ODF health is treated as an independent stateful platform.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Capacity-plan storage nodes, replication, network, and recovery.

---

## Advanced Deep Dive 107 — Machine vs Node

### Concept

Machine represents infrastructure lifecycle; Node represents Kubernetes registered compute. A Machine can exist while its Node is unhealthy or absent.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc -n openshift-machine-api get machines -o wide
oc get nodes -o wide
```

### Expected Evidence

Infrastructure and Kubernetes identities can be mapped.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Troubleshoot Machine provisioning separately from kubelet/node registration.

---

## Advanced Deep Dive 108 — MachineSet Scaling

### Concept

MachineSets scale groups of similar worker Machines. Scaling affects infrastructure capacity, not just Kubernetes replica count.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc -n openshift-machine-api get machinesets
```

### Expected Evidence

Desired/current Machine counts are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Verify cloud/on-prem quota, IPs, subnets, and storage before scaling.

---

## Advanced Deep Dive 109 — MachineHealthCheck Safety

### Concept

MachineHealthCheck can remediate unhealthy Machines automatically. Poor thresholds or maxUnhealthy settings can remove too many nodes during a broad outage.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc -n openshift-machine-api get machinehealthchecks
```

### Expected Evidence

Remediation policy and scope can be reviewed.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Set limits so correlated failures do not trigger destructive mass remediation.

---

## Advanced Deep Dive 110 — Infra Node Placement

### Concept

Ingress, registry, monitoring, logging, and other platform workloads can be moved to dedicated infrastructure nodes using labels, taints, and Operator-supported placement.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
infra node pool
  + role label
  + taint
  ↓
Ingress/Registry/Monitoring placement
```

### Expected Evidence

Platform capacity is separated from application worker capacity.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Preserve enough infra replicas across failure domains.

---

## Advanced Deep Dive 111 — Node Tuning Operator

### Concept

Node Tuning Operator manages performance/sysctl-style profiles declaratively rather than manual host changes.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get tuned -A 2>/dev/null || true
oc get profiles.tuned.openshift.io -A 2>/dev/null || true
```

### Expected Evidence

Applied tuning profiles can be inspected where available.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use supported tuned profiles and test workload impact.

---

## Advanced Deep Dive 112 — Performance Profile

### Concept

Latency-sensitive nodes may need CPU isolation, hugepages, NUMA alignment, or real-time kernel settings coordinated through supported performance APIs.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
PerformanceProfile
  ↓ MCO/Tuned
node kernel + CPU topology
  ↓ guaranteed workload placement
```

### Expected Evidence

Node and Pod configuration align around the intended latency model.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use dedicated nodes and measurable latency objectives.

---

## Advanced Deep Dive 113 — oc debug node Workflow

### Concept

`oc debug node` creates an ephemeral privileged debugging environment, then `chroot /host` exposes the real RHCOS node filesystem/services.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc debug node/<NODE>
# inside:
chroot /host
systemctl status kubelet
systemctl status crio
```

### Expected Evidence

Node troubleshooting is possible without permanent SSH configuration.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Capture evidence and exit without making undocumented host changes.

---

## Advanced Deep Dive 114 — CRI-O Troubleshooting

### Concept

CRI-O is the container runtime. Node issues such as image pulls, container creation, runtime crashes, and storage can require CRI-O journal/runtime evidence.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc debug node/<NODE> -- chroot /host journalctl -u crio -b --no-pager | tail -100
```

### Expected Evidence

Runtime errors can be correlated with Pod events.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use CRI-O evidence rather than Docker commands on OpenShift nodes.

---

## Advanced Deep Dive 115 — Kubelet Troubleshooting

### Concept

Kubelet drives Pod lifecycle on each node. Node NotReady, mount, CNI, certificate, eviction, and static-Pod symptoms often appear in kubelet logs.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc debug node/<NODE> -- chroot /host journalctl -u kubelet -b --no-pager | tail -120
```

### Expected Evidence

Node-agent errors are available even when a workload has no useful logs.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Preserve kubelet evidence before rebooting or replacing a node.

---

## Advanced Deep Dive 116 — Node NotReady Tree

### Concept

Node NotReady can stem from kubelet, CRI-O, OVN, API reachability, certificate/time, memory/disk/PID pressure, or MCO state.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc describe node <NODE>
oc get mcp
oc get pods -n openshift-ovn-kubernetes -o wide 2>/dev/null || true
```

### Expected Evidence

Conditions/events identify the failing subsystem.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Compare bad node state with a healthy peer before broad cluster changes.

---

## Advanced Deep Dive 117 — Disk Pressure

### Concept

Node local disk can be consumed by images, writable layers, logs, emptyDir, runtime metadata, or inode exhaustion.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc debug node/<NODE> -- chroot /host df -h
oc debug node/<NODE> -- chroot /host df -i
```

### Expected Evidence

Byte and inode pressure are separated.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use supported runtime/kubelet cleanup and log retention, not random file deletion.

---

## Advanced Deep Dive 118 — Monitoring Stack Mental Model

### Concept

OpenShift monitoring separates cluster platform monitoring from optional user workload monitoring while using Prometheus ecosystem components.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
cluster components
  ↓ metrics
platform Prometheus
  ↓ alerts/dashboards

user workloads
  ↓ ServiceMonitor/PodMonitor
user workload monitoring
```

### Expected Evidence

Platform and application metric ownership are clear.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not edit Operator-managed monitoring Deployments directly.

---

## Advanced Deep Dive 119 — User Workload Monitoring

### Concept

User-workload monitoring allows application namespaces to define metrics discovery and alerting through supported ServiceMonitor/PodMonitor/PrometheusRule resources.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc api-resources | grep -E 'servicemonitor|podmonitor|prometheusrule'
```

### Expected Evidence

Monitoring CRDs are available when the stack is enabled.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Give application teams project-scoped monitoring permissions rather than platform-admin access.

---

## Advanced Deep Dive 120 — ServiceMonitor Selection

### Concept

A ServiceMonitor discovers Services/endpoints by labels. Missing metrics often come from selector, namespace, port name, TLS, or RBAC mismatches.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get servicemonitor -A
oc get svc -n <PROJECT> --show-labels
```

### Expected Evidence

Monitor selector and Service labels can be compared.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Debug discovery before changing Prometheus scrape intervals.

---

## Advanced Deep Dive 121 — PrometheusRule Quality

### Concept

Alerts should include a meaningful threshold, sustained duration, severity, owner, runbook, and user/platform impact.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```yaml
labels:
  severity: warning
annotations:
  runbook_url: https://runbooks.example/...
```

### Expected Evidence

Alert metadata directs an operator toward the correct response.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Page only on actionable sustained conditions.

---

## Advanced Deep Dive 122 — OpenShift Logging Data Flow

### Concept

Modern logging commonly uses a collector, forwarding configuration, Loki/object storage, and external SIEM outputs depending on installed Operators.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
container/platform/audit logs
  ↓ collector
  ├─ Loki
  ├─ SIEM
  └─ external logging
```

### Expected Evidence

Log ownership, retention, and destinations are explicit.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Treat audit logs and application logs with different retention/access requirements where needed.

---

## Advanced Deep Dive 123 — ClusterLogForwarder

### Concept

ClusterLogForwarder-style APIs define which input classes go to which outputs and can reduce unnecessary log duplication.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc api-resources | grep -i clusterlogforwarder
```

### Expected Evidence

The installed logging API/version can be identified.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Review filters and output credentials before enabling forwarding.

---

## Advanced Deep Dive 124 — Log Retention and Cost

### Concept

Metrics, logs, traces, and network flows have different cardinality and cost profiles. Retention should reflect incident/compliance needs rather than defaulting to maximum.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
metrics: medium volume
logs: high volume
traces: sampled high-cardinality
flows: potentially massive
```

### Expected Evidence

Retention/storage budget is defined per telemetry class.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Set explicit retention, sampling, and access policy.

---

## Advanced Deep Dive 125 — Network Observability

### Concept

Network Observability collects flow metadata that can answer who communicated with whom, volumes, DNS behavior, and selected policy/network symptoms.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get flowcollectors -A 2>/dev/null || true
```

### Expected Evidence

Flow collection configuration is visible when installed.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Control sampling and storage to avoid uncontrolled telemetry growth.

---

## Advanced Deep Dive 126 — OpenTelemetry

### Concept

OpenTelemetry collects vendor-neutral traces, metrics, and logs from applications and platform components through collectors.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
app instrumentation
  ↓ OTel collector
  ↓
trace/metric/log backends
```

### Expected Evidence

Request traces can be correlated with Route, Service, and Pod behavior.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Instrument applications for user-path visibility, not just cluster metrics.

---

## Advanced Deep Dive 127 — GitOps Source of Truth

### Concept

OpenShift GitOps/Argo CD can continuously reconcile cluster resources from Git. Manual edits may be reverted because Git, not live YAML, is authoritative.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
Git
  ↓ Argo CD
OpenShift API
  ↓ Operators/controllers
live state
```

### Expected Evidence

Drift ownership is understood before emergency edits.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Identify GitOps ownership before changing managed resources.

---

## Advanced Deep Dive 128 — GitOps Project Boundaries

### Concept

Argo CD projects, repository credentials, cluster destinations, and resource allow/deny policy create the GitOps security boundary.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
repo
  ↓ Argo project
allowed namespaces/clusters
  ↓ sync
```

### Expected Evidence

A GitOps application cannot deploy outside approved destinations when configured correctly.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Separate platform and application GitOps identities.

---

## Advanced Deep Dive 129 — OpenShift Pipelines Identity

### Concept

Tekton Tasks/Pipelines run as Pods and can access source, secrets, registries, and deployment APIs. Their ServiceAccounts are supply-chain identities.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
clone SA
build SA
sign/push SA
deploy SA
```

### Expected Evidence

Pipeline stages can use different least-privilege identities.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not give one pipeline ServiceAccount cluster-admin for convenience.

---

## Advanced Deep Dive 130 — Tekton Workspace/Secret Handling

### Concept

Pipeline workspaces and Secrets can unintentionally persist or expose credentials between Tasks if designed carelessly.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
workspace
  + source
  + artifacts
secret mounts
  ↓ task pods
```

### Expected Evidence

Credential and artifact lifetime is explicit.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use short-lived credentials and limit shared workspaces.

---

## Advanced Deep Dive 131 — Cluster Update Preconditions

### Concept

A production update should start only when ClusterOperators are healthy, MCPs updated, critical Operators compatible, backup current, capacity sufficient, and no blocking Upgradeable condition exists.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co
oc get mcp
oc get clusterversion
oc adm upgrade
```

### Expected Evidence

Go/no-go criteria are evidence-based.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Stop the change if a precondition fails.

---

## Advanced Deep Dive 132 — Update Channels and Graph

### Concept

OpenShift update channels and graph define supported upgrade edges. Not every version can move directly to every newer version.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc adm upgrade
oc get clusterversion version -o yaml
```

### Expected Evidence

Available/recommended updates come from the supported graph and cluster conditions.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use supported graph edges instead of specifying arbitrary release images.

---

## Advanced Deep Dive 133 — Upgradeable=False

### Concept

A ClusterOperator may set Upgradeable=False when a configuration or component creates known upgrade risk.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co -o json | jq -r '.items[] | [.metadata.name,([.status.conditions[]|select(.type=="Upgradeable")][0].status),([.status.conditions[]|select(.type=="Upgradeable")][0].message)] | @tsv'
```

### Expected Evidence

The exact blocker and message are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Resolve the blocker rather than overriding it by default.

---

## Advanced Deep Dive 134 — EUS Planning

### Concept

Extended Update Support affects release lifecycle and upgrade timing, but eligibility and dates depend on Red Hat lifecycle/subscription policy.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
release train
  ↓ support window
maintenance/upgrade cadence
  ↓ target next supported release
```

### Expected Evidence

The organization has a documented supported-version deadline.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Check current lifecycle policy rather than relying on memorized dates.

---

## Advanced Deep Dive 135 — Disconnected Mirroring

### Concept

A disconnected cluster requires mirrored release payloads, Operator catalogs/images, and application content in internal registries.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
connected mirror host
  ↓ oc-mirror
internal registry
  ↓ disconnected cluster
```

### Expected Evidence

Every lifecycle artifact has an internal source.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Test the cluster with Internet access blocked.

---

## Advanced Deep Dive 136 — oc-mirror Workflow

### Concept

`oc-mirror` workflows create/update mirrored content sets and cluster mirror configuration. Exact syntax and metadata evolve by release.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
ImageSet configuration
  ↓ mirror operation
registry content
  ↓ generated cluster resources
apply to cluster
```

### Expected Evidence

The mirror process is reproducible and version-controlled.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Follow the documentation matching the live OCP version.

---

## Advanced Deep Dive 137 — Mirror Capacity Planning

### Concept

Mirrors need enough storage for multiple OCP releases, Operator channels, application images, metadata, and retention/rollback history.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```python
release_gb = 25
operator_gb = 80
apps_gb = 300
rollback_factor = 2
print("Approx mirror GB:", (release_gb + operator_gb + apps_gb) * rollback_factor)
```

### Expected Evidence

Capacity includes rollback/retention rather than only one current release.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Monitor mirror growth and garbage collection carefully.

---

## Advanced Deep Dive 138 — Proxy and NO_PROXY

### Concept

Connected enterprise clusters may require proxy configuration for platform egress while cluster-internal/API/Service CIDRs must bypass the proxy.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get proxy cluster -o yaml
```

### Expected Evidence

HTTP/HTTPS proxy and noProxy settings are visible from the supported API.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Include cluster, service, node, registry, and metadata endpoints in a tested noProxy design.

---

## Advanced Deep Dive 139 — Etcd Backup Scope

### Concept

OpenShift etcd backup protects Kubernetes/OpenShift API state, but not external database data, PVC contents, object storage, or every cloud resource.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
etcd backup:
projects, RBAC, Routes, Operator CRs, Secrets, cluster config

separate:
PVC/DB/object data, registry, external services
```

### Expected Evidence

Control-plane recovery and application-data recovery are treated separately.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Define application backup in addition to cluster backup.

---

## Advanced Deep Dive 140 — Etcd Backup Sensitivity

### Concept

An etcd backup contains sensitive API data including Secrets and RBAC. Backup archives require encryption, access control, retention, and off-cluster storage.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
snapshot + static resources
  ↓ encrypted repository
  ↓ restore-tested copy
```

### Expected Evidence

Backup handling matches cluster-credential sensitivity.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Never copy etcd backups to unsecured support shares.

---

## Advanced Deep Dive 141 — OpenShift Restore Runbook

### Concept

A supported restore requires the exact OCP-version procedure, compatible control-plane hosts, static resources, DNS/LB correctness, and post-restore Operator convergence.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
isolate recovery hosts
  ↓ restore etcd/static resources
API returns
  ↓ operators converge
  ↓ validate network/storage/ingress/apps
```

### Expected Evidence

The recovery test proves the whole platform, not just etcd startup.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Practice restore in an isolated clone and record RTO.

---

## Advanced Deep Dive 142 — Cluster RPO vs App RPO

### Concept

Cluster API-state RPO is based on etcd backup frequency; application RPO is based on DB transaction logs, snapshots/backups, and external data replication.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
cluster RPO ≠ application RPO
```

### Expected Evidence

Each state domain has its own recovery objective.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not claim zero data loss because an etcd snapshot exists.

---

## Advanced Deep Dive 143 — RTO Decomposition

### Concept

OpenShift recovery time includes detection, infrastructure, control plane, network, storage, Operators, identity, ingress, data restore, and application validation.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```python
steps = {"detect":5,"infra":20,"control_plane":20,"operators":20,"data":30,"validation":15}
print("Example RTO minutes:", sum(steps.values()))
```

### Expected Evidence

RTO is decomposed into measurable stages.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Measure recovery through game days instead of estimating from one command.

---

## Advanced Deep Dive 144 — must-gather Sensitivity

### Concept

`oc adm must-gather` collects broad platform diagnostics that can include topology, logs, resource specs, certificate metadata, and other sensitive operational information.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc adm must-gather
```

### Expected Evidence

A support archive is produced and handled as sensitive data.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Store/share must-gather only through approved secure channels.

---

## Advanced Deep Dive 145 — oc adm inspect

### Concept

`oc adm inspect` can collect targeted diagnostic information for a specific Operator/resource, reducing scope compared with a full must-gather.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc adm inspect clusteroperator/network
```

### Expected Evidence

A smaller relevant diagnostic dataset is collected.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use targeted inspection first when the affected component is known.

---

## Advanced Deep Dive 146 — Support Case Evidence

### Concept

A high-quality support case includes exact cluster version/ID, time window, symptoms, user impact, recent changes, reproduction, Operator conditions, and must-gather/inspect data.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
version + cluster ID
time window
impact
recent changes
commands/evidence
must-gather
```

### Expected Evidence

Support can start diagnosis without repeatedly requesting baseline information.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Preserve timestamps and avoid unapproved secret sharing.

---

## Advanced Deep Dive 147 — Cluster Health Quick Check

### Concept

A rapid platform assessment should cover ClusterVersion, ClusterOperators, nodes, MachineConfigPools, and failing Pods before deep component analysis.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get clusterversion
oc get co
oc get nodes
oc get mcp
oc get pods -A | grep -Ev 'Running|Completed' || true
```

### Expected Evidence

The first degraded platform layer is visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Use the quick check to scope the incident, not as the final diagnosis.

---

## Advanced Deep Dive 148 — Authentication Operator Failure

### Concept

Authentication can fail while existing ServiceAccount workloads continue. Troubleshoot authentication Operator, OAuth Pods/Route, IdP, certificates, DNS, and ingress.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co authentication
oc -n openshift-authentication get pods
```

### Expected Evidence

Authentication-specific health is separated from overall API health.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Avoid rotating every credential when the IdP/OAuth route is the real failure.

---

## Advanced Deep Dive 149 — Console Operator Failure

### Concept

The web console can fail while API and `oc` work. Console Operator, console Pods, Route, authentication, and ingress are separate dependencies.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co console
oc -n openshift-console get pods,route
```

### Expected Evidence

CLI access can be used to recover the console path.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not equate console outage with cluster outage.

---

## Advanced Deep Dive 150 — Registry Degraded

### Concept

Registry degradation often originates in registry storage, credentials, object-store reachability, image-registry Operator configuration, or registry Pod health.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get co image-registry
oc -n openshift-image-registry get pods
```

### Expected Evidence

The Operator and operand state are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Check storage first when registry Pods restart or refuse writes.

---

## Advanced Deep Dive 151 — ImagePullBackOff on OpenShift

### Concept

ImagePull failures may involve ImageStream, global pull secret, project pull Secret, mirror rules, proxy, registry TLS/DNS, or tag/digest mismatch.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Evidence

Runtime pull error explains which registry/reference failed.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Fix image trust/auth/mirror cause instead of repeatedly recreating the Pod.

---

## Advanced Deep Dive 152 — Build Output Push Failure

### Concept

A build can succeed locally but fail pushing its output because of registry auth, quota, ImageStream target, registry storage, or network.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc logs build/<BUILD> | tail -100
oc get is -n <PROJECT>
```

### Expected Evidence

The failure is isolated to the output/push stage.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Separate build compute success from artifact publication.

---

## Advanced Deep Dive 153 — Route TLS Failure Tree

### Concept

TLS failures can originate at external DNS, router default certificate, route certificate/key, SNI host, passthrough backend cert, re-encrypt destination CA, or certificate expiry.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
openssl s_client -connect <ROUTE_HOST>:443 -servername <ROUTE_HOST> </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Expected Evidence

The externally presented certificate identity and validity are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Trace TLS termination mode before replacing certificates.

---

## Advanced Deep Dive 154 — OVN Node Failure

### Concept

If Pods on one node lose network while other nodes are healthy, investigate OVN node agents, OVS/OVN state, MTU, routes, node interface, and CNO status.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get pods -n openshift-ovn-kubernetes -o wide 2>/dev/null || true
oc get co network
```

### Expected Evidence

The affected node's OVN component can be compared with healthy peers.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Contain the node if needed while preserving network evidence.

---

## Advanced Deep Dive 155 — DNS Failure Tree

### Concept

OpenShift DNS failure should be split into Pod resolver, DNS Service/endpoints, DNS Operator/Pods, NetworkPolicy, node resolver, and upstream DNS.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc run dns-test --rm -it --image=busybox -- nslookup kubernetes.default
```

### Expected Evidence

Cluster-local resolution can be tested independently.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Test internal and external names separately.

---

## Advanced Deep Dive 156 — PVC Pending Tree

### Concept

PVC Pending usually points to StorageClass/CSI/provisioner/topology/quota/capacity, not the application image.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc describe pvc <PVC> -n <PROJECT>
oc get storageclass
```

### Expected Evidence

Provisioning events reveal the blocked layer.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Start with claim events and CSI Operator health.

---

## Advanced Deep Dive 157 — MCP Updating Too Long

### Concept

A long-running MCP update often means one node cannot drain, reboot, become Ready, or apply the desired config.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get mcp
oc get nodes
oc get pdb -A
```

### Expected Evidence

The unavailable node and potential drain blocker are visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Investigate the specific node rather than pausing the whole cluster indefinitely.

---

## Advanced Deep Dive 158 — Webhook Outage

### Concept

An Operator-installed admission or conversion webhook can block API writes when its Service, certificate, DNS, or backend is broken.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get validatingwebhookconfigurations,mutatingwebhookconfigurations
oc get svc,endpointslices -A | grep -i webhook
```

### Expected Evidence

Webhook dependencies can be traced from API config to live endpoints.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Keep high-impact webhooks highly available and monitor certificate expiry.

---

## Advanced Deep Dive 159 — Operator Install Failure Tree

### Concept

Operator install failures should be followed through catalog/lifecycle object → RBAC/CRD/webhook → Operator Pod → managed CR status.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
Catalog
  ↓ Subscription/extension
InstallPlan
  ↓ CSV/Operator
CRD/webhook
  ↓ operand CR
```

### Expected Evidence

The exact failed lifecycle stage is identified.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Do not delete namespaces or CRDs as a first response.

---

## Advanced Deep Dive 160 — Update Blocked Tree

### Concept

Blocked updates commonly come from Upgradeable=False, degraded ClusterOperators, MCP degradation, unsupported Operator state, or unavailable graph edge.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc adm upgrade
oc get co
oc get mcp
oc describe clusterversion version
```

### Expected Evidence

The explicit blocker is visible.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Resolve the blocker before forcing update.

---

## Advanced Deep Dive 161 — Disconnected Pull Failure

### Concept

Disconnected image failures require checking content presence in the mirror, mirror policy, pull Secret, registry TLS, DNS, proxy/noProxy, and image digest.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```bash
oc get imagedigestmirrorsets,imagetagmirrorsets 2>/dev/null || true
```

### Expected Evidence

The source→mirror mapping can be inspected.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Prove the required digest exists in the internal registry.

---

## Advanced Deep Dive 162 — EX280 Persistence Mindset

### Concept

Performance-based exam tasks must persist after restart and reconciliation. Temporary shell commands or manual generated-resource edits are not valid durable administration.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
temporary:
manual edit generated Pod

persistent:
supported resource manifest / Operator config / RBAC / Route / SCC / project policy
```

### Expected Evidence

The solution is represented in cluster desired state.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Practice durable YAML/API-based solutions.

---

## Advanced Deep Dive 163 — EX280 Version Awareness

### Concept

The live OpenShift platform can be newer than the exam environment. Commands/resources that exist in current OCP may not exist in the stated EX280 version.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
production study: current OCP
exam practice: exam-stated OCP version
```

### Expected Evidence

Learners distinguish current operations from exam compatibility.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Verify exam objectives and cluster version before memorizing syntax.

---

## Advanced Deep Dive 164 — OpenShift Operational Readiness

### Concept

A production OpenShift platform needs healthy Operators, identity/RBAC, ingress, networking, registry/mirrors, storage, node pools, SCC/policy, observability, backups, update process, capacity, and support runbooks.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
[ ] ClusterOperators healthy
[ ] identity/RBAC
[ ] SCC/PSA
[ ] OVN/policy
[ ] ingress/routes
[ ] registry/mirror
[ ] storage/backup
[ ] MCO/node capacity
[ ] observability
[ ] updates/DR
[ ] runbooks/support
```

### Expected Evidence

The platform is operable before tenant onboarding.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Make platform readiness a formal launch gate.

---

## Advanced Deep Dive 165 — Evidence-First OpenShift Troubleshooting

### Concept

Strong OpenShift troubleshooting starts with ClusterVersion/ClusterOperators, identifies the owning Operator, then walks to operands, node/network/storage/runtime dependencies, recent changes, and user impact.

### Architecture / Mental Model

```text
User / Developer / Automation
          ↓
      OpenShift API
          ↓
 Kubernetes APIs + OpenShift APIs
          ↓
Cluster Operator / Installed Operator
          ↓
RHCOS + CRI-O + OVN + CSI + Ingress
          ↓
      Application / Data
```

### Command / YAML / Configuration

```text
symptom
  ↓ ClusterOperator?
owning Operator
  ↓ source-of-truth CR
operand status/logs
  ↓ node/network/storage dependency
small correction
  ↓ verify
```

### Expected Evidence

The failed layer is isolated before remediation.

### Why It Works

OpenShift is a Kubernetes distribution operated as an integrated product. Most major platform components are reconciled by Operators, the Cluster Version Operator controls release composition, the Machine Config Operator controls node operating-system state, and application traffic/data/security depend on supported OpenShift APIs layered over Kubernetes. Troubleshooting becomes reliable when the administrator first identifies the owning Operator and its source-of-truth resource, then validates the generated operands and lower Linux/network/storage dependencies.

### Production Example

For a production OpenShift service or platform component, record the owning Operator, source-of-truth CR, release/channel, node placement, network path, storage dependency, identity/RBAC, SCC/PSA posture, certificates, observability, backup/restore, maintenance/upgrade policy, and support owner.

### Troubleshooting Workflow

```text
Verify cluster/user/project
   ↓
ClusterVersion + ClusterOperators
   ↓
Identify owning Operator
   ↓
Inspect source-of-truth CR + conditions
   ↓
Inspect operand Pods/events/logs
   ↓
Inspect RHCOS/CRI-O/OVN/CSI/Ingress dependency
   ↓
Check recent config/update/change
   ↓
Make smallest supported correction
   ↓
Verify platform + application path
   ↓
Document prevention
```

### Common Mistakes

- Editing Operator-owned generated resources.
- Treating RHCOS like a manually patched traditional server.
- Granting `cluster-admin`, `anyuid`, or privileged SCC to bypass a narrow problem.
- Assuming a Route problem is automatically an ingress problem.
- Installing an Operator without reviewing its permissions and CRDs.
- Upgrading while ClusterOperators or MCPs are degraded.
- Treating etcd backup as an application-data backup.

### Best Practice

Preserve evidence, change one variable at a time, and document prevention.

---

# Supplemental Hands-on Lab Series — OpenShift

## Enhanced OpenShift Lab 1 — Operator Ownership and Source of Truth

### Objective

Turn **Operator Ownership and Source of Truth** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get clusteroperators
oc get deploy -A | grep -i operator
oc describe clusteroperator ingress
```

### Expected Result

The owning Operator and its status/message are identified before any change is made.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Change the supported Operator custom resource or configuration API, not generated operands.

---

## Enhanced OpenShift Lab 2 — ClusterVersion as Platform Desired State

### Objective

Turn **ClusterVersion as Platform Desired State** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get clusterversion
oc describe clusterversion version
```

### Expected Result

Desired version, history, channel, available updates, and conditions are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use ClusterVersion/CVO as the supported release lifecycle instead of upgrading core components individually.

---

## Enhanced OpenShift Lab 3 — ClusterOperator Condition Interpretation

### Objective

Turn **ClusterOperator Condition Interpretation** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co
oc get co network -o jsonpath='{range .status.conditions[*]}{.type}={.status}{" reason="}{.reason}{"\n"}{end}'
```

### Expected Result

The exact condition reason is visible instead of relying on a green/red summary.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Read Operator conditions and messages before restarting operands.

---

## Enhanced OpenShift Lab 4 — Release Payload Mental Model

### Objective

Turn **Release Payload Mental Model** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
release image
  ↓ verified payload
Cluster Version Operator
  ↓
Cluster Operators
  ↓
platform operands + RHCOS rollout
```

### Expected Result

The platform version is treated as one tested composition rather than independent package versions.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Upgrade through supported release graph edges.

---

## Enhanced OpenShift Lab 5 — CVO Failure Decomposition

### Objective

Turn **CVO Failure Decomposition** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get clusterversion
oc get co
oc get mcp
oc get events -A --sort-by=.metadata.creationTimestamp | tail -60
```

### Expected Result

The first non-converged layer is identified.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not force past upgrade blockers without understanding the reported risk.

---

## Enhanced OpenShift Lab 6 — RHCOS Immutable Node Model

### Objective

Turn **RHCOS Immutable Node Model** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get nodes -o wide
oc debug node/<NODE> -- chroot /host rpm-ostree status 2>/dev/null || true
```

### Expected Result

The node OS image/state can be inspected without treating the node as a traditional mutable server.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use MachineConfig and supported Operators for persistent node changes.

---

## Enhanced OpenShift Lab 7 — MachineConfig Merge

### Objective

Turn **MachineConfig Merge** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get mc
oc get mcp worker -o jsonpath='{.status.configuration.name}{"\n"}'
```

### Expected Result

The current rendered configuration name is visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Review all matching MachineConfigs before assuming which object caused a node change.

---

## Enhanced OpenShift Lab 8 — MachineConfigPool Rollout

### Objective

Turn **MachineConfigPool Rollout** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get mcp
oc describe mcp worker
```

### Expected Result

Updated, updating, degraded, ready, and unavailable machine counts are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Treat MCO changes like node-maintenance events with N-1 capacity.

---

## Enhanced OpenShift Lab 9 — MCP Degraded Diagnosis

### Objective

Turn **MCP Degraded Diagnosis** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get mcp
oc -n openshift-machine-config-operator get pods -o wide
oc -n openshift-machine-config-operator logs ds/machine-config-daemon --tail=100
```

### Expected Result

The affected pool/node and MCD error can be correlated.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Fix the actual node/config drift instead of deleting the pool or rendered config.

---

## Enhanced OpenShift Lab 10 — MCD Current vs Desired Configuration

### Objective

Turn **MCD Current vs Desired Configuration** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get node <NODE> -o jsonpath='{.metadata.annotations.machineconfiguration\.openshift\.io/currentConfig}{" current\n"}{.metadata.annotations.machineconfiguration\.openshift\.io/desiredConfig}{" desired\n"}'
```

### Expected Result

Current and desired rendered configurations can be compared.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use node annotations plus MCD logs to isolate rollout failures.

---

## Enhanced OpenShift Lab 11 — Control Plane vs Worker Pools

### Objective

Turn **Control Plane vs Worker Pools** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get mcp master worker
```

### Expected Result

Each pool's rollout state is independent and visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Apply the strictest change control to control-plane MachineConfig changes.

---

## Enhanced OpenShift Lab 12 — Custom MachineConfigPool

### Objective

Turn **Custom MachineConfigPool** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
worker pool
  ├─ general nodes
custom infra pool
  ├─ ingress/registry nodes
custom performance pool
  └─ low-latency nodes
```

### Expected Result

Specialized configuration is isolated to intended nodes.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use custom pools only when the operational need justifies extra lifecycle complexity.

---

## Enhanced OpenShift Lab 13 — MachineConfig Rollback

### Objective

Turn **MachineConfig Rollback** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
bad MC applied
  ↓ MCP rolls out
problem detected
  ↓ revert/delete custom MC
MCO renders corrected config
  ↓ nodes converge
```

### Expected Result

The rollback returns nodes to a supported rendered configuration.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Keep a version-controlled copy of every custom MachineConfig.

---

## Enhanced OpenShift Lab 14 — Installation Dependency Graph

### Objective

Turn **Installation Dependency Graph** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
DNS + LB + hosts
  ↓
bootstrap
  ↓
control-plane
  ↓
CNI/network
  ↓
operators
  ↓
cluster complete
```

### Expected Result

The failed installation stage can be placed in the dependency graph.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Troubleshoot the earliest failed dependency instead of repeatedly rerunning the installer.

---

## Enhanced OpenShift Lab 15 — IPI vs UPI Responsibility

### Objective

Turn **IPI vs UPI Responsibility** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
IPI: installer → infra + cluster
UPI: admin → infra, installer/assets → cluster
```

### Expected Result

Ownership of infrastructure creation and failure diagnosis is explicit.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Choose the model based on platform support and organizational infrastructure control.

---

## Enhanced OpenShift Lab 16 — Assisted Installation

### Objective

Turn **Assisted Installation** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
hosts boot discovery
  ↓ inventory/validation
assisted service
  ↓ install config
  ↓ cluster bootstrap
```

### Expected Result

Host validation failures are visible before cluster installation begins.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Resolve discovery validation errors rather than bypassing them.

---

## Enhanced OpenShift Lab 17 — Agent-Based Installation

### Objective

Turn **Agent-Based Installation** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
install-config + agent-config
  ↓ generate ISO
hosts boot
  ↓ agent discovery
  ↓ bootstrap/install
```

### Expected Result

Cluster intent and host mapping are predeclared and reproducible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Keep generated assets protected because they can contain cluster credentials/configuration.

---

## Enhanced OpenShift Lab 18 — Bootstrap Completion

### Objective

Turn **Bootstrap Completion** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
openshift-install wait-for bootstrap-complete --dir=<DIR> --log-level=debug
```

### Expected Result

The installer explicitly reports bootstrap completion.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Remove bootstrap infrastructure only after the supported completion signal.

---

## Enhanced OpenShift Lab 19 — Install Config Security

### Objective

Turn **Install Config Security** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
chmod 600 install-config.yaml
```

### Expected Result

The file is readable only by the intended operator account.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Treat installation assets as sensitive cluster-bootstrap material.

---

## Enhanced OpenShift Lab 20 — OpenShift DNS Prerequisites

### Objective

Turn **OpenShift DNS Prerequisites** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
dig api.<cluster>.<baseDomain>
dig api-int.<cluster>.<baseDomain>
dig test.apps.<cluster>.<baseDomain>
```

### Expected Result

Each critical name resolves to the intended load-balancer/address.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Validate DNS from bootstrap/control-plane/worker network paths before install.

---

## Enhanced OpenShift Lab 21 — API Load Balancer

### Objective

Turn **API Load Balancer** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
curl -k https://api.<cluster>.<baseDomain>:6443/readyz 2>/dev/null || true
```

### Expected Result

The API endpoint responds through the load balancer when the backend is ready.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Make API LB itself highly available and monitor backend readiness.

---

## Enhanced OpenShift Lab 22 — Ingress Load Balancer

### Objective

Turn **Ingress Load Balancer** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
*.apps DNS
  ↓ external/internal LB
router Pods
  ↓ Route
Service
```

### Expected Result

North-south traffic has a documented LB→router path.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Keep ingress LB and API LB roles separate.

---

## Enhanced OpenShift Lab 23 — Pull Secret Lifecycle

### Objective

Turn **Pull Secret Lifecycle** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get secret pull-secret -n openshift-config -o jsonpath='{.data.\.dockerconfigjson}' >/dev/null
```

### Expected Result

The secret exists at the expected cluster location without printing its value.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Never paste the pull secret into tickets or shell history.

---

## Enhanced OpenShift Lab 24 — kubeadmin Retirement

### Objective

Turn **kubeadmin Retirement** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get secret kubeadmin -n kube-system 2>/dev/null || true
```

### Expected Result

The team can verify whether temporary bootstrap credentials still exist.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Retire bootstrap identities after enterprise admin access is proven.

---

## Enhanced OpenShift Lab 25 — oc Context Safety

### Objective

Turn **oc Context Safety** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc whoami
oc whoami --show-server
oc project
```

### Expected Result

Operator identity, API endpoint, and project are visible before a write.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Make context verification part of every change runbook.

---

## Enhanced OpenShift Lab 26 — Projects as Policy Boundaries

### Objective

Turn **Projects as Policy Boundaries** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get project <PROJECT> -o yaml
oc get rolebinding,resourcequota,limitrange,networkpolicy -n <PROJECT>
```

### Expected Result

The project's policy controls can be inspected together.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Provision projects from a standard baseline, not as empty namespaces.

---

## Enhanced OpenShift Lab 27 — Project Request Template

### Objective

Turn **Project Request Template** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
new project request
  ↓ project template
namespace/project
  + quota
  + limits
  + RBAC
  + network policy
```

### Expected Result

New projects begin compliant by default.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use templates/automation to eliminate repetitive manual tenant setup.

---

## Enhanced OpenShift Lab 28 — ClusterResourceQuota

### Objective

Turn **ClusterResourceQuota** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get clusterresourcequota
```

### Expected Result

Cross-project quota policy and usage are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use aggregate quota for team-level governance while retaining per-project quotas where useful.

---

## Enhanced OpenShift Lab 29 — LimitRange Defaults

### Objective

Turn **LimitRange Defaults** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get limitrange -A
oc describe limitrange -n <PROJECT>
```

### Expected Result

Default/min/max constraints are explicit.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Pair LimitRange defaults with measurement-driven right-sizing.

---

## Enhanced OpenShift Lab 30 — ResourceQuota Admission

### Objective

Turn **ResourceQuota Admission** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc describe resourcequota -n <PROJECT>
```

### Expected Result

Used vs hard quota identifies whether admission is blocking creation.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Read the API error before changing node capacity.

---

## Enhanced OpenShift Lab 31 — Developer Self-Service Guardrails

### Objective

Turn **Developer Self-Service Guardrails** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
developer
  ↓ project-scoped RBAC
create workload
  ↓ quota / SCC / PSA / NetworkPolicy / policy
safe platform execution
```

### Expected Result

Developers can move quickly without bypassing platform governance.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Design guardrails rather than ticket-driven manual approvals for routine work.

---

## Enhanced OpenShift Lab 32 — OAuth Authentication Flow

### Objective

Turn **OAuth Authentication Flow** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
user
  ↓ IdP
OAuth
  ↓ token
OpenShift API
  ↓ RBAC
allowed / denied
```

### Expected Result

Login success can be separated from authorization failure.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Troubleshoot identity provider, OAuth route/certs, and RBAC independently.

---

## Enhanced OpenShift Lab 33 — OIDC Federation

### Objective

Turn **OIDC Federation** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
enterprise IdP
  ↓ signed ID token
OpenShift authentication
  ↓ user/groups
RBAC
```

### Expected Result

Identity claims map predictably to cluster users/groups.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use short-lived IdP-managed identities and MFA for human access.

---

## Enhanced OpenShift Lab 34 — LDAP Integration

### Objective

Turn **LDAP Integration** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
OpenShift OAuth
  ↓ LDAPS
directory
  ↓ user DN/attributes
mapped OpenShift user
```

### Expected Result

User lookup and TLS trust can be tested independently of RBAC.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Avoid broad directory searches and plaintext LDAP.

---

## Enhanced OpenShift Lab 35 — Group-Centric RBAC

### Objective

Turn **Group-Centric RBAC** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc adm groups new app-devs
oc adm policy add-role-to-group edit app-devs -n orders-dev
```

### Expected Result

Project access follows group membership.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Bind roles to identity-provider groups where possible.

---

## Enhanced OpenShift Lab 36 — admin vs edit vs view

### Objective

Turn **admin vs edit vs view** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc auth can-i --list -n <PROJECT>
```

### Expected Result

Effective verbs/resources can be reviewed rather than assumed from role name.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Test actual permissions before assigning broad roles.

---

## Enhanced OpenShift Lab 37 — Cluster-Admin Audit

### Objective

Turn **Cluster-Admin Audit** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get clusterrolebindings -o json | jq -r '.items[] | select(.roleRef.name=="cluster-admin") | .metadata.name'
```

### Expected Result

Cluster-admin bindings can be enumerated.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use project-scoped roles for application teams and break-glass for emergency access.

---

## Enhanced OpenShift Lab 38 — ServiceAccount Identity

### Objective

Turn **ServiceAccount Identity** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc create sa orders-api -n orders
oc auth can-i get configmaps --as=system:serviceaccount:orders:orders-api -n orders
```

### Expected Result

The exact workload identity and its effective access are verifiable.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

One ServiceAccount should represent one coherent application capability.

---

## Enhanced OpenShift Lab 39 — Bound ServiceAccount Tokens

### Objective

Turn **Bound ServiceAccount Tokens** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc create token orders-api -n orders --duration=10m
```

### Expected Result

A temporary token is issued without creating a permanent Secret.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Disable automount for workloads that never call the cluster API.

---

## Enhanced OpenShift Lab 40 — SCC Admission Mental Model

### Objective

Turn **SCC Admission Mental Model** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
Pod spec
  + caller identity
  + authorized SCCs
  ↓ SCC admission
selected SCC / rejection
```

### Expected Result

A denial can be traced to one requested privilege that no allowed SCC permits.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Fix the workload first; grant a broader SCC only when the requirement is justified.

---

## Enhanced OpenShift Lab 41 — Default SCC Immutability

### Objective

Turn **Default SCC Immutability** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get scc
```

### Expected Result

Default and custom SCCs can be distinguished.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Create a narrowly scoped custom SCC instead of modifying built-ins.

---

## Enhanced OpenShift Lab 42 — Arbitrary UID Image Design

### Objective

Turn **Arbitrary UID Image Design** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```dockerfile
RUN mkdir -p /opt/app/data  && chgrp -R 0 /opt/app  && chmod -R g=u /opt/app
```

### Expected Result

A random non-root UID can read/write required paths without world-writable permissions.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Design images for arbitrary UID rather than granting anyuid.

---

## Enhanced OpenShift Lab 43 — SCC Denial Diagnostics

### Objective

Turn **SCC Denial Diagnostics** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc describe pod <POD> -n <PROJECT> | sed -n '/Events:/,$p'
```

### Expected Result

Admission error text identifies which requested security settings are incompatible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Read the denial before assigning a more permissive SCC.

---

## Enhanced OpenShift Lab 44 — SCC Use Authorization

### Objective

Turn **SCC Use Authorization** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc adm policy who-can use scc/privileged
oc adm policy who-can use scc/anyuid
```

### Expected Result

Users/groups/ServiceAccounts with powerful SCC access are enumerated.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Review powerful SCC usage regularly.

---

## Enhanced OpenShift Lab 45 — Custom SCC Governance

### Objective

Turn **Custom SCC Governance** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
legacy app requirement
  ↓ identify exact missing permission
custom SCC
  ↓ bind only serviceaccount X
```

### Expected Result

The exception has limited blast radius.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Document each custom SCC as a security exception ADR.

---

## Enhanced OpenShift Lab 46 — SCC and PSA Together

### Objective

Turn **SCC and PSA Together** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
namespace PSA labels
  ↓ baseline/restricted policy
Pod create
  ↓ SCC authorization/defaulting
admitted only if both paths allow it
```

### Expected Result

Policy behavior is understood as layered admission.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Test both controls when a hardened Pod is unexpectedly rejected.

---

## Enhanced OpenShift Lab 47 — SELinux Confinement

### Objective

Turn **SELinux Confinement** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc debug node/<NODE> -- chroot /host ls -Z /var/lib/kubelet 2>/dev/null | head
```

### Expected Result

SELinux labels are visible on the host.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Fix supported labels/policies rather than disabling SELinux.

---

## Enhanced OpenShift Lab 48 — allowPrivilegeEscalation

### Objective

Turn **allowPrivilegeEscalation** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```yaml
securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop: ["ALL"]
```

### Expected Result

The Pod requests a restricted runtime privilege set.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use the smallest security context that still allows the application to function.

---

## Enhanced OpenShift Lab 49 — Seccomp RuntimeDefault

### Objective

Turn **Seccomp RuntimeDefault** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```yaml
securityContext:
  seccompProfile:
    type: RuntimeDefault
```

### Expected Result

The workload explicitly requests the runtime's default seccomp confinement.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Prefer RuntimeDefault over Unconfined.

---

## Enhanced OpenShift Lab 50 — Security Profiles Operator

### Objective

Turn **Security Profiles Operator** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
profile CR
  ↓ Security Profiles Operator
node profile installation
  ↓ workload references profile
```

### Expected Result

Custom profile lifecycle is cluster-managed rather than manually copied to nodes.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use custom profiles only after measuring the workload's required behavior.

---

## Enhanced OpenShift Lab 51 — Compliance Operator

### Objective

Turn **Compliance Operator** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get compliancesuites,compliancescans -A 2>/dev/null || true
```

### Expected Result

Scan state/findings are visible when the Operator is installed.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Treat automated remediation as change input, not something to apply blindly.

---

## Enhanced OpenShift Lab 52 — External Secret Integration

### Objective

Turn **External Secret Integration** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
workload identity
  ↓ external secret store
operator/CSI integration
  ↓ projected/synced secret
application
```

### Expected Result

Secret lifecycle is tied to an external source of truth.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use least-privilege workload identity and rotation.

---

## Enhanced OpenShift Lab 53 — Route vs Ingress

### Objective

Turn **Route vs Ingress** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get routes -A
oc get ingress -A
```

### Expected Result

The exposure resource used by each application is clear.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Choose one supported edge model and document TLS termination.

---

## Enhanced OpenShift Lab 54 — Edge Route TLS

### Objective

Turn **Edge Route TLS** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
client HTTPS
  ↓ TLS terminates
OpenShift router
  ↓ HTTP/backend
Service
```

### Expected Result

The router owns the public certificate/private key.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use edge termination only when plaintext or alternate backend protection is acceptable.

---

## Enhanced OpenShift Lab 55 — Passthrough Route TLS

### Objective

Turn **Passthrough Route TLS** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
client TLS
  ↓ router selects by SNI
unchanged TLS
  ↓ backend Pod
```

### Expected Result

The backend presents and owns the TLS certificate.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use passthrough when end-to-end application TLS ownership is required.

---

## Enhanced OpenShift Lab 56 — Re-encrypt Route TLS

### Objective

Turn **Re-encrypt Route TLS** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
client TLS
  ↓ terminate
router
  ↓ new TLS validated with destination CA
backend
```

### Expected Result

Both frontend and backend trust chains can be validated separately.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Maintain destination CA and backend certificate rotation carefully.

---

## Enhanced OpenShift Lab 57 — Route Admission Status

### Objective

Turn **Route Admission Status** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get route <ROUTE> -o yaml | sed -n '/status:/,$p'
```

### Expected Result

Admitted/host conditions explain whether a router accepted the Route.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Check admission before debugging the backend application.

---

## Enhanced OpenShift Lab 58 — Route 503 Decomposition

### Objective

Turn **Route 503 Decomposition** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get route <ROUTE>
oc get svc <SVC>
oc get endpointslices -l kubernetes.io/service-name=<SVC>
oc get pods -o wide
```

### Expected Result

The failure is narrowed from Route to Service to endpoint to Pod.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Trace north-south traffic one hop at a time.

---

## Enhanced OpenShift Lab 59 — IngressController Source of Truth

### Objective

Turn **IngressController Source of Truth** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc -n openshift-ingress-operator get ingresscontroller
oc -n openshift-ingress get pods -o wide
```

### Expected Result

The supported source-of-truth resource and generated router Pods are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Never make persistent changes directly to router Deployments.

---

## Enhanced OpenShift Lab 60 — Ingress Sharding

### Objective

Turn **Ingress Sharding** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
public IngressController
  ↓ routeSelector=public

internal IngressController
  ↓ namespaceSelector=internal
```

### Expected Result

Routes are admitted only by the intended router set.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use sharding for real network/certificate/tenancy boundaries, not cosmetic separation.

---

## Enhanced OpenShift Lab 61 — Ingress Certificate Lifecycle

### Objective

Turn **Ingress Certificate Lifecycle** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc -n openshift-ingress-operator get ingresscontroller default -o yaml
```

### Expected Result

The configured certificate reference and ingress status can be inspected.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Monitor certificate expiry and chain validity.

---

## Enhanced OpenShift Lab 62 — OVN-Kubernetes Mental Model

### Objective

Turn **OVN-Kubernetes Mental Model** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
Pod
  ↓ veth/interface
OVN logical switch/router
  ↓ node dataplane
underlay
  ↓ remote node/Pod
```

### Expected Result

Packet failures can be localized to Pod, OVN, node, or external network.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Troubleshoot through OpenShift/OVN APIs and supported tooling instead of manually editing OVN databases.

---

## Enhanced OpenShift Lab 63 — Cluster Network Operator

### Objective

Turn **Cluster Network Operator** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co network
oc -n openshift-network-operator get pods
```

### Expected Result

Operator health and namespace workloads are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Start at CNO conditions before application-specific workarounds.

---

## Enhanced OpenShift Lab 64 — Pod/Service CIDR Governance

### Objective

Turn **Pod/Service CIDR Governance** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get network.config.openshift.io cluster -o yaml
```

### Expected Result

Cluster and Service CIDRs can be inspected from the supported config API.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Document IPAM before installation and reserve growth capacity.

---

## Enhanced OpenShift Lab 65 — OVN MTU

### Objective

Turn **OVN MTU** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc debug node/<NODE> -- chroot /host ip link
```

### Expected Result

Node/interface MTUs are visible for comparison with overlay requirements.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Plan MTU from the real underlay and encapsulation overhead.

---

## Enhanced OpenShift Lab 66 — NetworkPolicy Default Deny

### Objective

Turn **NetworkPolicy Default Deny** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```yaml
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Expected Result

Selected Pods are isolated except for separately allowed flows.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Allow DNS and required dependencies before enabling egress deny.

---

## Enhanced OpenShift Lab 67 — NetworkPolicy Project Labels

### Objective

Turn **NetworkPolicy Project Labels** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get ns --show-labels
```

### Expected Result

Labels referenced by policy can be audited.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Govern security-significant labels so tenant users cannot self-escalate network access.

---

## Enhanced OpenShift Lab 68 — EgressFirewall

### Objective

Turn **EgressFirewall** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get egressfirewall -A 2>/dev/null || true
```

### Expected Result

Existing egress firewall objects and scope are visible where supported.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Treat DNS, proxies, registries, APIs, and update endpoints as explicit dependencies.

---

## Enhanced OpenShift Lab 69 — EgressIP

### Objective

Turn **EgressIP** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get egressips.k8s.ovn.org -A 2>/dev/null || true
```

### Expected Result

Configured egress identities can be inspected.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Provide redundancy so one node failure does not remove all egress IP capacity.

---

## Enhanced OpenShift Lab 70 — Admin Network Policy Concept

### Objective

Turn **Admin Network Policy Concept** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
admin baseline policy
  ↓
tenant NetworkPolicy
  ↓
OVN enforcement
```

### Expected Result

Platform and tenant policy responsibilities are separated.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Verify exact OCP support/maturity before production adoption.

---

## Enhanced OpenShift Lab 71 — Multus Secondary Networks

### Objective

Turn **Multus Secondary Networks** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get network-attachment-definitions -A
```

### Expected Result

Secondary network definitions can be inventoried.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Document routing, IPAM, security, and failure behavior for every secondary interface.

---

## Enhanced OpenShift Lab 72 — NetworkAttachmentDefinition

### Objective

Turn **NetworkAttachmentDefinition** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: storage-net
```

### Expected Result

The secondary network exists as an API object.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Keep plugin configuration and IPAM version-controlled.

---

## Enhanced OpenShift Lab 73 — SR-IOV Scheduling

### Objective

Turn **SR-IOV Scheduling** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get node -o json | jq -r '.items[] | [.metadata.name,.status.allocatable] | @json' | head
```

### Expected Result

Specialized allocatable resources can be inspected.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use dedicated node pools and capacity planning for SR-IOV workloads.

---

## Enhanced OpenShift Lab 74 — NMState Change Safety

### Objective

Turn **NMState Change Safety** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get nncp,nnce 2>/dev/null || true
```

### Expected Result

Desired policies and per-node enactment status are visible where NMState is installed.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Canary node network changes and maintain out-of-band recovery access.

---

## Enhanced OpenShift Lab 75 — LoadBalancer Service on Bare Metal

### Objective

Turn **LoadBalancer Service on Bare Metal** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get svc -A | grep LoadBalancer
oc get metallb -A 2>/dev/null || true
```

### Expected Result

Pending external IPs can be correlated with the installed LB implementation.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not assume cloud-provider behavior exists on-premises.

---

## Enhanced OpenShift Lab 76 — MetalLB BGP/L2 Trade-Off

### Objective

Turn **MetalLB BGP/L2 Trade-Off** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
L2 mode → ARP/NDP advertisement
BGP mode → route advertisement to peers
```

### Expected Result

The external path is documented and owned jointly with the network team.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Treat address pools and BGP policy as production network configuration.

---

## Enhanced OpenShift Lab 77 — DNS Operator Source of Truth

### Objective

Turn **DNS Operator Source of Truth** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co dns
oc get dns.operator/default -o yaml
```

### Expected Result

The supported DNS configuration object is visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Avoid editing generated CoreDNS workloads directly.

---

## Enhanced OpenShift Lab 78 — Route/DNS End-to-End Test

### Objective

Turn **Route/DNS End-to-End Test** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
curl -vk https://<ROUTE_HOST>/ 2>&1 | head -30
oc get route,svc,endpointslices -n <PROJECT>
```

### Expected Result

External TLS/HTTP behavior can be correlated with cluster resources.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Verify the whole north-south path after ingress changes.

---

## Enhanced OpenShift Lab 79 — Integrated Registry Operator

### Objective

Turn **Integrated Registry Operator** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co image-registry
oc get configs.imageregistry.operator.openshift.io cluster -o yaml
```

### Expected Result

Registry health and source-of-truth configuration are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Never persistently edit the generated registry Deployment.

---

## Enhanced OpenShift Lab 80 — Registry Storage Durability

### Objective

Turn **Registry Storage Durability** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
registry Pods
  ↓ durable object/file storage
  ↓ image layers/manifests
```

### Expected Result

Registry persistence is separate from the registry Deployment lifecycle.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Monitor storage capacity and backup/recovery requirements.

---

## Enhanced OpenShift Lab 81 — ImageStream Tag vs Digest

### Objective

Turn **ImageStream Tag vs Digest** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get is <NAME> -o yaml
oc get istag <NAME>:<TAG> -o yaml
```

### Expected Result

Tag history and resolved image digest can be inspected.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Promote immutable digests through environments.

---

## Enhanced OpenShift Lab 82 — Image Change Triggers

### Objective

Turn **Image Change Triggers** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc set triggers deployment/<DEPLOYMENT>
```

### Expected Result

Configured image/config triggers can be reviewed.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Know whether changing a tag automatically changes production workloads.

---

## Enhanced OpenShift Lab 83 — BuildConfig Supply-Chain Boundary

### Objective

Turn **BuildConfig Supply-Chain Boundary** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get bc,builds
oc describe bc <BUILD>
```

### Expected Result

Build strategy, ServiceAccount, triggers, and output target are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Separate build and deploy permissions.

---

## Enhanced OpenShift Lab 84 — S2I Builder Contract

### Objective

Turn **S2I Builder Contract** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
source
  ↓ assemble
builder image runtime
  ↓ output image
  ↓ run script
```

### Expected Result

The build can be reproduced from source revision and builder image.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Pin builder image/version and record source commit.

---

## Enhanced OpenShift Lab 85 — Build Failure Decomposition

### Objective

Turn **Build Failure Decomposition** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get builds
oc describe build <BUILD>
oc logs build/<BUILD>
```

### Expected Result

The failed build phase and exact log error are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Fix the failed supply-chain step instead of rerunning blindly.

---

## Enhanced OpenShift Lab 86 — Shipwright Build Model

### Objective

Turn **Shipwright Build Model** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc api-resources | grep -i shipwright
```

### Expected Result

The installed build API model can be identified.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not mix BuildConfig and Shipwright assumptions in one troubleshooting path.

---

## Enhanced OpenShift Lab 87 — Build Provenance

### Objective

Turn **Build Provenance** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
source commit
  ↓ trusted build
SBOM + scan + provenance
  ↓ signed image digest
```

### Expected Result

Incident responders can prove exactly how an image was created.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Promote artifacts, not source rebuilds, between environments.

---

## Enhanced OpenShift Lab 88 — Registry Mirror Trust

### Objective

Turn **Registry Mirror Trust** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
approved upstream
  ↓ mirror workflow
internal registry
  ↓ cluster pulls
```

### Expected Result

The internal mirror has TLS, auth, storage, backup, and monitoring ownership.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Treat mirror compromise/outage as platform-severity risk.

---

## Enhanced OpenShift Lab 89 — Image Mirror Policy

### Objective

Turn **Image Mirror Policy** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get imagedigestmirrorsets,imagetagmirrorsets 2>/dev/null || true
```

### Expected Result

Configured source-to-mirror relationships are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Test platform and workload pulls before broad mirror changes.

---

## Enhanced OpenShift Lab 90 — Classic OLM Control Flow

### Objective

Turn **Classic OLM Control Flow** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
CatalogSource
  ↓ package/channel
Subscription
  ↓ resolver
InstallPlan
  ↓
CSV + CRDs + RBAC + Operator
```

### Expected Result

A failed install can be placed at catalog, resolution, approval, CSV, or Operator-runtime stage.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Inspect lifecycle objects before deleting/reinstalling the Operator.

---

## Enhanced OpenShift Lab 91 — CatalogSource Health

### Objective

Turn **CatalogSource Health** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get catalogsource -A
oc describe catalogsource <NAME> -n <NS>
```

### Expected Result

Catalog connection/status errors are explicit.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Secure and monitor catalogs as software supply-chain inputs.

---

## Enhanced OpenShift Lab 92 — OperatorGroup Scope

### Objective

Turn **OperatorGroup Scope** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get operatorgroup -A
```

### Expected Result

Target namespaces/scope are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Match the Operator's supported install modes to the intended tenancy scope.

---

## Enhanced OpenShift Lab 93 — Subscription Channel Governance

### Objective

Turn **Subscription Channel Governance** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get subscription -A
oc describe subscription <SUB> -n <NS>
```

### Expected Result

Current channel, source, installed CSV, and upgrade state are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use manual approval when business change control requires review.

---

## Enhanced OpenShift Lab 94 — InstallPlan Approval

### Objective

Turn **InstallPlan Approval** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get installplan -A
```

### Expected Result

Pending plans can be reviewed before approval.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Inspect permissions, release notes, CRD changes, and backup readiness first.

---

## Enhanced OpenShift Lab 95 — CSV Failure

### Objective

Turn **CSV Failure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get csv -A
oc describe csv <CSV> -n <NS>
```

### Expected Result

Requirements and failure reasons are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Resolve the missing requirement instead of deleting the namespace.

---

## Enhanced OpenShift Lab 96 — Operator Permission Review

### Objective

Turn **Operator Permission Review** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get clusterrolebindings,clusterroles | grep -i <OPERATOR_NAME>
```

### Expected Result

The Operator's privilege footprint is reviewable.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Perform security review before installing third-party Operators.

---

## Enhanced OpenShift Lab 97 — Operator CR Status

### Objective

Turn **Operator CR Status** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get <CRD_KIND> <NAME> -o yaml | sed -n '/status:/,$p'
```

### Expected Result

Managed resource conditions explain operand health.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Troubleshoot Operator and operand separately.

---

## Enhanced OpenShift Lab 98 — Operator Finalizers

### Objective

Turn **Operator Finalizers** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get <RESOURCE> <NAME> -o jsonpath='{.metadata.finalizers}{"\n"}'
```

### Expected Result

Finalizer ownership explains the stuck deletion.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Restore the Operator/cleanup path before manually removing finalizers.

---

## Enhanced OpenShift Lab 99 — CRD Deletion Risk

### Objective

Turn **CRD Deletion Risk** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get crd | grep -i <OPERATOR>
```

### Expected Result

CRD inventory is known before uninstall.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Follow the Operator's documented uninstall procedure.

---

## Enhanced OpenShift Lab 100 — OLM v1 vs Classic

### Objective

Turn **OLM v1 vs Classic** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc api-resources | grep -Ei 'subscription|installplan|clusterserviceversion|catalog|extension'
```

### Expected Result

Installed lifecycle APIs reveal which model is available.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not assume one-to-one object mapping between classic and newer OLM.

---

## Enhanced OpenShift Lab 101 — Operator Compatibility Before OCP Update

### Objective

Turn **Operator Compatibility Before OCP Update** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
OCP target
  ↕ supported
Operator version/channel
  ↕
operand version + CRDs
```

### Expected Result

Every production Operator has a validated supported path.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Block cluster upgrade until critical Operator compatibility is confirmed.

---

## Enhanced OpenShift Lab 102 — CSI StorageClass Governance

### Objective

Turn **CSI StorageClass Governance** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get storageclass
```

### Expected Result

The default class and parameters are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Document each StorageClass as a service tier.

---

## Enhanced OpenShift Lab 103 — PVC Pending

### Objective

Turn **PVC Pending** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc describe pvc <PVC> -n <PROJECT>
oc get storageclass
```

### Expected Result

PVC events identify the provisioning failure.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Fix claim/provisioner before modifying application containers.

---

## Enhanced OpenShift Lab 104 — VolumeAttachment Failure

### Objective

Turn **VolumeAttachment Failure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get volumeattachments
```

### Expected Result

The volume's target node/attachment status is visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use storage fencing/driver-supported detach procedures for stateful recovery.

---

## Enhanced OpenShift Lab 105 — Snapshot vs Backup

### Objective

Turn **Snapshot vs Backup** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
PVC → snapshot → fast recovery
PVC/app → backup copy → independent failure domain
```

### Expected Result

Recovery architecture distinguishes snapshot from durable backup.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Test application-consistent restores.

---

## Enhanced OpenShift Lab 106 — ODF as Data Platform

### Objective

Turn **ODF as Data Platform** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
ODF Operators
  ↓ Ceph/data services
StorageClasses / object APIs
  ↓ applications
```

### Expected Result

ODF health is treated as an independent stateful platform.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Capacity-plan storage nodes, replication, network, and recovery.

---

## Enhanced OpenShift Lab 107 — Machine vs Node

### Objective

Turn **Machine vs Node** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc -n openshift-machine-api get machines -o wide
oc get nodes -o wide
```

### Expected Result

Infrastructure and Kubernetes identities can be mapped.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Troubleshoot Machine provisioning separately from kubelet/node registration.

---

## Enhanced OpenShift Lab 108 — MachineSet Scaling

### Objective

Turn **MachineSet Scaling** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc -n openshift-machine-api get machinesets
```

### Expected Result

Desired/current Machine counts are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Verify cloud/on-prem quota, IPs, subnets, and storage before scaling.

---

## Enhanced OpenShift Lab 109 — MachineHealthCheck Safety

### Objective

Turn **MachineHealthCheck Safety** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc -n openshift-machine-api get machinehealthchecks
```

### Expected Result

Remediation policy and scope can be reviewed.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Set limits so correlated failures do not trigger destructive mass remediation.

---

## Enhanced OpenShift Lab 110 — Infra Node Placement

### Objective

Turn **Infra Node Placement** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
infra node pool
  + role label
  + taint
  ↓
Ingress/Registry/Monitoring placement
```

### Expected Result

Platform capacity is separated from application worker capacity.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Preserve enough infra replicas across failure domains.

---

## Enhanced OpenShift Lab 111 — Node Tuning Operator

### Objective

Turn **Node Tuning Operator** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get tuned -A 2>/dev/null || true
oc get profiles.tuned.openshift.io -A 2>/dev/null || true
```

### Expected Result

Applied tuning profiles can be inspected where available.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use supported tuned profiles and test workload impact.

---

## Enhanced OpenShift Lab 112 — Performance Profile

### Objective

Turn **Performance Profile** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
PerformanceProfile
  ↓ MCO/Tuned
node kernel + CPU topology
  ↓ guaranteed workload placement
```

### Expected Result

Node and Pod configuration align around the intended latency model.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use dedicated nodes and measurable latency objectives.

---

## Enhanced OpenShift Lab 113 — oc debug node Workflow

### Objective

Turn **oc debug node Workflow** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc debug node/<NODE>
# inside:
chroot /host
systemctl status kubelet
systemctl status crio
```

### Expected Result

Node troubleshooting is possible without permanent SSH configuration.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Capture evidence and exit without making undocumented host changes.

---

## Enhanced OpenShift Lab 114 — CRI-O Troubleshooting

### Objective

Turn **CRI-O Troubleshooting** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc debug node/<NODE> -- chroot /host journalctl -u crio -b --no-pager | tail -100
```

### Expected Result

Runtime errors can be correlated with Pod events.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use CRI-O evidence rather than Docker commands on OpenShift nodes.

---

## Enhanced OpenShift Lab 115 — Kubelet Troubleshooting

### Objective

Turn **Kubelet Troubleshooting** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc debug node/<NODE> -- chroot /host journalctl -u kubelet -b --no-pager | tail -120
```

### Expected Result

Node-agent errors are available even when a workload has no useful logs.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Preserve kubelet evidence before rebooting or replacing a node.

---

## Enhanced OpenShift Lab 116 — Node NotReady Tree

### Objective

Turn **Node NotReady Tree** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc describe node <NODE>
oc get mcp
oc get pods -n openshift-ovn-kubernetes -o wide 2>/dev/null || true
```

### Expected Result

Conditions/events identify the failing subsystem.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Compare bad node state with a healthy peer before broad cluster changes.

---

## Enhanced OpenShift Lab 117 — Disk Pressure

### Objective

Turn **Disk Pressure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc debug node/<NODE> -- chroot /host df -h
oc debug node/<NODE> -- chroot /host df -i
```

### Expected Result

Byte and inode pressure are separated.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use supported runtime/kubelet cleanup and log retention, not random file deletion.

---

## Enhanced OpenShift Lab 118 — Monitoring Stack Mental Model

### Objective

Turn **Monitoring Stack Mental Model** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
cluster components
  ↓ metrics
platform Prometheus
  ↓ alerts/dashboards

user workloads
  ↓ ServiceMonitor/PodMonitor
user workload monitoring
```

### Expected Result

Platform and application metric ownership are clear.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not edit Operator-managed monitoring Deployments directly.

---

## Enhanced OpenShift Lab 119 — User Workload Monitoring

### Objective

Turn **User Workload Monitoring** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc api-resources | grep -E 'servicemonitor|podmonitor|prometheusrule'
```

### Expected Result

Monitoring CRDs are available when the stack is enabled.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Give application teams project-scoped monitoring permissions rather than platform-admin access.

---

## Enhanced OpenShift Lab 120 — ServiceMonitor Selection

### Objective

Turn **ServiceMonitor Selection** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get servicemonitor -A
oc get svc -n <PROJECT> --show-labels
```

### Expected Result

Monitor selector and Service labels can be compared.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Debug discovery before changing Prometheus scrape intervals.

---

## Enhanced OpenShift Lab 121 — PrometheusRule Quality

### Objective

Turn **PrometheusRule Quality** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```yaml
labels:
  severity: warning
annotations:
  runbook_url: https://runbooks.example/...
```

### Expected Result

Alert metadata directs an operator toward the correct response.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Page only on actionable sustained conditions.

---

## Enhanced OpenShift Lab 122 — OpenShift Logging Data Flow

### Objective

Turn **OpenShift Logging Data Flow** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
container/platform/audit logs
  ↓ collector
  ├─ Loki
  ├─ SIEM
  └─ external logging
```

### Expected Result

Log ownership, retention, and destinations are explicit.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Treat audit logs and application logs with different retention/access requirements where needed.

---

## Enhanced OpenShift Lab 123 — ClusterLogForwarder

### Objective

Turn **ClusterLogForwarder** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc api-resources | grep -i clusterlogforwarder
```

### Expected Result

The installed logging API/version can be identified.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Review filters and output credentials before enabling forwarding.

---

## Enhanced OpenShift Lab 124 — Log Retention and Cost

### Objective

Turn **Log Retention and Cost** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
metrics: medium volume
logs: high volume
traces: sampled high-cardinality
flows: potentially massive
```

### Expected Result

Retention/storage budget is defined per telemetry class.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Set explicit retention, sampling, and access policy.

---

## Enhanced OpenShift Lab 125 — Network Observability

### Objective

Turn **Network Observability** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get flowcollectors -A 2>/dev/null || true
```

### Expected Result

Flow collection configuration is visible when installed.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Control sampling and storage to avoid uncontrolled telemetry growth.

---

## Enhanced OpenShift Lab 126 — OpenTelemetry

### Objective

Turn **OpenTelemetry** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
app instrumentation
  ↓ OTel collector
  ↓
trace/metric/log backends
```

### Expected Result

Request traces can be correlated with Route, Service, and Pod behavior.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Instrument applications for user-path visibility, not just cluster metrics.

---

## Enhanced OpenShift Lab 127 — GitOps Source of Truth

### Objective

Turn **GitOps Source of Truth** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
Git
  ↓ Argo CD
OpenShift API
  ↓ Operators/controllers
live state
```

### Expected Result

Drift ownership is understood before emergency edits.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Identify GitOps ownership before changing managed resources.

---

## Enhanced OpenShift Lab 128 — GitOps Project Boundaries

### Objective

Turn **GitOps Project Boundaries** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
repo
  ↓ Argo project
allowed namespaces/clusters
  ↓ sync
```

### Expected Result

A GitOps application cannot deploy outside approved destinations when configured correctly.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Separate platform and application GitOps identities.

---

## Enhanced OpenShift Lab 129 — OpenShift Pipelines Identity

### Objective

Turn **OpenShift Pipelines Identity** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
clone SA
build SA
sign/push SA
deploy SA
```

### Expected Result

Pipeline stages can use different least-privilege identities.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not give one pipeline ServiceAccount cluster-admin for convenience.

---

## Enhanced OpenShift Lab 130 — Tekton Workspace/Secret Handling

### Objective

Turn **Tekton Workspace/Secret Handling** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
workspace
  + source
  + artifacts
secret mounts
  ↓ task pods
```

### Expected Result

Credential and artifact lifetime is explicit.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use short-lived credentials and limit shared workspaces.

---

## Enhanced OpenShift Lab 131 — Cluster Update Preconditions

### Objective

Turn **Cluster Update Preconditions** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co
oc get mcp
oc get clusterversion
oc adm upgrade
```

### Expected Result

Go/no-go criteria are evidence-based.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Stop the change if a precondition fails.

---

## Enhanced OpenShift Lab 132 — Update Channels and Graph

### Objective

Turn **Update Channels and Graph** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc adm upgrade
oc get clusterversion version -o yaml
```

### Expected Result

Available/recommended updates come from the supported graph and cluster conditions.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use supported graph edges instead of specifying arbitrary release images.

---

## Enhanced OpenShift Lab 133 — Upgradeable=False

### Objective

Turn **Upgradeable=False** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co -o json | jq -r '.items[] | [.metadata.name,([.status.conditions[]|select(.type=="Upgradeable")][0].status),([.status.conditions[]|select(.type=="Upgradeable")][0].message)] | @tsv'
```

### Expected Result

The exact blocker and message are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Resolve the blocker rather than overriding it by default.

---

## Enhanced OpenShift Lab 134 — EUS Planning

### Objective

Turn **EUS Planning** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
release train
  ↓ support window
maintenance/upgrade cadence
  ↓ target next supported release
```

### Expected Result

The organization has a documented supported-version deadline.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Check current lifecycle policy rather than relying on memorized dates.

---

## Enhanced OpenShift Lab 135 — Disconnected Mirroring

### Objective

Turn **Disconnected Mirroring** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
connected mirror host
  ↓ oc-mirror
internal registry
  ↓ disconnected cluster
```

### Expected Result

Every lifecycle artifact has an internal source.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Test the cluster with Internet access blocked.

---

## Enhanced OpenShift Lab 136 — oc-mirror Workflow

### Objective

Turn **oc-mirror Workflow** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
ImageSet configuration
  ↓ mirror operation
registry content
  ↓ generated cluster resources
apply to cluster
```

### Expected Result

The mirror process is reproducible and version-controlled.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Follow the documentation matching the live OCP version.

---

## Enhanced OpenShift Lab 137 — Mirror Capacity Planning

### Objective

Turn **Mirror Capacity Planning** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```python
release_gb = 25
operator_gb = 80
apps_gb = 300
rollback_factor = 2
print("Approx mirror GB:", (release_gb + operator_gb + apps_gb) * rollback_factor)
```

### Expected Result

Capacity includes rollback/retention rather than only one current release.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Monitor mirror growth and garbage collection carefully.

---

## Enhanced OpenShift Lab 138 — Proxy and NO_PROXY

### Objective

Turn **Proxy and NO_PROXY** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get proxy cluster -o yaml
```

### Expected Result

HTTP/HTTPS proxy and noProxy settings are visible from the supported API.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Include cluster, service, node, registry, and metadata endpoints in a tested noProxy design.

---

## Enhanced OpenShift Lab 139 — Etcd Backup Scope

### Objective

Turn **Etcd Backup Scope** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
etcd backup:
projects, RBAC, Routes, Operator CRs, Secrets, cluster config

separate:
PVC/DB/object data, registry, external services
```

### Expected Result

Control-plane recovery and application-data recovery are treated separately.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Define application backup in addition to cluster backup.

---

## Enhanced OpenShift Lab 140 — Etcd Backup Sensitivity

### Objective

Turn **Etcd Backup Sensitivity** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
snapshot + static resources
  ↓ encrypted repository
  ↓ restore-tested copy
```

### Expected Result

Backup handling matches cluster-credential sensitivity.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Never copy etcd backups to unsecured support shares.

---

## Enhanced OpenShift Lab 141 — OpenShift Restore Runbook

### Objective

Turn **OpenShift Restore Runbook** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
isolate recovery hosts
  ↓ restore etcd/static resources
API returns
  ↓ operators converge
  ↓ validate network/storage/ingress/apps
```

### Expected Result

The recovery test proves the whole platform, not just etcd startup.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Practice restore in an isolated clone and record RTO.

---

## Enhanced OpenShift Lab 142 — Cluster RPO vs App RPO

### Objective

Turn **Cluster RPO vs App RPO** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
cluster RPO ≠ application RPO
```

### Expected Result

Each state domain has its own recovery objective.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not claim zero data loss because an etcd snapshot exists.

---

## Enhanced OpenShift Lab 143 — RTO Decomposition

### Objective

Turn **RTO Decomposition** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```python
steps = {"detect":5,"infra":20,"control_plane":20,"operators":20,"data":30,"validation":15}
print("Example RTO minutes:", sum(steps.values()))
```

### Expected Result

RTO is decomposed into measurable stages.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Measure recovery through game days instead of estimating from one command.

---

## Enhanced OpenShift Lab 144 — must-gather Sensitivity

### Objective

Turn **must-gather Sensitivity** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc adm must-gather
```

### Expected Result

A support archive is produced and handled as sensitive data.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Store/share must-gather only through approved secure channels.

---

## Enhanced OpenShift Lab 145 — oc adm inspect

### Objective

Turn **oc adm inspect** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc adm inspect clusteroperator/network
```

### Expected Result

A smaller relevant diagnostic dataset is collected.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use targeted inspection first when the affected component is known.

---

## Enhanced OpenShift Lab 146 — Support Case Evidence

### Objective

Turn **Support Case Evidence** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
version + cluster ID
time window
impact
recent changes
commands/evidence
must-gather
```

### Expected Result

Support can start diagnosis without repeatedly requesting baseline information.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Preserve timestamps and avoid unapproved secret sharing.

---

## Enhanced OpenShift Lab 147 — Cluster Health Quick Check

### Objective

Turn **Cluster Health Quick Check** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get clusterversion
oc get co
oc get nodes
oc get mcp
oc get pods -A | grep -Ev 'Running|Completed' || true
```

### Expected Result

The first degraded platform layer is visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Use the quick check to scope the incident, not as the final diagnosis.

---

## Enhanced OpenShift Lab 148 — Authentication Operator Failure

### Objective

Turn **Authentication Operator Failure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co authentication
oc -n openshift-authentication get pods
```

### Expected Result

Authentication-specific health is separated from overall API health.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Avoid rotating every credential when the IdP/OAuth route is the real failure.

---

## Enhanced OpenShift Lab 149 — Console Operator Failure

### Objective

Turn **Console Operator Failure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co console
oc -n openshift-console get pods,route
```

### Expected Result

CLI access can be used to recover the console path.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not equate console outage with cluster outage.

---

## Enhanced OpenShift Lab 150 — Registry Degraded

### Objective

Turn **Registry Degraded** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get co image-registry
oc -n openshift-image-registry get pods
```

### Expected Result

The Operator and operand state are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Check storage first when registry Pods restart or refuse writes.

---

## Enhanced OpenShift Lab 151 — ImagePullBackOff on OpenShift

### Objective

Turn **ImagePullBackOff on OpenShift** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Result

Runtime pull error explains which registry/reference failed.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Fix image trust/auth/mirror cause instead of repeatedly recreating the Pod.

---

## Enhanced OpenShift Lab 152 — Build Output Push Failure

### Objective

Turn **Build Output Push Failure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc logs build/<BUILD> | tail -100
oc get is -n <PROJECT>
```

### Expected Result

The failure is isolated to the output/push stage.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Separate build compute success from artifact publication.

---

## Enhanced OpenShift Lab 153 — Route TLS Failure Tree

### Objective

Turn **Route TLS Failure Tree** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
openssl s_client -connect <ROUTE_HOST>:443 -servername <ROUTE_HOST> </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Expected Result

The externally presented certificate identity and validity are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Trace TLS termination mode before replacing certificates.

---

## Enhanced OpenShift Lab 154 — OVN Node Failure

### Objective

Turn **OVN Node Failure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get pods -n openshift-ovn-kubernetes -o wide 2>/dev/null || true
oc get co network
```

### Expected Result

The affected node's OVN component can be compared with healthy peers.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Contain the node if needed while preserving network evidence.

---

## Enhanced OpenShift Lab 155 — DNS Failure Tree

### Objective

Turn **DNS Failure Tree** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc run dns-test --rm -it --image=busybox -- nslookup kubernetes.default
```

### Expected Result

Cluster-local resolution can be tested independently.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Test internal and external names separately.

---

## Enhanced OpenShift Lab 156 — PVC Pending Tree

### Objective

Turn **PVC Pending Tree** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc describe pvc <PVC> -n <PROJECT>
oc get storageclass
```

### Expected Result

Provisioning events reveal the blocked layer.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Start with claim events and CSI Operator health.

---

## Enhanced OpenShift Lab 157 — MCP Updating Too Long

### Objective

Turn **MCP Updating Too Long** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get mcp
oc get nodes
oc get pdb -A
```

### Expected Result

The unavailable node and potential drain blocker are visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Investigate the specific node rather than pausing the whole cluster indefinitely.

---

## Enhanced OpenShift Lab 158 — Webhook Outage

### Objective

Turn **Webhook Outage** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get validatingwebhookconfigurations,mutatingwebhookconfigurations
oc get svc,endpointslices -A | grep -i webhook
```

### Expected Result

Webhook dependencies can be traced from API config to live endpoints.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Keep high-impact webhooks highly available and monitor certificate expiry.

---

## Enhanced OpenShift Lab 159 — Operator Install Failure Tree

### Objective

Turn **Operator Install Failure Tree** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
Catalog
  ↓ Subscription/extension
InstallPlan
  ↓ CSV/Operator
CRD/webhook
  ↓ operand CR
```

### Expected Result

The exact failed lifecycle stage is identified.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Do not delete namespaces or CRDs as a first response.

---

## Enhanced OpenShift Lab 160 — Update Blocked Tree

### Objective

Turn **Update Blocked Tree** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc adm upgrade
oc get co
oc get mcp
oc describe clusterversion version
```

### Expected Result

The explicit blocker is visible.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Resolve the blocker before forcing update.

---

## Enhanced OpenShift Lab 161 — Disconnected Pull Failure

### Objective

Turn **Disconnected Pull Failure** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```bash
oc get imagedigestmirrorsets,imagetagmirrorsets 2>/dev/null || true
```

### Expected Result

The source→mirror mapping can be inspected.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Prove the required digest exists in the internal registry.

---

## Enhanced OpenShift Lab 162 — EX280 Persistence Mindset

### Objective

Turn **EX280 Persistence Mindset** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
temporary:
manual edit generated Pod

persistent:
supported resource manifest / Operator config / RBAC / Route / SCC / project policy
```

### Expected Result

The solution is represented in cluster desired state.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Practice durable YAML/API-based solutions.

---

## Enhanced OpenShift Lab 163 — EX280 Version Awareness

### Objective

Turn **EX280 Version Awareness** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
production study: current OCP
exam practice: exam-stated OCP version
```

### Expected Result

Learners distinguish current operations from exam compatibility.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Verify exam objectives and cluster version before memorizing syntax.

---

## Enhanced OpenShift Lab 164 — OpenShift Operational Readiness

### Objective

Turn **OpenShift Operational Readiness** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
[ ] ClusterOperators healthy
[ ] identity/RBAC
[ ] SCC/PSA
[ ] OVN/policy
[ ] ingress/routes
[ ] registry/mirror
[ ] storage/backup
[ ] MCO/node capacity
[ ] observability
[ ] updates/DR
[ ] runbooks/support
```

### Expected Result

The platform is operable before tenant onboarding.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Make platform readiness a formal launch gate.

---

## Enhanced OpenShift Lab 165 — Evidence-First OpenShift Troubleshooting

### Objective

Turn **Evidence-First OpenShift Troubleshooting** into a repeatable OpenShift administration, engineering, security, or troubleshooting exercise.

### Safety Boundary

Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or disposable authorized OCP environment. ClusterVersion, MachineConfig, SCC, network, ingress, Operator, registry, disconnected mirror, and etcd changes require admin authorization, rollback planning, and preferably a disposable cluster.

### Procedure

1. Verify `oc whoami`, API server, project, and cluster version.
2. Identify the owning Cluster Operator or installed Operator.
3. Draw the expected Operator → operand → node/network/storage path.
4. Capture baseline conditions/events/logs with the command below.
5. If safe, introduce one reversible fault or configuration mismatch.
6. Diagnose from the supported source-of-truth API downward.
7. Recover through the supported Operator/API mechanism.
8. Verify cluster health plus user-facing application behavior.
9. Record security, availability, and upgrade/support implications.
10. Convert the finding into a runbook or monitoring improvement.

### Command / Configuration

```text
symptom
  ↓ ClusterOperator?
owning Operator
  ↓ source-of-truth CR
operand status/logs
  ↓ node/network/storage dependency
small correction
  ↓ verify
```

### Expected Result

The failed layer is isolated before remediation.

### Evidence Record

```text
Cluster/version
User/server/project
Owning Operator
Source-of-truth resource
ClusterOperator conditions
Operand Pods/events/logs
RHCOS/CRI-O/MCO
OVN/DNS/Ingress
Storage/CSI
RBAC/SCC/PSA
Recent changes
Root cause
Recovery
Verification
Prevention
```

### Best Practice

Preserve evidence, change one variable at a time, and document prevention.

---

## 5. Hands-on Lab / Practical Exercises

> Use a Red Hat Developer Sandbox, OpenShift Local, training cluster, or other authorized OpenShift lab. Cluster-level labs require admin privileges.

### Lab 1 — Identify Platform Version

Run:

```bash
oc version
oc get clusterversion
oc get nodes -o wide
```

Record:

```text
OpenShift version
Kubernetes version
client version
node OS
runtime
```

### Lab 2 — Cluster Operator Health

```bash
oc get clusteroperators
```

Create table:

```text
Operator
Available
Progressing
Degraded
Upgradeable
Message
```

Investigate one Operator with `oc describe`.

### Lab 3 — OpenShift Platform Namespaces

List:

```bash
oc get ns | grep openshift
```

Map at least 20 namespaces to platform functions.

### Lab 4 — Inspect ClusterVersion

```bash
oc describe clusterversion version
```

Record:

```text
desired version
history
channel
available updates
conditions
```

### Lab 5 — MachineConfigPools

```bash
oc get mcp
oc describe mcp worker
```

Record current rendered config and node counts.

### Lab 6 — MachineConfig Tabletop

Design a MachineConfig that creates a harmless file or systemd drop-in.

Explain:

```text
which pool
whether reboot required
rollout blast radius
rollback
```

Use only on disposable admin lab if actually applied.

### Lab 7 — Projects

Create:

```bash
oc new-project app-dev
```

Inspect:

```bash
oc get project app-dev -o yaml
oc project app-dev
```

Compare Project and Namespace metadata.

### Lab 8 — Project Quota

Create:

```text
CPU request quota
memory request quota
Pod count quota
PVC count quota
```

Attempt to exceed it.

### Lab 9 — LimitRange

Set defaults:

```text
CPU request/limit
memory request/limit
```

create Pod without explicit resources and inspect effective values.

### Lab 10 — Project Template Tabletop

Design default project template containing:

```text
ResourceQuota
LimitRange
NetworkPolicy
RoleBinding
labels
```

### Lab 11 — Users and Groups

In a training cluster, create/group identities appropriate to the environment.

Practice:

```bash
oc adm groups new developers
oc adm groups add-users developers USER
```

### Lab 12 — RBAC

Grant:

```text
view → auditor
edit → developer
admin → team lead
```

at project scope.

Verify:

```bash
oc auth can-i
```

### Lab 13 — ServiceAccount

Create:

```bash
oc create sa api-sa
```

Assign only read access to one ConfigMap/needed resource through Role.

### Lab 14 — SCC Inventory

```bash
oc get scc
```

Compare:

```text
restricted family
anyuid
privileged
hostaccess-related SCCs
```

Do not modify defaults.

### Lab 15 — Arbitrary UID

Build/use a container image that initially requires fixed UID/root.

Deploy under default OpenShift restrictions.

Observe failure.

Modify image permissions for arbitrary non-root UID compatibility and redeploy.

### Lab 16 — SCC Denial

Create a lab Pod requesting one prohibited security property.

Read event/admission error.

Identify exactly which field conflicts with available SCC.

### Lab 17 — Custom SCC Tabletop

Instead of editing default SCC, design a narrow custom SCC for a hypothetical legacy workload.

Document risk and ServiceAccount binding.

### Lab 18 — Pod Security Admission

Inspect namespace Pod Security labels.

Explain how PSA and SCC both affect OpenShift workload security.

### Lab 19 — ImageStream

Create/import image into ImageStream.

Inspect:

```bash
oc get is
oc describe is
oc get istag
```

Record tag and digest.

### Lab 20 — Integrated Registry

Inspect:

```text
Image Registry Operator
registry configuration
registry Pods
storage status
```

without changing production settings.

### Lab 21 — S2I / Source Build

Use a small Python/Node application and available supported builder.

Trace:

```text
Git source
builder
BuildConfig
build Pod
output image
ImageStream
```

### Lab 22 — Build Failure

Intentionally break dependency/source reference.

Use:

```bash
oc get builds
oc describe build
oc logs build/BUILD
```

to diagnose.

### Lab 23 — Shipwright Tabletop

Compare Shipwright workflow with BuildConfig.

Create architecture for:

```text
Build
BuildRun
strategy
output image
```

based on current installed APIs if available.

### Lab 24 — Kustomize

Create:

```text
base/
overlays/dev/
overlays/prod/
```

Deploy using:

```bash
oc apply -k overlays/dev
```

### Lab 25 — Helm

Install a simple application chart.

Inspect:

```bash
helm list
oc get all
```

Explain OCP 4.22 console's Helm v3 integration vs standalone Helm v4 availability.

### Lab 26 — Simple Route

Deploy an HTTP application.

```bash
oc expose service web
oc get route
```

Test externally.

### Lab 27 — Edge Route

Create edge TLS Route.

Verify:

```text
client TLS
router termination
backend
```

### Lab 28 — Passthrough Route

Deploy a TLS-speaking backend in lab.

Create passthrough Route and verify backend owns certificate.

### Lab 29 — Re-encrypt Route

Create/review:

```text
frontend certificate
backend certificate
destination CA
```

and trace TLS twice.

### Lab 30 — Route Failure Game

Simulate:

```text
Service selector wrong
Pod not Ready
targetPort wrong
bad destination CA
DNS wrong
```

diagnose 503/TLS errors.

### Lab 31 — IngressController

Inspect:

```bash
oc -n openshift-ingress-operator get ingresscontroller
oc -n openshift-ingress get pods
```

Map default router to apps domain.

### Lab 32 — Ingress Placement Tabletop

Design dedicated infra nodes for:

```text
router
registry
monitoring
```

using labels/taints/tolerations.

### Lab 33 — OVN-Kubernetes

Inspect networking:

```text
network ClusterOperator
OVN Pods
Pod CIDRs
Service CIDR
```

draw packet path.

### Lab 34 — NetworkPolicy

Create:

```text
default deny
frontend → api
api → db
DNS allowed
```

test allowed and blocked traffic.

### Lab 35 — Egress Firewall Tabletop

Design a project allowed to reach:

```text
internal database
approved API
DNS
```

but denied general Internet.

### Lab 36 — EgressIP Tabletop

Design fixed source IP for workload integrating with firewall allowlist.

Document node/availability requirements.

### Lab 37 — Secondary Network

If lab supports Multus, create/inspect NetworkAttachmentDefinition and attach second interface.

Otherwise document packet/interface architecture.

### Lab 38 — NMState Tabletop

Design a safe NodeNetworkConfigurationPolicy for VLAN/bond.

Define rollback/out-of-band access before implementation.

### Lab 39 — LoadBalancer Service

If lab supports, expose non-HTTP TCP application with:

```yaml
type: LoadBalancer
```

Compare with Route.

### Lab 40 — Install an Operator

Using lab OperatorHub/catalog, install low-risk Operator.

Document:

```text
source
channel
namespace
permissions
InstallPlan
CSV/modern lifecycle
```

### Lab 41 — Operator Lifecycle

Inspect classic resources where available:

```bash
oc get subscription,installplan,csv -A
```

Identify update approval.

### Lab 42 — Operator Uninstall

In disposable lab, follow Operator-specific uninstall procedure.

Observe which:

```text
CRDs
CRs
PVCs
namespaces
```

remain.

### Lab 43 — Storage

Create PVC from default StorageClass.

Trace:

```text
PVC
PV
CSI
Pod mount
```

### Lab 44 — Storage Failure

Break StorageClass name.

Diagnose PVC Pending from events.

Then restore.

### Lab 45 — Machine API

If platform has Machine API:

```bash
oc -n openshift-machine-api get machines
oc -n openshift-machine-api get machinesets
```

Map Machine to Node.

### Lab 46 — MachineHealthCheck Tabletop

Design remediation for worker failure.

Calculate maximum safe simultaneous remediation.

### Lab 47 — Node Debug

```bash
oc debug node/NODE
chroot /host
```

Inspect:

```bash
systemctl status kubelet
systemctl status crio
journalctl -u kubelet --since -10m
ip addr
df -h
```

Exit without changing host.

### Lab 48 — Monitoring

Inspect:

```text
openshift-monitoring
alerts
dashboards
ServiceMonitor
PrometheusRule
```

Create a user workload metric if environment supports.

### Lab 49 — Logging Architecture

Design:

```text
application stdout
collector
Loki
object storage
console
SIEM forwarding
```

Define retention.

### Lab 50 — Network Observability

If installed, inspect flow dashboard.

Otherwise design collection for:

```text
frontend → api
api → db
egress
denied flows
```

### Lab 51 — GitOps Tabletop

Design:

```text
Git
↓
Argo CD/OpenShift GitOps
↓
dev project
prod project
```

with RBAC and approval boundaries.

### Lab 52 — Pipelines Tabletop

Design Tekton pipeline:

```text
clone
test
build
scan
push
deploy
```

using separate build/deploy ServiceAccounts.

### Lab 53 — Cluster Update Precheck

Without triggering update, perform:

```bash
oc get co
oc get mcp
oc get clusterversion
oc adm upgrade
```

Build go/no-go checklist.

### Lab 54 — Disconnected Mirror Tabletop

Design:

```text
Internet-connected mirror host
↓
oc-mirror
↓
internal registry
↓
disconnected OCP cluster
```

Include releases + Operators + application content.

### Lab 55 — must-gather

On authorized lab:

```bash
oc adm must-gather
```

inspect output structure.

Document sensitive information handling.

### Lab 56 — Targeted Diagnostics

Use or design:

```bash
oc adm inspect clusteroperator/network
```

and targeted must-gather for one project/operator.

### Lab 57 — Cluster Operator Failure Game

Choose one reversible lab component and simulate a non-destructive failure.

Follow:

```text
CO condition
Operator logs
operand
dependency
recovery
```

### Lab 58 — EX280 Practice Set

Perform timed tasks:

```text
create/delete project
deploy YAML
Kustomize overlay
quota
LimitRange
RBAC
group
ServiceAccount
Route
TLS
NetworkPolicy
LoadBalancer
Operator install
SCC/application security
```

Use OCP 4.18-compatible environment if preparing specifically for exam.

### Lab 59 — Full Platform Incident Game Day

Simulate/tabletop:

1. authentication unavailable
2. Route 503
3. bad SCC request
4. registry degraded
5. image pull failure
6. OVN node failure
7. DNS failure
8. PVC Pending
9. MachineConfigPool degraded
10. node NotReady
11. Operator install failure
12. admission webhook outage
13. monitoring storage full
14. update blocked
15. disconnected mirror missing image

For each:

```text
Detection
Evidence
Owner Operator
Root Cause
Recovery
Verification
Prevention
```

### Lab 60 — Phase Capstone Validation

Review the final OpenShift platform project against:

```text
architecture
security
network
storage
Operators
observability
updates
backup
support
developer self-service
EX280 objectives
```

---

## 6. Mini Project

# Mini Project — Enterprise OpenShift Application Platform

Design a production OpenShift platform for a company running customer applications and internal manufacturing systems.

## Platform Baseline

```text
OpenShift Container Platform 4.22
RHCOS
CRI-O
OVN-Kubernetes
3 control-plane nodes
6+ worker nodes
dedicated infrastructure capacity
enterprise identity provider
persistent storage
private registry/mirrors
central observability
```

## Architecture

```text
                    Corporate Identity Provider
                              |
                           OAuth/OIDC
                              |
                              v
                         OpenShift API
                              |
                 +------------+------------+
                 |                         |
          Control Plane                Cluster Operators
                 |
             Worker Fleet
        +--------+---------+
        |                  |
      Infra             Applications
      Nodes                Nodes
        |                  |
Ingress/Registry       Projects/Apps
Monitoring/Logging
```

## External Traffic

```text
Public DNS
   ↓
External Load Balancer
   ↓
OpenShift Ingress Controller
   ↓
Routes
   ↓
Services
   ↓
Pods
```

## Project Structure

```text
platform-*
security-*
team-a-dev
team-a-prod
team-b-dev
team-b-prod
manufacturing-dev
manufacturing-prod
```

Every user project must have:

```text
ResourceQuota
LimitRange
default-deny NetworkPolicy
RBAC groups
restricted security baseline
labels
monitoring ownership
```

## Identity and RBAC

Define:

```text
platform-admins
security-admins
network-admins
storage-admins
developers
auditors
```

No shared administrator accounts.

## SCC / Security

Default application requirements:

```text
arbitrary non-root UID
no privileged mode
no hostPath
no hostNetwork
drop capabilities
RuntimeDefault seccomp
read-only root where possible
```

Document any custom SCC as an exception ADR.

## Networking

Include:

```text
OVN-Kubernetes
default deny
project communication matrix
EgressFirewall
EgressIP for partner allowlists
internal/external ingress
secondary network use case
DNS
```

## Images and Builds

Pipeline:

```text
Git
 ↓
Build
 ↓
unit tests
 ↓
SBOM
 ↓
vulnerability scan
 ↓
sign/provenance
 ↓
registry
 ↓
ImageStream or immutable image reference
 ↓
Deployment
```

## Operators

Maintain inventory:

```text
Operator
Catalog
Channel
Version
Namespace
Permissions
Approval mode
Data backup
Owner
Support
```

## Storage

Define:

```text
default class
fast class
shared class
snapshot class
registry storage
monitoring storage
logging object storage
application backup
```

## Nodes

Use:

```text
worker
infra
specialized hardware
```

with:

```text
MachineSets
MachineHealthChecks
MachineConfigPools
taints
labels
autoscaling
```

where infrastructure supports.

## Observability

Monitor:

```text
ClusterVersion
ClusterOperators
MCP
nodes
OVN
DNS
Ingress
registry
storage
Operators
applications
certificate expiry
security events
```

## Update Strategy

Define:

```text
channel
EUS policy
z-stream cadence
minor upgrade cadence
prechecks
backup
Operator compatibility
MCP health
maintenance
verification
rollback/support path
```

## Disconnected Strategy

Even if main cluster is connected, design emergency/internal mirror strategy for:

```text
release payloads
Operator catalogs
critical application images
```

## Backup / DR

Include:

```text
etcd backup
Git configuration
PKI/support data where required
PVC/database backup
registry strategy
identity/DNS/LB rebuild
object storage backup
```

## Required ADRs

```text
ADR-001-Installation-Model.md
ADR-002-Ingress.md
ADR-003-Network-Isolation.md
ADR-004-Storage.md
ADR-005-Identity.md
ADR-006-SCC-Policy.md
ADR-007-Operator-Governance.md
ADR-008-Observability.md
ADR-009-Update-Strategy.md
ADR-010-DR.md
```

## Required Runbooks

```text
RUNBOOK_CLUSTEROPERATOR_DEGRADED.md
RUNBOOK_AUTHENTICATION.md
RUNBOOK_ROUTE_503.md
RUNBOOK_ROUTE_TLS.md
RUNBOOK_SCC_DENIAL.md
RUNBOOK_IMAGE_PULL.md
RUNBOOK_BUILD_FAILURE.md
RUNBOOK_REGISTRY.md
RUNBOOK_OVN.md
RUNBOOK_DNS.md
RUNBOOK_PVC.md
RUNBOOK_NODE_NOTREADY.md
RUNBOOK_MCP_DEGRADED.md
RUNBOOK_OPERATOR_FAILURE.md
RUNBOOK_WEBHOOK.md
RUNBOOK_MONITORING.md
RUNBOOK_UPDATE_BLOCKED.md
RUNBOOK_MUST_GATHER.md
RUNBOOK_ETCD_BACKUP_RESTORE.md
```

---

## 7. Recommended Resources

This Markdown is designed to be self-contained for the learning path.

For production implementation and current behavior, use official Red Hat sources:

```text
OpenShift Container Platform 4.22 Documentation
OpenShift 4.22 Release Notes
Architecture
Installation
Postinstallation Configuration
Updating Clusters
Backup and Restore
etcd
Storage
Nodes
Machine Management
Machine Configuration
CLI Tools
Networking
OVN-Kubernetes
Ingress and Load Balancing
Authentication and Authorization
Security and Compliance
Images
Building Applications
Registry
Operators / OLM
Monitoring
Logging
Network Observability
OpenShift GitOps
OpenShift Pipelines
Support / must-gather
EX280 objectives
```

Always verify current documentation before:

```text
cluster updates
MachineConfig changes
network migration
SCC changes
Operator upgrades
disconnected mirroring
etcd restore
certificate changes
```

---

## 8. Certification Relevance

Direct certification:

```text
Red Hat Certified System Administrator in OpenShift
EX280
```

Current Red Hat exam page states:

```text
EX280 is performance-based
Exam baseline: OpenShift Container Platform 4.18
```

Current exam objectives include:

```text
Manage OpenShift Container Platform
Work with resource manifests
Deploy applications
Manage authentication and authorization
Configure network security
Expose non-HTTP/SNI applications
Enable developer self-service
Manage OpenShift Operators
Configure application security
```

This course uses OCP **4.22** for current production knowledge and explicitly retains the concepts needed for the **4.18-based EX280**.

For exam preparation, prioritize exact behavior and commands available in the stated exam version.

Recommended advanced path after EX280:

```text
DO380
EX380
```

for advanced enterprise-scale OpenShift administration.

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Treat OpenShift as Kubernetes plus UI.  
  **Best practice:** understand Cluster Operators, CVO, MCO, Routes, SCC, registry, and integrated lifecycle.

- **Mistake:** Manually edit Operator-owned Deployment.  
  **Best practice:** configure owning Operator/custom resource.

- **Mistake:** `dnf update` RHCOS nodes manually.  
  **Best practice:** OpenShift/CVO/MCO lifecycle.

- **Mistake:** Modify default SCC.  
  **Best practice:** fix application or create narrow custom SCC.

- **Mistake:** Grant `anyuid` because image cannot write.  
  **Best practice:** build arbitrary-UID-compatible image.

- **Mistake:** Use cluster-admin for developer.  
  **Best practice:** project roles/groups.

- **Mistake:** Put every user in one Project.  
  **Best practice:** project boundaries + quotas + RBAC + policies.

- **Mistake:** Assume Route works without healthy Service endpoints.  
  **Best practice:** trace Route → Service → EndpointSlice → Pod.

- **Mistake:** Confuse passthrough and re-encrypt.  
  **Best practice:** know where TLS terminates.

- **Mistake:** Edit router Deployment directly.  
  **Best practice:** IngressController.

- **Mistake:** Edit CoreDNS directly.  
  **Best practice:** DNS Operator-supported config.

- **Mistake:** Install Operator without reviewing permissions.  
  **Best practice:** treat Operator as privileged software supply chain.

- **Mistake:** Delete CRD to uninstall Operator.  
  **Best practice:** vendor/Red Hat uninstall procedure.

- **Mistake:** Assume OLM v1 and classic OLM resources are identical.  
  **Best practice:** identify lifecycle model/version.

- **Mistake:** Upgrade OCP with degraded MCP/Operator.  
  **Best practice:** healthy prechecks and supported graph.

- **Mistake:** Use old disconnected mirroring tutorials blindly.  
  **Best practice:** current `oc-mirror` and mirror APIs.

- **Mistake:** Run `oc adm must-gather` then share archive casually.  
  **Best practice:** treat diagnostics as sensitive.

- **Mistake:** Confuse current OCP version with EX280 version.  
  **Best practice:** production study on 4.22, exam practice on 4.18 behavior.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Current course OCP baseline?

**Answer:** OpenShift Container Platform 4.22.

### Q2. Current verified z-stream?

**Answer:** 4.22.9 as of August 11, 2026.

### Q3. OCP 4.22 Kubernetes version?

**Answer:** Kubernetes 1.35.

### Q4. OCP container runtime?

**Answer:** CRI-O.

### Q5. OCP node OS baseline?

**Answer:** RHCOS.

### Q6. CVO?

**Answer:** Cluster Version Operator managing OpenShift release payload lifecycle.

### Q7. MCO?

**Answer:** Machine Config Operator managing node OS/runtime configuration.

### Q8. MachineConfigPool?

**Answer:** Group of nodes receiving merged rendered MachineConfig.

### Q9. ClusterOperator conditions?

**Answer:** Available, Progressing, Degraded, Upgradeable.

### Q10. Project vs Namespace?

**Answer:** Project is OpenShift's namespace abstraction with additional metadata/self-service/RBAC behavior.

### Q11. OpenShift-specific external HTTP object?

**Answer:** Route.

### Q12. Route TLS modes?

**Answer:** Edge, passthrough, re-encrypt.

### Q13. Edge termination?

**Answer:** TLS terminates at router.

### Q14. Passthrough?

**Answer:** TLS remains encrypted through router to backend.

### Q15. Re-encrypt?

**Answer:** Router terminates client TLS and establishes new TLS to backend.

### Q16. Main OpenShift network plugin?

**Answer:** OVN-Kubernetes.

### Q17. SCC?

**Answer:** OpenShift security admission constraint controlling UID, privilege, capabilities, host access, SELinux, groups, and related Pod settings.

### Q18. Modify default SCC?

**Answer:** No; Red Hat recommends creating custom SCC instead.

### Q19. Arbitrary UID expectation?

**Answer:** Ordinary images should run without requiring fixed root UID.

### Q20. SCC vs PSA?

**Answer:** SCC is OpenShift-specific security admission/defaulting; PSA is Kubernetes namespace Pod Security Standards enforcement.

### Q21. ImageStream?

**Answer:** OpenShift image abstraction tracking image tags/digests.

### Q22. S2I?

**Answer:** Source-to-Image build process combining source with builder image.

### Q23. Shipwright?

**Answer:** Modern extensible Kubernetes/OpenShift build framework.

### Q24. Integrated registry managed by?

**Answer:** Image Registry Operator.

### Q25. OLM?

**Answer:** Operator Lifecycle Manager.

### Q26. Classic OLM main objects?

**Answer:** CatalogSource, OperatorGroup, Subscription, InstallPlan, CSV.

### Q27. Cluster Operator vs installed Operator?

**Answer:** Cluster Operator is core OCP release-managed platform component; installed Operator is optional lifecycle-managed software.

### Q28. Machine vs Node?

**Answer:** Machine represents infrastructure host lifecycle; Node is Kubernetes registered compute object.

### Q29. MachineSet?

**Answer:** Manages replicas of similar Machines.

### Q30. MachineHealthCheck?

**Answer:** Detects/remediates unhealthy Machines under configured safety rules.

### Q31. Cluster autoscaling components?

**Answer:** ClusterAutoscaler + MachineAutoscalers on supported MachineSets.

### Q32. OpenShift monitoring based on?

**Answer:** Prometheus ecosystem with Alertmanager and related components.

### Q33. User workload monitoring?

**Answer:** Monitoring stack for application/project metrics when enabled.

### Q34. `oc debug node`?

**Answer:** Creates privileged node troubleshooting environment.

### Q35. `oc adm must-gather`?

**Answer:** Collects broad cluster diagnostics for troubleshooting/support.

### Q36. Current EX280 certification title?

**Answer:** Red Hat Certified System Administrator in OpenShift.

### Q37. Current EX280 exam baseline?

**Answer:** OpenShift Container Platform 4.18.

### Q38. Current production course baseline vs EX280?

**Answer:** Course production baseline 4.22; EX280 baseline 4.18.

### Q39. Update source of truth?

**Answer:** ClusterVersion/CVO and supported update graph.

### Q40. Core OpenShift admin principle?

**Answer:** Find the owning Operator and configure its supported source-of-truth API instead of manually fighting generated resources.

---

# Expanded Self-Assessment Bank — OpenShift

### Q1. What is the key OpenShift engineering lesson from **Operator Ownership and Source of Truth**?

**Answer:** Change the supported Operator custom resource or configuration API, not generated operands.

### Q2. What is the key OpenShift engineering lesson from **ClusterVersion as Platform Desired State**?

**Answer:** Use ClusterVersion/CVO as the supported release lifecycle instead of upgrading core components individually.

### Q3. What is the key OpenShift engineering lesson from **ClusterOperator Condition Interpretation**?

**Answer:** Read Operator conditions and messages before restarting operands.

### Q4. What is the key OpenShift engineering lesson from **Release Payload Mental Model**?

**Answer:** Upgrade through supported release graph edges.

### Q5. What is the key OpenShift engineering lesson from **CVO Failure Decomposition**?

**Answer:** Do not force past upgrade blockers without understanding the reported risk.

### Q6. What is the key OpenShift engineering lesson from **RHCOS Immutable Node Model**?

**Answer:** Use MachineConfig and supported Operators for persistent node changes.

### Q7. What is the key OpenShift engineering lesson from **MachineConfig Merge**?

**Answer:** Review all matching MachineConfigs before assuming which object caused a node change.

### Q8. What is the key OpenShift engineering lesson from **MachineConfigPool Rollout**?

**Answer:** Treat MCO changes like node-maintenance events with N-1 capacity.

### Q9. What is the key OpenShift engineering lesson from **MCP Degraded Diagnosis**?

**Answer:** Fix the actual node/config drift instead of deleting the pool or rendered config.

### Q10. What is the key OpenShift engineering lesson from **MCD Current vs Desired Configuration**?

**Answer:** Use node annotations plus MCD logs to isolate rollout failures.

### Q11. What is the key OpenShift engineering lesson from **Control Plane vs Worker Pools**?

**Answer:** Apply the strictest change control to control-plane MachineConfig changes.

### Q12. What is the key OpenShift engineering lesson from **Custom MachineConfigPool**?

**Answer:** Use custom pools only when the operational need justifies extra lifecycle complexity.

### Q13. What is the key OpenShift engineering lesson from **MachineConfig Rollback**?

**Answer:** Keep a version-controlled copy of every custom MachineConfig.

### Q14. What is the key OpenShift engineering lesson from **Installation Dependency Graph**?

**Answer:** Troubleshoot the earliest failed dependency instead of repeatedly rerunning the installer.

### Q15. What is the key OpenShift engineering lesson from **IPI vs UPI Responsibility**?

**Answer:** Choose the model based on platform support and organizational infrastructure control.

### Q16. What is the key OpenShift engineering lesson from **Assisted Installation**?

**Answer:** Resolve discovery validation errors rather than bypassing them.

### Q17. What is the key OpenShift engineering lesson from **Agent-Based Installation**?

**Answer:** Keep generated assets protected because they can contain cluster credentials/configuration.

### Q18. What is the key OpenShift engineering lesson from **Bootstrap Completion**?

**Answer:** Remove bootstrap infrastructure only after the supported completion signal.

### Q19. What is the key OpenShift engineering lesson from **Install Config Security**?

**Answer:** Treat installation assets as sensitive cluster-bootstrap material.

### Q20. What is the key OpenShift engineering lesson from **OpenShift DNS Prerequisites**?

**Answer:** Validate DNS from bootstrap/control-plane/worker network paths before install.

### Q21. What is the key OpenShift engineering lesson from **API Load Balancer**?

**Answer:** Make API LB itself highly available and monitor backend readiness.

### Q22. What is the key OpenShift engineering lesson from **Ingress Load Balancer**?

**Answer:** Keep ingress LB and API LB roles separate.

### Q23. What is the key OpenShift engineering lesson from **Pull Secret Lifecycle**?

**Answer:** Never paste the pull secret into tickets or shell history.

### Q24. What is the key OpenShift engineering lesson from **kubeadmin Retirement**?

**Answer:** Retire bootstrap identities after enterprise admin access is proven.

### Q25. What is the key OpenShift engineering lesson from **oc Context Safety**?

**Answer:** Make context verification part of every change runbook.

### Q26. What is the key OpenShift engineering lesson from **Projects as Policy Boundaries**?

**Answer:** Provision projects from a standard baseline, not as empty namespaces.

### Q27. What is the key OpenShift engineering lesson from **Project Request Template**?

**Answer:** Use templates/automation to eliminate repetitive manual tenant setup.

### Q28. What is the key OpenShift engineering lesson from **ClusterResourceQuota**?

**Answer:** Use aggregate quota for team-level governance while retaining per-project quotas where useful.

### Q29. What is the key OpenShift engineering lesson from **LimitRange Defaults**?

**Answer:** Pair LimitRange defaults with measurement-driven right-sizing.

### Q30. What is the key OpenShift engineering lesson from **ResourceQuota Admission**?

**Answer:** Read the API error before changing node capacity.

### Q31. What is the key OpenShift engineering lesson from **Developer Self-Service Guardrails**?

**Answer:** Design guardrails rather than ticket-driven manual approvals for routine work.

### Q32. What is the key OpenShift engineering lesson from **OAuth Authentication Flow**?

**Answer:** Troubleshoot identity provider, OAuth route/certs, and RBAC independently.

### Q33. What is the key OpenShift engineering lesson from **OIDC Federation**?

**Answer:** Use short-lived IdP-managed identities and MFA for human access.

### Q34. What is the key OpenShift engineering lesson from **LDAP Integration**?

**Answer:** Avoid broad directory searches and plaintext LDAP.

### Q35. What is the key OpenShift engineering lesson from **Group-Centric RBAC**?

**Answer:** Bind roles to identity-provider groups where possible.

### Q36. What is the key OpenShift engineering lesson from **admin vs edit vs view**?

**Answer:** Test actual permissions before assigning broad roles.

### Q37. What is the key OpenShift engineering lesson from **Cluster-Admin Audit**?

**Answer:** Use project-scoped roles for application teams and break-glass for emergency access.

### Q38. What is the key OpenShift engineering lesson from **ServiceAccount Identity**?

**Answer:** One ServiceAccount should represent one coherent application capability.

### Q39. What is the key OpenShift engineering lesson from **Bound ServiceAccount Tokens**?

**Answer:** Disable automount for workloads that never call the cluster API.

### Q40. What is the key OpenShift engineering lesson from **SCC Admission Mental Model**?

**Answer:** Fix the workload first; grant a broader SCC only when the requirement is justified.

### Q41. What is the key OpenShift engineering lesson from **Default SCC Immutability**?

**Answer:** Create a narrowly scoped custom SCC instead of modifying built-ins.

### Q42. What is the key OpenShift engineering lesson from **Arbitrary UID Image Design**?

**Answer:** Design images for arbitrary UID rather than granting anyuid.

### Q43. What is the key OpenShift engineering lesson from **SCC Denial Diagnostics**?

**Answer:** Read the denial before assigning a more permissive SCC.

### Q44. What is the key OpenShift engineering lesson from **SCC Use Authorization**?

**Answer:** Review powerful SCC usage regularly.

### Q45. What is the key OpenShift engineering lesson from **Custom SCC Governance**?

**Answer:** Document each custom SCC as a security exception ADR.

### Q46. What is the key OpenShift engineering lesson from **SCC and PSA Together**?

**Answer:** Test both controls when a hardened Pod is unexpectedly rejected.

### Q47. What is the key OpenShift engineering lesson from **SELinux Confinement**?

**Answer:** Fix supported labels/policies rather than disabling SELinux.

### Q48. What is the key OpenShift engineering lesson from **allowPrivilegeEscalation**?

**Answer:** Use the smallest security context that still allows the application to function.

### Q49. What is the key OpenShift engineering lesson from **Seccomp RuntimeDefault**?

**Answer:** Prefer RuntimeDefault over Unconfined.

### Q50. What is the key OpenShift engineering lesson from **Security Profiles Operator**?

**Answer:** Use custom profiles only after measuring the workload's required behavior.

### Q51. What is the key OpenShift engineering lesson from **Compliance Operator**?

**Answer:** Treat automated remediation as change input, not something to apply blindly.

### Q52. What is the key OpenShift engineering lesson from **External Secret Integration**?

**Answer:** Use least-privilege workload identity and rotation.

### Q53. What is the key OpenShift engineering lesson from **Route vs Ingress**?

**Answer:** Choose one supported edge model and document TLS termination.

### Q54. What is the key OpenShift engineering lesson from **Edge Route TLS**?

**Answer:** Use edge termination only when plaintext or alternate backend protection is acceptable.

### Q55. What is the key OpenShift engineering lesson from **Passthrough Route TLS**?

**Answer:** Use passthrough when end-to-end application TLS ownership is required.

### Q56. What is the key OpenShift engineering lesson from **Re-encrypt Route TLS**?

**Answer:** Maintain destination CA and backend certificate rotation carefully.

### Q57. What is the key OpenShift engineering lesson from **Route Admission Status**?

**Answer:** Check admission before debugging the backend application.

### Q58. What is the key OpenShift engineering lesson from **Route 503 Decomposition**?

**Answer:** Trace north-south traffic one hop at a time.

### Q59. What is the key OpenShift engineering lesson from **IngressController Source of Truth**?

**Answer:** Never make persistent changes directly to router Deployments.

### Q60. What is the key OpenShift engineering lesson from **Ingress Sharding**?

**Answer:** Use sharding for real network/certificate/tenancy boundaries, not cosmetic separation.

### Q61. What is the key OpenShift engineering lesson from **Ingress Certificate Lifecycle**?

**Answer:** Monitor certificate expiry and chain validity.

### Q62. What is the key OpenShift engineering lesson from **OVN-Kubernetes Mental Model**?

**Answer:** Troubleshoot through OpenShift/OVN APIs and supported tooling instead of manually editing OVN databases.

### Q63. What is the key OpenShift engineering lesson from **Cluster Network Operator**?

**Answer:** Start at CNO conditions before application-specific workarounds.

### Q64. What is the key OpenShift engineering lesson from **Pod/Service CIDR Governance**?

**Answer:** Document IPAM before installation and reserve growth capacity.

### Q65. What is the key OpenShift engineering lesson from **OVN MTU**?

**Answer:** Plan MTU from the real underlay and encapsulation overhead.

### Q66. What is the key OpenShift engineering lesson from **NetworkPolicy Default Deny**?

**Answer:** Allow DNS and required dependencies before enabling egress deny.

### Q67. What is the key OpenShift engineering lesson from **NetworkPolicy Project Labels**?

**Answer:** Govern security-significant labels so tenant users cannot self-escalate network access.

### Q68. What is the key OpenShift engineering lesson from **EgressFirewall**?

**Answer:** Treat DNS, proxies, registries, APIs, and update endpoints as explicit dependencies.

### Q69. What is the key OpenShift engineering lesson from **EgressIP**?

**Answer:** Provide redundancy so one node failure does not remove all egress IP capacity.

### Q70. What is the key OpenShift engineering lesson from **Admin Network Policy Concept**?

**Answer:** Verify exact OCP support/maturity before production adoption.

### Q71. What is the key OpenShift engineering lesson from **Multus Secondary Networks**?

**Answer:** Document routing, IPAM, security, and failure behavior for every secondary interface.

### Q72. What is the key OpenShift engineering lesson from **NetworkAttachmentDefinition**?

**Answer:** Keep plugin configuration and IPAM version-controlled.

### Q73. What is the key OpenShift engineering lesson from **SR-IOV Scheduling**?

**Answer:** Use dedicated node pools and capacity planning for SR-IOV workloads.

### Q74. What is the key OpenShift engineering lesson from **NMState Change Safety**?

**Answer:** Canary node network changes and maintain out-of-band recovery access.

### Q75. What is the key OpenShift engineering lesson from **LoadBalancer Service on Bare Metal**?

**Answer:** Do not assume cloud-provider behavior exists on-premises.

### Q76. What is the key OpenShift engineering lesson from **MetalLB BGP/L2 Trade-Off**?

**Answer:** Treat address pools and BGP policy as production network configuration.

### Q77. What is the key OpenShift engineering lesson from **DNS Operator Source of Truth**?

**Answer:** Avoid editing generated CoreDNS workloads directly.

### Q78. What is the key OpenShift engineering lesson from **Route/DNS End-to-End Test**?

**Answer:** Verify the whole north-south path after ingress changes.

### Q79. What is the key OpenShift engineering lesson from **Integrated Registry Operator**?

**Answer:** Never persistently edit the generated registry Deployment.

### Q80. What is the key OpenShift engineering lesson from **Registry Storage Durability**?

**Answer:** Monitor storage capacity and backup/recovery requirements.

### Q81. What is the key OpenShift engineering lesson from **ImageStream Tag vs Digest**?

**Answer:** Promote immutable digests through environments.

### Q82. What is the key OpenShift engineering lesson from **Image Change Triggers**?

**Answer:** Know whether changing a tag automatically changes production workloads.

### Q83. What is the key OpenShift engineering lesson from **BuildConfig Supply-Chain Boundary**?

**Answer:** Separate build and deploy permissions.

### Q84. What is the key OpenShift engineering lesson from **S2I Builder Contract**?

**Answer:** Pin builder image/version and record source commit.

### Q85. What is the key OpenShift engineering lesson from **Build Failure Decomposition**?

**Answer:** Fix the failed supply-chain step instead of rerunning blindly.

### Q86. What is the key OpenShift engineering lesson from **Shipwright Build Model**?

**Answer:** Do not mix BuildConfig and Shipwright assumptions in one troubleshooting path.

### Q87. What is the key OpenShift engineering lesson from **Build Provenance**?

**Answer:** Promote artifacts, not source rebuilds, between environments.

### Q88. What is the key OpenShift engineering lesson from **Registry Mirror Trust**?

**Answer:** Treat mirror compromise/outage as platform-severity risk.

### Q89. What is the key OpenShift engineering lesson from **Image Mirror Policy**?

**Answer:** Test platform and workload pulls before broad mirror changes.

### Q90. What is the key OpenShift engineering lesson from **Classic OLM Control Flow**?

**Answer:** Inspect lifecycle objects before deleting/reinstalling the Operator.

### Q91. What is the key OpenShift engineering lesson from **CatalogSource Health**?

**Answer:** Secure and monitor catalogs as software supply-chain inputs.

### Q92. What is the key OpenShift engineering lesson from **OperatorGroup Scope**?

**Answer:** Match the Operator's supported install modes to the intended tenancy scope.

### Q93. What is the key OpenShift engineering lesson from **Subscription Channel Governance**?

**Answer:** Use manual approval when business change control requires review.

### Q94. What is the key OpenShift engineering lesson from **InstallPlan Approval**?

**Answer:** Inspect permissions, release notes, CRD changes, and backup readiness first.

### Q95. What is the key OpenShift engineering lesson from **CSV Failure**?

**Answer:** Resolve the missing requirement instead of deleting the namespace.

### Q96. What is the key OpenShift engineering lesson from **Operator Permission Review**?

**Answer:** Perform security review before installing third-party Operators.

### Q97. What is the key OpenShift engineering lesson from **Operator CR Status**?

**Answer:** Troubleshoot Operator and operand separately.

### Q98. What is the key OpenShift engineering lesson from **Operator Finalizers**?

**Answer:** Restore the Operator/cleanup path before manually removing finalizers.

### Q99. What is the key OpenShift engineering lesson from **CRD Deletion Risk**?

**Answer:** Follow the Operator's documented uninstall procedure.

### Q100. What is the key OpenShift engineering lesson from **OLM v1 vs Classic**?

**Answer:** Do not assume one-to-one object mapping between classic and newer OLM.

### Q101. What is the key OpenShift engineering lesson from **Operator Compatibility Before OCP Update**?

**Answer:** Block cluster upgrade until critical Operator compatibility is confirmed.

### Q102. What is the key OpenShift engineering lesson from **CSI StorageClass Governance**?

**Answer:** Document each StorageClass as a service tier.

### Q103. What is the key OpenShift engineering lesson from **PVC Pending**?

**Answer:** Fix claim/provisioner before modifying application containers.

### Q104. What is the key OpenShift engineering lesson from **VolumeAttachment Failure**?

**Answer:** Use storage fencing/driver-supported detach procedures for stateful recovery.

### Q105. What is the key OpenShift engineering lesson from **Snapshot vs Backup**?

**Answer:** Test application-consistent restores.

### Q106. What is the key OpenShift engineering lesson from **ODF as Data Platform**?

**Answer:** Capacity-plan storage nodes, replication, network, and recovery.

### Q107. What is the key OpenShift engineering lesson from **Machine vs Node**?

**Answer:** Troubleshoot Machine provisioning separately from kubelet/node registration.

### Q108. What is the key OpenShift engineering lesson from **MachineSet Scaling**?

**Answer:** Verify cloud/on-prem quota, IPs, subnets, and storage before scaling.

### Q109. What is the key OpenShift engineering lesson from **MachineHealthCheck Safety**?

**Answer:** Set limits so correlated failures do not trigger destructive mass remediation.

### Q110. What is the key OpenShift engineering lesson from **Infra Node Placement**?

**Answer:** Preserve enough infra replicas across failure domains.

### Q111. What is the key OpenShift engineering lesson from **Node Tuning Operator**?

**Answer:** Use supported tuned profiles and test workload impact.

### Q112. What is the key OpenShift engineering lesson from **Performance Profile**?

**Answer:** Use dedicated nodes and measurable latency objectives.

### Q113. What is the key OpenShift engineering lesson from **oc debug node Workflow**?

**Answer:** Capture evidence and exit without making undocumented host changes.

### Q114. What is the key OpenShift engineering lesson from **CRI-O Troubleshooting**?

**Answer:** Use CRI-O evidence rather than Docker commands on OpenShift nodes.

### Q115. What is the key OpenShift engineering lesson from **Kubelet Troubleshooting**?

**Answer:** Preserve kubelet evidence before rebooting or replacing a node.

### Q116. What is the key OpenShift engineering lesson from **Node NotReady Tree**?

**Answer:** Compare bad node state with a healthy peer before broad cluster changes.

### Q117. What is the key OpenShift engineering lesson from **Disk Pressure**?

**Answer:** Use supported runtime/kubelet cleanup and log retention, not random file deletion.

### Q118. What is the key OpenShift engineering lesson from **Monitoring Stack Mental Model**?

**Answer:** Do not edit Operator-managed monitoring Deployments directly.

### Q119. What is the key OpenShift engineering lesson from **User Workload Monitoring**?

**Answer:** Give application teams project-scoped monitoring permissions rather than platform-admin access.

### Q120. What is the key OpenShift engineering lesson from **ServiceMonitor Selection**?

**Answer:** Debug discovery before changing Prometheus scrape intervals.

### Q121. What is the key OpenShift engineering lesson from **PrometheusRule Quality**?

**Answer:** Page only on actionable sustained conditions.

### Q122. What is the key OpenShift engineering lesson from **OpenShift Logging Data Flow**?

**Answer:** Treat audit logs and application logs with different retention/access requirements where needed.

### Q123. What is the key OpenShift engineering lesson from **ClusterLogForwarder**?

**Answer:** Review filters and output credentials before enabling forwarding.

### Q124. What is the key OpenShift engineering lesson from **Log Retention and Cost**?

**Answer:** Set explicit retention, sampling, and access policy.

### Q125. What is the key OpenShift engineering lesson from **Network Observability**?

**Answer:** Control sampling and storage to avoid uncontrolled telemetry growth.

### Q126. What is the key OpenShift engineering lesson from **OpenTelemetry**?

**Answer:** Instrument applications for user-path visibility, not just cluster metrics.

### Q127. What is the key OpenShift engineering lesson from **GitOps Source of Truth**?

**Answer:** Identify GitOps ownership before changing managed resources.

### Q128. What is the key OpenShift engineering lesson from **GitOps Project Boundaries**?

**Answer:** Separate platform and application GitOps identities.

### Q129. What is the key OpenShift engineering lesson from **OpenShift Pipelines Identity**?

**Answer:** Do not give one pipeline ServiceAccount cluster-admin for convenience.

### Q130. What is the key OpenShift engineering lesson from **Tekton Workspace/Secret Handling**?

**Answer:** Use short-lived credentials and limit shared workspaces.

### Q131. What is the key OpenShift engineering lesson from **Cluster Update Preconditions**?

**Answer:** Stop the change if a precondition fails.

### Q132. What is the key OpenShift engineering lesson from **Update Channels and Graph**?

**Answer:** Use supported graph edges instead of specifying arbitrary release images.

### Q133. What is the key OpenShift engineering lesson from **Upgradeable=False**?

**Answer:** Resolve the blocker rather than overriding it by default.

### Q134. What is the key OpenShift engineering lesson from **EUS Planning**?

**Answer:** Check current lifecycle policy rather than relying on memorized dates.

### Q135. What is the key OpenShift engineering lesson from **Disconnected Mirroring**?

**Answer:** Test the cluster with Internet access blocked.

### Q136. What is the key OpenShift engineering lesson from **oc-mirror Workflow**?

**Answer:** Follow the documentation matching the live OCP version.

### Q137. What is the key OpenShift engineering lesson from **Mirror Capacity Planning**?

**Answer:** Monitor mirror growth and garbage collection carefully.

### Q138. What is the key OpenShift engineering lesson from **Proxy and NO_PROXY**?

**Answer:** Include cluster, service, node, registry, and metadata endpoints in a tested noProxy design.

### Q139. What is the key OpenShift engineering lesson from **Etcd Backup Scope**?

**Answer:** Define application backup in addition to cluster backup.

### Q140. What is the key OpenShift engineering lesson from **Etcd Backup Sensitivity**?

**Answer:** Never copy etcd backups to unsecured support shares.

### Q141. What is the key OpenShift engineering lesson from **OpenShift Restore Runbook**?

**Answer:** Practice restore in an isolated clone and record RTO.

### Q142. What is the key OpenShift engineering lesson from **Cluster RPO vs App RPO**?

**Answer:** Do not claim zero data loss because an etcd snapshot exists.

### Q143. What is the key OpenShift engineering lesson from **RTO Decomposition**?

**Answer:** Measure recovery through game days instead of estimating from one command.

### Q144. What is the key OpenShift engineering lesson from **must-gather Sensitivity**?

**Answer:** Store/share must-gather only through approved secure channels.

### Q145. What is the key OpenShift engineering lesson from **oc adm inspect**?

**Answer:** Use targeted inspection first when the affected component is known.

### Q146. What is the key OpenShift engineering lesson from **Support Case Evidence**?

**Answer:** Preserve timestamps and avoid unapproved secret sharing.

### Q147. What is the key OpenShift engineering lesson from **Cluster Health Quick Check**?

**Answer:** Use the quick check to scope the incident, not as the final diagnosis.

### Q148. What is the key OpenShift engineering lesson from **Authentication Operator Failure**?

**Answer:** Avoid rotating every credential when the IdP/OAuth route is the real failure.

### Q149. What is the key OpenShift engineering lesson from **Console Operator Failure**?

**Answer:** Do not equate console outage with cluster outage.

### Q150. What is the key OpenShift engineering lesson from **Registry Degraded**?

**Answer:** Check storage first when registry Pods restart or refuse writes.

### Q151. What is the key OpenShift engineering lesson from **ImagePullBackOff on OpenShift**?

**Answer:** Fix image trust/auth/mirror cause instead of repeatedly recreating the Pod.

### Q152. What is the key OpenShift engineering lesson from **Build Output Push Failure**?

**Answer:** Separate build compute success from artifact publication.

### Q153. What is the key OpenShift engineering lesson from **Route TLS Failure Tree**?

**Answer:** Trace TLS termination mode before replacing certificates.

### Q154. What is the key OpenShift engineering lesson from **OVN Node Failure**?

**Answer:** Contain the node if needed while preserving network evidence.

### Q155. What is the key OpenShift engineering lesson from **DNS Failure Tree**?

**Answer:** Test internal and external names separately.

### Q156. What is the key OpenShift engineering lesson from **PVC Pending Tree**?

**Answer:** Start with claim events and CSI Operator health.

### Q157. What is the key OpenShift engineering lesson from **MCP Updating Too Long**?

**Answer:** Investigate the specific node rather than pausing the whole cluster indefinitely.

### Q158. What is the key OpenShift engineering lesson from **Webhook Outage**?

**Answer:** Keep high-impact webhooks highly available and monitor certificate expiry.

### Q159. What is the key OpenShift engineering lesson from **Operator Install Failure Tree**?

**Answer:** Do not delete namespaces or CRDs as a first response.

### Q160. What is the key OpenShift engineering lesson from **Update Blocked Tree**?

**Answer:** Resolve the blocker before forcing update.

### Q161. What is the key OpenShift engineering lesson from **Disconnected Pull Failure**?

**Answer:** Prove the required digest exists in the internal registry.

### Q162. What is the key OpenShift engineering lesson from **EX280 Persistence Mindset**?

**Answer:** Practice durable YAML/API-based solutions.

### Q163. What is the key OpenShift engineering lesson from **EX280 Version Awareness**?

**Answer:** Verify exam objectives and cluster version before memorizing syntax.

### Q164. What is the key OpenShift engineering lesson from **OpenShift Operational Readiness**?

**Answer:** Make platform readiness a formal launch gate.

### Q165. What is the key OpenShift engineering lesson from **Evidence-First OpenShift Troubleshooting**?

**Answer:** Preserve evidence, change one variable at a time, and document prevention.

## Completion Checklist

- [ ] I understand OCP architecture and Kubernetes relationship.
- [ ] I understand RHCOS and CRI-O.
- [ ] I understand Cluster Operators.
- [ ] I can inspect ClusterVersion.
- [ ] I understand CVO.
- [ ] I understand MCO/MachineConfig/MCP.
- [ ] I understand installation models.
- [ ] I can use `oc` and web console.
- [ ] I understand Projects/project templates.
- [ ] I can configure quotas/LimitRanges.
- [ ] I understand users/groups/RBAC.
- [ ] I understand SCC and PSA.
- [ ] I can design arbitrary-UID-compatible images.
- [ ] I understand Routes and TLS modes.
- [ ] I understand IngressController.
- [ ] I understand OVN-Kubernetes.
- [ ] I understand NetworkPolicy/egress.
- [ ] I understand Multus/NMState/SR-IOV concepts.
- [ ] I understand ImageStreams.
- [ ] I understand registry.
- [ ] I understand S2I/BuildConfig/Shipwright.
- [ ] I understand Helm/Kustomize.
- [ ] I understand Operators/OLM.
- [ ] I understand OLM v1 vs classic context.
- [ ] I understand OpenShift storage/CSI.
- [ ] I understand Machine/MachineSet/MHC.
- [ ] I understand infra/specialized nodes.
- [ ] I understand monitoring/logging/observability.
- [ ] I understand GitOps/Pipelines concepts.
- [ ] I understand updates/EUS/disconnected mirroring.
- [ ] I understand must-gather/support workflow.
- [ ] I understand etcd/application backup distinction.
- [ ] I can troubleshoot common OpenShift failures.
- [ ] I understand current EX280 objectives/version.
- [ ] I completed all 60 labs.
- [ ] I completed the Enterprise OpenShift Application Platform capstone.
