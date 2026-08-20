# 41. OpenStack Fundamentals

> Phase 9 — Virtualization

This course moves from **virtualization platform administration** into **open-source Infrastructure as a Service (IaaS)**.

**Current reference baseline:** OpenStack **2026.1 “Gazpacho”**, released in April 2026 and listed as the current maintained release at the time this course was prepared.

The most important distinction is:

```text
Hypervisor
    creates/runs virtual machines

OpenStack
    coordinates pools of compute,
    networking,
    storage,
    identity,
    images,
    and APIs
    into a cloud service
```

A simple mental model is:

```text
                        User / Application
                              |
                CLI / Horizon / REST API
                              |
                           Keystone
                         Authentication
                              |
        +---------------------+---------------------+
        |                     |                     |
       Nova                Neutron                Cinder
     Compute              Networking          Block Storage
        |                     |                     |
     Placement             Virtual/             Storage
     Scheduler             Physical             Backends
        |                  Networking
     Compute
       Nodes
        |
   KVM / libvirt
        |
       VMs

        Glance = Images
        Swift = Object Storage
        Horizon = Dashboard
        Heat = Orchestration
        Barbican = Secrets
        Octavia = Load Balancing
```

OpenStack is intentionally modular. You do not need every service to operate a useful cloud.

The learning pattern is:

```text
Cloud Concept
   ↓
OpenStack Service
   ↓
Architecture Diagram
   ↓
openstack CLI / YAML Example
   ↓
Request Flow
   ↓
Failure Scenario
   ↓
Troubleshooting
```

Course 41 focuses on **how OpenStack works and how a cloud consumer/administrator thinks about it**. Course 42 will go deeper into deployment and operations.

---

## 1. Topic Title

**OpenStack Fundamentals**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain what OpenStack is and what problem it solves.
- Differentiate OpenStack from VMware vSphere, Kubernetes, and a hypervisor.
- Explain public, private, hybrid, and edge-cloud use cases.
- Explain OpenStack's modular service architecture.
- Explain controller, compute, network, storage, and supporting infrastructure roles.
- Explain Keystone identity concepts: domains, users, groups, projects, roles, assignments, tokens, service catalog, and endpoints.
- Explain application credentials and why automation should avoid human passwords.
- Explain Nova Compute architecture.
- Explain Placement and resource-provider concepts.
- Explain Nova Scheduler fundamentals.
- Explain cells conceptually.
- Explain KVM/libvirt integration on compute nodes.
- Explain flavors, images, instances, key pairs, metadata, user data, and cloud-init.
- Explain Glance Image service.
- Explain image formats and properties.
- Explain Neutron networking architecture.
- Differentiate provider and self-service networks.
- Explain networks, subnets, ports, routers, security groups, fixed IPs, floating IPs, DHCP, metadata, and NAT.
- Explain Open vSwitch/OVN at a conceptual level without tying OpenStack to one backend.
- Explain Cinder block-storage architecture.
- Explain volume types, attachment, snapshots, backups, and availability zones.
- Explain Swift object-storage fundamentals.
- Explain Horizon dashboard.
- Explain Heat orchestration fundamentals.
- Explain Octavia load-balancing fundamentals.
- Explain Barbican secret-management fundamentals.
- Explain Manila shared-file service conceptually.
- Explain Ironic bare-metal provisioning conceptually.
- Explain Designate DNS-as-a-Service conceptually.
- Explain telemetry/observability service categories.
- Explain API-first design and service endpoints.
- Configure OpenStack CLI authentication with `clouds.yaml` or environment variables.
- Use `openstack` CLI to inspect/create common cloud resources in an authorized lab.
- Explain quotas and multi-tenancy.
- Explain availability zones, host aggregates, and scheduling hints conceptually.
- Explain metadata service and cloud-init bootstrapping.
- Explain instance-build request flow end-to-end.
- Explain control-plane dependencies such as SQL databases and message queues.
- Explain OpenStack security groups versus host/firewall security.
- Explain cloud image security and key-pair handling.
- Explain high availability and failure domains at a fundamentals level.
- Explain backup, disaster recovery, and control-plane recovery concepts.
- Monitor core service/API health and troubleshoot common instance, network, volume, and identity failures.
- Build a complete OpenStack private-cloud design mini project.

---

## 3. Prerequisites

Recommended:

- 38. Virtualization Fundamentals
- 39. VMware vSphere administration
- 40. VMware NSX is helpful for software-defined networking comparisons
- Linux system administration
- networking and subnetting
- routing/NAT/firewalls
- storage fundamentals
- databases and message-queue fundamentals are helpful
- Python/REST/JSON basics

Recommended learning lab:

```text
OpenStack Cloud
   |
   +-- Project: lab-project
   +-- Network: lab-net
   +-- Router: lab-router
   +-- Image: Ubuntu
   +-- Flavor: lab.small
   +-- Instance: vm01
   +-- Volume: data01
```

If you do not have an OpenStack cloud, all CLI sections can still be studied as architecture exercises before Course 42.

---

## 4. Core Concepts Explanation

# Part 1 — What OpenStack Is

OpenStack is an open-source cloud infrastructure platform that controls pools of:

```text
compute
network
block storage
object storage
images
identity
```

through APIs and common authentication.

The output is an IaaS cloud.

# Part 2 — OpenStack Is Not a Hypervisor

Wrong model:

```text
OpenStack = another ESXi
```

Correct model:

```text
OpenStack
   ↓
Nova Compute
   ↓
libvirt
   ↓
KVM/QEMU
   ↓
Physical Hardware
```

OpenStack orchestrates the hypervisor layer.

# Part 3 — OpenStack vs vSphere

A simplified comparison:

```text
vSphere
  virtualization-centered platform
  ESX + vCenter + related services

OpenStack
  API-first IaaS cloud platform
  modular services around compute/network/storage/identity
```

Both can run private cloud workloads, but their architecture and operating models differ.

# Part 4 — OpenStack vs Kubernetes

```text
OpenStack:
IaaS
VMs, networks, volumes, images

Kubernetes:
container orchestration
Pods, Services, Deployments
```

Kubernetes can run **on top of** OpenStack VMs/bare metal.

# Part 5 — Private Cloud

```text
Organization Data Center
        |
     OpenStack
        |
Self-Service Projects
        |
VMs / Networks / Volumes
```

The organization owns/operates the cloud platform.

# Part 6 — Public Cloud

A provider can offer OpenStack-backed services to customers.

Users consume:

```text
API
CLI
Dashboard
```

without managing physical infrastructure.

# Part 7 — Edge Cloud

OpenStack is also used in distributed/edge environments such as telecom and retail, where compute must be placed close to workloads/users.

# Part 8 — Modular Architecture

OpenStack is a set of projects/services rather than one monolithic daemon.

Core service families include:

```text
Keystone   Identity
Nova       Compute
Placement  Resource inventory/allocation
Neutron    Networking
Glance     Images
Cinder     Block Storage
Swift      Object Storage
Horizon    Dashboard
```

Optional/common services include:

```text
Heat       Orchestration
Octavia    Load Balancing
Barbican   Secrets
Manila     Shared Filesystems
Ironic     Bare Metal
Designate  DNS
```

# Part 9 — Control Plane vs Data Plane

Control plane:

```text
APIs
Schedulers
Databases
Message queues
Controllers
```

Data plane:

```text
VM packets
storage I/O
instance execution
```

A control-plane outage can prevent new provisioning while already-running instances continue.

# Part 10 — Typical Node Roles

```text
Controller Nodes
  APIs
  schedulers
  identity
  databases
  message queue

Compute Nodes
  hypervisor
  instance execution

Network Functions
  virtual switching/routing depending backend

Storage Nodes
  block/object/file backends
```

Modern deployment tooling may combine/separate these differently.

# Part 11 — OpenStack APIs

Every major service exposes an HTTP API.

```text
Client
  |
HTTPS REST
  |
Service API
```

This API-first model makes automation central, not optional.

# Part 12 — OpenStack Client

The unified CLI uses commands such as:

```bash
openstack server list
openstack network list
openstack volume list
openstack image list
```

One CLI interacts with multiple service APIs.

# Part 13 — Keystone Identity Service

Keystone answers:

```text
Who are you?
What project/domain are you acting in?
What roles do you have?
Which service endpoints exist?
```

# Part 14 — Domain

A domain is a high-level administrative boundary containing identity resources such as users/groups/projects.

```text
Domain: ExampleCorp
  |
  +-- Users
  +-- Groups
  +-- Projects
```

# Part 15 — Project

Project is a tenancy/resource-ownership boundary.

```text
Project: Production
  |
  +-- Instances
  +-- Networks
  +-- Volumes
  +-- Floating IPs
```

Historically, “tenant” often referred to what is now called a project.

# Part 16 — User

A user is an identity that can authenticate.

Example:

```text
ahmed
backup-service
terraform-ci
```

Human and machine identities should be handled differently.

# Part 17 — Group

Groups simplify role assignment.

```text
Group: Cloud-Developers
   |
   +-- Alice
   +-- Bob
```

Assign the group rather than many individuals.

# Part 18 — Role

Roles express authorization level.

Examples commonly seen in modern OpenStack policy models include concepts such as:

```text
reader
member
manager/admin depending service/policy
```

Exact policy names and permissions are service-configurable.

# Part 19 — Role Assignment

Think of a role assignment as:

```text
Identity
 +
Role
 +
Scope
```

Example:

```text
User Ahmed
Role member
Project Production
```

# Part 20 — Authentication vs Authorization

```text
Authentication:
Who are you?

Authorization:
What may you do?
```

Keystone participates in both identity and token/role context.

# Part 21 — Token

After successful authentication, a client receives a scoped token.

```text
Credentials
   ↓
Keystone
   ↓
Token
   ↓
Service API
```

Tokens expire.

# Part 22 — Service Catalog

Keystone exposes a catalog of services/endpoints.

Concept:

```text
compute -> Nova URL
network -> Neutron URL
image   -> Glance URL
volume  -> Cinder URL
```

# Part 23 — Endpoint

Service endpoints can have interfaces such as:

```text
public
internal
admin-style deployment interfaces depending architecture
```

Clients discover where to send API requests.

# Part 24 — Application Credentials

Application credentials allow automation to authenticate without storing the user's main password.

Concept:

```text
User
  ↓ creates
Application Credential
  ↓
Terraform / CI / Script
```

They can be scoped/restricted according to roles and project context.

# Part 25 — Why Application Credentials Matter

Bad:

```yaml
username: ahmed
password: MyHumanPassword
```

Better:

```text
Dedicated application credential
limited project
limited role
rotatable secret
```

# Part 26 — `clouds.yaml`

A common OpenStack client configuration uses `clouds.yaml`.

Conceptual example:

```yaml
clouds:
  lab:
    auth:
      auth_url: https://identity.example/v3
      application_credential_id: APP_CRED_ID
      application_credential_secret: APP_CRED_SECRET
    region_name: RegionOne
    auth_type: v3applicationcredential
```

Do not commit real secrets to Git.

# Part 27 — Environment Authentication

Traditional shell environment can use variables such as:

```bash
export OS_AUTH_URL=https://identity.example/v3
export OS_PROJECT_NAME=lab-project
export OS_USERNAME=lab-user
export OS_PASSWORD='...'
export OS_IDENTITY_API_VERSION=3
```

Use secure secret handling in production.

# Part 28 — Test Authentication

```bash
openstack token issue
```

Expected fields include token metadata such as:

```text
project
domain
user
expiry
```

# Part 29 — Show Service Catalog

```bash
openstack catalog list
```

This helps troubleshoot missing/bad service endpoints.

# Part 30 — Nova Compute

Nova manages compute resources and VM lifecycle.

```text
API request
  ↓
Nova API
  ↓
Scheduler
  ↓
Compute Node
  ↓
Hypervisor
```

# Part 31 — Nova Components Mental Model

Conceptually:

```text
nova-api
nova-scheduler
nova-conductor
nova-compute
```

Supporting systems include:

```text
Placement
message queue
SQL database
```

# Part 32 — Nova API

Receives requests such as:

```text
create server
resize
reboot
delete
attach volume
```

It validates request context and coordinates downstream components.

# Part 33 — Nova Scheduler

Scheduler chooses a suitable compute host.

Inputs can include:

```text
available resources
Placement allocations
availability zone
host aggregates
traits
flavor requirements
policies
```

# Part 34 — Placement

Placement tracks resource providers, inventories, usages, traits, and allocations.

Concept:

```text
Compute Host
  |
Resource Provider
  |
CPU / Memory / Disk / Traits
```

# Part 35 — Allocation

When an instance consumes resources:

```text
vCPU
RAM
resource-class inventory
```

Placement records an allocation against providers.

# Part 36 — Nova Conductor

Conductor mediates database-related/orchestration operations between compute services and control plane, reducing direct DB access from compute nodes.

# Part 37 — Nova Compute

Runs on compute nodes and interacts with the hypervisor driver.

Common Linux architecture:

```text
nova-compute
   ↓
libvirt
   ↓
KVM/QEMU
   ↓
VM
```

# Part 38 — KVM in OpenStack

KVM provides hardware-assisted VM execution.

OpenStack does not replace KVM; Nova automates it.

# Part 39 — Cells Concept

Nova cells help scale/failure-isolate compute deployment.

Concept:

```text
API / Global Services
      |
  +---+---+
  |       |
Cell 1   Cell 2
 |        |
Compute  Compute
```

# Part 40 — Why Cells Matter

Large clouds can partition compute DB/message-queue domains and reduce failure blast radius while retaining common API access.

# Part 41 — Availability Zone

AZ exposes an administrative placement/failure-domain concept to users.

Example:

```text
nova AZ: zone-a
nova AZ: zone-b
```

Do not assume an AZ automatically maps to physically independent power/network unless operator designed it that way.

# Part 42 — Host Aggregate

Host aggregate groups compute hosts by operator-defined metadata.

Use cases:

```text
SSD hosts
GPU hosts
licensed hosts
site/rack groups
```

# Part 43 — Flavor

Flavor defines instance compute sizing and capabilities.

Example:

```text
lab.small
2 vCPU
4 GB RAM
20 GB root disk
```

# Part 44 — List Flavors

```bash
openstack flavor list
```

# Part 45 — Flavor Extra Specs

Extra specs can request capabilities/placement traits.

Concept:

```text
GPU
huge pages
CPU policy
NUMA
storage characteristics
```

These are advanced operator features.

# Part 46 — Image

Image is a bootable OS/appliance template managed by Glance.

```text
Ubuntu 24.x image
RHEL image
Windows image
custom appliance
```

# Part 47 — Glance

Glance provides image API/catalog metadata and integrates with configured storage backends.

```text
User
 ↓
Glance API
 ↓
Image Store
```

# Part 48 — Image Formats

Common VM image formats include:

```text
qcow2
raw
vmdk
vhd/vhdx depending support/import path
```

Format affects features/performance/compatibility.

# Part 49 — List Images

```bash
openstack image list
```

Inspect:

```bash
openstack image show IMAGE_NAME
```

# Part 50 — Upload Image

Authorized lab example:

```bash
openstack image create ubuntu-lab \
  --file ubuntu.qcow2 \
  --disk-format qcow2 \
  --container-format bare \
  --private
```

Validate image source/checksum before use.

# Part 51 — Image Visibility

Concepts include:

```text
private
shared/community/public according to policy
```

Do not make untrusted custom images broadly public.

# Part 52 — Cloud Image Security

Golden images should contain:

```text
patches
cloud-init
guest tools/agents as needed
baseline hardening
```

They should not contain:

```text
private keys
production passwords
unique host identity
```

# Part 53 — Key Pair

OpenStack key pairs commonly inject an SSH public key into instances.

Create:

```bash
openstack keypair create \
  --public-key ~/.ssh/id_ed25519.pub \
  lab-key
```

Private key stays with the user.

# Part 54 — Server / Instance

OpenStack calls a virtual machine a **server** in the Compute API/CLI.

```bash
openstack server list
```

# Part 55 — Boot Server

Example:

```bash
openstack server create vm01 \
  --image ubuntu-lab \
  --flavor lab.small \
  --network lab-net \
  --key-name lab-key
```

# Part 56 — Instance Build Flow

```text
Client
 ↓
Keystone token
 ↓
Nova API
 ↓
Placement/Scheduler
 ↓
Selected Compute
 ↓
Neutron ports
 ↓
Glance image
 ↓
Cinder volume if used
 ↓
libvirt/KVM
 ↓
VM ACTIVE
```

# Part 57 — Server Status

Common lifecycle states include concepts such as:

```text
BUILD
ACTIVE
SHUTOFF
ERROR
```

Always inspect fault details if status becomes `ERROR`.

# Part 58 — Show Server

```bash
openstack server show vm01
```

Inspect:

```text
host/project metadata
addresses
flavor
image
status
fault information where exposed
```

# Part 59 — Server Actions

Examples:

```bash
openstack server stop vm01
openstack server start vm01
openstack server reboot vm01
```

Understand guest/application impact before forcing actions.

# Part 60 — Resize

Resize changes flavor/resources.

Concept:

```text
small
 ↓ resize
medium
```

It may involve migration depending cloud configuration.

# Part 61 — Metadata

Instance metadata is key/value information associated with a server.

Example:

```bash
openstack server set vm01 \
  --property environment=development
```

# Part 62 — User Data

User data injects boot-time configuration.

Example cloud-init YAML:

```yaml
#cloud-config
packages:
  - nginx
runcmd:
  - systemctl enable --now nginx
```

Launch:

```bash
openstack server create vm01 \
  --image ubuntu-lab \
  --flavor lab.small \
  --network lab-net \
  --user-data cloud-init.yaml
```

# Part 63 — cloud-init

cloud-init can configure:

```text
hostname
SSH keys
packages
users
files
commands
networking depending datasource
```

This turns VM deployment into reproducible automation.

# Part 64 — Metadata Service

Instances can retrieve metadata/user-data through OpenStack metadata mechanisms.

Concept:

```text
Instance
  ↓
Metadata Endpoint
  ↓
Nova/Neutron metadata services
```

# Part 65 — Neutron

Neutron provides network connectivity as a service.

It manages concepts such as:

```text
networks
subnets
ports
routers
security groups
floating IPs
```

# Part 66 — Neutron Network

A network is a Layer-2 connectivity domain.

```bash
openstack network create lab-net
```

# Part 67 — Subnet

Subnet defines IP addressing on a network.

```bash
openstack subnet create lab-subnet \
  --network lab-net \
  --subnet-range 192.168.10.0/24 \
  --dns-nameserver 1.1.1.1
```

Use organization-approved DNS in real environments.

# Part 68 — Port

A Neutron port represents a logical interface attachment.

```text
VM vNIC
   ↓
Neutron Port
   ↓
Network
```

It can contain:

```text
MAC
fixed IP
security groups
binding information
```

# Part 69 — List Ports

```bash
openstack port list
```

Useful when an instance has network problems.

# Part 70 — Provider Network

Provider networks map more directly to physical data-center networks.

```text
VM
 ↓
Neutron Provider Network
 ↓
Physical VLAN/Flat Network
 ↓
Existing Router
```

# Part 71 — Self-Service Network

Project users can create isolated logical networks.

```text
Project VM
  ↓
Self-Service Network
  ↓
Virtual Router
  ↓
Provider External Network
```

# Part 72 — Provider vs Self-Service

Provider:

```text
simpler direct physical connectivity
operator-controlled
```

Self-service:

```text
project-owned private networks
virtual routing
NAT/floating IP patterns
```

# Part 73 — Router

Neutron router connects subnets/networks at Layer 3.

```bash
openstack router create lab-router
```

# Part 74 — Add Subnet to Router

```bash
openstack router add subnet \
  lab-router \
  lab-subnet
```

Now the router has an interface in the self-service subnet.

# Part 75 — External Gateway

Attach router to external provider network:

```bash
openstack router set \
  lab-router \
  --external-gateway public
```

# Part 76 — Fixed IP

A VM port receives a fixed IP from its subnet.

Example:

```text
192.168.10.25
```

This remains the instance's private/project-side address.

# Part 77 — Floating IP

Floating IPv4 provides externally reachable address mapping to a fixed IP.

```text
203.0.113.25
     ↓ DNAT/SNAT
192.168.10.25
```

# Part 78 — Create Floating IP

```bash
openstack floating ip create public
```

Associate:

```bash
openstack server add floating ip \
  vm01 \
  203.0.113.25
```

Use the actual allocated address returned by your cloud.

# Part 79 — Floating IP Is Not a Security Rule

A floating IP can exist while traffic remains blocked by security-group policy.

```text
Address Reachability
+
Security Group
=
usable service
```

# Part 80 — Security Group

Security group is a stateful virtual firewall applied to ports/instances.

Example policy:

```text
Allow SSH from admin subnet
Allow HTTPS from Internet
Deny other inbound
```

# Part 81 — List Security Groups

```bash
openstack security group list
```

# Part 82 — ICMP Rule

Lab example:

```bash
openstack security group rule create \
  --protocol icmp \
  default
```

Broad rules should be narrowed in production.

# Part 83 — SSH Rule

Safer example:

```bash
openstack security group rule create \
  --protocol tcp \
  --dst-port 22 \
  --remote-ip 10.10.50.0/24 \
  default
```

# Part 84 — Security Group Statefulness

When an allowed connection is established, return traffic is permitted as part of the tracked flow according to stateful firewall behavior.

