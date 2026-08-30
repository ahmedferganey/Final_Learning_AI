# 60. Kubernetes Administration

> Phase 15 — Containers

This course turns Kubernetes fundamentals into **cluster administration**: installing clusters, understanding the control plane, managing nodes and runtimes, designing networking and storage, securing API access, operating highly available clusters, upgrading safely, backing up etcd, maintaining workloads, monitoring the platform, and troubleshooting failures under pressure.

The course is intentionally deeper than a certification cram guide. It is designed to develop the operating model required for:

```text
Kubernetes Administrator
Platform Engineer
SRE
DevOps Engineer
Cloud Infrastructure Engineer
Kubernetes Security Engineer
```

while also aligning strongly with the **Certified Kubernetes Administrator (CKA)** skill set.

---

# Current Kubernetes and CKA Baseline

Upstream Kubernetes baseline used in this material:

```text
Current stable upstream minor line: Kubernetes v1.36
Latest stable patch verified for this course: v1.36.2
Kubernetes v1.37 planned for August 26, 2026
```

Current kubeadm documentation is written for Kubernetes **v1.36**.

The current CKA page reports:

```text
Exam type: performance-based
Environment: command-line Kubernetes tasks
Duration: 2 hours
Current exam environment: Kubernetes v1.35
Passing score: 66%
```

The Linux Foundation states that the CKA environment is aligned with the newest Kubernetes minor version approximately **4–8 weeks after release**, so the exact exam minor can change.

Current CKA domains:

```text
Cluster Architecture, Installation & Configuration    25%
Workloads & Scheduling                                 15%
Services & Networking                                  20%
Storage                                                10%
Troubleshooting                                        30%
```

This course uses Kubernetes **v1.36 administration** as the operational baseline and explicitly identifies CKA relevance where appropriate.

---

# Administrator Mental Model

A developer asks:

```text
"How do I deploy my app?"
```

A Kubernetes administrator asks:

```text
Is the API available?
Is etcd healthy?
Are nodes healthy?
Can Pods schedule?
Can Pods communicate?
Can Services resolve?
Can storage attach?
Are certificates valid?
Can users authenticate?
Are RBAC rules correct?
Can the cluster recover from node/control-plane failure?
Can I upgrade without breaking workloads?
Can I restore cluster state?
Can I prove why an incident happened?
```

The operating stack:

```text
                         Users / Automation
                                |
                             kubectl
                                |
                                v
                         kube-apiserver
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
            etcd            Scheduler       Controller Manager
             |
             +--------------------------------------------+
                                                          |
                                                     Worker Nodes
                                               +----------+----------+
                                               |                     |
                                            kubelet               kube-proxy
                                               |                     |
                                               v                     v
                                         containerd/CRI-O         Services
                                               |
                                               v
                                              Pods
                                               |
                              +----------------+----------------+
                              |                                 |
                            CNI                               CSI
                              |                                 |
                        Pod Networking                    Persistent Storage
```

A production cluster must also include:

```text
DNS
Ingress/Gateway
Load Balancing
Observability
Backups
RBAC
Admission
Pod security
Network policy
Certificates
Image supply chain
Node lifecycle
Upgrade process
DR runbooks
```

---

## 1. Topic Title

**Kubernetes Administration**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain production Kubernetes architecture in depth.
- Explain API server request processing.
- Explain etcd operation and backup/restore.
- Explain scheduler and controller-manager behavior.
- Explain kubelet, CRI, container runtime, and static Pods.
- Prepare Linux nodes for Kubernetes.
- Configure containerd for Kubernetes.
- Install kubeadm, kubelet, and kubectl.
- Initialize a cluster with kubeadm.
- Join worker and additional control-plane nodes.
- Install a CNI plugin.
- Understand kubeadm-generated certificates and kubeconfig files.
- Understand kubeadm phases and configuration API.
- Build a multi-control-plane architecture conceptually and practically in a lab.
- Understand control-plane endpoint/load-balancer requirements.
- Configure and troubleshoot CoreDNS.
- Configure and troubleshoot kube-proxy and Service networking.
- Explain iptables, nftables, IPVS, and eBPF-based Service implementations conceptually.
- Understand Pod CIDR, Service CIDR, node routing, encapsulation, and MTU.
- Implement NetworkPolicy.
- Understand Gateway API and Ingress administration.
- Understand CNI plugin responsibilities and debugging.
- Configure StorageClasses, PVs, PVCs, CSI, snapshots, and expansion.
- Troubleshoot volume binding, attachment, and mount problems.
- Configure node labels, taints, tolerations, affinity, and topology constraints.
- Configure resource requests, limits, quotas, and LimitRanges.
- Understand kubelet eviction and node-pressure behavior.
- Manage priority classes and preemption concepts.
- Configure Horizontal Pod Autoscaler fundamentals.
- Administer namespaces and multi-team cluster boundaries.
- Configure ServiceAccounts.
- Configure Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.
- Use `kubectl auth can-i` and impersonation for authorization testing.
- Understand authentication methods.
- Manage Kubernetes certificates and CSRs.
- Understand kubeconfig identities.
- Configure Pod security using SecurityContext and Pod Security Admission.
- Understand admission controllers.
- Understand API server admission webhooks.
- Explain encryption at rest for Kubernetes API data.
- Understand audit logging.
- Use image policies and supply-chain controls conceptually.
- Drain, cordon, uncordon, and safely maintain nodes.
- Upgrade kubeadm clusters without skipping minor versions.
- Understand Kubernetes version-skew policy.
- Back up and restore etcd safely.
- Understand control-plane HA and etcd topology choices.
- Manage certificates and certificate renewal.
- Monitor cluster and workload health.
- Use metrics-server and Prometheus concepts.
- Collect control-plane, kubelet, runtime, and application logs.
- Troubleshoot API server, etcd, scheduler, controller manager, kubelet, runtime, CNI, DNS, Services, storage, and scheduling.
- Diagnose failed Pods using events, logs, status, container runtime, and node evidence.
- Use `crictl` for CRI-level troubleshooting.
- Use `journalctl`, `systemctl`, `ss`, `ip`, `nsenter`, and networking tools on nodes.
- Recover from common cluster failures.
- Perform realistic CKA-style administrative tasks efficiently.
- Design and document a production-grade Kubernetes operations platform.

---

## 3. Prerequisites

Required:

- 57. Application Containers
- 58. Docker Fundamentals
- 59. Kubernetes Fundamentals
- Linux System Administration I/II
- Networking
- Bash
- Git
- Storage fundamentals
- Basic PKI/TLS concepts

Recommended lab:

```text
3–5 Linux VMs

cp1      control-plane
cp2      optional HA control-plane
worker1
worker2
lb       optional API load balancer
```

A smaller lab can use:

```text
1 control-plane
2 workers
```

Use disposable VMs or an authorized environment.

Recommended tools:

```text
kubeadm
kubelet
kubectl
containerd
crictl
etcdctl
openssl
curl
jq
yq
ip
ss
dig
nslookup
tcpdump
journalctl
systemctl
```

---

## 4. Core Concepts Explanation

# Part 1 — Administrator Responsibilities

A Kubernetes administrator owns the cluster platform rather than one application.

Responsibilities include:

```text
cluster installation
node lifecycle
networking
storage
identity
policy
upgrades
backups
monitoring
incident response
capacity
```

Clear ownership boundaries with application teams prevent configuration drift.

# Part 2 — Shared Responsibility Inside Kubernetes

Platform team typically owns:

```text
cluster
CNI
CSI
DNS
Ingress/Gateway platform
RBAC baseline
policy
monitoring
upgrades
```

Application team typically owns:

```text
Deployments
Services
resource sizing
health probes
application ConfigMaps
application Secrets
```

Organizations can divide these differently, but ownership must be explicit.

# Part 3 — Control Plane Availability

If the API server is unavailable:

```text
running Pods may continue
Service data plane may continue
```

but:

```text
new scheduling stops
controller reconciliation stops
kubectl/API operations fail
```

Control-plane availability is therefore essential for change/recovery operations.

# Part 4 — Data Plane Availability

Workers execute workloads.

A healthy control plane cannot serve users if:

```text
nodes unavailable
CNI broken
kube-proxy/service data plane broken
storage unavailable
```

Monitor control plane and data plane separately.

# Part 5 — Declarative Administration

Cluster administration should also be declarative.

Prefer:

```text
versioned kubeadm config
Git-managed add-ons
Helm/Kustomize
policy as code
IaC for nodes/network
```

over undocumented manual changes.

# Part 6 — API as Source of Truth

Most Kubernetes state is represented in the API and stored in etcd.

Node-local exceptions include:

```text
kubelet configuration
container runtime
static Pod manifests
OS networking
systemd services
CNI binaries/config
```

Administrators must understand both API state and host state.

# Part 7 — Cluster Failure Domains

Typical failure domains:

```text
control-plane node
worker node
availability zone
storage system
network path
DNS
registry
certificate/identity
cloud API
```

Design resilience around realistic correlated failures.

# Part 8 — Single Control Plane

Good for:

```text
learning
development
small noncritical lab
```

Not enough for high availability because one node outage can remove API/control loops.

# Part 9 — HA Control Plane

Typical:

```text
API Load Balancer
      |
+-----+-----+-----+
|     |     |     |
cp1   cp2   cp3
```

Each control-plane node runs API server and controller/scheduler components; etcd can be stacked or external.

# Part 10 — Odd etcd Members

etcd uses quorum consensus.

Common sizes:

```text
1 member → lab
3 members → standard HA
5 members → larger failure tolerance
```

Odd sizes make quorum efficient.

# Part 11 — Quorum

For `N` voting members, quorum is majority.

Examples:

```text
3 → 2 required
5 → 3 required
```

Losing quorum makes etcd unavailable for writes/normal cluster operation.

# Part 12 — Stacked etcd Topology

kubeadm commonly supports control-plane nodes each also running etcd:

```text
cp1: API + etcd
cp2: API + etcd
cp3: API + etcd
```

Simpler infrastructure, but control-plane and etcd failures are correlated.

# Part 13 — External etcd Topology

Separate etcd cluster:

```text
cp nodes → external etcd nodes
```

Provides independent failure domain but increases operational complexity and host count.

# Part 14 — Control Plane Endpoint

HA kubeadm clusters use stable API endpoint:

```text
k8s-api.example.com:6443
```

backed by load balancer/VIP.

Clients and joining nodes should not depend on one control-plane node IP.

# Part 15 — API Server Port

Default secure Kubernetes API server port is commonly:

```text
TCP 6443
```

Control-plane firewall design must allow required clients/nodes while restricting untrusted access.

# Part 16 — Node Communication Direction

Kubelets normally initiate communication toward API server.

Control-plane-to-node operations such as logs/exec/port-forward require reverse paths through kubelet/API proxying architecture.

Understand firewalls both directions.

# Part 17 — Konnectivity Concept

Konnectivity can provide control-plane-to-node tunneling, especially in managed/restricted network architectures.

Agents initiate connections to Konnectivity server, reducing direct control-plane reachability requirements.

# Part 18 — Version Lifecycle

Kubernetes maintains a rolling set of supported minor branches.

Production policy should define:

```text
current minor
upgrade window
patch cadence
EOL deadline
add-on compatibility
```

# Part 19 — Version Skew

Kubernetes components can run supported version differences, but rules are strict.

Never assume arbitrary version combinations work.

Consult the version-skew policy for API server, kubelet, kube-proxy, controller, scheduler, kubectl.

# Part 20 — No Minor-Version Skipping with kubeadm

Current kubeadm upgrade documentation explicitly supports sequential minor upgrades.

Example:

```text
1.35 → 1.36
```

not:

```text
1.34 → 1.36
```

Skipping a minor is unsupported.

# Part 21 — Cluster Add-ons

Core/near-core add-ons include:

```text
CNI
CoreDNS
kube-proxy
CSI drivers
metrics-server
Ingress/Gateway controller
monitoring
```

Each has its own compatibility lifecycle.

# Part 22 — Managed vs Self-Managed

Managed Kubernetes offloads parts of:

```text
control plane
etcd
patching
HA
```

but administrators still need fundamentals to troubleshoot:

```text
nodes
network
storage
RBAC
workloads
policy
```

# Part 23 — Cluster API Concept

Cluster API is a Kubernetes-style project for declarative lifecycle management of Kubernetes clusters.

It is not required for CKA fundamentals but is important in fleet/platform engineering.

# Part 24 — Fleet Administration

Operating one cluster manually does not scale.

Fleet management needs:

```text
standard versions
GitOps/IaC
policy
central observability
certificate inventory
upgrade automation
asset inventory
```

# Part 25 — Production Readiness

Before workloads:

```text
HA/control plane
CNI
DNS
storage
Ingress/Gateway
RBAC
security policy
monitoring
backup
upgrade plan
capacity
runbooks
```

must be defined.

# Part 26 — Change Management

Every risky cluster change should have:

```text
scope
prechecks
backup
rollback
monitoring
owner
maintenance window
```

# Part 27 — Blast Radius

Changing:

```text
one Deployment
```

has smaller blast radius than:

```text
CNI
CoreDNS
API server flags
etcd
node kernel
```

Review depth should reflect blast radius.

# Part 28 — Evidence Before Action

Incident workflow:

```text
capture current state
logs/events/metrics
form hypothesis
make smallest change
verify
```

Random restarts destroy evidence.

# Part 29 — Cluster Runbook

Every cluster needs documented procedures for:

```text
node failure
API failure
etcd restore
certificate expiry
DNS failure
CNI failure
upgrade
storage outage
```

# Part 30 — Admin Mental Model

Always locate failure layer:

```text
client
API
controller/scheduler
node/kubelet
runtime
network
storage
workload
external dependency
```

Then collect evidence at that layer.

# Part 31 — API Request Path

A typical request:

```text
kubectl
 ↓ TLS
kube-apiserver
 ↓ authentication
authorization
admission
validation/defaulting
 ↓
etcd
```

Read/write behavior depends on request and controllers.

# Part 32 — Authentication

Answers:

```text
Who are you?
```

Possible mechanisms include:

```text
client certificates
bearer tokens
OIDC
service-account tokens
authentication proxy
```

depending on cluster setup.

# Part 33 — Authorization

Answers:

```text
Are you allowed to perform this action?
```

Common mode:

```text
RBAC
```

API server can combine authorization modes.

# Part 34 — Admission

Admission occurs after authn/authz and before persistence.

It can:

```text
mutate object
validate object
enforce policy
inject defaults
```

# Part 35 — Validation

API validates object schema/invariants.

Example failures:

```text
invalid selector
unsupported field
immutable field update
bad value
```

# Part 36 — API Watch

Controllers use watch streams to receive object changes rather than polling everything constantly.

`resourceVersion` supports consistent watch/list behavior.

# Part 37 — Informer Concept

Controllers commonly use shared informers/caches:

```text
list
watch
local cache
event handlers
workqueue
```

This reduces API load.

# Part 38 — Controller Workqueue

Typical controller:

```text
event
 ↓
queue key
 ↓
reconcile
 ↓
retry/backoff if error
```

This explains eventual rather than instantaneous convergence.

# Part 39 — API Discovery

Administrators should know:

```bash
kubectl api-resources
kubectl api-versions
```

for removed/deprecated API diagnosis.

# Part 40 — API Deprecation

Before upgrading:

```text
scan manifests
check release notes
find deprecated APIs
upgrade controllers/CRDs
```

An API removed in new minor can break workloads/controllers.

# Part 41 — CRD Administration

CRDs extend API.

Admins must monitor:

```text
stored versions
conversion webhooks
controller compatibility
finalizers
backup/restore behavior
```

# Part 42 — Webhook Dependency Risk

A broken validating/mutating webhook can block API writes cluster-wide depending on rules/failurePolicy.

High-impact webhooks require HA and careful scope.

# Part 43 — API Priority and Fairness Concept

Protects API server from overload by classifying and queueing requests.

Important during controller storms or large clusters.

# Part 44 — etcd Data Model

etcd stores serialized Kubernetes API state under keys.

Administrators generally should not modify Kubernetes data directly in etcd.

Use Kubernetes API.

# Part 45 — etcd Client Port

etcd client communication commonly uses:

```text
TCP 2379
```

Peer communication commonly:

```text
TCP 2380
```

Protect both strongly.

# Part 46 — etcd TLS

Production etcd should use TLS for:

```text
client authentication
peer authentication
encryption in transit
```

kubeadm configures certificates for its managed etcd topology.

# Part 47 — etcd Health

Use authorized certificates:

```bash
ETCDCTL_API=3 etcdctl endpoint health ...
```

Check each member rather than one endpoint only.

# Part 48 — etcd Status

```bash
etcdctl endpoint status --write-out=table
```

shows:

```text
ID
version
DB size
leader
raft index
```

depending on command/version.

# Part 49 — etcd Leader

Raft elects a leader.

Leader failure normally causes new election if quorum remains.

Short control-plane disruption may occur.

# Part 50 — etcd Quorum Failure

If quorum is lost:

```text
API writes fail
controllers cannot update state
scheduling/reconciliation stops
```

Running workloads can continue temporarily.

# Part 51 — etcd Latency

Slow disk/network can make API server appear slow/unhealthy.

etcd needs low-latency reliable storage.

# Part 52 — etcd Database Size

Compaction/defragmentation controls historical revision/storage growth.

Operational procedures must follow current etcd guidance.

# Part 53 — etcd Snapshot

Snapshot captures etcd state.

For kubeadm cluster, snapshot is core disaster-recovery artifact.

Store securely outside the failed cluster.

# Part 54 — Snapshot Status

Validate snapshot metadata using current `etcdutl`/etcd tools appropriate to installed etcd version.

A file existing is not proof it is restorable.

# Part 55 — etcd Restore Principle

Restore creates a new data directory/member state from snapshot.

Cluster control-plane manifests/config must then point to restored etcd state correctly.

# Part 56 — Restore Testing

Test on isolated lab:

```text
snapshot
destroy test state
restore
start etcd/API
verify objects
```

Measure RTO.

# Part 57 — API Server Static Pod

kubeadm commonly writes:

```text
/etc/kubernetes/manifests/kube-apiserver.yaml
```

kubelet watches this directory and runs control-plane component as static Pod.

# Part 58 — Controller Manager Static Pod

kubeadm manifest commonly:

```text
/etc/kubernetes/manifests/kube-controller-manager.yaml
```

# Part 59 — Scheduler Static Pod

kubeadm manifest commonly:

```text
/etc/kubernetes/manifests/kube-scheduler.yaml
```

# Part 60 — etcd Static Pod

Stacked kubeadm control plane commonly:

```text
/etc/kubernetes/manifests/etcd.yaml
```

# Part 61 — Static Pod Recovery

If a control-plane static Pod disappears:

```text
check manifest file
kubelet logs
container runtime
certificates
ports
host filesystem
```

API may be unavailable, so node tools matter.

# Part 62 — Manifest Atomic Change

Editing files under static Pod manifest directory causes kubelet restart/recreate behavior.

Use controlled edits/backups; partial/invalid manifest can remove component.

# Part 63 — Control Plane Logs Without API

If API is down, use runtime:

```bash
crictl ps -a
crictl logs CONTAINER_ID
```

plus:

```bash
journalctl -u kubelet
```

# Part 64 — Scheduler Framework Concept

Scheduler pipeline broadly:

```text
queue
filter feasible nodes
score nodes
reserve/permit
bind
```

Plugins implement scheduling behavior.

# Part 65 — Controller Leader Election

In HA clusters, controller-manager/scheduler replicas use leader election so only one active leader performs most control loops.

API servers are active-active.

# Part 66 — Controller Manager Functions

Examples:

```text
node controller
replication controller logic
Job controller
namespace controller
service-account controller
endpoint controllers
```

# Part 67 — Cloud Controller Manager

Separates cloud-provider-specific logic:

```text
nodes
routes
load balancers
volumes historically/where applicable
```

from core Kubernetes.

# Part 68 — API Server Certificates

API serving certificate must cover:

```text
kubernetes DNS names
Service IP
control-plane endpoint
node IP/DNS SANs as configured
```

Missing SAN causes TLS errors.

# Part 69 — Certificate Authority

kubeadm cluster typically has CAs for:

```text
Kubernetes API
etcd
front-proxy
```

Protect CA private keys strongly.

# Part 70 — ServiceAccount Signing Keys

Control plane uses signing keys to issue ServiceAccount tokens.

These are separate from API client CA keys.

# Part 71 — Kubeconfig Files

kubeadm creates kubeconfigs such as:

```text
admin.conf
controller-manager.conf
scheduler.conf
kubelet.conf
```

with identities/cluster endpoints.

# Part 72 — admin.conf Risk

`/etc/kubernetes/admin.conf` carries powerful admin credentials.

Copy only to authorized admin account and protect permissions.

# Part 73 — Super-Admin Concept

Recent kubeadm versions can distinguish highly privileged super-admin kubeconfig from normal admin patterns in some workflows.

Avoid casual distribution of break-glass credentials.

# Part 74 — API Server Health Endpoints

Control-plane health can be checked using authenticated/appropriate endpoints and local component health.

Do not expose health/debug endpoints publicly.

# Part 75 — API Server Audit

Audit logs can record:

```text
request user
verb
resource
response
timestamp
source
```

according to audit policy.

# Part 76 — API Server Flags

Flags influence:

```text
advertise address
service CIDR
authorization modes
admission plugins
etcd endpoints
certificates
audit
encryption
```

Treat flag changes as cluster-wide changes.

# Part 77 — Component Configuration APIs

Kubernetes components increasingly use structured config files/APIs rather than huge command-line flags.

Version-control configuration.

# Part 78 — Control Plane Resource Limits

Static Pods consume node resources.

Small control-plane VMs can become unstable during:

```text
large API load
etcd compaction
controller storms
log growth
```

# Part 79 — Control Plane Time Sync

Accurate node time matters for:

```text
TLS
leases
logs
certificates
distributed coordination
```

Run reliable NTP/time synchronization.

# Part 80 — Control Plane Deep Mental Model

When API operations fail, distinguish:

```text
client TLS/auth
API process
admission
etcd
controller
scheduler
node
```

instead of assuming "Kubernetes is down."

# Part 81 — Node OS Preparation

Before kubeadm:

```text
supported Linux
hostname/IP stable
time sync
kernel modules
sysctl
container runtime
swap policy
firewall ports
DNS
```

# Part 82 — Unique Host Identity

Each node needs unique:

```text
hostname
MAC/product UUID where relevant
IP
```

Duplicate identity can cause kubelet/node registration problems.

# Part 83 — Required Ports

Common kubeadm ports include API server, etcd, kubelet, scheduler/controller local ports and NodePort range.

Exact firewall plan depends on topology/CNI.

Follow current kubeadm ports reference.

# Part 84 — Swap

Historically Kubernetes required swap disabled by default; modern kubelet supports configurable swap behavior.

For a predictable kubeadm lab, follow current kubeadm documentation and explicit kubelet swap configuration rather than relying on accidental host swap state.

# Part 85 — Kernel Modules

Networking commonly needs modules such as:

```text
overlay
br_netfilter
```

depending on runtime/CNI.

Load/configure based on current platform documentation.

# Part 86 — sysctl Networking

Common bridge/IP forwarding sysctls include:

```text
net.ipv4.ip_forward=1
bridge-nf-call-iptables
```

requirements vary by CNI/runtime.

Do not blindly copy old tutorials without checking current plugin docs.

# Part 87 — Containerd

containerd is a common CRI runtime.

Kubelet communicates through:

```text
CRI socket
```

rather than Docker daemon.

# Part 88 — containerd Configuration

Generate config:

```bash
containerd config default
```

then configure CRI, cgroups, registry, sandbox image as appropriate.

Version-control node configuration.

# Part 89 — systemd cgroups

Kubelet/runtime should use compatible cgroup driver.

Modern systemd Linux generally uses systemd cgroup integration.

Mismatched drivers cause node/resource issues.

# Part 90 — CRI Socket

Common containerd socket:

```text
unix:///run/containerd/containerd.sock
```

kubeadm can auto-detect or be configured explicitly.

# Part 91 — crictl

CRI troubleshooting CLI.

Configure endpoint:

```text
runtime-endpoint
image-endpoint
```

then:

```bash
crictl info
crictl ps
crictl images
```

# Part 92 — Pause / Sandbox Image

Pod sandbox requires infrastructure image used by runtime for network namespace lifecycle.

Version/configuration should align with Kubernetes/runtime guidance.

# Part 93 — Package Repositories

Modern Kubernetes packages use version-specific repository channels.

Do not follow old `apt.kubernetes.io` instructions blindly.

Current kubeadm docs provide supported repository paths.

# Part 94 — Install kubeadm

Install:

```text
kubeadm
kubelet
kubectl
```

from current Kubernetes package repository for target minor.

# Part 95 — Package Hold

On Debian/Ubuntu kubeadm workflows commonly hold package versions to prevent uncontrolled minor upgrades.

Upgrade intentionally.

# Part 96 — kubeadm Version

```bash
kubeadm version
```

The kubeadm version used for cluster creation/upgrade must comply with version-skew rules.

# Part 97 — kubelet Service

After package installation, kubelet may restart repeatedly until kubeadm provides configuration.

This can be expected before cluster bootstrap.

# Part 98 — Preflight Checks

`kubeadm init` checks:

```text
ports
swap/config
runtime
kernel
files
privilege
hostname
```

Do not suppress failures without understanding them.

# Part 99 — kubeadm init

Example concept:

```bash
sudo kubeadm init \
  --pod-network-cidr=10.244.0.0/16
```

Actual CIDR must match CNI design.

# Part 100 — Init Phases

kubeadm performs phases:

```text
preflight
certs
kubeconfig
etcd
control-plane
kubelet
wait-control-plane
upload-config
mark-control-plane
bootstrap-token
addons
```

Exact phases can be listed with kubeadm.

# Part 101 — kubeadm Config File

For repeatability, prefer structured config:

```yaml
apiVersion: kubeadm.k8s.io/v1beta...
kind: ClusterConfiguration
```

Use version supported by installed kubeadm.

Do not hardcode an obsolete API version.

# Part 102 — InitConfiguration

Controls local bootstrap values such as:

```text
node registration
local API endpoint
bootstrap tokens
CRI socket
```

# Part 103 — ClusterConfiguration

Defines cluster-wide values:

```text
kubernetesVersion
controlPlaneEndpoint
networking
etcd
apiServer
controllerManager
scheduler
certificatesDir
```

# Part 104 — KubeletConfiguration

Can configure:

```text
cgroup driver
eviction
DNS
authentication/authorization
resource reservation
```

depending on schema/version.

# Part 105 — Pod Network CIDR

Choose non-overlapping Pod address range.

Must align with CNI.

Consider:

```text
nodes
Pods per node
on-prem
VPN
cloud VPC
Service CIDR
```

# Part 106 — Service Subnet

kubeadm default/config defines Service CIDR.

Avoid overlap with:

```text
Pod network
node network
external networks
```

# Part 107 — DNS Domain

Default cluster domain commonly:

```text
cluster.local
```

Changing requires DNS/application assumptions to align.

# Part 108 — kubeadm Output

After init, kubeadm prints:

```text
admin kubeconfig setup
CNI requirement
join command/token
```

Save join data securely but rotate/regenerate as needed.

# Part 109 — Install CNI Before Workloads

After init:

```text
control plane may be NotReady
CoreDNS Pending
```

until Pod network add-on is installed.

Install exactly one compatible primary CNI.

# Part 110 — CNI Manifest

Install using vendor-supported Helm/manifests/operator.

Check:

```text
Kubernetes version
Pod CIDR mode
kube-proxy replacement
MTU
NetworkPolicy
```

# Part 111 — Control Plane Taint

kubeadm marks control-plane nodes to avoid ordinary workloads by default.

Lab can remove taint for single-node cluster, but production should normally preserve dedicated control plane.

# Part 112 — Worker Join

```bash
kubeadm join API_ENDPOINT \
  --token ... \
  --discovery-token-ca-cert-hash sha256:...
```

Node bootstrap authenticates cluster CA and obtains kubelet credentials.

# Part 113 — Bootstrap Token

Short-lived token used for node bootstrap/discovery.

Do not treat as permanent admin credential.

# Part 114 — Discovery CA Hash

Pins public CA key hash during token-based discovery to prevent connecting to rogue control plane.

# Part 115 — Generate Join Command

```bash
kubeadm token create --print-join-command
```

Run on authorized control-plane host.

# Part 116 — Token List

```bash
kubeadm token list
```

Review and delete unnecessary bootstrap tokens.

# Part 117 — Join Control Plane

Additional control-plane node requires:

```text
stable controlPlaneEndpoint
certificate/key distribution
--control-plane
```

and appropriate etcd topology.

# Part 118 — Certificate Key

kubeadm can temporarily encrypt/share control-plane cert material for joining control-plane nodes.

Treat certificate key as secret and time-limited mechanism.

# Part 119 — Upload Certs

`kubeadm init phase upload-certs --upload-certs` can support HA join workflows.

Follow current docs.

# Part 120 — Reset

```bash
kubeadm reset
```

reverts kubeadm-managed node state but does not necessarily clean:

```text
CNI interfaces/config
iptables/nftables
user kubeconfig
external data
```

Review before reusing node.

# Part 121 — Reset Is Destructive

Never run `kubeadm reset` on production node without knowing:

```text
role
etcd membership
workloads
drain status
```

# Part 122 — kubeadm Phases

```bash
kubeadm init phase
kubeadm join phase
```

can execute individual bootstrap steps.

Useful for advanced recovery/custom automation.

# Part 123 — kubeadm Config Images

```bash
kubeadm config images list
```

shows control-plane images for target Kubernetes version.

Pre-pull for air-gapped environments.

# Part 124 — Air-Gapped Cluster Concept

Requires controlled mirrors for:

```text
Kubernetes images
CNI images
CSI images
OS packages
Helm charts
application registry
```

plus internal DNS/time/cert infrastructure.

# Part 125 — Private Registry Mirrors

Configure containerd registry hosts/certs according to current containerd format.

Test before kubeadm init.

# Part 126 — Control Plane Load Balancer

HA API load balancer health checks:

```text
TCP 6443
or HTTPS-aware health
```

must avoid routing to dead API server.

Load balancer itself needs HA.

# Part 127 — VIP Alternatives

On-prem HA can use:

```text
HAProxy + Keepalived
kube-vip
external appliance
cloud load balancer
```

depending on environment.

# Part 128 — Node Registration

Kubelet registers Node object and reports:

```text
capacity
allocatable
conditions
addresses
runtime version
kernel
```

# Part 129 — Node NotReady After Join

Check:

```text
CNI installed?
kubelet?
runtime?
network?
cert?
node lease?
```

Use:

```bash
kubectl describe node
journalctl -u kubelet
```

# Part 130 — Kubelet Config Location

kubeadm commonly writes kubelet configuration under:

```text
/var/lib/kubelet/
```

and systemd drop-ins.

Paths can vary by packaging.

# Part 131 — PKI Directory

kubeadm default:

```text
/etc/kubernetes/pki
```

contains highly sensitive CA/component keys/certs.

Back up securely as part of DR strategy.

# Part 132 — Manifest Directory

Default static Pod manifest:

```text
/etc/kubernetes/manifests
```

Any manifest added here is managed by kubelet.

# Part 133 — Kubeconfig Admin Setup

Typical non-root admin:

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Only for authorized administrator.

# Part 134 — Installation Verification

```bash
kubectl get nodes -o wide
kubectl get pods -A
kubectl get --raw='/readyz?verbose'
```

Check DNS/CNI/system Pods.

# Part 135 — Smoke Test

Deploy:

```text
Deployment
Service
DNS lookup
cross-node traffic
PVC if storage installed
```

A cluster is not proven healthy by `kubectl get nodes` alone.

# Part 136 — Bootstrap Troubleshooting

If `kubeadm init` fails:

```text
read exact preflight/fatal message
kubelet logs
runtime status
ports
cert files
old manifests
network settings
```

Do not repeatedly rerun without cleanup/understanding.

# Part 137 — CRI Error

`container runtime is not running`:

```bash
systemctl status containerd
crictl info
journalctl -u containerd
```

check CRI plugin/cgroup configuration.

# Part 138 — Port Conflict

```bash
ss -lntp
```

Identify service occupying Kubernetes port.

Do not kill unknown production process blindly.

# Part 139 — Certificate SAN Failure

Client error:

```text
x509: certificate is valid for ..., not API_ENDPOINT
```

means API server serving certificate SANs do not include used endpoint.

Regenerate correctly; do not disable TLS verification.

# Part 140 — Join Token Expired

Generate new bootstrap token/join command.

Do not weaken discovery security.

# Part 141 — Node Name Conflict

Existing Node object with same name or reused host identity can interfere with join.

Confirm previous node lifecycle/deletion before reuse.

# Part 142 — CNI Mismatch

Wrong Pod CIDR/config can cause:

```text
Node NotReady
Pods no network
cross-node failures
DNS failure
```

align kubeadm networking with CNI.

# Part 143 — Snapshot Before Major Change

Before risky control-plane operation:

```text
etcd snapshot
PKI/config backup
manifest backup
current versions
cluster inventory
```

# Part 144 — Bootstrap Documentation

Record:

```text
Kubernetes version
kubeadm config
runtime version
CNI version/config
Service CIDR
Pod CIDR
controlPlaneEndpoint
cert expiry
```

# Part 145 — Installation Final Mental Model

Cluster installation is the integration of:

```text
Linux
runtime
PKI
API
etcd
kubelet
CNI
DNS
load balancing
```

A failure in any one can make the cluster appear broken.

# Part 146 — Kubernetes Network Requirements

Network must support:

```text
Pod-to-Pod
Node-to-Pod
Pod-to-Service
Pod-to-API
DNS
external ingress/egress
```

without accidental overlapping address plans.

# Part 147 — CNI Responsibilities

A CNI plugin typically handles:

```text
Pod interface creation
IP allocation
routes/encapsulation
network policy optionally
node networking integration
```

# Part 148 — CNI Config Location

Node CNI configurations commonly reside under:

```text
/etc/cni/net.d/
```

binaries commonly:

```text
/opt/cni/bin/
```

depending on installation.

# Part 149 — Pod Sandbox Network

Runtime creates Pod sandbox then invokes CNI to attach network.

If CNI fails:

```text
FailedCreatePodSandBox
```

appears in events.

# Part 150 — FailedCreatePodSandBox

Investigate:

```text
CNI Pods
CNI node logs
/etc/cni/net.d
IPAM
routes
MTU
kernel modules
```

# Part 151 — IPAM

IP Address Management allocates Pod IPs.

Implementations vary:

```text
host-local
Calico IP pools
Cilium
cloud VPC-native
```

# Part 152 — Overlay Networking

Encapsulates Pod traffic across node network.

Examples of encapsulation technologies:

```text
VXLAN
Geneve
IP-in-IP
```

depending on CNI.

Adds MTU overhead.

# Part 153 — Routed Networking

CNI can route Pod CIDRs directly using:

```text
BGP
cloud routes
native VPC routes
```

reducing overlay but requiring underlay integration.

# Part 154 — eBPF Networking

Modern CNI solutions can use eBPF for:

```text
routing
Service load balancing
NetworkPolicy
observability
```

and may replace kube-proxy.

# Part 155 — Pod CIDR Per Node

Some CNIs/controllers allocate each Node a Pod CIDR.

