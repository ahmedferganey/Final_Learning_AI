# 57. Application Containers

> Phase 15 — Containers

This course builds the **conceptual and operating-system foundation** required before Docker and Kubernetes.

The objective is not to memorize commands. It is to understand what a container actually is, why it behaves differently from a virtual machine, how Linux creates process isolation, how images become running processes, how networking and persistent storage work, and where the real security boundaries are.

A useful mental model is:

```text
Application Source
      ↓
Build
      ↓
OCI Image
      ↓
Registry
      ↓
Pull / Unpack
      ↓
OCI Runtime Bundle
      ↓
Container Runtime
      ↓
Linux Process + Isolation + Resource Controls
```

A container is not a tiny VM.

On Linux, a container is fundamentally a process or group of processes running on the **host kernel**, combined with filesystem isolation, namespaces, cgroups, capabilities, seccomp, security modules, and runtime configuration.

---

# Current Standards Baseline

The **Open Container Initiative (OCI)** defines three core standards families:

```text
OCI Image Specification
OCI Runtime Specification
OCI Distribution Specification
```

Current reference baseline used in this material:

```text
OCI Runtime Specification: v1.3.0
OCI Image Specification: v1.1.x line
OCI Distribution Specification: v1.1.x line
```

The OCI model is:

```text
Registry
   ↓
OCI Distribution API
   ↓
OCI Image
   ↓ unpack
OCI Runtime Bundle
   ↓
Low-Level Runtime
   ↓
Container Process
```

The Runtime Specification defines how a runtime such as `runc` creates and manages the container process from a filesystem bundle and runtime configuration.

---

## 1. Topic Title

**Application Containers**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain why application containers exist.
- Explain the difference between containers, virtual machines, and ordinary processes.
- Explain kernel sharing and the resulting security/compatibility implications.
- Explain container images, layers, manifests, configuration, and content-addressability.
- Explain container registries and image distribution.
- Explain OCI Image, Runtime, and Distribution specifications.
- Explain the roles of high-level and low-level container runtimes.
- Explain `containerd`, `CRI-O`, `runc`, `crun`, Kata Containers, and gVisor conceptually.
- Explain root filesystems and copy-on-write layers.
- Explain OverlayFS at a conceptual level.
- Explain Linux namespaces.
- Explain PID, mount, network, UTS, IPC, user, time, and cgroup namespaces.
- Explain cgroups v2.
- Explain CPU, memory, PIDs, and I/O resource control.
- Explain Linux capabilities and why root inside a container is not identical to unrestricted host root.
- Explain seccomp, AppArmor, SELinux, Landlock concepts, and defense in depth.
- Explain privileged containers and why they are dangerous.
- Explain rootless containers.
- Explain user namespace remapping.
- Explain container networking fundamentals.
- Explain virtual Ethernet pairs, bridges, namespaces, routing, NAT, and port publishing.
- Explain service-to-service container communication.
- Explain container DNS/service discovery concepts.
- Explain ephemeral writable layers.
- Explain volumes, bind mounts, tmpfs, and persistent data.
- Explain secrets/configuration separation.
- Explain process lifecycle, PID 1 behavior, signals, zombie reaping, and graceful shutdown.
- Explain health checks and readiness/liveness concepts.
- Explain resource exhaustion, OOM behavior, CPU throttling, and noisy-neighbor problems.
- Explain image provenance, tags, digests, SBOMs, signatures, and supply-chain risk.
- Explain image vulnerability scanning and why scanning is not enough.
- Explain minimal images, distroless images, and multi-stage build rationale.
- Explain immutable infrastructure and disposable container principles.
- Explain stateless vs stateful workloads.
- Explain twelve-factor application practices for containers.
- Explain logging and observability expectations.
- Explain container orchestration problems that lead to Kubernetes.
- Build and inspect a container manually enough to understand the runtime model.
- Troubleshoot container startup, networking, storage, permissions, signals, and resource-limit failures.

---

## 3. Prerequisites

Required:

- Linux Essentials
- Linux System Administration I/II
- Bash
- Networking fundamentals
- Basic programming
- Git
- Web/API fundamentals

Helpful commands:

```bash
ps
top
ip
ss
mount
lsns
unshare
nsenter
cat
grep
find
systemctl
journalctl
```

A Linux VM is strongly recommended for the labs.

---

## 4. Core Concepts Explanation

# Part 1 — Why Containers Exist

Before containers, deployment often looked like:

```text
Developer Laptop
    ↓
Application + dependencies
    ↓
Different Server
    ↓
"It worked on my machine"
```

Applications depended on:

```text
OS packages
library versions
environment variables
runtime versions
directory structure
system users
```

Containers package the application and its userspace dependencies into a reproducible execution unit.

# Part 2 — Application Packaging Problem

Two applications may require incompatible dependency versions:

```text
App A → Python 3.11
App B → Python 3.13
```

Installing everything globally creates dependency conflicts.

Containers separate each application's userspace.

# Part 3 — Process Isolation

A container is still based on host processes.

From host:

```text
PID 4312 → nginx inside container
PID 4318 → app worker inside container
```

Inside the container, the same process may appear as:

```text
PID 1
```

because it has a different PID namespace.

# Part 4 — Container vs Process

An ordinary process shares the host view of:

```text
process IDs
filesystem
network
hostname
IPC
users
```

A container process receives restricted/virtualized views using namespaces plus resource/security controls.

# Part 5 — Container vs Virtual Machine

Virtual machine:

```text
Hardware
 ↓
Hypervisor
 ↓
Guest Kernel
 ↓
Guest Userspace
 ↓
Application
```

Container:

```text
Hardware
 ↓
Host Kernel
 ↓
Container Userspace
 ↓
Application
```

Containers normally share the host kernel.

# Part 6 — Kernel Sharing

Kernel sharing gives:

```text
fast startup
lower memory overhead
high density
```

but means:

```text
kernel vulnerability can affect isolation
guest kernel cannot be arbitrarily different
```

# Part 7 — Linux Containers and Windows Containers

Containers rely on OS kernel features.

Linux containers need Linux kernel semantics.

Windows containers use Windows kernel/container technology.

Running Linux containers on Windows/macOS commonly involves a lightweight Linux VM beneath the container tooling.

# Part 8 — Container Density

A VM might consume:

```text
guest kernel
system services
memory overhead
virtual hardware
```

per VM.

Containers share the kernel, allowing more workloads per host when resource limits and security permit.

# Part 9 — Startup Time

A VM often boots:

```text
firmware
kernel
init system
services
```

A container usually starts:

```text
create namespaces/cgroups
prepare filesystem
exec application process
```

which is much faster.

# Part 10 — Disposable Runtime Model

Good container workloads assume:

```text
container can disappear
container can be replaced
container hostname can change
container IP can change
```

Durable state must therefore live outside disposable writable layers.

# Part 11 — Immutable Infrastructure

Instead of:

```text
SSH into running container
apt install package
edit config
```

prefer:

```text
change source
build new image
test
deploy new image
replace old container
```

This makes runtime state reproducible.

# Part 12 — Pets vs Cattle Analogy

A pet server:

```text
named
manually repaired
long-lived
unique
```

A container workload aims toward:

```text
replaceable
reproducible
automated
scaled
```

The analogy is imperfect, but useful operationally.

# Part 13 — Stateless Workload

Stateless application:

```text
request
 ↓
any replica
 ↓
shared database/cache/object store
```

No unique state is required in one container's local writable layer.

# Part 14 — Stateful Workload

Stateful applications have durable identity/data requirements.

Examples:

```text
database
message broker
distributed storage
```

Containers can run them, but storage and lifecycle design become more complex.

# Part 15 — Twelve-Factor Influence

Container-friendly application practices include:

```text
config outside code
logs as streams
stateless processes
disposable processes
environment parity
explicit dependencies
```

# Part 16 — Container Lifecycle

Typical lifecycle:

```text
Image
 ↓ create
Created Container
 ↓ start
Running
 ↓ stop/exit
Stopped
 ↓ remove
Deleted
```

The image normally remains after a container is removed.

# Part 17 — Image vs Container

Image:

```text
immutable template
```

Container:

```text
runtime instance of image
+
writable state
+
runtime configuration
```

# Part 18 — One Image, Many Containers

```text
myapp:v1
   ├─ container A
   ├─ container B
   ├─ container C
   └─ container D
```

Each gets its own process/filesystem/network runtime state.

# Part 19 — Container Host

A container host provides:

```text
kernel
runtime
CPU/memory
network
storage
security controls
```

Host hardening is therefore critical.

# Part 20 — Container Platform Layers

A simplified stack:

```text
CLI / Orchestrator
      ↓
High-Level Runtime
      ↓
Low-Level OCI Runtime
      ↓
Linux Kernel
      ↓
Hardware
```

# Part 21 — High-Level Runtime

Examples:

```text
containerd
CRI-O
```

Responsibilities can include:

```text
image management
container lifecycle
snapshots
runtime invocation
plugin integration
```

# Part 22 — Low-Level Runtime

Examples:

```text
runc
crun
```

They take an OCI runtime bundle/config and create the isolated process.

# Part 23 — Sandboxed Runtime

Examples conceptually:

```text
gVisor
Kata Containers
```

They strengthen isolation by adding a stronger sandbox/virtualization boundary compared with ordinary shared-kernel containers.

# Part 24 — Why Orchestration Exists

One container is easy.

Thousands require:

```text
scheduling
networking
service discovery
health
restarts
updates
secrets
storage
scaling
policy
```

This leads to orchestrators such as Kubernetes.

# Part 25 — Container Mental Model

When debugging, always ask:

```text
Which process?
Which namespace?
Which cgroup?
Which filesystem?
Which network path?
Which identity?
Which capability?
Which runtime config?
```

# Part 26 — Open Container Initiative

OCI standardizes interoperability among container tools.

Core specs:

```text
Runtime
Image
Distribution
```

# Part 27 — OCI Runtime Specification

Defines:

```text
runtime configuration
filesystem bundle
container lifecycle operations
Linux/Windows/other platform-specific runtime configuration
```

Low-level runtimes implement this contract.

# Part 28 — OCI Image Specification

Defines image layout/content:

```text
manifest
config
layers
media types
digests
annotations
```

# Part 29 — OCI Distribution Specification

Defines registry API behavior for distributing content.

It standardizes how clients:

```text
push
pull
discover
manage blobs/manifests
```

# Part 30 — OCI Runtime Bundle

Runtime bundle typically contains:

```text
rootfs/
config.json
```

The low-level runtime uses these to create the container.

# Part 31 — Image Manifest

Manifest references:

```text
image config digest
layer digests
media types
```

It is the map describing an image.

# Part 32 — Image Configuration

Image config contains metadata such as:

```text
entrypoint
command
environment
working directory
user
history
rootfs diff IDs
```

# Part 33 — Image Layer

A layer is a filesystem change set.

Example:

```text
Layer 1 → base filesystem
Layer 2 → runtime packages
Layer 3 → dependencies
Layer 4 → application
```

# Part 34 — Layer Reuse

If many images share base layers:

```text
Image A ─┐
Image B ─┼→ shared base blobs
Image C ─┘
```

the registry/host can store them once.

# Part 35 — Content Addressability

Image blobs are identified by cryptographic digest.

Example concept:

```text
sha256:abcd...
```

The digest changes if content changes.

# Part 36 — Tags

Tag:

```text
myapp:latest
myapp:1.4
```

is a mutable human-friendly reference.

A tag can point to a different digest later.

# Part 37 — Digest

Digest identifies exact content.

For reproducible deployment:

```text
registry/app@sha256:...
```

is stronger than relying only on `latest`.

# Part 38 — Manifest List / Image Index

A multi-platform reference can point to different manifests:

```text
linux/amd64
linux/arm64
windows/amd64
```

Client pulls matching platform image.

# Part 39 — Multi-Architecture Image

A single image name can support multiple architectures.

This is important for:

```text
x86 servers
ARM servers
Apple Silicon development
edge devices
```

# Part 40 — Registry

A registry stores and distributes OCI image content.

Examples conceptually:

```text
Docker Hub
GitHub Container Registry
Amazon ECR
Azure Container Registry
Google Artifact Registry
Harbor
```

# Part 41 — Repository

Registry repository groups image versions:

```text
registry.example.com/team/orders
  ├─ :1.0
  ├─ :1.1
  └─ :prod
```

# Part 42 — Pull

Image pull:

```text
resolve tag
 ↓
fetch manifest
 ↓
check local blobs
 ↓
download missing layers
 ↓
verify digests
 ↓
unpack
```

# Part 43 — Push

Image push:

```text
authenticate
 ↓
upload missing blobs
 ↓
upload config
 ↓
publish manifest
```

# Part 44 — Registry Authentication

Use:

```text
short-lived token
workload identity
credential helper
```

where supported.

Avoid embedding registry passwords in build scripts.

# Part 45 — Registry Authorization

Separate permissions:

```text
pull
push
delete
admin
```

CI should not need registry admin rights.

# Part 46 — Registry Garbage Collection Concept

Deleting tags does not always immediately delete blobs.

Registry implementations can need garbage collection or lifecycle policies.

# Part 47 — Image Provenance

You should know:

```text
who built image
from which source
which commit
which builder
which dependencies
which signature/attestation
```

# Part 48 — SBOM

Software Bill of Materials lists components/packages.

Useful for:

```text
vulnerability response
license review
supply-chain visibility
```

# Part 49 — Image Signature

A signature can assert:

```text
trusted builder signed this exact digest
```

Admission/deployment policy can verify it.

# Part 50 — Attestation

Attestations can describe:

```text
build provenance
SBOM
security scan
policy result
```

They complement signatures.

# Part 51 — Image Vulnerability Scan

Scanner compares installed packages/components against vulnerability data.

A clean scan does not prove an application is secure.

# Part 52 — Scanner Limitations

Scanners may miss:

```text
application logic flaws
runtime misconfiguration
zero-days
secrets
untracked dependencies
kernel exposure
```

# Part 53 — Base Image Selection

Choose:

```text
maintained
minimal
trusted source
compatible
regularly patched
```

Do not use abandoned base images.

# Part 54 — Minimal Image

Fewer packages means:

```text
smaller download
smaller attack surface
fewer vulnerabilities
```

but debugging tools may also be absent.

# Part 55 — Distroless Image

Distroless-style images contain application/runtime dependencies but omit package manager/shell where possible.

Security benefit:

```text
smaller runtime surface
```

Operational downside:

```text
interactive debugging is harder
```

# Part 56 — Scratch Image

`scratch` represents an empty base.

Useful for static binaries.

Your binary must bring what it needs:

```text
CA certificates?
timezone?
dynamic libraries?
```

# Part 57 — Image Build Reproducibility

Pin dependencies and record build source.

Bad:

```text
install latest everything
```

Better:

```text
versioned package lock
digest-pinned critical base
repeatable builder
```

# Part 58 — Layer Secrets Risk

Deleting a secret in a later layer does not necessarily remove it from earlier image history.

Never copy secrets into build context/layers unnecessarily.

# Part 59 — Build Context

Build system receives a context containing files.

Exclude:

```text
.git secrets
keys
large artifacts
local caches
```

using ignore rules.

# Part 60 — Image Promotion

Prefer:

```text
build once
test
sign
promote exact digest
```

rather than rebuilding separately for staging and production.

# Part 61 — Container Root Filesystem

Inside container:

```text
/
├─ bin
├─ etc
├─ app
├─ lib
└─ ...
```

is a constructed root filesystem, not the host root.

# Part 62 — Mount Namespace

Mount namespace gives a process a separate view of mount points.

The container can see its rootfs while the host has a different mount tree.

# Part 63 — Pivot Root Concept

Runtime can prepare a root filesystem and change the process's root view so `/` becomes the container rootfs.

# Part 64 — Copy-on-Write

Image layers are read-only.

A running container typically gets a writable layer above them.

```text
Writable Container Layer
------------------------
App Layer
Dependency Layer
Base Layer
```

# Part 65 — OverlayFS Concept

OverlayFS combines:

```text
lowerdir → read-only image layers
upperdir → container changes
workdir  → overlay operations
merged   → final visible filesystem
```

# Part 66 — Copy-Up

If a container modifies a file from a lower layer:

```text
lower read-only file
 ↓ copy-up
upper writable layer
 ↓ modify
```

This can have performance implications.

# Part 67 — Whiteout

Deleting a file from lower image layer is represented by metadata/whiteout in the upper layer rather than modifying the immutable lower layer.

# Part 68 — Writable Layer Ephemerality

When container is deleted:

```text
writable layer
→ removed
```

unless data was stored through a persistent mount.

# Part 69 — Linux Namespace

Namespace virtualizes a view of a kernel resource for a process group.

Namespaces isolate **views**, not necessarily physical resources.

# Part 70 — PID Namespace

Provides isolated process-ID numbering.

Host:

```text
PID 5000
```

Container:

```text
PID 1
```

for the same process.

# Part 71 — Nested PID Namespaces

PID namespaces can nest.

A parent namespace can observe processes in child namespaces; child cannot see processes outside its namespace.

# Part 72 — PID 1 Special Behavior

PID 1 has special responsibilities/behavior:

```text
signal handling
orphan adoption
zombie reaping
```

Applications that ignore this can shut down poorly.

# Part 73 — UTS Namespace

Isolates:

```text
hostname
domain name
```

so each container can have its own hostname.

# Part 74 — IPC Namespace

Isolates inter-process communication resources such as:

```text
System V IPC
POSIX message queues
shared memory namespaces
```

# Part 75 — Network Namespace

Provides isolated:

```text
interfaces
routes
firewall state
ports
sockets
```

A container can have its own `eth0`.

# Part 76 — Mount Namespace

Isolates mount table.

Container can mount filesystem paths without automatically changing host mount view.

# Part 77 — User Namespace

Maps container user/group IDs to different host IDs.

Example:

```text
container UID 0
→ host UID 100000
```

This can reduce privilege risk.

# Part 78 — Cgroup Namespace

Virtualizes the process view of cgroup hierarchy.

Useful so a container sees a restricted cgroup tree instead of the host's full hierarchy.

# Part 79 — Time Namespace

Linux time namespaces can virtualize selected clocks for processes.

They are less central to everyday containers but part of modern namespace capabilities.

# Part 80 — Namespace Creation

Linux system calls/flags such as:

```text
clone()
unshare()
setns()
```

create or join namespaces.

# Part 81 — lsns

Inspect namespaces:

```bash
lsns
```

Useful columns:

```text
NS
TYPE
NPROCS
PID
COMMAND
```

# Part 82 — unshare

Create new namespace in a lab:

```bash
sudo unshare --uts --fork bash
hostname container-lab
```

Exit returns to original namespace.

# Part 83 — nsenter

Enter another process's namespaces:

```bash
sudo nsenter -t PID -n -m -p
```

Use only on authorized systems.

# Part 84 — Namespace Is Not Full Security

Namespaces isolate views.

They are not by themselves a complete security boundary.

Combine:

```text
namespaces
cgroups
capabilities
seccomp
LSM
non-root user
filesystem restrictions
```

# Part 85 — Container Escape Concept

A container escape occurs when code crosses intended isolation and affects host/other containers.

Risk increases with:

```text
privileged mode
host mounts
kernel vulnerabilities
dangerous devices
Docker socket exposure
```

# Part 86 — Host PID Namespace

Sharing host PID namespace removes PID isolation.

This can expose other processes and increase security risk.

# Part 87 — Host Network Namespace

Host networking means container uses host network stack.

Advantages:

```text
less translation
direct ports
```

Risks:

```text
port conflicts
reduced network isolation
```

# Part 88 — Host Mounts

Mounting sensitive host paths:

```text
/etc
/
 /var/run/docker.sock
```

can effectively hand host control to the container.

# Part 89 — Docker Socket Risk Concept

A process that can control the container engine socket can often create privileged containers or mount host filesystems.

Treat engine API access as highly privileged.

# Part 90 — Device Access

Containers normally have limited device access.

Granting devices can expose:

```text
GPU
block device
USB
kernel interfaces
```

and must be intentional.

# Part 91 — Proc Filesystem

`/proc` exposes kernel/process information according to namespaces and mount restrictions.

Misconfiguration can leak host details.

# Part 92 — Sysfs

`/sys` exposes kernel/device information.

Write access is highly sensitive.

# Part 93 — Read-Only Root Filesystem

For many applications:

```text
rootfs = read-only
```

plus explicit writable mounts for required paths reduces tampering.

# Part 94 — tmpfs

Memory-backed temporary filesystem.

Useful for:

```text
temporary secrets
scratch
runtime files
```

that should not persist to disk.

# Part 95 — Bind Mount

Maps host path directly:

```text
/host/data
→ /container/data
```

Powerful but couples container to host filesystem layout.

# Part 96 — Managed Volume

Runtime-managed persistent storage abstraction.

More portable than arbitrary host paths.

# Part 97 — Volume Lifecycle

Volume can outlive a container.

```text
Container A
 ↓
Volume
 ↑
Container B
```

This allows replacement without data loss.

# Part 98 — Mount Permissions

Even if mounted correctly, app can fail because of:

```text
UID/GID
mode bits
ACL
SELinux labels
read-only flag
```

# Part 99 — File Ownership and Container UID

Image may run as UID 10001.

Volume created with root ownership can cause:

```text
Permission denied
```

Plan ownership/permissions.

# Part 100 — SELinux Volume Labels Concept

On SELinux hosts, filesystem labels can block container access even when Unix permissions appear correct.

Container tooling may provide relabel options.

# Part 101 — Persistent Database Storage

Database container should use durable storage:

```text
database process
 ↓
persistent volume
```

not only writable container layer.

# Part 102 — Backup vs Volume

A volume is not a backup.

You still need:

```text
backup
retention
restore test
off-host copy
```

# Part 103 — Ephemeral Application Storage

Use local writable layer for:

```text
temporary cache
generated temporary files
```

only if loss is acceptable.

# Part 104 — Filesystem Performance

Performance depends on:

```text
storage driver
copy-on-write
host filesystem
volume type
sync behavior
workload
```

Databases often benefit from direct persistent volumes rather than CoW writable layers.

# Part 105 — Image Layer Size

Large layers increase:

```text
pull time
registry storage
build/push time
```

Keep unnecessary build artifacts out of final image.

# Part 106 — Layer Ordering

Put stable steps earlier:

```text
OS deps
language deps
application source
```

so rebuilds reuse cache effectively.

# Part 107 — Layer Squashing Concept

Squashing can reduce some layer complexity but may reduce cache/reuse advantages.

Better Dockerfile/build design is usually preferred.

# Part 108 — Filesystem Debugging

Compare:

```text
image contents
container writable changes
mounts
permissions
```

to identify why a file exists or disappeared.

# Part 109 — Mount Propagation Concept

Mount propagation controls how mount events are shared between namespaces.

Advanced container storage/infrastructure tools may require specific propagation modes.

# Part 110 — Filesystem Final Mental Model

Container filesystem is:

```text
read-only image layers
+
writable container layer
+
explicit mounts
```

Always identify which layer contains important data.

# Part 111 — Control Groups

cgroups organize processes into resource-control hierarchies.

They can:

```text
measure
limit
prioritize
control
```

resource usage.

# Part 112 — cgroups v2

Modern Linux increasingly uses the unified cgroup v2 hierarchy.

Important controllers include:

```text
cpu
memory
io
pids
cpuset
```

# Part 113 — cgroup Filesystem

Inspect:

```bash
mount | grep cgroup
cat /proc/self/cgroup
```

On v2 you commonly see a unified cgroup filesystem.

# Part 114 — Memory Limit

Without a limit, a container may consume host memory until the host is under pressure.

Set intentional memory limits.

# Part 115 — Memory OOM

If a cgroup exceeds memory constraints, kernel may invoke OOM behavior and kill a process.

Symptoms:

```text
process exits unexpectedly
exit code 137 in some tooling
OOM events/logs
```

# Part 116 — Memory Reservation Concept

Some runtimes distinguish:

```text
hard limit
soft/reservation target
```

Behavior depends on runtime/cgroup configuration.

# Part 117 — Swap

Swap configuration changes memory pressure behavior.

For latency-sensitive services, swapping may cause severe performance degradation.

Understand host/container swap policy.

# Part 118 — CPU Limit

CPU constraints can cap execution time.

Unlike memory OOM, CPU overuse often results in throttling rather than process termination.

# Part 119 — CPU Shares / Weight

Relative weight matters when CPU is contended.

It is not always an absolute CPU guarantee.

# Part 120 — CPU Quota

Quota limits CPU time per period.

Concept:

```text
0.5 CPU
2 CPUs
```

tooling translates this to cgroup settings.

# Part 121 — cpuset

Pin processes to selected CPUs.

Useful for:

```text
latency-sensitive
NUMA/HPC
specialized workloads
```

but reduces scheduler flexibility.

# Part 122 — PIDs Limit

Limit process count.

Protects against:

```text
fork bomb
runaway worker creation
```

# Part 123 — I/O Control

cgroups can regulate block I/O weight/rate depending on controller/device/runtime support.

# Part 124 — Noisy Neighbor

One container can harm others by consuming:

```text
CPU
memory
I/O
PIDs
network
```

Resource controls improve isolation.

# Part 125 — Request vs Limit Concept

Orchestrators later distinguish:

```text
requested capacity
maximum limit
```

Application Containers foundation should understand both concepts even before Kubernetes.

# Part 126 — Resource Monitoring

Monitor:

```text
CPU usage
CPU throttling
memory working set
OOM events
I/O
PIDs
```

not just whether container is "running."

# Part 127 — Overcommit

Hosts can schedule workloads whose theoretical maximum exceeds physical resources.

Benefits:

```text
higher utilization
```

risk:

```text
contention
OOM
latency
```

# Part 128 — Capacity Planning

Record:

```text
average
peak
p95/p99
startup burst
failure mode
```

before setting resource limits.

# Part 129 — Too-Low Memory Limit

Symptoms:

```text
random restarts
OOMKilled
cache instability
slow startup
```

Tune from observed working set.

# Part 130 — Too-Low CPU Limit

Symptoms:

```text
high latency
timeouts
queue buildup
CPU throttling
```

even when host has idle CPU depending on quota.

# Part 131 — Container Density Calculation

If host has:

```text
16 GiB RAM
```

and each service reliably needs:

```text
1 GiB
```

you cannot safely schedule 16 services after accounting for:

```text
OS
runtime
cache
spikes
system daemons
```

# Part 132 — Host Resource Reserve

Leave resources for:

```text
kernel
runtime
logging
monitoring
storage
network
```

Container limits do not eliminate host overhead.

# Part 133 — cgroup Delegation

Modern system managers such as systemd organize services and container runtimes inside cgroup hierarchies.

Nested delegation must follow cgroup v2 rules.

# Part 134 — systemd and Containers

Container runtime itself commonly runs under systemd.

Inspect:

```bash
systemctl status containerd
systemctl status docker
systemd-cgls
```

when debugging runtime resource hierarchy.

# Part 135 — Metrics vs Limits

A limit is policy.

A metric is evidence.

Do not choose resource limits without measuring actual application behavior.

# Part 136 — Burst Workload

Short CPU spikes may be normal.

Alert based on:

```text
latency
throttling
error rate
queue
```

rather than CPU percentage alone.

# Part 137 — Memory Leak

Container restart can hide a leak temporarily.

Correct workflow:

```text
observe growth
capture profile
identify leak
fix application
```

not "restart forever."

# Part 138 — Fork Bomb Defense

PIDs limit plus non-root/capability restrictions reduces impact of runaway process creation.

# Part 139 — Resource Denial of Service

A compromised container can attack availability by exhausting host resources.

Defense:

```text
limits
quotas
isolation
monitoring
node separation
```

# Part 140 — Kernel Memory

Not all kernel-side resource consumption maps simply to userspace RSS.

Network buffers, page cache, and kernel structures matter.

# Part 141 — Page Cache

Containers share host kernel page cache.

Memory accounting can therefore differ from naïve process-only assumptions.

# Part 142 — NUMA Concept

On large hosts, memory/CPU locality can affect performance.

High-performance container workloads may require topology-aware scheduling later in Kubernetes.

# Part 143 — Huge Pages Concept

Some high-performance applications use huge pages.

They require explicit host/runtime/orchestrator configuration.

# Part 144 — Resource Troubleshooting Order

```text
process health
CPU
memory/OOM
PIDs
disk I/O
filesystem capacity
network
dependency
```

Correlate resource metrics with application latency/errors.

# Part 145 — Resource Final Mental Model

Namespaces answer:

```text
What can the process see?
```

cgroups answer:

```text
How much can the process consume?
```

# Part 146 — Container Security Boundary

A standard Linux container is a shared-kernel isolation mechanism.

Do not assume it provides the same boundary as a full VM for every threat model.

# Part 147 — Linux Capabilities

Traditional root privileges are split into capabilities such as:

```text
CAP_NET_ADMIN
CAP_SYS_ADMIN
CAP_CHOWN
CAP_NET_BIND_SERVICE
```

Containers can drop unnecessary capabilities.

# Part 148 — Drop Capabilities

Preferred:

```text
drop all
add only required
```

where application/tooling permits.

# Part 149 — CAP_SYS_ADMIN Risk

`CAP_SYS_ADMIN` covers many powerful operations and is often described as extremely broad.

Avoid granting it casually.

# Part 150 — Non-Root User

Run application as non-root:

```text
UID 10001
```

where possible.

This limits damage from many application compromises.

# Part 151 — Root Inside Container

UID 0 inside a container may still be restricted by:

```text
namespace mapping
capabilities
seccomp
LSM
mount restrictions
```

but root remains more dangerous than a non-root process.

# Part 152 — User Namespace Remapping

Map container root to unprivileged host UID range.

This reduces consequences of filesystem/kernel boundary mistakes.

# Part 153 — Rootless Containers

Rootless runtime runs daemon/container processes without host root privileges.

Benefits:

```text
reduced daemon/runtime privilege
smaller host compromise blast radius
```

Trade-offs can exist around networking, cgroups, and privileged features.

# Part 154 — Privileged Container

Privileged mode removes many isolation restrictions and exposes devices/capabilities.

Treat it as close to host-level trust.

# Part 155 — Seccomp

Seccomp filters system calls.

Container default profiles block risky/unnecessary syscalls while allowing normal application behavior.

# Part 156 — System Call

A userspace process asks the kernel to perform privileged operations through syscalls:

```text
open
read
write
mount
clone
socket
```

Seccomp can restrict this interface.

# Part 157 — Custom Seccomp Profile

Use only when you understand application syscall needs.

Too strict:

```text
application fails
```

too broad:

```text
reduced defense
```

# Part 158 — AppArmor

Linux Security Module that applies path/capability-based mandatory access-control profiles.

Container runtimes can apply AppArmor profiles to processes.

# Part 159 — SELinux

SELinux uses labels and policy.

Container files/processes can receive confined domains/types to prevent unauthorized host access.

# Part 160 — Landlock Concept

Landlock allows unprivileged processes to restrict their own filesystem access using Linux security mechanisms.

It complements rather than replaces namespaces/cgroups/LSMs.

# Part 161 — Read-Only RootFS

Use:

```text
read-only root
+
explicit writable tmp/volume paths
```

for applications that support it.

# Part 162 — No-New-Privileges

Prevent processes from gaining additional privileges through mechanisms such as setuid execution.

Useful hardening control.

# Part 163 — Secret Injection

Secrets should not be:

```text
baked into image
committed to Git
printed to logs
placed in labels
```

Inject at runtime from a secrets system.

# Part 164 — Environment Variable Secrets

Environment variables are convenient but can leak through:

```text
process inspection
debug output
crash diagnostics
orchestration metadata
```

Prefer secret mounts/APIs when threat model requires.

# Part 165 — Image Trust Policy

A production platform can require:

```text
approved registry
signed image
known digest
scan threshold
SBOM/provenance
```

# Part 166 — Image Tag Mutation

`latest` can change.

If an attacker/repository mistake replaces the tag, deployments may pull unexpected content.

Pin digests for critical releases.

# Part 167 — Supply-Chain Attack

Attack can enter through:

```text
base image
dependency package
CI runner
registry
build tool
credentials
maintainer account
```

Secure the whole chain.

# Part 168 — Dependency Confusion

Package manager may fetch a malicious public package if naming/index rules are unsafe.

Use trusted registries and locked dependency sources.

# Part 169 — Typosquatting

A package/image name that looks similar to trusted name may be malicious.

Verify exact publisher/repository.

# Part 170 — Secrets in Image History

Even if final filesystem no longer has the secret, earlier build layer/history may.

Use secret mounts/build-secret mechanisms rather than `COPY secret`.

# Part 171 — Container Registry Security

Controls:

```text
MFA/SSO
least privilege
immutable tags
scan
signing
retention
audit
network restrictions
```

# Part 172 — Host Kernel Patching

Because containers share host kernel, host kernel vulnerabilities can affect many containers.

Patch host/runtime promptly with controlled maintenance.

# Part 173 — Runtime Patching

Update:

```text
container engine
containerd
runc/crun
BuildKit
network/storage plugins
```

for security fixes.

# Part 174 — Kernel Attack Surface

Reducing capabilities, syscalls, devices, and writable host mounts reduces ways a compromised container can reach kernel-sensitive interfaces.

# Part 175 — Side-Channel Concept

Shared CPU/cache/kernel resources create possible side-channel considerations for high-threat workloads.

Use stronger isolation or dedicated hosts when required.

# Part 176 — Sandboxed Containers

gVisor/Kata-style approaches provide additional isolation for untrusted workloads.

Trade-off:

```text
performance
compatibility
complexity
```

# Part 177 — Container vs VM Security Decision

Use stronger VM boundary when:

```text
hostile multi-tenancy
kernel isolation requirement
regulatory isolation
untrusted code
```

unless a sandboxed-container architecture satisfies the threat model.

# Part 178 — Security Context

An application's runtime security context should define:

```text
UID/GID
capabilities
read-only root
seccomp
LSM
mounts
network
resource limits
```

# Part 179 — Attack Surface Minimization

Remove:

```text
shells
compilers
package managers
debug tools
unused ports
unused capabilities
```

from production image where they are not required.

# Part 180 — Debug Without Weakening Production

Options:

```text
logs
metrics
traces
ephemeral debug container later in Kubernetes
separate debug image
reproduce in staging
```

instead of shipping every admin tool in production image.

# Part 181 — Security Logging

Record:

```text
image digest
runtime identity
privilege
network exposure
exec sessions
deployment event
```

for incident reconstruction.

# Part 182 — Policy as Code Concept

Machine-enforce rules:

```text
no privileged
non-root
approved registry
required resource limits
signed image
```

later through orchestrator/admission policy.

# Part 183 — Threat Modeling Containers

Ask:

```text
What if application is compromised?
Can it reach host?
Can it reach metadata/API?
Can it steal credentials?
Can it attack neighbors?
Can it destroy persistent data?
```

# Part 184 — Defense in Depth

```text
patched host
non-root
namespaces
cgroups
capabilities
seccomp
LSM
read-only FS
network policy
secret management
monitoring
```

No single control is enough.

# Part 185 — Security Final Mental Model

Container security is:

```text
image security
+
runtime security
+
host security
+
network security
+
identity
+
supply chain
+
operations
```

# Part 186 — Container Networking Goal

Each container needs to communicate:

```text
container ↔ container
container ↔ host
container ↔ external network
external client ↔ container
```

# Part 187 — Network Namespace Interface

A container network namespace can contain:

```text
lo
eth0
routes
ARP/neighbor table
sockets
firewall state
```

# Part 188 — veth Pair

Virtual Ethernet pair behaves like a cable:

```text
veth-host ←→ veth-container
```

One end can be placed inside container namespace.

# Part 189 — Linux Bridge

Multiple veth host ends attach to a software bridge:

```text
container A ─┐
container B ─┼→ bridge → host uplink
container C ─┘
```

# Part 190 — Container IP

Container usually receives an IP in an isolated subnet.

The IP may change when container is recreated.

Applications should not hardcode it.

# Part 191 — NAT

Outbound traffic can be source-NATed:

```text
container private IP
 ↓
host public/private IP
 ↓
external network
```

# Part 192 — Port Publishing

Expose host port to container service:

```text
host:8080
 ↓ NAT/proxy
container:80
```

Publishing changes attack surface.

# Part 193 — Bind Address

Difference:

```text
0.0.0.0:8080 → all host interfaces
127.0.0.1:8080 → local host only
```

Bind deliberately.

# Part 194 — Container-to-Container DNS

Modern container networks commonly provide name-based service discovery:

```text
app
 ↓ DNS "db"
db container
```

rather than IP hardcoding.

# Part 195 — Bridge Network Isolation

Separate application networks reduce unintended connectivity.

Example:

```text
frontend network
backend network
```

Database need not join public-facing network.

# Part 196 — Host Networking

Container uses host stack directly.

No separate container IP/port namespace.

Use only when its performance/compatibility benefits justify reduced isolation.

# Part 197 — Macvlan / Ipvlan Concept

Advanced network drivers can give containers more direct L2/L3 presence on physical network.

Operational complexity increases.

# Part 198 — Overlay Network Concept

Multi-host platforms create virtual overlay networks so workloads on different hosts communicate through an encapsulated logical network.

Kubernetes CNIs implement related multi-node networking concepts.

# Part 199 — MTU

Encapsulation can reduce usable MTU.

Symptoms of MTU mismatch:

```text
small packets work
large HTTPS transfers hang
fragmentation issues
```

# Part 200 — DNS Failure

Debug:

```text
/etc/resolv.conf
service name
network membership
DNS server reachability
search domains
```

# Part 201 — Connection Refused vs Timeout

```text
refused:
route reached destination but no listener/rejection

timeout:
packet path/firewall/service hang
```

Not absolute, but useful clue.

# Part 202 — PID 1 Signals

Container stop generally sends termination signal to PID 1.

If PID 1 ignores/does not forward it:

```text
slow shutdown
forced kill
data loss risk
```

# Part 203 — Graceful Shutdown

Application should:

```text
receive SIGTERM
stop accepting new work
finish in-flight work
close DB/queue
flush state
exit
```

# Part 204 — Zombie Processes

Parent must reap exited children.

A poorly designed PID 1 can accumulate zombies.

Tiny init processes can help for multi-process workloads.

# Part 205 — One Process per Container?

Better rule:

```text
one primary responsibility per container
```

A container may legitimately have helper processes, but avoid running a full unmanaged server OS inside one container.

# Part 206 — Entrypoint vs Command Concept

Image defines default executable and arguments.

Runtime can override them.

Understand this later in Docker:

```text
ENTRYPOINT
CMD
```

# Part 207 — Exit Code

Process exit code becomes container status.

Common:

```text
0 → success
nonzero → failure
137 → often SIGKILL/OOM context
143 → often SIGTERM context
```

Interpret with runtime logs.

# Part 208 — Restart Policy Concept

A runtime/orchestrator may restart failed containers.

Restarting helps availability but can hide root cause.

Monitor restart rate.

# Part 209 — Health Check

A process can run while application is broken.

Health check asks:

```text
Can this workload actually serve?
```

# Part 210 — Liveness vs Readiness

Later orchestrators distinguish:

```text
liveness → should process be restarted?
readiness → should traffic be sent?
```

A service may be alive but not ready.

# Part 211 — Startup Probe Concept

Slow-start applications need a startup phase so liveness checks do not kill them before initialization completes.

# Part 212 — Logging to stdout/stderr

Container-friendly app writes:

```text
stdout
stderr
```

runtime/platform collects and routes logs.

# Part 213 — Structured Logging

Prefer machine-readable fields:

```json
{
  "level":"ERROR",
  "request_id":"abc",
  "service":"orders",
  "message":"payment failed"
}
```

# Part 214 — Metrics

Monitor:

```text
requests
errors
latency
resource saturation
restarts
OOM
business KPIs
```

# Part 215 — Tracing

Distributed tracing follows one request across:

```text
gateway
service A
service B
database
queue
```

# Part 216 — Correlation ID

Propagate request ID through logs/events.

This makes multi-container debugging practical.

# Part 217 — Container Inspection

When troubleshooting, collect:

```text
image digest
command
environment
mounts
network
UID
capabilities
resource limits
logs
exit status
```

# Part 218 — Ephemeral Debugging

Do not mutate production container permanently.

Use:

```text
temporary exec
debug image
reproduce locally/staging
```

and then fix source/image.

# Part 219 — From Containers to Kubernetes

Once you need:

```text
multiple hosts
scheduling
self-healing
rolling updates
service discovery
persistent volumes
secret/config management
autoscaling
policy
```

you need orchestration.

# Part 220 — Application Containers Final Model

A production container is:

```text
trusted image digest
+
isolated process
+
explicit resource controls
+
least privilege
+
controlled network
+
external durable state
+
observable lifecycle
```

Everything else is implementation detail around this model.


# Part 221 — Deep Dive — From execve() to Container Process

Ultimately a container application becomes a normal executable started by the kernel.

Simplified:

```text
runtime
 ↓
prepare namespaces/cgroups/mounts
 ↓
configure credentials/capabilities
 ↓
execve("/app/server", ...)
 ↓
kernel loads executable
 ↓
application process runs
```