# Part 85 — Neutron DHCP

DHCP assigns:

```text
fixed IP
subnet mask
router
DNS
```

according to subnet/network configuration.

# Part 86 — Virtual Router NAT

IPv4 self-service networks commonly use source NAT for outbound access through provider networks. Floating IPs provide destination-NAT-like external access to instances.

# Part 87 — Neutron Backend

Neutron supports multiple backend technologies.

Common modern architecture may use:

```text
OVN
Open vSwitch
vendor SDN integrations
```

Do not equate Neutron itself with one implementation.

# Part 88 — Open vSwitch Concept

OVS is a programmable virtual switch.

```text
VM tap/vNIC
   ↓
OVS bridge
   ↓
Tunnel / physical NIC
```

# Part 89 — OVN Concept

OVN provides logical networking/control for OVS-based environments.

Concept:

```text
Neutron API
   ↓
OVN logical network state
   ↓
OVS datapath on nodes
```

# Part 90 — Network Namespaces Legacy/Concept

Some Neutron architectures historically used Linux network namespaces and agents for DHCP/routing. Modern OVN architectures implement functions differently.

Learn the **logical function** first:

```text
DHCP
routing
NAT
metadata
```

# Part 91 — Neutron Troubleshooting Layers

```text
Instance OS
 ↓
Port
 ↓
Security Group
 ↓
Network/Subnet
 ↓
Virtual Switch/OVN
 ↓
Router/NAT
 ↓
Provider Network
 ↓
Physical Network
```

# Part 92 — No DHCP Address

Check:

```text
port status
subnet DHCP enabled
allocation pool
backend health
compute networking
instance config
```

# Part 93 — VM Cannot Reach Internet

Check:

```text
fixed IP
default route
security group
router interface
external gateway
SNAT
provider network
physical route
```

# Part 94 — Floating IP Unreachable

Check:

```text
floating IP association
security group
router
external network
physical reachability
backend realization
```

# Part 95 — Cinder

Cinder provides block storage as a service.

```text
User
 ↓
Cinder API
 ↓
Scheduler
 ↓
Volume Service
 ↓
Storage Backend
```

# Part 96 — Volume

Volume is persistent block storage independent of instance lifecycle.

```text
Instance
  |
attach
  |
Cinder Volume
```

# Part 97 — Create Volume

```bash
openstack volume create \
  --size 20 \
  data01
```

# Part 98 — Attach Volume

```bash
openstack server add volume \
  vm01 \
  data01
```

Inside Linux guest:

```bash
lsblk
```

Then partition/format/mount only the intended new disk.

# Part 99 — Persistent Volume Lifecycle

You can:

```text
create
attach
detach
reattach to another instance
snapshot
backup
delete
```

subject to policy/backend capabilities.

# Part 100 — Volume Type

Volume types expose storage classes/capabilities.

Example:

```text
standard
ssd
replicated
encrypted
```

Operator maps types to backend capabilities.

# Part 101 — Volume Snapshot

```bash
openstack volume snapshot create \
  --volume data01 \
  data01-snap1
```

Snapshots are not automatically independent backups.

# Part 102 — Cinder Backup

Cinder can support volume-backup workflows through configured backup backends.

Concept:

```text
Volume
  ↓
Backup Service
  ↓
Independent Backup Backend
```

# Part 103 — Boot from Volume

Instead of ephemeral root disk:

```text
Glance Image
   ↓
Cinder Boot Volume
   ↓
Instance boots from persistent volume
```

# Part 104 — Ephemeral vs Persistent Storage

Ephemeral instance disk:

```text
tied more closely to instance lifecycle
```

Cinder volume:

```text
persistent block-storage resource
```

Choose based on workload recovery requirements.

# Part 105 — Storage Backend Examples

Cinder can integrate with many storage systems, conceptually including:

```text
LVM/iSCSI
Ceph RBD
enterprise SAN arrays
other drivers
```

# Part 106 — Ceph Relationship

Ceph is not OpenStack, but it is commonly integrated.

```text
Nova/Glance/Cinder
      |
     Ceph
```

Ceph can provide distributed block/object storage depending deployment.

# Part 107 — Swift

Swift provides distributed object storage.

```text
Account
  ↓
Container
  ↓
Object
```

This “container” is an object-storage namespace, not a Docker container.

# Part 108 — Object Storage Use Cases

```text
backups
archives
images
logs
large unstructured objects
```

# Part 109 — Object vs Block

Block:

```text
mounted/formatted by OS
low-level disk semantics
```

Object:

```text
API-accessed objects
key + metadata
```

# Part 110 — Horizon

Horizon is the web dashboard.

```text
Browser
  ↓
Horizon
  ↓
OpenStack APIs
```

It is a client of OpenStack services, not the cloud control plane by itself.

# Part 111 — CLI vs Horizon

Horizon:

```text
easy interactive administration
```

CLI/API:

```text
repeatable
automatable
scriptable
```

Learn both, but prefer automation for repeated operations.

# Part 112 — Heat

Heat provides orchestration using templates.

Concept:

```text
Template
  ↓
Heat
  ↓
Networks
Servers
Volumes
Security Groups
```

# Part 113 — Heat Template YAML

Conceptual example:

```yaml
heat_template_version: 2021-04-16

resources:
  web_net:
    type: OS::Neutron::Net

  web_server:
    type: OS::Nova::Server
    properties:
      name: web01
      flavor: lab.small
      image: ubuntu-lab
```

Use a template-version supported by the target cloud.

# Part 114 — Why Heat Matters

Manual:

```text
click network
click subnet
click router
click VM
```

Orchestration:

```text
declarative stack
repeatable deployment
```

# Part 115 — Octavia

Octavia provides Load Balancing as a Service.

Concept:

```text
Client
  ↓
VIP
  ↓
Load Balancer
  ↓
Listener
  ↓
Pool
  ↓
Members
```

# Part 116 — Load-Balancer Objects

Understand:

```text
Load Balancer
Listener
Pool
Member
Health Monitor
```

# Part 117 — Barbican

Barbican provides secret-management services.

Use cases:

```text
TLS certificates
keys
application secrets
```

It reduces the need to place sensitive values directly in templates/configuration.

# Part 118 — Manila

Manila provides Shared File Systems as a Service.

Concept:

```text
Project
  ↓
Share
  ↓
NFS/SMB-style backend
```

# Part 119 — Ironic

Ironic provisions bare-metal machines using OpenStack-style APIs/workflows.

```text
API
 ↓
Ironic
 ↓
BMC / PXE / provisioning network
 ↓
Physical Server
```

# Part 120 — Why Bare Metal in a Cloud?

Use cases:

```text
special hardware
high performance
GPU/accelerators
licensing
no virtualization overhead
```

# Part 121 — Designate

Designate provides DNS as a Service.

Concept:

```text
Project
  ↓
Zone
  ↓
DNS Records
```

# Part 122 — Telemetry

OpenStack ecosystems can include telemetry/metrics/event services.

Fundamental monitoring categories:

```text
API availability
service state
instance metrics
network health
storage health
capacity
logs/events
```

# Part 123 — Service Database

Many control-plane services persist state in SQL databases.

Examples conceptually:

```text
Nova DB
Neutron DB
Cinder DB
Keystone DB
```

# Part 124 — Message Queue

Services communicate asynchronously through message-queue/RPC mechanisms.

Concept:

```text
Nova API
  ↓ message
Nova Scheduler
  ↓ message
Nova Compute
```

RabbitMQ is a common deployment choice, but architecture can vary.

# Part 125 — Why DB and MQ Are Critical

If database/message queue fails:

```text
running VMs may keep running
but
new API operations can fail
```

Control-plane HA must protect these dependencies.

# Part 126 — API Request Flow

Example `openstack server create`:

```text
CLI
 ↓
Keystone token
 ↓
Nova API
 ↓
Placement/Scheduler
 ↓
Neutron Port
 ↓
Glance Image
 ↓
Compute Node
 ↓
KVM instance
```

# Part 127 — Service-to-Service Authentication

OpenStack services authenticate to each other using configured service identities/credentials/tokens.

Do not use personal administrator credentials for service daemons.

# Part 128 — Quotas

Quotas prevent one project from consuming the entire cloud.

Examples:

```text
instances
vCPUs
RAM
volumes
GB
networks
routers
floating IPs
```

# Part 129 — Check Quota

Commands vary by resource/service, but unified CLI can inspect project limits/quotas.

Concept:

```text
Project requested 21st VM
Quota = 20
→ request denied
```

# Part 130 — Multi-Tenancy

OpenStack projects isolate ownership and quota domains.

But real isolation also depends on:

```text
network security
hypervisor security
storage isolation
RBAC
operator policy
```

# Part 131 — Security Groups vs Network ACL Thinking

Security groups are port/instance-level stateful rules.

They are not identical to every public-cloud NACL concept.

Learn the actual Neutron semantics rather than importing terminology from another cloud.

# Part 132 — Least Privilege

Separate:

```text
cloud operator
project admin/manager
project member
reader/auditor
automation account
```

# Part 133 — Admin Project Is Not a Magic Security Boundary

Administrative privileges can span resources according to policy. Protect operator identities strongly with centralized identity, MFA where integrated, logging, and separate admin endpoints/workstations.

# Part 134 — SSH Key Security

OpenStack stores the public key. The private key remains with the user.

Protect:

```text
~/.ssh private keys
CI secrets
jump-host credentials
```

# Part 135 — Image Trust

A public/shared image can become a supply-chain risk.

Use:

```text
controlled image pipeline
checksums/signing where available
patching
owner
version
retirement
```

# Part 136 — Metadata/User-Data Security

Do not place long-lived secrets directly in cloud-init user data unless the deployment provides secure handling and you understand its visibility/lifecycle.

Prefer secret-management/injected short-lived credentials.

# Part 137 — Network Security

Defense in depth:

```text
Security Groups
Host/Guest Firewall
Neutron routing boundaries
Physical Firewall
IDS/IPS / micro-segmentation where integrated
```

# Part 138 — Control-Plane Network Security

Separate/restrict:

```text
API network
management network
storage network
tunnel network
provider/external network
```

Deployment-specific architecture comes in Course 42.

# Part 139 — TLS

Production OpenStack APIs should use trusted TLS.

Avoid permanently using:

```bash
--insecure
```

because it disables server-certificate verification.

# Part 140 — API Service Health

A service can be:

```text
process running
but API unhealthy
```

Health checks should verify real API requests/authentication, not only systemd state.

# Part 141 — Compute Service Health

Conceptually inspect:

```text
registered compute nodes
service heartbeat
hypervisor resource inventory
Placement synchronization
```

# Part 142 — Network Service Health

Inspect:

```text
ports
binding
backend health
routers
DHCP
external connectivity
```

# Part 143 — Storage Service Health

Inspect:

```text
Cinder services
backend capacity
volume state
attachment state
storage paths
```

# Part 144 — Instance Stuck in BUILD

Possible areas:

```text
scheduler cannot place
image download
Neutron port binding
compute service
hypervisor
volume attach
quota
```

Read server fault/event information and service logs.

# Part 145 — No Valid Host

Common scheduler failure pattern.

Check:

```text
CPU/RAM/disk capacity
Placement inventory
flavor extra specs
traits
AZ
host aggregates
quotas
```

Do not randomly restart compute services.

# Part 146 — Instance ERROR

```bash
openstack server show SERVER
```

Inspect:

```text
fault message
host/task state if visible
```

Then trace Nova/Neutron/Glance/Cinder dependencies.

# Part 147 — Image Download Failure

Check:

```text
Glance API
image status
backend storage
compute-to-Glance connectivity
certificate/authentication
space
```

# Part 148 — Port Binding Failure

Symptoms:

```text
instance cannot spawn fully
port DOWN/unbound
```

Check:

```text
compute host networking
Neutron/OVN backend
physnet mapping
bridge mappings
MTU
agent/controller health depending backend
```

# Part 149 — Security Group Troubleshooting

If ping/SSH fails:

```text
instance IP
port security group
rule direction
protocol/port
remote CIDR
guest firewall
route
```

# Part 150 — Floating IP Troubleshooting

```text
Floating IP associated?
Fixed IP reachable?
Router external gateway?
Security group?
Provider network reachable?
NAT realized?
```

# Part 151 — Volume Stuck Attaching

Check:

```text
Cinder volume status
Nova attachment
compute host
storage backend
connector/iSCSI/RBD paths
multipath
```

Do not force database-backed state changes manually.

# Part 152 — Volume Full vs Backend Full

Guest filesystem can be full while Cinder backend has space, or the storage backend can be full while guest still reports free blocks.

Always identify the layer.

# Part 153 — Keystone Authentication Failure

Check:

```text
auth URL
DNS/TLS
username/application credential
project/domain scope
clock/time
token expiry
identity service health
```

# Part 154 — 401 vs 403

Concept:

```text
401 Unauthorized
commonly authentication/token issue

403 Forbidden
identity known but policy/role denies action
```

This distinction accelerates troubleshooting.

# Part 155 — Quota Failure

Typical message indicates limit exceeded.

Correct response:

```text
remove unused resources
or
request justified quota increase
```

not bypass policy.

# Part 156 — Availability and HA

OpenStack HA is layered:

```text
API/load balancers
controller services
databases
message queues
network services
storage
compute
```

There is no single “HA checkbox” for the whole cloud.

# Part 157 — Instance HA vs Cloud HA

Cloud control plane may be highly available while an individual VM remains a single instance.

Application HA still requires:

```text
multiple instances
load balancing
data replication
health checks
```

# Part 158 — Compute Failure

If compute host fails:

```text
VMs on that host fail
```

Recovery behavior depends on cloud features/operations and application architecture. Do not assume all OpenStack clouds automatically restart every VM elsewhere.

# Part 159 — Storage Failure Domain

A volume can be highly available only if its backend is designed accordingly.

OpenStack API does not magically make an unprotected single storage server resilient.

# Part 160 — Network Failure Domain

Provider uplinks, tunnel networks, routers, switches, and SDN backend all require redundancy according to the deployment design.

# Part 161 — Backups

Protect:

```text
application data
Cinder volumes
images where required
control-plane databases/configuration
secrets/certificates
network/storage configuration
```

# Part 162 — Disaster Recovery

DR requires more than instance images:

```text
identity
network definitions
images
volumes/data
DNS
secrets
orchestration templates
external connectivity
```

# Part 163 — Infrastructure as Code

OpenStack is highly automation-friendly.

Tools can include:

```text
Heat
Terraform
Ansible
Python SDK
REST
```

Course 43 will focus specifically on OpenStack APIs.

# Part 164 — Idempotent Automation

Desired:

```text
Run deployment twice
→ same intended state
```

Avoid scripts that create duplicate networks/servers every time.

# Part 165 — Naming and Tagging

Example naming:

```text
prd-web-01
prd-app-01
prd-db-01
```

Metadata/tags can record:

```text
owner
environment
application
cost center
backup policy
```

# Part 166 — Self-Service Governance

Self-service without governance can create:

```text
VM sprawl
unused floating IPs
orphan volumes
security-group exposure
cost/capacity waste
```

Use quotas, expiry, ownership, and reporting.

# Part 167 — Operational Inventory

Daily/weekly reports should include:

```text
instances
projects
compute capacity
volumes
images
networks
floating IPs
quotas
service health
```

# Part 168 — End-to-End Packet Walk

External SSH to instance:

```text
Admin Client
   ↓
Provider Network
   ↓
Floating IP / Router NAT
   ↓
Security Group
   ↓
Neutron Port
   ↓
Virtual Network Datapath
   ↓
VM eth0
   ↓
Guest Firewall / sshd
```

# Part 169 — End-to-End Boot Walk

```text
CLI
 ↓ Keystone
Token
 ↓ Nova API
Request
 ↓ Placement
Candidates
 ↓ Scheduler
Host Selected
 ↓ Neutron
Port Created
 ↓ Glance
Image Available
 ↓ Cinder if needed
Volume Prepared
 ↓ nova-compute/libvirt/KVM
VM Spawned
 ↓ metadata/cloud-init
Guest Configured
```

# Part 170 — Troubleshooting Philosophy

When an OpenStack request fails, ask:

```text
Identity?
API?
Scheduler?
Compute?
Network?
Image?
Storage?
Quota?
Policy?
Physical infrastructure?
```

Do not restart all services before identifying the failed layer.

---

# Enhanced Deep-Study Layer — OpenStack Fundamentals

This layer preserves the uploaded material and expands it using the study sequence:

```text
Concept → Detailed Explanation → Diagram → CLI/Code → Expected Result
→ Why It Works → Production Example → Troubleshooting → Best Practice
```

The uploaded source uses **OpenStack 2026.1 “Gazpacho”** as its reference baseline. Release-specific command behavior and optional-service details should always be checked against the exact cloud you operate.


## Advanced Deep Dive 1 — OpenStack as an IaaS control system

### Concept

OpenStack coordinates compute, networking, storage, identity, and images through APIs; it does not replace the hypervisor.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **OpenStack as an IaaS control system**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack service list
openstack catalog list
openstack hypervisor list
openstack network list
openstack volume list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **OpenStack as an IaaS control system**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 2 — Control plane versus data plane

### Concept

The control plane accepts/schedules/programs desired state, while the data plane executes VM CPU, packet forwarding, and storage I/O.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Control plane versus data plane**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack compute service list
openstack server list
openstack network list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Control plane versus data plane**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 3 — Keystone identity model

### Concept

Keystone combines domains, users, groups, projects, roles, scopes, tokens, catalog entries, and endpoints into one authorization model.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Keystone identity model**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack domain list
openstack project list
openstack user list
openstack group list
openstack role list
openstack role assignment list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Keystone identity model**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 4 — Scoped tokens and service catalog

### Concept

A scoped token carries project/domain/system context and the catalog tells clients where service APIs live.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Scoped tokens and service catalog**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack token issue
openstack catalog list
openstack endpoint list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Scoped tokens and service catalog**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 5 — Application credentials

### Concept

Automation should use revocable project-scoped credentials instead of human passwords.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Application credentials**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack application credential create lab-automation
openstack application credential list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Application credentials**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 6 — clouds.yaml profiles

### Concept

A named cloud profile centralizes auth, region, endpoint interface, and TLS settings for CLI and SDK clients.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **clouds.yaml profiles**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
export OS_CLOUD=lab
openstack token issue
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **clouds.yaml profiles**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 7 — Nova architecture

### Concept

Nova API, scheduler, conductor, compute, Placement, DB, and RPC cooperate to create and operate instances.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Nova architecture**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack compute service list
openstack hypervisor list
openstack server list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Nova architecture**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 8 — Placement resource providers

### Concept

Placement tracks inventories, traits, usages, and allocations and provides scheduling candidates.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Placement resource providers**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack hypervisor list
openstack resource provider list 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Placement resource providers**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 9 — Nova scheduling constraints

### Concept

Scheduling can depend on per-host fit, traits, host aggregates, availability zones, NUMA, huge pages, and PCI devices.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Nova scheduling constraints**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack flavor show <flavor>
openstack aggregate list
openstack availability zone list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Nova scheduling constraints**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 10 — Cells v2

### Concept

Cells partition Nova compute infrastructure for scale and failure isolation; Cell0 records requests that never reached a compute cell.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Cells v2**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack compute service list
openstack server list --all-projects 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Cells v2**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 11 — KVM, QEMU, and libvirt

### Concept

nova-compute commonly controls libvirt, which manages QEMU virtual machines accelerated by KVM.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **KVM, QEMU, and libvirt**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
virsh list --all
ps -ef | grep -E 'qemu|libvirt'
ls -l /dev/kvm
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **KVM, QEMU, and libvirt**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 12 — Flavor design

### Concept

Flavors define vCPU/RAM/disk and can carry extra specs that drive specialized placement.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Flavor design**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack flavor list
openstack flavor show <flavor>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Flavor design**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 13 — Glance image lifecycle

### Concept

Glance manages image metadata and binary data; image state, format, visibility, integrity, backend capacity, and access all matter.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Glance image lifecycle**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack image list
openstack image show <image>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Glance image lifecycle**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 14 — Image provenance and hardening

### Concept

Golden images are software supply-chain artifacts and should be patched, generalized, scanned, versioned, and free of secrets.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Image provenance and hardening**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
qemu-img info ubuntu.qcow2
sha256sum ubuntu.qcow2
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Image provenance and hardening**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 15 — cloud-init and metadata

### Concept

cloud-init uses metadata/user-data to customize a generic image during first boot.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **cloud-init and metadata**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
cloud-init status --long 2>/dev/null || true
cat /var/log/cloud-init.log 2>/dev/null | tail
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **cloud-init and metadata**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 16 — Neutron object model

### Concept

Networks, subnets, ports, routers, floating IPs, security groups, and backend realization form the Neutron control model.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Neutron object model**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack network list
openstack subnet list
openstack port list
openstack router list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Neutron object model**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 17 — Provider versus self-service networks

### Concept

Provider networks map directly to operator physical connectivity; self-service networks provide project-isolated logical topology.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Provider versus self-service networks**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack network show public
openstack network show private
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Provider versus self-service networks**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 18 — Neutron port binding

### Concept

Port binding maps a logical port to the selected compute host and concrete dataplane.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Neutron port binding**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack port show <port-id>
openstack port list --server <server-id>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Neutron port binding**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 19 — Security groups

### Concept