Example:

```text
worker1 → 10.244.1.0/24
worker2 → 10.244.2.0/24
```

# Part 156 — Cross-Node Packet Path

Pod A → Pod B on another Node:

```text
Pod A
 ↓ veth
CNI interface/routing
 ↓
Node A
 ↓ overlay/routed underlay
Node B
 ↓ CNI
Pod B
```

# Part 157 — MTU Planning

If underlay MTU is 1500 and overlay adds 50 bytes, Pod MTU may need around 1450.

Exact value depends on encapsulation.

Wrong MTU causes hard-to-diagnose large-packet failures.

# Part 158 — Service Virtual IP

ClusterIP is virtual address.

No process necessarily binds that IP.

kube-proxy/eBPF programs data plane to forward to Pod endpoints.

# Part 159 — kube-proxy Modes

Implementations vary by version/environment.

Historically:

```text
iptables
IPVS
```

modern Kubernetes also develops nftables support, while eBPF CNIs can implement Service handling independently.

# Part 160 — iptables Service Concept

Rules transform:

```text
ServiceIP:port
→ selected PodIP:targetPort
```

using NAT chains.

Large clusters can have many rules.

# Part 161 — IPVS Concept

Linux IP Virtual Server maintains virtual-service tables and load-balances connections to real servers.

Requires IPVS kernel support.

# Part 162 — nftables Concept

Modern Linux packet filtering uses nftables.

Recent Kubernetes versions include evolving kube-proxy nftables support.

Verify feature maturity/current defaults before production change.

# Part 163 — kube-proxy Logs

If Service forwarding fails:

```text
kube-proxy Pod/process logs
ConfigMap/config
node firewall
EndpointSlices
kernel mode support
```

# Part 164 — EndpointSlice Controller

Watches Service selectors/Pods and creates EndpointSlices.

If endpoints wrong, inspect:

```text
labels
readiness
Service selector
EndpointSlices
```

# Part 165 — CoreDNS Deployment

CoreDNS normally runs as Deployment in `kube-system` with Service named `kube-dns`.

Inspect:

```bash
kubectl -n kube-system get deploy,pod,svc
```

# Part 166 — CoreDNS ConfigMap

CoreDNS configuration is stored in ConfigMap `coredns` in many clusters.

Corefile controls:

```text
kubernetes plugin
forwarders
cache
health
errors
```

# Part 167 — DNS Request Path

```text
Pod resolver
 ↓
kube-dns Service IP
 ↓
CoreDNS Pod
 ↓
Kubernetes API / upstream DNS
```

# Part 168 — Cluster DNS IP

Kubelet passes cluster DNS Service IP to Pods.

If kubelet `clusterDNS` mismatches actual Service, every Pod DNS can break.

# Part 169 — CoreDNS Pending

Common causes:

```text
CNI not ready
taints
resource shortage
image pull
```

# Part 170 — CoreDNS CrashLoop

Check:

```bash
kubectl -n kube-system logs deploy/coredns
kubectl -n kube-system get cm coredns -o yaml
```

invalid Corefile/plugin config is common.

# Part 171 — DNS Upstream Failure

Cluster-local names may resolve while external names fail.

Check:

```text
CoreDNS forward configuration
node resolv.conf
upstream DNS
firewall
loop detection
```

# Part 172 — systemd-resolved Loop

Linux stub resolver configurations can cause DNS forwarding loops if kubelet/CoreDNS uses wrong `/etc/resolv.conf`.

Use correct resolvConf path for distro.

# Part 173 — NodeLocal DNS Cache Concept

Optional node-local DNS cache improves:

```text
latency
conntrack pressure
DNS resilience
```

but adds another component to operate.

# Part 174 — NetworkPolicy Enforcement

NetworkPolicy requires supporting CNI.

Test actual packet behavior after policy creation.

# Part 175 — Default Deny Strategy

Namespace baseline:

```text
deny ingress
deny egress
allow DNS
allow required service flows
```

requires complete dependency inventory.

# Part 176 — Namespace Selector

Allow traffic based on namespace labels.

Protect namespace label governance because security policy may depend on them.

# Part 177 — ipBlock

NetworkPolicy can allow/deny based on CIDRs for external networks depending on policy.

NAT behavior can affect observed source IP.

# Part 178 — NetworkPolicy Troubleshooting

Check:

```text
Pod selected?
policyTypes?
namespace labels?
ports?
DNS allowed?
CNI enforcement?
```

# Part 179 — Ingress Controller Admin

Administrators install/upgrade controller and manage:

```text
LoadBalancer
class
RBAC
TLS
resource limits
metrics
default backend
security config
```

# Part 180 — IngressClass

Associates Ingress resources with intended controller.

Multiple controllers can coexist.

# Part 181 — Gateway API Administration

Platform team commonly owns:

```text
GatewayClass
Gateway
infrastructure
TLS policy
listener policy
```

application teams own Routes.

# Part 182 — Gateway API v1.6 Context

Gateway API v1.6 is a current ecosystem reference in 2026 with standardized HTTP and increasingly mature TCP/UDP routing.

Gateway API is a separate Kubernetes SIG Network project installed via CRDs/controllers, not automatically available in every cluster.

# Part 183 — HTTPRoute Attachment

Routes attach only when:

```text
parentRefs allowed
listener compatible
namespace policy permits
controller supports
```

Check status conditions.

# Part 184 — External Load Balancers

Cloud environments integrate Service `LoadBalancer` with provider controller.

On-prem requires implementation such as:

```text
MetalLB
hardware LB
cloud-like controller
```

# Part 185 — MetalLB Concept

Provides LoadBalancer IP advertisement on bare metal through L2/BGP modes.

Requires careful address pool/routing design.

# Part 186 — NodePort Range

Default NodePort range is commonly:

```text
30000-32767
```

unless API server configured otherwise.

Avoid unnecessary exposure.

# Part 187 — externalTrafficPolicy Local

Can preserve source IP by sending only to node-local endpoints.

Risk:

```text
nodes without endpoints drop/no traffic
uneven load
```

# Part 188 — Hairpin Traffic

Pod reaching Service that returns to itself/another local endpoint can involve hairpin NAT/bridge behavior.

CNI/kube-proxy must support correct semantics.

# Part 189 — Conntrack

Linux connection tracking supports NAT/stateful packet processing.

Conntrack exhaustion can cause seemingly random Service/network failures under high connection load.

# Part 190 — Conntrack Inspection

Authorized node:

```bash
conntrack -S
sysctl net.netfilter.nf_conntrack_max
```

if tool/module available.

Tune only after evidence.

# Part 191 — Node Firewall

Host firewalls can block:

```text
Pod encapsulation
NodePort
kubelet
API
BGP
DNS
```

Coordinate CNI and firewall ownership.

# Part 192 — Cloud Security Groups

Cloud network controls operate outside Kubernetes.

A Kubernetes NetworkPolicy cannot fix cloud security group blocking node traffic.

# Part 193 — Pod Egress

External egress path may include:

```text
Pod
Node
SNAT/NAT gateway
firewall
proxy
Internet
```

trace each layer.

# Part 194 — Egress Gateway Concept

Some CNI/service-mesh platforms centralize Pod egress for:

```text
stable IP
inspection
policy
audit
```

# Part 195 — Service Mesh Administration

If using mesh, admins operate:

```text
control plane
sidecars/ambient data plane
cert rotation
mTLS
policy
telemetry
upgrade compatibility
```

This significantly increases platform complexity.

# Part 196 — API Server Network Path

Nodes require reliable API access.

Failure symptoms:

```text
Node NotReady
lease renew failures
kubelet authentication issues
controller disconnect
```

# Part 197 — Kubelet Port

Kubelet secure API commonly uses TCP 10250.

Protect from unauthorized access.

API server/control plane needs access for logs/exec/metrics paths depending on architecture.

# Part 198 — Node Lease

Nodes update Lease objects in `kube-node-lease` namespace for lightweight heartbeat.

If lease updates stop, control plane may mark Node unhealthy.

# Part 199 — Network Capture

Use `tcpdump` only on authorized nodes.

Capture at:

```text
Pod veth
CNI interface
node NIC
```

to identify where packet disappears.

# Part 200 — nsenter for Pod Network

With container sandbox PID:

```bash
nsenter -t PID -n ip addr
nsenter -t PID -n ip route
```

provides namespace-level view when Pod image lacks tools.

# Part 201 — CNI Logs

CNI often runs as DaemonSet.

```bash
kubectl -n kube-system logs DS_POD
```

look for:

```text
IPAM
BGP
encapsulation
policy
node identity
```

# Part 202 — CNI Upgrade

CNI upgrade can affect every Pod network.

Review:

```text
Kubernetes compatibility
migration steps
CRDs
kernel requirements
kube-proxy mode
MTU
rollback
```

# Part 203 — Dual Stack Concept

Kubernetes supports IPv4/IPv6 dual-stack.

Requires aligned:

```text
node networking
Pod CIDRs
Service CIDRs
CNI
load balancers
DNS
applications
```

# Part 204 — IPv6 Only Concept

Possible in supporting environments, but verify all:

```text
registry
DNS
control plane
CNI
load balancer
external dependencies
```

# Part 205 — Network Address Planning

Document:

```text
node CIDR
Pod CIDR(s)
Service CIDR(s)
LoadBalancer pool
VPN/on-prem
cloud VPC
DNS
```

before production.

# Part 206 — Service Troubleshooting Recipe

```bash
kubectl get svc
kubectl get endpointslices
kubectl get pods -o wide
kubectl describe svc
```

Then test Pod IP directly and Service IP/DNS.

# Part 207 — DNS Troubleshooting Recipe

```text
Pod resolv.conf
kube-dns Service
CoreDNS endpoints
CoreDNS logs
Corefile
upstream resolver
CNI/NetworkPolicy
```

# Part 208 — Cross-Node Failure

If same-node Pod communication works but cross-node fails:

```text
overlay tunnel
BGP/routes
cloud firewall
MTU
node IP
CNI agent
```

become primary suspects.

# Part 209 — All Pods on One Node Lose Network

Check:

```text
CNI DaemonSet on node
routes/interfaces
kube-proxy
node firewall
container runtime
```

# Part 210 — NodePort Failure

Check:

```text
Service endpoints
kube-proxy/eBPF
node firewall/cloud firewall
externalTrafficPolicy
Node IP
```

# Part 211 — Ingress 502/503

Check:

```text
Ingress/Gateway route
Service
EndpointSlices
readiness
backend port
TLS
controller logs
```

# Part 212 — TLS Routing Failure

Check:

```text
certificate Secret
hostname
listener
SNI
expiry
issuer/controller
route attachment
```

# Part 213 — Network Metrics

Monitor:

```text
packet loss
latency
DNS errors
conntrack
CNI agent health
Service errors
LB health
network policy drops
```

# Part 214 — Network Runbook Requirement

Document exact packet path for:

```text
Pod→Pod
Pod→Service
Internet→Ingress→Service→Pod
Pod→Internet
Pod→API
```

for your cluster.

# Part 215 — Networking Final Mental Model

Kubernetes networking is a composition of:

```text
Linux networking
CNI
Service data plane
DNS
NetworkPolicy
Ingress/Gateway
external network/cloud controls
```

Troubleshoot each independently.

# Part 216 — Storage Administration Scope

Administrators manage:

```text
CSI drivers
StorageClasses
PV lifecycle
PVC binding
topology
expansion
snapshots
backup
permissions
```

# Part 217 — PersistentVolume

Cluster-scoped object representing storage.

PV status:

```text
Available
Bound
Released
Failed
```

# Part 218 — PersistentVolumeClaim

Namespaced storage request.

PVC binds compatible PV based on:

```text
class
capacity
access modes
selectors
volume mode
```

# Part 219 — StorageClass

Defines dynamic provisioning:

```yaml
provisioner: csi.example.com
parameters:
  type: fast
reclaimPolicy: Delete
allowVolumeExpansion: true
```

Fields vary by driver.

# Part 220 — Default StorageClass

PVC without explicit class can use default StorageClass.

Know which class is default; unexpected default can create expensive/wrong storage.

# Part 221 — Dynamic Provisioning

PVC triggers CSI external-provisioner to create backing storage.

Failures appear in PVC events and CSI logs.

# Part 222 — Static Provisioning

Admin pre-creates PV pointing to existing storage.

Useful for:

```text
legacy storage
pre-existing data
controlled Retain lifecycle
```

# Part 223 — Volume Mode Filesystem

Default commonly mounts formatted filesystem.

CSI handles attach/mount while kubelet performs node staging/publish workflows.

# Part 224 — Volume Mode Block

Raw block volume can be exposed to container directly for applications needing block device.

Requires driver/application support.

# Part 225 — Access Mode Semantics

Modes include:

```text
RWO
ROX
RWX
RWOP
```

They describe mounting/access constraints, not necessarily application locking semantics.

# Part 226 — ReadWriteOncePod

RWOP restricts volume to one Pod cluster-wide where supported.

Useful for strict single-writer stateful apps.

# Part 227 — ReclaimPolicy Delete

Deleting PVC/PV relationship can delete backing storage depending on dynamic provisioning.

Understand before cleanup.

# Part 228 — ReclaimPolicy Retain

Backing storage remains after claim release.

Admin must manually recover/rebind/clean data.

# Part 229 — VolumeBindingMode Immediate

Provision/bind PVC immediately.

Can create zonal volume before scheduler knows where Pod will run.

# Part 230 — WaitForFirstConsumer

Delays provisioning until Pod scheduling constraints are known.

Important for topology-aware zonal storage.

# Part 231 — CSI Controller Components

Common sidecars:

```text
external-provisioner
external-attacher
external-resizer
external-snapshotter
```

depending on driver.

# Part 232 — CSI Node Plugin

DaemonSet on nodes handles:

```text
node stage
mount
publish
unmount
```

and exposes CSI socket to kubelet.

# Part 233 — VolumeAttachment

For attachable storage, Kubernetes tracks attachment to Node.

Stuck attachment can block Pod moving to another Node.

# Part 234 — Multi-Attach Error

Common with single-writer block disk when old Node still holds attachment.

Investigate:

```text
old Pod/node state
VolumeAttachment
cloud storage attachment
force detach risks
```

# Part 235 — PVC Pending

Check:

```bash
kubectl describe pvc CLAIM
kubectl get storageclass
kubectl get events
```

causes:

```text
no StorageClass
provisioner down
quota
topology
invalid parameters
capacity
```

# Part 236 — Mount Failure

Pod event:

```text
FailedMount
```

check:

```text
CSI node plugin
filesystem
permissions
secret
network storage
device
```

# Part 237 — Attach Failure

`FailedAttachVolume`:

```text
cloud API
CSI controller
node identity
availability zone
attachment limit
old attachment
```

# Part 238 — Volume Expansion

If StorageClass supports:

```text
allowVolumeExpansion: true
```

PVC requested size can be increased.

Filesystem expansion behavior depends on driver/filesystem.

# Part 239 — Shrink Not Generally Supported

Kubernetes PVC/storage workflows generally do not support simply shrinking volume.

Plan capacity/backup/migration.

# Part 240 — CSI Snapshot

VolumeSnapshot API uses CRDs/controllers:

```text
VolumeSnapshotClass
VolumeSnapshot
VolumeSnapshotContent
```

when snapshot controller/driver supports.

# Part 241 — Snapshot Is Not Backup

Snapshot may remain in same storage/account/failure domain.

Backup needs:

```text
retention
isolation
restore testing
off-cluster copy
```

# Part 242 — StatefulSet PVC Lifecycle

Each StatefulSet replica can retain dedicated PVC across Pod replacement.

Deleting StatefulSet does not always delete PVCs depending on retention policies/configuration.

# Part 243 — Local Persistent Volumes

Bind storage to one Node.

High performance, but node failure can make data unavailable.

Requires scheduling topology awareness.

# Part 244 — NFS / RWX

Shared filesystems can provide RWX.

Operational risks:

```text
server HA
latency
permissions
locking
mount options
```

# Part 245 — fsGroup

Pod security context can set filesystem group for mounted volumes.

Driver/filesystem support affects ownership behavior.

# Part 246 — Storage Secrets

CSI drivers may need credentials.

Use restricted Secrets/workload identity and do not expose cloud storage admin keys broadly.

# Part 247 — Storage Capacity Monitoring

Monitor:

```text
PV/PVC requested
actual filesystem usage
backend quota
IOPS
latency
throughput
inode usage
```

# Part 248 — Disk Pressure vs PVC

Node `DiskPressure` often refers to node local filesystem/image/ephemeral storage, not necessarily external PVC capacity.

Different metrics.

# Part 249 — Ephemeral CSI Volume Concept

Some CSI drivers provide ephemeral volumes tied to Pod lifecycle.

Do not confuse with durable PVC.

# Part 250 — Generic Ephemeral Volumes

Pod can use PVC-template-like ephemeral volume, automatically creating claim tied to Pod.

Useful for per-Pod temporary provisioned storage.

# Part 251 — StorageClass Migration

Changing default StorageClass affects new PVCs only.

Migrating existing data requires copy/restore/application migration.

# Part 252 — Backup Controller Concept

Tools such as Velero-style platforms back up Kubernetes objects plus supported volume data.

They complement, not replace, etcd and application-native backup strategy.

# Part 253 — Database Backup

For databases, prefer application-consistent mechanisms:

```text
logical dump
physical backup
operator backup
quiesced snapshot
```

rather than blindly copying mounted files.

# Part 254 — Storage DR

Define:

```text
PVC inventory
data owner
RPO
RTO
backup location
restore procedure
cross-region strategy
```

# Part 255 — Storage Final Mental Model

```text
Pod
 ↓
PVC
 ↓
StorageClass / PV
 ↓
CSI
 ↓
real storage
```

Troubleshoot each layer separately.

# Part 256 — Scheduler Inputs

Scheduler considers:

```text
requests
node labels
taints
affinity
topology
volumes
ports
priority
```

not just free CPU.

# Part 257 — Node Capacity vs Allocatable

`capacity` = physical/logical total.

`allocatable` = resources available to Pods after system reservations.

```bash
kubectl describe node
```

# Part 258 — kubeReserved

Reserve resources for Kubernetes daemons:

```text
kubelet
container runtime
kube-proxy
```

so Pods cannot consume everything.

# Part 259 — systemReserved

Reserve resources for OS/system daemons:

```text
sshd
journald
kernel-related userspace
monitoring
```

# Part 260 — Eviction Thresholds

Kubelet can evict Pods under pressure based on:

```text
memory.available
nodefs.available
imagefs.available
inodes
```

thresholds.

# Part 261 — Soft vs Hard Eviction

Hard threshold can evict immediately.

Soft threshold requires condition duration/grace settings.

Tune carefully.

# Part 262 — Node Conditions

Important:

```text
Ready
MemoryPressure
DiskPressure
PIDPressure
NetworkUnavailable
```

# Part 263 — Unschedulable Node

`cordon` sets Node unschedulable:

```bash
kubectl cordon worker1
```

Existing Pods continue.

# Part 264 — Uncordon

```bash
kubectl uncordon worker1
```

allows new scheduling.

# Part 265 — Drain

```bash
kubectl drain worker1 \
  --ignore-daemonsets \
  --delete-emptydir-data
```

evicts manageable Pods for maintenance.

Flags have data/availability consequences.

# Part 266 — PodDisruptionBudget

PDB limits **voluntary disruptions**.

Example:

```text
minAvailable: 2
```

helps drain/upgrade maintain application replicas.

# Part 267 — PDB Limitations

PDB does not protect from:

```text
node crash
OOM
application failure
involuntary disruption
```

and cannot create replicas that do not exist.

# Part 268 — NodeSelector

Simple hard placement using labels.

# Part 269 — Node Affinity Required

Hard constraint.

If no matching Node:

```text
Pod Pending
```

# Part 270 — Node Affinity Preferred

Scheduler prefers but can choose other Node if needed.

Useful for soft topology preferences.

# Part 271 — Pod Affinity

Co-locate workloads based on labels/topology.

Can be computationally expensive in large clusters.

# Part 272 — Pod Anti-Affinity

Separate replicas across nodes/zones.

Strict rules can make Pods unschedulable during capacity loss.

# Part 273 — Topology Spread

Controls skew across domains such as:

```text
topology.kubernetes.io/zone
kubernetes.io/hostname
```

Often best way to evenly spread replicas.

# Part 274 — Taints

```bash
kubectl taint node worker1 dedicated=gpu:NoSchedule
```

# Part 275 — Taint Effects

```text
NoSchedule
PreferNoSchedule
NoExecute
```

`NoExecute` can evict existing Pods that do not tolerate.

# Part 276 — Toleration Seconds

For `NoExecute`, Pods can tolerate for limited time.

Useful for temporary node unreachability scenarios.

# Part 277 — PriorityClass

Assign scheduling/eviction priority to workloads.

High priority can preempt lower-priority Pods.

# Part 278 — Preemption

Scheduler may remove lower-priority Pods to make room for higher priority.

Use carefully; it shifts outage to another workload.

# Part 279 — ResourceQuota

Namespace aggregate limits.

Example:

```yaml
hard:
  requests.cpu: "20"
  requests.memory: 40Gi
  pods: "100"
```

# Part 280 — LimitRange

Sets per-object/container defaults/min/max.

Useful to prevent BestEffort or extreme requests.

# Part 281 — Quota and Scheduling

Quota rejects API creation/update before scheduler.

Pending due resources is different from API admission rejection due quota.

# Part 282 — Resource Requests

Scheduler reserves based on requests.

A Node with low live CPU but insufficient unallocated requests will reject Pod.

# Part 283 — CPU Limits

Cgroup quota can throttle containers.

Some teams omit CPU limits for latency-sensitive apps while retaining requests; decision depends on workload/tenant isolation.

# Part 284 — Memory Limits

Memory limit is critical for isolation but should exceed legitimate working set/startup.

OOM can destabilize app if too low.

# Part 285 — QoS and Eviction

Under memory pressure, BestEffort/Burstable Pods exceeding requests are generally more vulnerable than Guaranteed, but exact eviction ranking also considers usage/priority.

# Part 286 — Ephemeral Storage Requests

Protect node disks by configuring:

```text
ephemeral-storage requests
ephemeral-storage limits
```

# Part 287 — Image Garbage Collection

Kubelet removes unused images when disk thresholds reached.

Large images/rapid rollouts can create disk pressure.

# Part 288 — Container Log Rotation

Kubelet/runtime log rotation prevents node filesystem exhaustion.

Settings must align with cluster logging architecture.

# Part 289 — PID Limits

Kubelet can protect node from process exhaustion; runtime and Pod-level process controls also matter.

Monitor PIDPressure.

# Part 290 — HPA

HPA reads metrics and adjusts controller replica count.

Common CPU utilization target depends on resource requests.

# Part 291 — HPA Formula Concept

Simplified:

```text
desired replicas
≈ current replicas × current metric / target metric
```

stabilization/tolerance prevents constant oscillation.

# Part 292 — HPA Custom Metrics

Can scale on:

```text
requests/sec
queue depth
external metric
```

with metrics adapter.

# Part 293 — Cluster Autoscaler Concept

Adds/removes Nodes when Pods cannot schedule or nodes underutilized.

Cloud/platform add-on, not built-in core controller in all clusters.

# Part 294 — HPA + Cluster Autoscaler

```text
HPA creates more Pods
 ↓
Pods Pending due capacity
 ↓
Cluster Autoscaler adds Nodes
```

Startup delay must be considered.

# Part 295 — VPA Concept

Analyzes/changes resource requests.

Can conflict with HPA on same CPU/memory signals; design intentionally.

# Part 296 — Descheduler Concept

Optional tool rebalances Pods when cluster state changes, subject to policies/PDB.

Not core scheduler.

# Part 297 — Scheduler Profiles Concept

Scheduler supports configurable profiles/plugins for advanced environments.

Do not customize until default scheduler limitations are clearly identified.

# Part 298 — Multiple Schedulers Concept

Pods can specify alternate scheduler name.

Custom schedulers add operational complexity and failure modes.

# Part 299 — Scheduling Event

`FailedScheduling` event gives actionable reasons:

```text
insufficient cpu
untolerated taint
node affinity mismatch
unbound PVC
```

# Part 300 — Pending Pod Diagnosis

```bash
kubectl describe pod POD
```

Read scheduler event literally before changing cluster.

# Part 301 — Capacity Fragmentation

Cluster may have enough total CPU but no single Node fits one large Pod.

Example:

```text
4 nodes × 1 free CPU
Pod requests 3 CPU
→ Pending
```

# Part 302 — Topology and Storage

Zonal PVC may force Pod to one zone.

Scheduler must satisfy:

```text
volume topology
node affinity
resources
taints
```

simultaneously.

# Part 303 — Maintenance Planning

Before draining Node check:

```text
PDB
replicas
local storage
DaemonSets
Stateful workloads
capacity elsewhere
```

# Part 304 — Critical System Pods

System components can use priority classes and tolerations to remain schedulable during pressure.

Do not copy critical priority to normal apps.

# Part 305 — Scheduling Final Mental Model

Scheduler solves a constraint problem.

Every new constraint improves intent but reduces available placement options.

Design for failure capacity, not only normal state.

# Part 306 — Kubernetes Security Layers

```text
authentication
authorization
admission
Pod security
network policy
secrets
etcd encryption
node security
image security
audit
```

# Part 307 — Human Authentication

Prefer centralized identity provider/OIDC in production.

Static client certs are useful for bootstrap/admin but harder to revoke/manage at scale.

# Part 308 — Client Certificate Identity

Certificate subject:

```text
CN → username
O  → groups
```

for Kubernetes client certificate authentication.

CA signing grants trust, so protect CA key.

# Part 309 — OIDC

API server can trust OIDC provider tokens.

Flow:

```text
human
 ↓ IdP
JWT
 ↓
kube-apiserver validates issuer/audience/signature
```

# Part 310 — ServiceAccount Tokens

Modern projected ServiceAccount tokens are:

```text
short-lived
audience-bound
Pod-bound
```

compared with legacy long-lived token Secrets.

# Part 311 — Disable Automount

For workload not calling Kubernetes API:

```yaml
automountServiceAccountToken: false
```

# Part 312 — RBAC Rule

```yaml
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get","list","watch"]
```

# Part 313 — Role vs ClusterRole

Role:

```text
namespaced
```

ClusterRole:

```text
cluster-scoped permissions or reusable namespaced rule set
```

# Part 314 — RoleBinding to ClusterRole

A RoleBinding can bind ClusterRole **within one namespace**.

Useful for reusable standard role.

# Part 315 — ClusterRoleBinding Risk

Binding cluster-admin to user/group grants cluster-wide power.

Audit these regularly.

# Part 316 — Aggregated ClusterRoles

Labels can aggregate rules into higher-level ClusterRoles.

Controllers/extensions use this to extend default user-facing roles.

# Part 317 — Impersonation

Authorized users can test as another identity:

```bash
kubectl auth can-i get pods \
  --as=user@example.com
```

Impersonation itself is privileged.

# Part 318 — RBAC Troubleshooting

For `Forbidden`:

```text
identity
verb
resource
API group
namespace
RoleBinding
inherited ClusterRole
```

Use `kubectl auth can-i`.

# Part 319 — Admission Controllers

Built-in controllers enforce/mutate API requests.

Examples include:

```text
NamespaceLifecycle
LimitRanger
ServiceAccount
ResourceQuota
PodSecurity
NodeRestriction
```

exact enabled set depends on cluster/version.

# Part 320 — NodeRestriction

Restricts kubelet ability to modify Node/Pod-related objects and protected labels.

Important because node credentials should not control arbitrary cluster objects.

# Part 321 — Pod Security Admission

Built-in admission implementing Pod Security Standards through namespace labels.

Modes:

```text
enforce
audit
warn
```

# Part 322 — Pod Security Levels

```text
Privileged
Baseline
Restricted
```

Restricted approximates strong defaults for ordinary workloads.

# Part 323 — Namespace PSA Labels

Concept:

```text
pod-security.kubernetes.io/enforce=restricted
pod-security.kubernetes.io/enforce-version=latest
```

Use version pinning/change process in production.

# Part 324 — SecurityContext

Enforce:

```text
runAsNonRoot
runAsUser
allowPrivilegeEscalation false
drop capabilities
readOnlyRootFilesystem
RuntimeDefault seccomp
```

# Part 325 — allowPrivilegeEscalation

Blocks processes from gaining more privileges through exec mechanisms.

Set false for ordinary apps.

# Part 326 — Seccomp RuntimeDefault

Uses runtime's default syscall filtering.

Better baseline than `Unconfined`.

# Part 327 — AppArmor in Kubernetes

Modern Kubernetes supports AppArmor profile configuration in Pod security context on supporting nodes/versions.

Profiles must exist/be supported according to current API/node behavior.

# Part 328 — SELinux

Pod security context can set SELinux options.

Commonly integrated in OpenShift and SELinux-enforcing hosts.

# Part 329 — hostPath

Host filesystem mount can bypass many isolation assumptions.

Restrict through admission/policy.

# Part 330 — Privileged Workloads

Some infrastructure components legitimately need broad host access:

```text
CNI
CSI
node monitoring
```

Place in protected namespaces, dedicated ServiceAccounts, limited operators.

# Part 331 — Secrets at Rest

By default, Kubernetes API data in etcd may not be encrypted with a separate application-level encryption provider.

Configure encryption-at-rest for Secrets/sensitive resources in production.

# Part 332 — EncryptionConfiguration

API server encryption config can define providers:

```text
KMS
AES-GCM/AES-CBC/secretbox depending version/support
identity fallback
```

Use current recommended providers.

# Part 333 — Encryption Rotation

Changing provider config does not automatically rewrite all existing objects.

Re-encrypt data through controlled API rewrite procedure.

# Part 334 — KMS Provider

External KMS integration can protect data-encryption keys and centralize key controls.

KMS availability becomes API write/read dependency for encrypted data.

# Part 335 — Secret Access Audit

Audit:

```text
who can get/list/watch secrets?
which service accounts?
cluster-admin bindings?
```

`list` often reveals all Secret contents in namespace.

# Part 336 — Audit Policy

Controls event levels:

```text
None
Metadata
Request
RequestResponse
```

by user/resource/verb.

Avoid logging sensitive Secret bodies unnecessarily.

# Part 337 — Audit Backend

API server can write audit log according to config; environments may forward to SIEM.

Plan retention/protection.

# Part 338 — ValidatingAdmissionPolicy Concept

Modern Kubernetes includes CEL-based validating admission policies for in-process policy rules.

Useful for some policies without external webhook.

# Part 339 — Mutating Webhook

Can modify object:

```text
inject sidecar
add labels
default fields
```

but adds latency/dependency.

# Part 340 — Validating Webhook

Can reject request.

Failure mode may block production deploys if webhook unavailable and `failurePolicy` fail-closed.

# Part 341 — Webhook TLS

Admission webhook requires trusted TLS between API server and webhook Service/endpoint.

Certificate expiry is common incident cause.

# Part 342 — Image Policy Concept

Admission can enforce:

```text
approved registry
digest pin
signature
SBOM/provenance
vulnerability threshold
```

through policy engines/admission integrations.

# Part 343 — Namespace Isolation

Multi-tenancy needs combination:

```text
RBAC
NetworkPolicy
ResourceQuota
LimitRange
Pod Security
separate nodes when needed
```

Namespace alone is not enough.

# Part 344 — Node Security

Harden:

```text
OS
SSH/admin access
kernel
containerd
kubelet API
filesystem permissions
CNI
credentials
```

# Part 345 — Kubelet Authentication

Kubelet secure API should authenticate clients and use webhook/appropriate authorization.

Anonymous access should not expose privileged operations.

# Part 346 — Kubelet Certificate Rotation

Kubelets can rotate client certs through Kubernetes CSR/bootstrap mechanisms.

Monitor failures/expiry.

# Part 347 — CSR API

```bash
kubectl get csr
kubectl describe csr NAME
```

Approvals must verify identity/use before signing.

# Part 348 — Certificate Expiry

kubeadm:

```bash
kubeadm certs check-expiration
```

shows kubeadm-managed certificate expiration.

# Part 349 — Certificate Renewal

kubeadm supports cert renewal commands.

After renewal, components may require restart/static Pod refresh and kubeconfigs may need redistribution.

# Part 350 — CA Rotation

CA rotation is significantly more complex than leaf certificate renewal.

Plan carefully, test, and follow current upstream procedures.

# Part 351 — ImagePull Secrets Risk

Registry Secret can expose pull credentials to anyone with Secret read permission.

Prefer node/workload identity integration where possible.

# Part 352 — Cloud Metadata Risk

Pods reaching node/cloud metadata endpoints may obtain credentials depending on platform.

Use workload identity and metadata protections.

# Part 353 — Network Segmentation

Security model:

```text
default deny
least service flows
isolated control plane
restricted node management
egress control
```

# Part 354 — Security Incident Containment

Compromised Pod:

```text
capture evidence
isolate NetworkPolicy
revoke ServiceAccount/secret
replace image
check node/runtime
review audit logs
```

Avoid destroying evidence before scope understood.

# Part 355 — Security Final Mental Model

Kubernetes API is an authorization-rich distributed control plane.

Protect credentials and cluster-admin rights as seriously as root access to infrastructure.

# Part 356 — Cordon Before Maintenance

Stop new workloads:

```bash
kubectl cordon NODE
```

# Part 357 — Drain

Evict workloads while respecting controllers/PDB where possible.

Review flags:

```text
--ignore-daemonsets
--delete-emptydir-data
--force
```

before use.

# Part 358 — Drain and emptyDir

`--delete-emptydir-data` acknowledges local ephemeral data loss.

Do not use if application improperly stores durable state there.

# Part 359 — Drain and Unmanaged Pods

Bare Pods not controlled by controller can block drain unless force options used.

Another reason to use controllers.

# Part 360 — Upgrade Planning

Before upgrade:

```text
release notes
deprecated APIs
CNI/CSI compatibility
Ingress/controller compatibility
etcd snapshot
PDB/capacity
certificate status
node OS
```

# Part 361 — Upgrade Control Plane First

kubeadm workflow generally:

```text
upgrade kubeadm
kubeadm upgrade plan
kubeadm upgrade apply
upgrade kubelet/kubectl
restart kubelet
```

on first control plane, then other nodes sequentially.

# Part 362 — kubeadm upgrade plan

Shows:

```text
current versions
available target
component configs
upgrade path
```

Use before apply.

# Part 363 — Upgrade Additional Control Planes

After first control plane upgrades cluster configuration, remaining control planes use node upgrade workflow appropriate to current kubeadm docs.

# Part 364 — Worker Upgrade

For each worker:

```text
cordon/drain
upgrade kubeadm
kubeadm upgrade node
upgrade kubelet/kubectl packages
restart
uncordon
verify
```

# Part 365 — No Skipped Minor

Upgrade sequentially:

```text
1.34 → 1.35 → 1.36
```

with validation between.

# Part 366 — Patch Upgrade

Patch upgrades within same minor are lower risk but still require testing and compatibility review.

# Part 367 — kubectl Version Skew

kubectl has supported skew relative to API server.

Use version-skew policy; do not rely on very old/new client indefinitely.

# Part 368 — kubelet Version Skew

kubelet is normally same or older than API server within supported skew, not newer in arbitrary ways.

Exact policy must be checked for current version.