This is why ordinary Linux process-debugging tools remain valuable inside container environments.

# Part 222 — Deep Dive — What the Kernel Does Not Know

The Linux kernel does not fundamentally have one universal object called a "Docker container."

It sees:

```text
processes
namespaces
cgroups
mounts
credentials
capabilities
network devices
security labels
```

Container runtimes combine these primitives into a higher-level object.

# Part 223 — Deep Dive — Host PID Mapping

A process has a host-visible PID and potentially different namespace-visible PID.

Inspect conceptually:

```bash
ps -ef
cat /proc/HOST_PID/status
```

The `NSpid` field on supported kernels can show PID values through nested PID namespaces.

# Part 224 — Deep Dive — Namespace File Descriptors

Linux exposes namespace handles under:

```text
/proc/<pid>/ns/
```

Example:

```bash
ls -l /proc/$$/ns/
```

You may see:

```text
mnt
uts
ipc
net
pid
user
cgroup
time
```

Two processes pointing to the same namespace inode are in the same namespace instance for that type.

# Part 225 — Deep Dive — Compare Namespace Inodes

Example:

```bash
readlink /proc/1/ns/net
readlink /proc/SELF_PID/ns/net
```

Output concept:

```text
net:[4026531992]
```

The numeric inode-like identifier helps compare namespace membership.

# Part 226 — Deep Dive — Why localhost Is Per Network Namespace

`127.0.0.1` means loopback of the **current network namespace**.

Therefore:

```text
Container A localhost
≠
Container B localhost
≠
Host localhost
```

This explains one of the most common beginner networking errors.

# Part 227 — Deep Dive — Why Container Hostnames Are Cheap

UTS namespace allows each container to have:

```text
hostname=api-1
hostname=api-2
```

without changing the host.

Hostname is only one identity signal; applications should rely on service discovery rather than durable hostname assumptions.

# Part 228 — Deep Dive — Mount Namespace and chroot Difference

`chroot` changes root directory view but does not provide the full isolation model of mount namespaces.

Containers combine:

```text
mount namespace
pivot_root/chroot-like root setup
readonly layers
mount restrictions
```

with many additional kernel controls.

# Part 229 — Deep Dive — User Namespace Mapping Files

Linux user namespaces expose mappings in:

```text
/proc/<pid>/uid_map
/proc/<pid>/gid_map
```

Conceptual mapping:

```text
container IDs 0-65535
→
host IDs 100000-165535
```

This makes container-root different from host-root.

# Part 230 — Deep Dive — Why User Namespace Is Powerful

If a process escapes only its mount namespace but remains mapped to an unprivileged host UID, its host permissions can still be constrained.

User namespaces therefore add another defense layer rather than replacing other controls.

# Part 231 — Deep Dive — Cgroup v2 Unified Hierarchy

cgroup v2 uses one unified hierarchy.

Inspect:

```bash
cat /sys/fs/cgroup/cgroup.controllers
```

Possible controllers:

```text
cpu cpuset io memory pids
```

Exact controllers depend on kernel/system configuration.

# Part 232 — Deep Dive — memory.current

Inside a cgroup-v2 lab, files such as:

```text
memory.current
memory.max
memory.events
```

show usage/limit/events.

Example interpretation:

```text
memory.max = 536870912
```

means a 512 MiB hard limit.

# Part 233 — Deep Dive — memory.events

`memory.events` can expose counters such as:

```text
low
high
max
oom
oom_kill
```

This provides stronger evidence than guessing from exit code alone.

# Part 234 — Deep Dive — cpu.max

cgroup v2 CPU quota uses:

```text
cpu.max
```

Conceptually:

```text
50000 100000
```

means 50 ms CPU time every 100 ms period, approximately 0.5 CPU.

# Part 235 — Deep Dive — cpu.stat

`cpu.stat` can expose:

```text
usage_usec
user_usec
system_usec
nr_periods
nr_throttled
throttled_usec
```

A high throttled duration explains latency caused by CPU limits.

# Part 236 — Deep Dive — pids.max

PIDs controller can set:

```text
pids.max
```

and report:

```text
pids.current
```

This protects the host from runaway process creation.

# Part 237 — Deep Dive — Resource Limit vs Application Sizing

A limit should be based on workload evidence.

Example:

```text
memory p95 = 420 MiB
startup peak = 560 MiB
```

A 450 MiB hard limit guarantees startup instability despite acceptable steady-state usage.

# Part 238 — Deep Dive — CPU Saturation Queue Effect

If requests arrive faster than CPU can process:

```text
request arrival
  ↓
queue grows
  ↓
latency rises
  ↓
timeouts
```

The application may remain "healthy" while user experience fails.

# Part 239 — Deep Dive — OverlayFS Directory Example

Conceptual host layout:

```text
lower/
  app.py

upper/
  config/generated.json

work/

merged/
  app.py
  config/generated.json
```

`merged/` is the container-visible view.

# Part 240 — Deep Dive — Why chmod in a Later Layer Can Be Expensive

Changing metadata/content of large copied trees may trigger additional layer data.

Better build design sets ownership during copy when tooling supports it rather than copying then recursively changing everything.

# Part 241 — Deep Dive — Image Config Is Not Runtime State

Image config may say:

```text
USER 10001
EXPOSE 8080
CMD ...
```

Runtime can override many values.

Always inspect actual container runtime config during incidents.

# Part 242 — Deep Dive — Entrypoint Resolution

When runtime starts the container it combines:

```text
image ENTRYPOINT
image CMD
runtime command override
runtime entrypoint override
```

Incorrect assumptions cause "container immediately exits" incidents.

# Part 243 — Deep Dive — Signal Propagation Through Shell

Consider:

```text
PID 1: /bin/sh -c "python app.py"
PID 7: python app.py
```

SIGTERM sent to PID 1 may not be forwarded as expected.

Using:

```sh
exec python app.py
```

makes Python replace the shell as PID 1.

# Part 244 — Deep Dive — Zombie Process Example

A child exits but parent never calls `wait()`:

```text
parent
 └─ child [defunct]
```

Kernel retains minimal process-table entry until reaped.

At scale, poor process supervision can exhaust PID resources.

# Part 245 — Deep Dive — Readiness Failure Without Process Failure

Example:

```text
API process running
DB credentials expired
```

Liveness:

```text
healthy process
```

Readiness:

```text
not ready to serve DB-backed requests
```

Traffic should stop without necessarily restarting the process immediately.

# Part 246 — Deep Dive — Network Packet Walk

Container A to external server:

```text
app socket
 ↓
container eth0
 ↓
veth
 ↓
bridge
 ↓
host routing/firewall
 ↓
SNAT
 ↓
physical NIC
 ↓
network
```

Troubleshooting follows the same sequence.

# Part 247 — Deep Dive — Inbound Published-Port Walk

External client to container:

```text
client
 ↓
host IP:8080
 ↓
host firewall/NAT
 ↓
bridge/veth
 ↓
container IP:80
 ↓
application socket
```

Each hop can fail independently.

# Part 248 — Deep Dive — Why Container IP Is Not Service Identity

Container recreation may produce:

```text
10.0.0.12 → old
10.0.0.25 → new
```

Name/service discovery abstracts this churn.

# Part 249 — Deep Dive — ARP/Neighbor Concepts

Inside a simple bridge network, container resolves local L2 next-hop neighbors using ARP/neighbor discovery.

Inspect in authorized lab:

```bash
ip neigh
```

This helps distinguish L2 from DNS/application issues.

# Part 250 — Deep Dive — MTU Failure Pattern

Common symptom:

```text
ping small packet works
curl small page works
large TLS/download stalls
```

Investigate:

```text
underlay MTU
overlay overhead
DF bit
path MTU discovery
```

# Part 251 — Deep Dive — Volume Mount Hides Image Directory

If image has:

```text
/app/data/default.db
```

and runtime mounts an empty volume at:

```text
/app/data
```

the mount hides the image directory contents from the process.

The file is still in image layer, just obscured by mount.

# Part 252 — Deep Dive — UID Mismatch Example

Image:

```text
USER 10001
```

Host bind directory:

```text
owner UID 1000
mode 0700
```

Container writes fail because numeric IDs, not user names, determine Unix permission behavior.

# Part 253 — Deep Dive — Named Users Can Mislead

`appuser` inside image and `appuser` on host may have different numeric UIDs.

Always inspect:

```bash
id
ls -ln
```

for mount permission debugging.

# Part 254 — Deep Dive — Why Volumes Need Application-Aware Backup

Copying database files while database is actively modifying them can produce inconsistent backup.

Use:

```text
database dump
snapshot with quiescing
vendor backup tool
```

as appropriate.

# Part 255 — Deep Dive — Capabilities Example

A process binding TCP 80 historically needs privileged-port capability.

Instead of running full root:

```text
non-root UID
+
CAP_NET_BIND_SERVICE
```

can be enough where needed.

# Part 256 — Deep Dive — Capability Bounding

Linux tracks several capability sets:

```text
permitted
effective
inheritable
bounding
ambient
```

Container runtimes simplify configuration, but understanding that privileges are sets—not one root bit—improves security reasoning.

# Part 257 — Deep Dive — Seccomp Failure Symptom

If a process attempts blocked syscall, behavior depends on profile action.

Application may report:

```text
Operation not permitted
```

or terminate.

Diagnose before disabling seccomp globally.

# Part 258 — Deep Dive — AppArmor/SELinux Denial Evidence

When Unix permissions look correct but access fails, inspect host security logs:

```text
AppArmor DENIED
SELinux AVC denial
```

This prevents the common `chmod 777` anti-pattern.

# Part 259 — Deep Dive — Rootless Threat Reduction

Rootful daemon compromise:

```text
daemon root
→ host root impact possible
```

Rootless daemon compromise:

```text
daemon user
→ bounded by unprivileged host user
```

Kernel vulnerabilities can still break boundaries, so rootless is one layer, not magic.

# Part 260 — Deep Dive — Runtime Socket Threat Example

If web container can access engine socket, an attacker who compromises web app may request:

```text
new privileged container
mount /
run host command
```

Therefore socket exposure turns an application compromise into potential host compromise.

# Part 261 — Deep Dive — Image Digest Verification

When registry returns blob:

```text
sha256:X
```

client hashes received bytes.

If computed hash differs:

```text
content is rejected
```

This protects integrity, not publisher authenticity by itself.

# Part 262 — Deep Dive — Digest vs Signature

Digest proves:

```text
content did not change
```

Signature proves:

```text
trusted signer approved this digest
```

Both are useful.

# Part 263 — Deep Dive — SBOM Incident Response

A new library CVE appears.

Without SBOM:

```text
Which images contain library?
```

requires rescanning/discovery.

With SBOM index:

```text
component → images → deployments
```

response is faster.

# Part 264 — Deep Dive — Runtime Scan vs Build Scan

Build-time scan sees known vulnerabilities at build.

Runtime environment may change through:

```text
new CVEs
mounted content
downloaded plugins
config exposure
```

Continuous assessment is still needed.

# Part 265 — Deep Dive — Image Promotion by Digest

Pipeline:

```text
build digest D
 ↓
test D
 ↓
security approve D
 ↓
prod deploy D
```

This guarantees production receives the exact tested artifact.

# Part 266 — Deep Dive — Log Backpressure

If logging pipeline blocks stdout writes, some applications can slow down.

Logging architecture must consider:

```text
driver buffering
disk
network exporter
backpressure behavior
```

# Part 267 — Deep Dive — Container Clock

Containers normally use host kernel time.

If logs between containers show incorrect time, inspect:

```text
timezone presentation
host clock sync
application timezone
```

not separate container hardware clocks.

# Part 268 — Deep Dive — Process Reproduction

To reproduce a production container locally, capture:

```text
image digest
command
env names
mount structure
network ports
resource limits
UID
```

Then substitute safe test secrets.

# Part 269 — Deep Dive — Debug Image Strategy

Production image:

```text
minimal
no shell
```

Debug image:

```text
same application version
+
curl
strace
dig
shell
```

Use only in controlled troubleshooting environments.

# Part 270 — Deep Dive — Orchestrator Boundary

Docker/container runtime answers:

```text
run this container on this host
```

Orchestrator answers:

```text
which host?
how many replicas?
what if host fails?
how to update?
how to discover service?
how to attach storage?
```

This distinction is the bridge to Kubernetes.

# Part 271 — Deep Dive — CRI Concept

Kubernetes does not need Docker Engine specifically.

It interacts with container runtimes through the **Container Runtime Interface (CRI)**.

Common runtimes:

```text
containerd
CRI-O
```

then invoke OCI-compatible low-level runtimes.

# Part 272 — Deep Dive — OCI and Kubernetes Relationship

Kubernetes workload image:

```text
OCI-compatible image
 ↓
CRI runtime
 ↓
OCI runtime
 ↓
Linux process
```

Docker skills remain relevant even when Kubernetes node does not run Docker Engine.

# Part 273 — Deep Dive — ContainerD Snapshotters

High-level runtimes use snapshotter/storage components to prepare image layers and writable snapshots.

OverlayFS is a common Linux implementation, but runtime architecture supports alternatives.

# Part 274 — Deep Dive — Why Container Names Are Runtime Metadata

Kernel does not schedule a process called "orders-api-container."

That human name lives in runtime/orchestrator metadata and maps to PIDs/namespaces/cgroups.

# Part 275 — Deep Dive — Container ID

A runtime container ID is an identifier in runtime metadata.

It is not the same as:

```text
image digest
process PID
hostname
service name
```

# Part 276 — Deep Dive — Restart Loop Risk

Automatic restart can create:

```text
start
fail
restart
fail
restart
...
```

which consumes CPU/log/disk and hides root cause.

Monitor restart frequency and use backoff in orchestrators.

# Part 277 — Deep Dive — State Externalization

A horizontally scalable API should externalize:

```text
session
uploads
database
queue
cache
```

so any replica can serve the next request.

# Part 278 — Deep Dive — Sidecar Pattern Preview

Later orchestration may run helper containers alongside an app:

```text
app
+
proxy/log agent/helper
```

inside one workload unit.

The pattern is useful, but indiscriminate sidecars increase resource/operational complexity.

# Part 279 — Deep Dive — Init Container Pattern Preview

Kubernetes later supports containers that run before main application:

```text
wait for prerequisite
prepare config
run migration
```

Do not overuse them for application logic that belongs in CI/CD or service startup.

# Part 280 — Deep Dive — Container Engineering Checklist

Before calling an application "containerized", verify:

```text
reproducible image
non-root runtime
graceful signals
health endpoints
external state
resource limits
service discovery
structured logs
secret handling
image provenance
backup for persistent data
```

Containerization is an operating model, not only packaging.
---

# Supplemental Deep-Study Layer — Application Containers

> **Source distinction:** The complete uploaded Course 57 remains preserved in this enhanced file. The material below is an additional engineering layer that expands Linux/OCI internals, runtime security, cgroup v2, networking, storage consistency, supply-chain evidence, observability, and the bridge to Kubernetes. Any exact OCI/runtime/kernel version statement in the original source remains source-derived; verify live standards and kernel documentation when version-specific production behavior matters.

Preferred learning sequence:

```text
Concept
  ↓
Detailed explanation
  ↓
Linux/OCI mental model
  ↓
Command/code
  ↓
Expected evidence
  ↓
Why it works
  ↓
Production example
  ↓
Troubleshooting
  ↓
Best practice
```


## Advanced Deep Dive 1 — Kernel View of a Container

### Concept

The kernel does not manage a universal object called a container. It manages processes, credentials, namespaces, cgroups, mounts, sockets, file descriptors, capabilities, security labels, and devices. A runtime composes these primitives into the container abstraction.

### Architecture / Mental Model

```text
Application requirement
      ↓
Kernel View of a Container
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
PID=$$
printf 'PID: %s\n' "$PID"
cat /proc/$PID/status | grep -E '^(Pid|NSpid|Uid|Gid|Cap)'
ls -l /proc/$PID/ns/
cat /proc/$PID/cgroup
```

### Expected Evidence

The evidence shows process identity, namespace handles, capabilities, and cgroup membership rather than a kernel-level 'container object'.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

When troubleshooting, translate the container symptom into the underlying Linux primitive.

---

## Advanced Deep Dive 2 — clone/unshare/setns Mental Model

### Concept

Linux namespace isolation is created or joined through kernel interfaces such as clone/clone3, unshare, and setns. Runtimes automate these calls, but understanding them explains how processes enter isolated views.

### Architecture / Mental Model

```text
Application requirement
      ↓
clone/unshare/setns Mental Model
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
sudo unshare --uts --fork bash -c 'hostname ns-lab; hostname'
hostname
```

### Expected Evidence

The temporary process sees a different UTS namespace while the host hostname remains unchanged.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use namespace tools in disposable labs to understand isolation before relying on runtime abstractions.

---

## Advanced Deep Dive 3 — Namespace Lifetime

### Concept

A namespace normally remains alive while at least one process or open namespace file descriptor references it. A namespace can therefore outlive the process that originally created it if another reference is retained.

### Architecture / Mental Model

```text
Application requirement
      ↓
Namespace Lifetime
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
ls -l /proc/$$/ns/
readlink /proc/$$/ns/mnt
```

### Expected Evidence

Namespace handles are represented as inode-like references under `/proc/<pid>/ns`.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Treat namespace membership as a reference/lifecycle concept, not merely a one-time process setting.

---

## Advanced Deep Dive 4 — Namespace Inode Comparison

### Concept

Two processes are in the same namespace of a given type when their namespace handles point to the same namespace object. Comparing `/proc/<pid>/ns/*` is a direct diagnostic technique.

### Architecture / Mental Model

```text
Application requirement
      ↓
Namespace Inode Comparison
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
readlink /proc/1/ns/net
readlink /proc/$$/ns/net
readlink /proc/1/ns/mnt
readlink /proc/$$/ns/mnt
```

### Expected Evidence

Equal identifiers indicate shared namespace membership for that namespace type.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Compare namespace handles before assuming two processes share the same network or mount view.

---

## Advanced Deep Dive 5 — PID Namespace Parent Visibility

### Concept

PID namespaces are hierarchical. A parent namespace can observe processes in child PID namespaces, while child namespaces cannot see processes in the parent or sibling namespaces.

### Architecture / Mental Model

```text
Application requirement
      ↓
PID Namespace Parent Visibility
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
sudo unshare --pid --fork --mount-proc bash -c 'echo "inside"; ps -ef'
```

### Expected Evidence

The child namespace presents its own PID numbering, commonly showing the shell or init-like process as PID 1.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Remember that host administrators can generally inspect container processes even when the container cannot see host processes.

---

## Advanced Deep Dive 6 — PID 1 Signal Semantics

### Concept

PID 1 has special signal and orphan-reaping behavior. An application that becomes container PID 1 should explicitly handle termination and reap children when it spawns them.

### Architecture / Mental Model

```text
Application requirement
      ↓
PID 1 Signal Semantics
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```python
import os, signal, time
def stop(sig, frame):
    print("received", sig)
    raise SystemExit(0)
signal.signal(signal.SIGTERM, stop)
print("pid", os.getpid())
while True:
    time.sleep(1)
```

### Expected Evidence

When run as the primary process, SIGTERM produces a controlled exit rather than a forced kill.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Design the primary process for graceful termination instead of relying on SIGKILL.

---

## Advanced Deep Dive 7 — Zombie Reaping

### Concept

When a child exits, its parent must call wait/waitpid or equivalent. If the parent never reaps children, zombie process-table entries accumulate and can exhaust PID capacity.

### Architecture / Mental Model

```text
Application requirement
      ↓
Zombie Reaping
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
ps -eo pid,ppid,state,cmd | awk '$3=="Z" {print}'
```

### Expected Evidence

Zombie processes appear with state `Z` and retain a parent relationship.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use a proper application supervisor or tiny init only when the workload legitimately spawns unmanaged children.

---

## Advanced Deep Dive 8 — Mount Namespace vs chroot

### Concept

`chroot` changes path resolution but does not provide the broader mount isolation of a mount namespace. Containers combine a prepared root filesystem with mount namespaces and other controls.

### Architecture / Mental Model

```text
Application requirement
      ↓
Mount Namespace vs chroot
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS | head -30
lsns -t mnt
```

### Expected Evidence

The host exposes multiple mount namespace instances and mount trees beyond simple root-directory changes.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Never treat chroot as equivalent to container isolation.

---

## Advanced Deep Dive 9 — pivot_root Concept

### Concept

Low-level runtimes often prepare an isolated root filesystem and switch the process's mount namespace so `/` refers to that root. The exact runtime technique may use pivot_root or related mount operations.

### Architecture / Mental Model

```text
Application requirement
      ↓
