# 58. Docker Fundamentals

> Phase 15 — Containers

This course turns the container theory from Course 57 into practical Docker engineering.

The goal is not merely to run:

```bash
docker run nginx
```

The goal is to understand:

```text
Docker CLI
    ↓ API
Docker Engine / dockerd
    ↓
containerd
    ↓
OCI Runtime
    ↓
Linux Kernel
```

and then use that stack correctly for:

```text
image building
container lifecycle
storage
networking
Compose
registries
security
observability
resource control
automation
troubleshooting
```

---

# Current Docker Baseline

Reference baseline used in this course:

```text
Docker Engine 29.x
Current release checked for this material: 29.7.2
Release date: 2026-08-05
```

Current Docker Engine installation packages on Linux typically include:

```text
docker-ce
docker-ce-cli
containerd.io
docker-buildx-plugin
docker-compose-plugin
```

Modern Docker build behavior uses:

```text
docker build
    ↓
Buildx client
    ↓
BuildKit backend
```

Docker documentation states that Buildx and BuildKit are installed out of the box with current Docker Desktop and Docker Engine packages.

For multi-container applications, use the current:

```text
Compose Specification
```

and command style:

```bash
docker compose ...
```

rather than treating old `docker-compose` v1 syntax/tooling as the primary model.

---

# Docker Architecture

```text
                       User
                        |
                   Docker CLI
                        |
                  Docker API
                        |
                    dockerd
               /       |       \
              /        |        \
        Images      Networks    Volumes
              \        |        /
               \       |       /
                 containerd
                     |
                  containerd-shim
                     |
                    runc
                     |
               Linux Container
```

Build path:

```text
Dockerfile
   +
Build Context
   |
   v
Buildx
   |
   v
BuildKit
   |
   +-- cache
   +-- secrets
   +-- multi-stage
   +-- multi-platform
   |
   v
OCI Image
   |
   v
Registry
```

Runtime path:

```text
Image
 ↓
docker create
 ↓
Container Metadata
 ↓
docker start
 ↓
Isolated Process
 ↓
logs / metrics / network / mounts
```

---

## 1. Topic Title

**Docker Fundamentals**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain Docker architecture.
- Explain Docker Engine, CLI, API, containerd, shim, and OCI runtime relationships.
- Install Docker Engine correctly on Linux.
- Understand Docker Desktop architecture and why Linux containers on Windows/macOS involve virtualization.
- Configure Docker daemon basics.
- Use Docker contexts.
- Understand Docker API security.
- Pull, inspect, tag, push, save, load, export, and import images appropriately.
- Create, start, stop, restart, pause, unpause, kill, remove, and inspect containers.
- Understand foreground, detached, interactive, and TTY modes.
- Use `docker exec` correctly.
- Interpret container exit codes.
- Configure restart policies.
- Understand PID 1 and signal handling.
- Build images with Dockerfile.
- Use FROM, RUN, COPY, ADD, WORKDIR, ENV, ARG, USER, EXPOSE, ENTRYPOINT, CMD, HEALTHCHECK, STOPSIGNAL, SHELL, LABEL, VOLUME.
- Understand shell vs exec form.
- Understand `.dockerignore`.
- Use build cache effectively.
- Explain BuildKit.
- Use multi-stage builds.
- Use BuildKit cache mounts and secret mounts.
- Build multi-platform images with Buildx.
- Understand OCI image indexes.
- Use image digests for reproducible releases.
- Reduce final-image size and attack surface.
- Use Docker volumes, bind mounts, and tmpfs.
- Understand volume ownership and permission issues.
- Back up and restore volumes.
- Understand Docker networking architecture.
- Create user-defined bridge networks.
- Understand container DNS.
- Publish ports safely.
- Explain host, none, bridge, macvlan, ipvlan, and overlay networking.
- Inspect network namespaces conceptually.
- Configure resource limits.
- Understand memory OOM and CPU throttling.
- Run containers as non-root.
- Use read-only filesystems and dropped capabilities.
- Understand Docker's default seccomp protections.
- Understand AppArmor/SELinux integration.
- Understand rootless Docker.
- Understand user namespace remapping.
- Secure Docker daemon/API/socket.
- Use registries securely.
- Build and use private registry workflows.
- Understand SBOM, scanning, image signatures, provenance, and supply-chain controls.
- Use Docker Compose.
- Define services, networks, volumes, configs, secrets, health checks, dependencies, profiles, scaling, and overrides.
- Use Compose for realistic local multi-service applications.
- Understand environment-variable precedence.
- Understand Docker health checks.
- Collect logs and inspect container statistics.
- Configure logging drivers conceptually.
- Use events, inspect, top, stats, system df, and prune commands safely.
- Troubleshoot container startup, image build, permissions, storage, networking, DNS, health, memory, and registry failures.
- Understand Docker Swarm at a foundational level and why Kubernetes is usually studied next.
- Build and harden a production-style Dockerized application.

---

## 3. Prerequisites

Required:

- 57. Application Containers
- Linux administration
- Bash
- Networking
- Git
- Basic backend/web development

Recommended lab environment:

```text
Ubuntu 24.04 or 26.04 Linux VM
or
Docker Desktop with Linux containers
```

You should be comfortable with:

```bash
cd
ls
cat
grep
curl
ss
ip
ps
systemctl
journalctl
```

---

## 4. Core Concepts Explanation

# Part 1 — What Docker Is

Docker is an application-container platform and tooling ecosystem.

At the Engine level it provides:

```text
image management
container lifecycle
network management
volume management
API
CLI integration
```

Docker packages Linux container primitives into a developer/operator-friendly workflow.

# Part 2 — Docker Is Not the Container Standard

Docker popularized containers, but modern interoperability comes from standards such as OCI.

A Docker-built image can often run on:

```text
containerd
CRI-O
Kubernetes
cloud container services
```

because it follows OCI-compatible formats.

# Part 3 — Docker Client

The `docker` command is a client.

```bash
docker ps
```

does not itself enumerate Linux processes directly.

It sends an API request to the Docker daemon.

# Part 4 — Docker Daemon

`dockerd` manages:

```text
containers
images
volumes
networks
plugins
API requests
```

The daemon is highly privileged in standard rootful mode.

# Part 5 — Docker API

CLI communicates with Engine through Docker API.

Local Linux default commonly uses Unix socket:

```text
/var/run/docker.sock
```

Remote API exposure must use strong authentication/TLS and network controls.

# Part 6 — Docker Socket Privilege

Membership in the group that can access Docker socket is effectively highly privileged.

A user controlling Docker can often:

```text
mount host filesystem
start privileged container
access host devices
```

Treat Docker group access similarly to administrative access.

# Part 7 — containerd

Docker Engine uses containerd for core container lifecycle/image runtime functions.

Simplified:

```text
dockerd
 ↓
containerd
 ↓
runc
```

# Part 8 — containerd-shim

A shim stays associated with a running container so the higher-level runtime can restart/upgrade independently and manage container I/O/lifecycle.

# Part 9 — runc

`runc` is a low-level OCI runtime.

It creates the actual isolated process from OCI runtime configuration/rootfs.

# Part 10 — Docker Architecture Request Flow

Example:

```bash
docker run nginx
```

conceptually becomes:

```text
CLI request
 ↓
dockerd
 ↓
resolve/pull image if needed
 ↓
create network/mount/cgroup config
 ↓
containerd
 ↓
runc
 ↓
nginx process
```

# Part 11 — Docker Engine vs Docker Desktop

Docker Engine:

```text
server daemon + CLI ecosystem
```

Docker Desktop:

```text
desktop application
Engine environment
GUI
Compose
Build tooling
VM/WSL integration
additional developer features
```

# Part 12 — Docker Desktop on Windows

Linux containers need a Linux kernel.

On Windows, Docker Desktop commonly uses WSL 2/virtualization for Linux-container execution.

Your Windows host is not directly acting as the Linux kernel.

# Part 13 — Docker Desktop on macOS

macOS does not provide a Linux kernel.

Docker Desktop runs Linux containers inside a managed Linux virtual machine.

# Part 14 — Native Linux Docker

On Linux:

```text
container processes
 ↓
host Linux kernel
```

No Linux compatibility VM is required for ordinary Linux containers.

# Part 15 — Official Linux Packages

Current Docker Engine repository installation typically installs:

```text
docker-ce
docker-ce-cli
containerd.io
docker-buildx-plugin
docker-compose-plugin
```

Avoid mixing conflicting distribution/runtime packages without understanding package ownership.

# Part 16 — Ubuntu Installation Principle

Use Docker's official repository instructions for supported Ubuntu releases.

Current documentation includes modern LTS releases such as:

```text
Ubuntu 24.04
Ubuntu 26.04
```

along with supported interim releases at the time.

# Part 17 — Verify Installation

```bash
docker version
docker info
```

`docker version` shows client/server versions.

`docker info` shows runtime/storage/network/security configuration.

# Part 18 — Hello World

```bash
docker run --rm hello-world
```

Tests:

```text
client → daemon
image pull
container create
container start
stdout
cleanup
```

# Part 19 — Docker Service

Linux:

```bash
systemctl status docker
systemctl status containerd
```

Logs:

```bash
journalctl -u docker
journalctl -u containerd
```

# Part 20 — Daemon Configuration

Linux daemon configuration commonly:

```text
/etc/docker/daemon.json
```

Example concept:

```json
{
  "log-level": "info"
}
```

Validate JSON before restart.

# Part 21 — Daemon Restart Risk

Changing daemon settings can disrupt container operations depending on configuration.

Use maintenance/change control on production hosts.

# Part 22 — Live Restore Concept

Docker Engine supports live-restore behavior in suitable configurations so containers can continue during some daemon outages/upgrades.

Understand limitations before relying on it.

# Part 23 — Storage Driver

Docker uses a storage driver for image/container writable-layer management.

Modern Linux commonly uses:

```text
overlay2
```

on supported filesystems/kernels.

# Part 24 — Backing Filesystem

Storage-driver behavior depends on host filesystem.

Check:

```bash
docker info
```

for:

```text
Storage Driver
Backing Filesystem
```

# Part 25 — Cgroup Driver

Docker integrates with Linux cgroups.

`docker info` reveals:

```text
Cgroup Driver
Cgroup Version
```

Modern Linux commonly uses cgroup v2.

# Part 26 — Docker Context

A context stores endpoint/TLS/orchestration connection settings.

```bash
docker context ls
```

Useful for multiple Engines/environments.

# Part 27 — Create Context Concept

```bash
docker context create lab-remote   --docker "host=ssh://user@host"
```

SSH transport can be safer than opening unauthenticated TCP daemon ports.

# Part 28 — Switch Context

```bash
docker context use lab-remote
docker ps
```

Always verify current context before destructive commands.

# Part 29 — DOCKER_HOST

Environment variable can redirect client endpoint.

Example concept:

```bash
export DOCKER_HOST=ssh://user@host
```

Contexts are generally easier to manage than ad hoc variables.

# Part 30 — Remote API Security

Never expose:

```text
dockerd TCP without TLS/authentication
```

to untrusted networks.

Daemon control can become host control.

# Part 31 — Docker Group

On Linux:

```bash
sudo usermod -aG docker USER
```

removes need for `sudo docker`, but grants major host privilege.

Use only for trusted administrators/developers.

# Part 32 — Rootless Alternative

Rootless Docker can run daemon/containers without host root.

This reduces daemon compromise impact but has feature/performance constraints to understand.

# Part 33 — Docker Information Baseline

Before troubleshooting capture:

```bash
docker version
docker info
docker context show
uname -a
df -h
```

This reveals many environment mismatches.

# Part 34 — Engine Upgrade

Upgrade all related Docker packages coherently.

Review:

```text
release notes
deprecated features
storage/network changes
runtime security fixes
```

# Part 35 — Current Engine Version Awareness

This course uses Docker Engine 29.x behavior as the modern baseline.

Exact patches change frequently, so production installation must follow current Docker release/security notes.

# Part 36 — docker run

`docker run` is approximately:

```text
docker create
+
docker start
```

plus optional attach behavior.

# Part 37 — Pull Image

```bash
docker pull nginx:alpine
```

Pull only downloads the image; it does not create a container.

# Part 38 — List Images

```bash
docker image ls
```

Important columns:

```text
REPOSITORY
TAG
IMAGE ID
CREATED
SIZE
```

# Part 39 — Inspect Image

```bash
docker image inspect nginx:alpine
```

Inspect:

```text
config
entrypoint
cmd
environment
architecture
digest metadata
```

# Part 40 — Image History

```bash
docker history IMAGE
```

Shows build-layer history/size.

Useful for image-size optimization and secret-risk review.

# Part 41 — Create Container

```bash
docker create --name web nginx:alpine
```

Container exists but process is not running yet.

# Part 42 — Start Container

```bash
docker start web
```

# Part 43 — List Containers

Running:

```bash
docker ps
```

All:

```bash
docker ps -a
```

# Part 44 — Container Naming

Use stable human-friendly names in labs:

```bash
docker run --name api ...
```

but orchestration later should not depend on manually unique container names.

# Part 45 — Detached Mode

```bash
docker run -d nginx
```

Container runs in background.

Get logs separately.

# Part 46 — Foreground Mode

Without `-d`, client attaches to process output.

Useful for:

```text
debugging
one-shot commands
learning
```

# Part 47 — Interactive Mode

```bash
docker run -it ubuntu bash
```

`-i` keeps stdin open.

`-t` allocates pseudo-TTY.

# Part 48 — Auto Remove

```bash
docker run --rm alpine echo hello
```

Container metadata/writable layer is removed after exit.

Good for disposable jobs.

# Part 49 — Stop

```bash
docker stop web
```

Docker sends configured stop signal, waits timeout, then may force kill.

Application should handle graceful termination.

# Part 50 — Kill

```bash
docker kill web
```

Default sends SIGKILL.

Use only when graceful stop is not working or for deliberate signal testing.

# Part 51 — Restart

```bash
docker restart web
```

Equivalent operationally to stop/start with restart semantics.

Repeated manual restart is not root-cause analysis.

# Part 52 — Pause

```bash
docker pause web
docker unpause web
```

Pauses processes through kernel freezer mechanisms.

Networking/application timeouts may occur while paused.

# Part 53 — Remove Container

```bash
docker rm web
```

Stopped container is deleted.

Persistent volumes are separate unless explicitly removed.

# Part 54 — Force Remove

```bash
docker rm -f web
```

Stops/removes forcefully.

Avoid on stateful services without understanding consequences.

# Part 55 — docker exec

Run a new process inside running container:

```bash
docker exec -it web sh
```

This does not change the image.

Changes you make interactively are non-reproducible.

# Part 56 — docker attach

Attaches terminal to the container's primary process streams.

Different from `exec`, which starts another process.

# Part 57 — Container Inspect

```bash
docker inspect web
```

Key data:

```text
State
Config
Mounts
NetworkSettings
HostConfig
```

# Part 58 — Formatted Inspect

```bash
docker inspect   --format '{{.State.Status}} {{.State.ExitCode}}' web
```

Use Go templates to extract targeted fields.

# Part 59 — Container Logs

```bash
docker logs web
docker logs -f web
docker logs --since 10m web
```

Only works as expected with compatible logging configuration.

# Part 60 — Container Top

```bash
docker top web
```

Shows processes associated with container from Docker's perspective.

# Part 61 — Container Stats

```bash
docker stats
```

Observe:

```text
CPU
memory
network
block I/O
PIDs
```

# Part 62 — Container Changes

```bash
docker diff web
```

Shows filesystem changes in writable layer:

```text
A added
C changed
D deleted
```

# Part 63 — Copy Files

```bash
docker cp file.txt web:/tmp/
docker cp web:/var/log/app.log .
```

Useful for controlled diagnostics, not deployment.

# Part 64 — Rename

```bash
docker rename old new
```

# Part 65 — Wait

```bash
docker wait job
```

Blocks until container exits and prints exit code.

Useful in scripts.

# Part 66 — Exit Codes

Examples:

```text
0   success
1   generic app error
126 command cannot execute
127 command not found
137 SIGKILL / often OOM context
143 SIGTERM context
```

Always confirm with logs/state.

# Part 67 — OOMKilled

Inspect:

```bash
docker inspect   --format '{{.State.OOMKilled}}' CONTAINER
```

If true, inspect memory limit/application behavior.

# Part 68 — Restart Policies

Common:

```text
no
on-failure
always
unless-stopped
```

Choose by workload.

# Part 69 — on-failure

Restarts after non-zero exit.

Useful for transient-failure jobs/services but avoid infinite crash loops without monitoring.

# Part 70 — always

Restarts regardless of exit under Engine restart semantics.

Can surprise operators during intentional exits.

# Part 71 — unless-stopped

Restarts unless explicitly stopped.

Useful for host-managed long-running services.

# Part 72 — PID 1

Container primary process becomes PID 1 inside PID namespace.

It must handle signals/reap children correctly.

# Part 73 — Init Process

```bash
docker run --init ...
```

adds a tiny init to forward signals/reap zombies.

Useful for applications that spawn children.

# Part 74 — Stop Signal

Runtime/image can define stop signal.

Default often SIGTERM.

Application should implement graceful handling.

# Part 75 — Stop Timeout

Give app enough time to drain:

```text
HTTP requests
queue messages
DB transactions
```

before forced termination.

# Part 76 — Environment Variables

```bash
docker run -e APP_ENV=prod IMAGE
```

Use for configuration, not casually for long-lived secrets.

# Part 77 — Environment File

```bash
docker run --env-file .env IMAGE
```

Protect `.env`:

```text
Git ignore
file permissions
secret policy
```

# Part 78 — Working Directory

Override:

```bash
docker run -w /app IMAGE command
```

# Part 79 — User Override

```bash
docker run --user 10001:10001 IMAGE
```

Can reveal application permission assumptions.

# Part 80 — Container Lifecycle Troubleshooting

If container immediately exits:

```text
inspect state/exit code
logs
entrypoint/cmd
missing dependency
permissions
config
mounts
resource limits
```

# Part 81 — Dockerfile

Dockerfile defines image build instructions.

Example:

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

# Part 82 — Build Command

```bash
docker build -t myapp:1.0 .
```

`.` is build context.

# Part 83 — Build Context

Build system can access files in context unless ignored.

Keep context minimal.

# Part 84 — .dockerignore

Example:

```text
.git
.env
*.pem
__pycache__
node_modules
dist
coverage
```

reduces context size and secret risk.

# Part 85 — FROM

Defines base image:

```dockerfile
FROM ubuntu:24.04
```

or:

```dockerfile
FROM scratch
```

# Part 86 — Pin Base Image

Tags can move.

Critical builds may pin digest:

```dockerfile
FROM python:3.13-slim@sha256:...
```

Update intentionally through dependency automation.

# Part 87 — RUN

Executes build-time command:

```dockerfile
RUN apt-get update &&     apt-get install -y --no-install-recommends curl &&     rm -rf /var/lib/apt/lists/*
```

# Part 88 — RUN Layer Hygiene

Package index/install should occur in same step for apt-based images to avoid stale cache and unnecessary layers.

# Part 89 — COPY

```dockerfile
COPY src/ /app/src/
```

Preferred for normal file copies from build context.

# Part 90 — ADD

`ADD` has extra behavior such as archive extraction/remote-source capabilities.

Use `COPY` when extra behavior is unnecessary.

# Part 91 — WORKDIR

```dockerfile
WORKDIR /app
```

Creates/sets working directory for later instructions/runtime defaults.

# Part 92 — ENV

Persistent image runtime environment:

```dockerfile
ENV APP_ENV=production
```

Do not bake secrets.

# Part 93 — ARG

Build-time variable:

```dockerfile
ARG VERSION
RUN echo "$VERSION"
```

Not a secret mechanism; values can appear in metadata/history.

# Part 94 — LABEL

Metadata:

```dockerfile
LABEL org.opencontainers.image.source="..."
```

Useful for provenance/source/version metadata.

# Part 95 — USER

Run subsequent build/runtime instructions as a non-root user:

```dockerfile
USER 10001
```

Set ownership first.

# Part 96 — EXPOSE

Documents expected listening port:

```dockerfile
EXPOSE 8080
```

It does **not** publish the port to host.

# Part 97 — CMD

Provides default command/arguments.

Can be overridden by runtime arguments.

# Part 98 — ENTRYPOINT

Defines primary executable.

Runtime command arguments are appended/used according to form.

# Part 99 — ENTRYPOINT + CMD

Good pattern:

```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--port", "8080"]
```

CMD provides default arguments.

# Part 100 — Exec Form

```dockerfile
CMD ["python", "app.py"]
```

Process executes directly and receives signals cleanly.

# Part 101 — Shell Form

```dockerfile
CMD python app.py
```

runs through a shell.

PID/signal behavior differs.

# Part 102 — Shell Wrapper Trap

Bad wrapper:

```sh
python app.py
```

leaves shell as PID 1.

Better:

```sh
exec python app.py
```

replaces shell with application.

# Part 103 — HEALTHCHECK

Example:

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s   CMD curl -f http://localhost:8080/health || exit 1
```

Health status does not automatically restart standalone Docker container by itself.

# Part 104 — STOPSIGNAL

```dockerfile
STOPSIGNAL SIGTERM
```

defines preferred stop signal.

# Part 105 — SHELL

Can change default shell used for shell-form instructions.

Useful on Windows or specialized shell requirements.

# Part 106 — VOLUME Instruction

Declares intended mount point.

Modern production designs often explicitly manage volumes at runtime/Compose rather than relying only on Dockerfile declaration.

# Part 107 — Build Cache

BuildKit reuses previous results when inputs are unchanged.

Order Dockerfile from least-changing to most-changing.

# Part 108 — Dependency Cache Pattern

Python:

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

Source changes do not force dependency reinstall if requirements unchanged.

# Part 109 — Node Dependency Cache Pattern

```dockerfile
COPY package*.json ./
RUN npm ci
COPY . .
```

# Part 110 — BuildKit

Modern Docker build backend.

Provides:

```text
parallel build graph
advanced cache
secret mounts
SSH mounts
multi-platform
better output
```

# Part 111 — Buildx

Docker Buildx is CLI/build frontend for BuildKit.

```bash
docker buildx ls
docker buildx build ...
```

# Part 112 — Builder Instance

```bash
docker buildx create   --name multi   --driver docker-container   --use
```

Creates dedicated BuildKit builder.

# Part 113 — Cache Mount

BuildKit syntax concept:

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip     pip install -r requirements.txt
```

Speeds builds without including cache in final image layer.

# Part 114 — Build Secret

Correct secret pattern:

```dockerfile
RUN --mount=type=secret,id=token     command-that-reads /run/secrets/token
```

Build invocation supplies secret separately.

# Part 115 — SSH Mount

Use BuildKit SSH forwarding for private Git dependencies without copying SSH private keys into image.

# Part 116 — Multi-Stage Build

```dockerfile
FROM golang:1.25 AS build
WORKDIR /src
COPY . .
RUN go build -o /out/app

FROM gcr.io/distroless/base
COPY --from=build /out/app /app
ENTRYPOINT ["/app"]
```

Compiler stays out of runtime image.

# Part 117 — Builder vs Runtime Stage

Builder:

```text
compiler
headers
source
test tools
```

Runtime:

```text
binary
runtime libraries
certificates
```

This reduces attack surface.

# Part 118 — Named Stages

```dockerfile
FROM node:... AS build
...
FROM nginx:... AS runtime
COPY --from=build ...
```

Names improve readability over stage numbers.

# Part 119 — Target Stage

Build a specific stage:

```bash
docker build --target test .
```

Useful for development/test pipelines.

# Part 120 — Multi-Platform Build

```bash
docker buildx build   --platform linux/amd64,linux/arm64   -t registry/app:1.0   --push .
```

# Part 121 — Emulation

BuildKit may use QEMU emulation for cross-platform builds.

Convenient but slower than native builders for heavy compilation.

# Part 122 — Native Multi-Node Builder Concept

Use builders on actual target architectures for faster/reliable cross-architecture builds.

# Part 123 — Cross Compilation

Some languages can cross-compile efficiently.

Example Go concept:

```text
GOOS=linux
GOARCH=arm64
```

then package target binary.

# Part 124 — Image Index

Multi-platform tag points to an OCI image index/manifest list containing architecture-specific manifests.

# Part 125 — Build Output

Buildx can output to:

```text
local Docker image store
registry
OCI archive
local directory
cache
```

depending on driver/options.

# Part 126 — Build Provenance

Modern BuildKit can produce provenance/attestation metadata for supply-chain traceability.

Use in secure CI/CD.

# Part 127 — SBOM Attestation Concept

Build pipeline can attach software component inventory.

Use downstream vulnerability/policy tooling.

# Part 128 — No-Cache

```bash
docker build --no-cache .
```

forces rebuilding steps.

Use for debugging or dependency refresh, not as default solution to bad Dockerfile cache design.

# Part 129 — Pull Latest Base

```bash
docker build --pull .
```

asks builder to check for newer referenced base image.

Still use controlled dependency update strategy.

# Part 130 — Build Args

```bash
docker build   --build-arg APP_VERSION=1.2.3 .
```

Do not use for secrets.

# Part 131 — Build Labels

Attach release metadata:

```text
commit SHA
version
source repository
build date
```

using OCI annotations/labels where appropriate.

# Part 132 — Image Size Analysis

Use:

```bash
docker image ls
docker history IMAGE
```

to find large layers.

Specialized tools can provide deeper layer exploration.

# Part 133 — Clean Package Caches

Do not leave:

```text
apt lists
pip caches
npm caches
source archives
```

in final image unless needed.

# Part 134 — Combine or Split RUN?

Combine commands when cleanup must happen in same layer.

Split logically stable cacheable steps when it improves rebuild performance.