# Part 369 — Rollback Cluster Version

Kubernetes downgrade is not a routine rollback.

Use:

```text
tested upgrade
etcd backup
infrastructure snapshot
application rollback
```

rather than assuming easy in-place downgrade.

# Part 370 — Control Plane HA

At least three failure-domain-aware control-plane/etcd members is common for HA.

Load balancer must target healthy API servers.

# Part 371 — Etcd Failure Domain

Do not place all etcd members on same physical host/storage failure domain despite different VMs.

# Part 372 — Control Plane Spread

Spread across:

```text
zones
racks
hosts
power domains
```

where environment supports.

# Part 373 — API Load Balancer Health

Check each backend API:

```text
TLS reachable
ready endpoint
latency
```

before routing.

# Part 374 — etcd Snapshot Schedule

Backup frequency should satisfy control-plane state RPO.

Snapshot storage should be:

```text
encrypted
off-cluster
access-controlled
versioned/retained
tested
```

# Part 375 — etcd Snapshot Contains Secrets

Snapshot includes Kubernetes Secret data and other cluster state.

Treat as highly sensitive.

# Part 376 — PKI Backup

Back up:

```text
CA cert/key as required
service-account keys
front-proxy CA
etcd CA
kubeadm config
```

according to topology.

Protect offline.

# Part 377 — DR Documentation

Recovery requires more than etcd:

```text
node/IaC
load balancer
network/CNI
storage drivers
registry
DNS
PKI
cluster add-ons
Git manifests
```

# Part 378 — Rebuild vs Restore

Two DR models:

```text
restore old control-plane state
or
build new cluster from IaC/Git + restore application data
```

Many organizations design both.

# Part 379 — Cluster Backup Scope

Classify:

```text
etcd
Kubernetes objects
CRDs
Secrets
PV data
external DBs
registry images
Git/IaC
PKI
```

# Part 380 — Certificate Expiry Runbook

Before expiry:

```text
check
renew
restart components
redistribute kubeconfigs
verify clients/nodes
```

Do not wait for outage.

# Part 381 — Node Replacement

Prefer replaceable nodes:

```text
cordon
drain
delete/rebuild
join
verify
```

instead of years of snowflake manual repair.

# Part 382 — Control Plane Node Replacement

Requires careful:

```text
etcd member
certificates
load balancer
kubeadm join
quorum
```

Never remove too many members at once.

# Part 383 — etcd Member Removal

Before decommissioning stacked control-plane member, ensure etcd cluster membership is updated safely and quorum remains.

# Part 384 — Maintenance Windows

Schedule:

```text
node patching
Kubernetes upgrades
CNI/CSI upgrades
certificate work
```

with stakeholder communication and rollback criteria.

# Part 385 — OS Patch

Kernel/runtime security patches may require reboot.

Use:

```text
cordon
drain
patch
reboot
verify
uncordon
```

# Part 386 — Runtime Upgrade

containerd/runc upgrades can affect all Pods on node.

Drain high-risk upgrades and validate CRI afterward.

# Part 387 — CNI Upgrade Strategy

Network add-on upgrade has cluster-wide blast radius.

Use vendor-supported sequence/canary where possible and monitor cross-node traffic/DNS.

# Part 388 — CSI Upgrade Strategy

Verify:

```text
controller compatibility
node plugin
snapshot CRDs
volume attachment
in-flight mounts
```

before upgrade.

# Part 389 — CoreDNS Upgrade

Review Corefile plugin compatibility and custom plugins/config.

Test cluster/external DNS.

# Part 390 — Ingress/Gateway Upgrade

Check CRDs, webhook certificates, API versions, data-plane compatibility, and route status.

# Part 391 — Upgrade Validation

After each node/control-plane step:

```text
nodes Ready
system Pods healthy
API health
DNS
Service traffic
storage
Ingress
workload smoke tests
```

# Part 392 — Rollback Criteria

Define before change:

```text
API error rate
node readiness
DNS failure
workload availability
storage errors
```

that trigger stop/rollback/recovery.

# Part 393 — Maintenance Evidence

Record:

```text
versions before/after
commands
timestamps
issues
verification
```

for audit and future improvement.

# Part 394 — Fleet Upgrade Waves

For multiple clusters:

```text
lab
dev
staging
small production
large production
```

with soak time.

# Part 395 — Lifecycle Final Mental Model

A cluster is never "installed and finished."

It is a continuously patched, upgraded, backed-up, tested distributed system.

# Part 396 — Observability Layers

Collect:

```text
API metrics/logs
etcd metrics
scheduler/controller metrics
kubelet metrics/logs
runtime logs
CNI/CSI logs
CoreDNS
workload logs/metrics/traces
node OS metrics
```

# Part 397 — Metrics Server

Provides resource metrics API for:

```text
kubectl top
HPA CPU/memory
```

It is not long-term monitoring/storage.

# Part 398 — Prometheus Concept

Prometheus scrapes time-series metrics.

Common Kubernetes stack uses:

```text
Prometheus
Alertmanager
Grafana
kube-state-metrics
node exporter
```

or managed equivalents.

# Part 399 — kube-state-metrics

Exposes object state:

```text
Deployment replicas
Pod phase
PVC state
node conditions
```

not container CPU itself.

# Part 400 — Node Metrics

Monitor:

```text
CPU
memory
disk
inodes
network
load
conntrack
PIDs
filesystem latency
```

# Part 401 — Control Plane Metrics

Monitor:

```text
API latency/errors
etcd latency/leader
scheduler attempts
controller queue depth
workqueue errors
```

# Part 402 — SLOs for Cluster

Examples:

```text
API availability
Pod scheduling latency
DNS success
workload availability
node readiness
```

Platform SLOs should reflect user impact.

# Part 403 — Events Are Ephemeral

Kubernetes Events have limited retention and are not full audit history.

Forward/observe important events externally if needed.

# Part 404 — Node Logs

Systemd nodes:

```bash
journalctl -u kubelet
journalctl -u containerd
```

# Part 405 — Control Plane Static Pod Logs

If API works:

```bash
kubectl -n kube-system logs kube-apiserver-NODE
```

If API fails:

```bash
crictl logs CONTAINER_ID
```

# Part 406 — crictl ps

```bash
crictl ps
crictl ps -a
```

shows CRI containers independent of kubectl.

# Part 407 — crictl pods

Shows Pod sandboxes:

```bash
crictl pods
```

Useful for CNI/runtime issues.

# Part 408 — crictl inspect

Inspect container/sandbox metadata.

Use to find PID/log path/runtime state.

# Part 409 — Runtime Image Troubleshooting

```bash
crictl images
crictl pull IMAGE
```

tests registry/runtime directly.

# Part 410 — API Server Down

On control-plane node:

```bash
systemctl status kubelet
crictl ps -a
crictl logs API_CONTAINER
ss -lntp | grep 6443
ls -l /etc/kubernetes/manifests
```

then check etcd/certs.

# Part 411 — etcd Down

Check:

```text
etcd static Pod logs
disk
TLS
member health
data directory
quorum
```

API server errors often reference etcd connection.

# Part 412 — Scheduler Down

Existing running Pods continue.

New Pods remain Pending without Node assignment.

Check scheduler static Pod/logs/leader election.

# Part 413 — Controller Manager Down

New ReplicaSet/Job/node reconciliation stops.

Existing Pods may run, but self-healing/control loops degrade.

# Part 414 — Kubelet Down

Node becomes NotReady after heartbeat timeout.

Containers may keep running under runtime, but API operations/probes/reconciliation on node fail.

# Part 415 — Runtime Down

Kubelet cannot create/start/manage containers.

Existing container processes may behave according to runtime/shim state, but node becomes unhealthy for workload lifecycle.

# Part 416 — Node NotReady

Check:

```bash
kubectl describe node NODE
ssh NODE
systemctl status kubelet
journalctl -u kubelet
crictl info
ip addr
df -h
```

# Part 417 — DiskPressure

Check:

```text
nodefs/imagefs
container logs
images
emptyDir
inode usage
```

clean through supported runtime/kubelet mechanisms.

# Part 418 — MemoryPressure

Check:

```text
node memory
Pod usage
requests/limits
system daemons
OOM logs
```

do not merely add memory without identifying leak/capacity.

# Part 419 — PIDPressure

Check runaway processes/containers and node PID limits.

A fork storm can destabilize node without high CPU/memory initially.

# Part 420 — Pod Pending

`describe` event reveals:

```text
resources
taints
affinity
PVC
ports
topology
```

read scheduler message first.

# Part 421 — CrashLoopBackOff

Check:

```bash
kubectl logs POD -c CONTAINER
kubectl logs POD -c CONTAINER --previous
kubectl describe pod POD
```

then config, probes, OOM, permissions.

# Part 422 — ImagePullBackOff

Check:

```text
image reference
registry auth
DNS
TLS
proxy
architecture
rate limit
```

# Part 423 — CreateContainerConfigError

Often:

```text
missing ConfigMap
missing Secret
bad key reference
invalid security config
```

# Part 424 — CreateContainerError

Often runtime-level:

```text
mount
command
security context
runtime
device
```

# Part 425 — Service No Endpoints

```text
selector mismatch
Pods not Ready
wrong namespace
```

inspect EndpointSlices.

# Part 426 — DNS Failure

Follow:

```text
Pod resolv.conf
kube-dns Service
EndpointSlices
CoreDNS Pods/logs
Corefile
NetworkPolicy
upstream
```

# Part 427 — PVC Pending

Follow:

```text
PVC events
StorageClass
CSI controller
capacity/quota
topology
```

# Part 428 — Volume Mount Failure

Follow:

```text
Pod event
VolumeAttachment
CSI controller/node logs
node filesystem
credential/network
```

# Part 429 — RBAC Forbidden

Use:

```bash
kubectl auth can-i VERB RESOURCE \
  --as SUBJECT \
  -n NAMESPACE
```

and inspect bindings.

# Part 430 — TLS Certificate Error

Determine:

```text
which endpoint?
which cert?
expiry?
SAN?
CA?
client vs server?
```

Never solve with `--insecure-skip-tls-verify` in production.

# Part 431 — High API Latency

Check:

```text
etcd disk/latency
API request volume
admission webhooks
API Priority/Fairness
control-plane CPU/memory
network
```

# Part 432 — Webhook Outage

Symptoms:

```text
InternalError
failed calling webhook
timeout
certificate error
```

Check webhook Service/endpoints/TLS/failurePolicy.

# Part 433 — CNI Outage

Symptoms:

```text
FailedCreatePodSandBox
cross-node timeout
NetworkUnavailable
```

check CNI agents/config/routes.

# Part 434 — Conntrack Exhaustion

Symptoms can be random connection failures.

Check node conntrack counters/capacity and connection patterns.

# Part 435 — Time-Skew Incident

Symptoms:

```text
certificate not yet valid
token failures
log chronology confusion
lease anomalies
```

verify NTP/clock.

# Part 436 — CKA Time Management

Performance exam skill:

```text
read task carefully
set context
do high-value tasks first
verify immediately
bookmark incomplete
```

Accuracy beats memorized shortcuts.

# Part 437 — CKA Domain Weights

Current domains:

```text
Architecture/Install/Config 25%
Workloads/Scheduling        15%
Services/Networking         20%
Storage                     10%
Troubleshooting             30%
```

Troubleshooting is the largest domain.

# Part 438 — Command Efficiency

Use:

```text
kubectl explain
--dry-run=client -o yaml
jsonpath
custom-columns
grep
aliases
```

but only if you understand output.

# Part 439 — Verification Habit

Every task ends with evidence:

```bash
kubectl get ...
kubectl describe ...
curl/nslookup
kubectl auth can-i
```

Do not assume a command succeeded semantically because exit code was zero.

# Part 440 — Kubernetes Administration Final Mental Model

A Kubernetes administrator maintains a distributed control system whose health depends on:

```text
PKI
etcd
API
controllers
scheduler
nodes
runtime
CNI
DNS
Service networking
CSI
identity
policy
observability
backup
upgrade discipline
```

Strong administration is systematic evidence-driven operation across all these layers.

---

# Supplemental Deep-Study Layer — Kubernetes Administration

> **Source distinction:** The complete uploaded Course 60 remains preserved in this enhanced file. The section below adds deeper production administration across API internals, etcd/Raft/maintenance, PKI and identity, kubeadm/node lifecycle, CRI/static Pods, CNI/Service/DNS, Gateway/Ingress, CSI/storage recovery, scheduling/node pressure, security/admission/encryption/audit, HA/DR, upgrades, observability, fleet engineering, supply chain, capacity, and incident response. Exact Kubernetes/CKA/kubeadm/add-on versions in the original source remain source-derived; verify current upstream/vendor documentation before version-specific production changes.

Preferred study flow:

```text
Concept
  ↓
Detailed explanation
  ↓
Control/data-plane mental model
  ↓
Command/configuration
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


## Advanced Deep Dive 1 — Control Plane vs Data Plane Failure

### Concept

A Kubernetes cluster can have healthy running workloads while the API/control loops are unavailable, or a healthy control plane while user traffic fails in the data plane. Administrators must monitor and troubleshoot these planes independently.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Control plane:
API + etcd + scheduler + controllers

Data plane:
nodes + runtime + CNI + Service data plane + storage + workloads
```

### Expected Evidence

The incident is classified by which plane is failing and which functions continue.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not summarize every outage as 'Kubernetes is down'.

---

## Advanced Deep Dive 2 — API Server Request Pipeline

### Concept

A mutating request passes TLS, authentication, authorization, mutating admission, schema/default validation, validating admission, storage, and watch notification.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
client
 ↓ TLS
authentication
 ↓ authorization
mutating admission
 ↓ validation/defaulting
validating admission
 ↓ etcd
 ↓ watch events
```

### Expected Evidence

A failure can be placed at a specific request-processing stage.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use the exact API error to identify the failing stage before changing policy or credentials.

---

## Advanced Deep Dive 3 — API Server Readiness

### Concept

API server process existence is not enough. Readiness endpoints expose checks for storage and internal health dependencies.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get --raw='/readyz?verbose'
kubectl get --raw='/livez?verbose'
```

### Expected Evidence

Individual health checks report success/failure when the API is reachable.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use readiness for load-balancer backend health, not only TCP port checks.

---

## Advanced Deep Dive 4 — API Server Latency Decomposition

### Concept

High API latency can originate in etcd, admission webhooks, authentication, API Priority and Fairness queues, control-plane CPU, or network latency.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get --raw='/metrics' 2>/dev/null | grep -E 'apiserver_request_duration|apiserver_flowcontrol' | head
```

### Expected Evidence

Metrics expose API request and flow-control behavior where authorized.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Investigate request class and dependency latency before scaling the API blindly.

---

## Advanced Deep Dive 5 — API Priority and Fairness

### Concept

APF protects the API from overload by classifying requests into priority levels and concurrency queues. Controller storms can otherwise starve critical administration.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get flowschemas
kubectl get prioritylevelconfigurations
```

### Expected Evidence

Configured flow schemas and priority levels are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Keep system-critical API flows protected and monitor rejected/queued requests.

---

## Advanced Deep Dive 6 — Watch and Informer Failure Modes

### Concept

Controllers depend heavily on list/watch caches. API disconnects or repeated relists can increase load and delay reconciliation.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
LIST initial state
  ↓ WATCH changes
local informer cache
  ↓ workqueue
reconcile
```

### Expected Evidence

Controller logs/metrics can distinguish watch reconnects from reconciliation errors.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat repeated watch relists as API/network pressure evidence.

---

## Advanced Deep Dive 7 — Admission Webhook Blast Radius

### Concept

A webhook with broad matching rules and fail-closed behavior can block large classes of API writes when its Service, DNS, certificate, or backend fails.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get mutatingwebhookconfigurations,validatingwebhookconfigurations
```

### Expected Evidence

Webhook scope, service references, timeout, and failurePolicy are inspectable.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Make high-impact webhooks highly available, narrowly scoped, and explicitly tested for outage behavior.

---

## Advanced Deep Dive 8 — ValidatingAdmissionPolicy

### Concept

CEL-based validating admission can enforce many policies in-process without an external webhook, reducing external dependency for suitable rules.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl api-resources | grep -i validatingadmission
```

### Expected Evidence

The cluster exposes the relevant policy APIs when supported.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Prefer built-in validation for simple deterministic policies where appropriate.

---

## Advanced Deep Dive 9 — CRD Stored Versions

### Concept

CRDs can serve multiple versions while storing one representation. Upgrade planning must account for storedVersions and conversion webhooks.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get crd <CRD> -o jsonpath='{.status.storedVersions}{"\n"}'
```

### Expected Evidence

The persisted API versions are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Migrate stored versions before removing an old served version.

---

## Advanced Deep Dive 10 — CRD Conversion Webhook Risk

### Concept

A conversion webhook outage can make CRD reads/writes fail during version conversion, impacting controllers that rely on the resource.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get crd <CRD> -o yaml | sed -n '/conversion:/,/preserveUnknownFields:/p'
```

### Expected Evidence

Conversion strategy and webhook client configuration are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat conversion webhooks as control-plane dependencies.

---

## Advanced Deep Dive 11 — Finalizer Deadlock

### Concept

Objects can remain Terminating when a finalizer controller is unavailable or cannot complete external cleanup.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get <RESOURCE> <NAME> -o jsonpath='{.metadata.deletionTimestamp}{" "}{.metadata.finalizers}{"\n"}'
```

### Expected Evidence

Deletion timestamp plus finalizer list explains why garbage collection is blocked.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Restore cleanup logic before manually removing finalizers.

---

## Advanced Deep Dive 12 — etcd Quorum Mathematics

### Concept

Raft requires a majority of voting members. Adding members increases failure tolerance only when the new members occupy independent failure domains.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```python
for n in [1,3,5,7]:
    print(n, "members -> quorum", n//2 + 1, "tolerates", n - (n//2 + 1), "failures")
```

### Expected Evidence

Quorum and tolerated member failures are explicit.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Prefer 3 or 5 well-separated members rather than many correlated members.

---

## Advanced Deep Dive 13 — etcd Member Failure vs Quorum Loss

### Concept

One failed member in a healthy three-member cluster is different from quorum loss. The first requires repair; the second prevents normal writes and may require DR.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
3 members:
1 down → quorum 2 remains
2 down → quorum lost
```

### Expected Evidence

The incident severity is based on remaining quorum, not simply member count.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Never remove/rebuild members without first calculating quorum.

---

## Advanced Deep Dive 14 — etcd Leader Election

### Concept

Leader loss is normally recoverable when quorum remains; a new leader is elected and API writes resume after a short interruption.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
etcdctl endpoint status --cluster -w table
```

### Expected Evidence

The current leader and member status are visible with proper certificates.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not restore from backup merely because the leader changed.

---

## Advanced Deep Dive 15 — etcd Disk Latency

### Concept

etcd is latency-sensitive. Slow fsync/storage can make the entire API appear slow or unstable even when CPU/memory are healthy.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
iostat -xz 1 5 2>/dev/null || true
```

### Expected Evidence

Storage latency/utilization can be correlated with etcd/API symptoms.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Place etcd on low-latency durable storage and monitor fsync latency.

---

## Advanced Deep Dive 16 — etcd Space Quota / Alarm

### Concept

etcd can enter alarm states such as NOSPACE when backend quota is exhausted; writes then fail until maintenance and space recovery occur.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
etcdctl alarm list
etcdctl endpoint status --cluster -w table
```

### Expected Evidence

Active alarms and DB sizes are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Monitor etcd DB growth and perform supported compaction/defragmentation procedures.

---

## Advanced Deep Dive 17 — etcd Compaction

### Concept

Compaction removes old MVCC revisions from logical history; it does not necessarily shrink the backend file immediately.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
revision history grows
  ↓ compaction
old revisions logically removed
  ↓ defragment
backend file can shrink
```

### Expected Evidence

Compaction and disk reclamation are treated as separate operations.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Follow current etcd maintenance guidance and avoid ad hoc direct file manipulation.

---

## Advanced Deep Dive 18 — etcd Defragmentation

### Concept

Defragmentation rewrites the backend to reclaim space after compaction. It can be I/O-intensive and should be performed one member at a time with health checks.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
etcdctl defrag --endpoints=https://127.0.0.1:2379
```

### Expected Evidence

Backend size decreases where free pages existed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Defragment one healthy member at a time and preserve quorum.

---

## Advanced Deep Dive 19 — etcd Snapshot Integrity

### Concept

A snapshot file existing does not prove recoverability. Validate snapshot metadata and copy it off-cluster with checksums.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
sha256sum snapshot.db
etcdutl snapshot status snapshot.db -w table 2>/dev/null || true
```

### Expected Evidence

Snapshot hash and metadata are recorded.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Store encrypted snapshots outside the failure domain and test restore.

---

## Advanced Deep Dive 20 — etcd Snapshot Security

### Concept

etcd snapshots contain cluster API state including Secrets and credentials. They are effectively highly sensitive control-plane backups.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
snapshot
  contains:
  API objects
  Secrets
  RBAC
  CRDs
  service-account data
```

### Expected Evidence

Backup handling is classified at the same sensitivity as cluster credentials.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Encrypt and tightly restrict snapshot storage.

---

## Advanced Deep Dive 21 — etcd Restore Isolation

### Concept

Restore should be tested in an isolated environment so a recovered cluster cannot accidentally conflict with a live production API, cloud resources, or workloads.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
snapshot
  ↓ isolated control plane
restore
  ↓ API verification
  ↓ workload/add-on smoke tests
```

### Expected Evidence

The restored state is validated without creating split-brain infrastructure.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Never test control-plane restore against the same live endpoints/resources unintentionally.

---

## Advanced Deep Dive 22 — Stacked vs External etcd

### Concept

Stacked etcd reduces host count but correlates control-plane and etcd failure. External etcd isolates state-store hosts at the cost of more infrastructure and operations.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
stacked:
cp1 API+etcd
cp2 API+etcd
cp3 API+etcd

external:
cp1/cp2/cp3 → etcd1/etcd2/etcd3
```

### Expected Evidence

The topology choice is linked to failure-domain and operational requirements.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Document the topology in an ADR and test member replacement.

---

## Advanced Deep Dive 23 — API Load Balancer

### Concept

HA clients and kubelets should use a stable control-plane endpoint backed by multiple ready API servers, not a single node IP.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
curl -k https://<CONTROL_PLANE_ENDPOINT>:6443/readyz 2>/dev/null || true
```

### Expected Evidence

The load-balanced endpoint returns API readiness when authenticated/allowed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Make the load balancer itself highly available and health-check API readiness.

---

## Advanced Deep Dive 24 — API Certificate SAN

### Concept

The API serving certificate must contain the hostnames/IPs clients actually use, including the stable control-plane endpoint.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
openssl s_client -connect <API_HOST>:6443 -servername <API_HOST> </dev/null 2>/dev/null  | openssl x509 -noout -subject -issuer -dates -ext subjectAltName 2>/dev/null
```

### Expected Evidence

Certificate validity and SANs can be compared with the client endpoint.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Fix certificate identity rather than using insecure TLS bypasses.

---

## Advanced Deep Dive 25 — PKI Inventory

### Concept

A kubeadm control plane uses multiple trust domains and credentials: Kubernetes CA, etcd CA, front-proxy CA, service-account signing keys, serving/client certificates, and kubeconfigs.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
find /etc/kubernetes/pki -maxdepth 2 -type f -printf '%p\n' 2>/dev/null | sort
```

### Expected Evidence

The local PKI inventory can be mapped to component purpose and sensitivity.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Maintain a documented PKI map and protected backup strategy.

---

## Advanced Deep Dive 26 — CA Private-Key Custody

### Concept

Possession of a Kubernetes client CA private key can create arbitrary trusted client identities. CA keys therefore deserve stronger protection than ordinary leaf credentials.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
CA private key
  ↓ sign client cert
arbitrary CN/O identity
  ↓ API authentication
```

### Expected Evidence

The trust consequence of CA compromise is explicit.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Restrict CA keys and use centralized/OIDC identity for humans where possible.

---

## Advanced Deep Dive 27 — ServiceAccount Signing Keys

### Concept

ServiceAccount signing keys issue workload API tokens and are distinct from the client certificate CA.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ls -l /etc/kubernetes/pki/sa.* 2>/dev/null || true
```

### Expected Evidence

Service-account signing material is inventoried separately.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Protect and back up signing keys according to the recovery model.

---

## Advanced Deep Dive 28 — Certificate Expiry Monitoring

### Concept

Waiting for certificate expiry creates avoidable outages. kubeadm-managed certificates should be inventoried and monitored well before expiration.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubeadm certs check-expiration
```

### Expected Evidence

Expiration dates and residual lifetimes are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Alert on certificate expiry with enough lead time for controlled renewal.

---

## Advanced Deep Dive 29 — Leaf Certificate Renewal

### Concept

Renewing a certificate may require static Pod restart or kubeconfig redistribution before components/clients consume the new material.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubeadm certs renew all
```

### Expected Evidence

Renewed files have updated validity and components can reconnect after reload/restart.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test renewal in a lab and document component reload behavior.

---

## Advanced Deep Dive 30 — CA Rotation Complexity

### Concept

Rotating a CA requires a trust-overlap strategy so clients and servers trust old/new chains during transition. It is much more complex than leaf renewal.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
old CA only
  ↓ add trust overlap
old + new trusted
  ↓ reissue leaves
new CA only
```

### Expected Evidence

The migration avoids an all-at-once trust break.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Plan CA rotation as a dedicated migration, not an emergency one-liner.

---

## Advanced Deep Dive 31 — kubeconfig Credential Scope

### Concept

Kubeconfig embeds or references cluster endpoints and user credentials. `admin.conf` or super-admin-style kubeconfigs can provide broad cluster power.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl config view --minify --raw
```

### Expected Evidence

The active cluster, user, and credential type are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Protect privileged kubeconfigs like root credentials.

---

## Advanced Deep Dive 32 — OIDC Human Authentication

### Concept

OIDC externalizes human lifecycle/MFA to an identity provider while Kubernetes consumes verified token claims as users/groups.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
human → IdP/MFA → OIDC token
                    ↓
              kube-apiserver
                    ↓ groups
                   RBAC
```

### Expected Evidence

Human cluster access can be revoked/managed centrally.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Prefer short-lived centralized human identity over static admin client certificates.

---

## Advanced Deep Dive 33 — RBAC Exact Tuple

### Concept

An RBAC decision is based on identity/groups plus verb, API group, resource/subresource, namespace, and optional resourceName. Troubleshooting must include the full tuple.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl auth can-i create pods/exec --as=<USER> -n <NS>
kubectl auth can-i list secrets --as=<USER> -n <NS>
```

### Expected Evidence

Each exact API operation returns yes/no.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Grant the smallest tuple that satisfies the task.

---

## Advanced Deep Dive 34 — RoleBinding to ClusterRole

### Concept

A namespaced RoleBinding can reuse a ClusterRole's rule set while limiting its grant to one namespace.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get rolebinding -n <NS> -o yaml
```

### Expected Evidence

The binding scope and referenced role are explicit.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use reusable ClusterRoles with RoleBindings instead of duplicating rules where appropriate.

---

## Advanced Deep Dive 35 — ClusterRoleBinding Audit

### Concept

ClusterRoleBindings can grant cluster-wide access and are a common privilege-escalation or over-permission risk.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get clusterrolebindings -o wide
```

### Expected Evidence

Subjects with cluster-wide roles can be inventoried.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Regularly review bindings to cluster-admin and other high-privilege roles.

---

## Advanced Deep Dive 36 — RBAC Wildcards

### Concept

Wildcards in verbs/resources/API groups can unintentionally grant future resources added to an API group.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
verbs: ["*"]
resources: ["*"]
apiGroups: ["*"]
```

### Expected Evidence

The risk of forward-expanding privilege is recognized.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Avoid broad wildcards in application roles.

---

## Advanced Deep Dive 37 — Impersonation

### Concept

Authorized impersonation is useful for testing access without sharing credentials, but impersonation itself is a privileged permission.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl auth can-i get pods --as=user@example.com -n app
```

### Expected Evidence

The API evaluates permissions as the impersonated subject.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Grant impersonation only to trusted administrators/support tooling.

---

## Advanced Deep Dive 38 — ServiceAccount Token Projection

### Concept

Modern projected tokens are short-lived and audience-bound. Workloads should request only the audience/lifetime they need.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```yaml
projected:
  sources:
    - serviceAccountToken:
        path: token
        audience: internal-api
        expirationSeconds: 3600
```

### Expected Evidence

The mounted token is scoped to an intended audience and expires.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Disable default automount where Kubernetes API access is not required.

---

## Advanced Deep Dive 39 — Node Authorizer / NodeRestriction

### Concept

Kubelet credentials should control only their own Node/Pods and protected node fields. NodeRestriction limits what a compromised kubelet can modify.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
node credential
  ↓ Node authorizer
  ↓ NodeRestriction admission
bounded node-specific operations
```

### Expected Evidence

Node identity cannot arbitrarily modify unrelated cluster resources when correctly configured.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Protect kubelet credentials and keep node authorization restrictions enabled.

---

## Advanced Deep Dive 40 — Pod Security Admission Rollout

### Concept

PSA supports warn, audit, and enforce modes, allowing a staged migration to Baseline or Restricted policy.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl label ns app pod-security.kubernetes.io/warn=restricted --overwrite
kubectl label ns app pod-security.kubernetes.io/audit=restricted --overwrite
```

### Expected Evidence

Existing violations become visible before enforcement.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use staged warn/audit → remediate → enforce.

---

## Advanced Deep Dive 41 — Restricted Pod Baseline

### Concept

A strong ordinary workload baseline uses non-root execution, no privilege escalation, capability drop, RuntimeDefault seccomp, and no host namespaces/privileged mode.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
```

### Expected Evidence

The workload satisfies a defensible least-privilege baseline.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Create documented exception paths for infrastructure workloads.

---

## Advanced Deep Dive 42 — Encryption at Rest Provider Order

### Concept

API encryption configuration can chain providers. The first provider encrypts new writes; later providers can decrypt existing data during migration.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
providers:
1 new KMS/encryption provider
2 old provider
3 identity only during migration if required
```

### Expected Evidence

New writes use the new provider while old data remains readable.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Plan key/provider rotation with explicit rewrite and rollback steps.

---

## Advanced Deep Dive 43 — Re-encryption Rewrite

### Concept

Changing EncryptionConfiguration does not rewrite existing objects automatically. Controlled API reads/writes are needed to re-encrypt stored data.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get secrets -A -o json >/tmp/secrets.json
# Rewrites must follow a reviewed current procedure; avoid logging secret bodies.
```

### Expected Evidence

Storage encryption state is migrated deliberately rather than assumed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test rewrite procedures and avoid exposing Secret plaintext during migration.

---

## Advanced Deep Dive 44 — KMS Availability Dependency

### Concept

External KMS increases key control but becomes an API data read/write dependency for encrypted resources.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
API server
  ↓ envelope encryption
KMS plugin/service
  ↓ KEK
etcd stores ciphertext
```

### Expected Evidence

KMS health is included in control-plane availability planning.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Design KMS HA, latency, monitoring, and recovery before using it.

---

## Advanced Deep Dive 45 — Audit Policy Design

### Concept

Audit policy should capture high-risk API actions such as Secret access, RBAC changes, exec/attach, admission changes, and node operations without logging unnecessary sensitive bodies.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```yaml
- level: Metadata
  resources:
    - group: ""
      resources: ["secrets"]
- level: Metadata
  verbs: ["create","update","patch","delete"]
```

### Expected Evidence

High-impact operations generate auditable events.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Balance forensic value against sensitive payload exposure and log volume.

---

## Advanced Deep Dive 46 — Audit Log Protection

### Concept

Audit logs can reveal usernames, resource names, source IPs, and request metadata. They need centralized retention and tamper-resistant access control.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
API server audit
  ↓ protected collector
  ↓ SIEM/log archive
```

### Expected Evidence

Security events remain available after a cluster or node incident.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Separate audit-log administration from workload administrators where possible.

---

## Advanced Deep Dive 47 — Node OS Baseline

### Concept

Kubernetes inherits Linux kernel, filesystem, DNS, time, firewall, cgroup, and package behavior. Cluster reliability starts with a controlled node OS baseline.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
uname -a
cat /etc/os-release
timedatectl status
mount | grep cgroup
```

### Expected Evidence

Kernel, distribution, time, and cgroup baseline are documented.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Standardize node images/configuration and avoid snowflake workers.

---

## Advanced Deep Dive 48 — Time Synchronization

### Concept

Clock drift breaks certificates, OIDC tokens, logs, leases, and distributed debugging.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
timedatectl status
chronyc tracking 2>/dev/null || true
```

### Expected Evidence

Nodes report synchronized time and bounded offset.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Monitor time sync as a cluster dependency.

---

## Advanced Deep Dive 49 — cgroup Driver Alignment

### Concept

Kubelet and runtime should use compatible cgroup v2/systemd behavior. Misalignment can create resource-accounting and node stability issues.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get node <NODE> -o jsonpath='{.status.nodeInfo.containerRuntimeVersion}{"\n"}'
crictl info 2>/dev/null | head -80
```

### Expected Evidence

Runtime and node configuration can be compared.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use systemd cgroup integration on modern systemd-based nodes unless platform guidance says otherwise.

---

## Advanced Deep Dive 50 — Swap Policy

### Concept

Modern Kubernetes can support configured swap modes, but accidental host swap behavior should never be left implicit.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
swapon --show
grep -R "memorySwap" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Evidence

Host swap state and kubelet policy are both known.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Follow the current Kubernetes/kubelet swap guidance for the chosen workload model.

---

## Advanced Deep Dive 51 — Kernel Module / sysctl Dependency

### Concept

CNI/runtime behavior may depend on overlay, br_netfilter, IP forwarding, conntrack, and other kernel facilities.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
lsmod | grep -E 'overlay|br_netfilter'
sysctl net.ipv4.ip_forward
```

### Expected Evidence

Required kernel facilities are explicitly verified.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use CNI/vendor-supported node settings rather than blindly copying old sysctl lists.

---

## Advanced Deep Dive 52 — Containerd CRI Health

### Concept

Kubelet depends on a healthy CRI endpoint. A running containerd process can still have CRI/config problems.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
systemctl status containerd --no-pager
crictl info
```

### Expected Evidence

CRI responds with runtime configuration and status.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use crictl to validate the kubelet-facing runtime interface.

---

## Advanced Deep Dive 53 — crictl Runtime Endpoint

### Concept

crictl should use explicit runtime/image endpoints to avoid probing wrong sockets or generating warnings.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```yaml
# /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
```

### Expected Evidence

crictl connects deterministically to the intended runtime.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Standardize crictl configuration on nodes.

---

## Advanced Deep Dive 54 — CRI Sandbox Mapping

### Concept

A Kubernetes Pod maps to a runtime Pod sandbox plus one or more containers. CNI is typically attached to the sandbox network namespace.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
crictl pods
crictl ps -a
```

### Expected Evidence

Pod sandbox IDs can be mapped to container IDs.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use sandbox evidence for FailedCreatePodSandBox/CNI troubleshooting.

---

## Advanced Deep Dive 55 — Static Pod Lifecycle

### Concept