pivot_root Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
host mount namespace
  ↓ create child mount namespace
mount image rootfs
  ↓
switch process root
  ↓
unmount/hide old host root
```

### Expected Evidence

The container process sees the intended root filesystem without exposing the host root by default.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Understand the root filesystem as a mount-namespace construction, not a copied mini-OS.

---

## Advanced Deep Dive 10 — Mount Propagation

### Concept

Mount propagation controls whether mount/unmount events flow between related mount namespaces. Shared, slave, private, and unbindable behavior matters for storage plugins and nested mount scenarios.

### Architecture / Mental Model

```text
Application requirement
      ↓
Mount Propagation
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
findmnt -o TARGET,PROPAGATION | head -30
```

### Expected Evidence

Each mount reports a propagation mode that affects whether future mount events propagate.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Keep default-private behavior for ordinary apps; change propagation only for infrastructure workloads that require it.

---

## Advanced Deep Dive 11 — Idmapped Mount Concept

### Concept

Modern Linux can apply UID/GID mappings to a mount without recursively changing on-disk ownership. This can improve container storage compatibility with user namespaces.

### Architecture / Mental Model

```text
Application requirement
      ↓
Idmapped Mount Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
on-disk UID 1000
   ↓ idmapped mount
container-visible UID 0 or 10001
   ↓
no recursive chown required
```

### Expected Evidence

The concept separates physical ownership from the ID view presented through a specific mount.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Prefer mapping-aware storage features over recursive ownership rewrites when the platform supports them safely.

---

## Advanced Deep Dive 12 — OverlayFS Lower/Upper/Work/Merged

### Concept

OverlayFS presents a merged view from immutable lower layers and a writable upper layer. Runtime storage drivers use this to make image layers appear as one filesystem.

### Architecture / Mental Model

```text
Application requirement
      ↓
OverlayFS Lower/Upper/Work/Merged
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
mount | grep -E 'overlay|overlayfs' || true
findmnt -t overlay -o TARGET,SOURCE,OPTIONS 2>/dev/null || true
```

### Expected Evidence

Overlay mounts show lowerdir, upperdir, workdir, and merged behavior on compatible hosts.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

When a file changes, ask whether it belongs to an image lower layer, writable upper layer, or explicit mount.

---

## Advanced Deep Dive 13 — OverlayFS Copy-Up Cost

### Concept

Modifying a file from a read-only lower layer can cause copy-up into the writable upper layer. Large write-heavy files can therefore behave poorly on the container writable layer.

### Architecture / Mental Model

```text
Application requirement
      ↓
OverlayFS Copy-Up Cost
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
lower: /var/lib/app/large.db
  ↓ first write
copy-up
  ↓
upper: full writable copy
```

### Expected Evidence

The first modification may incur extra I/O before normal writes continue.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Put write-heavy persistent state on dedicated volumes rather than the copy-on-write layer.

---

## Advanced Deep Dive 14 — Whiteouts and Deletion

### Concept

Deleting a lower-layer file does not rewrite the immutable image layer. Overlay-style filesystems record deletion metadata such as whiteouts in the upper layer.

### Architecture / Mental Model

```text
Application requirement
      ↓
Whiteouts and Deletion
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
image lower: /opt/app/debug-tool
container upper: whiteout marker
merged view: file appears deleted
```

### Expected Evidence

The original lower-layer content can still exist in the image history.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Never assume deleting a secret in a later image layer removes it from earlier layers.

---

## Advanced Deep Dive 15 — OCI Blob Digest vs Diff ID

### Concept

OCI image content uses compressed blob digests in manifests, while rootfs diff IDs represent uncompressed layer content in image configuration. These identifiers serve different integrity roles.

### Architecture / Mental Model

```text
Application requirement
      ↓
OCI Blob Digest vs Diff ID
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
manifest layer digest
  ↓ compressed blob bytes
decompress
  ↓
uncompressed filesystem tar
  ↓
config rootfs diff_id
```

### Expected Evidence

A layer can have both a distribution digest and a rootfs diff ID.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Do not confuse registry blob identity with the uncompressed rootfs change identity.

---

## Advanced Deep Dive 16 — OCI Image Index

### Concept

An OCI image index can point to multiple platform-specific manifests. The client selects the entry that matches OS, architecture, and optional variant.

### Architecture / Mental Model

```text
Application requirement
      ↓
OCI Image Index
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
app:1.2
  ↓ OCI index
  ├─ linux/amd64 → manifest A
  ├─ linux/arm64 → manifest B
  └─ windows/amd64 → manifest C
```

### Expected Evidence

One human image reference can resolve to different immutable manifests by platform.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Verify the selected platform digest during multi-architecture troubleshooting.

---

## Advanced Deep Dive 17 — OCI Artifact / Referrer Concept

### Concept

Modern OCI ecosystems can associate signatures, SBOMs, provenance, and other artifacts with an image digest without baking those documents into the runtime filesystem.

### Architecture / Mental Model

```text
Application requirement
      ↓
OCI Artifact / Referrer Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
image digest D
  ├─ signature → D
  ├─ SBOM → D
  └─ provenance → D
```

### Expected Evidence

Security metadata is bound to exact image content rather than only a mutable tag.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Anchor supply-chain evidence to immutable digests.

---

## Advanced Deep Dive 18 — Registry Pull Protocol Mental Model

### Concept

A registry pull resolves a reference, downloads manifest/index metadata, authenticates when required, fetches missing content-addressed blobs, verifies digests, and unpacks layers.

### Architecture / Mental Model

```text
Application requirement
      ↓
Registry Pull Protocol Mental Model
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
tag/digest
  ↓ GET manifest/index
  ↓ select platform
  ↓ fetch config + missing blobs
  ↓ verify sha256
  ↓ unpack
```

### Expected Evidence

Repeated pulls can reuse already-present blobs because content is addressed by digest.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Troubleshoot registry failures by separating auth, manifest resolution, blob transfer, TLS/DNS, and unpack stages.

---

## Advanced Deep Dive 19 — Registry Auth Token Flow

### Concept

Many registries use an authentication challenge followed by a token exchange scoped to repository actions such as pull or push.

### Architecture / Mental Model

```text
Application requirement
      ↓
Registry Auth Token Flow
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
client → registry
  ← 401 + auth challenge
client → token service
  ← scoped token
client → registry with token
```

### Expected Evidence

The token grants only the requested repository actions for a limited scope/time.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Prefer short-lived scoped tokens and workload identity over static registry passwords.

---

## Advanced Deep Dive 20 — Digest Integrity vs Publisher Trust

### Concept

A digest proves content integrity: the bytes match the expected hash. It does not prove that the publisher is trusted. Signatures/attestations address provenance and approval.

### Architecture / Mental Model

```text
Application requirement
      ↓
Digest Integrity vs Publisher Trust
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
digest → 'these exact bytes'
signature → 'trusted signer approved these bytes'
attestation → 'these claims apply to these bytes'
```

### Expected Evidence

Integrity, authenticity, and policy evidence are treated as separate controls.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use digests plus trusted signing/provenance policy for production releases.

---

## Advanced Deep Dive 21 — Reproducible Build Inputs

### Concept

A build is reproducible only when critical inputs are controlled: base image, package sources, dependency lock files, build toolchain, environment, and source revision.

### Architecture / Mental Model

```text
Application requirement
      ↓
Reproducible Build Inputs
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
source commit
+ locked deps
+ pinned base
+ controlled builder
+ deterministic steps
→ repeatable image
```

### Expected Evidence

Rebuilding the same release produces functionally equivalent or ideally bit-for-bit predictable output depending on the toolchain.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Record and pin inputs that materially affect the runtime artifact.

---

## Advanced Deep Dive 22 — Build Cache Poisoning Risk

### Concept

Build caches accelerate builds but are part of the supply chain. An untrusted or shared cache can inject stale or malicious outputs if cache trust is not controlled.

### Architecture / Mental Model

```text
Application requirement
      ↓
Build Cache Poisoning Risk
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
trusted CI cache
   ↓ verify scope/key
build step
   ↓
artifact
```

### Expected Evidence

Cache origin and namespace are controlled rather than blindly reused across trust boundaries.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Treat remote build cache as supply-chain infrastructure.

---

## Advanced Deep Dive 23 — SLSA / Provenance Mental Model

### Concept

Supply-chain provenance records how an artifact was built: source, builder identity, build parameters, and resulting digest. Frameworks such as SLSA help reason about provenance strength.

### Architecture / Mental Model

```text
Application requirement
      ↓
SLSA / Provenance Mental Model
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
source repo
  ↓ trusted build service
provenance statement
  ↓ binds
image digest
```

### Expected Evidence

A production artifact can be traced to a specific authorized build path.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use provenance to answer who built this image, from which source, and under which process.

---

## Advanced Deep Dive 24 — SBOM as Incident Index

### Concept

An SBOM becomes valuable when it is searchable across images and deployments. During a new CVE, operations should map component → image digest → running workload.

### Architecture / Mental Model

```text
Application requirement
      ↓
SBOM as Incident Index
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
CVE library X
  ↓ SBOM inventory
affected image digests
  ↓ deployment inventory
affected services
```

### Expected Evidence

Vulnerability response can identify impacted workloads without manually opening each image.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Store SBOMs in a searchable inventory tied to immutable digests.

---

## Advanced Deep Dive 25 — Vulnerability Scan Prioritization

### Concept

Scanner severity is only one input. Prioritize vulnerabilities using exploitability, network exposure, package reachability, privileges, business criticality, and available fix.

### Architecture / Mental Model

```text
Application requirement
      ↓
Vulnerability Scan Prioritization
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
finding
  ↓ severity
  ↓ exploit known?
  ↓ reachable in runtime?
  ↓ exposed?
  ↓ privileged?
  ↓ business criticality
```

### Expected Evidence

High-risk reachable findings are remediated before low-context noise.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use contextual risk, not raw CVE count.

---

## Advanced Deep Dive 26 — Container Root vs Host Root

### Concept

UID 0 inside a container remains powerful but can be constrained by user namespaces, capability sets, seccomp, LSMs, and mounts. Without user mapping, container root often maps to host UID 0.

### Architecture / Mental Model

```text
Application requirement
      ↓
Container Root vs Host Root
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
id
grep -E '^(Uid|Gid|Cap)' /proc/self/status
cat /proc/self/uid_map 2>/dev/null || true
```

### Expected Evidence

The numeric identity and capability state show whether container root is mapped or restricted.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Run applications as non-root even when additional isolation exists.

---

## Advanced Deep Dive 27 — User Namespace UID/GID Mapping

### Concept

User namespaces can map container IDs to unprivileged host ID ranges, reducing the impact of filesystem mistakes or partial isolation failures.

### Architecture / Mental Model

```text
Application requirement
      ↓
User Namespace UID/GID Mapping
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /proc/self/uid_map
cat /proc/self/gid_map
```

### Expected Evidence

Mappings show the container-visible ID range and corresponding host IDs.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use user namespace isolation where platform compatibility allows it.

---

## Advanced Deep Dive 28 — Rootless Runtime Architecture

### Concept

Rootless containers run the daemon/runtime and container processes under an unprivileged host user, often combining user namespaces with user-mode networking and cgroup delegation.

### Architecture / Mental Model

```text
Application requirement
      ↓
Rootless Runtime Architecture
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
host user
  ↓ rootless runtime
user namespace
  ↓
container UID 0
  maps to unprivileged host UID
```

### Expected Evidence

Compromise of the runtime is constrained by the host user's privileges rather than direct host root.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use rootless mode for appropriate workloads and understand its networking/cgroup/device limitations.

---

## Advanced Deep Dive 29 — Rootless Networking

### Concept

Rootless networking commonly uses user-space or unprivileged packet forwarding helpers because ordinary bridge/NAT setup requires host network privileges.

### Architecture / Mental Model

```text
Application requirement
      ↓
Rootless Networking
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
container netns
  ↓ user-mode forwarding
host user network
  ↓
external network
```

### Expected Evidence

Connectivity works without granting the user CAP_NET_ADMIN on the host.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Benchmark rootless networking when throughput/latency is performance-critical.

---

## Advanced Deep Dive 30 — Capabilities Sets

### Concept

Linux capabilities are tracked in several sets such as permitted, effective, inheritable, bounding, and ambient. Container runtimes present simplified add/drop controls over this model.

### Architecture / Mental Model

```text
Application requirement
      ↓
Capabilities Sets
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
grep '^Cap' /proc/self/status
command -v capsh >/dev/null && capsh --print | head -30 || true
```

### Expected Evidence

Capability bitmasks or decoded sets reveal the privileges available to the process.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Drop all capabilities by default and add only what the application requires.

---

## Advanced Deep Dive 31 — Bounding Set

### Concept

The capability bounding set limits which capabilities a process and descendants can acquire. Removing a capability from the bounding set creates a stronger ceiling than merely clearing the current effective set.

### Architecture / Mental Model

```text
Application requirement
      ↓
Bounding Set
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
grep '^CapBnd' /proc/self/status
```

### Expected Evidence

The bounding mask can differ from currently effective capabilities.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use runtime capability dropping to prevent later privilege reacquisition.

---

## Advanced Deep Dive 32 — no_new_privs

### Concept

`no_new_privs` prevents exec from granting additional privilege through setuid/setgid binaries or file capabilities, complementing capability and seccomp controls.

### Architecture / Mental Model

```text
Application requirement
      ↓
no_new_privs
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
grep '^NoNewPrivs' /proc/self/status
```

### Expected Evidence

A value of 1 indicates the process cannot gain privilege through exec transitions.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Enable no-new-privileges for ordinary application workloads where compatible.

---

## Advanced Deep Dive 33 — Seccomp Architecture

### Concept

Seccomp filters system calls at the kernel boundary. A good profile allows the application's required syscall set and blocks unnecessary high-risk kernel interfaces.

### Architecture / Mental Model

```text
Application requirement
      ↓
Seccomp Architecture
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
application
  ↓ syscall
seccomp filter
  ├─ allow
  ├─ errno
  ├─ kill
  └─ notify (advanced)
kernel
```

### Expected Evidence

Blocked syscalls produce a defined action instead of reaching the normal kernel implementation.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Diagnose exact denied syscalls before weakening the profile.

---

## Advanced Deep Dive 34 — Seccomp User Notification Concept

### Concept

Advanced seccomp modes can notify a supervisor about selected syscalls for policy decisions or emulation. This is powerful infrastructure behavior, not a normal application requirement.

### Architecture / Mental Model

```text
Application requirement
      ↓
Seccomp User Notification Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
process syscall
  ↓ seccomp notify
supervisor
  ↓ allow/emulate/deny
```

### Expected Evidence

A supervisor participates in selected syscall handling without making the workload unrestricted.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Keep advanced seccomp mediation confined to trusted sandbox/runtime infrastructure.

---

## Advanced Deep Dive 35 — AppArmor Denial Evidence

### Concept

AppArmor may deny file/capability operations even when Unix permissions appear correct. The host audit/kernel log is often the decisive evidence.

### Architecture / Mental Model

```text
Application requirement
      ↓
AppArmor Denial Evidence
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
sudo dmesg | grep -i 'apparmor.*denied' | tail -20 2>/dev/null || true
```

### Expected Evidence

Denied paths and profile names appear in audit messages on AppArmor-enabled systems.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Never respond to an LSM denial by blindly using chmod 777 or disabling confinement.

---

## Advanced Deep Dive 36 — SELinux Label Model

### Concept

SELinux authorizes interactions between labeled processes and objects. Container runtimes apply process/file types so a container cannot freely access arbitrary host paths.

### Architecture / Mental Model

```text
Application requirement
      ↓
SELinux Label Model
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
command -v getenforce >/dev/null && getenforce || true
ls -Z . 2>/dev/null | head
```

### Expected Evidence

SELinux-enabled hosts show enforcing state and security labels.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Fix labels/policy intentionally instead of disabling SELinux.

---

## Advanced Deep Dive 37 — LSM Defense in Depth

### Concept

Linux Security Modules such as SELinux or AppArmor add mandatory access controls independent of ordinary Unix ownership and container namespaces.

### Architecture / Mental Model

```text
Application requirement
      ↓
LSM Defense in Depth
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
Unix mode/ACL
  +
namespace view
  +
LSM policy
  ↓
final file/process authorization
```

### Expected Evidence

A workload can be denied even when POSIX permissions appear permissive.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Treat LSMs as an independent security layer in incident diagnosis.

---

## Advanced Deep Dive 38 — Read-Only Root Filesystem Design

### Concept

A read-only root filesystem prevents many runtime mutations. Applications should write only to explicit volumes or tmpfs paths.

### Architecture / Mental Model

```text
Application requirement
      ↓
Read-Only Root Filesystem Design
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
/            read-only
/tmp         tmpfs
/var/lib/app volume
/run         tmpfs
```

### Expected Evidence

Unexpected writes fail immediately, exposing hidden state assumptions.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Design writable paths explicitly rather than making the entire root filesystem mutable.

---

## Advanced Deep Dive 39 — tmpfs for Ephemeral Sensitive Data

### Concept

tmpfs keeps temporary data in memory-backed storage and disappears when the mount/container ends. It is useful for sensitive scratch data but still consumes memory.

### Architecture / Mental Model

```text
Application requirement
      ↓
tmpfs for Ephemeral Sensitive Data
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
mount | grep tmpfs | head
```

### Expected Evidence

tmpfs mounts are visible as memory-backed filesystems rather than persistent block storage.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use tmpfs for short-lived sensitive files when persistence is undesirable.

---

## Advanced Deep Dive 40 — Bind Mount Attack Surface

### Concept

A bind mount exposes a host path directly into the container. Write access to sensitive host directories can collapse the isolation boundary.

### Architecture / Mental Model

```text
Application requirement
      ↓
Bind Mount Attack Surface
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
host /srv/app-config
   ↓ read-only bind
container /etc/app

dangerous:
host /
   ↓ read-write
container /host
```

### Expected Evidence

Mount scope and read/write mode directly determine which host files the container can affect.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Bind only the minimum host path and prefer read-only when possible.

---

## Advanced Deep Dive 41 — Runtime Socket as Host Control Plane

### Concept

Access to a rootful container-engine socket commonly allows creation of privileged containers, device access, or host filesystem mounts. It should be treated as administrative host access.

### Architecture / Mental Model

```text
Application requirement
      ↓
Runtime Socket as Host Control Plane
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
compromised app
  ↓ engine API socket
create privileged workload
  ↓ mount host /
host compromise
```

### Expected Evidence

The runtime API can perform actions far beyond the original container's normal privileges.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Never mount the engine socket into ordinary application containers.

---

## Advanced Deep Dive 42 — Device Node Exposure

### Concept

Containers normally receive a restricted device set. Granting host devices can expose block storage, GPUs, USB, or kernel interfaces and changes the threat model.

### Architecture / Mental Model

```text
Application requirement
      ↓
Device Node Exposure
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
ls -l /dev | head -30
```

### Expected Evidence

The container or host exposes a finite list of device nodes rather than unrestricted hardware.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Grant only the exact device required and pair it with least-privilege capability/policy.

---

## Advanced Deep Dive 43 — procfs Information Exposure

### Concept

`/proc` exposes process and kernel information according to namespaces and mount options. Host PID sharing or permissive proc mounts can reveal neighboring workload details.

### Architecture / Mental Model

```text
Application requirement
      ↓
procfs Information Exposure
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
mount | grep ' on /proc '
ls /proc | head
```

### Expected Evidence

The process view depends on the active PID namespace and proc mount.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Avoid host PID namespace sharing for ordinary application workloads.

---

## Advanced Deep Dive 44 — sysfs Risk

### Concept

`/sys` exposes kernel and device state. Writable sysfs plus powerful capabilities can dramatically increase host impact.

### Architecture / Mental Model

```text
Application requirement
      ↓
sysfs Risk
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
mount | grep ' on /sys ' || true
findmnt /sys 2>/dev/null || true
```

### Expected Evidence

Mount options show whether sysfs is read-only or writable in the current environment.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Keep sysfs restricted/read-only unless trusted infrastructure software needs more.

---

## Advanced Deep Dive 45 — cgroup v2 memory.current / max

### Concept

cgroup v2 exposes current usage and hard limits through files such as memory.current and memory.max.

### Architecture / Mental Model

```text
Application requirement
      ↓
cgroup v2 memory.current / max
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
CG=/sys/fs/cgroup
cat "$CG/memory.current" 2>/dev/null || true
cat "$CG/memory.max" 2>/dev/null || true
```

### Expected Evidence

The current cgroup reports byte usage and either a numeric limit or `max`.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use cgroup counters to prove memory pressure instead of guessing from container exit code alone.

---

## Advanced Deep Dive 46 — memory.high vs memory.max

### Concept

`memory.high` is a throttling/reclaim pressure threshold while `memory.max` is a hard ceiling. This distinction lets systems pressure memory use before reaching fatal OOM behavior.

### Architecture / Mental Model

```text
Application requirement
      ↓