Security groups are stateful port-level virtual firewalls and are independent from guest firewalls and physical firewalls.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Security groups**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack security group list
openstack security group rule list <sg>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Security groups**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 20 — Floating IP packet walk

### Concept

Floating IP reachability requires association, virtual routing/NAT, security groups, provider network, physical routing, and a listening guest service.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Floating IP packet walk**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack floating ip list
openstack server show <server>
openstack router show <router>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Floating IP packet walk**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 21 — OVN and OVS architecture

### Concept

Neutron intent can be translated into OVN logical state and realized through OVS on compute/gateway nodes.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **OVN and OVS architecture**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
ovs-vsctl show
ovn-nbctl show 2>/dev/null || true
ovn-sbctl show 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **OVN and OVS architecture**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 22 — DHCP and metadata services

### Concept

A VM can have basic L2 connectivity while DHCP or metadata fails, breaking automatic addressing or cloud-init.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **DHCP and metadata services**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack subnet show <subnet>
openstack port show <port>
cloud-init status --long 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **DHCP and metadata services**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 23 — Cinder architecture

### Concept

Cinder API, scheduler, volume service, and backend driver provide persistent block storage independent of guest filesystem semantics.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Cinder architecture**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack volume service list
openstack volume list
openstack volume show <volume>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Cinder architecture**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 24 — Cinder volume attachment path

### Concept

Nova and Cinder coordinate an attachment; compute-side connector logic establishes the actual iSCSI/FC/RBD/NVMe path.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Cinder volume attachment path**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack server add volume <server> <volume>
openstack volume show <volume>
lsblk
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Cinder volume attachment path**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 25 — Snapshot versus backup

### Concept

Snapshots are usually primary-backend dependent; backups target a more independent recovery resource.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Snapshot versus backup**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack volume snapshot create --volume <volume> snap1
openstack volume backup create <volume> 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Snapshot versus backup**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 26 — Ceph integration

### Concept

Ceph is a separate distributed system frequently used by Glance, Cinder, and Nova for RBD storage.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Ceph integration**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
ceph -s 2>/dev/null || true
ceph df 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Ceph integration**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 27 — Swift object storage

### Concept

Swift exposes HTTP account/container/object semantics rather than block devices.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Swift object storage**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack container list 2>/dev/null || true
openstack object list <container> 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Swift object storage**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 28 — Heat orchestration

### Concept

Heat converts declarative templates into dependency-ordered API calls and tracks stack state/events.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Heat orchestration**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack stack list 2>/dev/null || true
openstack stack event list <stack> 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Heat orchestration**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 29 — Octavia load balancing

### Concept

Octavia models load balancer, listener, pool, members, and health monitor with separate provisioning and runtime health.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Octavia load balancing**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack loadbalancer list 2>/dev/null || true
openstack loadbalancer pool list 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Octavia load balancing**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 30 — Barbican secret management

### Concept

Barbican centralizes protected secret/key material so applications do not embed sensitive payloads directly in templates.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Barbican secret management**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack secret list 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Barbican secret management**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 31 — Manila shared file systems

### Concept

Manila provides network-accessed shared filesystems and access rules, distinct from Cinder block volumes.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Manila shared file systems**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack share list 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Manila shared file systems**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 32 — Ironic bare metal

### Concept

Ironic uses BMC control, network boot, hardware inventory, and images to provision physical servers through cloud workflows.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Ironic bare metal**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack baremetal node list 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Ironic bare metal**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 33 — Designate DNS

### Concept

Designate manages DNS zones and recordsets while authoritative backends actually serve DNS.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Designate DNS**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack zone list 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Designate DNS**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 34 — SQL database dependency

### Concept

Most OpenStack services persist control-plane state in SQL, so database quorum, capacity, and latency are cloud-wide dependencies.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **SQL database dependency**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
ss -lntp | grep 3306 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **SQL database dependency**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 35 — Message queue and RPC

### Concept

RPC/message queues decouple APIs, schedulers, conductors, and workers; API acceptance does not prove asynchronous execution succeeded.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Message queue and RPC**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
ss -lntp | grep 5672 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Message queue and RPC**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 36 — Quotas versus capacity

### Concept

Project quotas control governance while physical capacity and Placement/backends determine whether a request can actually fit.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Quotas versus capacity**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack quota show 2>/dev/null || true
openstack hypervisor stats show 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Quotas versus capacity**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 37 — Availability zones and aggregates

### Concept

Availability zones are user-visible scheduling/failure domains; aggregates are operator host groupings and metadata.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Availability zones and aggregates**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack availability zone list
openstack aggregate list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Availability zones and aggregates**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 38 — Layered multi-tenancy

### Concept

Secure multi-tenancy requires RBAC, Neutron isolation, storage ownership, hypervisor hardening, and operator policy—not only projects.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Layered multi-tenancy**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack role assignment list
openstack project list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Layered multi-tenancy**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 39 — API TLS trust

### Concept

Production API clients should verify the service certificate chain and hostname rather than relying on --insecure.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **API TLS trust**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openssl s_client -connect api.example:443 -servername api.example </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **API TLS trust**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 40 — Request IDs

### Concept

OpenStack request IDs allow operators to correlate one user action across distributed service logs.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Request IDs**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack --debug server list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Request IDs**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 41 — Instance build end-to-end

### Concept

A successful server create crosses Keystone, Nova API, Placement/Scheduler, Neutron, Glance, optional Cinder, nova-compute, libvirt/KVM, and metadata.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Instance build end-to-end**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack server create vm01 ...
openstack server show vm01
openstack port list --server vm01
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Instance build end-to-end**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 42 — NoValidHost

### Concept

NoValidHost means no scheduling candidate satisfied all resource and policy constraints; it is not proof that Nova API is down.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **NoValidHost**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack compute service list
openstack hypervisor list
openstack flavor show <flavor>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **NoValidHost**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 43 — Storage failure-domain thinking

### Concept

Cinder/Glance abstractions do not make an underlying single storage node resilient; durability belongs to the backend architecture.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Storage failure-domain thinking**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack volume service list
openstack image list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Storage failure-domain thinking**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 44 — Layered OpenStack HA

### Concept

OpenStack HA spans API VIPs, controllers, DB, MQ, networking, storage, compute, and application architecture.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Layered OpenStack HA**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack service list
openstack compute service list
openstack volume service list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Layered OpenStack HA**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 45 — Application HA versus cloud HA

### Concept

A highly available control plane does not make a single application VM highly available; application redundancy still matters.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Application HA versus cloud HA**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack server list
openstack loadbalancer list 2>/dev/null || true
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Application HA versus cloud HA**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 46 — Backup and disaster recovery scope

### Concept

DR must protect configuration, DB state, secrets/certificates, images, volumes/data, network definitions, DNS, and orchestration.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Backup and disaster recovery scope**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack image list
openstack volume list
openstack network list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Backup and disaster recovery scope**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 47 — Horizon as an API client

### Concept

Horizon is a UI over APIs; a Horizon outage can coexist with a healthy cloud.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Horizon as an API client**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack token issue
openstack server list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Horizon as an API client**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 48 — Telemetry and observability

### Concept

Operators need API SLOs, logs, request IDs, resource metrics, capacity, backend health, and synthetic user transactions.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Telemetry and observability**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack --debug server list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Telemetry and observability**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 49 — Naming and metadata governance

### Concept

Owner, environment, application, backup, and expiry metadata make self-service cloud resources governable.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Naming and metadata governance**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack server set vm01 --property owner=team-a --property environment=dev
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Naming and metadata governance**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 50 — Orphan resource lifecycle

### Concept

Volumes, floating IPs, ports, snapshots, and security groups can outlive a VM and consume quota/capacity.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Orphan resource lifecycle**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack volume list
openstack floating ip list
openstack port list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Orphan resource lifecycle**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 51 — OpenStack and Kubernetes layering

### Concept

Kubernetes can run on OpenStack and consume Cinder volumes, Octavia load balancers, and OpenStack VM/bare-metal nodes.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **OpenStack and Kubernetes layering**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack server list
openstack volume list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **OpenStack and Kubernetes layering**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 52 — External network IPAM

### Concept

Floating/provider address pools are finite and must align with enterprise IPAM and physical routing.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **External network IPAM**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack floating ip list
openstack subnet show <external-subnet>
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **External network IPAM**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


## Advanced Deep Dive 53 — Service catalog hygiene

### Concept

Stale endpoints or wrong regions/interfaces break clients even when service containers are healthy.

This topic should be understood as part of a dependency chain, not as an isolated definition. In OpenStack, a user-visible resource is normally the result of several cooperating services, persistent state, and a real compute/network/storage implementation.

### Architecture / Mental Model

```text
User / CLI / SDK
        |
    Keystone
        |
   Service API
        |
 Control service
  /     |      \
DB     MQ    Scheduler/Worker
               |
        Compute/Network/Storage
               |
          Final Resource
```

For **Service catalog hygiene**, ask four questions:

```text
1. Which service owns the API object?
2. Which persistent/control-plane dependency stores or moves the state?
3. Which node/backend realizes the data plane?
4. What evidence proves the final resource actually works?
```

### Commands / Code

```bash
openstack endpoint list
openstack catalog list
```

### Expected Result

The command output should match the intended project, region, object IDs, and service state. A resource should not be considered healthy only because it exists in an API list; verify the downstream state or actual workload behavior appropriate to the topic.

### Why It Works

OpenStack uses API-driven desired state. The control plane validates and records intent, then schedulers/workers/backends realize that intent on compute, networking, or storage infrastructure. This separation enables scale, but it also means failures can occur after the initial API request succeeds.

### Real Production Example

A platform team may see a server object in `BUILD`, a Neutron port already allocated, and an image marked `active`. The correct response is to identify the next missing stage rather than delete and recreate everything. The same dependency-based reasoning applies to **Service catalog hygiene**.

### Troubleshooting Workflow

```text
Symptom
  ↓
Identify owning service
  ↓
Check token/scope/catalog endpoint
  ↓
Check resource state + request ID
  ↓
Check DB/MQ/scheduler or controller dependency
  ↓
Check compute/network/storage realization
  ↓
Check physical/backend dependency
  ↓
Correct the smallest failed layer
  ↓
Repeat the original user transaction
```

### Security / Reliability Implication

Cloud abstractions concentrate privilege and blast radius. Use project-scoped identities, least privilege, trusted TLS, controlled images, explicit security groups, protected management networks, and independent backups.

### Best Practices

- Record UUIDs, not only names.
- Capture request IDs on failures.
- Keep human and automation credentials separate.
- Distinguish quota from physical capacity.
- Validate API state and data-plane behavior.
- Avoid database edits and broad service restarts as first-line troubleshooting.
- Document ownership and lifecycle metadata.

---


# Enhanced OpenStack Fundamentals Practical Labs