kubeadm control-plane components are commonly static Pods watched directly from `/etc/kubernetes/manifests` by kubelet.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ls -l /etc/kubernetes/manifests
crictl ps -a | grep -E 'kube-apiserver|etcd|scheduler|controller'
```

### Expected Evidence

Manifest files map to CRI containers even when the API is unavailable.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use node-local tools first during control-plane outages.

---

## Advanced Deep Dive 56 — Static Pod Manifest Safety

### Concept

Any file interpreted as a manifest in the static Pod directory can trigger kubelet changes. Editors/backups in that directory can have unintended effects.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
/etc/kubernetes/manifests/
  kube-apiserver.yaml
  scheduler.yaml
  accidental-backup.yaml  ← potentially dangerous
```

### Expected Evidence

Only intended static Pod manifests exist in the watched directory.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Keep backups outside the manifest path and make atomic reviewed changes.

---

## Advanced Deep Dive 57 — kubeadm Config as Code

### Concept

A kubeadm configuration file captures cluster-wide networking, endpoint, version, etcd, API, and kubelet decisions more reproducibly than a long command line.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubeadm config print init-defaults > kubeadm-init.yaml
```

### Expected Evidence

Bootstrap configuration is version-controlled and reviewable.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat kubeadm config as infrastructure source, not one-time shell history.

---

## Advanced Deep Dive 58 — kubeadm Preflight

### Concept

Preflight failures usually identify real prerequisites: swap, ports, files, runtime, identity, or privileges. Suppressing checks can turn clear bootstrap errors into later failures.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubeadm init --config kubeadm-init.yaml --dry-run
```

### Expected Evidence

Preflight findings are reviewed before cluster creation.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Resolve preflight causes instead of broadly ignoring them.

---

## Advanced Deep Dive 59 — Pod/Service CIDR Planning

### Concept

Pod and Service address ranges must not overlap node, VPC, VPN, on-prem, load-balancer, or each other.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Node:    10.10.0.0/16
Pods:    10.244.0.0/16
Services:10.96.0.0/12
LB pool: 10.20.50.0/24
```

### Expected Evidence

Every address domain is documented and non-overlapping.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Design IPAM before installing the CNI.

---

## Advanced Deep Dive 60 — Pod CIDR Capacity Math

### Concept

Pod CIDR size must cover nodes × Pods per node plus growth and CNI allocation mechanics.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```python
nodes = 100
pods_per_node = 110
needed = nodes * pods_per_node
print("Pod addresses required before reserve:", needed)
```

### Expected Evidence

Address demand is estimated before choosing CIDRs.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Leave address headroom for growth and CNI allocation blocks.

---

## Advanced Deep Dive 61 — Service CIDR Immutability Risk

### Concept

Changing Service CIDR after cluster creation is complex and affects DNS/API Service assumptions and Service IP allocation.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Service CIDR
  ↓ kube-apiserver/controller-manager
  ↓ cluster DNS Service
  ↓ all ClusterIPs
```

### Expected Evidence

The Service address plan is treated as foundational cluster configuration.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Choose Service CIDR carefully before production bootstrap.

---

## Advanced Deep Dive 62 — kubeadm Join Trust

### Concept

Bootstrap token discovery plus CA public-key hash helps a joining node verify it is talking to the intended control plane.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubeadm token create --print-join-command
```

### Expected Evidence

The join command contains endpoint, token, and CA pin.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat bootstrap tokens as short-lived and regenerate when needed.

---

## Advanced Deep Dive 63 — Node Name Reuse

### Concept

Reusing a hostname without cleaning old Node objects/certificates can create identity confusion during join.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get nodes
hostnamectl
```

### Expected Evidence

The intended node identity is unique.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use replaceable node lifecycle and cleanly delete stale Node objects before reuse.

---

## Advanced Deep Dive 64 — kubeadm Reset Scope

### Concept

`kubeadm reset` removes kubeadm-managed state but may leave CNI config/interfaces, firewall rules, user kubeconfig, containers, and external resources.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubeadm reset --dry-run 2>/dev/null || true
```

### Expected Evidence

Operators understand reset is not a complete machine reimage.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Reimage nodes for clean reproducible rebuilds when practical.

---

## Advanced Deep Dive 65 — Air-Gapped Dependency Inventory

### Concept

Offline Kubernetes requires internal access to OS packages, Kubernetes packages, control-plane images, pause image, CNI/CSI, DNS, ingress, charts, and application images.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
internal mirrors:
apt/rpm
registry
Helm/OCI charts
Git/artifacts
time/DNS/PKI
```

### Expected Evidence

Every bootstrap/runtime dependency has an offline source.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test an installation with Internet physically blocked before declaring it air-gapped.

---

## Advanced Deep Dive 66 — Registry Mirror Trust

### Concept

Node registry mirrors improve reliability and control but become cluster supply-chain dependencies.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
nodes/containerd
  ↓ internal mirror
  ↓ approved upstream
```

### Expected Evidence

Nodes pull through a managed trusted path.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Harden mirrors with TLS, auth, retention, scanning, and monitoring.

---

## Advanced Deep Dive 67 — CNI Responsibility

### Concept

The CNI layer creates Pod interfaces, assigns addresses, establishes routes/encapsulation, and often enforces NetworkPolicy.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
kubelet/runtime
  ↓ CNI ADD
network namespace
  ↓ veth/IP/routes/policy
Pod network ready
```

### Expected Evidence

Pod sandbox events can be correlated with CNI agent/config state.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Know exactly which CNI component owns IPAM, routing, and policy.

---

## Advanced Deep Dive 68 — FailedCreatePodSandBox

### Concept

FailedCreatePodSandBox usually occurs before app container start and frequently points to CNI, sandbox image, network namespace, or runtime setup.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
crictl pods
```

### Expected Evidence

The event message identifies runtime/CNI setup failure.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not debug application logs when the sandbox never started.

---

## Advanced Deep Dive 69 — CNI Config Inventory

### Concept

Node-local CNI config and binaries are part of cluster state not stored completely in the Kubernetes API.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ls -l /etc/cni/net.d 2>/dev/null
ls -l /opt/cni/bin 2>/dev/null | head
```

### Expected Evidence

Installed CNI configs/binaries are known.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Manage node CNI state declaratively through the supported add-on installer.

---

## Advanced Deep Dive 70 — Overlay MTU

### Concept

Encapsulation such as VXLAN/Geneve consumes MTU. Incorrect Pod MTU often causes small packets to work while large TLS responses stall.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ip link
ping -M do -s 1400 <AUTHORIZED_PEER> 2>/dev/null || true
```

### Expected Evidence

Interface MTUs and path behavior can be compared.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Derive Pod MTU from the actual underlay and encapsulation.

---

## Advanced Deep Dive 71 — Routed/BGP CNI

### Concept

Routed CNIs can advertise Pod prefixes through BGP or native routes instead of encapsulating every packet.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
worker PodCIDR
  ↓ BGP/native route
underlay
  ↓
remote worker PodCIDR
```

### Expected Evidence

Cross-node routing is visible in route/BGP state rather than tunnels.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Coordinate CNI routing with the data-center/cloud network team.

---

## Advanced Deep Dive 72 — eBPF Service Data Plane

### Concept

Some CNIs implement Service load balancing and policy with eBPF, potentially replacing kube-proxy. Troubleshooting must match the installed data plane.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-system get ds | grep -E 'cilium|calico|kube-proxy'
```

### Expected Evidence

The cluster's actual Service/network implementation is identified.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Never apply kube-proxy-specific troubleshooting assumptions to a kube-proxy-free cluster.

---

## Advanced Deep Dive 73 — kube-proxy Mode

### Concept

iptables, IPVS, nftables, or another data plane have different kernel structures and troubleshooting tools.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-system get cm kube-proxy -o yaml 2>/dev/null | head -120
```

### Expected Evidence

Configured kube-proxy mode can be identified where kube-proxy is used.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Document the Service data-plane implementation per cluster.

---

## Advanced Deep Dive 74 — Service Packet Path

### Concept

A ClusterIP request flows through Service lookup/NAT/load balancing to a Ready Pod endpoint, then returns through node/CNI paths.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
client Pod
  ↓ Service VIP:port
Service data plane
  ↓ selected EndpointSlice address
target Pod
```

### Expected Evidence

Each layer can be tested independently.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Check EndpointSlices before node packet rules.

---

## Advanced Deep Dive 75 — EndpointSlice Conditions

### Concept

EndpointSlice ready/serving/terminating state affects traffic during rollout and graceful termination.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get endpointslices -l kubernetes.io/service-name=<SVC> -o yaml
```

### Expected Evidence

Endpoint lifecycle is visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use endpoint conditions to explain traffic gaps during rollout.

---

## Advanced Deep Dive 76 — Conntrack Pressure

### Concept

Stateful Service NAT and high connection churn can exhaust conntrack tables, causing seemingly random connection failures.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
sysctl net.netfilter.nf_conntrack_max 2>/dev/null || true
conntrack -S 2>/dev/null || true
```

### Expected Evidence

Capacity and insert/drop counters are available where tooling is installed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Tune conntrack only after measuring connection behavior and table pressure.

---

## Advanced Deep Dive 77 — Ephemeral Port Pressure

### Concept

High-fanout node or Pod egress can exhaust source-port/NAT capacity independently of CPU or bandwidth.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
sysctl net.ipv4.ip_local_port_range
ss -s
```

### Expected Evidence

Socket and port-range evidence supports or rejects the hypothesis.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use connection pooling/reuse and adequate NAT capacity.

---

## Advanced Deep Dive 78 — CoreDNS Request Path

### Concept

Pod DNS traverses the Pod resolver, kube-dns Service VIP, Service data plane, CoreDNS Pod, and possibly upstream resolvers.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Pod /etc/resolv.conf
  ↓ kube-dns ClusterIP
CoreDNS
  ↓ kubernetes plugin / forward
upstream DNS
```

### Expected Evidence

Cluster-local and external DNS paths can be isolated.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test `kubernetes.default` separately from external domains.

---

## Advanced Deep Dive 79 — CoreDNS ConfigMap Change Risk

### Concept

An invalid Corefile can crash all CoreDNS Pods and create cluster-wide name-resolution failure.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-system get cm coredns -o yaml
kubectl -n kube-system logs deploy/coredns --tail=100
```

### Expected Evidence

Configuration and parser/runtime errors are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Validate CoreDNS changes in a staging cluster and retain rollback.

---

## Advanced Deep Dive 80 — systemd-resolved Interaction

### Concept

On some Linux distributions, kubelet/CoreDNS forwarding to a stub resolver can create loops or broken upstream DNS.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
readlink -f /etc/resolv.conf
cat /run/systemd/resolve/resolv.conf 2>/dev/null || true
```

### Expected Evidence

The node's real upstream resolver file can be distinguished from a local stub.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Configure kubelet resolvConf according to the OS/CNI guidance.

---

## Advanced Deep Dive 81 — NodeLocal DNS Cache

### Concept

Node-local DNS caching can reduce CoreDNS load and conntrack pressure but introduces node-local agents/configuration to operate.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-system get ds | grep -i dns
```

### Expected Evidence

The cluster can identify whether node-local DNS is installed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Monitor cache agents and preserve fallback behavior.

---

## Advanced Deep Dive 82 — NetworkPolicy Enforcement Verification

### Concept

A NetworkPolicy object is only useful if the CNI enforces it. Admins must test packet behavior, not merely object existence.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get networkpolicy -A
kubectl -n <NS> run test --rm -it --image=busybox -- sh
```

### Expected Evidence

An allowed flow succeeds and a denied flow fails in the authorized lab.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Include policy-enforcement tests in CNI upgrades.

---

## Advanced Deep Dive 83 — Default-Deny Egress

### Concept

Default-deny egress requires an explicit inventory of DNS, registries, APIs, databases, time, proxies, and external dependencies.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
deny all
  + DNS
  + database
  + required external API
  + registry only if workload pulls directly
```

### Expected Evidence

The dependency list becomes part of application/network policy.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Roll out deny egress gradually with observability.

---

## Advanced Deep Dive 84 — Ingress Controller HA

### Concept

Ingress is cluster edge infrastructure. Multiple replicas, spread, PDB, resource sizing, load-balancer health, and certificate management are platform concerns.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get deploy -A | grep -i ingress
kubectl get pdb -A
```

### Expected Evidence

Controller replica and disruption configuration are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat ingress as a production service with its own SLO.

---

## Advanced Deep Dive 85 — Ingress 502/503 Decomposition

### Concept

An ingress error can come from listener/TLS, route rule, Service, EndpointSlice, readiness, backend port, NetworkPolicy, or application response.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe ingress <ING>
kubectl get svc <SVC>
kubectl get endpointslices -l kubernetes.io/service-name=<SVC>
```

### Expected Evidence

The failing hop is isolated.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Walk edge → route → Service → endpoint → app.

---

## Advanced Deep Dive 86 — Gateway API Ownership

### Concept

Gateway API allows platform teams to own GatewayClass/Gateway and application teams to own Routes under attachment policy.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get gatewayclasses,gateways,httproutes -A
```

### Expected Evidence

Infrastructure and route resources can be audited separately.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use attachment policy to preserve tenancy boundaries.

---

## Advanced Deep Dive 87 — Gateway API Status Conditions

### Concept

Gateway/Route status conditions expose listener acceptance, reference resolution, and programmed state.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get httproute <ROUTE> -o yaml | sed -n '/status:/,$p'
```

### Expected Evidence

Rejected parent/backend references are explicit.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use status before editing DNS or load balancers.

---

## Advanced Deep Dive 88 — LoadBalancer Service on Bare Metal

### Concept

Bare-metal clusters need an implementation to assign/advertise LoadBalancer addresses, such as BGP/L2 software or an external appliance.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Service type LoadBalancer
  ↓ controller
address pool
  ↓ L2/BGP/appliance advertisement
```

### Expected Evidence

The source of external IP allocation is documented.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Avoid assuming cloud-controller behavior exists on-premises.

---

## Advanced Deep Dive 89 — StorageClass Governance

### Concept

The default StorageClass influences cost, performance, availability zone, encryption, and reclaim behavior for every PVC that omits `storageClassName`.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get storageclass
```

### Expected Evidence

The default class and key parameters are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use deliberate defaults and document service-level characteristics.

---

## Advanced Deep Dive 90 — CSI Controller vs Node Plugin

### Concept

CSI controller components provision/attach/resize while node plugins stage/mount/unmount on each worker.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pods -A | grep -i csi
kubectl get csidrivers
```

### Expected Evidence

Controller Deployments and node DaemonSets can be mapped.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Troubleshoot provision/attach and mount as separate CSI paths.

---

## Advanced Deep Dive 91 — PVC Pending

### Concept

Pending claims usually indicate StorageClass/provisioner/topology/quota/capacity issues before any container starts.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe pvc <PVC>
kubectl get storageclass
```

### Expected Evidence

PVC events identify the storage control-plane failure.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Read claim events before changing the workload controller.

---

## Advanced Deep Dive 92 — VolumeAttachment

### Concept

Attachable volumes create VolumeAttachment objects linking PV/CSI driver to a Node. Stale attachments can block failover.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get volumeattachments
```

### Expected Evidence

Attachment state and target node are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not force-detach until the old node's write ownership is understood.

---

## Advanced Deep Dive 93 — Multi-Attach Failure

### Concept

Single-writer block volumes cannot safely attach read-write to multiple nodes. Node failure can leave an old attachment that delays recovery.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Pod old node
  ↓ volume attached
node fails
replacement Pod new node
  ↓ multi-attach blocked
```

### Expected Evidence

The storage system and VolumeAttachment identify the current attachment owner.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use fencing/driver-supported detach procedures for stateful failover.

---

## Advanced Deep Dive 94 — WaitForFirstConsumer

### Concept

Delayed binding prevents zonal storage from being provisioned before scheduler knows the Pod's topology.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get storageclass <SC> -o jsonpath='{.volumeBindingMode}{"\n"}'
```

### Expected Evidence

The binding mode reflects topology-aware provisioning.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use WaitForFirstConsumer for zonal storage unless the driver has another documented model.

---

## Advanced Deep Dive 95 — Volume Expansion

### Concept

PVC expansion can involve controller-side resize and node/filesystem resize. A larger PVC object does not always mean the mounted filesystem already grew.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pvc <PVC>
kubectl describe pvc <PVC>
```

### Expected Evidence

Conditions/events show resize progression.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Verify filesystem capacity inside the workload after expansion.

---

## Advanced Deep Dive 96 — Volume Snapshot Control Plane

### Concept

CSI snapshots use VolumeSnapshot, VolumeSnapshotContent, VolumeSnapshotClass plus snapshot-controller/driver integration.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl api-resources | grep -i volumesnapshot
```

### Expected Evidence

Snapshot APIs exist only when the required CRDs/controllers are installed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat snapshots as optional CSI ecosystem functionality, not automatic core storage.

---

## Advanced Deep Dive 97 — Snapshot vs Backup

### Concept

Storage snapshots can be fast recovery points but may share account/region/storage failure domains and may be crash-consistent only.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
snapshot → fast local recovery
backup   → independent retention + isolation + restore test
```

### Expected Evidence

The recovery architecture distinguishes local snapshot from disaster backup.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Define off-cluster/off-domain backup for critical state.

---

## Advanced Deep Dive 98 — Database Consistency

### Concept

Databases may require native backup, WAL/log capture, quiesce, or operator-aware snapshots. Copying PVC files during writes can be inconsistent.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
database checkpoint/quiesce
  ↓ snapshot/backup
  ↓ resume
  ↓ restore validation
```

### Expected Evidence

Recovery produces a database that passes application integrity checks.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use database-aware backup semantics.

---

## Advanced Deep Dive 99 — Reclaim Policy Risk

### Concept

Delete reclaim policy can destroy backing storage when claims/PVs are deleted; Retain requires manual lifecycle management.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pv -o custom-columns=PV:.metadata.name,RECLAIM:.spec.persistentVolumeReclaimPolicy,STATUS:.status.phase
```

### Expected Evidence

Data-destruction behavior is visible before cleanup.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Require review for deletion of data-bearing PVCs/PVs.

---

## Advanced Deep Dive 100 — Node Capacity vs Allocatable

### Concept

Node capacity is total hardware; allocatable subtracts kube/system reservations and eviction requirements. Scheduler uses allocatable.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get node <NODE> -o jsonpath='{.status.capacity}{"\n"}{.status.allocatable}{"\n"}'
```

### Expected Evidence

Capacity and scheduler-available resources differ.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Reserve resources explicitly for the OS and Kubernetes daemons.

---

## Advanced Deep Dive 101 — kubeReserved / systemReserved

### Concept

Without reservations, Pods can crowd out kubelet, runtime, journald, CNI, and OS processes and make the node fail under load.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
node capacity
 - systemReserved
 - kubeReserved
 - eviction reserve
 = allocatable
```

### Expected Evidence

Host overhead is accounted before scheduling application Pods.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Capacity-plan the node as a system, not just a sum of Pod limits.

---

## Advanced Deep Dive 102 — Eviction Signals

### Concept

Kubelet monitors memory, nodefs/imagefs space/inodes, and other signals and can evict Pods before the node becomes unusable.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
grep -n "eviction" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Evidence

Configured eviction thresholds can be reviewed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Tune eviction with storage layout and workload behavior.

---

## Advanced Deep Dive 103 — DiskPressure Decomposition

### Concept

DiskPressure may come from container images, writable layers, logs, emptyDir, runtime metadata, or inode exhaustion.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
df -h
df -i
crictl images
du -sh /var/log/pods /var/log/containers 2>/dev/null || true
```

### Expected Evidence

The node-local disk consumer is identified.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use kubelet/runtime-supported cleanup rather than deleting random runtime files.

---

## Advanced Deep Dive 104 — Image Garbage Collection

### Concept

Kubelet garbage-collects unused images based on disk thresholds; large images and rapid rollouts can still create imagefs pressure.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
crictl images
grep -n "imageGCHighThresholdPercent\|imageGCLowThresholdPercent" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Evidence

Image inventory and GC thresholds are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Monitor imagefs usage and keep images small/immutable.

---

## Advanced Deep Dive 105 — Container Log Rotation

### Concept

Kubelet/runtime log rotation protects node disk, while centralized logging preserves history beyond local files.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
grep -n "containerLogMax" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Evidence

Local per-container rotation settings can be reviewed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Coordinate kubelet log rotation with the log collector.

---

## Advanced Deep Dive 106 — MemoryPressure

### Concept

Node memory pressure can trigger evictions even if an individual Pod has not exceeded its limit.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe node <NODE> | sed -n '/Conditions:/,/Allocated resources:/p'
free -h
```

### Expected Evidence

Node pressure and host memory state can be compared.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Distinguish node-level memory exhaustion from cgroup OOM.

---

## Advanced Deep Dive 107 — PIDPressure

### Concept

Runaway processes/threads can exhaust the node PID namespace without consuming extraordinary CPU/memory.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ps -e --no-headers | wc -l
kubectl describe node <NODE> | grep -A2 PIDPressure
```

### Expected Evidence

Node PID usage and pressure condition are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Apply process limits and investigate process leaks/fork storms.

---

## Advanced Deep Dive 108 — Scheduling Constraint Order

### Concept

Scheduler filters nodes by resources, taints, affinity, volume topology, ports, and other predicates before scoring remaining nodes.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Evidence

FailedScheduling messages list unsatisfied constraints.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Read scheduler events before changing node labels or resources.

---

## Advanced Deep Dive 109 — Capacity Fragmentation

### Concept

A cluster can have enough total free CPU/memory but no single node large enough for one Pod request.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
4 nodes × 1 CPU free
Pod requests 3 CPU
→ unschedulable
```

### Expected Evidence

Aggregate capacity is distinguished from per-node fit.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Track large-Pod fit and consider node-pool sizing.

---

## Advanced Deep Dive 110 — Topology Spread

### Concept

Topology spread can balance replicas across hostname/zone with controlled skew and explicit behavior when constraints cannot be satisfied.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pod -l app=api -o custom-columns=POD:.metadata.name,NODE:.spec.nodeName,ZONE:.metadata.labels.topology\.kubernetes\.io/zone
```

### Expected Evidence

Replica distribution across nodes/zones is visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test loss of a topology domain, not just normal distribution.

---

## Advanced Deep Dive 111 — PDB Semantics

### Concept

PDB limits voluntary disruptions, not node crashes, OOM, app failures, or all upgrade risks.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pdb -A
```

### Expected Evidence

Allowed disruptions and current healthy counts are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Set PDBs so maintenance remains possible under realistic capacity.

---

## Advanced Deep Dive 112 — Drain Prechecks

### Concept

Before drain, inspect PDBs, unmanaged Pods, DaemonSets, emptyDir, local PVs, StatefulSets, and spare capacity.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pods -A -o wide --field-selector spec.nodeName=<NODE>
kubectl get pdb -A
```

### Expected Evidence

Node workload inventory is known before eviction.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Never run drain blindly on stateful or capacity-constrained nodes.

---

## Advanced Deep Dive 113 — Cordon vs Drain

### Concept

Cordon only stops new scheduling; drain evicts eligible workloads. Confusing them can leave stateful services running during maintenance.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl cordon <NODE>
kubectl drain <NODE> --ignore-daemonsets
```

### Expected Evidence

The node becomes unschedulable, then managed workloads move according to policy.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use cordon for immediate placement stop and drain for maintenance evacuation.

---

## Advanced Deep Dive 114 — Priority and Preemption

### Concept

Higher-priority Pods can preempt lower-priority Pods when necessary. This protects critical workloads by moving impact elsewhere.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get priorityclasses
```

### Expected Evidence

Priority classes and values are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Reserve high priority for workloads whose importance justifies preemption.

---

## Advanced Deep Dive 115 — ResourceQuota

### Concept

Quota limits namespace aggregate resource/object consumption and rejects API requests before scheduling when the quota would be exceeded.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get resourcequota -A
kubectl describe resourcequota -n <NS>
```

### Expected Evidence

Used versus hard quota is visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use quotas to contain tenants and create predictable capacity boundaries.

---

## Advanced Deep Dive 116 — LimitRange

### Concept

LimitRange can default/bound requests and limits for namespace objects, reducing accidental BestEffort workloads.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get limitrange -A
```

### Expected Evidence

Namespace resource defaults/min/max are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Pair LimitRange with quota and application right-sizing.

---

## Advanced Deep Dive 117 — HPA Request Dependency

### Concept

CPU utilization HPA needs resource requests because utilization is relative to requested CPU.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe hpa <HPA>
```

### Expected Evidence

Current metric, target, and replica recommendation are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Fix missing/incorrect requests before tuning HPA targets.

---

## Advanced Deep Dive 118 — HPA Stabilization

### Concept

Scaling behavior includes tolerance and stabilization windows to reduce rapid oscillation.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
metric spike
  ↓ desired replicas
stabilization policy
  ↓ bounded scale action
```

### Expected Evidence

Autoscaling does not chase every momentary metric change.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Tune stabilization using workload startup and traffic patterns.

---

## Advanced Deep Dive 119 — Cluster Autoscaler Interaction

### Concept

HPA can create Pending Pods that drive a cluster autoscaler to add nodes. End-to-end response includes metrics, scheduling, node provisioning, and Pod startup.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
load ↑
HPA replicas ↑
Pending Pods
node autoscaler
new node
Pod start
```

### Expected Evidence

Burst response time includes multiple control loops.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Keep spare capacity or queues for traffic faster than node provisioning.

---

## Advanced Deep Dive 120 — Multi-Team Namespace Baseline

### Concept

A production namespace template should include ownership labels, quota, LimitRange, Pod security, default-deny policy, ServiceAccounts/RBAC, and observability.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Namespace
  + owner labels
  + quota
  + LimitRange
  + PSA
  + NetworkPolicy
  + RBAC
```

### Expected Evidence

New teams receive consistent guardrails.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Automate namespace provisioning rather than creating empty namespaces manually.

---

## Advanced Deep Dive 121 — Node Pool Separation

### Concept

Dedicated node pools can isolate GPU, untrusted, regulated, storage-heavy, or system workloads using taints/affinity and infrastructure controls.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
general pool
gpu pool
system pool
untrusted sandbox pool
```

### Expected Evidence

Workloads land on intended hardware/trust domains.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use separate pools only when the isolation/capability requirement justifies capacity fragmentation.

---

## Advanced Deep Dive 122 — Kubelet Secure Port

### Concept

Kubelet's authenticated HTTPS endpoint is a sensitive node-management surface used for logs/exec/metrics pathways.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ss -lntp | grep 10250
```

### Expected Evidence

The kubelet secure listener is visible on the node.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Restrict network access and keep anonymous/authorization settings hardened.

---

## Advanced Deep Dive 123 — Kubelet Logs

### Concept

Many node failures are explained by kubelet journal messages: certificate, CNI, eviction, runtime, volume, or static Pod errors.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
journalctl -u kubelet -b --no-pager | tail -120
```

### Expected Evidence

Recent node-agent failures are available even if kubectl is unavailable.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Preserve node logs before restarting kubelet.

---

## Advanced Deep Dive 124 — Runtime Logs

### Concept

containerd/runc failures may not be fully represented in Pod events. Runtime journal and crictl provide lower-level evidence.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
journalctl -u containerd -b --no-pager | tail -120
crictl ps -a
```

### Expected Evidence

Runtime errors can be correlated with Kubernetes container state.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use runtime evidence for CreateContainerError and image/sandbox failures.

---

## Advanced Deep Dive 125 — Control Plane without API

### Concept

When the API server is down, use systemd, static manifests, crictl, ss, PKI files, and etcd tools on the node.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
systemctl status kubelet --no-pager
crictl ps -a
ss -lntp | grep -E '6443|2379'
ls -l /etc/kubernetes/manifests
```

### Expected Evidence

The control-plane failure can be investigated without kubectl.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Practice API-down troubleshooting before an actual incident.

---

## Advanced Deep Dive 126 — Scheduler Failure

### Concept

If scheduler is unavailable, existing Pods continue but newly created unscheduled Pods remain Pending with no node assignment.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pods -A --field-selector spec.nodeName=
kubectl -n kube-system get pod -l component=kube-scheduler
```

### Expected Evidence

Unscheduled Pods and scheduler component state are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Differentiate scheduler outage from unsatisfied scheduling constraints.

---

## Advanced Deep Dive 127 — Controller Manager Failure

### Concept

Controller-manager outage stops many reconciliation loops: replica replacement, Job progress, node lifecycle, endpoints, and more.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-system get pod -l component=kube-controller-manager
```

### Expected Evidence

Controller component health can be checked when API still works.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Expect existing Pods to run while desired-state convergence degrades.

---

## Advanced Deep Dive 128 — Kubelet Failure

### Concept

When kubelet stops, runtime containers may keep running temporarily but node heartbeats, probes, new lifecycle operations, and API status updates fail.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
systemctl status kubelet --no-pager
kubectl describe node <NODE>
```

### Expected Evidence

Node Ready/Lease behavior can be correlated with kubelet state.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Fix the node agent rather than immediately deleting workloads.

---

## Advanced Deep Dive 129 — Container Runtime Failure

### Concept

If containerd/CRI fails, kubelet cannot create/manage containers even though some existing processes may continue through shims.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
systemctl status containerd --no-pager
crictl info
```

### Expected Evidence

Runtime health is confirmed independently of kubelet.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Restore CRI before interpreting Pod restart failures.

---

## Advanced Deep Dive 130 — Node Lease

### Concept

Nodes update Lease objects frequently for lightweight heartbeats. Lease failure can precede/drive Node NotReady status.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-node-lease get lease <NODE> -o yaml
```

### Expected Evidence

RenewTime shows recent node heartbeat activity.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Check API reachability and kubelet when lease updates stop.

---

## Advanced Deep Dive 131 — Node NotReady Tree

### Concept

Node NotReady can result from kubelet, runtime, CNI, API network, certificates, time, disk/memory/PID pressure, or host failure.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe node <NODE>
journalctl -u kubelet -b --no-pager | tail -100
crictl info
```

### Expected Evidence

Conditions/events and host evidence identify the failing subsystem.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Troubleshoot the node as a layered system.

---

## Advanced Deep Dive 132 — ImagePullBackOff Tree

### Concept

Cluster-wide image pulls can fail because registry DNS/TLS/auth/proxy/rate limits or node runtime config is broken.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
crictl pull <IMAGE>
```

### Expected Evidence

Direct CRI pull confirms whether the issue is runtime/registry rather than controller logic.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test from the affected node.

---

## Advanced Deep Dive 133 — CrashLoopBackOff Tree

### Concept

CrashLoopBackOff is application/runtime restart backoff. Use previous logs, exit reason, probe failure, OOM, and config evidence.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl logs <POD> -c <CONTAINER> --previous
kubectl describe pod <POD>
```

### Expected Evidence

The last terminated state is available before manual restart/delete.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Capture evidence before replacing the Pod.

---

## Advanced Deep Dive 134 — CreateContainerConfigError

### Concept

This state often points to missing ConfigMaps/Secrets, invalid key refs, ServiceAccount/imagePullSecret, or generated runtime configuration.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Evidence

The exact missing or invalid configuration object is named.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Fix the referenced object rather than changing the image.

---

## Advanced Deep Dive 135 — FailedMount Tree

### Concept

Mount errors can come from CSI node plugin, filesystem, secret, network storage, mount options, node kernel, or permissions.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
kubectl get volumeattachments
```

### Expected Evidence

The error can be placed at attach versus mount versus filesystem layer.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Follow PVC → PV → VolumeAttachment → CSI controller/node path.

---

## Advanced Deep Dive 136 — Service No Endpoints Tree

### Concept

A Service with no ready endpoints is usually selector/label/readiness/namespace rather than kube-proxy.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get svc <SVC> -o yaml
kubectl get endpointslices -l kubernetes.io/service-name=<SVC> -o wide
kubectl get pods --show-labels
```

### Expected Evidence

Selection and readiness are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not restart kube-proxy before proving endpoints exist.

---

## Advanced Deep Dive 137 — Cross-Node Network Failure

### Concept

If Pod communication works on the same node but fails cross-node, focus on CNI routing/tunnel/BGP, cloud firewall, node addresses, MTU, and CNI agents.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ip route
ip link
kubectl -n kube-system get pods -o wide
```

### Expected Evidence

Node-to-node data-plane state can be correlated with Pod placement.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Pin test Pods to different nodes and trace the packet path.

---

## Advanced Deep Dive 138 — All Pods on One Node Lose Network

### Concept

A node-local CNI agent, kube-proxy/eBPF agent, host firewall, routes, or runtime namespace issue can isolate only one node.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-system get pods -o wide --field-selector spec.nodeName=<NODE>
ip route
```

### Expected Evidence

Node-local network agents can be compared with healthy nodes.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Compare bad node state against a known-good node.

---

## Advanced Deep Dive 139 — DNS Local vs External Failure

### Concept

If `kubernetes.default` resolves but Internet names fail, CoreDNS upstream forwarding is suspect. If both fail, inspect kube-dns Service/endpoints/network policy first.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl run dns-test --rm -it --image=busybox --   sh -c 'nslookup kubernetes.default; nslookup example.com'
```

### Expected Evidence

Cluster-local and upstream resolution are tested separately.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Split DNS troubleshooting into internal and external branches.

---

## Advanced Deep Dive 140 — Webhook Outage Tree

### Concept

Webhook failures commonly present as API InternalError/timeouts or x509 errors.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get validatingwebhookconfiguration,mutatingwebhookconfiguration
kubectl get svc,endpointslices -A | grep -i webhook
```

### Expected Evidence

Webhook service reachability and configuration are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use a documented emergency policy only when a failing webhook blocks critical recovery.

---

## Advanced Deep Dive 141 — High API Error Rate

### Concept

API failures can be caused by etcd latency, exhausted CPU/memory, webhook latency, APF saturation, certificate/network issues, or pathological clients.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
API metric
  ↓ verb/resource/user-agent
  ↓ latency/error class
  ↓ etcd/webhook/control-plane dependency
```

### Expected Evidence

The request class causing load is identified.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Throttle/fix the noisy client rather than only scaling the control plane.

---

## Advanced Deep Dive 142 — Cluster SLOs

### Concept

Platform reliability should be expressed through measurable outcomes such as API availability, scheduling latency, DNS success, node readiness, and workload disruption.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
API availability ≥ 99.95%
p99 Pod scheduling < target
DNS success ≥ target
Ready nodes ≥ target
```

### Expected Evidence

Platform health is connected to user/team experience.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Define SLOs before deciding alert thresholds.

---

## Advanced Deep Dive 143 — Prometheus Platform Metrics

### Concept

A Kubernetes monitoring stack commonly combines Prometheus-compatible collection with kube-state-metrics, node metrics, component metrics, Alertmanager, and dashboards.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
components/node/app
  ↓ metrics
Prometheus/managed backend
  ↓ alerts + dashboards
```

### Expected Evidence

Control-plane, node, object, and application metrics are separated.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not use metrics-server as long-term monitoring.

---

## Advanced Deep Dive 144 — kube-state-metrics

### Concept

kube-state-metrics exports Kubernetes object state such as replica availability, Pod phase, PVC status, and node conditions; it does not measure process CPU itself.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Deployment desired/available
Pod phase
PVC status
Node condition
```

### Expected Evidence

Object-state metrics complement node/runtime metrics.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use object metrics for controller/SLO alerts.

---

## Advanced Deep Dive 145 — Platform Alert Quality

### Concept