memory.high vs memory.max
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /sys/fs/cgroup/memory.high 2>/dev/null || true
cat /sys/fs/cgroup/memory.max 2>/dev/null || true
```

### Expected Evidence

The two controls can differ, representing soft pressure versus hard enforcement.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use memory limits from measured working-set and startup peaks, not arbitrary round numbers.

---

## Advanced Deep Dive 47 — memory.events

### Concept

cgroup v2 memory.events records evidence such as high/max/oom/oom_kill counters. It is stronger evidence than assuming exit code 137 always means OOM.

### Architecture / Mental Model

```text
Application requirement
      ↓
memory.events
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /sys/fs/cgroup/memory.events 2>/dev/null || true
```

### Expected Evidence

Counters reveal whether the cgroup actually experienced OOM or hard-limit events.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Check kernel/cgroup evidence before diagnosing memory kills.

---

## Advanced Deep Dive 48 — OOM Group Semantics Concept

### Concept

cgroup v2 can treat a workload as an OOM group so related processes are killed together instead of leaving a partially broken multi-process service.

### Architecture / Mental Model

```text
Application requirement
      ↓
OOM Group Semantics Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
service cgroup
  ├─ process A
  ├─ process B
  └─ helper
OOM group policy
  ↓
fail workload consistently
```

### Expected Evidence

The system can avoid leaving a corrupted half-alive process group after memory exhaustion.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

For tightly coupled multi-process workloads, prefer coherent failure over unpredictable partial survival.

---

## Advanced Deep Dive 49 — CPU Quota and Throttling Evidence

### Concept

`cpu.max` defines quota/period while `cpu.stat` exposes usage and throttling counters. High throttling can explain latency even when the host has spare CPU.

### Architecture / Mental Model

```text
Application requirement
      ↓
CPU Quota and Throttling Evidence
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /sys/fs/cgroup/cpu.max 2>/dev/null || true
cat /sys/fs/cgroup/cpu.stat 2>/dev/null || true
```

### Expected Evidence

The output shows quota configuration plus throttling counters such as nr_throttled/throttled_usec on supported kernels.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Correlate CPU throttling with request latency and queue buildup.

---

## Advanced Deep Dive 50 — CPU Weight vs Quota

### Concept

CPU weight is relative priority during contention; CPU quota is an absolute time ceiling over a period. They are not interchangeable.

### Architecture / Mental Model

```text
Application requirement
      ↓
CPU Weight vs Quota
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
weight:
who wins when CPU is contested

quota:
maximum CPU time per period
```

### Expected Evidence

A workload can have high relative weight yet still be capped by quota.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Choose weight for relative fairness and quota for hard containment.

---

## Advanced Deep Dive 51 — cpuset and NUMA

### Concept

CPU pinning can improve locality for specialized workloads but reduces scheduler flexibility and can interact with NUMA memory placement.

### Architecture / Mental Model

```text
Application requirement
      ↓
cpuset and NUMA
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /sys/fs/cgroup/cpuset.cpus.effective 2>/dev/null || true
lscpu | grep -E 'NUMA|CPU\(s\)'
```

### Expected Evidence

The host reports effective CPUs and NUMA topology.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use cpuset/NUMA tuning only for measured latency or HPC requirements.

---

## Advanced Deep Dive 52 — PIDs Controller

### Concept

The pids controller limits process/thread creation and protects against runaway forks. `pids.current` shows current use and `pids.max` sets the ceiling.

### Architecture / Mental Model

```text
Application requirement
      ↓
PIDs Controller
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /sys/fs/cgroup/pids.current 2>/dev/null || true
cat /sys/fs/cgroup/pids.max 2>/dev/null || true
```

### Expected Evidence

The current process count and configured limit are visible.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Set a realistic PID ceiling for services that should never create thousands of processes.

---

## Advanced Deep Dive 53 — I/O Controller Concept

### Concept

cgroup v2 can control block I/O weight and rates for supported devices. This reduces noisy-neighbor impact from write-heavy workloads.

### Architecture / Mental Model

```text
Application requirement
      ↓
I/O Controller Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /sys/fs/cgroup/io.stat 2>/dev/null | head
```

### Expected Evidence

I/O counters show bytes and operations by block device where available.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Correlate storage latency with cgroup I/O and underlying disk performance.

---

## Advanced Deep Dive 54 — Pressure Stall Information

### Concept

Linux PSI measures time workloads spend stalled on CPU, memory, or I/O pressure. PSI can reveal contention before simple utilization reaches 100%.

### Architecture / Mental Model

```text
Application requirement
      ↓
Pressure Stall Information
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

### Expected Evidence

The output reports `some` and sometimes `full` stall averages and totals.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use PSI alongside utilization to understand resource contention and saturation.

---

## Advanced Deep Dive 55 — Host Reserve

### Concept

Container limits do not reserve resources for the host kernel, runtime, logging, networking, and monitoring. Packing workloads to 100% theoretical capacity makes hosts fragile.

### Architecture / Mental Model

```text
Application requirement
      ↓
Host Reserve
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```python
host_mem_gib = 32
system_reserve = 4
workload_budget = host_mem_gib - system_reserve
print(workload_budget)
```

### Expected Evidence

The workload capacity is lower than raw host memory because system overhead is explicitly reserved.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Capacity-plan the host, not just individual containers.

---

## Advanced Deep Dive 56 — Resource Limit Startup Burst

### Concept

A service can have low steady-state memory but high startup peaks. Setting a hard limit near the steady-state average creates restart loops.

### Architecture / Mental Model

```text
Application requirement
      ↓
Resource Limit Startup Burst
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
steady p95  = 400 MiB
startup peak = 620 MiB
limit         = 450 MiB  → unstable
```

### Expected Evidence

The proposed limit is compared with both steady and startup behavior.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Measure startup, failover, and peak behavior before setting hard limits.

---

## Advanced Deep Dive 57 — Network Namespace localhost

### Concept

127.0.0.1 belongs to the current network namespace. Container A localhost is not Container B localhost or host localhost.

### Architecture / Mental Model

```text
Application requirement
      ↓
Network Namespace localhost
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
ip addr show lo
ip route
```

### Expected Evidence

Loopback and route state are local to the current network namespace.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use service DNS/IP for inter-container traffic, not localhost.

---

## Advanced Deep Dive 58 — veth Packet Path

### Concept

A typical bridge-connected container uses a veth pair to connect its network namespace to a host bridge or networking stack.

### Architecture / Mental Model

```text
Application requirement
      ↓
veth Packet Path
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
container eth0
  ↕ veth pair
host veth
  ↓ bridge
host route/NAT
  ↓ external network
```

### Expected Evidence

Each packet crosses namespace, veth, bridge, routing/firewall, and optionally NAT layers.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Troubleshoot networking hop by hop rather than changing all firewall rules.

---

## Advanced Deep Dive 59 — Conntrack / NAT State Concept

### Concept

Stateful NAT/firewalling tracks connection tuples so return traffic is translated correctly. Large connection counts can exhaust conntrack or ephemeral-port resources.

### Architecture / Mental Model

```text
Application requirement
      ↓
Conntrack / NAT State Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
sysctl net.netfilter.nf_conntrack_max 2>/dev/null || true
ss -s
```

### Expected Evidence

The host exposes connection-table capacity and socket summary on compatible systems.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Monitor connection-table and ephemeral-port pressure for high-fanout workloads.

---

## Advanced Deep Dive 60 — Ephemeral Port Exhaustion

### Concept

A client opening many short-lived outbound connections can exhaust available source ports before CPU or bandwidth saturates.

### Architecture / Mental Model

```text
Application requirement
      ↓
Ephemeral Port Exhaustion
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
sysctl net.ipv4.ip_local_port_range
ss -tan state time-wait | wc -l
```

### Expected Evidence

The port range and TIME_WAIT population provide evidence for high connection churn.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use connection pooling/reuse and tune only after measuring the real bottleneck.

---

## Advanced Deep Dive 61 — MTU and Encapsulation

### Concept

Overlay, VPN, or tunnel headers reduce payload MTU. Mismatch can allow small packets while large TLS responses stall.

### Architecture / Mental Model

```text
Application requirement
      ↓
MTU and Encapsulation
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
ip link show
ping -M do -s 1400 <AUTHORIZED_TARGET> 2>/dev/null || true
```

### Expected Evidence

Interface MTUs and path-MTU behavior can be compared on an authorized lab network.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Account for encapsulation overhead when designing container overlays.

---

## Advanced Deep Dive 62 — DNS Search Domains

### Concept

Container DNS often uses search domains and resolver options generated by the runtime. A short name may resolve differently depending on search order.

### Architecture / Mental Model

```text
Application requirement
      ↓
DNS Search Domains
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
cat /etc/resolv.conf
getent hosts localhost
```

### Expected Evidence

Resolver configuration shows nameservers, search domains, and options.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

During DNS incidents, inspect the resolver file inside the actual network namespace.

---

## Advanced Deep Dive 63 — Service Discovery vs Container IP

### Concept

A container IP is ephemeral runtime state; service identity should be represented by DNS/service discovery or an orchestrator abstraction.

### Architecture / Mental Model

```text
Application requirement
      ↓
Service Discovery vs Container IP
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
container old IP 10.1.0.7
  ↓ recreate
container new IP 10.1.0.19
service name remains stable
```

### Expected Evidence

Clients can continue resolving the service despite container replacement.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Never persist container IP addresses in application configuration.

---

## Advanced Deep Dive 64 — Volume Is Not Backup

### Concept

Persistent volumes survive container replacement but do not protect against corruption, deletion, ransomware, or storage failure.

### Architecture / Mental Model

```text
Application requirement
      ↓
Volume Is Not Backup
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
container
  ↓ volume
persistent state
  ↓ separate backup
off-host/immutable copy
  ↓ restore test
```

### Expected Evidence

The storage design distinguishes persistence from recovery.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Define backup, retention, and restore tests for every durable volume.

---

## Advanced Deep Dive 65 — Application-Consistent Volume Backup

### Concept

Copying database files while writes are active can produce an inconsistent backup. Databases need quiesce/snapshot integration or native backup/log tools.

### Architecture / Mental Model

```text
Application requirement
      ↓
Application-Consistent Volume Backup
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
DB writes
  ↓ quiesce / native backup
consistent checkpoint
  ↓ snapshot/copy
  ↓ resume
```

### Expected Evidence

Restore validation succeeds without crash-recovery or logical inconsistency surprises.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use application-aware backup mechanisms for databases and stateful services.

---

## Advanced Deep Dive 66 — Volume UID/GID Debugging

### Concept

Unix permissions use numeric UID/GID. A user named `app` inside the image can have a different numeric ID from a host user with the same name.

### Architecture / Mental Model

```text
Application requirement
      ↓
Volume UID/GID Debugging
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
id
ls -ln /path/to/mount 2>/dev/null || true
```

### Expected Evidence

Numeric IDs reveal the actual ownership relationship.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Debug mount permissions with numeric IDs before changing modes.

---

## Advanced Deep Dive 67 — Filesystem Full vs Inode Full

### Concept

A volume can fail writes because bytes are exhausted or because the filesystem has no free inodes. Both should be monitored.

### Architecture / Mental Model

```text
Application requirement
      ↓
Filesystem Full vs Inode Full
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
df -h
df -i
```

### Expected Evidence

Capacity and inode availability are inspected separately.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Alert on both byte and inode exhaustion for file-heavy workloads.

---

## Advanced Deep Dive 68 — Graceful Queue Consumer Shutdown

### Concept

A worker should stop accepting new work after SIGTERM, finish or safely return in-flight work, then exit before the orchestrator's termination deadline.

### Architecture / Mental Model

```text
Application requirement
      ↓
Graceful Queue Consumer Shutdown
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
SIGTERM
  ↓ stop fetching
  ↓ finish/rollback current message
  ↓ commit/ack if successful
  ↓ close connections
  ↓ exit
```

### Expected Evidence

No message is silently lost because the worker was killed mid-transaction.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Design shutdown semantics around the queue/database acknowledgement boundary.

---

## Advanced Deep Dive 69 — Readiness Dependency Scope

### Concept

Readiness should represent whether the instance can serve meaningful traffic. Including every optional dependency can cause cascading removal of otherwise useful capacity.

### Architecture / Mental Model

```text
Application requirement
      ↓
Readiness Dependency Scope
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
required DB unavailable → not ready
optional analytics unavailable → still ready, degrade feature
```

### Expected Evidence

Readiness reflects critical dependencies only.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Classify dependencies as required versus optional before writing health checks.

---

## Advanced Deep Dive 70 — Liveness Anti-Pattern

### Concept

A liveness probe that checks a slow remote dependency can restart healthy processes during dependency outages, worsening the incident.

### Architecture / Mental Model

```text
Application requirement
      ↓
Liveness Anti-Pattern
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
remote DB slow
  ↓ liveness checks DB
probe fails
  ↓ restart storm
  ↓ more DB reconnect load
```

### Expected Evidence

The failure mode is recognized as a self-amplifying restart loop.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use liveness for local process deadlock/failure; use readiness for serving capability.

---

## Advanced Deep Dive 71 — Structured Log Correlation

### Concept

Container logs should include stable service/version/correlation fields so events can be joined across replicas and asynchronous workers.

### Architecture / Mental Model

```text
Application requirement
      ↓
Structured Log Correlation
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```json
{"level":"ERROR","service":"orders","version":"1.8.4","request_id":"r-123","event":"db_timeout"}
```

### Expected Evidence

One user request can be reconstructed across multiple container instances.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Put high-cardinality correlation IDs in logs/traces, not metric labels.

---

## Advanced Deep Dive 72 — Metrics Cardinality

### Concept

Metric labels should remain bounded. User IDs, request IDs, random URLs, or UUIDs create excessive time-series cardinality.

### Architecture / Mental Model

```text
Application requirement
      ↓
Metrics Cardinality
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
good labels:
service, region, status, route_template

bad labels:
user_id, request_id, raw_url, uuid
```

### Expected Evidence

The metric design produces a predictable number of series.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Keep unbounded identifiers in logs/traces.

---

## Advanced Deep Dive 73 — OpenTelemetry Mental Model

### Concept

OpenTelemetry provides a vendor-neutral model for application traces, metrics, and logs instrumentation/export. It complements runtime/container metrics.

### Architecture / Mental Model

```text
Application requirement
      ↓
OpenTelemetry Mental Model
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
application instrumentation
  ↓ OTel SDK/agent
collector
  ↓
metrics backend
log backend
trace backend
```

### Expected Evidence

Application telemetry can be correlated with container runtime/resource evidence.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Instrument the service, not only the container host.

---

## Advanced Deep Dive 74 — eBPF Observability Concept

### Concept

eBPF-based tools can observe kernel events such as networking, syscalls, scheduling, and file activity with low overhead when used carefully.

### Architecture / Mental Model

```text
Application requirement
      ↓
eBPF Observability Concept
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
kernel tracepoints/kprobes
  ↓ eBPF programs
events/metrics
  ↓
network / runtime / security visibility
```

### Expected Evidence

Kernel-level telemetry can reveal behavior even when the application image is minimal.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use eBPF observability as evidence, not as a reason to weaken container isolation.

---

## Advanced Deep Dive 75 — Container Escape Threat Model

### Concept

A container escape crosses the intended isolation boundary to affect the host or other workloads. Risk grows with privileged mode, host mounts, socket exposure, kernel vulnerabilities, and powerful capabilities.

### Architecture / Mental Model

```text
Application requirement
      ↓
Container Escape Threat Model
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
app compromise
  ↓ container privileges
  ↓ kernel/runtime attack surface
escape?
  ↓
host / neighbors
```

### Expected Evidence

The threat model identifies which controls reduce blast radius after application compromise.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Assume the application can be compromised and design the runtime boundary accordingly.

---

## Advanced Deep Dive 76 — Sandboxed Runtime Trade-Off

### Concept

gVisor- or Kata-style approaches add a stronger sandbox or VM-like boundary between application and host kernel, at the cost of compatibility, performance, and operational complexity.

### Architecture / Mental Model

```text
Application requirement
      ↓
Sandboxed Runtime Trade-Off
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
ordinary container:
app → host kernel

sandboxed:
app → sandbox kernel/runtime → host
or
app → lightweight VM kernel → host
```

### Expected Evidence

The isolation model is selected based on threat level and workload compatibility.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use stronger isolation for hostile multi-tenancy or untrusted code when justified.

---

## Advanced Deep Dive 77 — CRI Bridge to Kubernetes

### Concept

Kubernetes talks to container runtimes through the Container Runtime Interface. Modern nodes typically use containerd or CRI-O rather than depending on Docker Engine itself.

### Architecture / Mental Model

```text
Application requirement
      ↓
CRI Bridge to Kubernetes
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
kubelet
  ↓ CRI
containerd / CRI-O
  ↓ OCI runtime
runc/crun/sandbox runtime
  ↓ kernel
```

### Expected Evidence

The distinction explains why Docker-built OCI images still run on Kubernetes nodes without Docker Engine.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Separate image-building knowledge from node runtime implementation.

---

## Advanced Deep Dive 78 — Pod Sandbox Concept Preview

### Concept

Kubernetes groups one or more containers into a Pod sharing selected namespaces such as network. The runtime creates a pod sandbox that provides shared network identity.

### Architecture / Mental Model

```text
Application requirement
      ↓
Pod Sandbox Concept Preview
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
Pod
  ├─ app container
  ├─ sidecar
  └─ shared network namespace
       one Pod IP
```

### Expected Evidence

Multiple containers can communicate over localhost inside the same Pod because they share networking.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Do not map the Docker 'one container = one network identity' assumption directly to Kubernetes Pods.

---

## Advanced Deep Dive 79 — CNI / CSI Preview

### Concept

Kubernetes delegates networking and storage implementation through CNI- and CSI-based ecosystems. Container fundamentals map to namespace networking and persistent mount concepts.

### Architecture / Mental Model

```text
Application requirement
      ↓
CNI / CSI Preview
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
Pod request
  ↓ CNI → network attachment
  ↓ CSI → storage attachment/mount
container runtime
```

### Expected Evidence

Networking and persistent storage are separate pluggable control paths.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Carry your namespace/route/mount mental models into Kubernetes troubleshooting.

---

## Advanced Deep Dive 80 — Sidecar Cost Model

### Concept

Sidecars share lifecycle context with an application workload but consume CPU, memory, network, logs, and failure surface. One helper per Pod can multiply platform cost.

### Architecture / Mental Model

```text
Application requirement
      ↓
Sidecar Cost Model
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```python
pods = 200
sidecar_mib = 128
print("Sidecar memory GiB:", pods * sidecar_mib / 1024)
```

### Expected Evidence

Per-Pod helper overhead is converted into fleet-level resource consumption.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Use sidecars only when their per-workload coupling is genuinely needed.

---

## Advanced Deep Dive 81 — Init Container Boundary

### Concept

Initialization steps should prepare prerequisites and then exit. Long-running business logic or schema migrations with complex rollback often belong in deployment workflows rather than every workload startup.

### Architecture / Mental Model

```text
Application requirement
      ↓
Init Container Boundary
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
init step
  ↓ success
main workload starts

failure
  ↓ main workload blocked
```

### Expected Evidence

Startup dependencies are explicit and fail before serving traffic.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Keep initialization deterministic, idempotent, and bounded.

---

## Advanced Deep Dive 82 — Immutable Release Evidence

### Concept

A production deployment record should include image digest, source commit, build identity, SBOM/provenance references, runtime security context, and configuration version.

### Architecture / Mental Model

```text
Application requirement
      ↓
Immutable Release Evidence
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
service=orders
image_digest=sha256:...
source_commit=abc123
builder=trusted-ci
config_version=42
runtime_user=10001
```

### Expected Evidence

An incident can reconstruct exactly which artifact and runtime policy were active.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Make immutable artifact identity visible in deployment and logs.

---

## Advanced Deep Dive 83 — Operational Readiness Review

### Concept

A containerized workload is not production-ready only because it starts. It needs ownership, resource sizing, graceful shutdown, health semantics, storage recovery, network policy, secrets, telemetry, and rollback.

### Architecture / Mental Model

```text
Application requirement
      ↓
Operational Readiness Review
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```text
[ ] image provenance
[ ] non-root
[ ] limits
[ ] health
[ ] graceful stop
[ ] persistent backup
[ ] secret lifecycle
[ ] logs/metrics/traces
[ ] rollback
[ ] owner/runbook
```