## Enhanced Lab 1 — OpenStack as an IaaS control system

**Objective:** prove the architecture and failure boundaries of **OpenStack as an IaaS control system** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack service list
openstack catalog list
openstack hypervisor list
openstack network list
openstack volume list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 2 — Control plane versus data plane

**Objective:** prove the architecture and failure boundaries of **Control plane versus data plane** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack compute service list
openstack server list
openstack network list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 3 — Keystone identity model

**Objective:** prove the architecture and failure boundaries of **Keystone identity model** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack domain list
openstack project list
openstack user list
openstack group list
openstack role list
openstack role assignment list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 4 — Scoped tokens and service catalog

**Objective:** prove the architecture and failure boundaries of **Scoped tokens and service catalog** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack token issue
openstack catalog list
openstack endpoint list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 5 — Application credentials

**Objective:** prove the architecture and failure boundaries of **Application credentials** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack application credential create lab-automation
openstack application credential list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 6 — clouds.yaml profiles

**Objective:** prove the architecture and failure boundaries of **clouds.yaml profiles** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
export OS_CLOUD=lab
openstack token issue
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 7 — Nova architecture

**Objective:** prove the architecture and failure boundaries of **Nova architecture** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack compute service list
openstack hypervisor list
openstack server list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 8 — Placement resource providers

**Objective:** prove the architecture and failure boundaries of **Placement resource providers** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack hypervisor list
openstack resource provider list 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 9 — Nova scheduling constraints

**Objective:** prove the architecture and failure boundaries of **Nova scheduling constraints** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack flavor show <flavor>
openstack aggregate list
openstack availability zone list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 10 — Cells v2

**Objective:** prove the architecture and failure boundaries of **Cells v2** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack compute service list
openstack server list --all-projects 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 11 — KVM, QEMU, and libvirt

**Objective:** prove the architecture and failure boundaries of **KVM, QEMU, and libvirt** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
virsh list --all
ps -ef | grep -E 'qemu|libvirt'
ls -l /dev/kvm
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 12 — Flavor design

**Objective:** prove the architecture and failure boundaries of **Flavor design** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack flavor list
openstack flavor show <flavor>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 13 — Glance image lifecycle

**Objective:** prove the architecture and failure boundaries of **Glance image lifecycle** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack image list
openstack image show <image>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 14 — Image provenance and hardening

**Objective:** prove the architecture and failure boundaries of **Image provenance and hardening** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
qemu-img info ubuntu.qcow2
sha256sum ubuntu.qcow2
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 15 — cloud-init and metadata

**Objective:** prove the architecture and failure boundaries of **cloud-init and metadata** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
cloud-init status --long 2>/dev/null || true
cat /var/log/cloud-init.log 2>/dev/null | tail
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 16 — Neutron object model

**Objective:** prove the architecture and failure boundaries of **Neutron object model** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack network list
openstack subnet list
openstack port list
openstack router list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 17 — Provider versus self-service networks

**Objective:** prove the architecture and failure boundaries of **Provider versus self-service networks** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack network show public
openstack network show private
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 18 — Neutron port binding

**Objective:** prove the architecture and failure boundaries of **Neutron port binding** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack port show <port-id>
openstack port list --server <server-id>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 19 — Security groups

**Objective:** prove the architecture and failure boundaries of **Security groups** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack security group list
openstack security group rule list <sg>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 20 — Floating IP packet walk

**Objective:** prove the architecture and failure boundaries of **Floating IP packet walk** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack floating ip list
openstack server show <server>
openstack router show <router>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 21 — OVN and OVS architecture

**Objective:** prove the architecture and failure boundaries of **OVN and OVS architecture** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
ovs-vsctl show
ovn-nbctl show 2>/dev/null || true
ovn-sbctl show 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 22 — DHCP and metadata services

**Objective:** prove the architecture and failure boundaries of **DHCP and metadata services** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack subnet show <subnet>
openstack port show <port>
cloud-init status --long 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 23 — Cinder architecture

**Objective:** prove the architecture and failure boundaries of **Cinder architecture** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack volume service list
openstack volume list
openstack volume show <volume>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 24 — Cinder volume attachment path

**Objective:** prove the architecture and failure boundaries of **Cinder volume attachment path** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack server add volume <server> <volume>
openstack volume show <volume>
lsblk
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 25 — Snapshot versus backup

**Objective:** prove the architecture and failure boundaries of **Snapshot versus backup** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack volume snapshot create --volume <volume> snap1
openstack volume backup create <volume> 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 26 — Ceph integration

**Objective:** prove the architecture and failure boundaries of **Ceph integration** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
ceph -s 2>/dev/null || true
ceph df 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 27 — Swift object storage

**Objective:** prove the architecture and failure boundaries of **Swift object storage** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack container list 2>/dev/null || true
openstack object list <container> 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 28 — Heat orchestration

**Objective:** prove the architecture and failure boundaries of **Heat orchestration** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack stack list 2>/dev/null || true
openstack stack event list <stack> 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 29 — Octavia load balancing

**Objective:** prove the architecture and failure boundaries of **Octavia load balancing** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack loadbalancer list 2>/dev/null || true
openstack loadbalancer pool list 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 30 — Barbican secret management

**Objective:** prove the architecture and failure boundaries of **Barbican secret management** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack secret list 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 31 — Manila shared file systems

**Objective:** prove the architecture and failure boundaries of **Manila shared file systems** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack share list 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 32 — Ironic bare metal

**Objective:** prove the architecture and failure boundaries of **Ironic bare metal** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack baremetal node list 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 33 — Designate DNS

**Objective:** prove the architecture and failure boundaries of **Designate DNS** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack zone list 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 34 — SQL database dependency

**Objective:** prove the architecture and failure boundaries of **SQL database dependency** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
ss -lntp | grep 3306 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 35 — Message queue and RPC

**Objective:** prove the architecture and failure boundaries of **Message queue and RPC** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
ss -lntp | grep 5672 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 36 — Quotas versus capacity

**Objective:** prove the architecture and failure boundaries of **Quotas versus capacity** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack quota show 2>/dev/null || true
openstack hypervisor stats show 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 37 — Availability zones and aggregates

**Objective:** prove the architecture and failure boundaries of **Availability zones and aggregates** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack availability zone list
openstack aggregate list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 38 — Layered multi-tenancy

**Objective:** prove the architecture and failure boundaries of **Layered multi-tenancy** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack role assignment list
openstack project list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 39 — API TLS trust

**Objective:** prove the architecture and failure boundaries of **API TLS trust** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openssl s_client -connect api.example:443 -servername api.example </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 40 — Request IDs

**Objective:** prove the architecture and failure boundaries of **Request IDs** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack --debug server list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 41 — Instance build end-to-end

**Objective:** prove the architecture and failure boundaries of **Instance build end-to-end** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack server create vm01 ...
openstack server show vm01
openstack port list --server vm01
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 42 — NoValidHost

**Objective:** prove the architecture and failure boundaries of **NoValidHost** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack compute service list
openstack hypervisor list
openstack flavor show <flavor>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 43 — Storage failure-domain thinking

**Objective:** prove the architecture and failure boundaries of **Storage failure-domain thinking** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack volume service list
openstack image list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 44 — Layered OpenStack HA

**Objective:** prove the architecture and failure boundaries of **Layered OpenStack HA** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack service list
openstack compute service list
openstack volume service list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 45 — Application HA versus cloud HA

**Objective:** prove the architecture and failure boundaries of **Application HA versus cloud HA** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack server list
openstack loadbalancer list 2>/dev/null || true
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 46 — Backup and disaster recovery scope

**Objective:** prove the architecture and failure boundaries of **Backup and disaster recovery scope** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack image list
openstack volume list
openstack network list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 47 — Horizon as an API client

**Objective:** prove the architecture and failure boundaries of **Horizon as an API client** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack token issue
openstack server list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 48 — Telemetry and observability

**Objective:** prove the architecture and failure boundaries of **Telemetry and observability** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack --debug server list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 49 — Naming and metadata governance

**Objective:** prove the architecture and failure boundaries of **Naming and metadata governance** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack server set vm01 --property owner=team-a --property environment=dev
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 50 — Orphan resource lifecycle

**Objective:** prove the architecture and failure boundaries of **Orphan resource lifecycle** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack volume list
openstack floating ip list
openstack port list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 51 — OpenStack and Kubernetes layering

**Objective:** prove the architecture and failure boundaries of **OpenStack and Kubernetes layering** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack server list
openstack volume list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 52 — External network IPAM

**Objective:** prove the architecture and failure boundaries of **External network IPAM** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack floating ip list
openstack subnet show <external-subnet>
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---

## Enhanced Lab 53 — Service catalog hygiene

**Objective:** prove the architecture and failure boundaries of **Service catalog hygiene** using an authorized lab.

### Procedure
1. Record `OS_CLOUD`, region, project, and current token scope.
2. Draw the expected service dependency path before running commands.
3. Capture a read-only before-state.
4. Run the following commands and save the output with timestamps.
5. Record resource UUIDs and request IDs where available.
6. Verify the final API state.
7. Verify a real data-plane/application result when the topic has one.
8. If safe in a disposable lab, break one dependency only and repeat the test.
9. Restore the dependency and prove recovery.
10. Write: Symptom → Evidence → Root Cause → Correction → Verification.

```bash
openstack endpoint list
openstack catalog list
```

**Lab safety:** never use production credentials, manually edit OpenStack databases, disable cloud-wide security, or delete resources you do not own.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Map OpenStack Services

Draw:

```text
Keystone
Nova
Placement
Glance
Neutron
Cinder
Horizon
```

For each, write one API request it owns.

### Lab 2 — Configure CLI

Create a lab `clouds.yaml` using an application credential if supported.

Test:

```bash
openstack token issue
openstack catalog list
```

### Lab 3 — Identity Inventory

Run:

```bash
openstack project list
openstack user list
openstack role list
```

If your account cannot see all users/projects, document RBAC rather than requesting unnecessary admin access.

### Lab 4 — Compute Inventory

```bash
openstack hypervisor list
openstack compute service list
openstack flavor list
```

Draw compute-resource path.

### Lab 5 — Images

```bash
openstack image list
openstack image show ubuntu-lab
```

Document image format, size, visibility, properties, owner.

### Lab 6 — Create Key Pair

```bash
openstack keypair create \
  --public-key ~/.ssh/id_ed25519.pub \
  lab-key
```

Verify the private key never leaves your workstation.

### Lab 7 — Create Network and Subnet

```bash
openstack network create lab-net

openstack subnet create lab-subnet \
  --network lab-net \
  --subnet-range 192.168.10.0/24
```

### Lab 8 — Create Router