Do not optimize for layer count alone.

# Part 135 — Copy Ownership

```dockerfile
COPY --chown=10001:10001 . /app
```

avoids extra `chown` layer in compatible builds.

# Part 136 — Non-Root Dockerfile

Pattern:

```dockerfile
RUN adduser ...
COPY --chown=... .
USER 10001
```

Ensure required ports/files support non-root execution.

# Part 137 — Read-Only Runtime Design

Application writes only to:

```text
/tmp
explicit volume
```

so runtime can use read-only rootfs.

# Part 138 — Distroless Runtime

Use when application does not require shell/package manager in production.

Keep separate debug workflow.

# Part 139 — Alpine Trade-Off

Alpine is small but uses musl libc, which can create compatibility/performance differences for some software.

Smallest image is not always best image.

# Part 140 — Slim Debian/Ubuntu Trade-Off

Often provides broader glibc compatibility and familiar packages at somewhat larger size.

Choose based on application reliability/security, not only MB.

# Part 141 — Image Rebuild Cadence

Even unchanged application should be rebuilt when:

```text
base security updates
runtime patches
CA certificates
critical dependencies
```

change.

# Part 142 — Immutable Tag Strategy

Use:

```text
app:1.4.2
app:git-abc123
digest
```

and avoid rewriting release tags.

# Part 143 — Latest Tag

`latest` is only a tag name.

It has no built-in guarantee of being newest, secure, or stable.

# Part 144 — Image Tag

```bash
docker tag app:1.0 registry.example.com/team/app:1.0
```

Creates another reference to same image content locally.

# Part 145 — Image Push

```bash
docker push registry.example.com/team/app:1.0
```

Requires registry authentication/authorization.

# Part 146 — Image Save

```bash
docker image save app:1.0 -o app.tar
```

Preserves image structure/tags for transport.

# Part 147 — Image Load

```bash
docker image load -i app.tar
```

# Part 148 — Container Export

```bash
docker export CONTAINER > rootfs.tar
```

exports merged container filesystem but not complete image metadata/history.

# Part 149 — Image Import

```bash
docker import rootfs.tar image:name
```

creates image from filesystem archive.

Different use case from `save/load`.

# Part 150 — Save/Load vs Export/Import

```text
save/load:
image layers + metadata

export/import:
flattened container filesystem
```

# Part 151 — Build Failure: File Not Found

Check:

```text
build context
.dockerignore
COPY source path
working directory
case sensitivity
```

# Part 152 — Build Failure: Package Download

Check:

```text
DNS
proxy
CA certificate
repository
package version
architecture
```

# Part 153 — Build Failure: Secret

Never fix private dependency failure by copying permanent token into image.

Use BuildKit secret/SSH mount.

# Part 154 — Build Failure: Architecture

Error such as:

```text
exec format error
```

often means binary/image architecture mismatch.

Inspect:

```bash
docker image inspect IMAGE --format '{{.Architecture}}'
uname -m
```

# Part 155 — Build Engineering Mental Model

A production Docker image should be:

```text
reproducible
minimal
non-root
secret-free
versioned
scannable
signed/provenanced
multi-platform when required
```

# Part 156 — Container Writable Layer

Default writes go into ephemeral writable layer.

Deleting container deletes this data.

# Part 157 — Docker Volume

Managed persistent data:

```bash
docker volume create dbdata
```

Attach:

```bash
docker run -v dbdata:/var/lib/postgresql/data ...
```

# Part 158 — Volume Inspect

```bash
docker volume inspect dbdata
```

Shows driver, mountpoint, labels, options.

# Part 159 — Named Volume

Named volume is referenced by stable Docker name.

Better than anonymous volumes for intentional state.

# Part 160 — Anonymous Volume

Created without explicit name.

Can accumulate and become difficult to manage.

# Part 161 — Bind Mount

```bash
docker run   --mount type=bind,src="$PWD",dst=/app   IMAGE
```

Direct host path mapping.

# Part 162 — --mount vs -v

`--mount` is more explicit:

```text
type
source
destination
options
```

and is often preferred for clarity.

# Part 163 — Read-Only Mount

```bash
--mount type=bind,src=...,dst=/config,readonly
```

Protect configuration from container writes.

# Part 164 — tmpfs Mount

```bash
docker run   --tmpfs /run/secrets-temp   IMAGE
```

Memory-backed temporary storage.

# Part 165 — Volume Permissions

Common failure:

```text
container UID 10001
volume directory root:root
→ Permission denied
```

Fix ownership/design rather than running as root.

# Part 166 — Bind Mount Portability

Host path:

```text
/home/user/project
```

may not exist on another host.

Named volumes reduce host layout coupling.

# Part 167 — Development Bind Mount

Useful for live source editing:

```text
host source
 ↕
container /app
```

Production should usually deploy immutable image content.

# Part 168 — Database Volume

Stateful DB:

```text
PostgreSQL process
 ↓
named volume
```

but still needs backup.

# Part 169 — Volume Backup

Concept:

```bash
docker run --rm   -v dbdata:/data:ro   -v "$PWD":/backup   alpine   tar czf /backup/dbdata.tgz -C /data .
```

For real databases, use database-consistent backup tools when required.

# Part 170 — Volume Restore

Restore into empty/new volume, then validate application/database consistency.

# Part 171 — Volume Drivers

Docker volume plugins/drivers can integrate remote/network storage.

Understand availability/performance semantics before stateful production use.

# Part 172 — NFS Volume Concept

Docker can mount NFS through volume configuration.

Consider:

```text
locking
latency
UID/GID
availability
```

# Part 173 — Filesystem Full

Symptoms:

```text
write errors
DB failures
container instability
```

Check host and volume capacity:

```bash
df -h
docker system df
```

# Part 174 — Inodes

Filesystem can fail with free GB remaining if inode capacity is exhausted.

Check:

```bash
df -i
```

# Part 175 — Storage Driver vs Volume

Storage driver manages image/writable layers.

Volume driver manages persistent mounts.

Do not confuse them.

# Part 176 — Overlay2 Performance

Copy-on-write is excellent for application layers, but write-heavy state can perform better on direct volume mounts.

# Part 177 — Mount Propagation

Advanced host/container mount sharing can use propagation flags.

Use only when infrastructure software requires it.

# Part 178 — SELinux Bind Mounts

On SELinux hosts, labels may block bind-mounted content.

Docker supports relabel options in appropriate cases.

Understand shared/private labels before use.

# Part 179 — Volume Prune

```bash
docker volume prune
```

deletes unused volumes.

Never run blindly on hosts containing unknown state.

# Part 180 — Container Removal and Volumes

Removing container does not automatically remove named volume.

This is intentional for persistence.

# Part 181 — Compose Volume Lifecycle

Compose creates project-scoped named volumes.

```bash
docker compose down
```

normally keeps named volumes.

```bash
docker compose down -v
```

removes them.

The second command can destroy databases.

# Part 182 — Backup Policy

For every persistent volume define:

```text
owner
backup frequency
retention
restore procedure
RPO
RTO
```

# Part 183 — Secret File Mount

For sensitive runtime data, a read-only file mount can be safer than environment variable depending on workflow.

# Part 184 — Configuration Mount

Config file:

```text
host/config system
 ↓ read-only
container /etc/app/config.yaml
```

# Part 185 — tmpfs for Sensitive Scratch

Use tmpfs when data should disappear on stop and not persist to disk.

# Part 186 — Storage Ownership Strategy

Prefer stable numeric UID/GID in image.

Document persistent storage ownership.

Avoid random `chmod 777`.

# Part 187 — chmod 777 Anti-Pattern

World-writable permissions solve symptoms by removing controls.

Fix:

```text
correct UID/GID
group permission
ACL/label
mount options
```

# Part 188 — Volume Troubleshooting

Check:

```bash
docker inspect CONTAINER
docker volume inspect VOLUME
ls -ln HOSTPATH
df -h
df -i
```

Then inspect SELinux/AppArmor where relevant.

# Part 189 — Data Migration

When changing image/version:

```text
backup
schema migration
compatible volume format
rollback plan
```

must be considered.

# Part 190 — Storage Final Model

Use:

```text
image → immutable app
writable layer → disposable runtime
volume → persistent data
bind mount → host-integrated files
tmpfs → temporary memory data
```

# Part 191 — Docker Network Objects

List:

```bash
docker network ls
```

Common drivers:

```text
bridge
host
none
overlay
macvlan
ipvlan
```

# Part 192 — Default Bridge

Docker provides default bridge network.

It works, but user-defined bridges provide better service discovery/isolation for applications.

# Part 193 — User-Defined Bridge

```bash
docker network create appnet
```

Run:

```bash
docker run --network appnet --name api ...
docker run --network appnet --name db ...
```

# Part 194 — Built-In DNS

On user-defined networks, containers can resolve each other by container/service name.

```text
api → db
```

instead of fixed IP.

# Part 195 — Network Inspect

```bash
docker network inspect appnet
```

Inspect:

```text
subnet
gateway
containers
options
```

# Part 196 — Container IP

```bash
docker inspect   --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' CONTAINER
```

Do not hardcode it.

# Part 197 — Port Publishing

```bash
docker run -p 8080:80 nginx
```

means:

```text
host port 8080
→ container port 80
```

# Part 198 — Publish Bind Address

Safer local-only lab:

```bash
docker run -p 127.0.0.1:8080:80 nginx
```

instead of exposing on every interface.

# Part 199 — EXPOSE vs Publish

```text
EXPOSE:
image metadata/documentation

-p:
actual host port publication
```

# Part 200 — Random Port

```bash
docker run -P IMAGE
```

publishes exposed ports to available host ports.

Inspect:

```bash
docker port CONTAINER
```

# Part 201 — Container-to-Container Communication

Containers on same user-defined bridge use container port directly:

```text
api:8000
→ db:5432
```

They do not need host-published ports for internal communication.

# Part 202 — Frontend/Backend Networks

```text
frontend:
proxy ↔ api

backend:
api ↔ db
```

DB is not attached to frontend network.

# Part 203 — Multiple Networks

One container can attach to several networks.

Example:

```text
API
├─ frontend
└─ backend
```

# Part 204 — Connect/Disconnect

```bash
docker network connect backend api
docker network disconnect backend api
```

# Part 205 — Host Network

```bash
docker run --network host ...
```

shares host network namespace on supported platforms.

No port isolation.

# Part 206 — None Network

```bash
docker run --network none ...
```

container has loopback but no normal external Docker network.

Useful for highly isolated processing jobs.

# Part 207 — Macvlan

Makes containers appear as distinct L2 network endpoints.

Useful for legacy network integration but requires careful physical network design.

# Part 208 — Ipvlan

Provides L2/L3 networking with different host-side behavior than macvlan.

Advanced use case.

# Part 209 — Overlay Network

Multi-host network used with Docker Swarm.

Encapsulates traffic between Docker nodes.

# Part 210 — Bridge NAT

Typical outbound:

```text
container IP
 ↓ bridge
 ↓ NAT
host IP
 ↓
external
```

# Part 211 — DNS Configuration

Container `/etc/resolv.conf` is generated according to Docker/host/network configuration.

Inspect during DNS problems.

# Part 212 — Custom DNS

```bash
docker run --dns 10.0.0.53 ...
```

Use only when deliberate enterprise DNS is required.

# Part 213 — DNS Search Domain

```bash
--dns-search corp.example
```

changes resolver search behavior.

# Part 214 — Proxy Environment

Corporate proxy may require:

```text
daemon proxy
build proxy
container app proxy
```

These are different layers.

# Part 215 — NO_PROXY

Ensure internal names/CIDRs/services bypass proxy.

Poor `NO_PROXY` configuration causes confusing connectivity problems.

# Part 216 — MTU

Docker bridge/overlay MTU must fit underlying network.

Symptoms:

```text
curl small request works
large TLS response hangs
```

investigate MTU.

# Part 217 — IPv6

Docker supports IPv6 configuration.

Use only with deliberate address/firewall/routing planning.

# Part 218 — Firewall Interaction

Docker programs host networking/firewall rules.

Host firewall tools and Docker rules can interact in surprising ways.

Understand chain/order on production hosts.

# Part 219 — Published Ports Security

Published port can expose an application beyond expected interface.

Verify with:

```bash
ss -lntp
docker ps
```

# Part 220 — Network Namespace Inspection

Find container PID:

```bash
docker inspect -f '{{.State.Pid}}' CONTAINER
```

Then authorized Linux lab:

```bash
sudo nsenter -t PID -n ip addr
sudo nsenter -t PID -n ip route
```

# Part 221 — Connection Refused

Check:

```text
app is listening?
correct container port?
bind 0.0.0.0 vs 127.0.0.1?
network membership?
```

# Part 222 — Connection Timeout

Check:

```text
route
host firewall
Docker firewall
published bind
service health
remote security controls
```

# Part 223 — App Listening on 127.0.0.1

Inside a container:

```text
127.0.0.1
```

means loopback inside that network namespace.

Other containers/port mapping may not reach service if it binds only loopback.

Web apps normally bind `0.0.0.0` inside container when they must accept external container traffic.

# Part 224 — Port Already Allocated

Error:

```text
bind: address already in use
```

Find conflict:

```bash
ss -lntp
docker ps
```

Change host port or stop conflicting process.

# Part 225 — Network Name Resolution

If `api` cannot resolve `db`:

```text
same user-defined network?
correct service name?
DNS config?
container running?
```

# Part 226 — Internet Works on Host, Not Container

Check:

```text
bridge route
NAT/firewall
DNS
proxy
daemon network
IP forwarding
```

# Part 227 — Corporate VPN Conflict

VPN client routes/MTU/DNS can conflict with Docker address pools.

Use non-overlapping Docker subnets and deliberate daemon address pools.

# Part 228 — Default Address Pools

Configure daemon address pools when enterprise LAN/VPN overlaps Docker defaults.

Plan before many networks are created.

# Part 229 — Network Alias

User-defined networks can provide aliases.

Compose service names use similar built-in DNS behavior.

# Part 230 — Reverse Proxy Pattern

```text
Internet/localhost
 ↓
nginx/Traefik
 ↓
internal Docker network
 ↓
services
```

Only proxy publishes host ports.

# Part 231 — Database Network Pattern

```text
api
 ↓ backend network
db
```

No `-p 5432:5432` needed unless host/external client must connect.

# Part 232 — Network Isolation Principle

Only attach a service to networks it needs.

Network membership is part of least privilege.

# Part 233 — Network Observability

Use:

```text
docker inspect
ip
ss
curl
getent hosts
tcpdump on authorized host
```

to trace traffic.

# Part 234 — Network Debugging Method

Inside client container:

```bash
getent hosts SERVICE
curl -v http://SERVICE:PORT
```

Then server:

```bash
ss -lntp
```

# Part 235 — Docker Networking Final Model

```text
network namespace
+
veth
+
bridge/driver
+
routing/NAT
+
DNS
+
published ports
```

explains most Docker network behavior.

# Part 236 — Memory Limit

```bash
docker run --memory 512m IMAGE
```

Prevents unrestricted memory use.

Too-low limit can cause OOM.

# Part 237 — Memory Swap

Docker memory/swap flags influence cgroup memory behavior.

Understand host swap and cgroup v2 semantics before tuning production.

# Part 238 — CPU Limit

```bash
docker run --cpus 1.5 IMAGE
```

limits CPU quota approximately to 1.5 CPUs.

# Part 239 — CPU Shares

Relative weighting:

```bash
docker run --cpu-shares 512 ...
```

matters during contention, not as absolute CPU cap.

# Part 240 — cpuset

```bash
docker run --cpuset-cpus="0,1" ...
```

pins allowed CPUs.

# Part 241 — PIDs Limit

```bash
docker run --pids-limit 200 ...
```

reduces process-exhaustion risk.

# Part 242 — Resource Constraint Default

Docker documentation notes that containers have no resource constraints by default.

A container can consume host resources unless you configure limits.

# Part 243 — OOM Troubleshooting

```bash
docker inspect   -f '{{.State.OOMKilled}}' CONTAINER
docker stats
journalctl -k
```

Then profile application memory.

# Part 244 — CPU Throttling

Symptoms:

```text
latency
timeouts
slow worker
```

even when container appears healthy.

Check quota and workload demand.

# Part 245 — Non-Root Runtime

Dockerfile:

```dockerfile
USER 10001
```

or runtime:

```bash
docker run --user 10001 ...
```

# Part 246 — Read-Only Root

```bash
docker run --read-only   --tmpfs /tmp   IMAGE
```

reduces writable attack surface.

# Part 247 — Capabilities

Drop:

```bash
docker run --cap-drop ALL ...
```

then add only required capability:

```bash
--cap-add NET_BIND_SERVICE
```

if needed.

# Part 248 — Privileged Mode

```bash
docker run --privileged ...
```

greatly weakens isolation.

Do not use as generic fix for "permission denied."

# Part 249 — No New Privileges

```bash
docker run   --security-opt no-new-privileges:true   IMAGE
```

prevents privilege elevation through setuid-style mechanisms.

# Part 250 — Seccomp

Docker applies a default seccomp profile on supported Linux setups.

It blocks a set of higher-risk syscalls while preserving broad application compatibility.

# Part 251 — Disable Seccomp Risk

```bash
--security-opt seccomp=unconfined
```

removes syscall filtering.

Use only for controlled diagnosis when absolutely needed.

# Part 252 — Custom Seccomp

Apply reviewed profile:

```bash
docker run   --security-opt seccomp=profile.json   IMAGE
```

# Part 253 — AppArmor

On supported Ubuntu-style systems Docker can apply AppArmor profiles.

Inspect:

```bash
aa-status
```

and container security options.

# Part 254 — SELinux

On SELinux hosts, Docker integrates labels for process/filesystem isolation.

Bind mounts often require correct relabeling.

# Part 255 — Rootless Docker

Rootless mode runs daemon/containers as unprivileged user.

Docker documents it as a mitigation for daemon/runtime vulnerabilities.

# Part 256 — Rootless Requirements

Rootless commonly relies on:

```text
user namespaces
subuid/subgid
RootlessKit
user-mode networking
cgroup v2/systemd for full resource-control behavior
```

# Part 257 — Rootless Networking Trade-Off

User-mode networking can be slower than kernel networking.

Measure if performance-sensitive.

# Part 258 — Userns Remap

Rootful daemon can map container root to unprivileged host IDs.

Different from fully rootless daemon.

# Part 259 — Docker Socket Mount

Anti-pattern:

```bash
-v /var/run/docker.sock:/var/run/docker.sock
```

for ordinary application containers.

It grants control over host Docker daemon.

# Part 260 — Host Filesystem Mount

Anti-pattern:

```bash
-v /:/host
```

for normal workloads.

A compromised container may gain host data/control.

# Part 261 — Device Exposure

```bash
--device /dev/...
```

should be limited to workloads that truly need hardware access.

# Part 262 — Secrets at Runtime

Do not:

```text
docker inspect
```

and expose passwords through broad environment variables when stronger secret mechanisms exist.

Compose/Swarm/host secret files require deliberate design.

# Part 263 — Build Secrets

Build secrets and runtime secrets solve different problems.

```text
build secret → dependency fetch
runtime secret → application execution
```

# Part 264 — Registry Login

```bash
docker login REGISTRY
```

Prefer credential helpers/tokens.

Do not put password directly in shell command arguments.

# Part 265 — Password Stdin

Safer automation pattern:

```bash
printf '%s' "$TOKEN" |   docker login REGISTRY   --username USER   --password-stdin
```

Still protect environment/logs.

# Part 266 — Private Registry

Production registry controls:

```text
authentication
authorization
TLS
retention
immutability
scanning
audit
replication
```

# Part 267 — Registry TLS

Use trusted TLS certificates.

Avoid disabling certificate verification to "make it work."

# Part 268 — Insecure Registries

Daemon can be configured for insecure registries, but this weakens transport trust.

Do not use in production unless isolated exceptional design is explicitly accepted.

# Part 269 — SBOM

Generate/store SBOM in CI.

Use it to identify whether vulnerable component exists in deployed images.

# Part 270 — Vulnerability Scanning

Scan:

```text
base OS
language dependencies
image packages
```

and prioritize reachable/high-severity vulnerabilities.

# Part 271 — Image Signing Concept

Sign exact image digest with trusted identity/key using OCI-compatible signing tooling.

Verify before deployment.

# Part 272 — Provenance

Provenance answers:

```text
which source commit?
which builder?
which dependencies?
which build parameters?
```

# Part 273 — Runtime Image Policy

Production policy can require:

```text
approved registry
non-root
digest pin
scan threshold
signature
no privileged
resource limits
```

# Part 274 — Docker Daemon Hardening

Protect:

```text
socket
API
host root
plugin installation
daemon config
logs
certificates
```

# Part 275 — Host Hardening

Docker security depends on:

```text
patched kernel
runtime updates
minimal administrators
firewall
audit
disk security
host monitoring
```

# Part 276 — Container Security Inspection

```bash
docker inspect   --format '{{json .HostConfig.CapAdd}}' CONTAINER
```

Also inspect:

```text
Privileged
ReadonlyRootfs
SecurityOpt
User
Mounts
```

# Part 277 — Image User Check

```bash
docker image inspect   --format '{{.Config.User}}' IMAGE
```

Empty often means default root.

# Part 278 — Image Digest Deployment

Record:

```bash
docker image inspect IMAGE   --format '{{json .RepoDigests}}'
```

Use digest in release evidence.

# Part 279 — Security Failure Mode

If app fails after hardening:

```text
identify exact syscall/capability/path
modify least privilege
test
```

Do not jump immediately to privileged/unconfined.

# Part 280 — Docker Security Mental Model

```text
trusted image
+
non-root
+
minimum capabilities
+
seccomp/LSM
+
read-only root
+
safe mounts
+
resource limits
+
protected daemon
+
secure registry
```

# Part 281 — Docker Compose

Compose defines multi-container application in YAML.

Current command:

```bash
docker compose up
```

# Part 282 — Compose Specification

Current recommended format is Compose Specification.

A Compose file can define:

```text
services
networks
volumes
configs
secrets
```

# Part 283 — Basic Compose File

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

# Part 284 — Project Name

Compose resources are grouped by project name.

Default often derives from directory.

Override:

```bash
docker compose -p myapp up
```

# Part 285 — Compose Up

```bash
docker compose up
```

Creates required networks/volumes/services and attaches logs.

# Part 286 — Detached Compose

```bash
docker compose up -d
```

# Part 287 — Compose Down

```bash
docker compose down
```

removes service containers/networks.

Named volumes normally remain.

# Part 288 — Down with Volumes

```bash
docker compose down -v
```

removes project volumes.

Dangerous for databases.

# Part 289 — Compose ps

```bash
docker compose ps
```

shows service/container state.

# Part 290 — Compose Logs

```bash
docker compose logs -f
docker compose logs -f api
```

# Part 291 — Compose Exec

```bash
docker compose exec api sh
```

# Part 292 — Compose Run

One-off command:

```bash
docker compose run --rm api pytest
```

Different from exec into existing service.

# Part 293 — Service Build

```yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
```

# Part 294 — Image + Build

Compose can specify both:

```yaml
build: .
image: registry/app:dev
```

which controls build/tag behavior.

# Part 295 — Environment

```yaml
environment:
  APP_ENV: production
  LOG_LEVEL: info
```

# Part 296 — env_file

```yaml
env_file:
  - .env.runtime
```

Do not commit secrets.

# Part 297 — Compose Variable Interpolation

Host/`.env` values can interpolate:

```yaml
image: myapp:${APP_VERSION}
```

Understand interpolation vs container runtime environment.

# Part 298 — Environment Precedence

Compose has defined precedence among:

```text
CLI -e
interpolated environment
environment:
env_file:
image ENV
```

Test explicitly when configuration differs from expectation.

# Part 299 — Ports

```yaml
ports:
  - "127.0.0.1:8080:8000"
```

binds host loopback only.

# Part 300 — Expose

`expose` documents internal ports but does not publish them to host.

Services on same network can communicate without published port.

# Part 301 — Compose Default Network

Services automatically join a project default network unless customized.

They resolve each other by service name.

# Part 302 — Custom Networks

```yaml
networks:
  frontend:
  backend:
```

# Part 303 — Network Assignment

```yaml
services:
  api:
    networks:
      - frontend
      - backend
  db:
    networks:
      - backend
```

# Part 304 — Named Volume

```yaml
services:
  db:
    volumes:
      - dbdata:/var/lib/postgresql/data

volumes:
  dbdata:
```

# Part 305 — Bind Mount Compose

```yaml
volumes:
  - ./src:/app/src
```

good for development source sync.

# Part 306 — Read-Only Mount Compose

```yaml
volumes:
  - ./config.yaml:/app/config.yaml:ro
```

# Part 307 — tmpfs Compose

```yaml
tmpfs:
  - /tmp
```

for temporary memory-backed paths.

# Part 308 — depends_on

Controls startup dependency ordering.

It does not automatically guarantee a dependency application is ready unless health conditions are configured appropriately.

# Part 309 — Healthcheck Compose

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
  interval: 30s
  timeout: 3s
  retries: 3