### Expected Evidence

The service can be operated and recovered before real users depend on it.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Make operational readiness a release gate.

---

## Advanced Deep Dive 84 — Evidence-First Container Troubleshooting

### Concept

A consistent sequence prevents random changes: identify image/runtime config, process/exit state, namespaces, cgroups, mounts, UID/capabilities, network/DNS, logs/metrics, host health, then recent changes.

### Architecture / Mental Model

```text
Application requirement
      ↓
Evidence-First Container Troubleshooting
      ↓
Linux / OCI / Runtime primitive
      ↓
Observable evidence
      ↓
Production decision
```

### Command / Code / Configuration

```bash
ps -ef
lsns
cat /proc/self/cgroup
ip addr
ip route
df -h
cat /proc/pressure/memory
```

### Expected Evidence

The failing Linux/runtime layer is identified before remediation.

### Why It Works

Containers are composed from ordinary operating-system primitives. The runtime prepares process credentials, namespaces, mounts, cgroups, security controls, and networking before executing the application. Troubleshooting becomes reliable when the high-level container symptom is translated into the underlying primitive and verified from evidence.

### Production Example

For a production service, document how this topic affects the image, runtime identity, resource limits, filesystem, network path, persistent data, security boundary, observability, and recovery behavior. Link the decision to the exact image digest and deployment configuration.

### Troubleshooting Workflow

```text
Reproduce safely
   ↓
Identify process + image digest
   ↓
Inspect namespace / cgroup / mount / identity
   ↓
Inspect network / DNS / storage
   ↓
Inspect kernel/runtime/application evidence
   ↓
Change one controlled setting
   ↓
Verify
   ↓
Prevent recurrence
```

### Common Mistakes

- Treating a container as a miniature virtual machine.
- Debugging by permanently mutating a running container.
- Granting privileged mode or host mounts to bypass a narrow permission problem.
- Assuming a volume is a backup.
- Using `latest` instead of immutable artifact identity.
- Setting resource limits without measuring startup and peak behavior.

### Best Practice

Change one layer at a time and preserve the evidence that justified the change.

---

# Supplemental Hands-on Lab Series — Application Containers

## Enhanced Lab 1 — Kernel View of a Container

### Objective

Turn **Kernel View of a Container** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
PID=$$
printf 'PID: %s\n' "$PID"
cat /proc/$PID/status | grep -E '^(Pid|NSpid|Uid|Gid|Cap)'
ls -l /proc/$PID/ns/
cat /proc/$PID/cgroup
```

### Expected Result

The evidence shows process identity, namespace handles, capabilities, and cgroup membership rather than a kernel-level 'container object'.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

When troubleshooting, translate the container symptom into the underlying Linux primitive.

---

## Enhanced Lab 2 — clone/unshare/setns Mental Model

### Objective

Turn **clone/unshare/setns Mental Model** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
sudo unshare --uts --fork bash -c 'hostname ns-lab; hostname'
hostname
```

### Expected Result

The temporary process sees a different UTS namespace while the host hostname remains unchanged.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use namespace tools in disposable labs to understand isolation before relying on runtime abstractions.

---

## Enhanced Lab 3 — Namespace Lifetime

### Objective

Turn **Namespace Lifetime** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
ls -l /proc/$$/ns/
readlink /proc/$$/ns/mnt
```

### Expected Result

Namespace handles are represented as inode-like references under `/proc/<pid>/ns`.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat namespace membership as a reference/lifecycle concept, not merely a one-time process setting.

---

## Enhanced Lab 4 — Namespace Inode Comparison

### Objective

Turn **Namespace Inode Comparison** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
readlink /proc/1/ns/net
readlink /proc/$$/ns/net
readlink /proc/1/ns/mnt
readlink /proc/$$/ns/mnt
```

### Expected Result

Equal identifiers indicate shared namespace membership for that namespace type.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Compare namespace handles before assuming two processes share the same network or mount view.

---

## Enhanced Lab 5 — PID Namespace Parent Visibility

### Objective

Turn **PID Namespace Parent Visibility** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
sudo unshare --pid --fork --mount-proc bash -c 'echo "inside"; ps -ef'
```

### Expected Result

The child namespace presents its own PID numbering, commonly showing the shell or init-like process as PID 1.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Remember that host administrators can generally inspect container processes even when the container cannot see host processes.

---

## Enhanced Lab 6 — PID 1 Signal Semantics

### Objective

Turn **PID 1 Signal Semantics** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```python
import os, signal, time
def stop(sig, frame):
    print("received", sig)
    raise SystemExit(0)
signal.signal(signal.SIGTERM, stop)
print("pid", os.getpid())
while True:
    time.sleep(1)
```

### Expected Result

When run as the primary process, SIGTERM produces a controlled exit rather than a forced kill.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Design the primary process for graceful termination instead of relying on SIGKILL.

---

## Enhanced Lab 7 — Zombie Reaping

### Objective

Turn **Zombie Reaping** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
ps -eo pid,ppid,state,cmd | awk '$3=="Z" {print}'
```

### Expected Result

Zombie processes appear with state `Z` and retain a parent relationship.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use a proper application supervisor or tiny init only when the workload legitimately spawns unmanaged children.

---

## Enhanced Lab 8 — Mount Namespace vs chroot

### Objective

Turn **Mount Namespace vs chroot** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS | head -30
lsns -t mnt
```

### Expected Result

The host exposes multiple mount namespace instances and mount trees beyond simple root-directory changes.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never treat chroot as equivalent to container isolation.

---

## Enhanced Lab 9 — pivot_root Concept

### Objective

Turn **pivot_root Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
host mount namespace
  ↓ create child mount namespace
mount image rootfs
  ↓
switch process root
  ↓
unmount/hide old host root
```

### Expected Result

The container process sees the intended root filesystem without exposing the host root by default.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Understand the root filesystem as a mount-namespace construction, not a copied mini-OS.

---

## Enhanced Lab 10 — Mount Propagation

### Objective

Turn **Mount Propagation** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
findmnt -o TARGET,PROPAGATION | head -30
```

### Expected Result

Each mount reports a propagation mode that affects whether future mount events propagate.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep default-private behavior for ordinary apps; change propagation only for infrastructure workloads that require it.

---

## Enhanced Lab 11 — Idmapped Mount Concept

### Objective

Turn **Idmapped Mount Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
on-disk UID 1000
   ↓ idmapped mount
container-visible UID 0 or 10001
   ↓
no recursive chown required
```

### Expected Result

The concept separates physical ownership from the ID view presented through a specific mount.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer mapping-aware storage features over recursive ownership rewrites when the platform supports them safely.

---

## Enhanced Lab 12 — OverlayFS Lower/Upper/Work/Merged

### Objective

Turn **OverlayFS Lower/Upper/Work/Merged** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
mount | grep -E 'overlay|overlayfs' || true
findmnt -t overlay -o TARGET,SOURCE,OPTIONS 2>/dev/null || true
```

### Expected Result

Overlay mounts show lowerdir, upperdir, workdir, and merged behavior on compatible hosts.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

When a file changes, ask whether it belongs to an image lower layer, writable upper layer, or explicit mount.

---

## Enhanced Lab 13 — OverlayFS Copy-Up Cost

### Objective

Turn **OverlayFS Copy-Up Cost** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
lower: /var/lib/app/large.db
  ↓ first write
copy-up
  ↓
upper: full writable copy
```

### Expected Result

The first modification may incur extra I/O before normal writes continue.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Put write-heavy persistent state on dedicated volumes rather than the copy-on-write layer.

---

## Enhanced Lab 14 — Whiteouts and Deletion

### Objective

Turn **Whiteouts and Deletion** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
image lower: /opt/app/debug-tool
container upper: whiteout marker
merged view: file appears deleted
```

### Expected Result

The original lower-layer content can still exist in the image history.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never assume deleting a secret in a later image layer removes it from earlier layers.

---

## Enhanced Lab 15 — OCI Blob Digest vs Diff ID

### Objective

Turn **OCI Blob Digest vs Diff ID** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
manifest layer digest
  ↓ compressed blob bytes
decompress
  ↓
uncompressed filesystem tar
  ↓
config rootfs diff_id
```

### Expected Result

A layer can have both a distribution digest and a rootfs diff ID.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not confuse registry blob identity with the uncompressed rootfs change identity.

---

## Enhanced Lab 16 — OCI Image Index

### Objective

Turn **OCI Image Index** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
app:1.2
  ↓ OCI index
  ├─ linux/amd64 → manifest A
  ├─ linux/arm64 → manifest B
  └─ windows/amd64 → manifest C
```

### Expected Result

One human image reference can resolve to different immutable manifests by platform.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Verify the selected platform digest during multi-architecture troubleshooting.

---

## Enhanced Lab 17 — OCI Artifact / Referrer Concept

### Objective

Turn **OCI Artifact / Referrer Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
image digest D
  ├─ signature → D
  ├─ SBOM → D
  └─ provenance → D
```

### Expected Result

Security metadata is bound to exact image content rather than only a mutable tag.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Anchor supply-chain evidence to immutable digests.

---

## Enhanced Lab 18 — Registry Pull Protocol Mental Model

### Objective

Turn **Registry Pull Protocol Mental Model** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
tag/digest
  ↓ GET manifest/index
  ↓ select platform
  ↓ fetch config + missing blobs
  ↓ verify sha256
  ↓ unpack
```

### Expected Result

Repeated pulls can reuse already-present blobs because content is addressed by digest.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Troubleshoot registry failures by separating auth, manifest resolution, blob transfer, TLS/DNS, and unpack stages.

---

## Enhanced Lab 19 — Registry Auth Token Flow

### Objective

Turn **Registry Auth Token Flow** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
client → registry
  ← 401 + auth challenge
client → token service
  ← scoped token
client → registry with token
```

### Expected Result

The token grants only the requested repository actions for a limited scope/time.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer short-lived scoped tokens and workload identity over static registry passwords.

---

## Enhanced Lab 20 — Digest Integrity vs Publisher Trust

### Objective

Turn **Digest Integrity vs Publisher Trust** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
digest → 'these exact bytes'
signature → 'trusted signer approved these bytes'
attestation → 'these claims apply to these bytes'
```

### Expected Result

Integrity, authenticity, and policy evidence are treated as separate controls.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use digests plus trusted signing/provenance policy for production releases.

---

## Enhanced Lab 21 — Reproducible Build Inputs

### Objective

Turn **Reproducible Build Inputs** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
source commit
+ locked deps
+ pinned base
+ controlled builder
+ deterministic steps
→ repeatable image
```

### Expected Result

Rebuilding the same release produces functionally equivalent or ideally bit-for-bit predictable output depending on the toolchain.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Record and pin inputs that materially affect the runtime artifact.

---

## Enhanced Lab 22 — Build Cache Poisoning Risk

### Objective

Turn **Build Cache Poisoning Risk** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
trusted CI cache
   ↓ verify scope/key
build step
   ↓
artifact
```

### Expected Result

Cache origin and namespace are controlled rather than blindly reused across trust boundaries.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat remote build cache as supply-chain infrastructure.

---

## Enhanced Lab 23 — SLSA / Provenance Mental Model

### Objective

Turn **SLSA / Provenance Mental Model** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
source repo
  ↓ trusted build service
provenance statement
  ↓ binds
image digest
```

### Expected Result

A production artifact can be traced to a specific authorized build path.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use provenance to answer who built this image, from which source, and under which process.

---

## Enhanced Lab 24 — SBOM as Incident Index

### Objective

Turn **SBOM as Incident Index** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
CVE library X
  ↓ SBOM inventory
affected image digests
  ↓ deployment inventory
affected services
```

### Expected Result

Vulnerability response can identify impacted workloads without manually opening each image.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Store SBOMs in a searchable inventory tied to immutable digests.

---

## Enhanced Lab 25 — Vulnerability Scan Prioritization

### Objective

Turn **Vulnerability Scan Prioritization** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
finding
  ↓ severity
  ↓ exploit known?
  ↓ reachable in runtime?
  ↓ exposed?
  ↓ privileged?
  ↓ business criticality
```

### Expected Result

High-risk reachable findings are remediated before low-context noise.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use contextual risk, not raw CVE count.

---

## Enhanced Lab 26 — Container Root vs Host Root

### Objective

Turn **Container Root vs Host Root** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
id
grep -E '^(Uid|Gid|Cap)' /proc/self/status
cat /proc/self/uid_map 2>/dev/null || true
```

### Expected Result

The numeric identity and capability state show whether container root is mapped or restricted.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Run applications as non-root even when additional isolation exists.

---

## Enhanced Lab 27 — User Namespace UID/GID Mapping

### Objective

Turn **User Namespace UID/GID Mapping** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /proc/self/uid_map
cat /proc/self/gid_map
```

### Expected Result

Mappings show the container-visible ID range and corresponding host IDs.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use user namespace isolation where platform compatibility allows it.

---

## Enhanced Lab 28 — Rootless Runtime Architecture

### Objective

Turn **Rootless Runtime Architecture** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
host user
  ↓ rootless runtime
user namespace
  ↓
container UID 0
  maps to unprivileged host UID
```

### Expected Result

Compromise of the runtime is constrained by the host user's privileges rather than direct host root.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use rootless mode for appropriate workloads and understand its networking/cgroup/device limitations.

---

## Enhanced Lab 29 — Rootless Networking

### Objective

Turn **Rootless Networking** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
container netns
  ↓ user-mode forwarding
host user network
  ↓
external network
```

### Expected Result

Connectivity works without granting the user CAP_NET_ADMIN on the host.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Benchmark rootless networking when throughput/latency is performance-critical.

---

## Enhanced Lab 30 — Capabilities Sets

### Objective

Turn **Capabilities Sets** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
grep '^Cap' /proc/self/status
command -v capsh >/dev/null && capsh --print | head -30 || true
```

### Expected Result

Capability bitmasks or decoded sets reveal the privileges available to the process.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Drop all capabilities by default and add only what the application requires.

---

## Enhanced Lab 31 — Bounding Set

### Objective

Turn **Bounding Set** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
grep '^CapBnd' /proc/self/status
```

### Expected Result

The bounding mask can differ from currently effective capabilities.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use runtime capability dropping to prevent later privilege reacquisition.

---

## Enhanced Lab 32 — no_new_privs

### Objective

Turn **no_new_privs** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
grep '^NoNewPrivs' /proc/self/status
```

### Expected Result

A value of 1 indicates the process cannot gain privilege through exec transitions.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Enable no-new-privileges for ordinary application workloads where compatible.

---

## Enhanced Lab 33 — Seccomp Architecture

### Objective

Turn **Seccomp Architecture** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
application
  ↓ syscall
seccomp filter
  ├─ allow
  ├─ errno
  ├─ kill
  └─ notify (advanced)
kernel
```

### Expected Result

Blocked syscalls produce a defined action instead of reaching the normal kernel implementation.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Diagnose exact denied syscalls before weakening the profile.

---

## Enhanced Lab 34 — Seccomp User Notification Concept

### Objective

Turn **Seccomp User Notification Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
process syscall
  ↓ seccomp notify
supervisor
  ↓ allow/emulate/deny
```

### Expected Result

A supervisor participates in selected syscall handling without making the workload unrestricted.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep advanced seccomp mediation confined to trusted sandbox/runtime infrastructure.

---

## Enhanced Lab 35 — AppArmor Denial Evidence

### Objective

Turn **AppArmor Denial Evidence** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
sudo dmesg | grep -i 'apparmor.*denied' | tail -20 2>/dev/null || true
```

### Expected Result

Denied paths and profile names appear in audit messages on AppArmor-enabled systems.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never respond to an LSM denial by blindly using chmod 777 or disabling confinement.

---

## Enhanced Lab 36 — SELinux Label Model

### Objective

Turn **SELinux Label Model** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
command -v getenforce >/dev/null && getenforce || true
ls -Z . 2>/dev/null | head
```

### Expected Result

SELinux-enabled hosts show enforcing state and security labels.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix labels/policy intentionally instead of disabling SELinux.

---

## Enhanced Lab 37 — LSM Defense in Depth

### Objective

Turn **LSM Defense in Depth** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
Unix mode/ACL
  +
namespace view
  +
LSM policy
  ↓
final file/process authorization
```

### Expected Result

A workload can be denied even when POSIX permissions appear permissive.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat LSMs as an independent security layer in incident diagnosis.

---

## Enhanced Lab 38 — Read-Only Root Filesystem Design

### Objective

Turn **Read-Only Root Filesystem Design** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
/            read-only
/tmp         tmpfs
/var/lib/app volume
/run         tmpfs
```

### Expected Result

Unexpected writes fail immediately, exposing hidden state assumptions.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Design writable paths explicitly rather than making the entire root filesystem mutable.

---

## Enhanced Lab 39 — tmpfs for Ephemeral Sensitive Data

### Objective

Turn **tmpfs for Ephemeral Sensitive Data** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
mount | grep tmpfs | head
```

### Expected Result

tmpfs mounts are visible as memory-backed filesystems rather than persistent block storage.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use tmpfs for short-lived sensitive files when persistence is undesirable.

---

## Enhanced Lab 40 — Bind Mount Attack Surface

### Objective

Turn **Bind Mount Attack Surface** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
host /srv/app-config
   ↓ read-only bind
container /etc/app

dangerous:
host /
   ↓ read-write
container /host
```

### Expected Result

Mount scope and read/write mode directly determine which host files the container can affect.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Bind only the minimum host path and prefer read-only when possible.

---

## Enhanced Lab 41 — Runtime Socket as Host Control Plane

### Objective

Turn **Runtime Socket as Host Control Plane** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
compromised app
  ↓ engine API socket
create privileged workload
  ↓ mount host /
host compromise
```

### Expected Result

The runtime API can perform actions far beyond the original container's normal privileges.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never mount the engine socket into ordinary application containers.

---

## Enhanced Lab 42 — Device Node Exposure

### Objective

Turn **Device Node Exposure** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
ls -l /dev | head -30
```

### Expected Result

The container or host exposes a finite list of device nodes rather than unrestricted hardware.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Grant only the exact device required and pair it with least-privilege capability/policy.

---

## Enhanced Lab 43 — procfs Information Exposure

### Objective

Turn **procfs Information Exposure** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
mount | grep ' on /proc '
ls /proc | head
```

### Expected Result

The process view depends on the active PID namespace and proc mount.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Avoid host PID namespace sharing for ordinary application workloads.

---

## Enhanced Lab 44 — sysfs Risk

### Objective

Turn **sysfs Risk** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
mount | grep ' on /sys ' || true
findmnt /sys 2>/dev/null || true
```

### Expected Result

Mount options show whether sysfs is read-only or writable in the current environment.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep sysfs restricted/read-only unless trusted infrastructure software needs more.

---

## Enhanced Lab 45 — cgroup v2 memory.current / max

### Objective

Turn **cgroup v2 memory.current / max** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
CG=/sys/fs/cgroup
cat "$CG/memory.current" 2>/dev/null || true
cat "$CG/memory.max" 2>/dev/null || true
```

### Expected Result

The current cgroup reports byte usage and either a numeric limit or `max`.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use cgroup counters to prove memory pressure instead of guessing from container exit code alone.

---

## Enhanced Lab 46 — memory.high vs memory.max

### Objective

Turn **memory.high vs memory.max** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /sys/fs/cgroup/memory.high 2>/dev/null || true
cat /sys/fs/cgroup/memory.max 2>/dev/null || true
```

### Expected Result

The two controls can differ, representing soft pressure versus hard enforcement.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use memory limits from measured working-set and startup peaks, not arbitrary round numbers.

---

## Enhanced Lab 47 — memory.events

### Objective

Turn **memory.events** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /sys/fs/cgroup/memory.events 2>/dev/null || true
```

### Expected Result

Counters reveal whether the cgroup actually experienced OOM or hard-limit events.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Check kernel/cgroup evidence before diagnosing memory kills.

---

## Enhanced Lab 48 — OOM Group Semantics Concept

### Objective

Turn **OOM Group Semantics Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
service cgroup
  ├─ process A
  ├─ process B
  └─ helper
OOM group policy
  ↓
fail workload consistently
```

### Expected Result

The system can avoid leaving a corrupted half-alive process group after memory exhaustion.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

For tightly coupled multi-process workloads, prefer coherent failure over unpredictable partial survival.

---

## Enhanced Lab 49 — CPU Quota and Throttling Evidence

### Objective

Turn **CPU Quota and Throttling Evidence** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /sys/fs/cgroup/cpu.max 2>/dev/null || true
cat /sys/fs/cgroup/cpu.stat 2>/dev/null || true
```

### Expected Result