```bash
openstack router create lab-router
openstack router add subnet lab-router lab-subnet
openstack router set lab-router --external-gateway public
```

Draw the resulting topology.

### Lab 9 — Security Group

Create a dedicated group:

```bash
openstack security group create lab-web-sg
```

Allow SSH only from your admin subnet and HTTPS as required.

### Lab 10 — Create Server

```bash
openstack server create lab-vm01 \
  --image ubuntu-lab \
  --flavor lab.small \
  --network lab-net \
  --security-group lab-web-sg \
  --key-name lab-key
```

Watch status:

```bash
openstack server list
```

### Lab 11 — Inspect Server

```bash
openstack server show lab-vm01
openstack port list --server lab-vm01
```

Map server → port → network → subnet.

### Lab 12 — Floating IP

Allocate from external network, associate to lab VM, then test only the services allowed by the security group.

### Lab 13 — cloud-init

Create:

```yaml
#cloud-config
packages:
  - nginx
runcmd:
  - systemctl enable --now nginx
```

Launch a new VM using `--user-data` and verify web service.

### Lab 14 — Create Cinder Volume

```bash
openstack volume create --size 5 data01
openstack server add volume lab-vm01 data01
```

Inside guest:

```bash
lsblk
```

Format/mount only the correct new disk.

### Lab 15 — Volume Snapshot

Create a test file on the data volume, sync filesystem/app as appropriate, create snapshot, and explain consistency limits.

### Lab 16 — Boot From Volume Design

Compare:

```text
image-backed ephemeral root
vs
Cinder boot volume
```

for database, web, and disposable worker workloads.

### Lab 17 — Provider vs Self-Service Network

Draw packet paths for both models and identify where routing/NAT occurs.

### Lab 18 — Security Troubleshooting

Intentionally omit an SSH security-group rule in lab. Prove:

```text
floating IP exists
ping/port may fail by policy
```

Then add the correct narrow rule.

### Lab 19 — Quota Exercise

Inventory project resource usage and identify what would happen if instance/vCPU/floating-IP quota were reached.

### Lab 20 — Flavor/Scheduling Exercise

Create or analyze a flavor requiring more RAM than any compute host can provide. Predict and explain scheduler failure.

### Lab 21 — Heat Template

Write a template defining:

```text
network
subnet
security group
server
```

Validate syntax against your cloud before deployment.

### Lab 22 — Application Credential

Create a project-scoped application credential for a lab automation task. Use it from a second `clouds.yaml` entry and verify limited scope.

### Lab 23 — API Flow Diagram

For `openstack server create`, draw every service interaction:

```text
Keystone
Nova
Placement
Neutron
Glance
Cinder optional
Compute/KVM
```

### Lab 24 — Control-Plane Dependency Table

Create:

```text
Service | SQL DB | MQ | API | Worker/Agent | External Dependency
```

for Keystone, Nova, Neutron, Glance, and Cinder.

### Lab 25 — Network Troubleshooting

Analyze:

```text
VM has fixed IP
cannot reach Internet
```

Check guest route, security group, router, external gateway, NAT, provider network, and physical network.

### Lab 26 — Instance Build Failure

Simulate/analyze:

```text
NoValidHost
bad image
port binding failure
quota exceeded
```

For each, identify the responsible service/layer.

### Lab 27 — Volume Failure

Analyze a volume stuck in `attaching` and create a safe diagnostic checklist without manually modifying OpenStack databases.

### Lab 28 — Observability Dashboard

Design a dashboard for:

```text
API availability
compute service state
capacity
instance errors
network backend
volume backend
DB/MQ
quotas
```

### Lab 29 — Security Review

Audit:

```text
admin roles
application credentials
public images
open security groups
floating IPs
stale key pairs
TLS
metadata/user-data secrets
```

### Lab 30 — Troubleshooting Challenge

Analyze 15 scenarios:

1. Keystone authentication fails.
2. User receives 403.
3. Nova service down.
4. NoValidHost.
5. Instance stuck BUILD.
6. Image download fails.
7. Neutron port unbound.
8. DHCP fails.
9. Floating IP unreachable.
10. Security group blocks traffic.
11. Cinder volume stuck attaching.
12. Storage backend full.
13. Quota exceeded.
14. Controller API unavailable.
15. Compute host fails.

For every case:

```text
Symptom
Service
Layer
Evidence
Root Cause
Correction
Verification
Prevention
```

---

## 6. Mini Project

# Mini Project — OpenStack Private Cloud Application Environment

Design a private-cloud environment for a manufacturing company.

### Projects

```text
Production
Development
Infrastructure
```

### Core Services

```text
Keystone
Nova
Placement
Glance
Neutron
Cinder
Horizon
Heat
```

Optional design:

```text
Octavia
Barbican
Manila
Designate
```

### Production Application

```text
                   External Network
                         |
                    Floating IP
                         |
                    Load Balancer
                         |
                  +------+------+ 
                  |             |
                WEB01         WEB02
                  \             /
                   \           /
                    APP01 / APP02
                         |
                       DB01
                         |
                    Cinder Volume
```

### Network Design

Create:

```text
web-net  10.20.10.0/24
app-net  10.20.20.0/24
db-net   10.20.30.0/24
```

Router connects only required networks to external provider network.

### Security Groups

```text
WEB-SG:
HTTPS from approved external ranges
SSH only from bastion/admin

APP-SG:
application port only from WEB-SG/workload addresses

DB-SG:
database port only from APP tier
```

### Images

Build a controlled Ubuntu/RHEL-style cloud image pipeline containing:

```text
cloud-init
patch baseline
monitoring agent
security baseline
no secrets
```

### Storage

Use:

```text
Cinder persistent DB/data volumes
image/ephemeral storage for disposable web instances where appropriate
```

### Automation

Create a Heat/Terraform design for repeatable provisioning.

### Identity

Define:

```text
Production Operators
Developers
Auditors
Automation Application Credential
```

Use project-scoped least privilege.

### Quotas

Define limits for:

```text
instances
vCPU
RAM
volumes
storage GB
floating IPs
networks
routers
```

### HA

Design:

```text
redundant controllers
DB/MQ HA
multiple compute hosts
redundant external networking
resilient storage
application-level redundancy
```

### Deliverables

```text
README.md
ARCHITECTURE.md
SERVICES.md
IDENTITY_RBAC.md
COMPUTE.md
PLACEMENT_SCHEDULING.md
IMAGES.md
NETWORK.md
SECURITY_GROUPS.md
STORAGE.md
QUOTAS.md
HA.md
BACKUP_DR.md
HEAT_TEMPLATE.yaml
CLOUD_INIT.yaml
MONITORING.md
RUNBOOKS/
```

### Required Runbooks

```text
KEYSTONE_AUTH_FAILURE.md
NO_VALID_HOST.md
INSTANCE_BUILD_ERROR.md
NETWORK_FAILURE.md
FLOATING_IP.md
VOLUME_ATTACH.md
CONTROL_PLANE_OUTAGE.md
COMPUTE_FAILURE.md
```

---


# Expanded Capstone — Enterprise OpenStack Private Cloud Design

Design a private cloud supporting Production, Development, Infrastructure, and Security projects.

```text
Users / CI
    |
Keystone / API VIP
    |
+---+------+-------+-------+
| Nova     |Neutron|Cinder |Glance
|          |       |       |
Placement  OVN/OVS Storage Images
|          |       |
KVM        Fabric  Ceph/SAN
```

Create these deliverables:

```text
README.md
SERVICE_MAP.md
IDENTITY_RBAC.md
COMPUTE_PLACEMENT.md
IMAGE_PIPELINE.md
NETWORK_ARCHITECTURE.md
SECURITY_GROUPS.md
STORAGE_ARCHITECTURE.md
QUOTAS.md
HA.md
BACKUP_DR.md
OBSERVABILITY.md
CAPACITY.md
GOVERNANCE.md
RUNBOOKS/
```

Your design must explicitly cover:

- project/domain/role/application-credential model;
- general, high-memory, and accelerator compute pools;
- Placement traits, aggregates, and availability zones;
- controlled golden-image pipeline;
- provider and self-service networks;
- port binding, floating IP, security groups, DHCP, metadata, OVN/OVS;
- Cinder, Ceph/SAN, snapshots versus backups, Manila and Swift decision points;
- API/DB/MQ failure;
- compute, network, and storage failure domains;
- project quotas and physical capacity;
- cloud HA versus application HA;
- complete DR restore order;
- orphan-resource governance and ownership metadata.

For every critical flow create a packet/request walk and a troubleshooting runbook.


## 7. Recommended Resources

This Markdown file is intentionally designed to teach the required fundamentals without requiring an external tutorial.

For release-specific implementation in Courses 42 and 43, use documentation matching the installed release.

Current official documentation families relevant to this course include:

```text
OpenStack 2026.1 Gazpacho Documentation
Keystone Identity
Nova Compute
Placement
Neutron Networking
Glance Images
Cinder Block Storage
Swift Object Storage
Horizon Dashboard
Heat Orchestration
Octavia
Barbican
Manila
Ironic
Designate
OpenStackClient
```

Current-version facts reflected here:

- OpenStack 2026.1 “Gazpacho” is the current maintained release used as this course baseline.
- OpenStack is an API-driven cloud infrastructure platform controlling pools of compute, storage, and networking resources.
- Neutron provides network connectivity as a service.
- Keystone domains contain projects/users/groups and roles are assigned at project/domain scope.
- Keystone application credentials allow applications to authenticate without using a user's primary password.
- IPv4 self-service networks commonly reach provider networks through virtual routers/NAT; floating IPs provide externally reachable mappings.

---

## 8. Certification Relevance

This course supports roles such as:

```text
OpenStack Administrator
Private Cloud Engineer
Cloud Infrastructure Engineer
Linux Engineer
Virtualization Engineer
Network/Cloud Engineer
Platform Engineer
SRE
```

It is the direct prerequisite for:

```text
42. OpenStack Deployment and Operation
43. OpenStack APIs
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** OpenStack treated as a hypervisor.  
  **Best practice:** understand Nova orchestrates hypervisors such as KVM.

- **Mistake:** Horizon treated as the control plane.  
  **Best practice:** Horizon is a client of service APIs.

- **Mistake:** Human password placed in automation.  
  **Best practice:** use project-scoped application credentials/secrets.

- **Mistake:** Project assumed to provide all security isolation automatically.  
  **Best practice:** combine RBAC, networking, security groups, storage isolation, and hypervisor hardening.

- **Mistake:** Public image trusted because it exists in Glance.  
  **Best practice:** use controlled image provenance and patching.

- **Mistake:** Floating IP treated as firewall permission.  
  **Best practice:** configure security groups separately.

- **Mistake:** `0.0.0.0/0` SSH rules everywhere.  
  **Best practice:** restrict administration to bastion/admin networks.

- **Mistake:** VM in `ERROR` causes random service restarts.  
  **Best practice:** inspect fault and trace service dependency.

- **Mistake:** `NoValidHost` assumed to mean nova-compute is broken.  
  **Best practice:** inspect Placement capacity, flavor requirements, AZ, aggregates, and traits.

- **Mistake:** Cinder volume equals guest filesystem.  
  **Best practice:** separate cloud block-resource state from filesystem state inside the VM.

- **Mistake:** Snapshot assumed to be backup.  
  **Best practice:** maintain independent backup/recovery policy.

- **Mistake:** Single SQL/MQ/controller considered private-cloud HA.  
  **Best practice:** protect every control-plane dependency.

- **Mistake:** OpenStack HA assumed to make an individual app highly available.  
  **Best practice:** design application-level redundancy too.

- **Mistake:** Self-service without quotas/ownership.  
  **Best practice:** govern lifecycle, quota, tagging, expiry, and capacity.

- **Mistake:** Use `--insecure` permanently.  
  **Best practice:** use trusted TLS certificates.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is OpenStack?
**Short answer:** Open-source IaaS platform controlling pools of compute, networking, storage, images, and identity through APIs.

### Q2. Is OpenStack a hypervisor?
**Short answer:** No; Nova commonly orchestrates hypervisors such as KVM/libvirt.

### Q3. What does Keystone provide?
**Short answer:** Identity, authentication context, roles/scoping, tokens, service catalog, and endpoints.

### Q4. What is a domain?
**Short answer:** High-level administrative container for identity resources such as projects/users/groups.

### Q5. What is a project?
**Short answer:** Tenant/resource-ownership and quota scope.

### Q6. What is a role assignment?
**Short answer:** Identity plus role plus scope.

### Q7. What is an application credential?
**Short answer:** Project-scoped credential allowing applications to authenticate without using the user's main password.

### Q8. What is Nova?
**Short answer:** OpenStack Compute service managing VM lifecycle.

### Q9. What does Placement do?
**Short answer:** Tracks resource-provider inventories, traits, usages, and allocations for scheduling.

### Q10. What does Nova Scheduler do?
**Short answer:** Chooses a suitable compute host for a request.

### Q11. What is a flavor?
**Short answer:** Compute sizing/capability definition such as vCPU, RAM, disk, and extra specs.

### Q12. What is Glance?
**Short answer:** Image service/catalog.

### Q13. What is Neutron?
**Short answer:** Network connectivity as a service.

### Q14. Provider vs self-service network?
**Short answer:** Provider maps to operator/physical connectivity; self-service is project-created isolated networking typically using virtual routers/NAT.

### Q15. What is a Neutron port?
**Short answer:** Logical interface attachment containing fixed IP, MAC, security groups, and binding data.

### Q16. What is a floating IP?
**Short answer:** Externally reachable IPv4 mapping associated with an instance's fixed IP through virtual routing/NAT.

### Q17. What is a security group?
**Short answer:** Stateful virtual firewall policy applied to ports/instances.

### Q18. What is Cinder?
**Short answer:** Block Storage as a Service.

### Q19. What is Swift?
**Short answer:** Distributed Object Storage service.

### Q20. What is Horizon?
**Short answer:** Web dashboard/client for OpenStack APIs.

### Q21. What is Heat?
**Short answer:** Orchestration service for declarative infrastructure templates.

### Q22. What is Octavia?
**Short answer:** Load Balancing as a Service.

### Q23. What is Barbican?
**Short answer:** Secrets/key-management service.

### Q24. What is Manila?
**Short answer:** Shared File Systems as a Service.

### Q25. What is Ironic?
**Short answer:** Bare-metal provisioning service.

### Q26. What is cloud-init used for?
**Short answer:** First-boot instance configuration using metadata/user data.

### Q27. What is a service catalog?
**Short answer:** Keystone-provided list of service APIs/endpoints.

### Q28. Why are quotas needed?
**Short answer:** To limit project consumption and prevent resource monopolization.

### Q29. What does `NoValidHost` normally indicate?
**Short answer:** Scheduler could not find a compute host satisfying capacity/placement requirements.

### Q30. 401 vs 403?
**Short answer:** 401 generally indicates authentication/token issue; 403 means authenticated identity lacks authorization under policy.

### Q31. Why can running VMs survive a control-plane outage?
**Short answer:** VM execution/dataplane runs on compute/hypervisor nodes independently of some API/controller functions.

### Q32. Does OpenStack HA automatically make an application HA?
**Short answer:** No; application redundancy, data replication, and health-aware traffic handling are still needed.

### Q33. What is the best troubleshooting approach?
**Short answer:** Identify the responsible service/layer and trace Identity → API → scheduling → compute/network/image/storage rather than restarting everything.

---

# Expanded Self-Assessment Bank

### Q1. Why is OpenStack not a hypervisor?
**Answer:** It orchestrates hypervisors such as KVM through Nova.

### Q2. What is the control plane?
**Answer:** APIs, schedulers, databases, message queues, and controller processes that manage desired state.

### Q3. What is the data plane?
**Answer:** Running VM execution, network forwarding, and storage I/O.

### Q4. What does Keystone provide?
**Answer:** Identity, scopes, roles, tokens, catalog, and endpoints.

### Q5. What is the fundamental authorization model?
**Answer:** Identity + role + scope.

### Q6. Why use application credentials?
**Answer:** They separate automation secrets from human passwords and can be revoked independently.

### Q7. What is Placement?
**Answer:** Resource-provider inventory, traits, usage, and allocations used for scheduling.

### Q8. What does NoValidHost mean?
**Answer:** No eligible compute provider satisfies all requested constraints.

### Q9. What is Cells v2?
**Answer:** Nova scale/failure-isolation architecture that partitions compute.

### Q10. What is a flavor?
**Answer:** A standardized compute resource/capability request.

### Q11. What is Glance?
**Answer:** Image metadata and image-data service.

### Q12. Why are images a supply-chain concern?
**Answer:** All instances launched from them inherit their content.

### Q13. What does cloud-init do?
**Answer:** First-boot configuration from metadata and user data.

### Q14. What is a Neutron port?
**Answer:** Logical interface with MAC, fixed IP, SGs, and binding information.

### Q15. Provider vs self-service network?
**Answer:** Physical/operator connectivity versus project-isolated logical networks.

### Q16. What is port binding?
**Answer:** Mapping a logical Neutron port to a concrete host/datapath.

### Q17. What are security groups?
**Answer:** Stateful virtual firewall rules associated with ports.

### Q18. Why can floating IP be unreachable despite association?
**Answer:** Routing/NAT, SG, provider network, physical route, or guest service may fail.

### Q19. What is OVN?
**Answer:** Logical network/control system often used by Neutron.

### Q20. What is Cinder?
**Answer:** Block Storage as a Service.

### Q21. What happens during volume attachment?
**Answer:** Cinder/Nova coordinate state and the compute establishes the backend storage path.

### Q22. Snapshot vs backup?
**Answer:** Snapshot is usually primary-backend dependent; backup targets separate recovery storage.

### Q23. What is Ceph?
**Answer:** A separate distributed storage system commonly integrated with OpenStack.

### Q24. What is Swift?
**Answer:** Object Storage service.

### Q25. What is Heat?
**Answer:** Declarative orchestration service.

### Q26. What is Octavia?
**Answer:** Load Balancing as a Service.

### Q27. What is Barbican?
**Answer:** Secret/key management service.

### Q28. What is Manila?
**Answer:** Shared Filesystems as a Service.

### Q29. What is Ironic?
**Answer:** Bare-metal provisioning service.

### Q30. What is Designate?
**Answer:** DNS as a Service.

### Q31. Why is SQL critical?
**Answer:** Most services persist control state there.

### Q32. Why is RabbitMQ critical?
**Answer:** It carries asynchronous RPC/messages between services.

### Q33. Quota vs capacity?
**Answer:** Quota is governance; capacity is actual resources.

### Q34. AZ vs host aggregate?
**Answer:** AZ is user-facing placement domain; aggregate is operator grouping/metadata.

### Q35. Does project isolation alone guarantee multi-tenancy security?
**Answer:** No; network, storage, hypervisor, RBAC, and operator controls also matter.

### Q36. Why avoid --insecure?
**Answer:** It disables certificate verification and endpoint identity protection.

### Q37. Why capture request IDs?
**Answer:** They correlate one operation across distributed logs.

### Q38. What are the main server-create dependencies?
**Answer:** Keystone, Nova, Placement, Neutron, Glance, optional Cinder, nova-compute/libvirt/KVM.

### Q39. Why can APIs be healthy while VM I/O is slow?
**Answer:** Control-plane and storage/network data-plane health are different.

### Q40. Does OpenStack provide one HA switch?
**Answer:** No; HA is layered across control, data plane, storage, network, and applications.

### Q41. Cloud HA vs application HA?
**Answer:** Infrastructure availability does not replace app redundancy/data replication.

### Q42. What must DR protect?
**Answer:** Control state/config/secrets plus tenant images, volumes/data, networking, DNS, and automation.

### Q43. Why is Horizon not the cloud control plane?
**Answer:** It is a web client using the same APIs.

### Q44. Why are orphan resources important?
**Answer:** They waste capacity/quota and can become security/governance liabilities.

### Q45. Why is external IPAM important?
**Answer:** Floating/provider pools must not collide with enterprise physical addressing.

### Q46. What is the core troubleshooting method?
**Answer:** Identify the owning service, request stage, control dependency, and final dataplane.


## Completion Checklist

- [ ] I understand what OpenStack is and is not.
- [ ] I understand the modular service architecture.
- [ ] I understand Keystone domains/projects/users/roles/tokens.
- [ ] I understand application credentials.
- [ ] I understand Nova and Placement.
- [ ] I understand scheduler/flavor/host aggregate/AZ concepts.
- [ ] I understand Glance/images.
- [ ] I understand instance lifecycle and cloud-init.
- [ ] I understand Neutron networks/subnets/ports/routers.
- [ ] I understand provider vs self-service networking.
- [ ] I understand security groups and floating IPs.
- [ ] I understand Cinder volumes/snapshots/backups.
- [ ] I understand Swift object storage.
- [ ] I understand Horizon and Heat.
- [ ] I understand Octavia/Barbican/Manila/Ironic/Designate at a fundamentals level.
- [ ] I understand DB/MQ control-plane dependencies.
- [ ] I understand quotas and multi-tenancy.
- [ ] I can use core `openstack` CLI commands.
- [ ] I understand OpenStack security fundamentals.
- [ ] I understand layered HA/DR concepts.
- [ ] I can trace server-build and network packet flows.
- [ ] I can troubleshoot identity, compute, network, and volume failures.
- [ ] I completed all 30 labs.
- [ ] I completed the OpenStack Private Cloud Application Environment project.