```

# Part 310 — depends_on Health Condition

Compose can wait for dependency health in supported condition syntax.

Useful for development, but applications should still retry dependencies because runtime failures can occur later.

# Part 311 — Restart Compose

```yaml
restart: unless-stopped
```

maps to engine restart policy for ordinary Compose.

# Part 312 — Resource Limits in Compose

Compose supports resource-related configuration, but exact keys differ depending on local Compose vs Swarm deploy semantics.

Validate against current Compose Specification.

# Part 313 — Container Name Anti-Pattern

Avoid explicit `container_name` unless required.

It reduces Compose scaling flexibility and creates naming conflicts.

# Part 314 — Compose Scale

```bash
docker compose up -d --scale worker=3
```

works for services compatible with multiple replicas.

Published fixed host ports can conflict.

# Part 315 — Profiles

```yaml
profiles: ["debug"]
```

allow optional services such as:

```text
admin UI
debug proxy
local observability
```

# Part 316 — Compose Override Files

Use layered config:

```text
compose.yaml
compose.override.yaml
compose.prod.yaml
```

for environment-specific differences.

# Part 317 — Merge Behavior

Compose merges multiple files according to specification rules.

Always inspect final config:

```bash
docker compose config
```

# Part 318 — Compose Config

```bash
docker compose config
```

renders normalized/merged/interpolated configuration.

Excellent troubleshooting tool.

# Part 319 — Compose Secrets

Compose can mount secret files according to current implementation/specification.

For local development, ensure underlying host secret storage is protected.

# Part 320 — Compose Configs

Configs provide managed configuration-file semantics in supported Compose/platform contexts.

Do not put secrets into configs.

# Part 321 — Develop Watch Concept

Modern Compose supports development/watch workflows in current tooling.

Use for local iteration, not as production deployment model.

# Part 322 — Service Labels

Add metadata for:

```text
reverse proxy
monitoring
ownership
automation
```

but never store secrets in labels.

# Part 323 — Service Command Override

```yaml
command: ["python", "app.py", "--debug"]
```

overrides image CMD.

# Part 324 — Entrypoint Override

```yaml
entrypoint: ["/custom-entrypoint.sh"]
```

Use cautiously; can bypass image initialization.

# Part 325 — User in Compose

```yaml
user: "10001:10001"
```

enforces runtime user.

# Part 326 — Read-Only Compose

```yaml
read_only: true
tmpfs:
  - /tmp
```

strong default for compatible stateless services.

# Part 327 — Capability Drop Compose

```yaml
cap_drop:
  - ALL
```

add only required capabilities.

# Part 328 — Security Opt Compose

```yaml
security_opt:
  - no-new-privileges:true
```

and profile settings as appropriate.

# Part 329 — Compose Application Pattern

```text
reverse-proxy
 ↓ frontend
api
 ↓ backend