The output shows quota configuration plus throttling counters such as nr_throttled/throttled_usec on supported kernels.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Correlate CPU throttling with request latency and queue buildup.

---

## Enhanced Lab 50 — CPU Weight vs Quota

### Objective

Turn **CPU Weight vs Quota** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
weight:
who wins when CPU is contested

quota:
maximum CPU time per period
```

### Expected Result

A workload can have high relative weight yet still be capped by quota.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Choose weight for relative fairness and quota for hard containment.

---

## Enhanced Lab 51 — cpuset and NUMA

### Objective

Turn **cpuset and NUMA** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /sys/fs/cgroup/cpuset.cpus.effective 2>/dev/null || true
lscpu | grep -E 'NUMA|CPU\(s\)'
```

### Expected Result

The host reports effective CPUs and NUMA topology.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use cpuset/NUMA tuning only for measured latency or HPC requirements.

---

## Enhanced Lab 52 — PIDs Controller

### Objective

Turn **PIDs Controller** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /sys/fs/cgroup/pids.current 2>/dev/null || true
cat /sys/fs/cgroup/pids.max 2>/dev/null || true
```

### Expected Result

The current process count and configured limit are visible.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set a realistic PID ceiling for services that should never create thousands of processes.

---

## Enhanced Lab 53 — I/O Controller Concept

### Objective

Turn **I/O Controller Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /sys/fs/cgroup/io.stat 2>/dev/null | head
```

### Expected Result

I/O counters show bytes and operations by block device where available.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Correlate storage latency with cgroup I/O and underlying disk performance.

---

## Enhanced Lab 54 — Pressure Stall Information

### Objective

Turn **Pressure Stall Information** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

### Expected Result

The output reports `some` and sometimes `full` stall averages and totals.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use PSI alongside utilization to understand resource contention and saturation.

---

## Enhanced Lab 55 — Host Reserve

### Objective

Turn **Host Reserve** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```python
host_mem_gib = 32
system_reserve = 4
workload_budget = host_mem_gib - system_reserve
print(workload_budget)
```

### Expected Result

The workload capacity is lower than raw host memory because system overhead is explicitly reserved.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Capacity-plan the host, not just individual containers.

---

## Enhanced Lab 56 — Resource Limit Startup Burst

### Objective

Turn **Resource Limit Startup Burst** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
steady p95  = 400 MiB
startup peak = 620 MiB
limit         = 450 MiB  → unstable
```

### Expected Result

The proposed limit is compared with both steady and startup behavior.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Measure startup, failover, and peak behavior before setting hard limits.

---

## Enhanced Lab 57 — Network Namespace localhost

### Objective

Turn **Network Namespace localhost** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
ip addr show lo
ip route
```

### Expected Result

Loopback and route state are local to the current network namespace.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use service DNS/IP for inter-container traffic, not localhost.

---

## Enhanced Lab 58 — veth Packet Path

### Objective

Turn **veth Packet Path** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
container eth0
  ↕ veth pair
host veth
  ↓ bridge
host route/NAT
  ↓ external network
```

### Expected Result

Each packet crosses namespace, veth, bridge, routing/firewall, and optionally NAT layers.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Troubleshoot networking hop by hop rather than changing all firewall rules.

---

## Enhanced Lab 59 — Conntrack / NAT State Concept

### Objective

Turn **Conntrack / NAT State Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
sysctl net.netfilter.nf_conntrack_max 2>/dev/null || true
ss -s
```

### Expected Result

The host exposes connection-table capacity and socket summary on compatible systems.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Monitor connection-table and ephemeral-port pressure for high-fanout workloads.

---

## Enhanced Lab 60 — Ephemeral Port Exhaustion

### Objective

Turn **Ephemeral Port Exhaustion** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
sysctl net.ipv4.ip_local_port_range
ss -tan state time-wait | wc -l
```

### Expected Result

The port range and TIME_WAIT population provide evidence for high connection churn.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use connection pooling/reuse and tune only after measuring the real bottleneck.

---

## Enhanced Lab 61 — MTU and Encapsulation

### Objective

Turn **MTU and Encapsulation** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
ip link show
ping -M do -s 1400 <AUTHORIZED_TARGET> 2>/dev/null || true
```

### Expected Result

Interface MTUs and path-MTU behavior can be compared on an authorized lab network.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Account for encapsulation overhead when designing container overlays.

---

## Enhanced Lab 62 — DNS Search Domains

### Objective

Turn **DNS Search Domains** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
cat /etc/resolv.conf
getent hosts localhost
```

### Expected Result

Resolver configuration shows nameservers, search domains, and options.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

During DNS incidents, inspect the resolver file inside the actual network namespace.

---

## Enhanced Lab 63 — Service Discovery vs Container IP

### Objective

Turn **Service Discovery vs Container IP** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
container old IP 10.1.0.7
  ↓ recreate
container new IP 10.1.0.19
service name remains stable
```

### Expected Result

Clients can continue resolving the service despite container replacement.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never persist container IP addresses in application configuration.

---

## Enhanced Lab 64 — Volume Is Not Backup

### Objective

Turn **Volume Is Not Backup** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
container
  ↓ volume
persistent state
  ↓ separate backup
off-host/immutable copy
  ↓ restore test
```

### Expected Result

The storage design distinguishes persistence from recovery.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Define backup, retention, and restore tests for every durable volume.

---

## Enhanced Lab 65 — Application-Consistent Volume Backup

### Objective

Turn **Application-Consistent Volume Backup** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
DB writes
  ↓ quiesce / native backup
consistent checkpoint
  ↓ snapshot/copy
  ↓ resume
```

### Expected Result

Restore validation succeeds without crash-recovery or logical inconsistency surprises.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use application-aware backup mechanisms for databases and stateful services.

---

## Enhanced Lab 66 — Volume UID/GID Debugging

### Objective

Turn **Volume UID/GID Debugging** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
id
ls -ln /path/to/mount 2>/dev/null || true
```

### Expected Result

Numeric IDs reveal the actual ownership relationship.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Debug mount permissions with numeric IDs before changing modes.

---

## Enhanced Lab 67 — Filesystem Full vs Inode Full

### Objective

Turn **Filesystem Full vs Inode Full** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
df -h
df -i
```

### Expected Result

Capacity and inode availability are inspected separately.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Alert on both byte and inode exhaustion for file-heavy workloads.

---

## Enhanced Lab 68 — Graceful Queue Consumer Shutdown

### Objective

Turn **Graceful Queue Consumer Shutdown** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
SIGTERM
  ↓ stop fetching
  ↓ finish/rollback current message
  ↓ commit/ack if successful
  ↓ close connections
  ↓ exit
```

### Expected Result

No message is silently lost because the worker was killed mid-transaction.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Design shutdown semantics around the queue/database acknowledgement boundary.

---

## Enhanced Lab 69 — Readiness Dependency Scope

### Objective

Turn **Readiness Dependency Scope** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
required DB unavailable → not ready
optional analytics unavailable → still ready, degrade feature
```

### Expected Result

Readiness reflects critical dependencies only.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Classify dependencies as required versus optional before writing health checks.

---

## Enhanced Lab 70 — Liveness Anti-Pattern

### Objective

Turn **Liveness Anti-Pattern** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
remote DB slow
  ↓ liveness checks DB
probe fails
  ↓ restart storm
  ↓ more DB reconnect load
```

### Expected Result

The failure mode is recognized as a self-amplifying restart loop.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use liveness for local process deadlock/failure; use readiness for serving capability.

---

## Enhanced Lab 71 — Structured Log Correlation

### Objective

Turn **Structured Log Correlation** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```json
{"level":"ERROR","service":"orders","version":"1.8.4","request_id":"r-123","event":"db_timeout"}
```

### Expected Result

One user request can be reconstructed across multiple container instances.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Put high-cardinality correlation IDs in logs/traces, not metric labels.

---

## Enhanced Lab 72 — Metrics Cardinality

### Objective

Turn **Metrics Cardinality** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
good labels:
service, region, status, route_template

bad labels:
user_id, request_id, raw_url, uuid
```

### Expected Result

The metric design produces a predictable number of series.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep unbounded identifiers in logs/traces.

---

## Enhanced Lab 73 — OpenTelemetry Mental Model

### Objective

Turn **OpenTelemetry Mental Model** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
application instrumentation
  ↓ OTel SDK/agent
collector
  ↓
metrics backend
log backend
trace backend
```

### Expected Result

Application telemetry can be correlated with container runtime/resource evidence.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Instrument the service, not only the container host.

---

## Enhanced Lab 74 — eBPF Observability Concept

### Objective

Turn **eBPF Observability Concept** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
kernel tracepoints/kprobes
  ↓ eBPF programs
events/metrics
  ↓
network / runtime / security visibility
```

### Expected Result

Kernel-level telemetry can reveal behavior even when the application image is minimal.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use eBPF observability as evidence, not as a reason to weaken container isolation.

---

## Enhanced Lab 75 — Container Escape Threat Model

### Objective

Turn **Container Escape Threat Model** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
app compromise
  ↓ container privileges
  ↓ kernel/runtime attack surface
escape?
  ↓
host / neighbors
```

### Expected Result

The threat model identifies which controls reduce blast radius after application compromise.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Assume the application can be compromised and design the runtime boundary accordingly.

---

## Enhanced Lab 76 — Sandboxed Runtime Trade-Off

### Objective

Turn **Sandboxed Runtime Trade-Off** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
ordinary container:
app → host kernel

sandboxed:
app → sandbox kernel/runtime → host
or
app → lightweight VM kernel → host
```

### Expected Result

The isolation model is selected based on threat level and workload compatibility.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use stronger isolation for hostile multi-tenancy or untrusted code when justified.

---

## Enhanced Lab 77 — CRI Bridge to Kubernetes

### Objective

Turn **CRI Bridge to Kubernetes** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
kubelet
  ↓ CRI
containerd / CRI-O
  ↓ OCI runtime
runc/crun/sandbox runtime
  ↓ kernel
```

### Expected Result

The distinction explains why Docker-built OCI images still run on Kubernetes nodes without Docker Engine.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate image-building knowledge from node runtime implementation.

---

## Enhanced Lab 78 — Pod Sandbox Concept Preview

### Objective

Turn **Pod Sandbox Concept Preview** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
Pod
  ├─ app container
  ├─ sidecar
  └─ shared network namespace
       one Pod IP
```

### Expected Result

Multiple containers can communicate over localhost inside the same Pod because they share networking.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not map the Docker 'one container = one network identity' assumption directly to Kubernetes Pods.

---

## Enhanced Lab 79 — CNI / CSI Preview

### Objective

Turn **CNI / CSI Preview** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
Pod request
  ↓ CNI → network attachment
  ↓ CSI → storage attachment/mount
container runtime
```

### Expected Result

Networking and persistent storage are separate pluggable control paths.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Carry your namespace/route/mount mental models into Kubernetes troubleshooting.

---

## Enhanced Lab 80 — Sidecar Cost Model

### Objective

Turn **Sidecar Cost Model** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```python
pods = 200
sidecar_mib = 128
print("Sidecar memory GiB:", pods * sidecar_mib / 1024)
```

### Expected Result

Per-Pod helper overhead is converted into fleet-level resource consumption.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use sidecars only when their per-workload coupling is genuinely needed.

---

## Enhanced Lab 81 — Init Container Boundary

### Objective

Turn **Init Container Boundary** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
init step
  ↓ success
main workload starts

failure
  ↓ main workload blocked
```

### Expected Result

Startup dependencies are explicit and fail before serving traffic.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep initialization deterministic, idempotent, and bounded.

---

## Enhanced Lab 82 — Immutable Release Evidence

### Objective

Turn **Immutable Release Evidence** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
service=orders
image_digest=sha256:...
source_commit=abc123
builder=trusted-ci
config_version=42
runtime_user=10001
```

### Expected Result

An incident can reconstruct exactly which artifact and runtime policy were active.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make immutable artifact identity visible in deployment and logs.

---

## Enhanced Lab 83 — Operational Readiness Review

### Objective

Turn **Operational Readiness Review** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```text
[ ] image provenance
[ ] non-root
[ ] limits
[ ] health
[ ] graceful stop
[ ] persistent backup
[ ] secret lifecycle
[ ] logs/metrics/traces
[ ] rollback
[ ] owner/runbook
```

### Expected Result

The service can be operated and recovered before real users depend on it.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make operational readiness a release gate.

---

## Enhanced Lab 84 — Evidence-First Container Troubleshooting

### Objective

Turn **Evidence-First Container Troubleshooting** into a repeatable Linux/container engineering exercise.

### Safety Boundary

Use only your own Linux VM or an explicitly authorized lab host. Prefer read-only inspection. Namespace, cgroup, network, and filesystem mutation should be disposable and reversible.

### Procedure

1. Write the expected Linux/container model before running commands.
2. Capture host kernel, active user, and current namespace/cgroup baseline.
3. Execute the discovery command/code below.
4. Record the expected and observed evidence.
5. Where safe, create one reversible failure in a disposable namespace/container.
6. Diagnose from the underlying primitive rather than guessing.
7. Restore the intended state.
8. Document security, reliability, and performance impact.
9. Write one automation/check that would detect the issue earlier.

### Command / Code

```bash
ps -ef
lsns
cat /proc/self/cgroup
ip addr
ip route
df -h
cat /proc/pressure/memory
```

### Expected Result

The failing Linux/runtime layer is identified before remediation.

### Lab Record

```text
Concept
Expected state
Observed state
Relevant PID
Namespace/cgroup
Mount/storage
UID/GID/capabilities
Network/DNS
Evidence
Root cause
Fix
Verification
Prevention
```

### Best Practice

Change one layer at a time and preserve the evidence that justified the change.

---

## 5. Hands-on Lab / Practical Exercises

> Perform namespace and runtime labs only on your own Linux VM or authorized lab host.

### Lab 1 — Process vs Container Mental Model

Run:

```bash
ps -ef
```

Pick a normal process and document:

```text
PID
UID
open ports
mount view
network namespace
cgroup
```

Then predict what a container would isolate.

### Lab 2 — Inspect Namespaces

Run:

```bash
lsns
```

Record namespace types and owning PIDs.

### Lab 3 — UTS Namespace

```bash
sudo unshare --uts --fork bash
hostname lab-container
hostname
exit
hostname
```

Explain why host hostname did not change.

### Lab 4 — PID Namespace

Use:

```bash
sudo unshare --pid --fork --mount-proc bash
ps -ef
```

Explain why shell sees a new PID tree.

### Lab 5 — Mount Namespace

Create isolated mount namespace and mount a tmpfs.

Verify mount is not visible in original namespace.

### Lab 6 — Network Namespace

Create:

```bash
sudo ip netns add labns
sudo ip netns exec labns ip addr
```

Observe only loopback initially.

### Lab 7 — veth Pair

Create a veth pair and move one side into the namespace.

Assign:

```text
host side: 10.200.1.1/24
namespace: 10.200.1.2/24
```

Test ping.

### Lab 8 — Bridge

Create two network namespaces, two veth pairs, and one Linux bridge.

Demonstrate namespace-to-namespace communication.

### Lab 9 — Port Listener

Run a simple HTTP server inside network namespace.

Use routing/port-forwarding conceptually to expose it.

### Lab 10 — cgroup v2 Inspection

Run:

```bash
mount | grep cgroup
cat /proc/self/cgroup
systemd-cgls
```

Identify unified hierarchy.

### Lab 11 — Memory Limit Tabletop

Create a process that gradually allocates memory inside an authorized container/cgroup lab.

Observe memory pressure/OOM behavior.

Record:

```text
limit
working set
exit behavior
kernel/runtime evidence
```

### Lab 12 — CPU Throttling Tabletop

Compare unrestricted CPU-bound process with a cgroup-limited process.

Observe runtime/performance effect.

### Lab 13 — PIDs Limit

Create a safe controlled script that spawns child processes slowly.

Apply a low PID limit in a container runtime later and observe failure.

Do **not** run an uncontrolled fork bomb.

### Lab 14 — OCI Image Anatomy

Pull/export any small OCI-compatible image using container tooling.

Identify conceptually:

```text
manifest
config
layers
digest
```

### Lab 15 — Tags vs Digests

For one image:

```text
name:tag
digest
```

record both.

Explain why production deployment by digest is more reproducible.

### Lab 16 — Multi-Platform Image

Inspect a multi-architecture image manifest.

Record:

```text
linux/amd64
linux/arm64
```

and any other supported platforms.

### Lab 17 — Layer History

Inspect image history.

Identify:

```text
base layer
dependency step
application step
```

Predict which source-code change invalidates which cache layer.

### Lab 18 — Secret-in-Layer Tabletop

Bad build:

```text
COPY secret.txt /tmp/
RUN use-secret && rm /tmp/secret.txt
```

Explain why earlier layer can still contain secret.

Rewrite design using build-secret mechanism concept.

### Lab 19 — Writable Layer

Start a disposable container.

Create:

```text
/tmp/runtime-file
```

delete/recreate container.

Verify file disappears.

### Lab 20 — Persistent Volume

Attach a persistent volume.

Create a file.

Replace container.

Verify file remains.

### Lab 21 — Bind Mount

Bind-mount a host directory into container.

Demonstrate that editing inside container changes host file.

Document security risk.

### Lab 22 — Read-Only RootFS

Run a simple application with read-only root filesystem and explicit writable tmp path.

Identify files application attempts to write.

### Lab 23 — Non-Root Container

Run application as UID 10001.

Test:

```text
read app files
write approved volume
cannot modify protected system path
```

### Lab 24 — Capabilities Tabletop

For an application that only needs to bind an unprivileged port, propose:

```text
drop all capabilities
```

Then identify a case that might legitimately require one capability.

### Lab 25 — Seccomp Concept

Inspect your runtime's default seccomp profile documentation.

List five syscall categories that should be restricted for ordinary web workloads.

### Lab 26 — Rootless Architecture

Draw:

```text
unprivileged user
 ↓
rootless container engine
 ↓
user namespaces
 ↓
container
```

Compare with rootful daemon threat model.

### Lab 27 — PID 1 Signal Handling

Write a simple shell/Python service.

Send:

```bash
SIGTERM
```

Observe shutdown.

Modify app to trap signal and close gracefully.

### Lab 28 — Zombie Reaping Demonstration

Create a parent process that spawns and does not wait for children.

Observe process states.

Explain role of init/reaper.

### Lab 29 — Health Endpoint

Create:

```text
/health/live
/health/ready
```

where readiness fails if a required dependency is unavailable.

Explain why liveness should not always check every dependency.

### Lab 30 — Structured Logging

Convert:

```text
ERROR payment failed
```

into structured JSON with:

```text
timestamp
level
request_id
service
error_code
```

### Lab 31 — Container Threat Model

For a public API container, identify:

```text
asset
entry point
privilege
host impact
network reach
secret access
persistent data
```

Then define ten controls.

### Lab 32 — Registry Supply-Chain Design

Design:

```text
Developer
 ↓ Git
CI Build
 ↓
SBOM + Scan + Sign
 ↓
Private Registry
 ↓
Policy
 ↓
Production
```

### Lab 33 — Image Hardening

Take a hypothetical 1 GB image containing:

```text
compiler
curl
git
package manager
debug tools
source
```

design a minimal runtime image and explain what should disappear.

### Lab 34 — Resource Sizing Exercise

Given:

```text
CPU avg 0.2
CPU p95 0.7
CPU peak 1.3
Memory avg 350 MiB
Memory p95 480 MiB
Memory peak 550 MiB
```

propose initial request/limit-style values and explain trade-offs.

### Lab 35 — Full Container Failure Analysis

Analyze:

```text
container starts
passes process check
users get timeout
memory rises
restarts after 20 min
database volume persists
```

Build investigation tree covering:

```text
network
health
memory/OOM
dependency
logs
resource limit
signals
```

---

## 6. Mini Project

# Mini Project — Containerize and Harden a Three-Tier Application Conceptually

Application:

```text
Frontend
API
Worker
PostgreSQL
Redis
Object Storage
```

Your goal is to produce a container architecture **before using Docker Compose or Kubernetes**.

## Required Architecture

```text
Users
 ↓
Frontend
 ↓
API
 ↓
Database
 ↓
Object Storage

API
 ↓
Queue
 ↓
Worker

API / Worker
 ↓