Alerts should map to user/platform impact and a runbook, not simply fire for every transient event.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
alert:
condition
duration
severity
owner
runbook
user impact
```

### Expected Evidence

Each page has an actionable first response.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Page on sustained actionable conditions; dashboard noisy diagnostics.

---

## Advanced Deep Dive 146 — Certificate Alerting

### Concept

Certificate expiry is predictable and should be monitored as a time-to-failure signal.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
days_remaining
  ↓ warn threshold
  ↓ critical threshold
renew/runbook
```

### Expected Evidence

Expiry is handled before service interruption.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Monitor API, kubelet, webhook, ingress, and external certs.

---

## Advanced Deep Dive 147 — API Audit + Workload Logs Correlation

### Concept

Incident reconstruction often requires correlating API changes/exec sessions with workload and node events.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
audit: user verb resource timestamp
events: rollout/restart
logs: app failure
node: runtime/kernel
```

### Expected Evidence

One incident timeline can connect control-plane actions to data-plane effects.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Synchronize time and centralize logs.

---

## Advanced Deep Dive 148 — Backup Scope Classification

### Concept

Cluster recovery may require etcd, kubeadm/PKI, Git/IaC, CRDs, admission/controller configuration, registry images, and application/PV data.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
control-plane state → etcd
cluster construction → IaC/kubeadm
workload desired state → Git
persistent business data → app backups
artifacts → registry
```

### Expected Evidence

Each asset has a backup owner and recovery path.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not call an etcd snapshot a complete business backup.

---

## Advanced Deep Dive 149 — Rebuild vs Restore DR

### Concept

A mature platform can restore the old cluster state or build a clean replacement cluster from IaC/Git and restore application data.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Path A: etcd restore
Path B: new cluster → Git reconcile → data restore
```

### Expected Evidence

Both recovery strategies have documented RPO/RTO trade-offs.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test the recovery path you expect to use under pressure.

---

## Advanced Deep Dive 150 — Cluster RPO

### Concept

Control-plane RPO is determined by etcd snapshot frequency and desired-state sources; application RPO is determined separately by database/storage backup/log replication.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
cluster RPO ≠ application data RPO
```

### Expected Evidence

Different state domains receive separate RPO targets.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not infer application recoverability from etcd backup.

---

## Advanced Deep Dive 151 — Cluster RTO Decomposition

### Concept

RTO includes detection, decision, infrastructure, control plane, add-ons, identity, network, storage, workload reconciliation, data restore, and smoke validation.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```python
steps = {"detect":5,"infra":20,"control_plane":15,"addons":15,"data":30,"validate":10}
print("RTO minutes:", sum(steps.values()))
```

### Expected Evidence

Recovery time is broken into measurable components.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Measure RTO through full game days.

---

## Advanced Deep Dive 152 — Restore Test Evidence

### Concept

A DR test should prove API, DNS, CNI, CSI, ingress, identity, workloads, and business transactions—not merely that etcd started.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
restore complete?
  ↓ API
  ↓ system Pods
  ↓ DNS/network
  ↓ storage
  ↓ app
  ↓ business transaction
```

### Expected Evidence

The recovered platform supports end-to-end workload use.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Define a smoke-test checklist for every restore drill.

---

## Advanced Deep Dive 153 — Control Plane Failure-Domain Spread

### Concept

Three control-plane VMs on one hypervisor/rack/zone are not three independent failure domains.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
bad:
rack A: cp1 cp2 cp3

better:
rack/zone A: cp1
rack/zone B: cp2
rack/zone C: cp3
```

### Expected Evidence

Member placement is documented against physical/cloud failure domains.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Design HA against correlated infrastructure failures.

---

## Advanced Deep Dive 154 — Maintenance Capacity

### Concept

Drain and upgrades require spare capacity. A cluster at 100% requested capacity cannot safely evacuate a node.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```python
nodes = 4
usable_per_node = 8
normal_requested = 28
after_one_node_loss = (nodes-1)*usable_per_node
print("Capacity after one node loss:", after_one_node_loss, "requested:", normal_requested)
```

### Expected Evidence

The cluster's N-1 scheduling headroom is explicit.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Capacity-plan for the largest maintenance/failure scenario.

---

## Advanced Deep Dive 155 — Sequential Minor Upgrade

### Concept

kubeadm upgrades should follow supported sequential minor transitions with add-on and API compatibility checks.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
current minor
  ↓ release/API/add-on review
etcd snapshot
  ↓ first control plane
other control planes
  ↓ workers in waves
verify
```

### Expected Evidence

Every stage has a known target and verification gate.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Never skip unsupported minors or assume downgrade is easy.

---

## Advanced Deep Dive 156 — Version Skew Matrix

### Concept

API server, kubelet, kube-proxy, kubectl, scheduler/controller, and kubeadm have different supported skew rules.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
component → allowed relation to API server
API server
kubelet
kube-proxy
kubectl
kubeadm
```

### Expected Evidence

Upgrade sequencing follows upstream skew policy rather than intuition.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Maintain a version matrix for cluster and add-ons.

---

## Advanced Deep Dive 157 — API Deprecation Scan

### Concept

An upgrade can fail workloads/controllers when removed APIs remain in manifests or CRDs.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl api-resources
kubectl get --raw /metrics 2>/dev/null | grep apiserver_requested_deprecated_apis | head
```

### Expected Evidence

Deprecated API usage can be identified before upgrade where metrics are available.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat deprecation cleanup as an upgrade prerequisite.

---

## Advanced Deep Dive 158 — CNI Compatibility Gate

### Concept

CNI upgrades and Kubernetes upgrades have two-way compatibility requirements, kernel requirements, CRDs, and migration considerations.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Kubernetes target
  ↕ compatible
CNI version
  ↕
kernel / kube-proxy mode / CRDs
```

### Expected Evidence

The compatibility matrix is documented before change.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Never upgrade Kubernetes without validating CNI support.

---

## Advanced Deep Dive 159 — CSI Compatibility Gate

### Concept

Storage drivers may depend on Kubernetes CSI API behavior, external sidecar versions, snapshot CRDs, cloud APIs, and node kernels.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get csidrivers
kubectl get pods -A | grep -i csi
```

### Expected Evidence

Driver/sidecar inventory is recorded before upgrade.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test attach/mount/resize/snapshot after CSI upgrades.

---

## Advanced Deep Dive 160 — CoreDNS Upgrade Gate

### Concept

Custom Corefile plugins/options can become incompatible during CoreDNS/Kubernetes upgrades.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl -n kube-system get cm coredns -o yaml
```

### Expected Evidence

Custom DNS configuration is inventoried.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test internal/external DNS after every CoreDNS change.

---

## Advanced Deep Dive 161 — Admission Controller Upgrade Gate

### Concept

Webhooks and policy engines can depend on API versions and certificates. A Kubernetes upgrade may expose hidden webhook incompatibility.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get validatingwebhookconfigurations,mutatingwebhookconfigurations
```

### Expected Evidence

Webhook inventory is included in the upgrade plan.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Canary control-plane/API changes in nonproduction first.

---

## Advanced Deep Dive 162 — Worker Upgrade Wave

### Concept

Workers should be cordoned/drained, upgraded, verified, and uncordoned in controlled waves so one bad node image/runtime change does not affect the entire fleet.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
wave 1: one canary worker
  ↓ soak
wave 2: small percentage
  ↓
remaining workers
```

### Expected Evidence

A bad node change is contained to a small set.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use progressive node waves with workload smoke tests.

---

## Advanced Deep Dive 163 — Node Replacement over Repair

### Concept

Immutable or reproducible nodes reduce configuration drift. Rebuild/join often provides a safer known state than years of manual patching.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
cordon
drain
delete/reimage
bootstrap
join
verify
uncordon
```

### Expected Evidence

Replacement produces a node matching the current baseline.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Prefer replaceable nodes and automate bootstrap.

---

## Advanced Deep Dive 164 — Control Plane Node Replacement

### Concept

Replacing a stacked control-plane node affects API LB membership, etcd membership/quorum, certificates, and kubeadm state.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
verify quorum
remove bad LB backend
remove/replace etcd member safely
join new control plane
verify quorum/API
restore LB backend
```

### Expected Evidence

Quorum remains healthy throughout replacement.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Never remove multiple stacked control planes simultaneously without quorum math.

---

## Advanced Deep Dive 165 — Etcd Member Removal

### Concept

Removing a member changes quorum membership and should be done only when the cluster still has a healthy majority.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
etcdctl member list -w table
```

### Expected Evidence

Member IDs and state are known before removal.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Take a snapshot and verify quorum before membership changes.

---

## Advanced Deep Dive 166 — GitOps Add-on Management

### Concept

CNI, CSI, ingress, metrics, policy, and observability add-ons can be versioned/reconciled through GitOps, but bootstrap dependencies require careful ordering.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
cluster bootstrap
  ↓ minimal CNI/DNS
GitOps controller
  ↓ reconciles add-ons
```

### Expected Evidence

Add-on versions and configuration are auditable in Git.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Avoid two controllers/tools owning the same add-on fields.

---

## Advanced Deep Dive 167 — Fleet Upgrade Waves

### Concept

Multiple clusters should move through lab/dev/staging/canary-production/production waves with soak time and rollback criteria.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
lab → dev → staging → prod-canary → prod-fleet
```

### Expected Evidence

A regression is caught before all clusters are changed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat cluster upgrades like application releases.

---

## Advanced Deep Dive 168 — Cluster Inventory

### Concept

Administrators need a fleet inventory of Kubernetes version, node OS/kernel, runtime, CNI, CSI, ingress, Gateway CRDs, policy engine, certificate dates, and backup status.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
cluster
version
runtime
CNI
CSI
ingress
cert expiry
last etcd backup
last restore test
```

### Expected Evidence

Fleet risk can be queried rather than discovered during incidents.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Automate inventory collection.

---

## Advanced Deep Dive 169 — Supply-Chain Policy

### Concept

Cluster admission can require approved registries, immutable digests, signatures/provenance, and security context before workload execution.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
image reference
  ↓ registry allow-list
  ↓ digest/signature/provenance
  ↓ policy
allow / reject
```

### Expected Evidence

Untrusted artifacts are blocked before runtime.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Combine supply-chain policy with runtime least privilege.

---

## Advanced Deep Dive 170 — Node Image Provenance

### Concept

Node OS images are also supply-chain artifacts. Kernel/runtime/CNI security depends on trusted image builds and patch provenance.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
node image source
  ↓ hardened build
scan/sign
  ↓ node pool
```

### Expected Evidence

Node versions can be traced to an approved image build.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Treat node images as immutable release artifacts.

---

## Advanced Deep Dive 171 — Runtime Socket Protection

### Concept

CRI/containerd sockets and host root access can control containers and often the node. They should be limited to root/trusted system services.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
ls -l /run/containerd/containerd.sock 2>/dev/null || true
```

### Expected Evidence

Socket ownership/mode is visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Do not mount host runtime sockets into ordinary workloads.

---

## Advanced Deep Dive 172 — HostPath/Privileged Inventory

### Concept

Infrastructure Pods may legitimately use hostPath, hostPID, hostNetwork, or privileged mode. These exceptions should be inventoried and isolated.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pods -A -o json | jq -r '
.items[] | select(
  .spec.hostNetwork==true or .spec.hostPID==true or
  ([.spec.containers[]?.securityContext.privileged] | any(.==true))
) | [.metadata.namespace,.metadata.name] | @tsv' 2>/dev/null
```

### Expected Evidence

High-privilege Pods can be enumerated.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Keep exceptions in protected namespaces with dedicated identities and operators.

---

## Advanced Deep Dive 173 — Cloud Metadata Protection

### Concept

Pods should not inherit node cloud credentials through metadata endpoints. Managed workload identity is safer than node-wide credentials.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Pod
  ✕ node metadata broad credential
  ✓ workload identity scoped credential
```

### Expected Evidence

Application identity is decoupled from node identity.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use cloud workload identity and metadata restrictions.

---

## Advanced Deep Dive 174 — Security Incident Containment

### Concept

Containment should preserve evidence while limiting network/API credentials and preventing further scheduling or data access.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
detect compromised Pod
  ↓ capture logs/imageID/audit
  ↓ isolate network
revoke/rotate credentials
  ↓ replace artifact
  ↓ inspect node/runtime scope
```

### Expected Evidence

Containment actions reduce blast radius without immediately destroying forensic state.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Prepare a Kubernetes-specific incident runbook.

---

## Advanced Deep Dive 175 — Namespace Escape Threat Model

### Concept

Namespaces are organizational API scopes, not kernel isolation. A privileged Pod in one namespace can still compromise a shared node/cluster.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
namespace boundary
 ≠
kernel/VM boundary
```

### Expected Evidence

Tenancy design accounts for node/runtime trust.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use dedicated clusters/nodes/sandboxed runtimes for hostile multi-tenancy when required.

---

## Advanced Deep Dive 176 — Sandboxed RuntimeClass

### Concept

RuntimeClass can select alternative runtimes such as sandboxed container implementations for workloads requiring stronger isolation.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get runtimeclasses
```

### Expected Evidence

Available runtime handlers are visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use stronger isolation for untrusted workloads and account for performance/compatibility overhead.

---

## Advanced Deep Dive 177 — RuntimeClass Scheduling Overhead

### Concept

Sandboxed runtimes can require additional CPU/memory and specific node labels. RuntimeClass overhead can be accounted for by scheduling.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Pod resources
+ RuntimeClass overhead
= scheduler accounting
```

### Expected Evidence

The platform includes sandbox overhead in capacity planning.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Measure overhead before broad adoption.

---

## Advanced Deep Dive 178 — Cluster DNS SLO

### Concept

DNS is a critical shared service; monitor query success, latency, saturation, CoreDNS replicas, and upstream failures.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
DNS SLI:
successful queries / total
p95 latency
SERVFAIL rate
```

### Expected Evidence

DNS problems are detected before applications report widespread timeouts.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Give CoreDNS explicit resources, spread, and PDB where appropriate.

---

## Advanced Deep Dive 179 — Service Data Plane SLO

### Concept

Service routing should be measured through synthetic in-cluster probes and endpoint health, not inferred from kube-proxy Pod Running state.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
synthetic Pod
  ↓ Service DNS/VIP
test endpoint
  ↓ latency/success
```

### Expected Evidence

The actual data path is continuously validated.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use synthetic checks for critical shared network paths.

---

## Advanced Deep Dive 180 — Storage SLO

### Concept

Storage platform health includes provision latency, attach/mount success, I/O latency, capacity, and recovery—not only CSI Pod readiness.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
PVC provision time
attach latency
mount error rate
backend capacity
restore success
```

### Expected Evidence

Storage alerts reflect workload impact.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Measure storage lifecycle operations and data-path health.

---

## Advanced Deep Dive 181 — Platform Capacity Forecasting

### Concept

Capacity planning includes requests, daemon overhead, PDB/drain headroom, failover zones, image/storage growth, IPs, NAT/conntrack, and control-plane scale.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
CPU/memory
Pod IPs
Service IPs
PVC/backend quota
node disk/inodes
conntrack/NAT
control-plane QPS
```

### Expected Evidence

Cluster growth limits are known before they become incidents.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Forecast every finite resource, not just CPU and memory.

---

## Advanced Deep Dive 182 — Pod IP Exhaustion

### Concept

CNI IP pools or cloud subnet secondary ranges can exhaust even when nodes have CPU/memory capacity.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get pods -A -o wide | wc -l
kubectl get nodes -o wide
```

### Expected Evidence

Pod count can be compared with CNI/IPAM capacity.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Monitor address pools as a first-class capacity metric.

---

## Advanced Deep Dive 183 — Service IP Exhaustion

### Concept

Service CIDR is finite. Very large clusters/automation can exhaust virtual Service addresses.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get svc -A | wc -l
```

### Expected Evidence

Service count can be compared with CIDR capacity.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Avoid unnecessary short-lived Services and size the CIDR for fleet needs.

---

## Advanced Deep Dive 184 — Control Plane Resource Reservation

### Concept

Control-plane static Pods, etcd, kubelet, runtime, logs, and OS need guaranteed capacity; undersized control-plane nodes fail under API/controller bursts.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl top nodes 2>/dev/null || true
kubectl -n kube-system top pods 2>/dev/null || true
```

### Expected Evidence

Control-plane resource consumption can be observed when metrics are installed.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Size control planes for failure state and maintenance, not average usage.

---

## Advanced Deep Dive 185 — Admission Latency Budget

### Concept

Every mutating/validating webhook adds latency and another network/TLS dependency to API writes.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
API request
  + webhook A
  + webhook B
  + webhook C
= cumulative latency/failure risk
```

### Expected Evidence

Webhook count and timeouts are considered in API SLO.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Minimize webhook scope/count and monitor webhook latency.

---

## Advanced Deep Dive 186 — Controller Storm

### Concept

A bad controller can create rapid object churn/retries, overwhelming the API and etcd.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
event
  ↓ reconcile error
requeue too fast
  ↓ API write storm
```

### Expected Evidence

Noisy controller user-agent/requests can be identified from logs/metrics.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use exponential backoff and rate limiting in custom controllers.

---

## Advanced Deep Dive 187 — Large Secret/ConfigMap Misuse

### Concept

Kubernetes API/etcd is not a bulk object store. Huge config blobs increase API/etcd load and watch traffic.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
small config/metadata → API
large artifacts/data → object store/registry/database
```

### Expected Evidence

Application artifacts are kept out of etcd.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use the API for desired-state metadata, not large file distribution.

---

## Advanced Deep Dive 188 — API Object Churn

### Concept

Rapid creation/deletion of Jobs, Pods, Events, and CRs increases etcd revisions and controller load.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get jobs -A | wc -l
kubectl get events -A | wc -l
```

### Expected Evidence

High-churn object classes can be identified.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Use TTL/history limits and efficient controllers for transient workloads.

---

## Advanced Deep Dive 189 — CronJob History Retention

### Concept

CronJobs can accumulate Jobs/Pods unless success/failure history limits or TTL cleanup are configured.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
kubectl get cronjob -A
kubectl get jobs -A
```

### Expected Evidence

Historical object growth is visible.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Configure retention appropriate to audit/debug needs.

---

## Advanced Deep Dive 190 — Node Drain + Local Data

### Concept

emptyDir/local PV/static Pods/hostPath workloads can make drain destructive or incomplete.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
before drain:
emptyDir?
local PV?
unmanaged Pod?
DaemonSet?
PDB?
```

### Expected Evidence

Data-loss or immovable workloads are identified before eviction.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Make local-state dependencies explicit.

---

## Advanced Deep Dive 191 — Graceful Node Shutdown

### Concept

Kubelet can participate in graceful node shutdown on supported systems, allowing Pods to terminate before OS poweroff/reboot.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```bash
grep -n "shutdownGracePeriod" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Evidence

Node shutdown grace configuration can be inspected.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Coordinate OS maintenance with kubelet graceful shutdown behavior.

---

## Advanced Deep Dive 192 — Non-Graceful Node Shutdown Recovery

### Concept

Unexpected power loss can leave volume attachments, leases, and Pods requiring recovery decisions. Stateful workloads may need fencing.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
node lost
  ↓ control plane detects
replacement Pod
  ↓ storage attach/fencing
  ↓
resume service
```

### Expected Evidence

Recovery sequence accounts for old-node write safety.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Design fencing and storage behavior for hard node failure.

---

## Advanced Deep Dive 193 — Platform Runbook Structure

### Concept

A useful runbook states symptoms, scope, safety constraints, evidence commands, decision points, recovery, verification, and escalation.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
Trigger
Impact
Safety warning
Evidence
Decision tree
Recovery
Verification
Escalation
Prevention
```

### Expected Evidence

Runbooks are executable under incident pressure.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Test runbooks during game days.

---

## Advanced Deep Dive 194 — Game Day Design

### Concept

A game day intentionally tests one or more failure modes with stop conditions, observers, recovery criteria, and postmortem actions.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
hypothesis
failure injection
expected detection
recovery target
stop conditions
actual result
actions
```

### Expected Evidence

The exercise measures real detection/RTO and exposes undocumented dependencies.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Practice failures before production chooses the timing.

---

## Advanced Deep Dive 195 — Change Evidence Chain

### Concept

A high-risk cluster change should connect Git/IaC, ticket/approval, command/deployment, audit logs, node/runtime changes, monitoring, and verification.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
commit
  ↓ change record
apply/upgrade
  ↓ audit/logs
metrics
  ↓ verification
```

### Expected Evidence

An incident can identify exactly what changed and by whom.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Preserve change evidence for control-plane/add-on upgrades.

---

## Advanced Deep Dive 196 — Operational Readiness Review

### Concept

A production cluster needs HA, IPAM, CNI, DNS, CSI, ingress/Gateway, identity, RBAC, PSA/policy, encryption, audit, observability, backups, restore tests, upgrade process, capacity, and runbooks.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
[ ] HA/API endpoint
[ ] etcd backup + restore
[ ] CNI/DNS
[ ] CSI/storage recovery
[ ] identity/RBAC
[ ] Pod security/policy
[ ] encryption/audit
[ ] monitoring/SLO
[ ] upgrade matrix
[ ] capacity N-1
[ ] runbooks/game day
```

### Expected Evidence

The platform can survive routine operations and defined failures before tenant onboarding.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Make operational readiness a cluster launch gate.

---

## Advanced Deep Dive 197 — Evidence-First Administration

### Concept

Strong administration follows a stable method: classify plane/layer, capture state, form one hypothesis, make the smallest reversible change, verify, and document prevention.

### Architecture / Mental Model

```text
Client / Automation
        ↓
kube-apiserver
        ↓
authn → authz → admission
        ↓
       etcd
        ↓
controllers / scheduler
        ↓
kubelet / CRI
        ↓
CNI + Service + CSI
        ↓
workloads / persistent data
```

### Command / Configuration / Code

```text
symptom
  ↓ classify layer
capture evidence
  ↓ hypothesis
small change
  ↓ verify
root cause + prevention
```

### Expected Evidence

Incidents are resolved without random restarts or destructive guesswork.

### Why It Works

Kubernetes administration spans both API state and node-local state. The API/control plane stores and reconciles desired state, while kubelet, container runtime, Linux networking, CNI, CSI, DNS, certificates, and storage create the real execution environment. Correct diagnosis requires identifying which layer owns the failed operation and collecting evidence at that layer.

### Production Example

For a production cluster, document the component owner, failure domain, version, configuration source, credentials/PKI, network/storage dependency, metrics/logs, backup or rollback method, maintenance requirements, and user impact for this topic.

### Troubleshooting Workflow

```text
Classify control plane vs data plane
   ↓
Capture current versions / context / scope
   ↓
Inspect API status + events if available
   ↓
Inspect node/systemd/CRI if needed
   ↓
Inspect CNI/DNS/Service/CSI path
   ↓
Inspect PKI/RBAC/admission
   ↓
Inspect resource/capacity pressure
   ↓
Make smallest reversible correction
   ↓
Run platform + workload smoke tests
   ↓
Document prevention
```

### Common Mistakes

- Restarting components before collecting evidence.
- Treating etcd snapshot as complete application backup.
- Removing etcd members without quorum calculation.
- Granting cluster-admin to solve a narrow RBAC problem.
- Disabling TLS, Pod security, seccomp, or NetworkPolicy instead of finding the real dependency.
- Upgrading Kubernetes without CNI/CSI/API compatibility review.
- Draining nodes without PDB, state, and capacity checks.

### Best Practice

Preserve evidence and change one variable at a time.

---

# Supplemental Administration Lab Series — Kubernetes Administration

## Enhanced Administration Lab 1 — Control Plane vs Data Plane Failure

### Objective

Turn **Control Plane vs Data Plane Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Control plane:
API + etcd + scheduler + controllers

Data plane:
nodes + runtime + CNI + Service data plane + storage + workloads
```

### Expected Result

The incident is classified by which plane is failing and which functions continue.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not summarize every outage as 'Kubernetes is down'.

---

## Enhanced Administration Lab 2 — API Server Request Pipeline

### Objective

Turn **API Server Request Pipeline** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
client
 ↓ TLS
authentication
 ↓ authorization
mutating admission
 ↓ validation/defaulting
validating admission
 ↓ etcd
 ↓ watch events
```

### Expected Result

A failure can be placed at a specific request-processing stage.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use the exact API error to identify the failing stage before changing policy or credentials.

---

## Enhanced Administration Lab 3 — API Server Readiness

### Objective

Turn **API Server Readiness** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get --raw='/readyz?verbose'
kubectl get --raw='/livez?verbose'
```

### Expected Result

Individual health checks report success/failure when the API is reachable.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use readiness for load-balancer backend health, not only TCP port checks.

---

## Enhanced Administration Lab 4 — API Server Latency Decomposition

### Objective

Turn **API Server Latency Decomposition** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get --raw='/metrics' 2>/dev/null | grep -E 'apiserver_request_duration|apiserver_flowcontrol' | head
```

### Expected Result

Metrics expose API request and flow-control behavior where authorized.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Investigate request class and dependency latency before scaling the API blindly.

---

## Enhanced Administration Lab 5 — API Priority and Fairness

### Objective

Turn **API Priority and Fairness** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get flowschemas
kubectl get prioritylevelconfigurations
```

### Expected Result

Configured flow schemas and priority levels are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Keep system-critical API flows protected and monitor rejected/queued requests.

---

## Enhanced Administration Lab 6 — Watch and Informer Failure Modes

### Objective

Turn **Watch and Informer Failure Modes** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
LIST initial state
  ↓ WATCH changes
local informer cache
  ↓ workqueue
reconcile
```

### Expected Result

Controller logs/metrics can distinguish watch reconnects from reconciliation errors.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat repeated watch relists as API/network pressure evidence.

---

## Enhanced Administration Lab 7 — Admission Webhook Blast Radius

### Objective

Turn **Admission Webhook Blast Radius** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get mutatingwebhookconfigurations,validatingwebhookconfigurations
```

### Expected Result

Webhook scope, service references, timeout, and failurePolicy are inspectable.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Make high-impact webhooks highly available, narrowly scoped, and explicitly tested for outage behavior.

---

## Enhanced Administration Lab 8 — ValidatingAdmissionPolicy

### Objective

Turn **ValidatingAdmissionPolicy** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl api-resources | grep -i validatingadmission
```

### Expected Result

The cluster exposes the relevant policy APIs when supported.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Prefer built-in validation for simple deterministic policies where appropriate.

---

## Enhanced Administration Lab 9 — CRD Stored Versions

### Objective

Turn **CRD Stored Versions** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get crd <CRD> -o jsonpath='{.status.storedVersions}{"\n"}'
```

### Expected Result

The persisted API versions are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Migrate stored versions before removing an old served version.

---

## Enhanced Administration Lab 10 — CRD Conversion Webhook Risk

### Objective

Turn **CRD Conversion Webhook Risk** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get crd <CRD> -o yaml | sed -n '/conversion:/,/preserveUnknownFields:/p'
```

### Expected Result

Conversion strategy and webhook client configuration are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat conversion webhooks as control-plane dependencies.

---

## Enhanced Administration Lab 11 — Finalizer Deadlock

### Objective