db + redis
worker
```

Only proxy publishes external port.

# Part 330 — Database Startup Race

Bad:

```text
API starts
DB process not ready
API exits forever
```

Fix:

```text
health check
dependency retry/backoff
proper startup behavior
```

# Part 331 — Compose for Development

Compose excels at:

```text
local multi-service dev
integration testing
reproducible labs
CI service dependencies
```

# Part 332 — Compose for Production

Compose can run production workloads on single hosts, but it lacks many cluster-level features of Kubernetes.

Use deliberate operations if used in production.

# Part 333 — Compose and Kubernetes

Compose describes multi-container app locally.

Kubernetes later adds:

```text
multi-node scheduling
controllers
service discovery
rolling deployments
cluster storage
policy
```

# Part 334 — Compose Troubleshooting

Use:

```bash
docker compose config
docker compose ps
docker compose logs
docker compose events
docker inspect
```

# Part 335 — Compose Final Model

Compose is:

```text
application topology
+
service configuration
+
networks
+
volumes
+
dependencies
```

defined declaratively for Docker environments.

# Part 336 — Logging Drivers

Docker supports logging drivers.

Common:

```text
json-file
local
journald
syslog
fluentd
cloud drivers
```

depending on environment.

# Part 337 — Default Log Growth

Unbounded local logs can fill disk.

Configure rotation/retention.

# Part 338 — Local Logging Driver

Docker's `local` driver is optimized for local storage/rotation use compared with raw unbounded JSON logs in many scenarios.

# Part 339 — json-file Rotation

Daemon/container options can set:

```text
max-size
max-file
```

to control log growth.

# Part 340 — Docker Events

```bash
docker events
```

streams:

```text
create
start
die
kill
network
volume
image
```

events.

Useful for timeline investigation.

# Part 341 — docker system df

```bash
docker system df
docker system df -v
```

shows image/container/volume/build-cache disk usage.

# Part 342 — Prune

Commands:

```bash
docker container prune
docker image prune
docker network prune
docker volume prune
docker builder prune
docker system prune
```

Understand exactly what each removes.

# Part 343 — System Prune Risk

Do not use:

```bash
docker system prune -a --volumes
```

blindly on important hosts.

It can delete data/artifacts needed for recovery.

# Part 344 — Build Cache Cleanup

```bash
docker builder prune
docker buildx prune
```

can recover disk but increase next build time.

# Part 345 — Image Dangling vs Unused

Dangling:

```text
unreferenced image layers/manifests
```

Unused:

```text
not used by container
```

`-a` prune changes scope.

# Part 346 — Disk Pressure Incident

Investigate:

```bash
df -h
df -i
docker system df -v
du -sh /var/lib/docker/*  # only with care/authorized host
```

Do not manually delete files under Docker data root while daemon is running.

# Part 347 — Container Health Status

```bash
docker inspect   --format '{{json .State.Health}}' CONTAINER
```

shows healthcheck history.

# Part 348 — Stats vs Application Health

Low CPU does not mean healthy.

Combine:

```text
container resources
healthcheck
application metrics
logs
dependency metrics
```

# Part 349 — Registry Pull Failure

Check:

```text
image name/tag
authentication
TLS
DNS
proxy
registry rate limits
architecture
```

# Part 350 — Manifest Unknown

Usually:

```text
wrong tag
repository
architecture manifest missing
```

Check registry and image reference.

# Part 351 — TLS Certificate Error

Do not disable TLS verification immediately.

Fix:

```text
CA trust
certificate chain
hostname
proxy interception
clock
```

# Part 352 — Docker Hub Rate Limits Concept

Public registry services may apply pull/rate policies.

CI should use authenticated/cache/private-registry strategies appropriate to provider terms.

# Part 353 — Registry Mirror Concept

A mirror/cache can reduce repeated upstream pulls.

Secure and maintain it like supply-chain infrastructure.

# Part 354 — Local Registry Lab

Docker Distribution-based registry can run locally for labs.

Production needs:

```text
TLS
auth
storage
backup
security
lifecycle
```

# Part 355 — Swarm Mode Overview

Docker Engine includes Swarm orchestration capabilities.

Core concepts:

```text
manager
worker
service
task
overlay network
secret
config
```

# Part 356 — Swarm Manager

Maintains cluster state and schedules services.

Uses Raft consensus among managers.

# Part 357 — Swarm Worker

Runs assigned service tasks.

# Part 358 — Swarm Service

Desired-state application definition.

Example:

```text
web replicas = 3
```

Swarm maintains three tasks.

# Part 359 — Swarm Overlay Network

Connects service tasks across hosts through overlay networking.

# Part 360 — Swarm Secret

Swarm provides secret-distribution capability to services.

Better than baking secrets into images.

# Part 361 — Why Kubernetes Next

Kubernetes dominates modern cloud-native orchestration training because it provides a broad ecosystem and standardized cluster API.

Docker remains fundamental for image/build/local runtime skills.

# Part 362 — Troubleshooting Framework

Always collect:

```text
version/context
container state
logs
inspect
network
mounts
resources
daemon logs
host capacity
```

before making changes.

# Part 363 — Daemon Won't Start

Check:

```bash
systemctl status docker
journalctl -u docker -b
cat /etc/docker/daemon.json
```

Common:

```text
invalid JSON
storage driver
network conflict
package/runtime conflict
disk full
```

# Part 364 — Container Exits Immediately

Check:

```bash
docker ps -a
docker inspect CONTAINER
docker logs CONTAINER
```

Then:

```text
command
entrypoint
config
permissions
dependency
architecture
```

# Part 365 — Permission Denied on Volume

Check:

```text
container UID/GID
host path ownership
volume ownership
read-only flags
SELinux/AppArmor
```

# Part 366 — Container Cannot Resolve DNS

Check:

```bash
docker exec CONTAINER cat /etc/resolv.conf
docker exec CONTAINER getent hosts example.com
```

Then inspect host/VPN/proxy DNS.

# Part 367 — Container Cannot Reach Another Container

Check:

```text
same network
service/container name
target port
application bind address
firewall
container running
```

# Part 368 — Published Port Not Reachable

Check:

```bash
docker ps
docker port CONTAINER
ss -lntp
curl localhost:PORT
```

then external firewall/routing.

# Part 369 — Memory Crash Loop

Check:

```text
OOMKilled
memory limit
app heap
restart policy
host memory
```

Fix leak/size rather than infinite restart.

# Part 370 — High CPU

Determine:

```text
real workload
busy loop
CPU throttling
too few replicas
malicious activity
```

using `docker stats` plus application profiling.

# Part 371 — Slow Build

Check:

```text
huge build context
cache invalidation
network
package registry
emulation
large COPY
no cache mounts
```

# Part 372 — Huge Image

Use:

```bash
docker history
```

Then:

```text
multi-stage
remove build tools
clean caches
avoid copied artifacts
use minimal runtime
```

# Part 373 — Compose Service Won't Start

```bash
docker compose ps
docker compose logs SERVICE
docker compose config
```

Check health/dependency/env/mount.

# Part 374 — Wrong Environment Value

Run:

```bash
docker compose config
docker compose exec SERVICE env
```

Compare Compose precedence sources.

# Part 375 — Stale Image

If source changed but service still uses old image:

```text
did build run?
tag reused?
cache?
compose pull/build behavior?
```

Inspect image ID/digest.

# Part 376 — Host Disk Full

Docker may fail:

```text
build
pull
start
logs
DB writes
```

Treat disk capacity as a production metric.

# Part 377 — Time Synchronization

Large clock drift can break:

```text
TLS
tokens
distributed logs
authentication
```

Containers share host clock in normal configuration; fix host time.

# Part 378 — Docker Production Checklist

```text
patched Engine/runtime
non-root app
resource limits
safe networking
persistent backups
log rotation
private registry
immutable image digest
scan/sign
health check
restart/runbook
```

# Part 379 — Docker-to-Kubernetes Transition

Docker knowledge maps directly:

```text
image          → Pod container image
port           → containerPort/Service
volume         → PV/PVC
healthcheck    → probes
env/config     → ConfigMap/Secret
resource limit → requests/limits
network        → CNI/Service
```

# Part 380 — Docker Final Mental Model

A reliable Docker workflow is:

```text
write code
 ↓
build reproducible image
 ↓
scan/sign/tag by digest
 ↓
run least-privilege container
 ↓
attach explicit network/storage
 ↓
limit resources
 ↓
observe health/logs
 ↓
replace, don't mutate
```

---

# Supplemental Deep-Study Layer — Docker Fundamentals

> **Source distinction:** The complete uploaded Course 58 remains preserved in this enhanced file. The section below adds deeper Docker Engine administration, BuildKit/Buildx engineering, storage/network internals, Compose behavior, runtime hardening, registry/supply-chain design, observability, CI/CD, rollback, and troubleshooting. Exact Engine/BuildKit/Buildx/Compose patch versions and version-specific flags in the original source remain source-derived; verify live Docker documentation before production upgrades or relying on recently introduced behavior.

Preferred learning sequence:

```text
Concept
  ↓
Detailed explanation
  ↓
Architecture / mental model
  ↓
Docker/BuildKit/Compose command
  ↓
Expected evidence
  ↓
Why it works
  ↓
Production scenario
  ↓
Troubleshooting
  ↓
Best practice
```


## Advanced Deep Dive 1 — Docker Client/API/Daemon Boundary

### Concept

The Docker CLI is an API client. `docker ps`, `docker run`, and `docker build` do not directly create namespaces; they send requests to an Engine endpoint that owns runtime state.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker context show
docker version
docker info
```

### Expected Evidence

Client and server versions/endpoints are visible separately.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Troubleshoot client context and daemon health before debugging the container itself.

---

## Advanced Deep Dive 2 — Unix Socket Privilege

### Concept

On a rootful Engine, the Unix socket is a privileged host control plane. A user or container that can issue arbitrary Docker API requests can often mount host filesystems or start privileged workloads.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
ls -l /var/run/docker.sock 2>/dev/null || true
getent group docker 2>/dev/null || true
```

### Expected Evidence

Socket ownership and trusted group membership are explicit.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Treat Docker socket access as administrative privilege.

---

## Advanced Deep Dive 3 — Remote Docker over SSH

### Concept

Docker contexts can use SSH transport to reach a remote Engine without exposing the daemon API directly on an unauthenticated TCP port.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker context create lab-remote --docker "host=ssh://user@host"
docker context ls
```

### Expected Evidence

The remote endpoint is represented as a named context.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Prefer SSH or properly authenticated TLS over public unauthenticated daemon TCP.

---

## Advanced Deep Dive 4 — Mutual TLS Daemon API Concept

### Concept

When the Docker API is exposed over TCP, strong designs authenticate both client and daemon using trusted certificates and network restrictions.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
client cert
  ↓ mTLS
dockerd TCP endpoint
  ↓
authorized host/network only
```

### Expected Evidence

The network path requires authenticated clients rather than relying only on IP allowlisting.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Do not expose the rootful daemon API to untrusted networks.

---

## Advanced Deep Dive 5 — Context Safety

### Concept

A destructive command acts on the current context. Operators with local, staging, and production contexts need an explicit verification habit.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker context ls
docker context show
docker info --format '{{.Name}}'
```

### Expected Evidence

The current Engine endpoint is known before deletion/prune/restart commands.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Make context verification part of every operational runbook.

---

## Advanced Deep Dive 6 — DOCKER_HOST Precedence Risk

### Concept

`DOCKER_HOST` can silently redirect the CLI away from the context an operator expects. Shell profiles and CI environments can therefore cause wrong-host actions.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
printf 'DOCKER_HOST=%s\n' "${DOCKER_HOST:-<unset>}"
docker context show
```

### Expected Evidence

The shell endpoint override is visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Keep endpoint selection explicit and avoid hidden environment overrides in production automation.

---

## Advanced Deep Dive 7 — Daemon Configuration Validation

### Concept

Invalid `daemon.json` can prevent Docker from starting. Validate syntax and supported settings before restarting a production daemon.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
python3 -m json.tool /etc/docker/daemon.json 2>/dev/null || true
sudo dockerd --validate --config-file=/etc/docker/daemon.json 2>/dev/null || true
```

### Expected Evidence

JSON is syntactically valid and the daemon validator reports configuration status when supported.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Validate daemon configuration before restart and keep a rollback copy.

---

## Advanced Deep Dive 8 — systemd Service Evidence

### Concept

On Linux, dockerd and containerd commonly run as systemd services. Unit status and journal logs are primary evidence when the Engine fails to start.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
systemctl status docker --no-pager
systemctl status containerd --no-pager
journalctl -u docker -b --no-pager | tail -80
```

### Expected Evidence

Service exit status and recent daemon errors are visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use systemd/journal evidence before reinstalling Docker.

---

## Advanced Deep Dive 9 — Data Root

### Concept

Docker stores local images, container writable layers, metadata, volumes, and build data under a configured data root. Moving or deleting this tree incorrectly can destroy runtime state.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker info --format '{{.DockerRootDir}}'
```

### Expected Evidence

The active Docker data directory is known.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Never manually delete Docker data-root files while the daemon is managing them.

---

## Advanced Deep Dive 10 — Data Root Migration

### Concept

Moving Docker storage requires a controlled stop, verified copy, daemon configuration change, ownership/SELinux consideration, restart, and validation.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
stop workloads/daemon
  ↓ backup metadata/data
copy data root preserving xattrs/ownership
  ↓ configure new data-root
start daemon
  ↓ validate images/volumes/containers
```

### Expected Evidence

The migration preserves runtime state and security metadata.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Treat Docker data-root movement as storage migration, not a simple directory rename.

---

## Advanced Deep Dive 11 — Live Restore Limits

### Concept

Live restore can keep some containers running while dockerd is unavailable, but it does not eliminate all daemon-upgrade, networking, logging, or operational limitations.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker info | grep -i 'Live Restore' || true
```

### Expected Evidence

The operator knows whether live restore is enabled and does not assume all daemon changes are zero-impact.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Test daemon-maintenance behavior on the exact host/runtime configuration.

---

## Advanced Deep Dive 12 — containerd Shim Role

### Concept

The shim keeps container process I/O and lifecycle decoupled from the high-level daemon/runtime so running processes do not require a permanently attached `runc` process.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
dockerd
  ↓
containerd
  ↓
containerd-shim
  ↓
container process
```

### Expected Evidence

The process hierarchy can show shim processes associated with running containers.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use the runtime stack mental model when diagnosing daemon-versus-container failures.

---

## Advanced Deep Dive 13 — Storage Driver vs Volume Driver

### Concept

The storage driver manages image layers and container writable layers; volume drivers manage persistent mount sources. They solve different data paths.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker info | grep -E 'Storage Driver|Backing Filesystem'
docker volume ls
```

### Expected Evidence

Image-layer storage and persistent volume inventory are inspected separately.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Do not troubleshoot database-volume performance as if it were only an overlay storage-driver issue.

---

## Advanced Deep Dive 14 — overlay2 Copy-Up

### Concept

With overlay-style storage, modifying lower-layer files can trigger copy-up into the writable layer. Write-heavy state belongs on explicit volumes.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker info | grep -i 'Storage Driver'
docker diff <CONTAINER> 2>/dev/null || true
```

### Expected Evidence

Writable-layer changes are distinguishable from mounted persistent data.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Keep databases and heavy mutable data off the container writable layer.

---

## Advanced Deep Dive 15 — Container Writable-Layer Recovery

### Concept

A stopped container retains its writable layer; a removed container does not. Recovery plans should never depend on a disposable layer as the only copy of important data.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker ps -a
docker inspect <CONTAINER> --format '{{json .Mounts}}' 2>/dev/null || true
```

### Expected Evidence

Important paths are confirmed to use volumes or external storage.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Assume the writable layer can disappear at any time.

---

## Advanced Deep Dive 16 — Named Volume Ownership

### Concept

A non-root image can fail on a volume created with incompatible numeric ownership. Runtime user, volume ownership, and initialization strategy must align.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format '{{.Config.User}} {{json .Mounts}}' 2>/dev/null || true
docker run --rm -v <VOLUME>:/data alpine sh -c 'ls -ldn /data'
```

### Expected Evidence

The application UID/GID can be compared with volume ownership.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Fix numeric ownership intentionally instead of running the application as root.

---

## Advanced Deep Dive 17 — Volume Backup Consistency

### Concept

A raw tar of live database files may not be application-consistent. Database-aware backups, quiescing, or snapshot integration are needed for stateful services.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
database
  ↓ native backup / quiesce
consistent point
  ↓ copy/snapshot volume
  ↓ restore test
```

### Expected Evidence

The backup process identifies whether it is crash-consistent or application-consistent.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use database-native backup for transactional data unless storage snapshots are integrated with quiescing.

---

## Advanced Deep Dive 18 — Bind Mount Portability

### Concept

Bind mounts couple a container to a specific host path, ownership model, filesystem, and security labels. They are excellent for development but reduce deployment portability.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format '{{json .Mounts}}' 2>/dev/null || true
```

### Expected Evidence

Bind and volume mount types are distinguishable.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use bind mounts deliberately for host integration; use immutable images/managed volumes for portable production workloads.

---

## Advanced Deep Dive 19 — Bind Mount Propagation

### Concept

Advanced infrastructure containers may require mount propagation so nested host/container mounts become visible across namespaces. This changes isolation and should not be used casually.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
private  → mount events do not propagate
shared   → bidirectional propagation
slave    → receives from parent but does not send back
```

### Expected Evidence

The requested propagation mode is tied to a real infrastructure requirement.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Keep ordinary application bind mounts private.

---

## Advanced Deep Dive 20 — tmpfs Mount Security

### Concept

tmpfs stores temporary files in memory-backed storage and disappears with the container, useful for ephemeral sensitive or high-churn scratch data.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm --tmpfs /run/secure:rw,noexec,nosuid,size=16m alpine   sh -c 'mount | grep /run/secure; df -h /run/secure'
```

### Expected Evidence

The path is mounted as tmpfs with explicit options and size.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use tmpfs for short-lived data that should not persist, while accounting for memory usage.

---

## Advanced Deep Dive 21 — Dockerfile Syntax Directive

### Concept

Modern Dockerfile frontends can use a syntax directive to select Dockerfile frontend behavior. This matters when using newer BuildKit features.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN echo hello
```

### Expected Evidence

The Dockerfile declares the frontend syntax family it expects.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Pin/standardize build frontend expectations in CI for reproducible builds.

---

## Advanced Deep Dive 22 — Dockerfile ARG Scope

### Concept

`ARG` has build-stage scope rules. An argument declared before `FROM` can influence base selection but normally needs redeclaration inside stages if used there.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
ARG BASE=alpine:3.22
FROM ${BASE}
ARG BASE
RUN echo "base=$BASE"
```

### Expected Evidence

The build demonstrates where the argument is available.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use ARG for non-secret build parameters and understand stage scope.

---

## Advanced Deep Dive 23 — ENV vs ARG

### Concept

`ARG` configures the build; `ENV` becomes image/runtime configuration. Neither is a secret mechanism.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
ARG BUILD_MODE=release
ENV APP_ENV=production
RUN echo "$BUILD_MODE"
```

### Expected Evidence

Runtime inspection contains ENV but not a secret-safe ARG mechanism.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Keep secrets out of both ARG and ENV image metadata.

---

## Advanced Deep Dive 24 — ONBUILD Instruction Concept

### Concept

`ONBUILD` stores trigger instructions that run when another Dockerfile uses the image as a base. It can be useful for framework builder images but creates hidden behavior.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
FROM alpine
ONBUILD COPY . /src
```

### Expected Evidence

Child builds execute inherited triggers even when their Dockerfile does not show the full behavior locally.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Avoid ONBUILD in general-purpose bases unless the implicit behavior is well documented.

---

## Advanced Deep Dive 25 — Heredoc Build Steps

### Concept

Dockerfile heredoc-style syntax can make multi-line scripts or generated files clearer when supported by the selected frontend.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN <<'EOF'
set -eu
echo "step one"
echo "step two"
EOF
```

### Expected Evidence

The multi-line build logic runs as one readable instruction.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use heredocs for clarity, not to hide large unmaintainable shell scripts.

---

## Advanced Deep Dive 26 — COPY Ownership

### Concept

`COPY --chown` can set final ownership while copying, avoiding a separate recursive chown layer and improving non-root image design.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
COPY --chown=10001:10001 app/ /app/
USER 10001
```

### Expected Evidence

Runtime files already have the correct numeric owner.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Set ownership during copy where supported instead of adding wasteful correction layers.

---

## Advanced Deep Dive 27 — COPY --link Concept

### Concept

Modern BuildKit Dockerfile frontends support independent-copy semantics such as `COPY --link` in compatible environments, improving cache reuse for some build graphs.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
# syntax=docker/dockerfile:1
COPY --link src/ /app/src/
```

### Expected Evidence

The build frontend treats the copy as a cache-friendly independent layer when supported.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use advanced Dockerfile features only when CI/builders are standardized and tested.

---

## Advanced Deep Dive 28 — Build Context Minimization

### Concept

Every file in a local build context is potentially available to the builder unless excluded. Large contexts slow builds and secrets in context increase risk even if not copied.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
du -sh .
find . -maxdepth 2 -type f | head
cat .dockerignore
```

### Expected Evidence

The context excludes `.git`, credentials, local caches, and irrelevant large artifacts.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Keep build context intentionally small and secret-free.

---

## Advanced Deep Dive 29 — Remote/Git Build Context Trust

### Concept

Remote build contexts are convenient but become supply-chain inputs. Source revision, authentication, submodules, and fetched content must be pinned and auditable.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
Git URL
  ↓ pin commit/tag
builder fetches source
  ↓
BuildKit
```

### Expected Evidence

The build references a known source revision rather than an unbounded moving branch.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Pin remote source and record the resolved commit in provenance.

---

## Advanced Deep Dive 30 — BuildKit LLB Mental Model

### Concept

BuildKit converts build instructions into a graph-like low-level build representation so independent steps can run/cache efficiently rather than behaving only as a linear shell script.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
Dockerfile
  ↓ frontend
LLB build graph
  ├─ source op
  ├─ exec op
  ├─ copy op
  └─ cache dependencies
```

### Expected Evidence

Independent graph nodes can be cached or executed in parallel where possible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Optimize build dependency graphs, not only Dockerfile layer count.

---

## Advanced Deep Dive 31 — Build Cache Key

### Concept

Build cache reuse depends on instruction, referenced files/content, build args, mount behavior, and parent state. Source-code COPY placed too early invalidates expensive dependency steps.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### Expected Evidence

Changing source code alone preserves the dependency-install cache.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Order stable dependency inputs before frequently changing application files.

---

## Advanced Deep Dive 32 — BuildKit Cache Mount

### Concept

A cache mount keeps package-manager download/build cache outside the final image layer while accelerating subsequent builds.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip     pip install -r requirements.txt
```

### Expected Evidence

Repeated builds reuse package cache without bloating the runtime image.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use cache mounts for performance, not for required runtime content.

---

## Advanced Deep Dive 33 — BuildKit Secret Lifetime

### Concept

Build secrets are mounted only for the build step that requests them and are not intended to persist in the image. The build command can still leak them if it prints/copies the secret.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
RUN --mount=type=secret,id=token     sh -c 'test -s /run/secrets/token && echo "token available"'
```

### Expected Evidence

The secret is available only at the expected temporary path during the step.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Never echo, copy, or persist BuildKit secrets into layers/logs.

---

## Advanced Deep Dive 34 — BuildKit SSH Mount

### Concept

SSH mounts forward an agent/socket to a build step so private Git dependencies can be fetched without copying a private key into the build context.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
RUN --mount=type=ssh git clone git@github.com:example/private-repo.git
```

### Expected Evidence

The build can authenticate using forwarded SSH credentials while the key is absent from the final image.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use short-lived/agent-forwarded build identity rather than copying private keys.

---

## Advanced Deep Dive 35 — Build Cache Export/Import

### Concept

CI systems can export BuildKit cache to a trusted remote backend and import it in later builds. Cache scope and trust need deliberate design.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker buildx build   --cache-from type=registry,ref=registry.example.com/app:buildcache   --cache-to type=registry,ref=registry.example.com/app:buildcache,mode=max   .
```

### Expected Evidence

A later CI runner can reuse cache without sharing local disk.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Separate caches across trust boundaries and do not treat cache as authoritative source code.

---

## Advanced Deep Dive 36 — Buildx Builder Drivers

### Concept

Buildx can use different builder drivers, which affects isolation, multi-platform support, output behavior, and cache/storage location.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker buildx ls
docker buildx inspect --bootstrap
```

### Expected Evidence

The active builder driver, nodes, and supported platforms are visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Inspect the builder before diagnosing multi-platform or cache behavior.

---

## Advanced Deep Dive 37 — Multi-Platform Emulation vs Native Build

### Concept

QEMU-style emulation is convenient for cross-architecture builds but can be much slower and can expose emulation-specific test behavior. Native builders or cross-compilation may be better.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker buildx inspect --bootstrap
uname -m
```

### Expected Evidence

Supported build platforms can be compared with the local host architecture.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use native builders for heavy architecture-specific compilation when practical.

---

## Advanced Deep Dive 38 — Cross-Compilation Stage Pattern

### Concept

Languages such as Go can compile for a target platform in one stage, then copy the target binary into a minimal runtime stage.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
FROM --platform=$BUILDPLATFORM golang:1.25 AS build
ARG TARGETOS TARGETARCH
RUN GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /out/app ./cmd/app
```

### Expected Evidence

One builder can produce architecture-specific binaries without emulating the full target userspace.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Prefer language-native cross-compilation when it is well supported.

---

## Advanced Deep Dive 39 — Build Provenance

### Concept

Build provenance should bind image digest to source commit, builder identity, and build parameters so production can prove where an artifact came from.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
source commit
  ↓ trusted builder
provenance
  ↓ image digest
```

### Expected Evidence

A release record maps exact artifact bytes to an authorized build.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Store provenance alongside immutable image digests.

---

## Advanced Deep Dive 40 — SBOM Build Output

### Concept

An SBOM describes packages/components in the image. It is most valuable when indexed so a new vulnerability can map component → image → deployment.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
image digest
  └─ SBOM
       ├─ OS packages
       └─ language packages
```

### Expected Evidence

Security teams can identify affected artifacts without manually opening every image.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Generate and retain SBOMs for release images.

---

## Advanced Deep Dive 41 — Multi-Stage Test Gate

### Concept

A Dockerfile can include a test stage that installs test-only tools while the final runtime stage remains minimal.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
FROM base AS test
RUN pytest -q

FROM base AS runtime
COPY --from=build /app /app
```

### Expected Evidence

CI can fail before the runtime image is published while keeping test dependencies out of production.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Separate build/test/runtime concerns into explicit stages.

---

## Advanced Deep Dive 42 — Distroless Debug Strategy

### Concept

Minimal/distroless images improve runtime surface but intentionally remove shell and tools. Debugging should use logs, tracing, a matching debug image, or an isolated reproduction.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
prod image: app + runtime only
debug image: same app version + shell/curl/strace
```

### Expected Evidence

Production remains minimal while operators still have a controlled diagnostic path.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Do not add permanent admin tooling to production solely for convenience.

---

## Advanced Deep Dive 43 — Base Image Digest Updates

### Concept

Digest pinning makes builds reproducible, but it also stops automatic security refresh. Dependency automation must intentionally update pinned base digests.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```dockerfile
FROM python:3.13-slim@sha256:<approved-digest>
```

### Expected Evidence

The build uses exact base content and updates occur through reviewed changes.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Pair digest pinning with scheduled dependency/security update automation.

---

## Advanced Deep Dive 44 — Image Promotion by Digest

### Concept

Build once, test the exact digest, then promote/tag/reference that digest in production rather than rebuilding.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
build digest D
  ↓ test D
  ↓ scan/sign D
  ↓ production deploy D
```

### Expected Evidence

Production receives byte-identical image content to the tested artifact.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use digest as the release identity and tags as human metadata.

---

## Advanced Deep Dive 45 — Registry Credential Helper

### Concept

Docker credential helpers keep registry credentials out of plaintext-ish Docker config entries and integrate with OS/cloud credential stores.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
cat ~/.docker/config.json 2>/dev/null | sed -n '1,80p'
```

### Expected Evidence

The configuration indicates helper/store use rather than embedded reusable passwords where supported.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use credential helpers or short-lived cloud tokens for registry authentication.

---

## Advanced Deep Dive 46 — Registry Token Scope

### Concept

CI should receive only the repository actions it needs: typically push to a build repository; runtime hosts need pull; deletion/admin should be separate.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
CI builder: pull base + push app
runtime: pull app
retention bot: delete expired
registry admin: separate
```

### Expected Evidence

Registry privileges are separated by workload role.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Apply least privilege to registry actions just like cloud IAM.

---

## Advanced Deep Dive 47 — Private Registry TLS

### Concept

A private registry needs valid TLS identity and client trust. Disabling verification to fix certificate errors weakens supply-chain transport trust.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
openssl s_client -connect registry.example.com:443   -servername registry.example.com </dev/null 2>/dev/null | head
```

### Expected Evidence

The presented certificate chain/hostname can be inspected.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Fix CA trust, chain, hostname, proxy, or clock rather than marking production registries insecure.

---

## Advanced Deep Dive 48 — Registry Mirror / Pull-Through Cache

### Concept

A mirror or pull-through cache reduces repeated upstream downloads and can improve availability, but it becomes trusted supply-chain infrastructure that needs TLS, access control, storage, and lifecycle.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
build hosts
  ↓
trusted registry cache
  ↓
upstream public registry
```

### Expected Evidence

The cache reduces external pulls without bypassing image integrity/security checks.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Secure and monitor mirrors like production registries.

---

## Advanced Deep Dive 49 — Image Scan Context

### Concept

A vulnerability scanner reports package risk at a point in time. New CVEs can appear after build, and scanners do not detect authorization bugs or unsafe runtime configuration.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
build scan
  +
continuous image inventory
  +
runtime hardening
  +
secure coding
```

### Expected Evidence

Scanning is treated as one layer rather than proof that the image is secure.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Re-scan deployed digests as vulnerability intelligence changes.

---

## Advanced Deep Dive 50 — Signature vs Digest

### Concept

An image digest proves exact content; a signature proves a trusted identity approved that digest. Both are needed for strong artifact trust.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
sha256 digest → integrity
signature       → signer authenticity/approval
provenance      → build claims
```

### Expected Evidence

Release policy distinguishes integrity from publisher trust.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Verify signatures/attestations against immutable digests.

---

## Advanced Deep Dive 51 — Runtime Image Policy

### Concept

A production platform can enforce approved registry, digest pinning, non-root, no privileged mode, required limits, and trusted signature/provenance.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
release request
  ↓ policy checks
approved?
  ├─ yes → run
  └─ no  → block
```

### Expected Evidence

Unsafe artifacts/configurations are rejected before runtime.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Convert recurring review rules into policy-as-code when the platform supports it.

---

## Advanced Deep Dive 52 — Default Bridge vs User-Defined Bridge

### Concept

User-defined bridges provide scoped DNS/service-name resolution and better application isolation compared with treating the default bridge as the primary multi-service design.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker network create appnet
docker network inspect appnet
```

### Expected Evidence

The network has its own subnet, gateway, and attached containers.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Create one or more application networks rather than depending on default bridge behavior.

---

## Advanced Deep Dive 53 — Embedded Docker DNS

### Concept

On user-defined networks, Docker provides service/container-name resolution through an embedded DNS mechanism. Names are stable; IPs can change.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker exec <CLIENT> getent hosts <SERVICE> 2>/dev/null || true
docker exec <CLIENT> cat /etc/resolv.conf 2>/dev/null || true
```

### Expected Evidence

The service name resolves inside the shared network.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use service names, not container IPs.

---

## Advanced Deep Dive 54 — Application Bind Address

### Concept

A web server listening on `127.0.0.1` inside the container is only reachable from that network namespace. Other containers and published ports generally need the app to listen on an appropriate container interface such as `0.0.0.0`.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker exec <CONTAINER> ss -lntp 2>/dev/null || true
```

### Expected Evidence

The listening address and port match the intended client path.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Check the application socket before changing Docker networking.

---

## Advanced Deep Dive 55 — Published-Port Exposure

### Concept

`-p 8080:80` may bind on all suitable host interfaces, while `127.0.0.1:8080:80` limits host exposure to loopback.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker ps --format 'table {{.Names}}\t{{.Ports}}'
ss -lntp
```

### Expected Evidence

The real host bind address is visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Publish only the entrypoint ports and bind to the narrowest host interface.

---

## Advanced Deep Dive 56 — Docker Firewall Interaction

### Concept

Docker programs host firewall/NAT rules to implement bridge networking and published ports. Host firewall policy must account for Docker-managed chains/rules.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
sudo iptables -S 2>/dev/null | grep -E 'DOCKER|FORWARD' | head -40 || true
sudo nft list ruleset 2>/dev/null | grep -i docker | head -40 || true
```

### Expected Evidence

Docker-managed filtering/NAT rules are visible on the host where applicable.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Test host-firewall changes with Docker networking instead of assuming rule order.

---

## Advanced Deep Dive 57 — DOCKER-USER Policy Concept

### Concept

On iptables-based setups, the DOCKER-USER chain provides a place for administrator filtering before Docker's forwarding accept logic. Exact backend behavior should be verified on the host.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
sudo iptables -S DOCKER-USER 2>/dev/null || true
```

### Expected Evidence

Host-level policy rules are distinguishable from automatically generated Docker rules.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Place administrator policy in supported extension points rather than editing Docker-managed rules manually.

---

## Advanced Deep Dive 58 — Network Namespace Inspection

### Concept

Docker metadata maps a container to a host PID; `nsenter` can inspect the actual container network namespace from an authorized Linux host.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
PID=$(docker inspect -f '{{.State.Pid}}' <CONTAINER>)
sudo nsenter -t "$PID" -n ip addr
sudo nsenter -t "$PID" -n ip route
```

### Expected Evidence

The actual interface, route table, and namespace network state are visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use namespace evidence when Docker-level inspection is insufficient.

---

## Advanced Deep Dive 59 — DNS Failure Decomposition

### Concept

Separate name resolution from packet reachability. If an IP works but a name fails, inspect resolver configuration, search domains, host/VPN DNS, and container network membership.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker exec <CONTAINER> cat /etc/resolv.conf
docker exec <CONTAINER> getent hosts example.com || true
```

### Expected Evidence

DNS failure is distinguished from routing or application failure.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Do not change bridge subnets to fix a resolver-only problem.

---

## Advanced Deep Dive 60 — Corporate VPN Overlap

### Concept

VPN routes can overlap Docker bridge address pools, sending container traffic toward the wrong next hop. Default address pools should be planned around enterprise CIDRs.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
ip route
docker network ls
docker network inspect <NETWORK>
```

### Expected Evidence

Docker subnet overlap with VPN/LAN ranges can be identified.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Plan non-overlapping container address pools before large-scale developer rollout.

---

## Advanced Deep Dive 61 — MTU Diagnosis

### Concept

VPNs, overlays, and cloud tunnels reduce effective MTU. Small requests can work while large TLS/data transfers hang.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
ip link
docker network inspect <NETWORK> 2>/dev/null || true
ping -M do -s 1400 <AUTHORIZED_TARGET> 2>/dev/null || true
```

### Expected Evidence

Host/network MTUs and path behavior can be compared.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Account for tunnel overhead instead of disabling TLS or changing application timeouts first.

---

## Advanced Deep Dive 62 — Host Network Trade-Off

### Concept

`--network host` removes the container's separate network namespace on supported Linux hosts, reducing network isolation and causing direct port conflicts.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm --network host alpine ip addr
```

### Expected Evidence

The container sees the host network namespace state.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use host networking only when a measured compatibility/performance requirement justifies it.

---

## Advanced Deep Dive 63 — None Network

### Concept

`--network none` provides a container with loopback but no normal Docker external network, useful for isolated processing jobs.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm --network none alpine ip addr
```

### Expected Evidence

Only isolated loopback-style networking is available.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use no-network execution for jobs that do not need network access.

---

## Advanced Deep Dive 64 — macvlan / ipvlan Decision

### Concept

macvlan and ipvlan give containers more direct L2/L3 presence but introduce switch, host-reachability, IPAM, and security complexity.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
bridge → host-mediated container subnet
macvlan → container appears as distinct L2 endpoint
ipvlan → shared/controlled L2 identity with distinct IP behavior
```

### Expected Evidence

The chosen driver is tied to a real legacy/network-integration requirement.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Prefer bridge networking unless direct network presence is required.

---

## Advanced Deep Dive 65 — Container Connection Refused vs Timeout

### Concept

Connection refused usually suggests the destination path was reached but no listener/active accept path exists; timeout more often points to path filtering, routing, or a hung service.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker exec <CLIENT> getent hosts <SERVICE>
docker exec <CLIENT> sh -c 'nc -vz -w2 <SERVICE> <PORT>' 2>/dev/null || true
```

### Expected Evidence

The failure mode helps narrow listener versus network-path investigation.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use the error semantics as a clue, not an absolute diagnosis.

---

## Advanced Deep Dive 66 — Container Resource Defaults

### Concept

Docker containers have no application-specific CPU/memory/PID limits unless configured. A noisy or compromised container can therefore consume host capacity.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format 'Memory={{.HostConfig.Memory}} NanoCPUs={{.HostConfig.NanoCpus}} Pids={{.HostConfig.PidsLimit}}'
```

### Expected Evidence

Zero/unset values reveal missing hard limits.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Set intentional resource controls from measured workload behavior.

---

## Advanced Deep Dive 67 — Memory Reservation vs Hard Limit

### Concept

Docker can express a softer memory reservation and a hard memory ceiling depending on host/kernel behavior. The hard ceiling protects the host; the softer target influences pressure behavior.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format 'Memory={{.HostConfig.Memory}} Reservation={{.HostConfig.MemoryReservation}}'
```

### Expected Evidence

Hard and reservation values can be compared.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Size memory from startup peak, steady working set, and failure behavior.

---

## Advanced Deep Dive 68 — OOM Evidence

### Concept

Exit code 137 is not enough to prove OOM. Inspect `.State.OOMKilled`, daemon/kernel logs, and cgroup memory events.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format 'Exit={{.State.ExitCode}} OOM={{.State.OOMKilled}}'
journalctl -k --since '-10 min' | grep -i -E 'oom|out of memory' | tail -20
```

### Expected Evidence

The investigation produces direct evidence for or against OOM.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Confirm OOM before raising memory limits.

---

## Advanced Deep Dive 69 — CPU Quota vs Shares

### Concept

`--cpus` limits CPU time; CPU shares/weight influence relative scheduling under contention. A high share value does not override a strict quota.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format 'NanoCPUs={{.HostConfig.NanoCpus}} CpuShares={{.HostConfig.CpuShares}}'
```

### Expected Evidence

Absolute and relative CPU controls are visible separately.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use quota for containment and shares/weight for relative fairness.

---

## Advanced Deep Dive 70 — CPU Throttling Diagnosis

### Concept

A container can show moderate CPU but still be latency-bound because its cgroup is throttled by quota.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
PID=$(docker inspect -f '{{.State.Pid}}' <CONTAINER>)
cat /proc/$PID/cgroup
docker stats --no-stream <CONTAINER>
```

### Expected Evidence

Container runtime stats can be correlated with the underlying cgroup.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Investigate throttling counters when latency rises under CPU limits.

---

## Advanced Deep Dive 71 — PIDs Limit

### Concept

`--pids-limit` prevents runaway process/thread creation from consuming the host process table.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format '{{.HostConfig.PidsLimit}}'
docker stats --no-stream <CONTAINER>
```

### Expected Evidence

The configured PID ceiling and current PIDs are visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Set realistic PID limits for services with bounded concurrency models.

---

## Advanced Deep Dive 72 — ulimits

### Concept

Process limits such as open file descriptors can fail before CPU or memory. Docker can set per-container ulimits.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm --ulimit nofile=1024:1024 alpine sh -c 'ulimit -n'
```

### Expected Evidence

The process reports the configured file-descriptor ceiling.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Capacity-plan file descriptors for high-concurrency servers.

---

## Advanced Deep Dive 73 — Shared Memory Size

### Concept

The default `/dev/shm` size can be too small for browsers, databases, or multiprocessing workloads that rely on POSIX shared memory.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm alpine df -h /dev/shm
```

### Expected Evidence

The runtime shared-memory filesystem size is visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Increase shared memory only for workloads that actually require it.

---

## Advanced Deep Dive 74 — Read-Only Root + Explicit Writes

### Concept

A hardened container can run with `--read-only` while writable `/tmp`, runtime state, and durable data are mounted explicitly.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm --read-only --tmpfs /tmp alpine   sh -c 'touch /tmp/ok; touch /fail 2>&1 || true'
```

### Expected Evidence

Temporary writes succeed only on approved writable mounts.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use read-only root filesystems for compatible stateless services.

---

## Advanced Deep Dive 75 — Capability Minimization

### Concept

Most applications need far fewer capabilities than the default set. Start from `--cap-drop ALL` and add one capability only when the application proves it requires it.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm --cap-drop ALL alpine sh -c 'grep ^Cap /proc/self/status'
```

### Expected Evidence

The process runs with a minimal capability mask.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Solve privilege errors with the narrow required capability, not `--privileged`.

---

## Advanced Deep Dive 76 — no-new-privileges

### Concept

The no-new-privileges security option prevents exec transitions from gaining new privilege through setuid/setgid or file capabilities.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker run --rm --security-opt no-new-privileges:true alpine   sh -c "grep NoNewPrivs /proc/self/status"
```

### Expected Evidence

The container process reports NoNewPrivs enabled.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use no-new-privileges for ordinary application containers.

---

## Advanced Deep Dive 77 — Seccomp Failure Diagnosis

### Concept

If hardening blocks a syscall, diagnose the exact syscall/profile behavior rather than disabling seccomp globally.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
application error
  ↓ check audit/runtime evidence
identify syscall
  ↓
is syscall truly needed?
  ├─ yes → narrow reviewed exception
  └─ no  → fix application
```

### Expected Evidence

The remediation is scoped to the real syscall requirement.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Treat `seccomp=unconfined` only as a temporary controlled diagnostic step, not a production fix.

---

## Advanced Deep Dive 78 — AppArmor / SELinux Mount Denials

### Concept

Unix permissions can look correct while an LSM blocks access. Host audit logs and labels are required evidence.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
sudo dmesg | grep -i -E 'apparmor.*denied|avc:.*denied' | tail -30 2>/dev/null || true
```

### Expected Evidence

Security-module denials identify the affected path/profile/type where supported.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Fix labels/profile policy rather than chmod 777 or disabling the LSM.

---

## Advanced Deep Dive 79 — Rootless Docker Threat Reduction

### Concept

Rootless Docker moves the daemon and containers under an unprivileged host account, reducing the impact of daemon compromise while introducing networking/cgroup/device limitations.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker info | grep -i -E 'rootless|security options' -A5 || true
id
```

### Expected Evidence

The operator can determine whether the active Engine is rootless.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use rootless where its feature/performance trade-offs fit the workload.

---

## Advanced Deep Dive 80 — userns-remap vs Rootless

### Concept

User namespace remapping can map container root to unprivileged host IDs while dockerd itself remains rootful. Rootless mode also runs the daemon without host root.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
userns-remap:
rootful dockerd
  ↓ mapped container IDs

rootless:
unprivileged dockerd
  ↓ mapped container IDs
```

### Expected Evidence

The security model distinguishes daemon privilege from container UID mapping.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Choose the model intentionally instead of treating both features as equivalent.

---

## Advanced Deep Dive 81 — Host PID / Host IPC / Host Network Risk

### Concept

Sharing host namespaces removes important isolation boundaries and exposes host process/network/IPC state to the container.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
ordinary app:
private PID + network + IPC

host namespace sharing:
reduced isolation
larger blast radius
```

### Expected Evidence

Any use of host namespace sharing has a documented infrastructure requirement.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Never enable host namespaces to solve an unrelated connectivity or permission issue.

---

## Advanced Deep Dive 82 — Device Access

### Concept

Passing devices changes the container threat and reliability model. GPU, block, USB, or character devices may require additional runtime configuration and permissions.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format '{{json .HostConfig.Devices}}' 2>/dev/null || true
```

### Expected Evidence

Granted host devices are visible and auditable.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Expose only exact required devices and keep them out of ordinary web workloads.

---

## Advanced Deep Dive 83 — Compose Project Isolation

### Concept

Compose prefixes resources with a project name so multiple copies of the same topology can coexist. Project naming therefore affects network/volume/resource identity.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose ls
docker compose -p lab1 ps
```

### Expected Evidence

Compose resources can be attributed to a project boundary.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Set explicit project names in CI and shared hosts to avoid collisions.

---

## Advanced Deep Dive 84 — Compose Config as Source of Truth

### Concept

`docker compose config` renders merged files, interpolation, profiles, networks, and volumes. It is the best first command for configuration surprises.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose config
```

### Expected Evidence

The normalized configuration shows what Compose will actually apply.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Debug the rendered configuration before editing service code.

---

## Advanced Deep Dive 85 — Compose Environment Precedence

### Concept

Image ENV, env_file, compose `environment`, interpolation sources, and CLI overrides can produce unexpected values. The final container environment should be inspected.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose config
docker compose exec <SERVICE> env | sort
```

### Expected Evidence

The declared and actual runtime environment can be compared.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Document configuration ownership and avoid duplicating the same variable across many precedence layers.

---

## Advanced Deep Dive 86 — Compose Secrets Are Not Magic Encryption

### Concept

Local Compose secrets are typically mounted from host-managed sources. They avoid baking secrets into images/environment, but security still depends on host file storage, permissions, and lifecycle.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```yaml
services:
  api:
    secrets:
      - db_password
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### Expected Evidence

The secret is mounted as a file rather than stored in the image.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Protect the underlying secret source and never commit it to Git.

---

## Advanced Deep Dive 87 — Compose depends_on vs Runtime Resilience

### Concept

`depends_on` can coordinate startup ordering/health conditions, but it does not solve dependency failure after startup. Applications still need timeout, retry, and graceful degradation.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
startup:
Compose health ordering

runtime:
DB restarts later
  ↓
application retry/backoff/reconnect still required
```

### Expected Evidence

The application can recover from dependency restart after the stack is already running.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use Compose dependency logic for startup convenience, not as a substitute for resilient application design.

---

## Advanced Deep Dive 88 — Compose Healthcheck Design

### Concept

Health checks should be cheap, deterministic, and scoped. Liveness-style checks should not create cascading restarts because a remote optional dependency is slow.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```yaml
healthcheck:
  test: ["CMD", "wget", "-qO-", "http://127.0.0.1:8080/health"]
  interval: 30s
  timeout: 3s
  retries: 3
```

### Expected Evidence

Health status reflects useful local service state without excessive load.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Separate local process health from external dependency readiness when possible.

---

## Advanced Deep Dive 89 — Compose Profiles

### Concept

Profiles let optional debug/admin/observability services stay out of the default stack while remaining reproducible when needed.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```yaml
services:
  adminer:
    image: adminer
    profiles: ["debug"]
```

### Expected Evidence

The optional service starts only when its profile is activated.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Keep privileged or debug tooling opt-in and disabled by default.

---

## Advanced Deep Dive 90 — Compose Override Discipline

### Concept

Multiple Compose files are useful for dev/prod differences, but merge behavior can be non-obvious. Every deployment should render and review the final config.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose -f compose.yaml -f compose.prod.yaml config > rendered.yaml
```

### Expected Evidence

The final merged model is captured before deployment.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Review rendered Compose configuration in CI.

---

## Advanced Deep Dive 91 — Compose Scaling and Fixed Ports

### Concept

Scaling a service to multiple replicas conflicts with fixed host-port bindings because only one process can own a specific host IP:port.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose up -d --scale worker=3
docker compose ps
```

### Expected Evidence

Replicated services without fixed published ports scale cleanly.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Publish only entrypoint/proxy ports; keep scalable workers on internal networks.

---

## Advanced Deep Dive 92 — Compose Network Least Privilege

### Concept

A service should join only networks it needs. Database and cache services generally do not need the public-facing frontend network.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```yaml
services:
  api:
    networks: [frontend, backend]
  db:
    networks: [backend]
```

### Expected Evidence

The topology prevents direct frontend-network access to the database.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Treat network membership as a least-privilege control.

---

## Advanced Deep Dive 93 — Compose Volume Destruction

### Concept

`docker compose down -v` removes project volumes. For stateful stacks this can permanently destroy local database data.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose volumes 2>/dev/null || true
docker volume ls
```

### Expected Evidence

Operators can identify persistent volumes before destructive teardown.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Separate disposable test stacks from data-bearing environments and require confirmation for volume deletion.

---

## Advanced Deep Dive 94 — Compose Read-Only Service

### Concept

Compose can combine `read_only`, tmpfs, non-root user, capability drop, and no-new-privileges for a hardened stateless service.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```yaml
services:
  api:
    read_only: true
    tmpfs: [/tmp]
    cap_drop: [ALL]
    security_opt:
      - no-new-privileges:true
```

### Expected Evidence

The service can start without broad writable/privileged defaults.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Harden from a working least-privilege baseline and document required exceptions.

---

## Advanced Deep Dive 95 — Compose One-Off Jobs

### Concept

`docker compose run --rm` starts a new one-off container from service configuration; `exec` runs a command inside an existing service container. They have different lifecycle/network implications.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose run --rm api pytest
docker compose exec api sh -c 'id'
```

### Expected Evidence

The operator can distinguish ephemeral job execution from in-place diagnostics.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use `run --rm` for jobs/tests and `exec` for temporary investigation.

---

## Advanced Deep Dive 96 — Logging Driver Selection

### Concept

Docker logging drivers differ in local storage, rotation, buffering, and external-delivery behavior. The application should usually log to stdout/stderr while the platform handles routing.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker info --format '{{.LoggingDriver}}'
docker inspect <CONTAINER> --format '{{json .HostConfig.LogConfig}}' 2>/dev/null || true
```

### Expected Evidence

The daemon default and container-specific logging settings are known.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Choose a driver and retention model that cannot fill the host silently.

---

## Advanced Deep Dive 97 — Blocking vs Non-Blocking Logging Concept

### Concept

A logging pipeline can create backpressure. If writes block on a slow log driver, application performance can degrade; non-blocking buffers trade durability for availability.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
app stdout
  ↓ logging driver
  ↓ buffer
external collector

collector slow:
blocking → app may stall
non-blocking → buffer/drop policy matters
```

### Expected Evidence

Logging failure behavior is explicitly understood.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Decide whether logs may be dropped versus allowed to block application throughput.

---

## Advanced Deep Dive 98 — Log Rotation

### Concept

Unbounded local container logs are a common cause of host disk exhaustion. Rotation limits should be defined before high-volume production use.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format '{{json .HostConfig.LogConfig}}'
docker system df -v
```

### Expected Evidence

Log-driver options and Docker disk usage are visible.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Set log size/retention limits and monitor the host filesystem.

---

## Advanced Deep Dive 99 — Docker Events as Timeline

### Concept

`docker events` provides a control-plane timeline for create/start/die/kill/health/network/volume events and is useful during intermittent failures.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker events --since 10m
```

### Expected Evidence

Lifecycle events can be correlated with application logs and host events.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Capture event timelines during restart loops and unexplained container replacement.

---

## Advanced Deep Dive 100 — docker inspect Release Evidence

### Concept

`docker inspect` exposes image reference, command, environment, mounts, network, security options, limits, and runtime state. A targeted snapshot is valuable incident evidence.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> > inspect.json
docker inspect <CONTAINER> --format 'Image={{.Image}} User={{.Config.User}} Privileged={{.HostConfig.Privileged}}'
```

### Expected Evidence

The exact runtime configuration is preserved for analysis.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Capture inspect output before replacing a failing container.

---

## Advanced Deep Dive 101 — docker diff for Drift

### Concept

`docker diff` reveals writable-layer additions/changes/deletions, useful for discovering unexpected runtime mutation.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker diff <CONTAINER> | head -100
```

### Expected Evidence

Unexpected modified paths can be identified.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Treat significant runtime drift as a signal to fix image/configuration rather than preserving the mutated container.

---

## Advanced Deep Dive 102 — docker system df

### Concept

`docker system df -v` separates disk usage among images, containers, volumes, and build cache so cleanup targets the real consumer.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker system df
docker system df -v
```

### Expected Evidence

Disk pressure is attributed to a Docker object category.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Inspect usage before pruning anything.

---

## Advanced Deep Dive 103 — Prune Safety

### Concept

Prune commands delete objects considered unused by Docker, but an 'unused' image, volume, or cache can still be operationally valuable for rollback or recovery.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
before prune:
inventory
owner
backup/rollback need
exact command scope
dry-run style review where possible
```

### Expected Evidence

Deletion scope is reviewed before execution.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Never run broad prune commands blindly on important hosts.

---

## Advanced Deep Dive 104 — Inode Exhaustion

### Concept

Docker hosts can fail writes even with free GB when filesystems run out of inodes, especially under heavy layer/log/small-file workloads.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
df -h
df -i
docker system df -v
```

### Expected Evidence

Byte capacity and inode capacity are evaluated independently.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Monitor both disk space and inode pressure.

---

## Advanced Deep Dive 105 — Daemon Metrics / Host Monitoring Concept

### Concept

Container stats alone are not enough. Production monitoring should include Docker daemon health, host CPU/memory/PSI, filesystem, network, runtime restarts, and application SLOs.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
host:
CPU memory PSI disk inode network

Docker:
daemon availability events container restarts

app:
requests errors latency business KPI
```

### Expected Evidence

The monitoring design covers platform and service layers.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Alert on user/service impact and use container/host metrics for diagnosis.

---

## Advanced Deep Dive 106 — docker stats Limitations

### Concept

`docker stats` is useful for live resource inspection but is not a durable historical monitoring system and does not explain application-level health.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker stats --no-stream
```

### Expected Evidence

A point-in-time resource snapshot is available.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Export long-term metrics to a monitoring system and correlate with application telemetry.

---

## Advanced Deep Dive 107 — Health Status vs Restart

### Concept

Docker HEALTHCHECK updates container health state, but standalone Engine restart policy is based primarily on process lifecycle, not a universal 'restart unhealthy' behavior.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format '{{json .State.Health}}' 2>/dev/null || true
```

### Expected Evidence

Health history and process running state can be different.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use orchestration/supervision logic explicitly if unhealthy state should trigger replacement.

---

## Advanced Deep Dive 108 — Restart Loop Backoff Awareness

### Concept

Automatic restart can hide a deterministic failure and flood logs/CPU. Operators need restart counts, exit codes, and application root-cause evidence.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format 'RestartCount={{.RestartCount}} Exit={{.State.ExitCode}} Error={{.State.Error}}'
```

### Expected Evidence

Crash-loop evidence is visible without manually restarting again.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Fix the failing entrypoint/config/dependency instead of relying on infinite restart.

---

## Advanced Deep Dive 109 — Graceful HTTP Shutdown

### Concept

A web service should stop accepting new requests on SIGTERM, drain in-flight work, close dependencies, and exit before Docker's stop timeout.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
docker stop
  ↓ SIGTERM
server stops accept
  ↓ drain requests
close DB/queue
  ↓ exit 0
```

### Expected Evidence

Normal stop does not require SIGKILL.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Set stop timeout from measured worst-case drain time.

---

## Advanced Deep Dive 110 — Queue Worker Shutdown

### Concept

A queue consumer must define what happens to an in-flight message during stop: acknowledge only after durable completion or release/return the work safely.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
SIGTERM
  ↓ stop fetching
finish/rollback current message
  ↓ ack only after success
close
  ↓ exit
```

### Expected Evidence

Stopping the container does not silently lose or duplicate business work.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Design graceful stop around message acknowledgement semantics.

---

## Advanced Deep Dive 111 — Time Synchronization

### Concept

Containers normally use the host kernel clock. Large host drift breaks TLS, tokens, logs, and distributed coordination across every container on that host.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
timedatectl status
date -Is
docker run --rm alpine date
```

### Expected Evidence

Host and container time are consistent.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Fix host time synchronization rather than configuring independent container clocks.

---

## Advanced Deep Dive 112 — Proxy Layers

### Concept

Corporate proxy configuration can exist at daemon pull time, build time, and application runtime. Fixing only one layer leaves confusing partial connectivity.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
dockerd proxy → image pulls
BuildKit/build proxy → package downloads
container env proxy → application egress
NO_PROXY → internal services
```

### Expected Evidence

Each network client uses the intended proxy/no-proxy configuration.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Document proxy configuration by layer.

---

## Advanced Deep Dive 113 — NO_PROXY Design

### Concept

Incorrect `NO_PROXY` can send internal service traffic through a corporate proxy or bypass required proxy paths. CIDRs, hostnames, and service domains should be tested.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
env | grep -i proxy
docker exec <CONTAINER> env | grep -i proxy 2>/dev/null || true
```

### Expected Evidence

Runtime proxy variables match internal/external routing needs.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Test internal service names and cloud metadata/private endpoints explicitly.

---

## Advanced Deep Dive 114 — Registry Pull Failure Workflow

### Concept

Pull failures should be decomposed into reference, DNS, TLS, proxy, authentication, authorization, manifest/platform, and rate-limit stages.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker pull <IMAGE>
docker manifest inspect <IMAGE> 2>/dev/null | head -60 || true
```

### Expected Evidence

The failure is tied to a specific registry stage.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Do not solve TLS/auth errors by marking the registry insecure.

---

## Advanced Deep Dive 115 — Wrong Architecture

### Concept

`exec format error` often means the pulled image/binary does not match the host architecture or the image index lacks the requested platform.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
uname -m
docker image inspect <IMAGE> --format '{{.Os}}/{{.Architecture}}'
```

### Expected Evidence

Host and image platform are directly compared.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Publish and test every required platform in multi-architecture releases.

---

## Advanced Deep Dive 116 — Container Immediately Exits

### Concept

A container only stays running while its primary process is running. Wrong CMD/ENTRYPOINT, missing config, permission error, or one-shot command leads to immediate exit.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker ps -a
docker inspect <CONTAINER> --format 'Exit={{.State.ExitCode}} Error={{.State.Error}} Cmd={{json .Config.Cmd}} Entry={{json .Config.Entrypoint}}'
docker logs <CONTAINER>
```

### Expected Evidence

Exit code, error, entrypoint, command, and logs are available.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Diagnose the primary process before adding restart policies.

---

## Advanced Deep Dive 117 — Volume Permission Failure

### Concept

A mount permission problem can come from UID/GID, read-only option, host ACL, SELinux/AppArmor, or filesystem ownership.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker inspect <CONTAINER> --format '{{json .Mounts}}'
docker exec <CONTAINER> id 2>/dev/null || true
ls -ldn <HOST_PATH> 2>/dev/null || true
```

### Expected Evidence

Identity and mount ownership/options are compared.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Fix the exact permission layer instead of using root or chmod 777.

---

## Advanced Deep Dive 118 — Published Port Failure

### Concept

A published port requires a running container, correct host binding, Docker firewall/NAT, and an application listening on the container port/address.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker ps
docker port <CONTAINER>
docker exec <CONTAINER> ss -lntp 2>/dev/null || true
ss -lntp
```

### Expected Evidence

The host mapping and container listener can be verified separately.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Check the listener before changing host firewall.

---

## Advanced Deep Dive 119 — Compose Dependency Failure

### Concept

If a Compose service cannot reach another service, verify shared network, service-name DNS, target container port, listener bind address, health, and credentials.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker compose ps
docker compose exec <CLIENT> getent hosts <TARGET>
docker compose exec <CLIENT> sh -c 'nc -vz -w2 <TARGET> <PORT>' 2>/dev/null || true
```

### Expected Evidence

DNS and TCP reachability are tested from the real client service.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Troubleshoot from inside the client container, not only from the host.

---

## Advanced Deep Dive 120 — Disk Pressure Incident

### Concept

Docker builds, pulls, logs, writable layers, and databases can all fail when the host filesystem is full. Manual deletion under Docker's data root can make the incident worse.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
df -h
df -i
docker system df -v
```

### Expected Evidence

The largest capacity consumer is identified safely.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Free space through known Docker objects/log policy, not by deleting internal metadata files.

---

## Advanced Deep Dive 121 — Build Failure Network Decomposition

### Concept

A package download failure during build can come from BuildKit network namespace, DNS, proxy, CA trust, repository outage, rate limit, or target architecture.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker buildx inspect --bootstrap
docker build --progress=plain .
```

### Expected Evidence

Plain build output exposes the failing fetch/install step.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Debug build networking independently from runtime container networking.

---

## Advanced Deep Dive 122 — Build Reproducibility Evidence

### Concept

Release builds should record source commit, Dockerfile hash, base digest, dependency lock, builder version, build args, image digest, and provenance.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
commit=...
dockerfile_sha=...
base_digest=...
builder=...
image_digest=...
sbom=...
provenance=...
```

### Expected Evidence

A later incident can reconstruct the exact release inputs.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Make reproducibility metadata part of the CI artifact record.

---

## Advanced Deep Dive 123 — CI Least Privilege

### Concept

CI needs permission to read source, pull bases, push application images, and possibly deploy. It does not need registry administration or host root on unrelated systems.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
CI:
source read
registry pull/push scoped repo
sign/attest
deploy scoped environment

not:
global registry admin
host root everywhere
```

### Expected Evidence

Build identity permissions match the pipeline actions.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Separate build, deploy, and runtime identities.

---

## Advanced Deep Dive 124 — Build Runner Isolation

### Concept

Builds execute untrusted or semi-trusted source scripts. Shared long-lived runners can leak credentials/cache/workspace state across projects if not isolated.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
job
  ↓ ephemeral runner/builder
scoped credentials
  ↓ destroy after job
```

### Expected Evidence

Build jobs do not inherit stale credentials or workspace artifacts from unrelated projects.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Prefer ephemeral isolated builders for sensitive CI.

---

## Advanced Deep Dive 125 — Secret Leakage in Logs

### Concept

Even BuildKit secrets can leak if the build script echoes them, enables shell tracing, embeds them in URLs, or prints package-manager diagnostics.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```sh
set +x
# consume secret without echoing it
```

### Expected Evidence

Build logs contain no reusable credential material.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Redact logs and disable shell tracing around secret-handling steps.

---

## Advanced Deep Dive 126 — Dockerfile Lint / Policy Gate

### Concept

CI can statically reject dangerous Dockerfile patterns such as root runtime, secret-like COPY, unpinned critical base, privileged assumptions, or missing health metadata.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
policy examples:
USER must be non-root
no COPY *.pem
no secret ARG names
approved base registries
required OCI labels
```

### Expected Evidence

Unsafe patterns fail before image publication.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Automate repeatable Dockerfile review rules.

---

## Advanced Deep Dive 127 — Release Rollback

### Concept

Rollback requires retaining the previous known-good image digest and compatible database/configuration state. A mutable tag is not a reliable rollback artifact.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
current digest D2 fails
  ↓
shift/deploy previous digest D1
  ↓
verify
```

### Expected Evidence

Rollback can select an exact prior artifact.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Retain immutable release digests for the full rollback/support window.

---

## Advanced Deep Dive 128 — Schema Migration Compatibility

### Concept

Container rollback can fail if the new version already applied a destructive database migration. Application and schema deployment must use backward-compatible sequencing.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
expand schema
  ↓ deploy old+new compatible app
migrate data
  ↓ contract later
```

### Expected Evidence

Both old and new application versions can operate during the rollout window.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use expand/contract database migrations for reversible deployments.

---

## Advanced Deep Dive 129 — Operational Readiness Review

### Concept

A production Docker workload needs owner/on-call, image provenance, resource limits, health, graceful shutdown, network exposure review, persistent backup/restore, log retention, security options, and rollback.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
[ ] immutable digest
[ ] non-root
[ ] limits
[ ] health
[ ] graceful stop
[ ] network least privilege
[ ] backup restore test
[ ] logging rotation
[ ] security options
[ ] rollback/runbook
```

### Expected Evidence

The workload can be operated and recovered before production launch.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Make operational readiness a deployment gate.

---

## Advanced Deep Dive 130 — Evidence-First Docker Troubleshooting

### Concept

Use a stable sequence: context/version, daemon, container state/exit, logs, inspect, image, mounts, network/DNS, resources/OOM, host capacity, events, recent changes.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```bash
docker context show
docker version
docker info
docker ps -a
docker events --since 10m
docker system df
```

### Expected Evidence

The failed layer is identified before broad remediation.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Preserve inspect/log/event evidence and change one layer at a time.

---

## Advanced Deep Dive 131 — Docker-to-Kubernetes Image Boundary

### Concept

Docker remains highly relevant for image build, local runtime, Compose, and debugging even when Kubernetes nodes use containerd/CRI-O instead of Docker Engine.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
Dockerfile/BuildKit
  ↓ OCI image
registry
  ↓
Kubernetes CRI runtime
  ↓ OCI runtime
container process
```

### Expected Evidence

The build artifact is portable across OCI-compatible runtime ecosystems.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Separate Docker Engine administration skills from OCI image engineering skills.

---

## Advanced Deep Dive 132 — Compose-to-Kubernetes Mapping

### Concept

Compose models services, networks, volumes, health, and local topology; Kubernetes adds controllers, multi-node scheduling, Services, probes, persistent-volume orchestration, and admission policy.

### Architecture / Mental Model

```text
Source / Operator
      ↓
Docker CLI / Compose / Buildx
      ↓
Docker API / BuildKit
      ↓
containerd / OCI runtime
      ↓
Linux namespaces + cgroups + mounts + network
      ↓
Application process
```

### Command / Dockerfile / Compose / Code

```text
Compose service → Deployment/StatefulSet + Service
network DNS     → Service/CoreDNS/CNI
volume          → PV/PVC/CSI
healthcheck     → probes
env/config      → ConfigMap/Secret
limits          → requests/limits
```

### Expected Evidence

The learner can identify which local Docker concepts carry forward and which need cluster abstractions.

### Why It Works

Docker is a control and tooling layer over OCI images and Linux container primitives. The Engine stores metadata and orchestrates image, mount, network, cgroup, and runtime configuration; the application itself is still an ordinary process. Reliable troubleshooting therefore separates Docker control-plane state from the actual process, filesystem, network, resource, and security state.

### Production Example

Apply this topic to a production-style service by recording the image digest, build source, Docker/Compose configuration, runtime identity, resource limits, mounts, network exposure, health behavior, logging, persistent-data recovery, and rollback procedure.

### Troubleshooting Workflow

```text
Verify context + Engine
   ↓
Inspect container state / exit code
   ↓
Inspect logs + events
   ↓
Inspect image / entrypoint / command
   ↓
Inspect mounts + UID/GID
   ↓
Inspect network / DNS / listener
   ↓
Inspect CPU / memory / PIDs / disk
   ↓
Inspect security options
   ↓
Make one controlled correction
   ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting Docker socket access casually.
- Using `latest` as a production release identity.
- Baking credentials into ARG, ENV, layers, or build logs.
- Running as root or privileged to bypass a narrow issue.
- Publishing database/cache ports unnecessarily.
- Using a volume without a tested backup.
- Running broad prune commands during disk pressure without inventory.

### Best Practice

Use Docker/Compose to master containers before adding cluster orchestration complexity.

---

# Supplemental Hands-on Lab Series — Docker Fundamentals

## Enhanced Lab 1 — Docker Client/API/Daemon Boundary

### Objective

Turn **Docker Client/API/Daemon Boundary** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker context show
docker version
docker info
```

### Expected Result

Client and server versions/endpoints are visible separately.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Troubleshoot client context and daemon health before debugging the container itself.

---

## Enhanced Lab 2 — Unix Socket Privilege

### Objective

Turn **Unix Socket Privilege** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
ls -l /var/run/docker.sock 2>/dev/null || true
getent group docker 2>/dev/null || true
```

### Expected Result

Socket ownership and trusted group membership are explicit.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat Docker socket access as administrative privilege.

---

## Enhanced Lab 3 — Remote Docker over SSH

### Objective

Turn **Remote Docker over SSH** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker context create lab-remote --docker "host=ssh://user@host"
docker context ls
```

### Expected Result

The remote endpoint is represented as a named context.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer SSH or properly authenticated TLS over public unauthenticated daemon TCP.

---

## Enhanced Lab 4 — Mutual TLS Daemon API Concept

### Objective

Turn **Mutual TLS Daemon API Concept** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
client cert
  ↓ mTLS
dockerd TCP endpoint
  ↓
authorized host/network only
```

### Expected Result

The network path requires authenticated clients rather than relying only on IP allowlisting.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not expose the rootful daemon API to untrusted networks.

---

## Enhanced Lab 5 — Context Safety

### Objective

Turn **Context Safety** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker context ls
docker context show
docker info --format '{{.Name}}'
```

### Expected Result

The current Engine endpoint is known before deletion/prune/restart commands.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make context verification part of every operational runbook.

---

## Enhanced Lab 6 — DOCKER_HOST Precedence Risk

### Objective

Turn **DOCKER_HOST Precedence Risk** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
printf 'DOCKER_HOST=%s\n' "${DOCKER_HOST:-<unset>}"
docker context show
```

### Expected Result

The shell endpoint override is visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep endpoint selection explicit and avoid hidden environment overrides in production automation.

---

## Enhanced Lab 7 — Daemon Configuration Validation

### Objective

Turn **Daemon Configuration Validation** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
python3 -m json.tool /etc/docker/daemon.json 2>/dev/null || true
sudo dockerd --validate --config-file=/etc/docker/daemon.json 2>/dev/null || true
```

### Expected Result

JSON is syntactically valid and the daemon validator reports configuration status when supported.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Validate daemon configuration before restart and keep a rollback copy.

---

## Enhanced Lab 8 — systemd Service Evidence

### Objective

Turn **systemd Service Evidence** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
systemctl status docker --no-pager
systemctl status containerd --no-pager
journalctl -u docker -b --no-pager | tail -80
```

### Expected Result

Service exit status and recent daemon errors are visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use systemd/journal evidence before reinstalling Docker.

---

## Enhanced Lab 9 — Data Root

### Objective

Turn **Data Root** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker info --format '{{.DockerRootDir}}'
```

### Expected Result

The active Docker data directory is known.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never manually delete Docker data-root files while the daemon is managing them.

---

## Enhanced Lab 10 — Data Root Migration

### Objective

Turn **Data Root Migration** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
stop workloads/daemon
  ↓ backup metadata/data
copy data root preserving xattrs/ownership
  ↓ configure new data-root
start daemon
  ↓ validate images/volumes/containers
```

### Expected Result

The migration preserves runtime state and security metadata.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat Docker data-root movement as storage migration, not a simple directory rename.

---

## Enhanced Lab 11 — Live Restore Limits

### Objective

Turn **Live Restore Limits** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker info | grep -i 'Live Restore' || true
```

### Expected Result

The operator knows whether live restore is enabled and does not assume all daemon changes are zero-impact.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Test daemon-maintenance behavior on the exact host/runtime configuration.

---

## Enhanced Lab 12 — containerd Shim Role

### Objective

Turn **containerd Shim Role** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
dockerd
  ↓
containerd
  ↓
containerd-shim
  ↓
container process
```

### Expected Result

The process hierarchy can show shim processes associated with running containers.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use the runtime stack mental model when diagnosing daemon-versus-container failures.

---

## Enhanced Lab 13 — Storage Driver vs Volume Driver

### Objective

Turn **Storage Driver vs Volume Driver** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker info | grep -E 'Storage Driver|Backing Filesystem'
docker volume ls
```

### Expected Result

Image-layer storage and persistent volume inventory are inspected separately.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not troubleshoot database-volume performance as if it were only an overlay storage-driver issue.

---

## Enhanced Lab 14 — overlay2 Copy-Up

### Objective

Turn **overlay2 Copy-Up** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker info | grep -i 'Storage Driver'
docker diff <CONTAINER> 2>/dev/null || true
```

### Expected Result

Writable-layer changes are distinguishable from mounted persistent data.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep databases and heavy mutable data off the container writable layer.

---

## Enhanced Lab 15 — Container Writable-Layer Recovery

### Objective

Turn **Container Writable-Layer Recovery** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker ps -a
docker inspect <CONTAINER> --format '{{json .Mounts}}' 2>/dev/null || true
```

### Expected Result

Important paths are confirmed to use volumes or external storage.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Assume the writable layer can disappear at any time.

---

## Enhanced Lab 16 — Named Volume Ownership

### Objective

Turn **Named Volume Ownership** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format '{{.Config.User}} {{json .Mounts}}' 2>/dev/null || true
docker run --rm -v <VOLUME>:/data alpine sh -c 'ls -ldn /data'
```

### Expected Result

The application UID/GID can be compared with volume ownership.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix numeric ownership intentionally instead of running the application as root.

---

## Enhanced Lab 17 — Volume Backup Consistency

### Objective

Turn **Volume Backup Consistency** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
database
  ↓ native backup / quiesce
consistent point
  ↓ copy/snapshot volume
  ↓ restore test
```

### Expected Result

The backup process identifies whether it is crash-consistent or application-consistent.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use database-native backup for transactional data unless storage snapshots are integrated with quiescing.

---

## Enhanced Lab 18 — Bind Mount Portability

### Objective

Turn **Bind Mount Portability** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format '{{json .Mounts}}' 2>/dev/null || true
```

### Expected Result

Bind and volume mount types are distinguishable.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use bind mounts deliberately for host integration; use immutable images/managed volumes for portable production workloads.

---

## Enhanced Lab 19 — Bind Mount Propagation

### Objective

Turn **Bind Mount Propagation** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
private  → mount events do not propagate
shared   → bidirectional propagation
slave    → receives from parent but does not send back
```

### Expected Result

The requested propagation mode is tied to a real infrastructure requirement.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep ordinary application bind mounts private.

---

## Enhanced Lab 20 — tmpfs Mount Security

### Objective

Turn **tmpfs Mount Security** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm --tmpfs /run/secure:rw,noexec,nosuid,size=16m alpine   sh -c 'mount | grep /run/secure; df -h /run/secure'
```

### Expected Result

The path is mounted as tmpfs with explicit options and size.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use tmpfs for short-lived data that should not persist, while accounting for memory usage.

---

## Enhanced Lab 21 — Dockerfile Syntax Directive

### Objective

Turn **Dockerfile Syntax Directive** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN echo hello
```

### Expected Result

The Dockerfile declares the frontend syntax family it expects.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Pin/standardize build frontend expectations in CI for reproducible builds.

---

## Enhanced Lab 22 — Dockerfile ARG Scope

### Objective

Turn **Dockerfile ARG Scope** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
ARG BASE=alpine:3.22
FROM ${BASE}
ARG BASE
RUN echo "base=$BASE"
```

### Expected Result

The build demonstrates where the argument is available.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use ARG for non-secret build parameters and understand stage scope.

---

## Enhanced Lab 23 — ENV vs ARG

### Objective

Turn **ENV vs ARG** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
ARG BUILD_MODE=release
ENV APP_ENV=production
RUN echo "$BUILD_MODE"
```

### Expected Result

Runtime inspection contains ENV but not a secret-safe ARG mechanism.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep secrets out of both ARG and ENV image metadata.

---

## Enhanced Lab 24 — ONBUILD Instruction Concept

### Objective

Turn **ONBUILD Instruction Concept** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
FROM alpine
ONBUILD COPY . /src
```

### Expected Result

Child builds execute inherited triggers even when their Dockerfile does not show the full behavior locally.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Avoid ONBUILD in general-purpose bases unless the implicit behavior is well documented.

---

## Enhanced Lab 25 — Heredoc Build Steps

### Objective

Turn **Heredoc Build Steps** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN <<'EOF'
set -eu
echo "step one"
echo "step two"
EOF
```

### Expected Result

The multi-line build logic runs as one readable instruction.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use heredocs for clarity, not to hide large unmaintainable shell scripts.

---

## Enhanced Lab 26 — COPY Ownership

### Objective

Turn **COPY Ownership** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
COPY --chown=10001:10001 app/ /app/
USER 10001
```

### Expected Result

Runtime files already have the correct numeric owner.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set ownership during copy where supported instead of adding wasteful correction layers.

---

## Enhanced Lab 27 — COPY --link Concept

### Objective

Turn **COPY --link Concept** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
# syntax=docker/dockerfile:1
COPY --link src/ /app/src/
```

### Expected Result

The build frontend treats the copy as a cache-friendly independent layer when supported.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use advanced Dockerfile features only when CI/builders are standardized and tested.

---

## Enhanced Lab 28 — Build Context Minimization

### Objective

Turn **Build Context Minimization** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
du -sh .
find . -maxdepth 2 -type f | head
cat .dockerignore
```

### Expected Result

The context excludes `.git`, credentials, local caches, and irrelevant large artifacts.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep build context intentionally small and secret-free.

---

## Enhanced Lab 29 — Remote/Git Build Context Trust

### Objective

Turn **Remote/Git Build Context Trust** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
Git URL
  ↓ pin commit/tag
builder fetches source
  ↓
BuildKit
```

### Expected Result

The build references a known source revision rather than an unbounded moving branch.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Pin remote source and record the resolved commit in provenance.

---

## Enhanced Lab 30 — BuildKit LLB Mental Model

### Objective

Turn **BuildKit LLB Mental Model** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
Dockerfile
  ↓ frontend
LLB build graph
  ├─ source op
  ├─ exec op
  ├─ copy op
  └─ cache dependencies
```

### Expected Result

Independent graph nodes can be cached or executed in parallel where possible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Optimize build dependency graphs, not only Dockerfile layer count.

---

## Enhanced Lab 31 — Build Cache Key

### Objective

Turn **Build Cache Key** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### Expected Result

Changing source code alone preserves the dependency-install cache.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Order stable dependency inputs before frequently changing application files.

---

## Enhanced Lab 32 — BuildKit Cache Mount

### Objective

Turn **BuildKit Cache Mount** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip     pip install -r requirements.txt
```

### Expected Result

Repeated builds reuse package cache without bloating the runtime image.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use cache mounts for performance, not for required runtime content.

---

## Enhanced Lab 33 — BuildKit Secret Lifetime

### Objective

Turn **BuildKit Secret Lifetime** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
RUN --mount=type=secret,id=token     sh -c 'test -s /run/secrets/token && echo "token available"'
```

### Expected Result

The secret is available only at the expected temporary path during the step.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never echo, copy, or persist BuildKit secrets into layers/logs.

---

## Enhanced Lab 34 — BuildKit SSH Mount

### Objective

Turn **BuildKit SSH Mount** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
RUN --mount=type=ssh git clone git@github.com:example/private-repo.git
```

### Expected Result

The build can authenticate using forwarded SSH credentials while the key is absent from the final image.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use short-lived/agent-forwarded build identity rather than copying private keys.

---

## Enhanced Lab 35 — Build Cache Export/Import

### Objective

Turn **Build Cache Export/Import** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker buildx build   --cache-from type=registry,ref=registry.example.com/app:buildcache   --cache-to type=registry,ref=registry.example.com/app:buildcache,mode=max   .
```

### Expected Result

A later CI runner can reuse cache without sharing local disk.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate caches across trust boundaries and do not treat cache as authoritative source code.

---

## Enhanced Lab 36 — Buildx Builder Drivers

### Objective

Turn **Buildx Builder Drivers** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker buildx ls
docker buildx inspect --bootstrap
```

### Expected Result

The active builder driver, nodes, and supported platforms are visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Inspect the builder before diagnosing multi-platform or cache behavior.

---

## Enhanced Lab 37 — Multi-Platform Emulation vs Native Build

### Objective

Turn **Multi-Platform Emulation vs Native Build** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker buildx inspect --bootstrap
uname -m
```

### Expected Result

Supported build platforms can be compared with the local host architecture.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use native builders for heavy architecture-specific compilation when practical.

---

## Enhanced Lab 38 — Cross-Compilation Stage Pattern

### Objective

Turn **Cross-Compilation Stage Pattern** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
FROM --platform=$BUILDPLATFORM golang:1.25 AS build
ARG TARGETOS TARGETARCH
RUN GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /out/app ./cmd/app
```

### Expected Result

One builder can produce architecture-specific binaries without emulating the full target userspace.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer language-native cross-compilation when it is well supported.

---

## Enhanced Lab 39 — Build Provenance

### Objective

Turn **Build Provenance** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
source commit
  ↓ trusted builder
provenance
  ↓ image digest
```

### Expected Result

A release record maps exact artifact bytes to an authorized build.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Store provenance alongside immutable image digests.

---

## Enhanced Lab 40 — SBOM Build Output

### Objective

Turn **SBOM Build Output** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
image digest
  └─ SBOM
       ├─ OS packages
       └─ language packages
```

### Expected Result

Security teams can identify affected artifacts without manually opening every image.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Generate and retain SBOMs for release images.

---

## Enhanced Lab 41 — Multi-Stage Test Gate

### Objective

Turn **Multi-Stage Test Gate** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
FROM base AS test
RUN pytest -q

FROM base AS runtime
COPY --from=build /app /app
```

### Expected Result

CI can fail before the runtime image is published while keeping test dependencies out of production.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate build/test/runtime concerns into explicit stages.

---

## Enhanced Lab 42 — Distroless Debug Strategy

### Objective

Turn **Distroless Debug Strategy** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
prod image: app + runtime only
debug image: same app version + shell/curl/strace
```

### Expected Result

Production remains minimal while operators still have a controlled diagnostic path.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not add permanent admin tooling to production solely for convenience.

---

## Enhanced Lab 43 — Base Image Digest Updates

### Objective

Turn **Base Image Digest Updates** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```dockerfile
FROM python:3.13-slim@sha256:<approved-digest>
```

### Expected Result

The build uses exact base content and updates occur through reviewed changes.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Pair digest pinning with scheduled dependency/security update automation.

---

## Enhanced Lab 44 — Image Promotion by Digest

### Objective

Turn **Image Promotion by Digest** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
build digest D
  ↓ test D
  ↓ scan/sign D
  ↓ production deploy D
```

### Expected Result

Production receives byte-identical image content to the tested artifact.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use digest as the release identity and tags as human metadata.

---

## Enhanced Lab 45 — Registry Credential Helper

### Objective

Turn **Registry Credential Helper** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
cat ~/.docker/config.json 2>/dev/null | sed -n '1,80p'
```

### Expected Result

The configuration indicates helper/store use rather than embedded reusable passwords where supported.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use credential helpers or short-lived cloud tokens for registry authentication.

---

## Enhanced Lab 46 — Registry Token Scope

### Objective

Turn **Registry Token Scope** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
CI builder: pull base + push app
runtime: pull app
retention bot: delete expired
registry admin: separate
```

### Expected Result

Registry privileges are separated by workload role.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Apply least privilege to registry actions just like cloud IAM.

---

## Enhanced Lab 47 — Private Registry TLS

### Objective

Turn **Private Registry TLS** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
openssl s_client -connect registry.example.com:443   -servername registry.example.com </dev/null 2>/dev/null | head
```

### Expected Result

The presented certificate chain/hostname can be inspected.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix CA trust, chain, hostname, proxy, or clock rather than marking production registries insecure.

---

## Enhanced Lab 48 — Registry Mirror / Pull-Through Cache

### Objective

Turn **Registry Mirror / Pull-Through Cache** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
build hosts
  ↓
trusted registry cache
  ↓
upstream public registry
```

### Expected Result

The cache reduces external pulls without bypassing image integrity/security checks.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Secure and monitor mirrors like production registries.

---

## Enhanced Lab 49 — Image Scan Context

### Objective

Turn **Image Scan Context** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
build scan
  +
continuous image inventory
  +
runtime hardening
  +
secure coding
```

### Expected Result

Scanning is treated as one layer rather than proof that the image is secure.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Re-scan deployed digests as vulnerability intelligence changes.

---

## Enhanced Lab 50 — Signature vs Digest

### Objective

Turn **Signature vs Digest** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
sha256 digest → integrity
signature       → signer authenticity/approval
provenance      → build claims
```

### Expected Result

Release policy distinguishes integrity from publisher trust.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Verify signatures/attestations against immutable digests.

---

## Enhanced Lab 51 — Runtime Image Policy

### Objective

Turn **Runtime Image Policy** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
release request
  ↓ policy checks
approved?
  ├─ yes → run
  └─ no  → block
```

### Expected Result

Unsafe artifacts/configurations are rejected before runtime.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Convert recurring review rules into policy-as-code when the platform supports it.

---

## Enhanced Lab 52 — Default Bridge vs User-Defined Bridge

### Objective

Turn **Default Bridge vs User-Defined Bridge** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker network create appnet
docker network inspect appnet
```

### Expected Result

The network has its own subnet, gateway, and attached containers.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Create one or more application networks rather than depending on default bridge behavior.

---

## Enhanced Lab 53 — Embedded Docker DNS

### Objective

Turn **Embedded Docker DNS** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker exec <CLIENT> getent hosts <SERVICE> 2>/dev/null || true
docker exec <CLIENT> cat /etc/resolv.conf 2>/dev/null || true
```

### Expected Result

The service name resolves inside the shared network.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use service names, not container IPs.

---

## Enhanced Lab 54 — Application Bind Address

### Objective

Turn **Application Bind Address** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker exec <CONTAINER> ss -lntp 2>/dev/null || true
```

### Expected Result

The listening address and port match the intended client path.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Check the application socket before changing Docker networking.

---

## Enhanced Lab 55 — Published-Port Exposure

### Objective

Turn **Published-Port Exposure** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker ps --format 'table {{.Names}}\t{{.Ports}}'
ss -lntp
```

### Expected Result

The real host bind address is visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Publish only the entrypoint ports and bind to the narrowest host interface.

---

## Enhanced Lab 56 — Docker Firewall Interaction

### Objective

Turn **Docker Firewall Interaction** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
sudo iptables -S 2>/dev/null | grep -E 'DOCKER|FORWARD' | head -40 || true
sudo nft list ruleset 2>/dev/null | grep -i docker | head -40 || true
```

### Expected Result

Docker-managed filtering/NAT rules are visible on the host where applicable.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Test host-firewall changes with Docker networking instead of assuming rule order.

---

## Enhanced Lab 57 — DOCKER-USER Policy Concept

### Objective

Turn **DOCKER-USER Policy Concept** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
sudo iptables -S DOCKER-USER 2>/dev/null || true
```

### Expected Result

Host-level policy rules are distinguishable from automatically generated Docker rules.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Place administrator policy in supported extension points rather than editing Docker-managed rules manually.

---

## Enhanced Lab 58 — Network Namespace Inspection

### Objective

Turn **Network Namespace Inspection** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
PID=$(docker inspect -f '{{.State.Pid}}' <CONTAINER>)
sudo nsenter -t "$PID" -n ip addr
sudo nsenter -t "$PID" -n ip route
```

### Expected Result

The actual interface, route table, and namespace network state are visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use namespace evidence when Docker-level inspection is insufficient.

---

## Enhanced Lab 59 — DNS Failure Decomposition

### Objective

Turn **DNS Failure Decomposition** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker exec <CONTAINER> cat /etc/resolv.conf
docker exec <CONTAINER> getent hosts example.com || true
```

### Expected Result

DNS failure is distinguished from routing or application failure.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not change bridge subnets to fix a resolver-only problem.

---

## Enhanced Lab 60 — Corporate VPN Overlap

### Objective

Turn **Corporate VPN Overlap** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
ip route
docker network ls
docker network inspect <NETWORK>
```

### Expected Result

Docker subnet overlap with VPN/LAN ranges can be identified.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Plan non-overlapping container address pools before large-scale developer rollout.

---

## Enhanced Lab 61 — MTU Diagnosis

### Objective

Turn **MTU Diagnosis** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
ip link
docker network inspect <NETWORK> 2>/dev/null || true
ping -M do -s 1400 <AUTHORIZED_TARGET> 2>/dev/null || true
```

### Expected Result

Host/network MTUs and path behavior can be compared.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Account for tunnel overhead instead of disabling TLS or changing application timeouts first.

---

## Enhanced Lab 62 — Host Network Trade-Off

### Objective

Turn **Host Network Trade-Off** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm --network host alpine ip addr
```

### Expected Result

The container sees the host network namespace state.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use host networking only when a measured compatibility/performance requirement justifies it.

---

## Enhanced Lab 63 — None Network

### Objective

Turn **None Network** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm --network none alpine ip addr
```

### Expected Result

Only isolated loopback-style networking is available.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use no-network execution for jobs that do not need network access.

---

## Enhanced Lab 64 — macvlan / ipvlan Decision

### Objective

Turn **macvlan / ipvlan Decision** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
bridge → host-mediated container subnet
macvlan → container appears as distinct L2 endpoint
ipvlan → shared/controlled L2 identity with distinct IP behavior
```

### Expected Result

The chosen driver is tied to a real legacy/network-integration requirement.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer bridge networking unless direct network presence is required.

---

## Enhanced Lab 65 — Container Connection Refused vs Timeout

### Objective

Turn **Container Connection Refused vs Timeout** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker exec <CLIENT> getent hosts <SERVICE>
docker exec <CLIENT> sh -c 'nc -vz -w2 <SERVICE> <PORT>' 2>/dev/null || true
```

### Expected Result

The failure mode helps narrow listener versus network-path investigation.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use the error semantics as a clue, not an absolute diagnosis.

---

## Enhanced Lab 66 — Container Resource Defaults

### Objective

Turn **Container Resource Defaults** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format 'Memory={{.HostConfig.Memory}} NanoCPUs={{.HostConfig.NanoCpus}} Pids={{.HostConfig.PidsLimit}}'
```

### Expected Result

Zero/unset values reveal missing hard limits.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set intentional resource controls from measured workload behavior.

---

## Enhanced Lab 67 — Memory Reservation vs Hard Limit

### Objective

Turn **Memory Reservation vs Hard Limit** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format 'Memory={{.HostConfig.Memory}} Reservation={{.HostConfig.MemoryReservation}}'
```

### Expected Result

Hard and reservation values can be compared.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Size memory from startup peak, steady working set, and failure behavior.

---

## Enhanced Lab 68 — OOM Evidence

### Objective

Turn **OOM Evidence** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format 'Exit={{.State.ExitCode}} OOM={{.State.OOMKilled}}'
journalctl -k --since '-10 min' | grep -i -E 'oom|out of memory' | tail -20
```

### Expected Result

The investigation produces direct evidence for or against OOM.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Confirm OOM before raising memory limits.

---

## Enhanced Lab 69 — CPU Quota vs Shares

### Objective

Turn **CPU Quota vs Shares** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format 'NanoCPUs={{.HostConfig.NanoCpus}} CpuShares={{.HostConfig.CpuShares}}'
```

### Expected Result

Absolute and relative CPU controls are visible separately.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use quota for containment and shares/weight for relative fairness.

---

## Enhanced Lab 70 — CPU Throttling Diagnosis

### Objective

Turn **CPU Throttling Diagnosis** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
PID=$(docker inspect -f '{{.State.Pid}}' <CONTAINER>)
cat /proc/$PID/cgroup
docker stats --no-stream <CONTAINER>
```

### Expected Result

Container runtime stats can be correlated with the underlying cgroup.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Investigate throttling counters when latency rises under CPU limits.

---

## Enhanced Lab 71 — PIDs Limit

### Objective

Turn **PIDs Limit** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format '{{.HostConfig.PidsLimit}}'
docker stats --no-stream <CONTAINER>
```

### Expected Result

The configured PID ceiling and current PIDs are visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set realistic PID limits for services with bounded concurrency models.

---

## Enhanced Lab 72 — ulimits

### Objective

Turn **ulimits** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm --ulimit nofile=1024:1024 alpine sh -c 'ulimit -n'
```

### Expected Result

The process reports the configured file-descriptor ceiling.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Capacity-plan file descriptors for high-concurrency servers.

---

## Enhanced Lab 73 — Shared Memory Size

### Objective

Turn **Shared Memory Size** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm alpine df -h /dev/shm
```

### Expected Result

The runtime shared-memory filesystem size is visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Increase shared memory only for workloads that actually require it.

---

## Enhanced Lab 74 — Read-Only Root + Explicit Writes

### Objective

Turn **Read-Only Root + Explicit Writes** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm --read-only --tmpfs /tmp alpine   sh -c 'touch /tmp/ok; touch /fail 2>&1 || true'
```

### Expected Result

Temporary writes succeed only on approved writable mounts.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use read-only root filesystems for compatible stateless services.

---

## Enhanced Lab 75 — Capability Minimization

### Objective

Turn **Capability Minimization** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm --cap-drop ALL alpine sh -c 'grep ^Cap /proc/self/status'
```

### Expected Result

The process runs with a minimal capability mask.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Solve privilege errors with the narrow required capability, not `--privileged`.

---

## Enhanced Lab 76 — no-new-privileges

### Objective

Turn **no-new-privileges** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker run --rm --security-opt no-new-privileges:true alpine   sh -c "grep NoNewPrivs /proc/self/status"
```

### Expected Result

The container process reports NoNewPrivs enabled.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use no-new-privileges for ordinary application containers.

---

## Enhanced Lab 77 — Seccomp Failure Diagnosis

### Objective

Turn **Seccomp Failure Diagnosis** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
application error
  ↓ check audit/runtime evidence
identify syscall
  ↓
is syscall truly needed?
  ├─ yes → narrow reviewed exception
  └─ no  → fix application
```

### Expected Result

The remediation is scoped to the real syscall requirement.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat `seccomp=unconfined` only as a temporary controlled diagnostic step, not a production fix.

---

## Enhanced Lab 78 — AppArmor / SELinux Mount Denials

### Objective

Turn **AppArmor / SELinux Mount Denials** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
sudo dmesg | grep -i -E 'apparmor.*denied|avc:.*denied' | tail -30 2>/dev/null || true
```

### Expected Result

Security-module denials identify the affected path/profile/type where supported.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix labels/profile policy rather than chmod 777 or disabling the LSM.

---

## Enhanced Lab 79 — Rootless Docker Threat Reduction

### Objective

Turn **Rootless Docker Threat Reduction** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker info | grep -i -E 'rootless|security options' -A5 || true
id
```

### Expected Result

The operator can determine whether the active Engine is rootless.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use rootless where its feature/performance trade-offs fit the workload.

---

## Enhanced Lab 80 — userns-remap vs Rootless

### Objective

Turn **userns-remap vs Rootless** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
userns-remap:
rootful dockerd
  ↓ mapped container IDs

rootless:
unprivileged dockerd
  ↓ mapped container IDs
```

### Expected Result

The security model distinguishes daemon privilege from container UID mapping.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Choose the model intentionally instead of treating both features as equivalent.

---

## Enhanced Lab 81 — Host PID / Host IPC / Host Network Risk

### Objective

Turn **Host PID / Host IPC / Host Network Risk** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
ordinary app:
private PID + network + IPC

host namespace sharing:
reduced isolation
larger blast radius
```

### Expected Result

Any use of host namespace sharing has a documented infrastructure requirement.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never enable host namespaces to solve an unrelated connectivity or permission issue.

---

## Enhanced Lab 82 — Device Access

### Objective

Turn **Device Access** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format '{{json .HostConfig.Devices}}' 2>/dev/null || true
```

### Expected Result

Granted host devices are visible and auditable.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Expose only exact required devices and keep them out of ordinary web workloads.

---

## Enhanced Lab 83 — Compose Project Isolation

### Objective

Turn **Compose Project Isolation** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose ls
docker compose -p lab1 ps
```

### Expected Result

Compose resources can be attributed to a project boundary.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set explicit project names in CI and shared hosts to avoid collisions.

---

## Enhanced Lab 84 — Compose Config as Source of Truth

### Objective

Turn **Compose Config as Source of Truth** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose config
```

### Expected Result

The normalized configuration shows what Compose will actually apply.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Debug the rendered configuration before editing service code.

---

## Enhanced Lab 85 — Compose Environment Precedence

### Objective

Turn **Compose Environment Precedence** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose config
docker compose exec <SERVICE> env | sort
```

### Expected Result

The declared and actual runtime environment can be compared.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Document configuration ownership and avoid duplicating the same variable across many precedence layers.

---

## Enhanced Lab 86 — Compose Secrets Are Not Magic Encryption

### Objective

Turn **Compose Secrets Are Not Magic Encryption** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```yaml
services:
  api:
    secrets:
      - db_password
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### Expected Result

The secret is mounted as a file rather than stored in the image.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Protect the underlying secret source and never commit it to Git.

---

## Enhanced Lab 87 — Compose depends_on vs Runtime Resilience

### Objective

Turn **Compose depends_on vs Runtime Resilience** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
startup:
Compose health ordering

runtime:
DB restarts later
  ↓
application retry/backoff/reconnect still required
```

### Expected Result

The application can recover from dependency restart after the stack is already running.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use Compose dependency logic for startup convenience, not as a substitute for resilient application design.

---

## Enhanced Lab 88 — Compose Healthcheck Design

### Objective

Turn **Compose Healthcheck Design** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```yaml
healthcheck:
  test: ["CMD", "wget", "-qO-", "http://127.0.0.1:8080/health"]
  interval: 30s
  timeout: 3s
  retries: 3
```

### Expected Result

Health status reflects useful local service state without excessive load.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate local process health from external dependency readiness when possible.

---

## Enhanced Lab 89 — Compose Profiles

### Objective

Turn **Compose Profiles** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```yaml
services:
  adminer:
    image: adminer
    profiles: ["debug"]
```

### Expected Result

The optional service starts only when its profile is activated.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Keep privileged or debug tooling opt-in and disabled by default.

---

## Enhanced Lab 90 — Compose Override Discipline

### Objective

Turn **Compose Override Discipline** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose -f compose.yaml -f compose.prod.yaml config > rendered.yaml
```

### Expected Result

The final merged model is captured before deployment.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Review rendered Compose configuration in CI.

---

## Enhanced Lab 91 — Compose Scaling and Fixed Ports

### Objective

Turn **Compose Scaling and Fixed Ports** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose up -d --scale worker=3
docker compose ps
```

### Expected Result

Replicated services without fixed published ports scale cleanly.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Publish only entrypoint/proxy ports; keep scalable workers on internal networks.

---

## Enhanced Lab 92 — Compose Network Least Privilege

### Objective

Turn **Compose Network Least Privilege** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```yaml
services:
  api:
    networks: [frontend, backend]
  db:
    networks: [backend]
```

### Expected Result

The topology prevents direct frontend-network access to the database.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat network membership as a least-privilege control.

---

## Enhanced Lab 93 — Compose Volume Destruction

### Objective

Turn **Compose Volume Destruction** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose volumes 2>/dev/null || true
docker volume ls
```

### Expected Result

Operators can identify persistent volumes before destructive teardown.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate disposable test stacks from data-bearing environments and require confirmation for volume deletion.

---

## Enhanced Lab 94 — Compose Read-Only Service

### Objective

Turn **Compose Read-Only Service** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```yaml
services:
  api:
    read_only: true
    tmpfs: [/tmp]
    cap_drop: [ALL]
    security_opt:
      - no-new-privileges:true
```

### Expected Result

The service can start without broad writable/privileged defaults.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Harden from a working least-privilege baseline and document required exceptions.

---

## Enhanced Lab 95 — Compose One-Off Jobs

### Objective

Turn **Compose One-Off Jobs** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose run --rm api pytest
docker compose exec api sh -c 'id'
```

### Expected Result

The operator can distinguish ephemeral job execution from in-place diagnostics.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use `run --rm` for jobs/tests and `exec` for temporary investigation.

---

## Enhanced Lab 96 — Logging Driver Selection

### Objective

Turn **Logging Driver Selection** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker info --format '{{.LoggingDriver}}'
docker inspect <CONTAINER> --format '{{json .HostConfig.LogConfig}}' 2>/dev/null || true
```

### Expected Result

The daemon default and container-specific logging settings are known.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Choose a driver and retention model that cannot fill the host silently.

---

## Enhanced Lab 97 — Blocking vs Non-Blocking Logging Concept

### Objective

Turn **Blocking vs Non-Blocking Logging Concept** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
app stdout
  ↓ logging driver
  ↓ buffer
external collector

collector slow:
blocking → app may stall
non-blocking → buffer/drop policy matters
```

### Expected Result

Logging failure behavior is explicitly understood.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Decide whether logs may be dropped versus allowed to block application throughput.

---

## Enhanced Lab 98 — Log Rotation

### Objective

Turn **Log Rotation** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format '{{json .HostConfig.LogConfig}}'
docker system df -v
```

### Expected Result

Log-driver options and Docker disk usage are visible.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set log size/retention limits and monitor the host filesystem.

---

## Enhanced Lab 99 — Docker Events as Timeline

### Objective

Turn **Docker Events as Timeline** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker events --since 10m
```

### Expected Result

Lifecycle events can be correlated with application logs and host events.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Capture event timelines during restart loops and unexplained container replacement.

---

## Enhanced Lab 100 — docker inspect Release Evidence

### Objective

Turn **docker inspect Release Evidence** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> > inspect.json
docker inspect <CONTAINER> --format 'Image={{.Image}} User={{.Config.User}} Privileged={{.HostConfig.Privileged}}'
```

### Expected Result

The exact runtime configuration is preserved for analysis.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Capture inspect output before replacing a failing container.

---

## Enhanced Lab 101 — docker diff for Drift

### Objective

Turn **docker diff for Drift** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker diff <CONTAINER> | head -100
```

### Expected Result

Unexpected modified paths can be identified.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Treat significant runtime drift as a signal to fix image/configuration rather than preserving the mutated container.

---

## Enhanced Lab 102 — docker system df

### Objective

Turn **docker system df** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker system df
docker system df -v
```

### Expected Result

Disk pressure is attributed to a Docker object category.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Inspect usage before pruning anything.

---

## Enhanced Lab 103 — Prune Safety

### Objective

Turn **Prune Safety** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
before prune:
inventory
owner
backup/rollback need
exact command scope
dry-run style review where possible
```

### Expected Result

Deletion scope is reviewed before execution.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Never run broad prune commands blindly on important hosts.

---

## Enhanced Lab 104 — Inode Exhaustion

### Objective

Turn **Inode Exhaustion** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
df -h
df -i
docker system df -v
```

### Expected Result

Byte capacity and inode capacity are evaluated independently.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Monitor both disk space and inode pressure.

---

## Enhanced Lab 105 — Daemon Metrics / Host Monitoring Concept

### Objective

Turn **Daemon Metrics / Host Monitoring Concept** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
host:
CPU memory PSI disk inode network

Docker:
daemon availability events container restarts

app:
requests errors latency business KPI
```

### Expected Result

The monitoring design covers platform and service layers.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Alert on user/service impact and use container/host metrics for diagnosis.

---

## Enhanced Lab 106 — docker stats Limitations

### Objective

Turn **docker stats Limitations** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker stats --no-stream
```

### Expected Result

A point-in-time resource snapshot is available.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Export long-term metrics to a monitoring system and correlate with application telemetry.

---

## Enhanced Lab 107 — Health Status vs Restart

### Objective

Turn **Health Status vs Restart** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format '{{json .State.Health}}' 2>/dev/null || true
```

### Expected Result

Health history and process running state can be different.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use orchestration/supervision logic explicitly if unhealthy state should trigger replacement.

---

## Enhanced Lab 108 — Restart Loop Backoff Awareness

### Objective

Turn **Restart Loop Backoff Awareness** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format 'RestartCount={{.RestartCount}} Exit={{.State.ExitCode}} Error={{.State.Error}}'
```

### Expected Result

Crash-loop evidence is visible without manually restarting again.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix the failing entrypoint/config/dependency instead of relying on infinite restart.

---

## Enhanced Lab 109 — Graceful HTTP Shutdown

### Objective

Turn **Graceful HTTP Shutdown** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
docker stop
  ↓ SIGTERM
server stops accept
  ↓ drain requests
close DB/queue
  ↓ exit 0
```

### Expected Result

Normal stop does not require SIGKILL.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Set stop timeout from measured worst-case drain time.

---

## Enhanced Lab 110 — Queue Worker Shutdown

### Objective

Turn **Queue Worker Shutdown** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
SIGTERM
  ↓ stop fetching
finish/rollback current message
  ↓ ack only after success
close
  ↓ exit
```

### Expected Result

Stopping the container does not silently lose or duplicate business work.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Design graceful stop around message acknowledgement semantics.

---

## Enhanced Lab 111 — Time Synchronization

### Objective

Turn **Time Synchronization** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
timedatectl status
date -Is
docker run --rm alpine date
```

### Expected Result

Host and container time are consistent.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix host time synchronization rather than configuring independent container clocks.

---

## Enhanced Lab 112 — Proxy Layers

### Objective

Turn **Proxy Layers** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
dockerd proxy → image pulls
BuildKit/build proxy → package downloads
container env proxy → application egress
NO_PROXY → internal services
```

### Expected Result

Each network client uses the intended proxy/no-proxy configuration.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Document proxy configuration by layer.

---

## Enhanced Lab 113 — NO_PROXY Design

### Objective

Turn **NO_PROXY Design** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
env | grep -i proxy
docker exec <CONTAINER> env | grep -i proxy 2>/dev/null || true
```

### Expected Result

Runtime proxy variables match internal/external routing needs.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Test internal service names and cloud metadata/private endpoints explicitly.

---

## Enhanced Lab 114 — Registry Pull Failure Workflow

### Objective

Turn **Registry Pull Failure Workflow** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker pull <IMAGE>
docker manifest inspect <IMAGE> 2>/dev/null | head -60 || true
```

### Expected Result

The failure is tied to a specific registry stage.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Do not solve TLS/auth errors by marking the registry insecure.

---

## Enhanced Lab 115 — Wrong Architecture

### Objective

Turn **Wrong Architecture** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
uname -m
docker image inspect <IMAGE> --format '{{.Os}}/{{.Architecture}}'
```

### Expected Result

Host and image platform are directly compared.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Publish and test every required platform in multi-architecture releases.

---

## Enhanced Lab 116 — Container Immediately Exits

### Objective

Turn **Container Immediately Exits** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker ps -a
docker inspect <CONTAINER> --format 'Exit={{.State.ExitCode}} Error={{.State.Error}} Cmd={{json .Config.Cmd}} Entry={{json .Config.Entrypoint}}'
docker logs <CONTAINER>
```

### Expected Result

Exit code, error, entrypoint, command, and logs are available.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Diagnose the primary process before adding restart policies.

---

## Enhanced Lab 117 — Volume Permission Failure

### Objective

Turn **Volume Permission Failure** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker inspect <CONTAINER> --format '{{json .Mounts}}'
docker exec <CONTAINER> id 2>/dev/null || true
ls -ldn <HOST_PATH> 2>/dev/null || true
```

### Expected Result

Identity and mount ownership/options are compared.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Fix the exact permission layer instead of using root or chmod 777.

---

## Enhanced Lab 118 — Published Port Failure

### Objective

Turn **Published Port Failure** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker ps
docker port <CONTAINER>
docker exec <CONTAINER> ss -lntp 2>/dev/null || true
ss -lntp
```

### Expected Result

The host mapping and container listener can be verified separately.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Check the listener before changing host firewall.

---

## Enhanced Lab 119 — Compose Dependency Failure

### Objective

Turn **Compose Dependency Failure** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker compose ps
docker compose exec <CLIENT> getent hosts <TARGET>
docker compose exec <CLIENT> sh -c 'nc -vz -w2 <TARGET> <PORT>' 2>/dev/null || true
```

### Expected Result

DNS and TCP reachability are tested from the real client service.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Troubleshoot from inside the client container, not only from the host.

---

## Enhanced Lab 120 — Disk Pressure Incident

### Objective

Turn **Disk Pressure Incident** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
df -h
df -i
docker system df -v
```

### Expected Result

The largest capacity consumer is identified safely.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Free space through known Docker objects/log policy, not by deleting internal metadata files.

---

## Enhanced Lab 121 — Build Failure Network Decomposition

### Objective

Turn **Build Failure Network Decomposition** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker buildx inspect --bootstrap
docker build --progress=plain .
```

### Expected Result

Plain build output exposes the failing fetch/install step.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Debug build networking independently from runtime container networking.

---

## Enhanced Lab 122 — Build Reproducibility Evidence

### Objective

Turn **Build Reproducibility Evidence** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
commit=...
dockerfile_sha=...
base_digest=...
builder=...
image_digest=...
sbom=...
provenance=...
```

### Expected Result

A later incident can reconstruct the exact release inputs.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make reproducibility metadata part of the CI artifact record.

---

## Enhanced Lab 123 — CI Least Privilege

### Objective

Turn **CI Least Privilege** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
CI:
source read
registry pull/push scoped repo
sign/attest
deploy scoped environment

not:
global registry admin
host root everywhere
```

### Expected Result

Build identity permissions match the pipeline actions.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate build, deploy, and runtime identities.

---

## Enhanced Lab 124 — Build Runner Isolation

### Objective

Turn **Build Runner Isolation** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
job
  ↓ ephemeral runner/builder
scoped credentials
  ↓ destroy after job
```

### Expected Result

Build jobs do not inherit stale credentials or workspace artifacts from unrelated projects.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Prefer ephemeral isolated builders for sensitive CI.

---

## Enhanced Lab 125 — Secret Leakage in Logs

### Objective

Turn **Secret Leakage in Logs** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```sh
set +x
# consume secret without echoing it
```

### Expected Result

Build logs contain no reusable credential material.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Redact logs and disable shell tracing around secret-handling steps.

---

## Enhanced Lab 126 — Dockerfile Lint / Policy Gate

### Objective

Turn **Dockerfile Lint / Policy Gate** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
policy examples:
USER must be non-root
no COPY *.pem
no secret ARG names
approved base registries
required OCI labels
```

### Expected Result

Unsafe patterns fail before image publication.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Automate repeatable Dockerfile review rules.

---

## Enhanced Lab 127 — Release Rollback

### Objective

Turn **Release Rollback** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
current digest D2 fails
  ↓
shift/deploy previous digest D1
  ↓
verify
```

### Expected Result

Rollback can select an exact prior artifact.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Retain immutable release digests for the full rollback/support window.

---

## Enhanced Lab 128 — Schema Migration Compatibility

### Objective

Turn **Schema Migration Compatibility** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
expand schema
  ↓ deploy old+new compatible app
migrate data
  ↓ contract later
```

### Expected Result

Both old and new application versions can operate during the rollout window.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use expand/contract database migrations for reversible deployments.

---

## Enhanced Lab 129 — Operational Readiness Review

### Objective

Turn **Operational Readiness Review** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
[ ] immutable digest
[ ] non-root
[ ] limits
[ ] health
[ ] graceful stop
[ ] network least privilege
[ ] backup restore test
[ ] logging rotation
[ ] security options
[ ] rollback/runbook
```

### Expected Result

The workload can be operated and recovered before production launch.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Make operational readiness a deployment gate.

---

## Enhanced Lab 130 — Evidence-First Docker Troubleshooting

### Objective

Turn **Evidence-First Docker Troubleshooting** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```bash
docker context show
docker version
docker info
docker ps -a
docker events --since 10m
docker system df
```

### Expected Result

The failed layer is identified before broad remediation.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Preserve inspect/log/event evidence and change one layer at a time.

---

## Enhanced Lab 131 — Docker-to-Kubernetes Image Boundary

### Objective

Turn **Docker-to-Kubernetes Image Boundary** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
Dockerfile/BuildKit
  ↓ OCI image
registry
  ↓
Kubernetes CRI runtime
  ↓ OCI runtime
container process
```

### Expected Result

The build artifact is portable across OCI-compatible runtime ecosystems.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Separate Docker Engine administration skills from OCI image engineering skills.

---

## Enhanced Lab 132 — Compose-to-Kubernetes Mapping

### Objective

Turn **Compose-to-Kubernetes Mapping** into a repeatable Docker administration, engineering, or troubleshooting exercise.

### Safety Boundary

Use your own Docker Desktop or disposable Linux VM. Do not expose a Docker daemon to the public Internet. Use fake secrets, non-production registries, and disposable data.

### Procedure

1. Verify Docker context, client/server version, and host capacity.
2. Draw the expected request/build/runtime path.
3. Run the discovery command/configuration below.
4. Record the expected state.
5. Introduce one reversible failure when safe.
6. Diagnose with Docker metadata and Linux/runtime evidence.
7. Restore the intended configuration.
8. Verify application behavior, not only container state.
9. Record security, reliability, and cost/performance implications.
10. Clean up only resources you created.

### Command / Configuration

```text
Compose service → Deployment/StatefulSet + Service
network DNS     → Service/CoreDNS/CNI
volume          → PV/PVC/CSI
healthcheck     → probes
env/config      → ConfigMap/Secret
limits          → requests/limits
```

### Expected Result

The learner can identify which local Docker concepts carry forward and which need cluster abstractions.

### Evidence Record

```text
Context
Engine
Image digest
Container/service
Exit/health state
Entrypoint/Cmd
User/security options
Mounts
Network/DNS/listener
Resource limits
Logs/events
Root cause
Fix
Verification
Prevention
```

### Best Practice

Use Docker/Compose to master containers before adding cluster orchestration complexity.

---

## 5. Hands-on Lab / Practical Exercises

> Use your own Linux VM or Docker Desktop environment. Do not expose lab Docker daemons to the public Internet.

### Lab 1 — Installation and Baseline

Install Docker Engine using the current official procedure.

Verify:

```bash
docker version
docker info
docker compose version
docker buildx version
```

Record:

```text
Engine
API
containerd
runc
storage driver
cgroup version
logging driver
```

### Lab 2 — Docker Architecture Trace

Run:

```bash
docker run --rm hello-world
```

Draw every step:

```text
CLI
daemon
image pull
containerd
runc
process
```

### Lab 3 — Context Safety

Run:

```bash
docker context ls
docker context show
```

Create a second local/SSH lab context if available.

Practice verifying context before destructive operations.

### Lab 4 — Lifecycle

Perform:

```bash
docker create
docker start
docker stop
docker restart
docker pause
docker unpause
docker rm
```

Observe state at every step.

### Lab 5 — Interactive vs Detached

Compare:

```bash
docker run -it ubuntu bash
docker run -d nginx
```

Explain stdin/TTY/foreground behavior.

### Lab 6 — Inspect and Logs

Use:

```bash
docker inspect
docker logs
docker top
docker stats
docker diff
```

on one container.

Create an incident evidence sheet.

### Lab 7 — Exit Codes

Run disposable containers that exit:

```text
0
1
127
```

Record Docker state and logs.

### Lab 8 — Signal Handling

Create Python service:

```python
import signal
import time

running = True

def stop(sig, frame):
    global running
    print("SIGTERM received")
    running = False

signal.signal(signal.SIGTERM, stop)

while running:
    time.sleep(1)

print("graceful exit")
```

Containerize it and run `docker stop`.

Observe.

### Lab 9 — PID 1 / Init

Create shell wrapper without `exec`.

Compare signal behavior with:

```text
wrapper
wrapper using exec
docker run --init
```

### Lab 10 — First Dockerfile

Create FastAPI app:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "docker-course"}

@app.get("/health")
def health():
    return {"status": "ok"}
```

Build and run.

### Lab 11 — Dockerfile Cache

Build:

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

Change application source only.

Observe dependency layer reuse.

### Lab 12 — .dockerignore

Add:

```text
.git
.env
*.pem
__pycache__
.venv
```

Compare build-context transfer.

### Lab 13 — Non-Root Image

Create UID 10001.

Run app as non-root.

Verify:

```bash
docker exec CONTAINER id
```

### Lab 14 — Multi-Stage Build

Build a Go/Node/frontend app with:

```text
builder stage
runtime stage
```

Compare image sizes.

### Lab 15 — Build Secret

Use BuildKit secret mount for a fake private package token.

Verify secret is absent from final image and normal history.

### Lab 16 — Cache Mount

Use package-manager cache mount.

Compare cold vs warm build duration.

### Lab 17 — Multi-Platform Build

Inspect builder:

```bash
docker buildx ls
```

Build or plan:

```text
linux/amd64
linux/arm64
```

Inspect manifest/index.

### Lab 18 — Tags and Digests

Tag an image:

```text
app:1.0
app:stable
```

Verify both reference same ID locally.

Push to private/lab registry if available and record digest.

### Lab 19 — Save/Load vs Export/Import

Perform:

```bash
docker save
docker load
docker export
docker import
```

Compare:

```text
layers
history
metadata
```

### Lab 20 — Named Volume

Create PostgreSQL with named volume.

Insert test data.

Remove container.

Create replacement with same volume.

Verify data remains.

### Lab 21 — Volume Backup

Back up a non-production lab volume.

Restore into a new volume.

Validate file checksum/data.

### Lab 22 — Bind Mount

Mount source folder for development.

Edit host file and observe container change.

Document why this is not immutable deployment.

### Lab 23 — Read-Only RootFS

Run application:

```bash
docker run --read-only --tmpfs /tmp ...
```

Identify any required writable directories.

### Lab 24 — User-Defined Network

Create:

```bash
docker network create backend
```

Run `api` and `db`.

Resolve:

```bash
getent hosts db
```

from API container.

### Lab 25 — Frontend/Backend Isolation

Create:

```text
frontend network
backend network
```

Attach:

```text
proxy → frontend
api → frontend + backend
db → backend
```

Prove proxy cannot reach DB directly.

### Lab 26 — Port Publishing

Compare:

```bash
-p 8080:80
-p 127.0.0.1:8081:80
```

Use:

```bash
ss -lntp
```

to inspect exposure.

### Lab 27 — Network Namespace

Find container PID:

```bash
docker inspect -f '{{.State.Pid}}' CONTAINER
```

Then:

```bash
sudo nsenter -t PID -n ip addr
sudo nsenter -t PID -n ip route
```

Compare host/container network.

### Lab 28 — DNS Failure

Break DNS intentionally using invalid DNS config in a disposable container.

Observe:

```text
IP connectivity
name resolution failure
```

Restore.

### Lab 29 — Memory Limit

Run a controlled memory allocation workload with:

```bash
--memory 128m
```

Observe OOM state.

Do not run on critical host.

### Lab 30 — CPU Limit

Run CPU-bound workload with:

```bash
--cpus 0.5
```

then:

```bash
--cpus 2
```

Compare completion time.

### Lab 31 — PID Limit

Use a safe slow child-process spawning script with:

```bash
--pids-limit 50
```

Observe process creation failure.

### Lab 32 — Capability Hardening

Run a normal web app with:

```bash
--cap-drop ALL
--security-opt no-new-privileges:true
```

Add only a capability if application truly needs it.

### Lab 33 — Rootless Docker Study

Install/use rootless mode in a disposable Linux user environment or document architecture.

Compare:

```text
daemon UID
socket path
network
cgroups
host privilege
```

### Lab 34 — Seccomp

Inspect default profile behavior through official documentation.

Run a safe workload and explain why disabling seccomp is not an acceptable generic troubleshooting fix.

### Lab 35 — Registry Workflow

Use a private lab registry or cloud registry:

```text
login
tag
push
pull by digest
```

Document required permissions.

### Lab 36 — Supply-Chain Pipeline

Design:

```text
Git
 ↓
BuildKit
 ↓
SBOM
 ↓
scan
 ↓
sign
 ↓
registry
 ↓
deploy digest
```

Define a policy gate.

### Lab 37 — Compose Web + Database

Create:

```yaml
services:
  api:
  db:

volumes:
  dbdata:
```

Use service-name DNS, not localhost for DB.

### Lab 38 — Compose Health Dependencies

Add database healthcheck and API dependency.

Then stop DB after startup and confirm API still needs runtime retry handling.

### Lab 39 — Compose Networks

Create:

```text
frontend
backend
```

and isolate database.

### Lab 40 — Compose Profiles

Add optional:

```text
adminer
debug tools
```

under `debug` profile.

Start only when needed.

### Lab 41 — Compose Overrides

Create:

```text
compose.yaml
compose.dev.yaml
compose.prod.yaml
```

Use:

```bash
docker compose -f ... config
```

to inspect final merged config.

### Lab 42 — Compose Scale

Scale worker:

```bash
docker compose up -d --scale worker=3
```

Verify all replicas consume from queue or run identical stateless work.

### Lab 43 — Log Rotation and Disk Use

Inspect:

```bash
docker system df -v
```

Configure log rotation in a lab.

Generate logs and observe size.

### Lab 44 — Failure Troubleshooting Game Day

Simulate:

```text
bad entrypoint
wrong architecture
volume permission denied
DNS failure
port conflict
OOM
healthcheck failure
registry TLS failure
Compose env precedence bug
disk pressure
```

For each:

```text
Evidence
Root Cause
Fix
Verification
Prevention
```

### Lab 45 — Docker-to-Kubernetes Mapping

Create a mapping table:

```text
Docker image        → Kubernetes image
Docker container    → Pod container
Docker network DNS  → Service/CoreDNS
Docker volume       → PV/PVC
Docker healthcheck  → probes
Compose service     → Deployment/StatefulSet + Service
resource limits     → requests/limits
```

Explain which problems Docker Compose cannot solve across many hosts.

---

## 6. Mini Project

# Mini Project — Production-Style Docker Application Platform

Build a realistic local/single-host application using:

```text
Reverse Proxy
Frontend
API
Worker
PostgreSQL
Redis
```

Architecture:

```text
User
 ↓
Reverse Proxy
 ↓
Frontend / API
        |
        +------> PostgreSQL
        |
        +------> Redis
        |
        +------> Queue
                    |
                  Worker
```

## Repository

```text
docker-platform/
├── compose.yaml
├── compose.dev.yaml
├── compose.prod.yaml
├── .env.example
├── frontend/
│   └── Dockerfile
├── api/
│   └── Dockerfile
├── worker/
│   └── Dockerfile
├── proxy/
│   └── nginx.conf
├── scripts/
└── docs/
```

## Image Requirements

Every custom image must:

```text
use supported trusted base
use .dockerignore
use non-root user
avoid secrets
use multi-stage build where useful
include health behavior
define graceful stop behavior
carry source/version labels
be tagged with version
```

## Network Requirements

```text
frontend network:
  proxy
  frontend
  api

backend network:
  api
  worker
  postgres
  redis
```

Rules:

```text
PostgreSQL not published to host in production config
Redis not published to host
Only proxy exposes HTTP port
```

## Storage Requirements

Persistent:

```text
postgres_data
```

Optional persistent:

```text
redis_data
```

Ephemeral:

```text
/tmp
application caches
```

Create backup/restore script for PostgreSQL lab data.

## Security Requirements

Use:

```text
non-root
cap_drop where possible
no-new-privileges
read-only rootfs where possible
tmpfs for temporary writes
no Docker socket mount
no privileged mode
no host PID/network
short-lived registry credentials
no secrets in image
```

## Resource Requirements

Set/test resource policy for:

```text
API
Worker
PostgreSQL
Redis
```

Document:

```text
CPU
memory
PIDs
```

and expected behavior under pressure.

## Health Requirements

Create:

```text
API health
worker heartbeat/log metric
PostgreSQL health
Redis health
proxy health
```

Do not rely only on process existence.

## Compose Requirements

Use:

```text
services
networks
volumes
healthchecks
depends_on
profiles
environment
read_only
tmpfs
restart
```

where appropriate.

## Build Pipeline Design

```text
Git
 ↓
Buildx / BuildKit
 ↓
unit tests
 ↓
image build
 ↓
SBOM
 ↓
vulnerability scan
 ↓
signature / provenance
 ↓
registry
 ↓
pull by immutable version/digest
```

## Observability

Capture:

```text
structured stdout logs
container stats
health status
restart counts
disk use
application latency/errors
```

## Required Runbooks

```text
RUNBOOK_CONTAINER_EXIT.md
RUNBOOK_OOM.md
RUNBOOK_CPU_THROTTLE.md
RUNBOOK_VOLUME_PERMISSION.md
RUNBOOK_DATABASE_VOLUME.md
RUNBOOK_DNS_FAILURE.md
RUNBOOK_PORT_CONFLICT.md
RUNBOOK_REGISTRY_FAILURE.md
RUNBOOK_DISK_FULL.md
RUNBOOK_COMPOSE_DEPENDENCY.md
RUNBOOK_ROLLBACK.md
```

## Required Deliverables

```text
README.md
ARCHITECTURE.md
DOCKERFILES.md
COMPOSE.md
NETWORK.md
STORAGE.md
SECURITY.md
RESOURCE_LIMITS.md
SUPPLY_CHAIN.md
OBSERVABILITY.md
BACKUP_RESTORE.md
TROUBLESHOOTING.md
RUNBOOKS/
```

---

## 7. Recommended Resources

This Markdown is designed to be self-contained.

For current production syntax and behavior, use official Docker and OCI sources:

```text
Docker Engine documentation
Docker Engine release notes
Dockerfile reference
Docker Build / BuildKit / Buildx documentation
Docker storage documentation
Docker networking documentation
Docker security documentation
Docker rootless mode
Docker Compose Specification
Docker Compose reference
OCI Runtime/Image/Distribution specifications
```

Because Docker changes frequently, verify current behavior before production upgrades, especially:

```text
Engine patches
BuildKit
Buildx
Compose
networking behavior
security defaults
deprecated features
```

---

## 8. Certification Relevance

This is a practical foundation for:

```text
59. Kubernetes Fundamentals
60. Kubernetes Administration
61. OpenShift
CKA
CKAD
CKS
DevOps
Platform Engineering
Cloud-Native Development
DevSecOps
Container Security
```

It also builds skills used in:

```text
AWS ECS/EKS
Azure Container Apps/AKS
Google Cloud Run/GKE
CI/CD pipelines
local development environments
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Docker equals containers themselves.  
  **Best practice:** understand Docker as tooling over OCI/Linux container primitives.

- **Mistake:** Give every developer Docker socket access without considering privilege.  
  **Best practice:** treat daemon control as admin-equivalent.

- **Mistake:** Use `latest` for production releases.  
  **Best practice:** immutable version and digest.

- **Mistake:** Bake secrets into Dockerfile/image.  
  **Best practice:** BuildKit secrets + runtime secret management.

- **Mistake:** Run as root.  
  **Best practice:** non-root USER.

- **Mistake:** `--privileged` to solve errors.  
  **Best practice:** identify exact capability/mount/security requirement.

- **Mistake:** No memory/CPU/PID limits.  
  **Best practice:** measure and constrain.

- **Mistake:** Store DB data in writable layer.  
  **Best practice:** persistent volume + backup.

- **Mistake:** Publish every service port.  
  **Best practice:** internal networks; publish only entrypoint.

- **Mistake:** Use `localhost` to reach another container.  
  **Best practice:** service/container DNS name.

- **Mistake:** App binds to `127.0.0.1` inside container.  
  **Best practice:** bind to appropriate container interface such as `0.0.0.0` when network clients must reach it.

- **Mistake:** Use Compose `depends_on` as complete availability logic.  
  **Best practice:** application retry/backoff + health checks.

- **Mistake:** Keep unbounded local logs.  
  **Best practice:** log rotation/centralization.

- **Mistake:** Run `docker system prune -a --volumes` blindly.  
  **Best practice:** inspect disk ownership/state first.

- **Mistake:** Modify running containers manually.  
  **Best practice:** rebuild image and replace.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Docker CLI talks to what?

**Answer:** Docker Engine API/daemon.

### Q2. Docker Engine uses which high-level runtime?

**Answer:** containerd.

### Q3. Typical low-level OCI runtime?

**Answer:** runc.

### Q4. Current course Engine baseline?

**Answer:** Docker Engine 29.x, with 29.7.2 checked for this material.

### Q5. Modern Docker build backend?

**Answer:** BuildKit, driven through Buildx.

### Q6. Compose command style?

**Answer:** `docker compose`.

### Q7. `docker run` roughly equals?

**Answer:** `docker create` + `docker start` plus attach/options.

### Q8. `docker exec`?

**Answer:** Starts an additional process inside a running container.

### Q9. `docker attach`?

**Answer:** Attaches to primary process streams.

### Q10. `COPY` vs `ADD`?

**Answer:** COPY performs normal context copy; ADD has additional behaviors such as archive extraction/remote-source handling.

### Q11. `ARG` secure for secrets?

**Answer:** No.

### Q12. `EXPOSE` publish a host port?

**Answer:** No.

### Q13. Exec-form CMD benefit?

**Answer:** Direct process execution and cleaner signal handling.

### Q14. Multi-stage build?

**Answer:** Uses separate builder/runtime stages to keep build tools out of final image.

### Q15. BuildKit secret mount?

**Answer:** Provides build-time secret without baking it into normal image layers.

### Q16. Named volume?

**Answer:** Docker-managed persistent storage that can outlive containers.

### Q17. Bind mount?

**Answer:** Direct host-path mount into container.

### Q18. tmpfs?

**Answer:** Memory-backed temporary mount.

### Q19. User-defined bridge advantage?

**Answer:** Better isolation and built-in DNS/service-name resolution.

### Q20. `-p 8080:80`?

**Answer:** Host port 8080 maps to container port 80.

### Q21. Container-to-container needs published port?

**Answer:** No, if services share a Docker network and connect to container port.

### Q22. Default resource constraints?

**Answer:** Containers have no explicit resource limits unless configured.

### Q23. `--memory`?

**Answer:** Sets memory limit.

### Q24. `--cpus`?

**Answer:** Sets CPU quota-like limit.

### Q25. `--pids-limit`?

**Answer:** Limits number of processes.

### Q26. Rootless Docker?

**Answer:** Runs daemon and containers without host-root privileges where supported.

### Q27. Docker socket risk?

**Answer:** Control of socket can effectively provide host administrative control.

### Q28. Compose default network?

**Answer:** Project-scoped network connecting services by service-name DNS.

### Q29. `docker compose config`?

**Answer:** Renders merged/interpolated normalized Compose configuration.

### Q30. `docker compose down -v` risk?

**Answer:** Removes project volumes and can destroy persistent data.

### Q31. Healthcheck automatically restart standalone container?

**Answer:** Health status alone does not inherently restart it; restart/orchestration behavior is separate.

### Q32. `docker system df`?

**Answer:** Shows Docker disk usage.

### Q33. `docker events`?

**Answer:** Streams Docker lifecycle/system events.

### Q34. Save/load vs export/import?

**Answer:** Save/load preserves image layers/metadata; export/import handles flattened container filesystem.

### Q35. Docker to Kubernetes transition?

**Answer:** Kubernetes adds multi-node scheduling, controllers, Services, probes, persistent-volume orchestration, policy, and cluster management.

---

# Expanded Self-Assessment Bank — Docker Fundamentals

### Q1. What is the key engineering lesson from **Docker Client/API/Daemon Boundary**?

**Answer:** Troubleshoot client context and daemon health before debugging the container itself.

### Q2. What is the key engineering lesson from **Unix Socket Privilege**?

**Answer:** Treat Docker socket access as administrative privilege.

### Q3. What is the key engineering lesson from **Remote Docker over SSH**?

**Answer:** Prefer SSH or properly authenticated TLS over public unauthenticated daemon TCP.

### Q4. What is the key engineering lesson from **Mutual TLS Daemon API Concept**?

**Answer:** Do not expose the rootful daemon API to untrusted networks.

### Q5. What is the key engineering lesson from **Context Safety**?

**Answer:** Make context verification part of every operational runbook.

### Q6. What is the key engineering lesson from **DOCKER_HOST Precedence Risk**?

**Answer:** Keep endpoint selection explicit and avoid hidden environment overrides in production automation.

### Q7. What is the key engineering lesson from **Daemon Configuration Validation**?

**Answer:** Validate daemon configuration before restart and keep a rollback copy.

### Q8. What is the key engineering lesson from **systemd Service Evidence**?

**Answer:** Use systemd/journal evidence before reinstalling Docker.

### Q9. What is the key engineering lesson from **Data Root**?

**Answer:** Never manually delete Docker data-root files while the daemon is managing them.

### Q10. What is the key engineering lesson from **Data Root Migration**?

**Answer:** Treat Docker data-root movement as storage migration, not a simple directory rename.

### Q11. What is the key engineering lesson from **Live Restore Limits**?

**Answer:** Test daemon-maintenance behavior on the exact host/runtime configuration.

### Q12. What is the key engineering lesson from **containerd Shim Role**?

**Answer:** Use the runtime stack mental model when diagnosing daemon-versus-container failures.

### Q13. What is the key engineering lesson from **Storage Driver vs Volume Driver**?

**Answer:** Do not troubleshoot database-volume performance as if it were only an overlay storage-driver issue.

### Q14. What is the key engineering lesson from **overlay2 Copy-Up**?

**Answer:** Keep databases and heavy mutable data off the container writable layer.

### Q15. What is the key engineering lesson from **Container Writable-Layer Recovery**?

**Answer:** Assume the writable layer can disappear at any time.

### Q16. What is the key engineering lesson from **Named Volume Ownership**?

**Answer:** Fix numeric ownership intentionally instead of running the application as root.

### Q17. What is the key engineering lesson from **Volume Backup Consistency**?

**Answer:** Use database-native backup for transactional data unless storage snapshots are integrated with quiescing.

### Q18. What is the key engineering lesson from **Bind Mount Portability**?

**Answer:** Use bind mounts deliberately for host integration; use immutable images/managed volumes for portable production workloads.

### Q19. What is the key engineering lesson from **Bind Mount Propagation**?

**Answer:** Keep ordinary application bind mounts private.

### Q20. What is the key engineering lesson from **tmpfs Mount Security**?

**Answer:** Use tmpfs for short-lived data that should not persist, while accounting for memory usage.

### Q21. What is the key engineering lesson from **Dockerfile Syntax Directive**?

**Answer:** Pin/standardize build frontend expectations in CI for reproducible builds.

### Q22. What is the key engineering lesson from **Dockerfile ARG Scope**?

**Answer:** Use ARG for non-secret build parameters and understand stage scope.

### Q23. What is the key engineering lesson from **ENV vs ARG**?

**Answer:** Keep secrets out of both ARG and ENV image metadata.

### Q24. What is the key engineering lesson from **ONBUILD Instruction Concept**?

**Answer:** Avoid ONBUILD in general-purpose bases unless the implicit behavior is well documented.

### Q25. What is the key engineering lesson from **Heredoc Build Steps**?

**Answer:** Use heredocs for clarity, not to hide large unmaintainable shell scripts.

### Q26. What is the key engineering lesson from **COPY Ownership**?

**Answer:** Set ownership during copy where supported instead of adding wasteful correction layers.

### Q27. What is the key engineering lesson from **COPY --link Concept**?

**Answer:** Use advanced Dockerfile features only when CI/builders are standardized and tested.

### Q28. What is the key engineering lesson from **Build Context Minimization**?

**Answer:** Keep build context intentionally small and secret-free.

### Q29. What is the key engineering lesson from **Remote/Git Build Context Trust**?

**Answer:** Pin remote source and record the resolved commit in provenance.

### Q30. What is the key engineering lesson from **BuildKit LLB Mental Model**?

**Answer:** Optimize build dependency graphs, not only Dockerfile layer count.

### Q31. What is the key engineering lesson from **Build Cache Key**?

**Answer:** Order stable dependency inputs before frequently changing application files.

### Q32. What is the key engineering lesson from **BuildKit Cache Mount**?

**Answer:** Use cache mounts for performance, not for required runtime content.

### Q33. What is the key engineering lesson from **BuildKit Secret Lifetime**?

**Answer:** Never echo, copy, or persist BuildKit secrets into layers/logs.

### Q34. What is the key engineering lesson from **BuildKit SSH Mount**?

**Answer:** Use short-lived/agent-forwarded build identity rather than copying private keys.

### Q35. What is the key engineering lesson from **Build Cache Export/Import**?

**Answer:** Separate caches across trust boundaries and do not treat cache as authoritative source code.

### Q36. What is the key engineering lesson from **Buildx Builder Drivers**?

**Answer:** Inspect the builder before diagnosing multi-platform or cache behavior.

### Q37. What is the key engineering lesson from **Multi-Platform Emulation vs Native Build**?

**Answer:** Use native builders for heavy architecture-specific compilation when practical.

### Q38. What is the key engineering lesson from **Cross-Compilation Stage Pattern**?

**Answer:** Prefer language-native cross-compilation when it is well supported.

### Q39. What is the key engineering lesson from **Build Provenance**?

**Answer:** Store provenance alongside immutable image digests.

### Q40. What is the key engineering lesson from **SBOM Build Output**?

**Answer:** Generate and retain SBOMs for release images.

### Q41. What is the key engineering lesson from **Multi-Stage Test Gate**?

**Answer:** Separate build/test/runtime concerns into explicit stages.

### Q42. What is the key engineering lesson from **Distroless Debug Strategy**?

**Answer:** Do not add permanent admin tooling to production solely for convenience.

### Q43. What is the key engineering lesson from **Base Image Digest Updates**?

**Answer:** Pair digest pinning with scheduled dependency/security update automation.

### Q44. What is the key engineering lesson from **Image Promotion by Digest**?

**Answer:** Use digest as the release identity and tags as human metadata.

### Q45. What is the key engineering lesson from **Registry Credential Helper**?

**Answer:** Use credential helpers or short-lived cloud tokens for registry authentication.

### Q46. What is the key engineering lesson from **Registry Token Scope**?

**Answer:** Apply least privilege to registry actions just like cloud IAM.

### Q47. What is the key engineering lesson from **Private Registry TLS**?

**Answer:** Fix CA trust, chain, hostname, proxy, or clock rather than marking production registries insecure.

### Q48. What is the key engineering lesson from **Registry Mirror / Pull-Through Cache**?

**Answer:** Secure and monitor mirrors like production registries.

### Q49. What is the key engineering lesson from **Image Scan Context**?

**Answer:** Re-scan deployed digests as vulnerability intelligence changes.

### Q50. What is the key engineering lesson from **Signature vs Digest**?

**Answer:** Verify signatures/attestations against immutable digests.

### Q51. What is the key engineering lesson from **Runtime Image Policy**?

**Answer:** Convert recurring review rules into policy-as-code when the platform supports it.

### Q52. What is the key engineering lesson from **Default Bridge vs User-Defined Bridge**?

**Answer:** Create one or more application networks rather than depending on default bridge behavior.

### Q53. What is the key engineering lesson from **Embedded Docker DNS**?

**Answer:** Use service names, not container IPs.

### Q54. What is the key engineering lesson from **Application Bind Address**?

**Answer:** Check the application socket before changing Docker networking.

### Q55. What is the key engineering lesson from **Published-Port Exposure**?

**Answer:** Publish only the entrypoint ports and bind to the narrowest host interface.

### Q56. What is the key engineering lesson from **Docker Firewall Interaction**?

**Answer:** Test host-firewall changes with Docker networking instead of assuming rule order.

### Q57. What is the key engineering lesson from **DOCKER-USER Policy Concept**?

**Answer:** Place administrator policy in supported extension points rather than editing Docker-managed rules manually.

### Q58. What is the key engineering lesson from **Network Namespace Inspection**?

**Answer:** Use namespace evidence when Docker-level inspection is insufficient.

### Q59. What is the key engineering lesson from **DNS Failure Decomposition**?

**Answer:** Do not change bridge subnets to fix a resolver-only problem.

### Q60. What is the key engineering lesson from **Corporate VPN Overlap**?

**Answer:** Plan non-overlapping container address pools before large-scale developer rollout.

### Q61. What is the key engineering lesson from **MTU Diagnosis**?

**Answer:** Account for tunnel overhead instead of disabling TLS or changing application timeouts first.

### Q62. What is the key engineering lesson from **Host Network Trade-Off**?

**Answer:** Use host networking only when a measured compatibility/performance requirement justifies it.

### Q63. What is the key engineering lesson from **None Network**?

**Answer:** Use no-network execution for jobs that do not need network access.

### Q64. What is the key engineering lesson from **macvlan / ipvlan Decision**?

**Answer:** Prefer bridge networking unless direct network presence is required.

### Q65. What is the key engineering lesson from **Container Connection Refused vs Timeout**?

**Answer:** Use the error semantics as a clue, not an absolute diagnosis.

### Q66. What is the key engineering lesson from **Container Resource Defaults**?

**Answer:** Set intentional resource controls from measured workload behavior.

### Q67. What is the key engineering lesson from **Memory Reservation vs Hard Limit**?

**Answer:** Size memory from startup peak, steady working set, and failure behavior.

### Q68. What is the key engineering lesson from **OOM Evidence**?

**Answer:** Confirm OOM before raising memory limits.

### Q69. What is the key engineering lesson from **CPU Quota vs Shares**?

**Answer:** Use quota for containment and shares/weight for relative fairness.

### Q70. What is the key engineering lesson from **CPU Throttling Diagnosis**?

**Answer:** Investigate throttling counters when latency rises under CPU limits.

### Q71. What is the key engineering lesson from **PIDs Limit**?

**Answer:** Set realistic PID limits for services with bounded concurrency models.

### Q72. What is the key engineering lesson from **ulimits**?

**Answer:** Capacity-plan file descriptors for high-concurrency servers.

### Q73. What is the key engineering lesson from **Shared Memory Size**?

**Answer:** Increase shared memory only for workloads that actually require it.

### Q74. What is the key engineering lesson from **Read-Only Root + Explicit Writes**?

**Answer:** Use read-only root filesystems for compatible stateless services.

### Q75. What is the key engineering lesson from **Capability Minimization**?

**Answer:** Solve privilege errors with the narrow required capability, not `--privileged`.

### Q76. What is the key engineering lesson from **no-new-privileges**?

**Answer:** Use no-new-privileges for ordinary application containers.

### Q77. What is the key engineering lesson from **Seccomp Failure Diagnosis**?

**Answer:** Treat `seccomp=unconfined` only as a temporary controlled diagnostic step, not a production fix.

### Q78. What is the key engineering lesson from **AppArmor / SELinux Mount Denials**?

**Answer:** Fix labels/profile policy rather than chmod 777 or disabling the LSM.

### Q79. What is the key engineering lesson from **Rootless Docker Threat Reduction**?

**Answer:** Use rootless where its feature/performance trade-offs fit the workload.

### Q80. What is the key engineering lesson from **userns-remap vs Rootless**?

**Answer:** Choose the model intentionally instead of treating both features as equivalent.

### Q81. What is the key engineering lesson from **Host PID / Host IPC / Host Network Risk**?

**Answer:** Never enable host namespaces to solve an unrelated connectivity or permission issue.

### Q82. What is the key engineering lesson from **Device Access**?

**Answer:** Expose only exact required devices and keep them out of ordinary web workloads.

### Q83. What is the key engineering lesson from **Compose Project Isolation**?

**Answer:** Set explicit project names in CI and shared hosts to avoid collisions.

### Q84. What is the key engineering lesson from **Compose Config as Source of Truth**?

**Answer:** Debug the rendered configuration before editing service code.

### Q85. What is the key engineering lesson from **Compose Environment Precedence**?

**Answer:** Document configuration ownership and avoid duplicating the same variable across many precedence layers.

### Q86. What is the key engineering lesson from **Compose Secrets Are Not Magic Encryption**?

**Answer:** Protect the underlying secret source and never commit it to Git.

### Q87. What is the key engineering lesson from **Compose depends_on vs Runtime Resilience**?

**Answer:** Use Compose dependency logic for startup convenience, not as a substitute for resilient application design.

### Q88. What is the key engineering lesson from **Compose Healthcheck Design**?

**Answer:** Separate local process health from external dependency readiness when possible.

### Q89. What is the key engineering lesson from **Compose Profiles**?

**Answer:** Keep privileged or debug tooling opt-in and disabled by default.

### Q90. What is the key engineering lesson from **Compose Override Discipline**?

**Answer:** Review rendered Compose configuration in CI.

### Q91. What is the key engineering lesson from **Compose Scaling and Fixed Ports**?

**Answer:** Publish only entrypoint/proxy ports; keep scalable workers on internal networks.

### Q92. What is the key engineering lesson from **Compose Network Least Privilege**?

**Answer:** Treat network membership as a least-privilege control.

### Q93. What is the key engineering lesson from **Compose Volume Destruction**?

**Answer:** Separate disposable test stacks from data-bearing environments and require confirmation for volume deletion.

### Q94. What is the key engineering lesson from **Compose Read-Only Service**?

**Answer:** Harden from a working least-privilege baseline and document required exceptions.

### Q95. What is the key engineering lesson from **Compose One-Off Jobs**?

**Answer:** Use `run --rm` for jobs/tests and `exec` for temporary investigation.

### Q96. What is the key engineering lesson from **Logging Driver Selection**?

**Answer:** Choose a driver and retention model that cannot fill the host silently.

### Q97. What is the key engineering lesson from **Blocking vs Non-Blocking Logging Concept**?

**Answer:** Decide whether logs may be dropped versus allowed to block application throughput.

### Q98. What is the key engineering lesson from **Log Rotation**?

**Answer:** Set log size/retention limits and monitor the host filesystem.

### Q99. What is the key engineering lesson from **Docker Events as Timeline**?

**Answer:** Capture event timelines during restart loops and unexplained container replacement.

### Q100. What is the key engineering lesson from **docker inspect Release Evidence**?

**Answer:** Capture inspect output before replacing a failing container.

### Q101. What is the key engineering lesson from **docker diff for Drift**?

**Answer:** Treat significant runtime drift as a signal to fix image/configuration rather than preserving the mutated container.

### Q102. What is the key engineering lesson from **docker system df**?

**Answer:** Inspect usage before pruning anything.

### Q103. What is the key engineering lesson from **Prune Safety**?

**Answer:** Never run broad prune commands blindly on important hosts.

### Q104. What is the key engineering lesson from **Inode Exhaustion**?

**Answer:** Monitor both disk space and inode pressure.

### Q105. What is the key engineering lesson from **Daemon Metrics / Host Monitoring Concept**?

**Answer:** Alert on user/service impact and use container/host metrics for diagnosis.

### Q106. What is the key engineering lesson from **docker stats Limitations**?

**Answer:** Export long-term metrics to a monitoring system and correlate with application telemetry.

### Q107. What is the key engineering lesson from **Health Status vs Restart**?

**Answer:** Use orchestration/supervision logic explicitly if unhealthy state should trigger replacement.

### Q108. What is the key engineering lesson from **Restart Loop Backoff Awareness**?

**Answer:** Fix the failing entrypoint/config/dependency instead of relying on infinite restart.

### Q109. What is the key engineering lesson from **Graceful HTTP Shutdown**?

**Answer:** Set stop timeout from measured worst-case drain time.

### Q110. What is the key engineering lesson from **Queue Worker Shutdown**?

**Answer:** Design graceful stop around message acknowledgement semantics.

### Q111. What is the key engineering lesson from **Time Synchronization**?

**Answer:** Fix host time synchronization rather than configuring independent container clocks.

### Q112. What is the key engineering lesson from **Proxy Layers**?

**Answer:** Document proxy configuration by layer.

### Q113. What is the key engineering lesson from **NO_PROXY Design**?

**Answer:** Test internal service names and cloud metadata/private endpoints explicitly.

### Q114. What is the key engineering lesson from **Registry Pull Failure Workflow**?

**Answer:** Do not solve TLS/auth errors by marking the registry insecure.

### Q115. What is the key engineering lesson from **Wrong Architecture**?

**Answer:** Publish and test every required platform in multi-architecture releases.

### Q116. What is the key engineering lesson from **Container Immediately Exits**?

**Answer:** Diagnose the primary process before adding restart policies.

### Q117. What is the key engineering lesson from **Volume Permission Failure**?

**Answer:** Fix the exact permission layer instead of using root or chmod 777.

### Q118. What is the key engineering lesson from **Published Port Failure**?

**Answer:** Check the listener before changing host firewall.

### Q119. What is the key engineering lesson from **Compose Dependency Failure**?

**Answer:** Troubleshoot from inside the client container, not only from the host.

### Q120. What is the key engineering lesson from **Disk Pressure Incident**?

**Answer:** Free space through known Docker objects/log policy, not by deleting internal metadata files.

### Q121. What is the key engineering lesson from **Build Failure Network Decomposition**?

**Answer:** Debug build networking independently from runtime container networking.

### Q122. What is the key engineering lesson from **Build Reproducibility Evidence**?

**Answer:** Make reproducibility metadata part of the CI artifact record.

### Q123. What is the key engineering lesson from **CI Least Privilege**?

**Answer:** Separate build, deploy, and runtime identities.

### Q124. What is the key engineering lesson from **Build Runner Isolation**?

**Answer:** Prefer ephemeral isolated builders for sensitive CI.

### Q125. What is the key engineering lesson from **Secret Leakage in Logs**?

**Answer:** Redact logs and disable shell tracing around secret-handling steps.

### Q126. What is the key engineering lesson from **Dockerfile Lint / Policy Gate**?

**Answer:** Automate repeatable Dockerfile review rules.

### Q127. What is the key engineering lesson from **Release Rollback**?

**Answer:** Retain immutable release digests for the full rollback/support window.

### Q128. What is the key engineering lesson from **Schema Migration Compatibility**?

**Answer:** Use expand/contract database migrations for reversible deployments.

### Q129. What is the key engineering lesson from **Operational Readiness Review**?

**Answer:** Make operational readiness a deployment gate.

### Q130. What is the key engineering lesson from **Evidence-First Docker Troubleshooting**?

**Answer:** Preserve inspect/log/event evidence and change one layer at a time.

### Q131. What is the key engineering lesson from **Docker-to-Kubernetes Image Boundary**?

**Answer:** Separate Docker Engine administration skills from OCI image engineering skills.

### Q132. What is the key engineering lesson from **Compose-to-Kubernetes Mapping**?

**Answer:** Use Docker/Compose to master containers before adding cluster orchestration complexity.

## Completion Checklist

- [ ] I understand Docker architecture.
- [ ] I understand daemon/client/API/containerd/runc.
- [ ] I can install and verify Docker.
- [ ] I understand Docker contexts.
- [ ] I can operate container lifecycle.
- [ ] I understand signals/PID 1/restart policies.
- [ ] I can write production-oriented Dockerfiles.
- [ ] I understand BuildKit and Buildx.
- [ ] I understand cache and secret mounts.
- [ ] I can build multi-stage images.
- [ ] I understand multi-platform builds.
- [ ] I understand tags/digests/registries.
- [ ] I understand save/load/export/import.
- [ ] I can manage volumes/bind/tmpfs.
- [ ] I understand persistent backup/restore.
- [ ] I can design Docker networks.
- [ ] I understand DNS/ports/bridges/NAT.
- [ ] I can set resource limits.
- [ ] I understand non-root/read-only/capabilities.
- [ ] I understand seccomp/LSMs.
- [ ] I understand rootless/userns.
- [ ] I understand registry/supply-chain security.
- [ ] I can use Docker Compose deeply.
- [ ] I understand Compose networks/volumes/health/dependencies.
- [ ] I understand logging/events/disk management.
- [ ] I can troubleshoot Docker systematically.
- [ ] I understand basic Swarm concepts.
- [ ] I completed all 45 labs.
- [ ] I completed the Production-Style Docker Application Platform project.
