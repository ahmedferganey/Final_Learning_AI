# Phase 15 — Containers

This phase develops the container platform stack from Linux container fundamentals through Docker, Kubernetes, Kubernetes administration, and enterprise OpenShift.

## Courses

```text
57. Application Containers
58. Docker Fundamentals
59. Kubernetes Fundamentals
60. Kubernetes Administration
61. OpenShift
```

## Recommended Order

```text
57. Application Containers
        ↓
58. Docker Fundamentals
        ↓
59. Kubernetes Fundamentals
        ↓
60. Kubernetes Administration
        ↓
61. OpenShift
```

## Phase Goal

By the end of Phase 15, you should be able to:

- Explain Linux container internals including namespaces, cgroups, OCI images, runtimes, storage, networking, and container security.
- Build, run, secure, network, store, observe, and troubleshoot applications with Docker.
- Use Dockerfile, BuildKit, Buildx, registries, multi-stage builds, Compose, and container supply-chain controls.
- Understand Kubernetes architecture, declarative reconciliation, Pods, controllers, Services, configuration, storage, networking, security, scheduling, and autoscaling.
- Install and administer Kubernetes clusters using kubeadm, containerd, CNI, CSI, CoreDNS, RBAC, PKI, etcd backup/restore, upgrades, observability, and systematic troubleshooting.
- Administer Red Hat OpenShift Container Platform using `oc`, Cluster Operators, CVO, MCO, RHCOS, CRI-O, OVN-Kubernetes, Routes, SCCs, Operators, storage, monitoring, updates, and support tooling.
- Design production container platforms with high availability, least privilege, persistent storage, observability, backup and recovery, upgrade procedures, and operational runbooks.

## Current Course Baselines

```text
Application Containers:
  OCI Runtime/Image/Distribution specifications

Docker Fundamentals:
  Docker Engine 29.x

Kubernetes Fundamentals / Administration:
  Kubernetes v1.36-era upstream behavior

OpenShift:
  Current production study baseline: OpenShift Container Platform 4.22
  Underlying Kubernetes: 1.35
  Runtime: CRI-O

OpenShift certification:
  EX280 — Red Hat Certified System Administrator in OpenShift
  Current exam baseline: OpenShift Container Platform 4.18
```

## Folder Structure

```text
Phase_15_Containers/
│
├── README.md
├── 57_Application_Containers.md
├── 58_Docker_Fundamentals.md
├── 59_Kubernetes_Fundamentals.md
├── 60_Kubernetes_Administration.md
└── 61_OpenShift.md
```

## Main Progression

```text
Linux Processes
      ↓
Application Containers
      ↓
Docker
      ↓
Kubernetes Workloads
      ↓
Kubernetes Cluster Administration
      ↓
Enterprise OpenShift Platform
```

## Next Phase

```text
Phase 16 — Infrastructure as Code

62. Infrastructure as Code Fundamentals
63. Terraform
64. Terraform Remote State Management
```