Turn **Finalizer Deadlock** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get <RESOURCE> <NAME> -o jsonpath='{.metadata.deletionTimestamp}{" "}{.metadata.finalizers}{"\n"}'
```

### Expected Result

Deletion timestamp plus finalizer list explains why garbage collection is blocked.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Restore cleanup logic before manually removing finalizers.

---

## Enhanced Administration Lab 12 — etcd Quorum Mathematics

### Objective

Turn **etcd Quorum Mathematics** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```python
for n in [1,3,5,7]:
    print(n, "members -> quorum", n//2 + 1, "tolerates", n - (n//2 + 1), "failures")
```

### Expected Result

Quorum and tolerated member failures are explicit.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Prefer 3 or 5 well-separated members rather than many correlated members.

---

## Enhanced Administration Lab 13 — etcd Member Failure vs Quorum Loss

### Objective

Turn **etcd Member Failure vs Quorum Loss** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
3 members:
1 down → quorum 2 remains
2 down → quorum lost
```

### Expected Result

The incident severity is based on remaining quorum, not simply member count.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Never remove/rebuild members without first calculating quorum.

---

## Enhanced Administration Lab 14 — etcd Leader Election

### Objective

Turn **etcd Leader Election** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
etcdctl endpoint status --cluster -w table
```

### Expected Result

The current leader and member status are visible with proper certificates.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not restore from backup merely because the leader changed.

---

## Enhanced Administration Lab 15 — etcd Disk Latency

### Objective

Turn **etcd Disk Latency** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
iostat -xz 1 5 2>/dev/null || true
```

### Expected Result

Storage latency/utilization can be correlated with etcd/API symptoms.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Place etcd on low-latency durable storage and monitor fsync latency.

---

## Enhanced Administration Lab 16 — etcd Space Quota / Alarm

### Objective

Turn **etcd Space Quota / Alarm** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
etcdctl alarm list
etcdctl endpoint status --cluster -w table
```

### Expected Result

Active alarms and DB sizes are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Monitor etcd DB growth and perform supported compaction/defragmentation procedures.

---

## Enhanced Administration Lab 17 — etcd Compaction

### Objective

Turn **etcd Compaction** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
revision history grows
  ↓ compaction
old revisions logically removed
  ↓ defragment
backend file can shrink
```

### Expected Result

Compaction and disk reclamation are treated as separate operations.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Follow current etcd maintenance guidance and avoid ad hoc direct file manipulation.

---

## Enhanced Administration Lab 18 — etcd Defragmentation

### Objective

Turn **etcd Defragmentation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
etcdctl defrag --endpoints=https://127.0.0.1:2379
```

### Expected Result

Backend size decreases where free pages existed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Defragment one healthy member at a time and preserve quorum.

---

## Enhanced Administration Lab 19 — etcd Snapshot Integrity

### Objective

Turn **etcd Snapshot Integrity** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
sha256sum snapshot.db
etcdutl snapshot status snapshot.db -w table 2>/dev/null || true
```

### Expected Result

Snapshot hash and metadata are recorded.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Store encrypted snapshots outside the failure domain and test restore.

---

## Enhanced Administration Lab 20 — etcd Snapshot Security

### Objective

Turn **etcd Snapshot Security** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
snapshot
  contains:
  API objects
  Secrets
  RBAC
  CRDs
  service-account data
```

### Expected Result

Backup handling is classified at the same sensitivity as cluster credentials.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Encrypt and tightly restrict snapshot storage.

---

## Enhanced Administration Lab 21 — etcd Restore Isolation

### Objective

Turn **etcd Restore Isolation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
snapshot
  ↓ isolated control plane
restore
  ↓ API verification
  ↓ workload/add-on smoke tests
```

### Expected Result

The restored state is validated without creating split-brain infrastructure.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Never test control-plane restore against the same live endpoints/resources unintentionally.

---

## Enhanced Administration Lab 22 — Stacked vs External etcd

### Objective

Turn **Stacked vs External etcd** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
stacked:
cp1 API+etcd
cp2 API+etcd
cp3 API+etcd

external:
cp1/cp2/cp3 → etcd1/etcd2/etcd3
```

### Expected Result

The topology choice is linked to failure-domain and operational requirements.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Document the topology in an ADR and test member replacement.

---

## Enhanced Administration Lab 23 — API Load Balancer

### Objective

Turn **API Load Balancer** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
curl -k https://<CONTROL_PLANE_ENDPOINT>:6443/readyz 2>/dev/null || true
```

### Expected Result

The load-balanced endpoint returns API readiness when authenticated/allowed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Make the load balancer itself highly available and health-check API readiness.

---

## Enhanced Administration Lab 24 — API Certificate SAN

### Objective

Turn **API Certificate SAN** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
openssl s_client -connect <API_HOST>:6443 -servername <API_HOST> </dev/null 2>/dev/null  | openssl x509 -noout -subject -issuer -dates -ext subjectAltName 2>/dev/null
```

### Expected Result

Certificate validity and SANs can be compared with the client endpoint.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Fix certificate identity rather than using insecure TLS bypasses.

---

## Enhanced Administration Lab 25 — PKI Inventory

### Objective

Turn **PKI Inventory** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
find /etc/kubernetes/pki -maxdepth 2 -type f -printf '%p\n' 2>/dev/null | sort
```

### Expected Result

The local PKI inventory can be mapped to component purpose and sensitivity.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Maintain a documented PKI map and protected backup strategy.

---

## Enhanced Administration Lab 26 — CA Private-Key Custody

### Objective

Turn **CA Private-Key Custody** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
CA private key
  ↓ sign client cert
arbitrary CN/O identity
  ↓ API authentication
```

### Expected Result

The trust consequence of CA compromise is explicit.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Restrict CA keys and use centralized/OIDC identity for humans where possible.

---

## Enhanced Administration Lab 27 — ServiceAccount Signing Keys

### Objective

Turn **ServiceAccount Signing Keys** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ls -l /etc/kubernetes/pki/sa.* 2>/dev/null || true
```

### Expected Result

Service-account signing material is inventoried separately.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Protect and back up signing keys according to the recovery model.

---

## Enhanced Administration Lab 28 — Certificate Expiry Monitoring

### Objective

Turn **Certificate Expiry Monitoring** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubeadm certs check-expiration
```

### Expected Result

Expiration dates and residual lifetimes are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Alert on certificate expiry with enough lead time for controlled renewal.

---

## Enhanced Administration Lab 29 — Leaf Certificate Renewal

### Objective

Turn **Leaf Certificate Renewal** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubeadm certs renew all
```

### Expected Result

Renewed files have updated validity and components can reconnect after reload/restart.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test renewal in a lab and document component reload behavior.

---

## Enhanced Administration Lab 30 — CA Rotation Complexity

### Objective

Turn **CA Rotation Complexity** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
old CA only
  ↓ add trust overlap
old + new trusted
  ↓ reissue leaves
new CA only
```

### Expected Result

The migration avoids an all-at-once trust break.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Plan CA rotation as a dedicated migration, not an emergency one-liner.

---

## Enhanced Administration Lab 31 — kubeconfig Credential Scope

### Objective

Turn **kubeconfig Credential Scope** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl config view --minify --raw
```

### Expected Result

The active cluster, user, and credential type are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Protect privileged kubeconfigs like root credentials.

---

## Enhanced Administration Lab 32 — OIDC Human Authentication

### Objective

Turn **OIDC Human Authentication** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
human → IdP/MFA → OIDC token
                    ↓
              kube-apiserver
                    ↓ groups
                   RBAC
```

### Expected Result

Human cluster access can be revoked/managed centrally.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Prefer short-lived centralized human identity over static admin client certificates.

---

## Enhanced Administration Lab 33 — RBAC Exact Tuple

### Objective

Turn **RBAC Exact Tuple** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl auth can-i create pods/exec --as=<USER> -n <NS>
kubectl auth can-i list secrets --as=<USER> -n <NS>
```

### Expected Result

Each exact API operation returns yes/no.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Grant the smallest tuple that satisfies the task.

---

## Enhanced Administration Lab 34 — RoleBinding to ClusterRole

### Objective

Turn **RoleBinding to ClusterRole** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get rolebinding -n <NS> -o yaml
```

### Expected Result

The binding scope and referenced role are explicit.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use reusable ClusterRoles with RoleBindings instead of duplicating rules where appropriate.

---

## Enhanced Administration Lab 35 — ClusterRoleBinding Audit

### Objective

Turn **ClusterRoleBinding Audit** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get clusterrolebindings -o wide
```

### Expected Result

Subjects with cluster-wide roles can be inventoried.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Regularly review bindings to cluster-admin and other high-privilege roles.

---

## Enhanced Administration Lab 36 — RBAC Wildcards

### Objective

Turn **RBAC Wildcards** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
verbs: ["*"]
resources: ["*"]
apiGroups: ["*"]
```

### Expected Result

The risk of forward-expanding privilege is recognized.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Avoid broad wildcards in application roles.

---

## Enhanced Administration Lab 37 — Impersonation

### Objective

Turn **Impersonation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl auth can-i get pods --as=user@example.com -n app
```

### Expected Result

The API evaluates permissions as the impersonated subject.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Grant impersonation only to trusted administrators/support tooling.

---

## Enhanced Administration Lab 38 — ServiceAccount Token Projection

### Objective

Turn **ServiceAccount Token Projection** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```yaml
projected:
  sources:
    - serviceAccountToken:
        path: token
        audience: internal-api
        expirationSeconds: 3600
```

### Expected Result

The mounted token is scoped to an intended audience and expires.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Disable default automount where Kubernetes API access is not required.

---

## Enhanced Administration Lab 39 — Node Authorizer / NodeRestriction

### Objective

Turn **Node Authorizer / NodeRestriction** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
node credential
  ↓ Node authorizer
  ↓ NodeRestriction admission
bounded node-specific operations
```

### Expected Result

Node identity cannot arbitrarily modify unrelated cluster resources when correctly configured.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Protect kubelet credentials and keep node authorization restrictions enabled.

---

## Enhanced Administration Lab 40 — Pod Security Admission Rollout

### Objective

Turn **Pod Security Admission Rollout** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl label ns app pod-security.kubernetes.io/warn=restricted --overwrite
kubectl label ns app pod-security.kubernetes.io/audit=restricted --overwrite
```

### Expected Result

Existing violations become visible before enforcement.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use staged warn/audit → remediate → enforce.

---

## Enhanced Administration Lab 41 — Restricted Pod Baseline

### Objective

Turn **Restricted Pod Baseline** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
```

### Expected Result

The workload satisfies a defensible least-privilege baseline.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Create documented exception paths for infrastructure workloads.

---

## Enhanced Administration Lab 42 — Encryption at Rest Provider Order

### Objective

Turn **Encryption at Rest Provider Order** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
providers:
1 new KMS/encryption provider
2 old provider
3 identity only during migration if required
```

### Expected Result

New writes use the new provider while old data remains readable.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Plan key/provider rotation with explicit rewrite and rollback steps.

---

## Enhanced Administration Lab 43 — Re-encryption Rewrite

### Objective

Turn **Re-encryption Rewrite** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get secrets -A -o json >/tmp/secrets.json
# Rewrites must follow a reviewed current procedure; avoid logging secret bodies.
```

### Expected Result

Storage encryption state is migrated deliberately rather than assumed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test rewrite procedures and avoid exposing Secret plaintext during migration.

---

## Enhanced Administration Lab 44 — KMS Availability Dependency

### Objective

Turn **KMS Availability Dependency** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
API server
  ↓ envelope encryption
KMS plugin/service
  ↓ KEK
etcd stores ciphertext
```

### Expected Result

KMS health is included in control-plane availability planning.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Design KMS HA, latency, monitoring, and recovery before using it.

---

## Enhanced Administration Lab 45 — Audit Policy Design

### Objective

Turn **Audit Policy Design** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```yaml
- level: Metadata
  resources:
    - group: ""
      resources: ["secrets"]
- level: Metadata
  verbs: ["create","update","patch","delete"]
```

### Expected Result

High-impact operations generate auditable events.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Balance forensic value against sensitive payload exposure and log volume.

---

## Enhanced Administration Lab 46 — Audit Log Protection

### Objective

Turn **Audit Log Protection** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
API server audit
  ↓ protected collector
  ↓ SIEM/log archive
```

### Expected Result

Security events remain available after a cluster or node incident.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Separate audit-log administration from workload administrators where possible.

---

## Enhanced Administration Lab 47 — Node OS Baseline

### Objective

Turn **Node OS Baseline** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
uname -a
cat /etc/os-release
timedatectl status
mount | grep cgroup
```

### Expected Result

Kernel, distribution, time, and cgroup baseline are documented.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Standardize node images/configuration and avoid snowflake workers.

---

## Enhanced Administration Lab 48 — Time Synchronization

### Objective

Turn **Time Synchronization** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
timedatectl status
chronyc tracking 2>/dev/null || true
```

### Expected Result

Nodes report synchronized time and bounded offset.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Monitor time sync as a cluster dependency.

---

## Enhanced Administration Lab 49 — cgroup Driver Alignment

### Objective

Turn **cgroup Driver Alignment** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get node <NODE> -o jsonpath='{.status.nodeInfo.containerRuntimeVersion}{"\n"}'
crictl info 2>/dev/null | head -80
```

### Expected Result

Runtime and node configuration can be compared.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use systemd cgroup integration on modern systemd-based nodes unless platform guidance says otherwise.

---

## Enhanced Administration Lab 50 — Swap Policy

### Objective

Turn **Swap Policy** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
swapon --show
grep -R "memorySwap" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Result

Host swap state and kubelet policy are both known.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Follow the current Kubernetes/kubelet swap guidance for the chosen workload model.

---

## Enhanced Administration Lab 51 — Kernel Module / sysctl Dependency

### Objective

Turn **Kernel Module / sysctl Dependency** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
lsmod | grep -E 'overlay|br_netfilter'
sysctl net.ipv4.ip_forward
```

### Expected Result

Required kernel facilities are explicitly verified.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use CNI/vendor-supported node settings rather than blindly copying old sysctl lists.

---

## Enhanced Administration Lab 52 — Containerd CRI Health

### Objective

Turn **Containerd CRI Health** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
systemctl status containerd --no-pager
crictl info
```

### Expected Result

CRI responds with runtime configuration and status.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use crictl to validate the kubelet-facing runtime interface.

---

## Enhanced Administration Lab 53 — crictl Runtime Endpoint

### Objective

Turn **crictl Runtime Endpoint** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```yaml
# /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
```

### Expected Result

crictl connects deterministically to the intended runtime.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Standardize crictl configuration on nodes.

---

## Enhanced Administration Lab 54 — CRI Sandbox Mapping

### Objective

Turn **CRI Sandbox Mapping** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
crictl pods
crictl ps -a
```

### Expected Result

Pod sandbox IDs can be mapped to container IDs.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use sandbox evidence for FailedCreatePodSandBox/CNI troubleshooting.

---

## Enhanced Administration Lab 55 — Static Pod Lifecycle

### Objective

Turn **Static Pod Lifecycle** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ls -l /etc/kubernetes/manifests
crictl ps -a | grep -E 'kube-apiserver|etcd|scheduler|controller'
```

### Expected Result

Manifest files map to CRI containers even when the API is unavailable.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use node-local tools first during control-plane outages.

---

## Enhanced Administration Lab 56 — Static Pod Manifest Safety

### Objective

Turn **Static Pod Manifest Safety** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
/etc/kubernetes/manifests/
  kube-apiserver.yaml
  scheduler.yaml
  accidental-backup.yaml  ← potentially dangerous
```

### Expected Result

Only intended static Pod manifests exist in the watched directory.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Keep backups outside the manifest path and make atomic reviewed changes.

---

## Enhanced Administration Lab 57 — kubeadm Config as Code

### Objective

Turn **kubeadm Config as Code** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubeadm config print init-defaults > kubeadm-init.yaml
```

### Expected Result

Bootstrap configuration is version-controlled and reviewable.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat kubeadm config as infrastructure source, not one-time shell history.

---

## Enhanced Administration Lab 58 — kubeadm Preflight

### Objective

Turn **kubeadm Preflight** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubeadm init --config kubeadm-init.yaml --dry-run
```

### Expected Result

Preflight findings are reviewed before cluster creation.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Resolve preflight causes instead of broadly ignoring them.

---

## Enhanced Administration Lab 59 — Pod/Service CIDR Planning

### Objective

Turn **Pod/Service CIDR Planning** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Node:    10.10.0.0/16
Pods:    10.244.0.0/16
Services:10.96.0.0/12
LB pool: 10.20.50.0/24
```

### Expected Result

Every address domain is documented and non-overlapping.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Design IPAM before installing the CNI.

---

## Enhanced Administration Lab 60 — Pod CIDR Capacity Math

### Objective

Turn **Pod CIDR Capacity Math** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```python
nodes = 100
pods_per_node = 110
needed = nodes * pods_per_node
print("Pod addresses required before reserve:", needed)
```

### Expected Result

Address demand is estimated before choosing CIDRs.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Leave address headroom for growth and CNI allocation blocks.

---

## Enhanced Administration Lab 61 — Service CIDR Immutability Risk

### Objective

Turn **Service CIDR Immutability Risk** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Service CIDR
  ↓ kube-apiserver/controller-manager
  ↓ cluster DNS Service
  ↓ all ClusterIPs
```

### Expected Result

The Service address plan is treated as foundational cluster configuration.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Choose Service CIDR carefully before production bootstrap.

---

## Enhanced Administration Lab 62 — kubeadm Join Trust

### Objective

Turn **kubeadm Join Trust** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubeadm token create --print-join-command
```

### Expected Result

The join command contains endpoint, token, and CA pin.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat bootstrap tokens as short-lived and regenerate when needed.

---

## Enhanced Administration Lab 63 — Node Name Reuse

### Objective

Turn **Node Name Reuse** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get nodes
hostnamectl
```

### Expected Result

The intended node identity is unique.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use replaceable node lifecycle and cleanly delete stale Node objects before reuse.

---

## Enhanced Administration Lab 64 — kubeadm Reset Scope

### Objective

Turn **kubeadm Reset Scope** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubeadm reset --dry-run 2>/dev/null || true
```

### Expected Result

Operators understand reset is not a complete machine reimage.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Reimage nodes for clean reproducible rebuilds when practical.

---

## Enhanced Administration Lab 65 — Air-Gapped Dependency Inventory

### Objective

Turn **Air-Gapped Dependency Inventory** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
internal mirrors:
apt/rpm
registry
Helm/OCI charts
Git/artifacts
time/DNS/PKI
```

### Expected Result

Every bootstrap/runtime dependency has an offline source.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test an installation with Internet physically blocked before declaring it air-gapped.

---

## Enhanced Administration Lab 66 — Registry Mirror Trust

### Objective

Turn **Registry Mirror Trust** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
nodes/containerd
  ↓ internal mirror
  ↓ approved upstream
```

### Expected Result

Nodes pull through a managed trusted path.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Harden mirrors with TLS, auth, retention, scanning, and monitoring.

---

## Enhanced Administration Lab 67 — CNI Responsibility

### Objective

Turn **CNI Responsibility** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
kubelet/runtime
  ↓ CNI ADD
network namespace
  ↓ veth/IP/routes/policy
Pod network ready
```

### Expected Result

Pod sandbox events can be correlated with CNI agent/config state.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Know exactly which CNI component owns IPAM, routing, and policy.

---

## Enhanced Administration Lab 68 — FailedCreatePodSandBox

### Objective

Turn **FailedCreatePodSandBox** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
crictl pods
```

### Expected Result

The event message identifies runtime/CNI setup failure.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not debug application logs when the sandbox never started.

---

## Enhanced Administration Lab 69 — CNI Config Inventory

### Objective

Turn **CNI Config Inventory** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ls -l /etc/cni/net.d 2>/dev/null
ls -l /opt/cni/bin 2>/dev/null | head
```

### Expected Result

Installed CNI configs/binaries are known.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Manage node CNI state declaratively through the supported add-on installer.

---

## Enhanced Administration Lab 70 — Overlay MTU

### Objective

Turn **Overlay MTU** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ip link
ping -M do -s 1400 <AUTHORIZED_PEER> 2>/dev/null || true
```

### Expected Result

Interface MTUs and path behavior can be compared.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Derive Pod MTU from the actual underlay and encapsulation.

---

## Enhanced Administration Lab 71 — Routed/BGP CNI

### Objective

Turn **Routed/BGP CNI** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
worker PodCIDR
  ↓ BGP/native route
underlay
  ↓
remote worker PodCIDR
```

### Expected Result

Cross-node routing is visible in route/BGP state rather than tunnels.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Coordinate CNI routing with the data-center/cloud network team.

---

## Enhanced Administration Lab 72 — eBPF Service Data Plane

### Objective

Turn **eBPF Service Data Plane** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-system get ds | grep -E 'cilium|calico|kube-proxy'
```

### Expected Result

The cluster's actual Service/network implementation is identified.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Never apply kube-proxy-specific troubleshooting assumptions to a kube-proxy-free cluster.

---

## Enhanced Administration Lab 73 — kube-proxy Mode

### Objective

Turn **kube-proxy Mode** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-system get cm kube-proxy -o yaml 2>/dev/null | head -120
```

### Expected Result

Configured kube-proxy mode can be identified where kube-proxy is used.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Document the Service data-plane implementation per cluster.

---

## Enhanced Administration Lab 74 — Service Packet Path

### Objective

Turn **Service Packet Path** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
client Pod
  ↓ Service VIP:port
Service data plane
  ↓ selected EndpointSlice address
target Pod
```

### Expected Result

Each layer can be tested independently.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Check EndpointSlices before node packet rules.

---

## Enhanced Administration Lab 75 — EndpointSlice Conditions

### Objective

Turn **EndpointSlice Conditions** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get endpointslices -l kubernetes.io/service-name=<SVC> -o yaml
```

### Expected Result

Endpoint lifecycle is visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use endpoint conditions to explain traffic gaps during rollout.

---

## Enhanced Administration Lab 76 — Conntrack Pressure

### Objective

Turn **Conntrack Pressure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
sysctl net.netfilter.nf_conntrack_max 2>/dev/null || true
conntrack -S 2>/dev/null || true
```

### Expected Result

Capacity and insert/drop counters are available where tooling is installed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Tune conntrack only after measuring connection behavior and table pressure.

---

## Enhanced Administration Lab 77 — Ephemeral Port Pressure

### Objective

Turn **Ephemeral Port Pressure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
sysctl net.ipv4.ip_local_port_range
ss -s
```

### Expected Result

Socket and port-range evidence supports or rejects the hypothesis.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use connection pooling/reuse and adequate NAT capacity.

---

## Enhanced Administration Lab 78 — CoreDNS Request Path

### Objective

Turn **CoreDNS Request Path** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Pod /etc/resolv.conf
  ↓ kube-dns ClusterIP
CoreDNS
  ↓ kubernetes plugin / forward
upstream DNS
```

### Expected Result

Cluster-local and external DNS paths can be isolated.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test `kubernetes.default` separately from external domains.

---

## Enhanced Administration Lab 79 — CoreDNS ConfigMap Change Risk

### Objective

Turn **CoreDNS ConfigMap Change Risk** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-system get cm coredns -o yaml
kubectl -n kube-system logs deploy/coredns --tail=100
```

### Expected Result

Configuration and parser/runtime errors are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Validate CoreDNS changes in a staging cluster and retain rollback.

---

## Enhanced Administration Lab 80 — systemd-resolved Interaction

### Objective

Turn **systemd-resolved Interaction** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
readlink -f /etc/resolv.conf
cat /run/systemd/resolve/resolv.conf 2>/dev/null || true
```

### Expected Result

The node's real upstream resolver file can be distinguished from a local stub.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Configure kubelet resolvConf according to the OS/CNI guidance.

---

## Enhanced Administration Lab 81 — NodeLocal DNS Cache

### Objective

Turn **NodeLocal DNS Cache** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-system get ds | grep -i dns
```

### Expected Result

The cluster can identify whether node-local DNS is installed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Monitor cache agents and preserve fallback behavior.

---

## Enhanced Administration Lab 82 — NetworkPolicy Enforcement Verification

### Objective

Turn **NetworkPolicy Enforcement Verification** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get networkpolicy -A
kubectl -n <NS> run test --rm -it --image=busybox -- sh
```

### Expected Result

An allowed flow succeeds and a denied flow fails in the authorized lab.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Include policy-enforcement tests in CNI upgrades.

---

## Enhanced Administration Lab 83 — Default-Deny Egress

### Objective

Turn **Default-Deny Egress** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
deny all
  + DNS
  + database
  + required external API
  + registry only if workload pulls directly
```

### Expected Result

The dependency list becomes part of application/network policy.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Roll out deny egress gradually with observability.

---

## Enhanced Administration Lab 84 — Ingress Controller HA

### Objective

Turn **Ingress Controller HA** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get deploy -A | grep -i ingress
kubectl get pdb -A
```

### Expected Result

Controller replica and disruption configuration are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat ingress as a production service with its own SLO.

---

## Enhanced Administration Lab 85 — Ingress 502/503 Decomposition

### Objective

Turn **Ingress 502/503 Decomposition** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe ingress <ING>
kubectl get svc <SVC>
kubectl get endpointslices -l kubernetes.io/service-name=<SVC>
```

### Expected Result

The failing hop is isolated.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Walk edge → route → Service → endpoint → app.

---

## Enhanced Administration Lab 86 — Gateway API Ownership

### Objective

Turn **Gateway API Ownership** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get gatewayclasses,gateways,httproutes -A
```

### Expected Result

Infrastructure and route resources can be audited separately.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use attachment policy to preserve tenancy boundaries.

---

## Enhanced Administration Lab 87 — Gateway API Status Conditions

### Objective

Turn **Gateway API Status Conditions** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get httproute <ROUTE> -o yaml | sed -n '/status:/,$p'
```

### Expected Result

Rejected parent/backend references are explicit.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use status before editing DNS or load balancers.

---

## Enhanced Administration Lab 88 — LoadBalancer Service on Bare Metal

### Objective

Turn **LoadBalancer Service on Bare Metal** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Service type LoadBalancer
  ↓ controller
address pool
  ↓ L2/BGP/appliance advertisement
```

### Expected Result

The source of external IP allocation is documented.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Avoid assuming cloud-controller behavior exists on-premises.

---

## Enhanced Administration Lab 89 — StorageClass Governance

### Objective

Turn **StorageClass Governance** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get storageclass
```

### Expected Result

The default class and key parameters are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use deliberate defaults and document service-level characteristics.

---

## Enhanced Administration Lab 90 — CSI Controller vs Node Plugin

### Objective

Turn **CSI Controller vs Node Plugin** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pods -A | grep -i csi
kubectl get csidrivers
```

### Expected Result

Controller Deployments and node DaemonSets can be mapped.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Troubleshoot provision/attach and mount as separate CSI paths.

---

## Enhanced Administration Lab 91 — PVC Pending

### Objective

Turn **PVC Pending** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe pvc <PVC>
kubectl get storageclass
```

### Expected Result

PVC events identify the storage control-plane failure.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Read claim events before changing the workload controller.

---

## Enhanced Administration Lab 92 — VolumeAttachment

### Objective

Turn **VolumeAttachment** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get volumeattachments
```

### Expected Result

Attachment state and target node are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not force-detach until the old node's write ownership is understood.

---

## Enhanced Administration Lab 93 — Multi-Attach Failure

### Objective

Turn **Multi-Attach Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Pod old node
  ↓ volume attached
node fails
replacement Pod new node
  ↓ multi-attach blocked
```

### Expected Result

The storage system and VolumeAttachment identify the current attachment owner.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use fencing/driver-supported detach procedures for stateful failover.

---

## Enhanced Administration Lab 94 — WaitForFirstConsumer

### Objective

Turn **WaitForFirstConsumer** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get storageclass <SC> -o jsonpath='{.volumeBindingMode}{"\n"}'
```

### Expected Result

The binding mode reflects topology-aware provisioning.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use WaitForFirstConsumer for zonal storage unless the driver has another documented model.

---

## Enhanced Administration Lab 95 — Volume Expansion

### Objective

Turn **Volume Expansion** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pvc <PVC>
kubectl describe pvc <PVC>
```

### Expected Result

Conditions/events show resize progression.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Verify filesystem capacity inside the workload after expansion.

---

## Enhanced Administration Lab 96 — Volume Snapshot Control Plane

### Objective

Turn **Volume Snapshot Control Plane** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl api-resources | grep -i volumesnapshot
```

### Expected Result

Snapshot APIs exist only when the required CRDs/controllers are installed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat snapshots as optional CSI ecosystem functionality, not automatic core storage.

---

## Enhanced Administration Lab 97 — Snapshot vs Backup

### Objective

Turn **Snapshot vs Backup** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
snapshot → fast local recovery
backup   → independent retention + isolation + restore test
```

### Expected Result

The recovery architecture distinguishes local snapshot from disaster backup.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Define off-cluster/off-domain backup for critical state.

---

## Enhanced Administration Lab 98 — Database Consistency

### Objective

Turn **Database Consistency** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
database checkpoint/quiesce
  ↓ snapshot/backup
  ↓ resume
  ↓ restore validation
```

### Expected Result

Recovery produces a database that passes application integrity checks.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use database-aware backup semantics.

---

## Enhanced Administration Lab 99 — Reclaim Policy Risk

### Objective

Turn **Reclaim Policy Risk** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pv -o custom-columns=PV:.metadata.name,RECLAIM:.spec.persistentVolumeReclaimPolicy,STATUS:.status.phase
```

### Expected Result

Data-destruction behavior is visible before cleanup.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Require review for deletion of data-bearing PVCs/PVs.

---

## Enhanced Administration Lab 100 — Node Capacity vs Allocatable

### Objective

Turn **Node Capacity vs Allocatable** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get node <NODE> -o jsonpath='{.status.capacity}{"\n"}{.status.allocatable}{"\n"}'
```

### Expected Result

Capacity and scheduler-available resources differ.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Reserve resources explicitly for the OS and Kubernetes daemons.

---

## Enhanced Administration Lab 101 — kubeReserved / systemReserved

### Objective

Turn **kubeReserved / systemReserved** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
node capacity
 - systemReserved
 - kubeReserved
 - eviction reserve
 = allocatable
```

### Expected Result

Host overhead is accounted before scheduling application Pods.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Capacity-plan the node as a system, not just a sum of Pod limits.

---

## Enhanced Administration Lab 102 — Eviction Signals

### Objective

Turn **Eviction Signals** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
grep -n "eviction" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Result

Configured eviction thresholds can be reviewed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Tune eviction with storage layout and workload behavior.

---

## Enhanced Administration Lab 103 — DiskPressure Decomposition

### Objective

Turn **DiskPressure Decomposition** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
df -h
df -i
crictl images
du -sh /var/log/pods /var/log/containers 2>/dev/null || true
```

### Expected Result

The node-local disk consumer is identified.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use kubelet/runtime-supported cleanup rather than deleting random runtime files.

---

## Enhanced Administration Lab 104 — Image Garbage Collection

### Objective

Turn **Image Garbage Collection** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
crictl images
grep -n "imageGCHighThresholdPercent\|imageGCLowThresholdPercent" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Result

Image inventory and GC thresholds are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Monitor imagefs usage and keep images small/immutable.

---

## Enhanced Administration Lab 105 — Container Log Rotation

### Objective

Turn **Container Log Rotation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
grep -n "containerLogMax" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Result

Local per-container rotation settings can be reviewed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Coordinate kubelet log rotation with the log collector.

---

## Enhanced Administration Lab 106 — MemoryPressure

### Objective

Turn **MemoryPressure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe node <NODE> | sed -n '/Conditions:/,/Allocated resources:/p'
free -h
```

### Expected Result

Node pressure and host memory state can be compared.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Distinguish node-level memory exhaustion from cgroup OOM.

---

## Enhanced Administration Lab 107 — PIDPressure

### Objective

Turn **PIDPressure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ps -e --no-headers | wc -l
kubectl describe node <NODE> | grep -A2 PIDPressure
```

### Expected Result

Node PID usage and pressure condition are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Apply process limits and investigate process leaks/fork storms.

---

## Enhanced Administration Lab 108 — Scheduling Constraint Order

### Objective

Turn **Scheduling Constraint Order** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Result

FailedScheduling messages list unsatisfied constraints.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Read scheduler events before changing node labels or resources.

---

## Enhanced Administration Lab 109 — Capacity Fragmentation

### Objective

Turn **Capacity Fragmentation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
4 nodes × 1 CPU free
Pod requests 3 CPU
→ unschedulable
```

### Expected Result

Aggregate capacity is distinguished from per-node fit.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Track large-Pod fit and consider node-pool sizing.

---

## Enhanced Administration Lab 110 — Topology Spread

### Objective

Turn **Topology Spread** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pod -l app=api -o custom-columns=POD:.metadata.name,NODE:.spec.nodeName,ZONE:.metadata.labels.topology\.kubernetes\.io/zone
```

### Expected Result

Replica distribution across nodes/zones is visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test loss of a topology domain, not just normal distribution.

---

## Enhanced Administration Lab 111 — PDB Semantics

### Objective

Turn **PDB Semantics** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pdb -A
```

### Expected Result

Allowed disruptions and current healthy counts are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Set PDBs so maintenance remains possible under realistic capacity.

---

## Enhanced Administration Lab 112 — Drain Prechecks

### Objective

Turn **Drain Prechecks** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pods -A -o wide --field-selector spec.nodeName=<NODE>
kubectl get pdb -A
```

### Expected Result

Node workload inventory is known before eviction.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Never run drain blindly on stateful or capacity-constrained nodes.

---

## Enhanced Administration Lab 113 — Cordon vs Drain

### Objective

Turn **Cordon vs Drain** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl cordon <NODE>
kubectl drain <NODE> --ignore-daemonsets
```

### Expected Result

The node becomes unschedulable, then managed workloads move according to policy.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use cordon for immediate placement stop and drain for maintenance evacuation.

---

## Enhanced Administration Lab 114 — Priority and Preemption

### Objective

Turn **Priority and Preemption** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get priorityclasses
```

### Expected Result

Priority classes and values are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Reserve high priority for workloads whose importance justifies preemption.

---

## Enhanced Administration Lab 115 — ResourceQuota

### Objective

Turn **ResourceQuota** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get resourcequota -A
kubectl describe resourcequota -n <NS>
```

### Expected Result

Used versus hard quota is visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use quotas to contain tenants and create predictable capacity boundaries.

---

## Enhanced Administration Lab 116 — LimitRange

### Objective

Turn **LimitRange** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get limitrange -A
```

### Expected Result

Namespace resource defaults/min/max are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Pair LimitRange with quota and application right-sizing.

---

## Enhanced Administration Lab 117 — HPA Request Dependency

### Objective

Turn **HPA Request Dependency** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe hpa <HPA>
```

### Expected Result

Current metric, target, and replica recommendation are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Fix missing/incorrect requests before tuning HPA targets.

---

## Enhanced Administration Lab 118 — HPA Stabilization

### Objective

Turn **HPA Stabilization** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
metric spike
  ↓ desired replicas
stabilization policy
  ↓ bounded scale action
```

### Expected Result

Autoscaling does not chase every momentary metric change.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Tune stabilization using workload startup and traffic patterns.

---

## Enhanced Administration Lab 119 — Cluster Autoscaler Interaction

### Objective

Turn **Cluster Autoscaler Interaction** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
load ↑
HPA replicas ↑
Pending Pods
node autoscaler
new node
Pod start
```

### Expected Result

Burst response time includes multiple control loops.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Keep spare capacity or queues for traffic faster than node provisioning.

---

## Enhanced Administration Lab 120 — Multi-Team Namespace Baseline

### Objective

Turn **Multi-Team Namespace Baseline** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Namespace
  + owner labels
  + quota
  + LimitRange
  + PSA
  + NetworkPolicy
  + RBAC
```

### Expected Result

New teams receive consistent guardrails.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Automate namespace provisioning rather than creating empty namespaces manually.

---

## Enhanced Administration Lab 121 — Node Pool Separation

### Objective

Turn **Node Pool Separation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
general pool
gpu pool
system pool
untrusted sandbox pool
```

### Expected Result

Workloads land on intended hardware/trust domains.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use separate pools only when the isolation/capability requirement justifies capacity fragmentation.

---

## Enhanced Administration Lab 122 — Kubelet Secure Port

### Objective

Turn **Kubelet Secure Port** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ss -lntp | grep 10250
```

### Expected Result

The kubelet secure listener is visible on the node.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Restrict network access and keep anonymous/authorization settings hardened.

---

## Enhanced Administration Lab 123 — Kubelet Logs

### Objective

Turn **Kubelet Logs** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
journalctl -u kubelet -b --no-pager | tail -120
```

### Expected Result

Recent node-agent failures are available even if kubectl is unavailable.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Preserve node logs before restarting kubelet.

---

## Enhanced Administration Lab 124 — Runtime Logs

### Objective

Turn **Runtime Logs** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
journalctl -u containerd -b --no-pager | tail -120
crictl ps -a
```

### Expected Result

Runtime errors can be correlated with Kubernetes container state.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use runtime evidence for CreateContainerError and image/sandbox failures.

---

## Enhanced Administration Lab 125 — Control Plane without API

### Objective

Turn **Control Plane without API** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
systemctl status kubelet --no-pager
crictl ps -a
ss -lntp | grep -E '6443|2379'
ls -l /etc/kubernetes/manifests
```

### Expected Result

The control-plane failure can be investigated without kubectl.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Practice API-down troubleshooting before an actual incident.

---

## Enhanced Administration Lab 126 — Scheduler Failure

### Objective

Turn **Scheduler Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pods -A --field-selector spec.nodeName=
kubectl -n kube-system get pod -l component=kube-scheduler
```

### Expected Result

Unscheduled Pods and scheduler component state are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Differentiate scheduler outage from unsatisfied scheduling constraints.

---

## Enhanced Administration Lab 127 — Controller Manager Failure

### Objective

Turn **Controller Manager Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-system get pod -l component=kube-controller-manager
```

### Expected Result

Controller component health can be checked when API still works.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Expect existing Pods to run while desired-state convergence degrades.

---

## Enhanced Administration Lab 128 — Kubelet Failure

### Objective

Turn **Kubelet Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
systemctl status kubelet --no-pager
kubectl describe node <NODE>
```

### Expected Result

Node Ready/Lease behavior can be correlated with kubelet state.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Fix the node agent rather than immediately deleting workloads.

---

## Enhanced Administration Lab 129 — Container Runtime Failure

### Objective

Turn **Container Runtime Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
systemctl status containerd --no-pager
crictl info
```

### Expected Result

Runtime health is confirmed independently of kubelet.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Restore CRI before interpreting Pod restart failures.

---

## Enhanced Administration Lab 130 — Node Lease

### Objective

Turn **Node Lease** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-node-lease get lease <NODE> -o yaml
```

### Expected Result

RenewTime shows recent node heartbeat activity.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Check API reachability and kubelet when lease updates stop.

---

## Enhanced Administration Lab 131 — Node NotReady Tree

### Objective

Turn **Node NotReady Tree** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe node <NODE>
journalctl -u kubelet -b --no-pager | tail -100
crictl info
```

### Expected Result

Conditions/events and host evidence identify the failing subsystem.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Troubleshoot the node as a layered system.

---

## Enhanced Administration Lab 132 — ImagePullBackOff Tree

### Objective

Turn **ImagePullBackOff Tree** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
crictl pull <IMAGE>
```

### Expected Result

Direct CRI pull confirms whether the issue is runtime/registry rather than controller logic.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test from the affected node.

---

## Enhanced Administration Lab 133 — CrashLoopBackOff Tree

### Objective

Turn **CrashLoopBackOff Tree** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl logs <POD> -c <CONTAINER> --previous
kubectl describe pod <POD>
```

### Expected Result

The last terminated state is available before manual restart/delete.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Capture evidence before replacing the Pod.

---

## Enhanced Administration Lab 134 — CreateContainerConfigError

### Objective

Turn **CreateContainerConfigError** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
```

### Expected Result

The exact missing or invalid configuration object is named.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Fix the referenced object rather than changing the image.

---

## Enhanced Administration Lab 135 — FailedMount Tree

### Objective

Turn **FailedMount Tree** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl describe pod <POD> | sed -n '/Events:/,$p'
kubectl get volumeattachments
```

### Expected Result

The error can be placed at attach versus mount versus filesystem layer.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Follow PVC → PV → VolumeAttachment → CSI controller/node path.

---

## Enhanced Administration Lab 136 — Service No Endpoints Tree

### Objective

Turn **Service No Endpoints Tree** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get svc <SVC> -o yaml
kubectl get endpointslices -l kubernetes.io/service-name=<SVC> -o wide
kubectl get pods --show-labels
```

### Expected Result

Selection and readiness are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not restart kube-proxy before proving endpoints exist.

---

## Enhanced Administration Lab 137 — Cross-Node Network Failure

### Objective

Turn **Cross-Node Network Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ip route
ip link
kubectl -n kube-system get pods -o wide
```

### Expected Result

Node-to-node data-plane state can be correlated with Pod placement.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Pin test Pods to different nodes and trace the packet path.

---

## Enhanced Administration Lab 138 — All Pods on One Node Lose Network

### Objective

Turn **All Pods on One Node Lose Network** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-system get pods -o wide --field-selector spec.nodeName=<NODE>
ip route
```

### Expected Result

Node-local network agents can be compared with healthy nodes.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Compare bad node state against a known-good node.

---

## Enhanced Administration Lab 139 — DNS Local vs External Failure

### Objective

Turn **DNS Local vs External Failure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl run dns-test --rm -it --image=busybox --   sh -c 'nslookup kubernetes.default; nslookup example.com'
```

### Expected Result

Cluster-local and upstream resolution are tested separately.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Split DNS troubleshooting into internal and external branches.

---

## Enhanced Administration Lab 140 — Webhook Outage Tree

### Objective

Turn **Webhook Outage Tree** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get validatingwebhookconfiguration,mutatingwebhookconfiguration
kubectl get svc,endpointslices -A | grep -i webhook
```

### Expected Result

Webhook service reachability and configuration are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use a documented emergency policy only when a failing webhook blocks critical recovery.

---

## Enhanced Administration Lab 141 — High API Error Rate

### Objective

Turn **High API Error Rate** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
API metric
  ↓ verb/resource/user-agent
  ↓ latency/error class
  ↓ etcd/webhook/control-plane dependency
```

### Expected Result

The request class causing load is identified.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Throttle/fix the noisy client rather than only scaling the control plane.

---

## Enhanced Administration Lab 142 — Cluster SLOs

### Objective

Turn **Cluster SLOs** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
API availability ≥ 99.95%
p99 Pod scheduling < target
DNS success ≥ target
Ready nodes ≥ target
```

### Expected Result

Platform health is connected to user/team experience.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Define SLOs before deciding alert thresholds.

---

## Enhanced Administration Lab 143 — Prometheus Platform Metrics

### Objective

Turn **Prometheus Platform Metrics** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
components/node/app
  ↓ metrics
Prometheus/managed backend
  ↓ alerts + dashboards
```

### Expected Result

Control-plane, node, object, and application metrics are separated.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not use metrics-server as long-term monitoring.

---

## Enhanced Administration Lab 144 — kube-state-metrics

### Objective

Turn **kube-state-metrics** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Deployment desired/available
Pod phase
PVC status
Node condition
```

### Expected Result

Object-state metrics complement node/runtime metrics.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use object metrics for controller/SLO alerts.

---

## Enhanced Administration Lab 145 — Platform Alert Quality

### Objective

Turn **Platform Alert Quality** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
alert:
condition
duration
severity
owner
runbook
user impact
```

### Expected Result

Each page has an actionable first response.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Page on sustained actionable conditions; dashboard noisy diagnostics.

---

## Enhanced Administration Lab 146 — Certificate Alerting

### Objective

Turn **Certificate Alerting** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
days_remaining
  ↓ warn threshold
  ↓ critical threshold
renew/runbook
```

### Expected Result

Expiry is handled before service interruption.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Monitor API, kubelet, webhook, ingress, and external certs.

---

## Enhanced Administration Lab 147 — API Audit + Workload Logs Correlation

### Objective

Turn **API Audit + Workload Logs Correlation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
audit: user verb resource timestamp
events: rollout/restart
logs: app failure
node: runtime/kernel
```

### Expected Result

One incident timeline can connect control-plane actions to data-plane effects.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Synchronize time and centralize logs.

---

## Enhanced Administration Lab 148 — Backup Scope Classification

### Objective

Turn **Backup Scope Classification** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
control-plane state → etcd
cluster construction → IaC/kubeadm
workload desired state → Git
persistent business data → app backups
artifacts → registry
```

### Expected Result

Each asset has a backup owner and recovery path.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not call an etcd snapshot a complete business backup.

---

## Enhanced Administration Lab 149 — Rebuild vs Restore DR

### Objective

Turn **Rebuild vs Restore DR** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Path A: etcd restore
Path B: new cluster → Git reconcile → data restore
```

### Expected Result

Both recovery strategies have documented RPO/RTO trade-offs.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test the recovery path you expect to use under pressure.

---

## Enhanced Administration Lab 150 — Cluster RPO

### Objective

Turn **Cluster RPO** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
cluster RPO ≠ application data RPO
```

### Expected Result

Different state domains receive separate RPO targets.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not infer application recoverability from etcd backup.

---

## Enhanced Administration Lab 151 — Cluster RTO Decomposition

### Objective

Turn **Cluster RTO Decomposition** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```python
steps = {"detect":5,"infra":20,"control_plane":15,"addons":15,"data":30,"validate":10}
print("RTO minutes:", sum(steps.values()))
```

### Expected Result

Recovery time is broken into measurable components.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Measure RTO through full game days.

---

## Enhanced Administration Lab 152 — Restore Test Evidence

### Objective

Turn **Restore Test Evidence** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
restore complete?
  ↓ API
  ↓ system Pods
  ↓ DNS/network
  ↓ storage
  ↓ app
  ↓ business transaction
```

### Expected Result

The recovered platform supports end-to-end workload use.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Define a smoke-test checklist for every restore drill.

---

## Enhanced Administration Lab 153 — Control Plane Failure-Domain Spread

### Objective

Turn **Control Plane Failure-Domain Spread** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
bad:
rack A: cp1 cp2 cp3

better:
rack/zone A: cp1
rack/zone B: cp2
rack/zone C: cp3
```

### Expected Result

Member placement is documented against physical/cloud failure domains.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Design HA against correlated infrastructure failures.

---

## Enhanced Administration Lab 154 — Maintenance Capacity

### Objective

Turn **Maintenance Capacity** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```python
nodes = 4
usable_per_node = 8
normal_requested = 28
after_one_node_loss = (nodes-1)*usable_per_node
print("Capacity after one node loss:", after_one_node_loss, "requested:", normal_requested)
```

### Expected Result

The cluster's N-1 scheduling headroom is explicit.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Capacity-plan for the largest maintenance/failure scenario.

---

## Enhanced Administration Lab 155 — Sequential Minor Upgrade

### Objective

Turn **Sequential Minor Upgrade** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
current minor
  ↓ release/API/add-on review
etcd snapshot
  ↓ first control plane
other control planes
  ↓ workers in waves
verify
```

### Expected Result

Every stage has a known target and verification gate.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Never skip unsupported minors or assume downgrade is easy.

---

## Enhanced Administration Lab 156 — Version Skew Matrix

### Objective

Turn **Version Skew Matrix** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
component → allowed relation to API server
API server
kubelet
kube-proxy
kubectl
kubeadm
```

### Expected Result

Upgrade sequencing follows upstream skew policy rather than intuition.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Maintain a version matrix for cluster and add-ons.

---

## Enhanced Administration Lab 157 — API Deprecation Scan

### Objective

Turn **API Deprecation Scan** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl api-resources
kubectl get --raw /metrics 2>/dev/null | grep apiserver_requested_deprecated_apis | head
```

### Expected Result

Deprecated API usage can be identified before upgrade where metrics are available.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat deprecation cleanup as an upgrade prerequisite.

---

## Enhanced Administration Lab 158 — CNI Compatibility Gate

### Objective

Turn **CNI Compatibility Gate** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Kubernetes target
  ↕ compatible
CNI version
  ↕
kernel / kube-proxy mode / CRDs
```

### Expected Result

The compatibility matrix is documented before change.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Never upgrade Kubernetes without validating CNI support.

---

## Enhanced Administration Lab 159 — CSI Compatibility Gate

### Objective

Turn **CSI Compatibility Gate** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get csidrivers
kubectl get pods -A | grep -i csi
```

### Expected Result

Driver/sidecar inventory is recorded before upgrade.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test attach/mount/resize/snapshot after CSI upgrades.

---

## Enhanced Administration Lab 160 — CoreDNS Upgrade Gate

### Objective

Turn **CoreDNS Upgrade Gate** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl -n kube-system get cm coredns -o yaml
```

### Expected Result

Custom DNS configuration is inventoried.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test internal/external DNS after every CoreDNS change.

---

## Enhanced Administration Lab 161 — Admission Controller Upgrade Gate

### Objective

Turn **Admission Controller Upgrade Gate** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get validatingwebhookconfigurations,mutatingwebhookconfigurations
```

### Expected Result

Webhook inventory is included in the upgrade plan.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Canary control-plane/API changes in nonproduction first.

---

## Enhanced Administration Lab 162 — Worker Upgrade Wave

### Objective

Turn **Worker Upgrade Wave** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
wave 1: one canary worker
  ↓ soak
wave 2: small percentage
  ↓
remaining workers
```

### Expected Result

A bad node change is contained to a small set.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use progressive node waves with workload smoke tests.

---

## Enhanced Administration Lab 163 — Node Replacement over Repair

### Objective

Turn **Node Replacement over Repair** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
cordon
drain
delete/reimage
bootstrap
join
verify
uncordon
```

### Expected Result

Replacement produces a node matching the current baseline.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Prefer replaceable nodes and automate bootstrap.

---

## Enhanced Administration Lab 164 — Control Plane Node Replacement

### Objective

Turn **Control Plane Node Replacement** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
verify quorum
remove bad LB backend
remove/replace etcd member safely
join new control plane
verify quorum/API
restore LB backend
```

### Expected Result

Quorum remains healthy throughout replacement.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Never remove multiple stacked control planes simultaneously without quorum math.

---

## Enhanced Administration Lab 165 — Etcd Member Removal

### Objective

Turn **Etcd Member Removal** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
etcdctl member list -w table
```

### Expected Result

Member IDs and state are known before removal.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Take a snapshot and verify quorum before membership changes.

---

## Enhanced Administration Lab 166 — GitOps Add-on Management

### Objective

Turn **GitOps Add-on Management** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
cluster bootstrap
  ↓ minimal CNI/DNS
GitOps controller
  ↓ reconciles add-ons
```

### Expected Result

Add-on versions and configuration are auditable in Git.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Avoid two controllers/tools owning the same add-on fields.

---

## Enhanced Administration Lab 167 — Fleet Upgrade Waves

### Objective

Turn **Fleet Upgrade Waves** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
lab → dev → staging → prod-canary → prod-fleet
```

### Expected Result

A regression is caught before all clusters are changed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat cluster upgrades like application releases.

---

## Enhanced Administration Lab 168 — Cluster Inventory

### Objective

Turn **Cluster Inventory** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
cluster
version
runtime
CNI
CSI
ingress
cert expiry
last etcd backup
last restore test
```

### Expected Result

Fleet risk can be queried rather than discovered during incidents.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Automate inventory collection.

---

## Enhanced Administration Lab 169 — Supply-Chain Policy

### Objective

Turn **Supply-Chain Policy** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
image reference
  ↓ registry allow-list
  ↓ digest/signature/provenance
  ↓ policy
allow / reject
```

### Expected Result

Untrusted artifacts are blocked before runtime.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Combine supply-chain policy with runtime least privilege.

---

## Enhanced Administration Lab 170 — Node Image Provenance

### Objective

Turn **Node Image Provenance** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
node image source
  ↓ hardened build
scan/sign
  ↓ node pool
```

### Expected Result

Node versions can be traced to an approved image build.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Treat node images as immutable release artifacts.

---

## Enhanced Administration Lab 171 — Runtime Socket Protection

### Objective

Turn **Runtime Socket Protection** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
ls -l /run/containerd/containerd.sock 2>/dev/null || true
```

### Expected Result

Socket ownership/mode is visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Do not mount host runtime sockets into ordinary workloads.

---

## Enhanced Administration Lab 172 — HostPath/Privileged Inventory

### Objective

Turn **HostPath/Privileged Inventory** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pods -A -o json | jq -r '
.items[] | select(
  .spec.hostNetwork==true or .spec.hostPID==true or
  ([.spec.containers[]?.securityContext.privileged] | any(.==true))
) | [.metadata.namespace,.metadata.name] | @tsv' 2>/dev/null
```

### Expected Result

High-privilege Pods can be enumerated.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Keep exceptions in protected namespaces with dedicated identities and operators.

---

## Enhanced Administration Lab 173 — Cloud Metadata Protection

### Objective

Turn **Cloud Metadata Protection** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Pod
  ✕ node metadata broad credential
  ✓ workload identity scoped credential
```

### Expected Result

Application identity is decoupled from node identity.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use cloud workload identity and metadata restrictions.

---

## Enhanced Administration Lab 174 — Security Incident Containment

### Objective

Turn **Security Incident Containment** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
detect compromised Pod
  ↓ capture logs/imageID/audit
  ↓ isolate network
revoke/rotate credentials
  ↓ replace artifact
  ↓ inspect node/runtime scope
```

### Expected Result

Containment actions reduce blast radius without immediately destroying forensic state.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Prepare a Kubernetes-specific incident runbook.

---

## Enhanced Administration Lab 175 — Namespace Escape Threat Model

### Objective

Turn **Namespace Escape Threat Model** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
namespace boundary
 ≠
kernel/VM boundary
```

### Expected Result

Tenancy design accounts for node/runtime trust.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use dedicated clusters/nodes/sandboxed runtimes for hostile multi-tenancy when required.

---

## Enhanced Administration Lab 176 — Sandboxed RuntimeClass

### Objective

Turn **Sandboxed RuntimeClass** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get runtimeclasses
```

### Expected Result

Available runtime handlers are visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use stronger isolation for untrusted workloads and account for performance/compatibility overhead.

---

## Enhanced Administration Lab 177 — RuntimeClass Scheduling Overhead

### Objective

Turn **RuntimeClass Scheduling Overhead** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Pod resources
+ RuntimeClass overhead
= scheduler accounting
```

### Expected Result

The platform includes sandbox overhead in capacity planning.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Measure overhead before broad adoption.

---

## Enhanced Administration Lab 178 — Cluster DNS SLO

### Objective

Turn **Cluster DNS SLO** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
DNS SLI:
successful queries / total
p95 latency
SERVFAIL rate
```

### Expected Result

DNS problems are detected before applications report widespread timeouts.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Give CoreDNS explicit resources, spread, and PDB where appropriate.

---

## Enhanced Administration Lab 179 — Service Data Plane SLO

### Objective

Turn **Service Data Plane SLO** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
synthetic Pod
  ↓ Service DNS/VIP
test endpoint
  ↓ latency/success
```

### Expected Result

The actual data path is continuously validated.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use synthetic checks for critical shared network paths.

---

## Enhanced Administration Lab 180 — Storage SLO

### Objective

Turn **Storage SLO** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
PVC provision time
attach latency
mount error rate
backend capacity
restore success
```

### Expected Result

Storage alerts reflect workload impact.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Measure storage lifecycle operations and data-path health.

---

## Enhanced Administration Lab 181 — Platform Capacity Forecasting

### Objective

Turn **Platform Capacity Forecasting** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
CPU/memory
Pod IPs
Service IPs
PVC/backend quota
node disk/inodes
conntrack/NAT
control-plane QPS
```

### Expected Result

Cluster growth limits are known before they become incidents.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Forecast every finite resource, not just CPU and memory.

---

## Enhanced Administration Lab 182 — Pod IP Exhaustion

### Objective

Turn **Pod IP Exhaustion** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get pods -A -o wide | wc -l
kubectl get nodes -o wide
```

### Expected Result

Pod count can be compared with CNI/IPAM capacity.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Monitor address pools as a first-class capacity metric.

---

## Enhanced Administration Lab 183 — Service IP Exhaustion

### Objective

Turn **Service IP Exhaustion** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get svc -A | wc -l
```

### Expected Result

Service count can be compared with CIDR capacity.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Avoid unnecessary short-lived Services and size the CIDR for fleet needs.

---

## Enhanced Administration Lab 184 — Control Plane Resource Reservation

### Objective

Turn **Control Plane Resource Reservation** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl top nodes 2>/dev/null || true
kubectl -n kube-system top pods 2>/dev/null || true
```

### Expected Result

Control-plane resource consumption can be observed when metrics are installed.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Size control planes for failure state and maintenance, not average usage.

---

## Enhanced Administration Lab 185 — Admission Latency Budget

### Objective

Turn **Admission Latency Budget** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
API request
  + webhook A
  + webhook B
  + webhook C
= cumulative latency/failure risk
```

### Expected Result

Webhook count and timeouts are considered in API SLO.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Minimize webhook scope/count and monitor webhook latency.

---

## Enhanced Administration Lab 186 — Controller Storm

### Objective

Turn **Controller Storm** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
event
  ↓ reconcile error
requeue too fast
  ↓ API write storm
```

### Expected Result

Noisy controller user-agent/requests can be identified from logs/metrics.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use exponential backoff and rate limiting in custom controllers.

---

## Enhanced Administration Lab 187 — Large Secret/ConfigMap Misuse

### Objective

Turn **Large Secret/ConfigMap Misuse** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
small config/metadata → API
large artifacts/data → object store/registry/database
```

### Expected Result

Application artifacts are kept out of etcd.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use the API for desired-state metadata, not large file distribution.

---

## Enhanced Administration Lab 188 — API Object Churn

### Objective

Turn **API Object Churn** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get jobs -A | wc -l
kubectl get events -A | wc -l
```

### Expected Result

High-churn object classes can be identified.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Use TTL/history limits and efficient controllers for transient workloads.

---

## Enhanced Administration Lab 189 — CronJob History Retention

### Objective

Turn **CronJob History Retention** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
kubectl get cronjob -A
kubectl get jobs -A
```

### Expected Result

Historical object growth is visible.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Configure retention appropriate to audit/debug needs.

---

## Enhanced Administration Lab 190 — Node Drain + Local Data

### Objective

Turn **Node Drain + Local Data** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
before drain:
emptyDir?
local PV?
unmanaged Pod?
DaemonSet?
PDB?
```

### Expected Result

Data-loss or immovable workloads are identified before eviction.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Make local-state dependencies explicit.

---

## Enhanced Administration Lab 191 — Graceful Node Shutdown

### Objective

Turn **Graceful Node Shutdown** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```bash
grep -n "shutdownGracePeriod" /var/lib/kubelet/config.yaml 2>/dev/null || true
```

### Expected Result

Node shutdown grace configuration can be inspected.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Coordinate OS maintenance with kubelet graceful shutdown behavior.

---

## Enhanced Administration Lab 192 — Non-Graceful Node Shutdown Recovery

### Objective

Turn **Non-Graceful Node Shutdown Recovery** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
node lost
  ↓ control plane detects
replacement Pod
  ↓ storage attach/fencing
  ↓
resume service
```

### Expected Result

Recovery sequence accounts for old-node write safety.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Design fencing and storage behavior for hard node failure.

---

## Enhanced Administration Lab 193 — Platform Runbook Structure

### Objective

Turn **Platform Runbook Structure** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
Trigger
Impact
Safety warning
Evidence
Decision tree
Recovery
Verification
Escalation
Prevention
```

### Expected Result

Runbooks are executable under incident pressure.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Test runbooks during game days.

---

## Enhanced Administration Lab 194 — Game Day Design

### Objective

Turn **Game Day Design** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
hypothesis
failure injection
expected detection
recovery target
stop conditions
actual result
actions
```

### Expected Result

The exercise measures real detection/RTO and exposes undocumented dependencies.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Practice failures before production chooses the timing.

---

## Enhanced Administration Lab 195 — Change Evidence Chain

### Objective

Turn **Change Evidence Chain** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
commit
  ↓ change record
apply/upgrade
  ↓ audit/logs
metrics
  ↓ verification
```

### Expected Result

An incident can identify exactly what changed and by whom.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Preserve change evidence for control-plane/add-on upgrades.

---

## Enhanced Administration Lab 196 — Operational Readiness Review

### Objective

Turn **Operational Readiness Review** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
[ ] HA/API endpoint
[ ] etcd backup + restore
[ ] CNI/DNS
[ ] CSI/storage recovery
[ ] identity/RBAC
[ ] Pod security/policy
[ ] encryption/audit
[ ] monitoring/SLO
[ ] upgrade matrix
[ ] capacity N-1
[ ] runbooks/game day
```

### Expected Result

The platform can survive routine operations and defined failures before tenant onboarding.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Make operational readiness a cluster launch gate.

---

## Enhanced Administration Lab 197 — Evidence-First Administration

### Objective

Turn **Evidence-First Administration** into a repeatable cluster-administration or incident-response exercise.

### Safety Boundary

Use disposable VMs/cluster clones or another explicitly authorized lab. For etcd, PKI, CNI, admission, upgrades, and node disruption, create a backup/snapshot and define rollback before mutation. Never use destructive failure injection on shared production.

### Procedure

1. Record cluster/node/runtime/add-on versions.
2. Draw the expected control/data path and failure domains.
3. Capture baseline evidence with the command/configuration below.
4. State the failure hypothesis and stop condition.
5. Introduce one reversible fault in the lab where appropriate.
6. Diagnose from API evidence and node-local evidence.
7. Recover using the documented procedure.
8. Run cluster and workload smoke tests.
9. Record actual RPO/RTO or disruption where relevant.
10. Convert findings into monitoring, automation, or a runbook improvement.

### Command / Configuration

```text
symptom
  ↓ classify layer
capture evidence
  ↓ hypothesis
small change
  ↓ verify
root cause + prevention
```

### Expected Result

Incidents are resolved without random restarts or destructive guesswork.

### Evidence Record

```text
Cluster/version
Affected plane/layer
Symptoms
API status
etcd/control-plane state
Node/kubelet/runtime
CNI/DNS/Service
CSI/storage
Identity/RBAC/admission
Capacity/pressure
Root cause
Recovery
Verification
RTO/RPO
Prevention
```

### Best Practice

Preserve evidence and change one variable at a time.

---

## 5. Hands-on Lab / Practical Exercises

> Perform these labs only on your own/disposable Kubernetes environment.

### Lab 1 — Build the Administration Lab

Create:

```text
cp1
worker1
worker2
```

Linux VMs.

Record:

```text
OS
kernel
IP
hostname
CPU
memory
disk
```

### Lab 2 — Prepare Linux Nodes

Configure:

```text
time sync
required kernel modules
sysctl
containerd
firewall rules
```

according to current kubeadm/CNI documentation.

### Lab 3 — Inspect cgroups and containerd

```bash
containerd --version
crictl info
mount | grep cgroup
systemd-cgls
```

Verify cgroup v2/systemd alignment.

### Lab 4 — Install Kubernetes Packages

Install target v1.36 line:

```text
kubeadm
kubelet
kubectl
```

using current Kubernetes package repository.

Hold/pin packages intentionally.

### Lab 5 — kubeadm Preflight

Run:

```bash
kubeadm init --dry-run
```

or inspect preflight behavior in disposable setup.

Document every warning/error rather than ignoring it.

### Lab 6 — Initialize Control Plane

Use kubeadm configuration file defining:

```text
Kubernetes version
Pod CIDR
Service CIDR
control-plane endpoint if applicable
```

Initialize cluster.

### Lab 7 — Inspect kubeadm Artifacts

Inspect:

```text
/etc/kubernetes/manifests
/etc/kubernetes/pki
/etc/kubernetes/*.conf
/var/lib/kubelet
```

Build a table of purpose and sensitivity.

### Lab 8 — Install CNI

Install a current compatible CNI.

Verify:

```bash
kubectl get nodes
kubectl get pods -A
```

and cross-node Pod networking.

### Lab 9 — Join Workers

Use bootstrap token join.

Verify Node objects and kubelet certificates.

### Lab 10 — CRI Troubleshooting

On worker:

```bash
crictl pods
crictl ps
crictl images
crictl info
```

Map one Pod from Kubernetes to sandbox/container IDs.

### Lab 11 — Static Pod Inspection

On control plane inspect:

```text
kube-apiserver
etcd
scheduler
controller-manager
```

static Pod manifests and runtime containers.

### Lab 12 — Break API Server Safely

In disposable lab, make a reversible invalid change to API static manifest.

Observe:

```text
kubectl failure
kubelet logs
crictl ps -a
API container logs
```

Restore manifest.

### Lab 13 — etcd Health

Use correct certificates to run:

```text
endpoint health
endpoint status
member list
```

Record leader/member information.

### Lab 14 — etcd Snapshot

Create snapshot.

Copy outside cluster.

Validate snapshot metadata.

### Lab 15 — etcd Restore

In isolated/disposable environment:

```text
create test object
snapshot
delete/change state
restore
verify object state
```

Document exact recovery steps.

### Lab 16 — API Request Flow

Create a Namespace and trace conceptually:

```text
kubectl
TLS
authentication
RBAC
admission
etcd
```

Use audit logs if configured.

### Lab 17 — API Deprecation Review

List:

```bash
kubectl api-resources
kubectl api-versions
```

Find any manifests in your lab using non-current/deprecated APIs and update them.

### Lab 18 — HA Architecture Tabletop

Design:

```text
LB
cp1/cp2/cp3
stacked etcd
worker nodes
```

Calculate quorum under one/two member failures.

### Lab 19 — Control-Plane Join Tabletop

Document required:

```text
controlPlaneEndpoint
certificate key
join command
etcd membership
LB health
```

for adding `cp2`.

### Lab 20 — CoreDNS Troubleshooting

Test:

```bash
nslookup kubernetes.default
nslookup external-domain
```

Then intentionally break CoreDNS ConfigMap in reversible lab and recover.

### Lab 21 — kube-proxy / Service Path

Create Service and inspect:

```text
Service IP
EndpointSlices
node kube-proxy
packet path
```

Use node networking tools.

### Lab 22 — Cross-Node Networking

Create Pods pinned to different workers.

Test:

```text
Pod IP → Pod IP
Service → Pod
DNS → Service
```

### Lab 23 — CNI Failure

On disposable lab, stop/delete one CNI node agent or break safe config temporarily.

Observe:

```text
Pod sandbox failures
node/network conditions
CNI logs
```

Recover.

### Lab 24 — MTU Tabletop

Given underlay MTU 1500 and VXLAN overhead, calculate safe Pod MTU.

Design tests with `ping` payload sizes and `curl`.

### Lab 25 — NetworkPolicy

Implement:

```text
default deny ingress/egress
allow DNS
frontend → api
api → db
```

Verify both allowed and denied paths.

### Lab 26 — Gateway API Architecture

Design:

```text
GatewayClass
Gateway
HTTPRoute
TLS
platform/app ownership
```

for two namespaces.

### Lab 27 — CSI Inventory

Inspect:

```bash
kubectl get csidrivers
kubectl get storageclass
kubectl get pods -A | grep -i csi
```

Map controller and node plugins.

### Lab 28 — Dynamic PVC

Create PVC.

Trace:

```text
PVC
StorageClass
PV
CSI provisioning
volume attachment
mount
```

### Lab 29 — PVC Pending Failure

Break StorageClass name or topology.

Use PVC events and CSI logs to diagnose.

### Lab 30 — Volume Expansion

If lab driver supports it, increase PVC size.

Verify:

```text
PVC requested
PV capacity
filesystem capacity
```

### Lab 31 — Snapshot Tabletop

Define:

```text
VolumeSnapshotClass
VolumeSnapshot
restore PVC
```

and explain why application-consistent DB backup may still be required.

### Lab 32 — Scheduling Constraints

Create Pods using:

```text
nodeSelector
required node affinity
preferred node affinity
```

Observe scheduling.

### Lab 33 — Taints and Tolerations

Taint worker:

```text
dedicated=infra:NoSchedule
```

Test Pod without/with toleration.

### Lab 34 — Topology Spread

Deploy 6 replicas.

Spread across:

```text
hostname
zone
```

and inspect distribution.

### Lab 35 — ResourceQuota

Create namespace quota for:

```text
requests.cpu
requests.memory
pods
PVCs
```

Attempt to exceed it.

### Lab 36 — LimitRange

Set default requests/limits.

Create Pod without resources and inspect mutated/defaulted values.

### Lab 37 — Cordon and Drain

Deploy replicated app with PDB.

Run:

```bash
kubectl cordon worker1
kubectl drain worker1 --ignore-daemonsets
```

Observe rescheduling.

Then uncordon.

### Lab 38 — PDB Failure

Create too-restrictive PDB.

Attempt drain.

Explain why drain blocks and how to resolve safely.

### Lab 39 — ServiceAccount + RBAC

Create:

```text
namespace app
ServiceAccount reader
Role pod-reader
RoleBinding
```

Test:

```bash
kubectl auth can-i
```

### Lab 40 — RBAC Impersonation

Test authorized scenarios:

```bash
kubectl auth can-i get pods \
  --as system:serviceaccount:app:reader \
  -n app
```

Then test denied Secret read.

### Lab 41 — Pod Security Admission

Label test namespace for:

```text
enforce=restricted
```

Try privileged Pod.

Observe admission rejection.

Deploy compliant Pod.

### Lab 42 — SecurityContext

Create hardened workload:

```text
runAsNonRoot
allowPrivilegeEscalation false
drop ALL
RuntimeDefault seccomp
readOnlyRootFilesystem
```

Add writable tmpfs/emptyDir only where necessary.

### Lab 43 — Encryption at Rest Tabletop

Design API server EncryptionConfiguration for Secrets using KMS or supported strong provider.

Explain:

```text
existing object rewrite
key rotation
backup
KMS availability
```

### Lab 44 — Audit Logging

Create lab audit policy capturing metadata for:

```text
Secret reads
RBAC changes
Pod exec
```

without logging Secret response bodies.

### Lab 45 — Certificate Expiry

Run:

```bash
kubeadm certs check-expiration
```

Map every certificate to component.

### Lab 46 — Certificate Renewal Tabletop

Document:

```text
renew
restart/static Pod refresh
copy kubeconfig
verify
```

for kubeadm-managed certs.

### Lab 47 — Upgrade Planning

From v1.35 lab/state tabletop to v1.36:

```text
release notes
deprecated APIs
CNI/CSI support
etcd backup
PDB/capacity
```

Build change plan.

### Lab 48 — kubeadm Upgrade

On disposable cluster, perform supported sequential upgrade following current upstream instructions.

Do not skip minor version.

### Lab 49 — Node Upgrade

For one worker:

```text
cordon
drain
package upgrade
kubeadm upgrade node
kubelet restart
verify
uncordon
```

### Lab 50 — Node NotReady Incident

Stop kubelet on worker.

Observe:

```text
Lease
Node Ready
Pod behavior
events
```

Restore and verify.

### Lab 51 — Runtime Failure

Stop containerd on disposable worker.

Use:

```text
systemctl
journalctl
crictl
kubectl describe node
```

to diagnose.

### Lab 52 — DiskPressure Simulation/Tabletop

Fill a controlled small test filesystem or model thresholds.

Inspect:

```text
image usage
logs
emptyDir
inodes
evictions
```

Avoid damaging host root filesystem.

### Lab 53 — API Server Incident

Simulate:

```text
expired/mismatched cert
etcd unavailable
bad static manifest
port conflict
```

as separate tabletop scenarios.

For each define evidence.

### Lab 54 — DNS Incident

Simulate:

```text
CoreDNS down
kube-dns endpoints missing
upstream DNS broken
NetworkPolicy blocks UDP/TCP 53
```

Build diagnostic tree.

### Lab 55 — Service Incident

Simulate:

```text
selector mismatch
readiness false
wrong targetPort
kube-proxy failure
NetworkPolicy deny
```

### Lab 56 — Storage Incident

Simulate:

```text
PVC Pending
FailedAttach
FailedMount
multi-attach
filesystem full
```

### Lab 57 — CKA Troubleshooting Drill

Without hints, solve in sequence:

```text
Node NotReady
Pod Pending
CrashLoopBackOff
Service no endpoints
DNS failure
PVC Pending
RBAC forbidden
```

Time each task.

### Lab 58 — Control Plane Recovery Drill

From a known-good snapshot and documented manifests/PKI, practice recovery in an isolated clone of the lab.

Measure RTO.

### Lab 59 — Platform Monitoring

Create dashboard/alert plan for:

```text
API
etcd
nodes
DNS
CNI
CSI
Pods
PVC
Ingress
certificates
```

### Lab 60 — Full Cluster Game Day

Simulate or tabletop:

1. API server down
2. etcd leader failure
3. etcd quorum loss
4. kubelet down
5. runtime down
6. CNI node failure
7. DNS outage
8. Service routing failure
9. storage attach failure
10. node memory pressure
11. node disk pressure
12. certificate expiry
13. admission webhook outage
14. bad upgrade
15. registry outage

For each:

```text
Detection
Evidence
Impact
Containment
Recovery
Verification
Prevention
```

---

## 6. Mini Project

# Mini Project — Production Kubernetes Administration Platform

Design and operate a production-style Kubernetes platform.

## Infrastructure

```text
API Load Balancer
      |
+-----+-----+-----+
|     |     |     |
cp1   cp2   cp3
|     |     |
+-- stacked etcd --+
      |
worker1
worker2
worker3
worker4
```

Or provide an external-etcd ADR explaining why.

## Required Baseline

```text
Kubernetes v1.36 line
containerd
kubeadm
multi-control-plane design
CNI with NetworkPolicy
CoreDNS
CSI
Ingress/Gateway
metrics-server
Prometheus-style monitoring
central logs
```

## Address Plan

Document:

```text
Node network
Pod CIDR
Service CIDR
LoadBalancer pool
Ingress addresses
on-prem/cloud CIDRs
DNS
```

No overlap.

## Security

Implement/design:

```text
OIDC/human identity
ServiceAccounts
least privilege RBAC
Pod Security Admission
restricted workload baseline
NetworkPolicy default deny
etcd encryption at rest
audit logging
protected kubelet
protected API
private registry
image provenance policy
```

## Storage

Define:

```text
default StorageClass
fast StorageClass
backup StorageClass if applicable
volume expansion
snapshot
reclaim policy
topology
```

## Availability

Require:

```text
3 control planes
3 etcd members
API load balancer
replicas across nodes/zones
PDBs
topology spread
tested node drain
```

## Backup / DR

Back up:

```text
etcd
PKI/config
Git manifests
CRDs
application data
registry metadata if needed
```

Define:

```text
Cluster RPO
Cluster RTO
Application RPO/RTO
restore-test frequency
```

## Upgrade Plan

Create:

```text
release assessment
API deprecation scan
add-on matrix
control-plane sequence
worker waves
verification
rollback/recovery
```

## Observability

Dashboard:

```text
API availability/latency
etcd health
node Ready
CPU/memory/disk
DNS
CNI
CSI
Pod restarts
scheduling latency
PVC status
certificate expiry
Ingress errors
```

## Required Documentation

```text
README.md
ARCHITECTURE.md
KUBEADM_CONFIG.md
NETWORK.md
CNI.md
DNS.md
STORAGE.md
SECURITY.md
RBAC.md
PKI.md
AUDIT.md
MONITORING.md
BACKUP_DR.md
UPGRADE.md
CAPACITY.md
RUNBOOKS/
ADRS/
```

## Required ADRs

```text
ADR-001-Etcd-Topology.md
ADR-002-CNI.md
ADR-003-Service-Data-Plane.md
ADR-004-Ingress-vs-Gateway.md
ADR-005-Storage.md
ADR-006-Identity.md
ADR-007-Backup-Strategy.md
ADR-008-Upgrade-Strategy.md
```

## Required Runbooks

```text
RUNBOOK_API_DOWN.md
RUNBOOK_ETCD.md
RUNBOOK_ETCD_RESTORE.md
RUNBOOK_NODE_NOTREADY.md
RUNBOOK_KUBELET.md
RUNBOOK_CONTAINERD.md
RUNBOOK_CNI.md
RUNBOOK_DNS.md
RUNBOOK_SERVICE.md
RUNBOOK_INGRESS.md
RUNBOOK_PVC_PENDING.md
RUNBOOK_VOLUME_ATTACH.md
RUNBOOK_DISK_PRESSURE.md
RUNBOOK_MEMORY_PRESSURE.md
RUNBOOK_CERTIFICATE_EXPIRY.md
RUNBOOK_WEBHOOK_OUTAGE.md
RUNBOOK_UPGRADE.md
RUNBOOK_SECURITY_INCIDENT.md
```

---

## 7. Recommended Resources

This Markdown is intended to be self-contained for study.

For production implementation use current upstream sources:

```text
Kubernetes Documentation
Kubernetes Releases
Kubernetes Cluster Architecture
kubeadm Installation
Creating a cluster with kubeadm
Upgrading kubeadm clusters
Kubernetes Version Skew Policy
Kubernetes Networking
Kubernetes Storage / CSI
Kubernetes Security
Kubernetes PKI / Certificates
Kubernetes Troubleshooting
Gateway API Documentation
Linux Foundation CKA curriculum
CNCF CKA curriculum
```

Current operational baseline:

```text
Kubernetes upstream: v1.36
Latest verified patch: v1.36.2
Current CKA environment: v1.35
```

Because the CKA environment follows upstream releases with a delay, verify the current exam page before scheduling.

---

## 8. Certification Relevance

Direct certification:

```text
Certified Kubernetes Administrator (CKA)
```

Current CKA domain weights:

```text
Cluster Architecture, Installation & Configuration    25%
Workloads & Scheduling                                 15%
Services & Networking                                  20%
Storage                                                10%
Troubleshooting                                        30%
```

The exam is currently performance-based, command-line driven, and two hours long. The current exam environment is Kubernetes v1.35, while this course uses upstream v1.36 administration.

Course emphasis intentionally mirrors the largest practical domain:

```text
Troubleshooting = 30%
```

but goes beyond CKA with deeper:

```text
HA
etcd DR
policy
audit
network internals
platform operations
fleet thinking
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Install cluster from random old blog.  
  **Best practice:** current upstream kubeadm docs and version-specific repositories.

- **Mistake:** Ignore preflight failures.  
  **Best practice:** understand every warning/error.

- **Mistake:** Mismatched cgroup drivers.  
  **Best practice:** align kubelet/runtime with systemd/cgroup v2 environment.

- **Mistake:** Overlapping Pod/Service/on-prem CIDRs.  
  **Best practice:** IPAM plan before build.

- **Mistake:** Treat API load balancer as optional in HA.  
  **Best practice:** stable highly available control-plane endpoint.

- **Mistake:** Three control planes on one physical failure domain.  
  **Best practice:** failure-domain spread.

- **Mistake:** No etcd backup.  
  **Best practice:** encrypted off-cluster snapshots + restore testing.

- **Mistake:** Snapshot exists therefore DR works.  
  **Best practice:** full restore drills including PKI/network/add-ons.

- **Mistake:** Skip Kubernetes minor version during kubeadm upgrade.  
  **Best practice:** sequential supported upgrades.

- **Mistake:** Upgrade Kubernetes without CNI/CSI compatibility check.  
  **Best practice:** add-on compatibility matrix.

- **Mistake:** `kubectl delete pod` as universal troubleshooting.  
  **Best practice:** capture evidence and identify layer.

- **Mistake:** Solve Forbidden with cluster-admin.  
  **Best practice:** `kubectl auth can-i` and least privilege.

- **Mistake:** Disable seccomp/Pod security to make workload start.  
  **Best practice:** identify exact required permission.

- **Mistake:** Assume NetworkPolicy works with any CNI.  
  **Best practice:** verify enforcement capability.

- **Mistake:** Use liveness dependent on every backend.  
  **Best practice:** separate liveness/readiness/startup.

- **Mistake:** Drain without checking PDB/local state/capacity.  
  **Best practice:** pre-maintenance checks.

- **Mistake:** Modify etcd directly.  
  **Best practice:** use Kubernetes API except documented recovery operations.

- **Mistake:** Ignore certificate expiry.  
  **Best practice:** monitor/renew before outage.

- **Mistake:** Run all system/add-on components without resource requests.  
  **Best practice:** reserve and monitor system capacity.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Current upstream course baseline?

**Answer:** Kubernetes v1.36, latest verified patch v1.36.2.

### Q2. Current CKA exam environment?

**Answer:** Kubernetes v1.35 at the time this course was prepared.

### Q3. Largest CKA domain?

**Answer:** Troubleshooting, 30%.

### Q4. kubeadm minor-version skipping supported?

**Answer:** No; upgrade sequentially.

### Q5. Core kubeadm control-plane components?

**Answer:** kube-apiserver, etcd, kube-scheduler, kube-controller-manager.

### Q6. Static Pod manifest path commonly?

**Answer:** `/etc/kubernetes/manifests`.

### Q7. kubeadm PKI path commonly?

**Answer:** `/etc/kubernetes/pki`.

### Q8. API server secure port commonly?

**Answer:** TCP 6443.

### Q9. etcd client/peer ports commonly?

**Answer:** 2379 and 2380.

### Q10. Quorum for 3-member etcd?

**Answer:** 2.

### Q11. Quorum for 5-member etcd?

**Answer:** 3.

### Q12. CRI?

**Answer:** Interface between kubelet and container runtime.

### Q13. Common runtime?

**Answer:** containerd or CRI-O.

### Q14. `crictl` purpose?

**Answer:** CRI-level runtime troubleshooting.

### Q15. CNI?

**Answer:** Pod networking plugin interface/ecosystem.

### Q16. CSI?

**Answer:** Storage plugin interface.

### Q17. CoreDNS?

**Answer:** Common Kubernetes cluster DNS add-on.

### Q18. kube-proxy?

**Answer:** Implements Service data-plane forwarding unless replaced by another compatible data plane.

### Q19. NodeLease?

**Answer:** Lightweight heartbeat object for node liveness.

### Q20. Pod CIDR vs Service CIDR?

**Answer:** Pod addresses vs virtual Service address range; must not overlap.

### Q21. PVC Pending first command?

**Answer:** `kubectl describe pvc`.

### Q22. FailedMount layer?

**Answer:** CSI/node filesystem/credentials/network mount path.

### Q23. `cordon`?

**Answer:** Prevents new Pods scheduling to Node.

### Q24. `drain`?

**Answer:** Evicts eligible Pods for maintenance.

### Q25. PDB protects from?

**Answer:** Voluntary disruptions, not node crashes.

### Q26. Node pressure conditions?

**Answer:** MemoryPressure, DiskPressure, PIDPressure.

### Q27. LimitRange?

**Answer:** Per-namespace default/min/max resource constraints.

### Q28. ResourceQuota?

**Answer:** Namespace aggregate resource/object limits.

### Q29. Pod Security Admission?

**Answer:** Built-in admission enforcement for Pod Security Standards.

### Q30. Pod Security levels?

**Answer:** Privileged, Baseline, Restricted.

### Q31. Encryption at rest?

**Answer:** API server encryption provider configuration protecting selected resource data before etcd.

### Q32. Audit policy?

**Answer:** Defines which API requests are recorded and at what detail level.

### Q33. `kubeadm certs check-expiration`?

**Answer:** Shows kubeadm-managed certificate expiry.

### Q34. API down, which tools still useful?

**Answer:** `systemctl`, `journalctl`, `crictl`, `ss`, filesystem/PKI inspection.

### Q35. etcd backup contains Secrets?

**Answer:** Yes; protect snapshot as highly sensitive.

### Q36. Service has no endpoints first check?

**Answer:** Selector, labels, readiness, EndpointSlices.

### Q37. Pod Pending first check?

**Answer:** `kubectl describe pod` scheduling events.

### Q38. CrashLoopBackOff first checks?

**Answer:** current/previous logs, describe, exit reason, probes, OOM/config.

### Q39. CNI failure common event?

**Answer:** `FailedCreatePodSandBox`.

### Q40. Good administration principle?

**Answer:** Collect evidence, identify layer, make smallest safe change, verify, document prevention.

---

# Expanded Self-Assessment Bank — Kubernetes Administration

### Q1. What is the key administrative lesson from **Control Plane vs Data Plane Failure**?

**Answer:** Do not summarize every outage as 'Kubernetes is down'.

### Q2. What is the key administrative lesson from **API Server Request Pipeline**?

**Answer:** Use the exact API error to identify the failing stage before changing policy or credentials.

### Q3. What is the key administrative lesson from **API Server Readiness**?

**Answer:** Use readiness for load-balancer backend health, not only TCP port checks.

### Q4. What is the key administrative lesson from **API Server Latency Decomposition**?

**Answer:** Investigate request class and dependency latency before scaling the API blindly.

### Q5. What is the key administrative lesson from **API Priority and Fairness**?

**Answer:** Keep system-critical API flows protected and monitor rejected/queued requests.

### Q6. What is the key administrative lesson from **Watch and Informer Failure Modes**?

**Answer:** Treat repeated watch relists as API/network pressure evidence.

### Q7. What is the key administrative lesson from **Admission Webhook Blast Radius**?

**Answer:** Make high-impact webhooks highly available, narrowly scoped, and explicitly tested for outage behavior.

### Q8. What is the key administrative lesson from **ValidatingAdmissionPolicy**?

**Answer:** Prefer built-in validation for simple deterministic policies where appropriate.

### Q9. What is the key administrative lesson from **CRD Stored Versions**?

**Answer:** Migrate stored versions before removing an old served version.

### Q10. What is the key administrative lesson from **CRD Conversion Webhook Risk**?

**Answer:** Treat conversion webhooks as control-plane dependencies.

### Q11. What is the key administrative lesson from **Finalizer Deadlock**?

**Answer:** Restore cleanup logic before manually removing finalizers.

### Q12. What is the key administrative lesson from **etcd Quorum Mathematics**?

**Answer:** Prefer 3 or 5 well-separated members rather than many correlated members.

### Q13. What is the key administrative lesson from **etcd Member Failure vs Quorum Loss**?

**Answer:** Never remove/rebuild members without first calculating quorum.

### Q14. What is the key administrative lesson from **etcd Leader Election**?

**Answer:** Do not restore from backup merely because the leader changed.

### Q15. What is the key administrative lesson from **etcd Disk Latency**?

**Answer:** Place etcd on low-latency durable storage and monitor fsync latency.

### Q16. What is the key administrative lesson from **etcd Space Quota / Alarm**?

**Answer:** Monitor etcd DB growth and perform supported compaction/defragmentation procedures.

### Q17. What is the key administrative lesson from **etcd Compaction**?

**Answer:** Follow current etcd maintenance guidance and avoid ad hoc direct file manipulation.

### Q18. What is the key administrative lesson from **etcd Defragmentation**?

**Answer:** Defragment one healthy member at a time and preserve quorum.

### Q19. What is the key administrative lesson from **etcd Snapshot Integrity**?

**Answer:** Store encrypted snapshots outside the failure domain and test restore.

### Q20. What is the key administrative lesson from **etcd Snapshot Security**?

**Answer:** Encrypt and tightly restrict snapshot storage.

### Q21. What is the key administrative lesson from **etcd Restore Isolation**?

**Answer:** Never test control-plane restore against the same live endpoints/resources unintentionally.

### Q22. What is the key administrative lesson from **Stacked vs External etcd**?

**Answer:** Document the topology in an ADR and test member replacement.

### Q23. What is the key administrative lesson from **API Load Balancer**?

**Answer:** Make the load balancer itself highly available and health-check API readiness.

### Q24. What is the key administrative lesson from **API Certificate SAN**?

**Answer:** Fix certificate identity rather than using insecure TLS bypasses.

### Q25. What is the key administrative lesson from **PKI Inventory**?

**Answer:** Maintain a documented PKI map and protected backup strategy.

### Q26. What is the key administrative lesson from **CA Private-Key Custody**?

**Answer:** Restrict CA keys and use centralized/OIDC identity for humans where possible.

### Q27. What is the key administrative lesson from **ServiceAccount Signing Keys**?

**Answer:** Protect and back up signing keys according to the recovery model.

### Q28. What is the key administrative lesson from **Certificate Expiry Monitoring**?

**Answer:** Alert on certificate expiry with enough lead time for controlled renewal.

### Q29. What is the key administrative lesson from **Leaf Certificate Renewal**?

**Answer:** Test renewal in a lab and document component reload behavior.

### Q30. What is the key administrative lesson from **CA Rotation Complexity**?

**Answer:** Plan CA rotation as a dedicated migration, not an emergency one-liner.

### Q31. What is the key administrative lesson from **kubeconfig Credential Scope**?

**Answer:** Protect privileged kubeconfigs like root credentials.

### Q32. What is the key administrative lesson from **OIDC Human Authentication**?

**Answer:** Prefer short-lived centralized human identity over static admin client certificates.

### Q33. What is the key administrative lesson from **RBAC Exact Tuple**?

**Answer:** Grant the smallest tuple that satisfies the task.

### Q34. What is the key administrative lesson from **RoleBinding to ClusterRole**?

**Answer:** Use reusable ClusterRoles with RoleBindings instead of duplicating rules where appropriate.

### Q35. What is the key administrative lesson from **ClusterRoleBinding Audit**?

**Answer:** Regularly review bindings to cluster-admin and other high-privilege roles.

### Q36. What is the key administrative lesson from **RBAC Wildcards**?

**Answer:** Avoid broad wildcards in application roles.

### Q37. What is the key administrative lesson from **Impersonation**?

**Answer:** Grant impersonation only to trusted administrators/support tooling.

### Q38. What is the key administrative lesson from **ServiceAccount Token Projection**?

**Answer:** Disable default automount where Kubernetes API access is not required.

### Q39. What is the key administrative lesson from **Node Authorizer / NodeRestriction**?

**Answer:** Protect kubelet credentials and keep node authorization restrictions enabled.

### Q40. What is the key administrative lesson from **Pod Security Admission Rollout**?

**Answer:** Use staged warn/audit → remediate → enforce.

### Q41. What is the key administrative lesson from **Restricted Pod Baseline**?

**Answer:** Create documented exception paths for infrastructure workloads.

### Q42. What is the key administrative lesson from **Encryption at Rest Provider Order**?

**Answer:** Plan key/provider rotation with explicit rewrite and rollback steps.

### Q43. What is the key administrative lesson from **Re-encryption Rewrite**?

**Answer:** Test rewrite procedures and avoid exposing Secret plaintext during migration.

### Q44. What is the key administrative lesson from **KMS Availability Dependency**?

**Answer:** Design KMS HA, latency, monitoring, and recovery before using it.

### Q45. What is the key administrative lesson from **Audit Policy Design**?

**Answer:** Balance forensic value against sensitive payload exposure and log volume.

### Q46. What is the key administrative lesson from **Audit Log Protection**?

**Answer:** Separate audit-log administration from workload administrators where possible.

### Q47. What is the key administrative lesson from **Node OS Baseline**?

**Answer:** Standardize node images/configuration and avoid snowflake workers.

### Q48. What is the key administrative lesson from **Time Synchronization**?

**Answer:** Monitor time sync as a cluster dependency.

### Q49. What is the key administrative lesson from **cgroup Driver Alignment**?

**Answer:** Use systemd cgroup integration on modern systemd-based nodes unless platform guidance says otherwise.

### Q50. What is the key administrative lesson from **Swap Policy**?

**Answer:** Follow the current Kubernetes/kubelet swap guidance for the chosen workload model.

### Q51. What is the key administrative lesson from **Kernel Module / sysctl Dependency**?

**Answer:** Use CNI/vendor-supported node settings rather than blindly copying old sysctl lists.

### Q52. What is the key administrative lesson from **Containerd CRI Health**?

**Answer:** Use crictl to validate the kubelet-facing runtime interface.

### Q53. What is the key administrative lesson from **crictl Runtime Endpoint**?

**Answer:** Standardize crictl configuration on nodes.

### Q54. What is the key administrative lesson from **CRI Sandbox Mapping**?

**Answer:** Use sandbox evidence for FailedCreatePodSandBox/CNI troubleshooting.

### Q55. What is the key administrative lesson from **Static Pod Lifecycle**?

**Answer:** Use node-local tools first during control-plane outages.

### Q56. What is the key administrative lesson from **Static Pod Manifest Safety**?

**Answer:** Keep backups outside the manifest path and make atomic reviewed changes.

### Q57. What is the key administrative lesson from **kubeadm Config as Code**?

**Answer:** Treat kubeadm config as infrastructure source, not one-time shell history.

### Q58. What is the key administrative lesson from **kubeadm Preflight**?

**Answer:** Resolve preflight causes instead of broadly ignoring them.

### Q59. What is the key administrative lesson from **Pod/Service CIDR Planning**?

**Answer:** Design IPAM before installing the CNI.

### Q60. What is the key administrative lesson from **Pod CIDR Capacity Math**?

**Answer:** Leave address headroom for growth and CNI allocation blocks.

### Q61. What is the key administrative lesson from **Service CIDR Immutability Risk**?

**Answer:** Choose Service CIDR carefully before production bootstrap.

### Q62. What is the key administrative lesson from **kubeadm Join Trust**?

**Answer:** Treat bootstrap tokens as short-lived and regenerate when needed.

### Q63. What is the key administrative lesson from **Node Name Reuse**?

**Answer:** Use replaceable node lifecycle and cleanly delete stale Node objects before reuse.

### Q64. What is the key administrative lesson from **kubeadm Reset Scope**?

**Answer:** Reimage nodes for clean reproducible rebuilds when practical.

### Q65. What is the key administrative lesson from **Air-Gapped Dependency Inventory**?

**Answer:** Test an installation with Internet physically blocked before declaring it air-gapped.

### Q66. What is the key administrative lesson from **Registry Mirror Trust**?

**Answer:** Harden mirrors with TLS, auth, retention, scanning, and monitoring.

### Q67. What is the key administrative lesson from **CNI Responsibility**?

**Answer:** Know exactly which CNI component owns IPAM, routing, and policy.

### Q68. What is the key administrative lesson from **FailedCreatePodSandBox**?

**Answer:** Do not debug application logs when the sandbox never started.

### Q69. What is the key administrative lesson from **CNI Config Inventory**?

**Answer:** Manage node CNI state declaratively through the supported add-on installer.

### Q70. What is the key administrative lesson from **Overlay MTU**?

**Answer:** Derive Pod MTU from the actual underlay and encapsulation.

### Q71. What is the key administrative lesson from **Routed/BGP CNI**?

**Answer:** Coordinate CNI routing with the data-center/cloud network team.

### Q72. What is the key administrative lesson from **eBPF Service Data Plane**?

**Answer:** Never apply kube-proxy-specific troubleshooting assumptions to a kube-proxy-free cluster.

### Q73. What is the key administrative lesson from **kube-proxy Mode**?

**Answer:** Document the Service data-plane implementation per cluster.

### Q74. What is the key administrative lesson from **Service Packet Path**?

**Answer:** Check EndpointSlices before node packet rules.

### Q75. What is the key administrative lesson from **EndpointSlice Conditions**?

**Answer:** Use endpoint conditions to explain traffic gaps during rollout.

### Q76. What is the key administrative lesson from **Conntrack Pressure**?

**Answer:** Tune conntrack only after measuring connection behavior and table pressure.

### Q77. What is the key administrative lesson from **Ephemeral Port Pressure**?

**Answer:** Use connection pooling/reuse and adequate NAT capacity.

### Q78. What is the key administrative lesson from **CoreDNS Request Path**?

**Answer:** Test `kubernetes.default` separately from external domains.

### Q79. What is the key administrative lesson from **CoreDNS ConfigMap Change Risk**?

**Answer:** Validate CoreDNS changes in a staging cluster and retain rollback.

### Q80. What is the key administrative lesson from **systemd-resolved Interaction**?

**Answer:** Configure kubelet resolvConf according to the OS/CNI guidance.

### Q81. What is the key administrative lesson from **NodeLocal DNS Cache**?

**Answer:** Monitor cache agents and preserve fallback behavior.

### Q82. What is the key administrative lesson from **NetworkPolicy Enforcement Verification**?

**Answer:** Include policy-enforcement tests in CNI upgrades.

### Q83. What is the key administrative lesson from **Default-Deny Egress**?

**Answer:** Roll out deny egress gradually with observability.

### Q84. What is the key administrative lesson from **Ingress Controller HA**?

**Answer:** Treat ingress as a production service with its own SLO.

### Q85. What is the key administrative lesson from **Ingress 502/503 Decomposition**?

**Answer:** Walk edge → route → Service → endpoint → app.

### Q86. What is the key administrative lesson from **Gateway API Ownership**?

**Answer:** Use attachment policy to preserve tenancy boundaries.

### Q87. What is the key administrative lesson from **Gateway API Status Conditions**?

**Answer:** Use status before editing DNS or load balancers.

### Q88. What is the key administrative lesson from **LoadBalancer Service on Bare Metal**?

**Answer:** Avoid assuming cloud-controller behavior exists on-premises.

### Q89. What is the key administrative lesson from **StorageClass Governance**?

**Answer:** Use deliberate defaults and document service-level characteristics.

### Q90. What is the key administrative lesson from **CSI Controller vs Node Plugin**?

**Answer:** Troubleshoot provision/attach and mount as separate CSI paths.

### Q91. What is the key administrative lesson from **PVC Pending**?

**Answer:** Read claim events before changing the workload controller.

### Q92. What is the key administrative lesson from **VolumeAttachment**?

**Answer:** Do not force-detach until the old node's write ownership is understood.

### Q93. What is the key administrative lesson from **Multi-Attach Failure**?

**Answer:** Use fencing/driver-supported detach procedures for stateful failover.

### Q94. What is the key administrative lesson from **WaitForFirstConsumer**?

**Answer:** Use WaitForFirstConsumer for zonal storage unless the driver has another documented model.

### Q95. What is the key administrative lesson from **Volume Expansion**?

**Answer:** Verify filesystem capacity inside the workload after expansion.

### Q96. What is the key administrative lesson from **Volume Snapshot Control Plane**?

**Answer:** Treat snapshots as optional CSI ecosystem functionality, not automatic core storage.

### Q97. What is the key administrative lesson from **Snapshot vs Backup**?

**Answer:** Define off-cluster/off-domain backup for critical state.

### Q98. What is the key administrative lesson from **Database Consistency**?

**Answer:** Use database-aware backup semantics.

### Q99. What is the key administrative lesson from **Reclaim Policy Risk**?

**Answer:** Require review for deletion of data-bearing PVCs/PVs.

### Q100. What is the key administrative lesson from **Node Capacity vs Allocatable**?

**Answer:** Reserve resources explicitly for the OS and Kubernetes daemons.

### Q101. What is the key administrative lesson from **kubeReserved / systemReserved**?

**Answer:** Capacity-plan the node as a system, not just a sum of Pod limits.

### Q102. What is the key administrative lesson from **Eviction Signals**?

**Answer:** Tune eviction with storage layout and workload behavior.

### Q103. What is the key administrative lesson from **DiskPressure Decomposition**?

**Answer:** Use kubelet/runtime-supported cleanup rather than deleting random runtime files.

### Q104. What is the key administrative lesson from **Image Garbage Collection**?

**Answer:** Monitor imagefs usage and keep images small/immutable.

### Q105. What is the key administrative lesson from **Container Log Rotation**?

**Answer:** Coordinate kubelet log rotation with the log collector.

### Q106. What is the key administrative lesson from **MemoryPressure**?

**Answer:** Distinguish node-level memory exhaustion from cgroup OOM.

### Q107. What is the key administrative lesson from **PIDPressure**?

**Answer:** Apply process limits and investigate process leaks/fork storms.

### Q108. What is the key administrative lesson from **Scheduling Constraint Order**?

**Answer:** Read scheduler events before changing node labels or resources.

### Q109. What is the key administrative lesson from **Capacity Fragmentation**?

**Answer:** Track large-Pod fit and consider node-pool sizing.

### Q110. What is the key administrative lesson from **Topology Spread**?

**Answer:** Test loss of a topology domain, not just normal distribution.

### Q111. What is the key administrative lesson from **PDB Semantics**?

**Answer:** Set PDBs so maintenance remains possible under realistic capacity.

### Q112. What is the key administrative lesson from **Drain Prechecks**?

**Answer:** Never run drain blindly on stateful or capacity-constrained nodes.

### Q113. What is the key administrative lesson from **Cordon vs Drain**?

**Answer:** Use cordon for immediate placement stop and drain for maintenance evacuation.

### Q114. What is the key administrative lesson from **Priority and Preemption**?

**Answer:** Reserve high priority for workloads whose importance justifies preemption.

### Q115. What is the key administrative lesson from **ResourceQuota**?

**Answer:** Use quotas to contain tenants and create predictable capacity boundaries.

### Q116. What is the key administrative lesson from **LimitRange**?

**Answer:** Pair LimitRange with quota and application right-sizing.

### Q117. What is the key administrative lesson from **HPA Request Dependency**?

**Answer:** Fix missing/incorrect requests before tuning HPA targets.

### Q118. What is the key administrative lesson from **HPA Stabilization**?

**Answer:** Tune stabilization using workload startup and traffic patterns.

### Q119. What is the key administrative lesson from **Cluster Autoscaler Interaction**?

**Answer:** Keep spare capacity or queues for traffic faster than node provisioning.

### Q120. What is the key administrative lesson from **Multi-Team Namespace Baseline**?

**Answer:** Automate namespace provisioning rather than creating empty namespaces manually.

### Q121. What is the key administrative lesson from **Node Pool Separation**?

**Answer:** Use separate pools only when the isolation/capability requirement justifies capacity fragmentation.

### Q122. What is the key administrative lesson from **Kubelet Secure Port**?

**Answer:** Restrict network access and keep anonymous/authorization settings hardened.

### Q123. What is the key administrative lesson from **Kubelet Logs**?

**Answer:** Preserve node logs before restarting kubelet.

### Q124. What is the key administrative lesson from **Runtime Logs**?

**Answer:** Use runtime evidence for CreateContainerError and image/sandbox failures.

### Q125. What is the key administrative lesson from **Control Plane without API**?

**Answer:** Practice API-down troubleshooting before an actual incident.

### Q126. What is the key administrative lesson from **Scheduler Failure**?

**Answer:** Differentiate scheduler outage from unsatisfied scheduling constraints.

### Q127. What is the key administrative lesson from **Controller Manager Failure**?

**Answer:** Expect existing Pods to run while desired-state convergence degrades.

### Q128. What is the key administrative lesson from **Kubelet Failure**?

**Answer:** Fix the node agent rather than immediately deleting workloads.

### Q129. What is the key administrative lesson from **Container Runtime Failure**?

**Answer:** Restore CRI before interpreting Pod restart failures.

### Q130. What is the key administrative lesson from **Node Lease**?

**Answer:** Check API reachability and kubelet when lease updates stop.

### Q131. What is the key administrative lesson from **Node NotReady Tree**?

**Answer:** Troubleshoot the node as a layered system.

### Q132. What is the key administrative lesson from **ImagePullBackOff Tree**?

**Answer:** Test from the affected node.

### Q133. What is the key administrative lesson from **CrashLoopBackOff Tree**?

**Answer:** Capture evidence before replacing the Pod.

### Q134. What is the key administrative lesson from **CreateContainerConfigError**?

**Answer:** Fix the referenced object rather than changing the image.

### Q135. What is the key administrative lesson from **FailedMount Tree**?

**Answer:** Follow PVC → PV → VolumeAttachment → CSI controller/node path.

### Q136. What is the key administrative lesson from **Service No Endpoints Tree**?

**Answer:** Do not restart kube-proxy before proving endpoints exist.

### Q137. What is the key administrative lesson from **Cross-Node Network Failure**?

**Answer:** Pin test Pods to different nodes and trace the packet path.

### Q138. What is the key administrative lesson from **All Pods on One Node Lose Network**?

**Answer:** Compare bad node state against a known-good node.

### Q139. What is the key administrative lesson from **DNS Local vs External Failure**?

**Answer:** Split DNS troubleshooting into internal and external branches.

### Q140. What is the key administrative lesson from **Webhook Outage Tree**?

**Answer:** Use a documented emergency policy only when a failing webhook blocks critical recovery.

### Q141. What is the key administrative lesson from **High API Error Rate**?

**Answer:** Throttle/fix the noisy client rather than only scaling the control plane.

### Q142. What is the key administrative lesson from **Cluster SLOs**?

**Answer:** Define SLOs before deciding alert thresholds.

### Q143. What is the key administrative lesson from **Prometheus Platform Metrics**?

**Answer:** Do not use metrics-server as long-term monitoring.

### Q144. What is the key administrative lesson from **kube-state-metrics**?

**Answer:** Use object metrics for controller/SLO alerts.

### Q145. What is the key administrative lesson from **Platform Alert Quality**?

**Answer:** Page on sustained actionable conditions; dashboard noisy diagnostics.

### Q146. What is the key administrative lesson from **Certificate Alerting**?

**Answer:** Monitor API, kubelet, webhook, ingress, and external certs.

### Q147. What is the key administrative lesson from **API Audit + Workload Logs Correlation**?

**Answer:** Synchronize time and centralize logs.

### Q148. What is the key administrative lesson from **Backup Scope Classification**?

**Answer:** Do not call an etcd snapshot a complete business backup.

### Q149. What is the key administrative lesson from **Rebuild vs Restore DR**?

**Answer:** Test the recovery path you expect to use under pressure.

### Q150. What is the key administrative lesson from **Cluster RPO**?

**Answer:** Do not infer application recoverability from etcd backup.

### Q151. What is the key administrative lesson from **Cluster RTO Decomposition**?

**Answer:** Measure RTO through full game days.

### Q152. What is the key administrative lesson from **Restore Test Evidence**?

**Answer:** Define a smoke-test checklist for every restore drill.

### Q153. What is the key administrative lesson from **Control Plane Failure-Domain Spread**?

**Answer:** Design HA against correlated infrastructure failures.

### Q154. What is the key administrative lesson from **Maintenance Capacity**?

**Answer:** Capacity-plan for the largest maintenance/failure scenario.

### Q155. What is the key administrative lesson from **Sequential Minor Upgrade**?

**Answer:** Never skip unsupported minors or assume downgrade is easy.

### Q156. What is the key administrative lesson from **Version Skew Matrix**?

**Answer:** Maintain a version matrix for cluster and add-ons.

### Q157. What is the key administrative lesson from **API Deprecation Scan**?

**Answer:** Treat deprecation cleanup as an upgrade prerequisite.

### Q158. What is the key administrative lesson from **CNI Compatibility Gate**?

**Answer:** Never upgrade Kubernetes without validating CNI support.

### Q159. What is the key administrative lesson from **CSI Compatibility Gate**?

**Answer:** Test attach/mount/resize/snapshot after CSI upgrades.

### Q160. What is the key administrative lesson from **CoreDNS Upgrade Gate**?

**Answer:** Test internal/external DNS after every CoreDNS change.

### Q161. What is the key administrative lesson from **Admission Controller Upgrade Gate**?

**Answer:** Canary control-plane/API changes in nonproduction first.

### Q162. What is the key administrative lesson from **Worker Upgrade Wave**?

**Answer:** Use progressive node waves with workload smoke tests.

### Q163. What is the key administrative lesson from **Node Replacement over Repair**?

**Answer:** Prefer replaceable nodes and automate bootstrap.

### Q164. What is the key administrative lesson from **Control Plane Node Replacement**?

**Answer:** Never remove multiple stacked control planes simultaneously without quorum math.

### Q165. What is the key administrative lesson from **Etcd Member Removal**?

**Answer:** Take a snapshot and verify quorum before membership changes.

### Q166. What is the key administrative lesson from **GitOps Add-on Management**?

**Answer:** Avoid two controllers/tools owning the same add-on fields.

### Q167. What is the key administrative lesson from **Fleet Upgrade Waves**?

**Answer:** Treat cluster upgrades like application releases.

### Q168. What is the key administrative lesson from **Cluster Inventory**?

**Answer:** Automate inventory collection.

### Q169. What is the key administrative lesson from **Supply-Chain Policy**?

**Answer:** Combine supply-chain policy with runtime least privilege.

### Q170. What is the key administrative lesson from **Node Image Provenance**?

**Answer:** Treat node images as immutable release artifacts.

### Q171. What is the key administrative lesson from **Runtime Socket Protection**?

**Answer:** Do not mount host runtime sockets into ordinary workloads.

### Q172. What is the key administrative lesson from **HostPath/Privileged Inventory**?

**Answer:** Keep exceptions in protected namespaces with dedicated identities and operators.

### Q173. What is the key administrative lesson from **Cloud Metadata Protection**?

**Answer:** Use cloud workload identity and metadata restrictions.

### Q174. What is the key administrative lesson from **Security Incident Containment**?

**Answer:** Prepare a Kubernetes-specific incident runbook.

### Q175. What is the key administrative lesson from **Namespace Escape Threat Model**?

**Answer:** Use dedicated clusters/nodes/sandboxed runtimes for hostile multi-tenancy when required.

### Q176. What is the key administrative lesson from **Sandboxed RuntimeClass**?

**Answer:** Use stronger isolation for untrusted workloads and account for performance/compatibility overhead.

### Q177. What is the key administrative lesson from **RuntimeClass Scheduling Overhead**?

**Answer:** Measure overhead before broad adoption.

### Q178. What is the key administrative lesson from **Cluster DNS SLO**?

**Answer:** Give CoreDNS explicit resources, spread, and PDB where appropriate.

### Q179. What is the key administrative lesson from **Service Data Plane SLO**?

**Answer:** Use synthetic checks for critical shared network paths.

### Q180. What is the key administrative lesson from **Storage SLO**?

**Answer:** Measure storage lifecycle operations and data-path health.

### Q181. What is the key administrative lesson from **Platform Capacity Forecasting**?

**Answer:** Forecast every finite resource, not just CPU and memory.

### Q182. What is the key administrative lesson from **Pod IP Exhaustion**?

**Answer:** Monitor address pools as a first-class capacity metric.

### Q183. What is the key administrative lesson from **Service IP Exhaustion**?

**Answer:** Avoid unnecessary short-lived Services and size the CIDR for fleet needs.

### Q184. What is the key administrative lesson from **Control Plane Resource Reservation**?

**Answer:** Size control planes for failure state and maintenance, not average usage.

### Q185. What is the key administrative lesson from **Admission Latency Budget**?

**Answer:** Minimize webhook scope/count and monitor webhook latency.

### Q186. What is the key administrative lesson from **Controller Storm**?

**Answer:** Use exponential backoff and rate limiting in custom controllers.

### Q187. What is the key administrative lesson from **Large Secret/ConfigMap Misuse**?

**Answer:** Use the API for desired-state metadata, not large file distribution.

### Q188. What is the key administrative lesson from **API Object Churn**?

**Answer:** Use TTL/history limits and efficient controllers for transient workloads.

### Q189. What is the key administrative lesson from **CronJob History Retention**?

**Answer:** Configure retention appropriate to audit/debug needs.

### Q190. What is the key administrative lesson from **Node Drain + Local Data**?

**Answer:** Make local-state dependencies explicit.

### Q191. What is the key administrative lesson from **Graceful Node Shutdown**?

**Answer:** Coordinate OS maintenance with kubelet graceful shutdown behavior.

### Q192. What is the key administrative lesson from **Non-Graceful Node Shutdown Recovery**?

**Answer:** Design fencing and storage behavior for hard node failure.

### Q193. What is the key administrative lesson from **Platform Runbook Structure**?

**Answer:** Test runbooks during game days.

### Q194. What is the key administrative lesson from **Game Day Design**?

**Answer:** Practice failures before production chooses the timing.

### Q195. What is the key administrative lesson from **Change Evidence Chain**?

**Answer:** Preserve change evidence for control-plane/add-on upgrades.

### Q196. What is the key administrative lesson from **Operational Readiness Review**?

**Answer:** Make operational readiness a cluster launch gate.

### Q197. What is the key administrative lesson from **Evidence-First Administration**?

**Answer:** Preserve evidence and change one variable at a time.

## Completion Checklist

- [ ] I understand production cluster architecture.
- [ ] I understand API request flow.
- [ ] I understand etcd/quorum/backup/restore.
- [ ] I can use crictl.
- [ ] I understand static Pods.
- [ ] I can prepare nodes for kubeadm.
- [ ] I can install containerd/kubeadm/kubelet/kubectl.
- [ ] I can initialize and join nodes.
- [ ] I understand HA control-plane design.
- [ ] I understand CNI and Pod networking.
- [ ] I can troubleshoot CoreDNS.
- [ ] I understand kube-proxy/Service data plane.
- [ ] I understand NetworkPolicy.
- [ ] I understand Ingress/Gateway administration.
- [ ] I understand CSI/PV/PVC/StorageClass.
- [ ] I can troubleshoot storage.
- [ ] I understand scheduling constraints.
- [ ] I can cordon/drain/uncordon.
- [ ] I understand PDB.
- [ ] I understand quotas/LimitRanges/eviction.
- [ ] I understand ServiceAccounts/RBAC.
- [ ] I understand authentication/certificates.
- [ ] I understand Pod Security Admission.
- [ ] I understand API encryption/audit.
- [ ] I can check/renew kubeadm certificates.
- [ ] I can plan and perform sequential upgrades.
- [ ] I understand version skew.
- [ ] I understand HA/DR.
- [ ] I understand cluster monitoring.
- [ ] I can troubleshoot control-plane/node/runtime/network/storage failures.
- [ ] I know current CKA domain weights.
- [ ] I completed all 60 labs.
- [ ] I completed the Production Kubernetes Administration Platform project.