Redis
```

## Image Design

For each application component define:

```text
base image
runtime dependencies
non-root UID
entrypoint
command
read-only paths
writable paths
health check
image tag/digest strategy
```

## Network Design

Define:

```text
frontend network
backend network
data network
```

Rules:

```text
Frontend → API
API → DB
API → Redis
Worker → DB
Worker → Redis
DB not reachable from Frontend
```

## Storage Design

Classify each path as:

```text
immutable image
ephemeral writable layer
tmpfs
persistent volume
object storage
```

## Resource Design

For each service define:

```text
CPU target
CPU limit
memory target
memory limit
PIDs limit
```

and explain why.

## Security Design

Require:

```text
non-root
drop capabilities
no privileged mode
read-only rootfs where possible
seccomp
LSM
no host socket
no host PID/network
approved image registry
signed image
SBOM
scan
secret injection
```

## Runtime Lifecycle

Define:

```text
startup
readiness
liveness
graceful shutdown
restart behavior
logging
```

## Required Deliverables

```text
README.md
CONTAINER_MODEL.md
IMAGE_DESIGN.md
NETWORK.md
STORAGE.md
RESOURCE_LIMITS.md
SECURITY.md
SUPPLY_CHAIN.md
HEALTH.md
OBSERVABILITY.md
FAILURE_MODES.md
```

Required failure-mode table:

```text
Failure             Detection             Response
-----------------------------------------------------------
Process crash       exit status           restart
Memory exhaustion   OOM metric/log        tune/fix leak
DB unavailable      readiness/errors      stop traffic
Volume full         filesystem metric     capacity/runbook
Image compromised   security finding      block/replace
Host kernel issue   node monitoring       evacuate/reboot
```

---

## 7. Recommended Resources

This course is designed to be self-contained.

For current standards and kernel behavior, use official references:

```text
Open Container Initiative
OCI Runtime Specification
OCI Image Specification
OCI Distribution Specification
Linux kernel cgroup v2 documentation
Linux namespaces manual/kernel documentation
Docker/containerd/runc documentation
```

---

## 8. Certification Relevance

This course is foundational rather than mapped to one vendor exam.

It directly prepares for:

```text
58. Docker Fundamentals
59. Kubernetes Fundamentals
60. Kubernetes Administration
61. OpenShift
CKA
CKAD
CKS
Docker/container platform work
Cloud-native security
DevSecOps
```

Important certification concepts introduced here:

```text
namespaces
cgroups
OCI
images
layers
registries
network namespaces
persistent storage
resource limits
security contexts
capabilities
seccomp
container lifecycle
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** A container is a lightweight VM.  
  **Best practice:** think isolated host process sharing the kernel.

- **Mistake:** Namespace isolation alone means secure sandbox.  
  **Best practice:** combine namespaces, cgroups, capabilities, seccomp, LSM, non-root, and hardened host.

- **Mistake:** Store database data in writable container layer.  
  **Best practice:** persistent volume plus tested backup.

- **Mistake:** Run every application as root.  
  **Best practice:** non-root UID.

- **Mistake:** Use privileged mode to fix permissions.  
  **Best practice:** identify required capability/mount/permission precisely.

- **Mistake:** Expose the container runtime socket.  
  **Best practice:** treat runtime API as host-level privileged control.

- **Mistake:** Use mutable `latest` tag for production.  
  **Best practice:** deploy immutable version/digest.

- **Mistake:** Delete a secret in a later image layer and assume it is gone.  
  **Best practice:** never put secret into layer.

- **Mistake:** No CPU/memory/PIDs limits.  
  **Best practice:** measure and apply intentional resource controls.

- **Mistake:** Treat image scanner as proof of security.  
  **Best practice:** combine scan, signing, provenance, runtime controls, and secure coding.

- **Mistake:** Write logs only inside container filesystem.  
  **Best practice:** stdout/stderr or external logging pipeline.

- **Mistake:** Hardcode container IPs.  
  **Best practice:** service discovery/DNS.

- **Mistake:** Health check only verifies PID exists.  
  **Best practice:** verify useful application health/readiness.

- **Mistake:** Debug by permanently changing running container.  
  **Best practice:** reproduce, fix source/image, redeploy.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is a Linux container fundamentally?

**Answer:** An isolated process/group of processes sharing the host kernel with namespaces, cgroups, filesystem/runtime and security controls.

### Q2. Container vs VM?

**Answer:** VM has its own guest kernel; container normally shares host kernel.

### Q3. Image vs container?

**Answer:** Image is immutable template; container is a runtime instance with writable/runtime state.

### Q4. OCI core specifications?

**Answer:** Runtime, Image, Distribution.

### Q5. Runtime bundle?

**Answer:** Root filesystem plus OCI runtime configuration used by low-level runtime.

### Q6. Content digest?

**Answer:** Cryptographic identifier of exact image content.

### Q7. Tag vs digest?

**Answer:** Tag is mutable reference; digest identifies immutable content.

### Q8. Namespace purpose?

**Answer:** Isolate/virtualize a process view of kernel resources.

### Q9. PID namespace?

**Answer:** Isolates process ID numbering/view.

### Q10. Network namespace?

**Answer:** Isolates interfaces, routes, sockets, ports, and network stack view.

### Q11. User namespace?

**Answer:** Maps container UIDs/GIDs to different host IDs.

### Q12. cgroups?

**Answer:** Hierarchical resource accounting/control for process groups.

### Q13. Memory limit breach can cause?

**Answer:** OOM kill behavior.

### Q14. CPU limit usually causes?

**Answer:** Throttling rather than immediate process termination.

### Q15. Writable container layer?

**Answer:** Ephemeral copy-on-write layer above read-only image layers.

### Q16. Volume?

**Answer:** Persistent storage mount that can outlive a container.

### Q17. Bind mount?

**Answer:** Directly maps host path into container.

### Q18. Linux capability?

**Answer:** One unit of privilege split from traditional root powers.

### Q19. Seccomp?

**Answer:** System-call filtering.

### Q20. Rootless container?

**Answer:** Container engine/runtime operating without host root privileges where supported.

### Q21. Privileged container?

**Answer:** Container with broad host-level capabilities/device access and greatly reduced isolation.

### Q22. SBOM?

**Answer:** Software Bill of Materials listing software components.

### Q23. Image signature?

**Answer:** Cryptographic assertion binding a trusted signer to exact image content.

### Q24. veth?

**Answer:** Virtual Ethernet pair used to connect namespaces/bridges.

### Q25. Port publishing?

**Answer:** Maps host address/port to a service inside container network namespace.

### Q26. PID 1 responsibility?

**Answer:** Signal handling/orphan adoption/zombie reaping considerations.

### Q27. Graceful shutdown?

**Answer:** Receive termination, stop new work, finish/close safely, exit before forced kill.

### Q28. Liveness vs readiness?

**Answer:** Liveness asks whether process should restart; readiness asks whether it should receive traffic.

### Q29. Why containers lead to Kubernetes?

**Answer:** Multi-host scheduling, discovery, self-healing, scaling, rolling updates, persistent storage, policy, and orchestration complexity.

### Q30. Strong container security model?

**Answer:** Trusted image + least privilege + kernel/runtime hardening + resource limits + controlled network + external state + monitoring.

---

# Expanded Self-Assessment Bank — Application Containers

### Q1. What is the key engineering lesson from **Kernel View of a Container**?

**Answer:** When troubleshooting, translate the container symptom into the underlying Linux primitive.

### Q2. What is the key engineering lesson from **clone/unshare/setns Mental Model**?

**Answer:** Use namespace tools in disposable labs to understand isolation before relying on runtime abstractions.

### Q3. What is the key engineering lesson from **Namespace Lifetime**?

**Answer:** Treat namespace membership as a reference/lifecycle concept, not merely a one-time process setting.

### Q4. What is the key engineering lesson from **Namespace Inode Comparison**?

**Answer:** Compare namespace handles before assuming two processes share the same network or mount view.

### Q5. What is the key engineering lesson from **PID Namespace Parent Visibility**?

**Answer:** Remember that host administrators can generally inspect container processes even when the container cannot see host processes.

### Q6. What is the key engineering lesson from **PID 1 Signal Semantics**?

**Answer:** Design the primary process for graceful termination instead of relying on SIGKILL.

### Q7. What is the key engineering lesson from **Zombie Reaping**?

**Answer:** Use a proper application supervisor or tiny init only when the workload legitimately spawns unmanaged children.

### Q8. What is the key engineering lesson from **Mount Namespace vs chroot**?

**Answer:** Never treat chroot as equivalent to container isolation.

### Q9. What is the key engineering lesson from **pivot_root Concept**?

**Answer:** Understand the root filesystem as a mount-namespace construction, not a copied mini-OS.

### Q10. What is the key engineering lesson from **Mount Propagation**?

**Answer:** Keep default-private behavior for ordinary apps; change propagation only for infrastructure workloads that require it.

### Q11. What is the key engineering lesson from **Idmapped Mount Concept**?

**Answer:** Prefer mapping-aware storage features over recursive ownership rewrites when the platform supports them safely.

### Q12. What is the key engineering lesson from **OverlayFS Lower/Upper/Work/Merged**?

**Answer:** When a file changes, ask whether it belongs to an image lower layer, writable upper layer, or explicit mount.

### Q13. What is the key engineering lesson from **OverlayFS Copy-Up Cost**?

**Answer:** Put write-heavy persistent state on dedicated volumes rather than the copy-on-write layer.

### Q14. What is the key engineering lesson from **Whiteouts and Deletion**?

**Answer:** Never assume deleting a secret in a later image layer removes it from earlier layers.

### Q15. What is the key engineering lesson from **OCI Blob Digest vs Diff ID**?

**Answer:** Do not confuse registry blob identity with the uncompressed rootfs change identity.

### Q16. What is the key engineering lesson from **OCI Image Index**?

**Answer:** Verify the selected platform digest during multi-architecture troubleshooting.

### Q17. What is the key engineering lesson from **OCI Artifact / Referrer Concept**?

**Answer:** Anchor supply-chain evidence to immutable digests.

### Q18. What is the key engineering lesson from **Registry Pull Protocol Mental Model**?

**Answer:** Troubleshoot registry failures by separating auth, manifest resolution, blob transfer, TLS/DNS, and unpack stages.

### Q19. What is the key engineering lesson from **Registry Auth Token Flow**?

**Answer:** Prefer short-lived scoped tokens and workload identity over static registry passwords.

### Q20. What is the key engineering lesson from **Digest Integrity vs Publisher Trust**?

**Answer:** Use digests plus trusted signing/provenance policy for production releases.

### Q21. What is the key engineering lesson from **Reproducible Build Inputs**?

**Answer:** Record and pin inputs that materially affect the runtime artifact.

### Q22. What is the key engineering lesson from **Build Cache Poisoning Risk**?

**Answer:** Treat remote build cache as supply-chain infrastructure.

### Q23. What is the key engineering lesson from **SLSA / Provenance Mental Model**?

**Answer:** Use provenance to answer who built this image, from which source, and under which process.

### Q24. What is the key engineering lesson from **SBOM as Incident Index**?

**Answer:** Store SBOMs in a searchable inventory tied to immutable digests.

### Q25. What is the key engineering lesson from **Vulnerability Scan Prioritization**?

**Answer:** Use contextual risk, not raw CVE count.

### Q26. What is the key engineering lesson from **Container Root vs Host Root**?

**Answer:** Run applications as non-root even when additional isolation exists.

### Q27. What is the key engineering lesson from **User Namespace UID/GID Mapping**?

**Answer:** Use user namespace isolation where platform compatibility allows it.

### Q28. What is the key engineering lesson from **Rootless Runtime Architecture**?

**Answer:** Use rootless mode for appropriate workloads and understand its networking/cgroup/device limitations.

### Q29. What is the key engineering lesson from **Rootless Networking**?

**Answer:** Benchmark rootless networking when throughput/latency is performance-critical.

### Q30. What is the key engineering lesson from **Capabilities Sets**?

**Answer:** Drop all capabilities by default and add only what the application requires.

### Q31. What is the key engineering lesson from **Bounding Set**?

**Answer:** Use runtime capability dropping to prevent later privilege reacquisition.

### Q32. What is the key engineering lesson from **no_new_privs**?

**Answer:** Enable no-new-privileges for ordinary application workloads where compatible.

### Q33. What is the key engineering lesson from **Seccomp Architecture**?

**Answer:** Diagnose exact denied syscalls before weakening the profile.

### Q34. What is the key engineering lesson from **Seccomp User Notification Concept**?

**Answer:** Keep advanced seccomp mediation confined to trusted sandbox/runtime infrastructure.

### Q35. What is the key engineering lesson from **AppArmor Denial Evidence**?

**Answer:** Never respond to an LSM denial by blindly using chmod 777 or disabling confinement.

### Q36. What is the key engineering lesson from **SELinux Label Model**?

**Answer:** Fix labels/policy intentionally instead of disabling SELinux.

### Q37. What is the key engineering lesson from **LSM Defense in Depth**?

**Answer:** Treat LSMs as an independent security layer in incident diagnosis.

### Q38. What is the key engineering lesson from **Read-Only Root Filesystem Design**?

**Answer:** Design writable paths explicitly rather than making the entire root filesystem mutable.

### Q39. What is the key engineering lesson from **tmpfs for Ephemeral Sensitive Data**?

**Answer:** Use tmpfs for short-lived sensitive files when persistence is undesirable.

### Q40. What is the key engineering lesson from **Bind Mount Attack Surface**?

**Answer:** Bind only the minimum host path and prefer read-only when possible.

### Q41. What is the key engineering lesson from **Runtime Socket as Host Control Plane**?

**Answer:** Never mount the engine socket into ordinary application containers.

### Q42. What is the key engineering lesson from **Device Node Exposure**?

**Answer:** Grant only the exact device required and pair it with least-privilege capability/policy.

### Q43. What is the key engineering lesson from **procfs Information Exposure**?

**Answer:** Avoid host PID namespace sharing for ordinary application workloads.

### Q44. What is the key engineering lesson from **sysfs Risk**?

**Answer:** Keep sysfs restricted/read-only unless trusted infrastructure software needs more.

### Q45. What is the key engineering lesson from **cgroup v2 memory.current / max**?

**Answer:** Use cgroup counters to prove memory pressure instead of guessing from container exit code alone.

### Q46. What is the key engineering lesson from **memory.high vs memory.max**?

**Answer:** Use memory limits from measured working-set and startup peaks, not arbitrary round numbers.

### Q47. What is the key engineering lesson from **memory.events**?

**Answer:** Check kernel/cgroup evidence before diagnosing memory kills.

### Q48. What is the key engineering lesson from **OOM Group Semantics Concept**?

**Answer:** For tightly coupled multi-process workloads, prefer coherent failure over unpredictable partial survival.

### Q49. What is the key engineering lesson from **CPU Quota and Throttling Evidence**?

**Answer:** Correlate CPU throttling with request latency and queue buildup.

### Q50. What is the key engineering lesson from **CPU Weight vs Quota**?

**Answer:** Choose weight for relative fairness and quota for hard containment.

### Q51. What is the key engineering lesson from **cpuset and NUMA**?

**Answer:** Use cpuset/NUMA tuning only for measured latency or HPC requirements.

### Q52. What is the key engineering lesson from **PIDs Controller**?

**Answer:** Set a realistic PID ceiling for services that should never create thousands of processes.

### Q53. What is the key engineering lesson from **I/O Controller Concept**?

**Answer:** Correlate storage latency with cgroup I/O and underlying disk performance.

### Q54. What is the key engineering lesson from **Pressure Stall Information**?

**Answer:** Use PSI alongside utilization to understand resource contention and saturation.

### Q55. What is the key engineering lesson from **Host Reserve**?

**Answer:** Capacity-plan the host, not just individual containers.

### Q56. What is the key engineering lesson from **Resource Limit Startup Burst**?

**Answer:** Measure startup, failover, and peak behavior before setting hard limits.

### Q57. What is the key engineering lesson from **Network Namespace localhost**?

**Answer:** Use service DNS/IP for inter-container traffic, not localhost.

### Q58. What is the key engineering lesson from **veth Packet Path**?

**Answer:** Troubleshoot networking hop by hop rather than changing all firewall rules.

### Q59. What is the key engineering lesson from **Conntrack / NAT State Concept**?

**Answer:** Monitor connection-table and ephemeral-port pressure for high-fanout workloads.

### Q60. What is the key engineering lesson from **Ephemeral Port Exhaustion**?

**Answer:** Use connection pooling/reuse and tune only after measuring the real bottleneck.

### Q61. What is the key engineering lesson from **MTU and Encapsulation**?

**Answer:** Account for encapsulation overhead when designing container overlays.

### Q62. What is the key engineering lesson from **DNS Search Domains**?

**Answer:** During DNS incidents, inspect the resolver file inside the actual network namespace.

### Q63. What is the key engineering lesson from **Service Discovery vs Container IP**?

**Answer:** Never persist container IP addresses in application configuration.

### Q64. What is the key engineering lesson from **Volume Is Not Backup**?

**Answer:** Define backup, retention, and restore tests for every durable volume.

### Q65. What is the key engineering lesson from **Application-Consistent Volume Backup**?

**Answer:** Use application-aware backup mechanisms for databases and stateful services.

### Q66. What is the key engineering lesson from **Volume UID/GID Debugging**?

**Answer:** Debug mount permissions with numeric IDs before changing modes.

### Q67. What is the key engineering lesson from **Filesystem Full vs Inode Full**?

**Answer:** Alert on both byte and inode exhaustion for file-heavy workloads.

### Q68. What is the key engineering lesson from **Graceful Queue Consumer Shutdown**?

**Answer:** Design shutdown semantics around the queue/database acknowledgement boundary.

### Q69. What is the key engineering lesson from **Readiness Dependency Scope**?

**Answer:** Classify dependencies as required versus optional before writing health checks.

### Q70. What is the key engineering lesson from **Liveness Anti-Pattern**?

**Answer:** Use liveness for local process deadlock/failure; use readiness for serving capability.

### Q71. What is the key engineering lesson from **Structured Log Correlation**?

**Answer:** Put high-cardinality correlation IDs in logs/traces, not metric labels.

### Q72. What is the key engineering lesson from **Metrics Cardinality**?

**Answer:** Keep unbounded identifiers in logs/traces.

### Q73. What is the key engineering lesson from **OpenTelemetry Mental Model**?

**Answer:** Instrument the service, not only the container host.

### Q74. What is the key engineering lesson from **eBPF Observability Concept**?

**Answer:** Use eBPF observability as evidence, not as a reason to weaken container isolation.

### Q75. What is the key engineering lesson from **Container Escape Threat Model**?

**Answer:** Assume the application can be compromised and design the runtime boundary accordingly.

### Q76. What is the key engineering lesson from **Sandboxed Runtime Trade-Off**?

**Answer:** Use stronger isolation for hostile multi-tenancy or untrusted code when justified.

### Q77. What is the key engineering lesson from **CRI Bridge to Kubernetes**?

**Answer:** Separate image-building knowledge from node runtime implementation.

### Q78. What is the key engineering lesson from **Pod Sandbox Concept Preview**?

**Answer:** Do not map the Docker 'one container = one network identity' assumption directly to Kubernetes Pods.

### Q79. What is the key engineering lesson from **CNI / CSI Preview**?

**Answer:** Carry your namespace/route/mount mental models into Kubernetes troubleshooting.

### Q80. What is the key engineering lesson from **Sidecar Cost Model**?

**Answer:** Use sidecars only when their per-workload coupling is genuinely needed.

### Q81. What is the key engineering lesson from **Init Container Boundary**?

**Answer:** Keep initialization deterministic, idempotent, and bounded.

### Q82. What is the key engineering lesson from **Immutable Release Evidence**?

**Answer:** Make immutable artifact identity visible in deployment and logs.

### Q83. What is the key engineering lesson from **Operational Readiness Review**?

**Answer:** Make operational readiness a release gate.

### Q84. What is the key engineering lesson from **Evidence-First Container Troubleshooting**?

**Answer:** Change one layer at a time and preserve the evidence that justified the change.

## Completion Checklist

- [ ] I understand container vs VM.
- [ ] I understand shared-kernel implications.
- [ ] I understand OCI specs.
- [ ] I understand image manifests/config/layers.
- [ ] I understand tags vs digests.
- [ ] I understand registries and image distribution.
- [ ] I understand namespaces.
- [ ] I understand cgroups v2.
- [ ] I understand resource limits and OOM.
- [ ] I understand OverlayFS/copy-on-write.
- [ ] I understand writable layer vs volume.
- [ ] I understand bind mounts/tmpfs.
- [ ] I understand network namespaces/veth/bridges/NAT.
- [ ] I understand capabilities/seccomp/LSMs.
- [ ] I understand non-root/rootless models.
- [ ] I understand image supply-chain security.
- [ ] I understand PID 1/signals.
- [ ] I understand health checks.
- [ ] I understand logging/metrics/tracing.
- [ ] I completed all 35 labs.
- [ ] I completed the container architecture mini project.
