# 42. OpenStack Deployment and Operation

> Phase 9 — Virtualization

This course takes the architecture from **41. OpenStack Fundamentals** and turns it into an operator workflow: **plan, deploy, validate, operate, scale, secure, upgrade, recover, and troubleshoot an OpenStack cloud**.

**Reference baseline:** OpenStack **2026.1 “Gazpacho”**, using **Kolla Ansible 22.x** as the primary practical deployment framework.

OpenStack is a distributed system, not one application:

```text
User / API Client
        |
        v
      HAProxy
        |
   +----+------------------------------+
   |                                   |
Keystone                            Nova API
   |                                   |
   |                       +-----------+-----------+
   |                       |           |           |
   |                   Placement   Scheduler   Conductor
   |                                               |
   +--> Glance                                    |
   +--> Neutron                                   v
   +--> Cinder                               nova-compute
   +--> Horizon                                    |
                                                   v
                                                KVM/libvirt

Control-plane services
        |
        +--> MariaDB
        +--> RabbitMQ
        +--> Cache
        +--> DNS/NTP/TLS

Kolla Ansible
        |
        +--> inventory
        +--> globals.yml
        +--> passwords.yml
        +--> Ansible
        +--> container runtime
```

The teaching pattern is:

```text
Concept
   ↓
Architecture
   ↓
Configuration / Command
   ↓
Expected Behavior
   ↓
Why It Works
   ↓
Failure Scenario
   ↓
Troubleshooting
```

---

## 1. Topic Title

**OpenStack Deployment and Operation**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Design all-in-one and multinode OpenStack deployments.
- Explain controller, compute, network, storage, and deployment-node roles.
- Plan management, API, overlay, storage, and provider/external networks.
- Plan DNS, NTP, VIPs, MTU, VLANs, routes, and physical NIC mappings.
- Install and configure Kolla Ansible in an isolated Python environment.
- Build Kolla inventories and `/etc/kolla` configuration.
- Use `kolla-genpwd`, `bootstrap-servers`, `prechecks`, `pull`, `deploy`, and `post-deploy`.
- Validate Keystone, Nova, Placement, Neutron, Glance, Cinder, and Horizon.
- Understand HAProxy, Keepalived, MariaDB/Galera, and RabbitMQ high availability.
- Operate Nova compute hosts, Cells v2, Placement, host aggregates, and availability zones.
- Operate Neutron provider/self-service networking and troubleshoot port binding and floating IPs.
- Operate Glance and Cinder and understand external Ceph integration.
- Inspect Kolla containers, configuration, and logs.
- Use `reconfigure`, `genconfig`, `validate-config`, `deploy-containers`, `stop`, and `upgrade`.
- Explain in-series updates, cross-series upgrades, and SLURP/skip-level concepts.
- Protect configuration, secrets, databases, certificates, and tenant data.
- Monitor API, DB, MQ, compute, network, and storage capacity.
- Troubleshoot common OpenStack control-plane and data-plane failures.
- Build a production-style OpenStack private-cloud mini project.

---

## 3. Prerequisites

Required:

- 41. OpenStack Fundamentals
- Linux System Administration
- Networking
- Storage Fundamentals
- Virtualization Fundamentals
- Ansible basics
- container fundamentals
- relational database fundamentals

Recommended lab:

```text
Deployment01  10.10.10.10

Controller01  10.10.10.11
Controller02  10.10.10.12
Controller03  10.10.10.13

Compute01     10.10.10.21
Compute02     10.10.10.22

Storage01     10.10.10.31
```

Suggested networks:

```text
Management/API  10.10.10.0/24
Overlay/Tunnel  10.10.20.0/24
Storage         10.10.30.0/24
External        physical provider VLAN/interface
Internal VIP    10.10.10.250
```

A single-node all-in-one deployment is acceptable for a resource-constrained lab, but the course still teaches production-style multinode architecture.

---

## 4. Core Concepts Explanation

# Part 1 — OpenStack Deployment Is a Distributed-Systems Problem

Installing OpenStack means coordinating APIs, databases, message queues, hypervisors, networking, storage, identity, and high availability.

```text
API Service
   ↓
SQL state
   ↓
RPC/message queue
   ↓
worker/scheduler
   ↓
compute/network/storage dataplane
```

A service can be "running" while the cloud operation still fails because a downstream dependency is unavailable.

# Part 2 — Manual Installation vs Deployment Automation

Manual installation is excellent for understanding service internals. Production operations benefit from repeatability.

```text
Manual:
operator edits many service files

Automated:
desired configuration
      ↓
Ansible
      ↓
repeatable state
```

Automation does not remove the need to understand what it automates.

# Part 3 — Kolla and Kolla Ansible

Kolla provides container images; Kolla Ansible deploys and operates them.

```text
Kolla
  → OpenStack container images

Kolla Ansible
  → inventory + configuration + Ansible orchestration
```

This separation matters when troubleshooting whether a problem is image content, deployment configuration, or host infrastructure.

# Part 4 — All-in-One Deployment

An all-in-one cloud places control plane, compute, networking, and supporting services on one host.

```text
One Host
 ├─ Keystone
 ├─ Nova API
 ├─ nova-compute
 ├─ Neutron
 ├─ Glance
 ├─ DB/MQ
 └─ Horizon
```

Use it for evaluation and labs. It does not model production HA or failure-domain separation.

# Part 5 — Multinode Deployment

A multinode cloud separates functional roles.

```text
Controllers → API / DB / MQ / schedulers
Computes    → KVM / nova-compute / network dataplane
Storage     → Cinder/Ceph/NFS/Swift backends
```

This enables independent scaling and better resilience.

# Part 6 — Controller Node

Controllers typically host API and coordination services such as Keystone, Nova API/Scheduler/Conductor, Neutron Server, Glance API, Cinder API/Scheduler, Horizon, HAProxy, RabbitMQ, and MariaDB.

The controller is a **control-plane node**, not where most tenant VM CPU runs.

# Part 7 — Compute Node

Compute nodes run tenant workloads.

```text
Nova control plane
      ↓
nova-compute
      ↓
libvirt
      ↓
KVM
      ↓
instance
```

They also participate in Neutron's networking dataplane.

# Part 8 — Network Node Concept

Some architectures dedicate nodes to routing, DHCP, metadata, gateways, or OVN gateway functionality. Modern deployments may distribute these functions differently.

Learn the function first:

```text
tenant networking
external routing
DHCP
metadata
gateway
```

then map it to the deployment backend.

# Part 9 — Storage Node

Storage nodes may host Cinder LVM, Ceph, NFS, Swift, or other supported backends.

Storage design determines:

```text
VM disk availability
volume performance
image performance
backup/recovery behavior
```

# Part 10 — Deployment Node

The deployment node contains the operator tooling:

```text
Kolla Ansible
Ansible inventory
/etc/kolla
SSH keys
OpenStack client
```

It is highly privileged and should be protected accordingly.

# Part 11 — Management/API Network

Management traffic includes SSH, Ansible, internal service communication, and APIs according to the design.

```text
Deployment Node
      |
Management Network
      |
Controllers / Computes
```

Do not expose this network to ordinary tenant/user traffic.

# Part 12 — Overlay/Tunnel Network

Tenant self-service networks need transport between compute nodes.

```text
VM
 ↓
overlay encapsulation
 ↓
tunnel network
 ↓
remote compute
```

The backend may use VXLAN/GENEVE/OVN concepts depending on configuration.

# Part 13 — Storage Network

Storage traffic is often isolated from API and tenant traffic.

```text
Compute
   |
Storage VLAN
   |
Ceph / Cinder / NFS
```

This improves predictability, troubleshooting, and security.

# Part 14 — Provider/External Network

Provider networking connects OpenStack to the physical network.

```text
VM
 ↓
Neutron
 ↓
provider network
 ↓
physical bridge/NIC
 ↓
switch/router
```

Kolla commonly dedicates a physical interface to Neutron external networking.

# Part 15 — Physical NIC Planning

Example:

```text
eth0 → management/API
eth1 → external/provider
eth2 → storage
eth3 → overlay
```

A lab can consolidate interfaces, but production should document which traffic class uses which failure domain.

# Part 16 — VLAN Planning

Example VLAN plan:

```text
VLAN 10  Management
VLAN 20  Overlay
VLAN 30  Storage
VLAN 100-199 Provider
```

OpenStack/Kolla settings and physical switch configuration must agree.

# Part 17 — MTU Planning

Overlay encapsulation adds headers. If the underlay MTU is too small, symptoms may be deceptive:

```text
small ping works
large transfer fails
```

Validate MTU end to end instead of setting jumbo frames on only one interface.

# Part 18 — DNS

Controllers and computes should resolve names consistently.

```bash
getent hosts controller01
getent hosts compute01
```

DNS errors often appear as API, TLS, RabbitMQ, or cluster failures rather than obvious "DNS errors."

# Part 19 — NTP

Time synchronization is critical for tokens, TLS, logs, and clustered services.

```bash
timedatectl
chronyc sources -v
```

A distributed cloud without consistent time is extremely difficult to troubleshoot.

# Part 20 — SSH and Privileged Access

Use dedicated administrative access over the management network.

Prefer:

```text
SSH key
sudo
named operator
restricted source network
```

Avoid shared root passwords and unlogged access.

# Part 21 — Python Virtual Environment

Install deployment tooling in an isolated Python environment.

```bash
python3 -m venv ~/venvs/kolla
source ~/venvs/kolla/bin/activate
pip install -U pip
```

This prevents dependency conflicts with system Python packages.

# Part 22 — Install Stable Kolla Ansible

For a 2026.1 lab, use the stable series rather than the development branch.

```bash
pip install --upgrade   git+https://opendev.org/openstack/kolla-ansible@stable/2026.1
```

Production teams should additionally pin and test the exact tool version used in CI/CD.

# Part 23 — Create `/etc/kolla`

```bash
sudo mkdir -p /etc/kolla
sudo chown "$USER:$USER" /etc/kolla
```

This directory holds deployment configuration and sensitive material. Protect its permissions and backups.

# Part 24 — Kolla Example Configuration

The installed Kolla Ansible package contains example files such as:

```text
globals.yml
passwords.yml
all-in-one inventory
multinode inventory
```

Copy the examples and edit your own environment-specific version.

# Part 25 — Ansible Inventory

Inventory maps hosts to service roles.

```ini
[control]
controller01
controller02
controller03

[compute]
compute01
compute02
```

The inventory is the deployment topology expressed as code.

# Part 26 — All-in-One Inventory

The all-in-one inventory targets localhost for a small evaluation cloud.

Commands then use:

```bash
kolla-ansible prechecks -i ./all-in-one
kolla-ansible deploy -i ./all-in-one
```

# Part 27 — Multinode Inventory

Multinode inventory separates controllers, computes, storage, and network roles. Keep it version-controlled because it represents the physical/cloud topology.

# Part 28 — Test Ansible Reachability

Before OpenStack:

```bash
ansible -i ./multinode all -m ping
```

If this fails, fix SSH, DNS, Python, sudo, or firewalling before attempting Kolla deployment.

# Part 29 — `globals.yml`

`/etc/kolla/globals.yml` is the main Kolla configuration file.

Example:

```yaml
kolla_base_distro: "ubuntu"
network_interface: "eth0"
neutron_external_interface: "eth1"
kolla_internal_vip_address: "10.10.10.250"
```

# Part 30 — Base Distribution

Use a host/container distribution supported by the exact Kolla series. Current Kolla quick-start guidance uses modern supported systems such as Ubuntu 24.04 or Rocky Linux 10 for newcomers.

Do not mix unsupported host operating systems into production.

# Part 31 — `network_interface`

This is Kolla's default management-style interface.

```yaml
network_interface: "eth0"
```

The interface must be reachable between deployment/control nodes and match the chosen management network.

# Part 32 — `neutron_external_interface`

Example:

```yaml
neutron_external_interface: "eth1"
```

This interface is typically dedicated to Neutron external/provider traffic and often has no ordinary host IP address.

# Part 33 — Internal VIP

Example:

```yaml
kolla_internal_vip_address: "10.10.10.250"
```

The address must be unused and reachable on the management/API subnet.

```text
Clients
  ↓
VIP
  ↓
HAProxy
  ↓
API backends
```

# Part 34 — Keepalived

Keepalived provides VIP failover among controller nodes.

```text
Controller01  ACTIVE
Controller02  BACKUP
Controller03  BACKUP
        |
        v
   10.10.10.250
```

If one controller fails, the VIP can move to another.

# Part 35 — HAProxy

HAProxy provides API load balancing and backend health checking.

```text
VIP:5000
   ↓
HAProxy
   +--> Keystone01
   +--> Keystone02
   +--> Keystone03
```

A healthy VIP with all unhealthy backends still means service outage.

# Part 36 — `passwords.yml`

`passwords.yml` contains service credentials and other generated secrets.

Never commit it to a public repository.

Protect:

```text
file permissions
encrypted backup
operator access
secret rotation plan
```

# Part 37 — `kolla-genpwd`

Generate required passwords:

```bash
kolla-genpwd
```

Back up the generated file securely because losing service credentials complicates disaster recovery.

# Part 38 — Modular `globals.d`

Current Kolla supports modular global configuration under:

```text
/etc/kolla/globals.d/
```

Example:

```text
10-network.yml
20-storage.yml
30-monitoring.yml
```

This improves review and separation of concerns.

# Part 39 — Enable Additional Services

Kolla exposes service enablement variables.

Concept:

```yaml
enable_horizon: "yes"
enable_cinder: "yes"
```

Only enable services your team can monitor, secure, back up, and upgrade.

# Part 40 — `install-deps`

Install required Ansible collections:

```bash
kolla-ansible install-deps
```

Run this after installing or upgrading Kolla Ansible.

# Part 41 — Bootstrap Servers

```bash
kolla-ansible bootstrap-servers -i ./multinode
```

Bootstrap prepares the hosts: container runtime and other prerequisites are configured before OpenStack services are deployed.

# Part 42 — Prechecks

```bash
kolla-ansible prechecks -i ./multinode
```

Prechecks detect obvious deployment problems such as wrong interfaces, port conflicts, unsupported state, or missing virtualization prerequisites.

Never treat precheck failure as an optional warning.

# Part 43 — Pull Images

```bash
kolla-ansible pull -i ./multinode
```

Pulling ahead of a change window isolates image-download delays from the deployment itself.

# Part 44 — Local Container Registry

A local registry improves control in multinode environments.

```text
Build/Pull
   ↓
Local Registry
   ↓
Controller + Compute nodes
```

Benefits include predictable image versions and reduced external bandwidth dependency.

# Part 45 — Deploy

```bash
kolla-ansible deploy -i ./multinode
```

Deployment generates configuration, creates containers, initializes databases, and starts services according to inventory and Kolla settings.

# Part 46 — Rerunnable Deployment

Kolla/Ansible workflows are designed to converge state. If a deployment task fails, fix the root cause and rerun rather than manually rebuilding random containers.

# Part 47 — Post Deploy

```bash
kolla-ansible post-deploy -i ./multinode
```

Current Kolla generates OpenStack client configuration such as `/etc/kolla/clouds.yaml`.

# Part 48 — `clouds.yaml`

`clouds.yaml` is used by OpenStackClient and OpenStackSDK.

```yaml
clouds:
  admin:
    auth:
      auth_url: https://cloud.example/v3
      username: admin
      project_name: admin
```

Use a secret manager or protected file for credentials.

# Part 49 — OpenStack Client

Install the unified client:

```bash
pip install python-openstackclient
```

Then:

```bash
export OS_CLOUD=admin
openstack token issue
```

A successful token proves Keystone/API reachability and client configuration.

# Part 50 — Service Catalog Validation

```bash
openstack service list
openstack endpoint list
openstack catalog list
```

A running service with a missing or wrong endpoint can still be unusable by clients.

# Part 51 — Keystone Validation

```bash
openstack token issue
openstack project list
openstack user list
```

If token issuance fails, check authentication settings, domain, endpoint/VIP, DB, and time.

# Part 52 — Glance Validation

```bash
openstack image list
```

Upload a lab image:

```bash
openstack image create cirros   --disk-format qcow2   --container-format bare   --file cirros.qcow2
```

Verify the image reaches `active`.

# Part 53 — Nova Validation

```bash
openstack compute service list
openstack hypervisor list
```

Compute services should be `up` and `enabled` before expecting scheduling to succeed.

# Part 54 — Placement

Placement tracks resource providers, inventories, traits, and allocations.

```text
Flavor request
   ↓
Nova Scheduler
   ↓
Placement candidates
   ↓
selected compute
```

`NoValidHost` is often a scheduling/Placement problem rather than an API outage.

# Part 55 — Neutron Validation

```bash
openstack network list
openstack subnet list
openstack router list
```

If using classic agents:

```bash
openstack network agent list
```

With OVN, understand the OVN control/dataplane instead of expecting every legacy agent.

# Part 56 — Create Provider Network

A provider network maps OpenStack networking to physical infrastructure.

```text
OpenStack physnet
   ↓
bridge mapping
   ↓
external interface
   ↓
physical VLAN/switch
```

This mapping must be correct end to end.

# Part 57 — Create Self-Service Network

```bash
openstack network create private

openstack subnet create private-subnet   --network private   --subnet-range 192.168.10.0/24
```

This creates tenant L2/L3 resources independent of the external provider network.

# Part 58 — Router

```bash
openstack router create router1
```

Concept:

```text
Private subnet
    ↓
Neutron router
    ↓
External network
```

# Part 59 — Floating IP

```bash
openstack floating ip create public
```

Floating IP connectivity requires more than NAT:

```text
provider network
router
security group
guest network
physical route
```

# Part 60 — Security Groups

Create least-access rules.

```bash
openstack security group create web-sg

openstack security group rule create web-sg   --protocol tcp   --dst-port 22   --remote-ip 10.10.0.0/16
```

Avoid broad admin exposure.

# Part 61 — Flavors

```bash
openstack flavor create m1.small   --ram 2048   --disk 20   --vcpus 2
```

Flavor is the resource request; it does not guarantee a suitable host exists.

# Part 62 — Key Pairs

Upload only the public key:

```bash
openstack keypair create lab-key   --public-key ~/.ssh/id_ed25519.pub
```

Never upload a user's private SSH key.

# Part 63 — Boot Instance

```bash
openstack server create vm01   --image cirros   --flavor m1.small   --network private   --key-name lab-key
```

Then inspect:

```bash
openstack server show vm01
```

# Part 64 — Instance State Machine

Important states include:

```text
BUILD
ACTIVE
ERROR
SHUTOFF
MIGRATING
RESIZE
```

`ERROR` is a symptom; the `fault` and service logs contain the real evidence.

# Part 65 — `NoValidHost`

Potential causes:

```text
insufficient RAM/vCPU/disk
host disabled
aggregate/AZ constraints
traits
NUMA/hugepages
PCI/GPU
Placement inventory
```

Read scheduler logs before adding hardware.

# Part 66 — Nova Cells v2

Cells v2 scales Nova and isolates compute failure domains.

```text
API/Scheduler
   |
   +-- Cell0: failed-to-schedule records
   |
   +-- Cell1: computes + cell DB/message path
```

Operators must understand cells during scaling and upgrades.

# Part 67 — Cell0

Cell0 contains instances that never reached a compute cell.

Repeated scheduling failures can leave records there; this is different from an instance that failed after being scheduled to a compute host.

# Part 68 — Disable a Compute Service

Before maintenance:

```bash
openstack compute service set   --disable compute01 nova-compute
```

Existing VMs remain; new scheduling avoids the host.

# Part 69 — Compute Maintenance Workflow

```text
disable scheduling
   ↓
migrate/evacuate workloads
   ↓
patch/reboot
   ↓
validate libvirt/nova/network
   ↓
enable scheduling
```

# Part 70 — Live Migration

Nova can live-migrate supported instances.

Requirements include:

```text
CPU compatibility
destination capacity
network
storage/block migration path
libvirt
```

Always verify instance and storage characteristics first.

# Part 71 — Cold Migration

Cold migration moves an instance without maintaining uninterrupted execution. It can be operationally simpler than live migration in some storage designs.

# Part 72 — Evacuation

Evacuation recovers instances from a failed compute host onto another host when the architecture supports it.

It is a **failure recovery** operation, not the same as routine live migration.

# Part 73 — Add Compute Host

Process:

```text
prepare OS/network/storage
add to inventory
bootstrap
deploy nova/network services
validate Placement
validate Neutron
enable scheduling
```

# Part 74 — Remove Compute Host

Process:

```text
disable
drain VMs
verify no workloads
remove scheduling metadata
remove inventory/deploy state
clean securely
```

Never wipe a compute that still owns local-instance data.

# Part 75 — Host Aggregates

Aggregates group compute hosts for scheduling policy.

Examples:

```text
GPU
SSD
Licensed
HighMemory
```

Metadata can be matched to flavors/images.

# Part 76 — Availability Zones

Availability zones expose scheduling domains to users.

```text
AZ-A
AZ-B
```

Do not expose every internal aggregate as an availability zone unless there is a user-facing reason.

# Part 77 — Quotas

Quotas protect finite resources:

```text
instances
vCPUs
RAM
volumes
GB
ports
floating IPs
```

A quota error does not mean the physical cloud is full.

# Part 78 — Resource Overcommit

Operators may overcommit CPU and thin-provision storage.

```text
logical allocation
>
physical instantaneous use
```

Safe overcommit requires monitoring, capacity forecasting, and workload knowledge.

# Part 79 — OVN Architecture

A common modern Neutron backend is OVN.

```text
Neutron API
   ↓
OVN Northbound DB
   ↓
OVN Southbound DB
   ↓
ovn-controller
   ↓
Open vSwitch
```

# Part 80 — Open vSwitch

OVS provides software switching.

```bash
ovs-vsctl show
```

Use it for inspection. Avoid manual flow changes that conflict with OVN/Neutron controller ownership.

# Part 81 — Port Binding

A Neutron port must bind to a concrete host/dataplane.

Failure can result in:

```text
instance BUILD/ERROR
port DOWN
no connectivity
```

Check binding host, mechanism/OVN state, and bridge mappings.

# Part 82 — External Bridge Mapping

Example:

```text
physnet1
   ↓
br-ex
   ↓
eth1
```

An incorrect physnet-to-interface mapping breaks provider/floating IP traffic.

# Part 83 — Floating IP Troubleshooting

Trace:

```text
client
 ↓
physical router
 ↓
provider network
 ↓
Neutron router/NAT
 ↓
security group
 ↓
instance port
 ↓
guest firewall
```

# Part 84 — DHCP Troubleshooting

Check:

```text
subnet DHCP flag
DHCP backend/service
port state
security
guest interface
```

If static addressing works but DHCP does not, the L2 path may be fine.

# Part 85 — Metadata Service

Metadata provides cloud-init data such as:

```text
instance ID
hostname
SSH key
user-data
```

If VM boots but user-data/key injection fails, inspect metadata connectivity.

# Part 86 — Glance Storage Backend

Glance metadata and image binary storage are different layers.

Backends can include:

```text
filesystem
Ceph RBD
object storage
```

Check both API and backend capacity.

# Part 87 — Compute Image Cache

Compute nodes may cache base images to accelerate repeated launches.

This consumes local disk; cache pressure can cause image-download or instance-creation failures.

# Part 88 — Glance Upload Failure

If an image remains `queued`/`saving` or becomes failed:

```text
Glance API
backend
capacity
permissions
network
DB
```

must be checked.

# Part 89 — Cinder Architecture

```text
Client
 ↓
Cinder API
 ↓
Scheduler
 ↓
cinder-volume
 ↓
storage backend
```

Backend examples include LVM, Ceph RBD, and vendor SAN/NAS drivers.

# Part 90 — Cinder Service Validation

```bash
openstack volume service list
```

Check scheduler and backend services are up/enabled.

# Part 91 — Create and Attach Volume

```bash
openstack volume create --size 10 data01
openstack server add volume vm01 data01
```

A successful attach requires Nova, Cinder, backend connectivity, and the compute host.

# Part 92 — Volume Attachment Path

```text
Nova
 ↓
Cinder attachment
 ↓
backend connection info
 ↓
compute os-brick
 ↓
iSCSI/RBD/FC
 ↓
guest block device
```

This gives you a precise troubleshooting path.

# Part 93 — External Ceph Integration

OpenStack can use an external Ceph cluster.

```text
Glance → RBD
Cinder → RBD
Nova disks → RBD
```

Ceph remains its own distributed system with independent monitoring and recovery.

# Part 94 — Ceph Failure Impact

A Ceph latency incident may make:

```text
VM disks slow
volumes fail
images slow
```

while Keystone/Nova APIs still respond normally. Control-plane health is not data-plane health.

# Part 95 — Horizon

Horizon is a web dashboard over the APIs.

If Horizon fails:

```text
OpenStack CLI/API may still work
```

Always validate the API independently.

# Part 96 — Heat Operations

Heat orchestrates resources but depends on Keystone and downstream services.

A stack failure may actually originate from Nova, Neutron, Cinder, or quota limits.

# Part 97 — Octavia Operations

Octavia provides load balancing. Its deployment can involve controller services, network paths, and provider-specific load-balancer resources.

Monitor both Octavia services and the actual load-balancer dataplane.

# Part 98 — Barbican Operations

Barbican stores keys/secrets and may protect TLS material.

Its database, encryption/master-key design, and access policy are security-critical.

# Part 99 — Manila Operations

Manila manages shared file systems.

```text
Manila API
 ↓
Scheduler
 ↓
Share backend
```

It is distinct from Cinder block storage.

# Part 100 — Designate Operations

Designate provides DNS as a service and can integrate with authoritative DNS backends.

DNS changes affect external reachability, so backend synchronization and zone health matter.

# Part 101 — Ironic Operations

Ironic provisions bare-metal machines through BMC and network boot workflows.

```text
API
 ↓
Ironic conductor
 ↓
BMC / PXE / image
 ↓
physical server
```

BMC credentials are highly privileged.

# Part 102 — Inspect Kolla Containers

```bash
docker ps
```

Map containers to services before troubleshooting.

Example categories:

```text
keystone
nova
neutron
glance
cinder
mariadb
rabbitmq
haproxy
```

# Part 103 — Kolla Logs

Service logs are commonly available under:

```text
/var/log/kolla/
```

Container stdout may also be useful:

```bash
docker logs <container>
```

Capture the first meaningful error instead of only the final failure message.

# Part 104 — Do Not Restart First

Restarting can hide evidence and briefly mask a dependency failure.

Evidence-first:

```text
status
logs
DB
MQ
network
storage
```

then restart only if justified.

# Part 105 — `reconfigure`

Apply changed service configuration:

```bash
kolla-ansible reconfigure -i ./multinode
```

Use after review and validation, not as an uncontrolled fix-all command.

# Part 106 — `genconfig`

Generate configuration without applying it:

```bash
kolla-ansible genconfig -i ./multinode
```

This enables diff/review before a production change.

# Part 107 — `validate-config`

```bash
kolla-ansible validate-config -i ./multinode
```

Current Kolla records detected configuration-validation issues under `/var/log/kolla/config-validate` by default.

# Part 108 — `deploy-containers`

```bash
kolla-ansible deploy-containers -i ./multinode
```

This reconciles containers without regenerating service configuration, useful in specific operational workflows.

# Part 109 — `stop`

```bash
kolla-ansible stop -i ./multinode
```

This stops deployment containers and is disruptive. Do not use it as routine troubleshooting.

# Part 110 — `destroy`

`kolla-ansible destroy` is destructive cleanup.

Use it for intentional lab teardown or an approved rebuild—not production diagnosis.

# Part 111 — Configuration Overrides

Custom service overrides can be kept under Kolla's configuration hierarchy.

Principle:

```text
override only what is required
```

Every custom option increases upgrade/testing responsibility.

# Part 112 — Configuration as Code

Version-control:

```text
inventory
globals
network design
service enablement
non-secret overrides
```

Keep secrets, keys, and credentials outside ordinary Git history.

# Part 113 — MariaDB/Galera Control-Plane HA

Most OpenStack services persist state in SQL.

```text
Controller01 DB
Controller02 DB
Controller03 DB
      |
replicated cluster
```

Database quorum and network health are cloud-wide dependencies.

# Part 114 — Database Cluster Recovery

Kolla provides:

```bash
kolla-ansible mariadb-recovery -i ./multinode
```

for a completely stopped MariaDB cluster.

Use only after confirming cluster state and following supported recovery procedure.

# Part 115 — Database Backup

Protect:

```text
service databases
Kolla configuration
passwords
certificates
custom overrides
```

Tenant volume/image data requires separate backend protection.

# Part 116 — RabbitMQ

RPC and asynchronous work often flow through RabbitMQ.

```text
Nova API
  ↓
RabbitMQ
  ↓
Scheduler / Conductor / Compute
```

A request may be accepted by the API and then stall if messaging fails.

# Part 117 — RabbitMQ HA

Monitor:

```text
cluster members
queues
connections
memory alarm
disk alarm
partitions
```

A RabbitMQ disk alarm can halt publishing even when the process is running.

# Part 118 — Cache Layer

Caching reduces repetitive Keystone/DB load.

A cache outage may increase latency and DB traffic rather than causing immediate total failure.

Understand cache as an acceleration layer, not source of truth.

# Part 119 — HAProxy Troubleshooting

If APIs fail through VIP:

```text
DNS
VIP ownership
HAProxy
backend service
TLS
```

If direct backend works but VIP fails, focus on HAProxy/Keepalived.

# Part 120 — Keepalived Troubleshooting

Symptoms:

```text
VIP missing
duplicate VIP
flapping
```

Check VRRP network, interface, firewall, priority/state, and IP conflicts.

# Part 121 — TLS

Production APIs should use TLS.

Certificate lifecycle includes:

```text
issuance
trust
renewal
rotation
revocation
expiry monitoring
```

Do not wait for expiry to discover that automation cannot authenticate.

# Part 122 — Secrets Management

Kolla credentials may be integrated into stronger operator secret-management workflows.

Principles:

```text
least access
no plaintext CI logs
rotation
encrypted backup
separate cloud-user and host-admin credentials
```

# Part 123 — RBAC and Service Identities

Separate:

```text
cloud administrator
project user
service account
deployment-node administrator
automation account
```

A cloud admin token should not be the default credential for every integration.

# Part 124 — Monitoring Layers

Monitor each layer:

```text
host
container runtime
service
API
DB
MQ
hypervisor
network
storage
user transaction
```

The most useful monitor often performs a real authenticated read operation, not merely a TCP check.

# Part 125 — Capacity Monitoring

Track:

```text
Nova: vCPU/RAM/disk/Placement
Neutron: ports/IPs/bandwidth
Cinder: backend capacity
Ceph: usable capacity/latency
Glance: image backend
```

Capacity exhaustion often appears as scheduling failures before a node itself crashes.

# Part 126 — Quotas vs Capacity

Quota and physical capacity are different.

```text
Project quota exhausted
but
cloud has resources
```

or:

```text
project quota available
but
no physical host fits request
```

Diagnose the correct layer.

# Part 127 — Centralized Logging

Centralize:

```text
Kolla logs
journald
DB/MQ logs
hypervisor
OVN/OVS
storage
```

All systems must use synchronized time to correlate one request.

# Part 128 — Request IDs

OpenStack requests commonly include request identifiers.

Use them to trace one operation across:

```text
API
scheduler
conductor
compute
network
storage
```

This is one of the most effective operator habits.

# Part 129 — Instance BUILD Troubleshooting

Trace:

```text
Nova API
 ↓
Scheduler
 ↓
Placement
 ↓
Conductor
 ↓
Compute
 ↓
Glance/Neutron/Cinder
```

Find the layer where progress stopped.

# Part 130 — Instance ERROR Troubleshooting

Start with:

```bash
openstack server show vm01
```

Inspect `fault`, host/task information, then correlate service logs and request ID.

Never manually set instance state in SQL as the first response.

# Part 131 — Keystone 401 vs 403

```text
401 Unauthorized
  authentication failed

403 Forbidden
  identity authenticated but lacks authorization
```

This distinction immediately narrows troubleshooting.

# Part 132 — Endpoint / 404 Problems

Check:

```bash
openstack endpoint list
openstack catalog list
```

Wrong endpoint path, interface, region, or API version can produce 404 even when the service is running.

# Part 133 — Message Queue Failure Pattern

Symptom:

```text
API accepts request
resource remains pending
```

Check message-bus connectivity and whether backend consumers are processing queues.

# Part 134 — Database Failure Pattern

Many APIs fail with 500/timeout simultaneously.

Check:

```text
DB connections
cluster quorum
disk
locks
latency
```

before restarting every API container.

# Part 135 — Compute Capacity Planning

Track special scheduling dimensions:

```text
NUMA
huge pages
CPU pinning
GPU/PCI
traits
local disk
```

A cloud can have free CPU yet still have no host matching a specialized request.

# Part 136 — Network Capacity Planning

Monitor:

```text
overlay throughput
provider uplink
north-south
east-west
floating IP pool
router/gateway scale
```

# Part 137 — Storage Capacity Planning

Track both logical and physical views:

```text
Cinder reported free
backend actual free
thin allocation
replication overhead
IOPS
latency
```

# Part 138 — In-Series Updates

Within one OpenStack series, the usual pattern is:

```text
update Kolla tooling
pull/build updated images
review release notes
deploy/reconcile
```

This is different from a cross-series database/API upgrade.

# Part 139 — Cross-Series Upgrade

Kolla provides:

```bash
kolla-ansible upgrade -i ./multinode
```

This can recreate containers and perform database schema/service upgrade work. Treat it as a planned infrastructure change, not a routine restart.

# Part 140 — Upgrade Preparation

Before upgrade:

```text
read target release notes
back up /etc/kolla
back up SQL
preserve secrets/certs
update Kolla tooling
diff inventory
pull images
run prechecks
test staging
```

# Part 141 — `kolla-mergepwd`

When a new release introduces new password keys, merge the old secret set into the new template.

```bash
kolla-mergepwd   --old passwords.yml.old   --new passwords.yml.new   --final /etc/kolla/passwords.yml
```

# Part 142 — SLURP / Skip-Level Upgrades

Selected OpenStack releases support specific skip-level upgrade strategies. This does **not** mean arbitrary releases can be skipped.

Dependencies such as RabbitMQ, databases, Ansible, and service-specific migrations still require explicit preparation.

# Part 143 — Upgrade Testing

A good staging test uses:

```text
same integrations
same custom overrides
representative workloads
same networking/storage model
```

Test VM lifecycle, networking, volumes, HA, APIs, and automation before production.

# Part 144 — Rollback Reality

Database schema changes can make rollback complex.

Therefore:

```text
backup
tested upgrade
recovery plan
maintenance window
```

are more important than assuming old containers can simply be started again.

# Part 145 — OpenStack Backup Scope

A complete protection strategy includes:

```text
Kolla config
passwords
SQL
TLS
Glance data
Cinder/volume data
Ceph state
Heat templates
automation
DNS/IPAM integrations
```

# Part 146 — Disaster Recovery

Cloud DR is not only restoring controllers.

You need:

```text
control plane
compute
networking
storage
identity
DNS
VIP
images
volumes
secrets
```

and a tested recovery order.

# Part 147 — Rebuild vs Restore

Stateless service containers should often be recreated from configuration.

Stateful components require restoration:

```text
SQL
tenant data
keys/certificates
persistent backends
```

This is the immutable-infrastructure mindset applied to cloud control planes.

# Part 148 — Daily Operations

Daily check:

```text
API health
VIP/HAProxy
MariaDB
RabbitMQ
Nova services
Neutron/OVN
Cinder
Glance
capacity
backups
alarms
```

# Part 149 — Weekly Operations

Review:

```text
disabled hosts
stale images
orphan volumes
quota pressure
certificate expiry
failed backups
old logs
capacity trend
```

# Part 150 — Incident Workflow

```text
1. Reproduce user symptom
2. Capture request ID
3. Identify service
4. Check API
5. Check DB/MQ
6. Check scheduler/control process
7. Check compute/network/storage dataplane
8. Correct root cause
9. Verify user transaction
10. Document prevention
```

# Part 151 — Change Workflow

```text
Git change
 ↓
peer review
 ↓
genconfig
 ↓
validate-config
 ↓
approved maintenance
 ↓
reconfigure/deploy
 ↓
health checks
```

# Part 152 — Adding Capacity

Do not wait for saturation.

```text
forecast
procure
prepare
network/storage test
inventory
bootstrap
deploy
validate
enable scheduling
```

# Part 153 — Decommissioning

A safe decommission:

```text
disable
drain
verify data
remove scheduling references
remove from inventory
wipe secrets/data
update CMDB/docs
```

# Part 154 — Operational Documentation

Maintain:

```text
ARCHITECTURE.md
INVENTORY.md
NETWORK.md
STORAGE.md
GLOBALS.md
HA.md
SECURITY.md
BACKUP.md
UPGRADE.md
RUNBOOKS/
```

# Part 155 — Core Operator Mental Model

When a VM does not boot, ask the whole chain:

```text
Keystone?
Nova API?
Scheduler?
Placement?
Neutron?
Glance?
Cinder?
nova-compute?
libvirt?
KVM?
network?
storage?
```

This dependency-based reasoning is the central skill of OpenStack operations.

---

# Enhanced Deep-Study Layer — OpenStack Deployment and Operation

This layer preserves the uploaded course and expands the operator workflow using:

```text
Plan → Deploy → Validate → Operate → Monitor → Change → Upgrade → Recover
```

The source uses **OpenStack 2026.1 “Gazpacho”** and **Kolla Ansible 22.x** as the reference baseline. Use the exact documentation for the release actually installed before production actions.


## Advanced Deep Dive 1 — Kolla and Kolla Ansible operating model

### Concept

Kolla supplies service container images; Kolla Ansible turns inventory and configuration into a repeatable OpenStack deployment.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible --version
ansible -i ./multinode all -m ping
kolla-ansible prechecks -i ./multinode
docker ps
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Kolla and Kolla Ansible operating model**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 2 — Deployment node security

### Concept

The deployment node can SSH to cloud nodes, holds Kolla configuration/secrets, and can reconfigure the entire cloud.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ls -l /etc/kolla
stat ~/.ssh/id_ed25519
git status
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Deployment node security**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 3 — All-in-one versus multinode

### Concept

All-in-one is useful for learning; multinode separates controller, compute, network, and storage roles for scale and HA.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ansible-inventory -i ./multinode --graph 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **All-in-one versus multinode**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 4 — Controller role

### Concept

Controllers host APIs, schedulers/control services, HA endpoints, database, and message queue components.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
docker ps | grep -E 'keystone|nova|neutron|glance|cinder|mariadb|rabbit|haproxy'
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Controller role**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 5 — Compute role

### Concept

Compute nodes run nova-compute, KVM/libvirt, and networking dataplane components that execute tenant workloads.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack compute service list
openstack hypervisor list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Compute role**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 6 — Network/gateway role

### Concept

Some architectures dedicate nodes or Edge-like gateway functions to external routing, DHCP, metadata, or OVN gateway tasks.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack network agent list 2>/dev/null || true
openstack router list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Network/gateway role**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 7 — Storage role

### Concept

Storage nodes/backends may provide Cinder, Ceph, NFS, Swift, or vendor storage and define VM/volume durability.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack volume service list
openstack volume type list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Storage role**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 8 — Management/API network

### Concept

The management network carries SSH, Ansible, internal service traffic, and often API/VIP communication.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ip -br addr
ip route
getent hosts controller01
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Management/API network**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 9 — Overlay/tunnel network

### Concept

Tenant network encapsulation between compute/gateway nodes depends on routed underlay reachability and correct MTU.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ip -d link
ip route
ping -M do -s <size> <peer> 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Overlay/tunnel network**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 10 — Storage network

### Concept

Compute-to-storage traffic should use a deliberate network path with enough bandwidth, redundancy, and isolation.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ip -br addr
ip route
ss -ntp | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Storage network**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 11 — Provider/external network

### Concept

Neutron provider/floating-IP traffic needs an exact physnet→bridge→NIC→switch/router mapping.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack network show public
ovs-vsctl show
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Provider/external network**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 12 — Physical NIC and VLAN planning

### Concept

Kolla interface variables must correspond to real NICs/VLANs and upstream switch configuration.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ip -br link
ip -d link
ethtool <iface> 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Physical NIC and VLAN planning**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 13 — MTU planning

### Concept

Overlay headers consume MTU headroom, so host, OVS/OVN, physical switches, and peers must agree.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ip link show
ping -M do -s <size> <peer> 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **MTU planning**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 14 — DNS and NTP

### Concept

Name resolution and synchronized time are prerequisites for TLS, tokens, logs, DB/MQ clusters, and service discovery.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
getent hosts controller01
chronyc sources -v
timedatectl
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **DNS and NTP**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 15 — Python virtual environment

### Concept

Kolla Ansible should run in a controlled Python environment to avoid dependency conflicts with system packages.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
python3 -m venv ~/venvs/kolla
source ~/venvs/kolla/bin/activate
python -m pip list | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Python virtual environment**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 16 — Stable Kolla Ansible installation

### Concept

Deployment tooling version should match the intended OpenStack release and be pinned/tested in automation.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
pip show kolla-ansible 2>/dev/null || true
kolla-ansible --version
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Stable Kolla Ansible installation**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 17 — /etc/kolla structure

### Concept

/etc/kolla holds globals, passwords, overrides, generated configs, and client configuration and must be protected/backed up.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
find /etc/kolla -maxdepth 2 -type f | sort | head -100
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **/etc/kolla structure**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 18 — Inventory as architecture-as-code

### Concept

The Ansible inventory describes which physical hosts perform which cloud roles.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ansible-inventory -i ./multinode --graph 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Inventory as architecture-as-code**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 19 — Ansible reachability

### Concept

OpenStack deployment should not begin until SSH, Python, sudo, DNS, and firewall assumptions pass Ansible checks.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ansible -i ./multinode all -m ping
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Ansible reachability**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 20 — globals.yml

### Concept

globals.yml expresses major Kolla choices such as distro, interfaces, VIP, networking, and service enablement.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
grep -vE '^\s*(#|$)' /etc/kolla/globals.yml 2>/dev/null | head -100
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **globals.yml**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 21 — globals.d modular configuration

### Concept

Splitting network, storage, security, and monitoring settings into globals.d improves review and ownership.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
find /etc/kolla/globals.d -maxdepth 1 -type f -print 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **globals.d modular configuration**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 22 — passwords.yml lifecycle

### Concept

passwords.yml is persistent secret state; losing, exposing, or regenerating it carelessly can break the running cloud.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
stat /etc/kolla/passwords.yml 2>/dev/null || true
sha256sum /etc/kolla/passwords.yml 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **passwords.yml lifecycle**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 23 — kolla-genpwd

### Concept

kolla-genpwd creates required service secrets and should be followed by secure backup and restricted permissions.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-genpwd
chmod 600 /etc/kolla/passwords.yml
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **kolla-genpwd**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 24 — install-deps

### Concept

Kolla Ansible relies on required Ansible collections/dependencies that should be installed for the exact tool version.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible install-deps
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **install-deps**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 25 — bootstrap-servers

### Concept

bootstrap-servers prepares hosts and should only run after supported OS, network, DNS, NTP, sudo, and storage prerequisites are correct.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible bootstrap-servers -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **bootstrap-servers**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 26 — prechecks

### Concept

prechecks are a deployment/change gate; failed checks should be understood and corrected before proceeding.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible prechecks -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **prechecks**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 27 — Image pull and local registry

### Concept

Pre-pulling or using a local registry removes external registry dependency from the maintenance window.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible pull -i ./multinode
docker images | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Image pull and local registry**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 28 — deploy convergence

### Concept

Kolla/Ansible should converge to desired state; after fixing the root cause of a failed task, rerun rather than perform random manual repairs.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible deploy -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **deploy convergence**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 29 — post-deploy and clouds.yaml

### Concept

post-deploy creates client configuration so the operator can validate the actual OpenStack APIs.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible post-deploy -i ./multinode
export OS_CLOUD=admin
openstack token issue
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **post-deploy and clouds.yaml**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 30 — Service catalog validation

### Concept

A service can be running but unusable if catalog/endpoint configuration is wrong.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack service list
openstack endpoint list
openstack catalog list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Service catalog validation**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 31 — Keystone smoke test

### Concept

Token issuance validates DNS/TLS/VIP/HAProxy/Keystone/DB integration.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack token issue
openstack project list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Keystone smoke test**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 32 — Glance smoke test

### Concept

Image list/upload validates Glance API, backend, auth, and capacity.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack image list
openstack image show <image>
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Glance smoke test**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 33 — Nova smoke test

### Concept

Compute service/hypervisor checks validate nova-compute registration and basic Placement visibility.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack compute service list
openstack hypervisor list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Nova smoke test**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 34 — Placement and NoValidHost

### Concept

NoValidHost is a scheduling result and requires capacity/trait/AZ/aggregate diagnosis, not random Nova restarts.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack hypervisor list
openstack flavor show <flavor>
openstack aggregate list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Placement and NoValidHost**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 35 — Neutron smoke test

### Concept

Network, subnet, router, port, and backend state should be validated before declaring deployment ready.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack network list
openstack subnet list
openstack router list
openstack port list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Neutron smoke test**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 36 — Provider network bridge mapping

### Concept

Provider traffic requires correct physnet mapping through OVS bridge and physical NIC/VLAN.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack network show public
ovs-vsctl show
ip -br link
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Provider network bridge mapping**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 37 — OVN architecture

### Concept

Neutron can program OVN NB/SB databases and ovn-controller/OVS realizes the dataplane.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ovn-nbctl show 2>/dev/null || true
ovn-sbctl show 2>/dev/null || true
ovs-vsctl show
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **OVN architecture**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 38 — Port binding

### Concept

A Neutron port must bind to the selected host/dataplane or VM build/networking can fail.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack port show <port-id>
openstack port list --server <server-id>
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Port binding**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 39 — Floating IP path

### Concept

Floating IP failures must be traced through provider network, router/NAT, security group, VM port, guest firewall, and physical routing.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack floating ip list
openstack router list
openstack port list --server <server>
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Floating IP path**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 40 — DHCP and metadata

### Concept

A VM can be ACTIVE while DHCP or metadata fails, causing no address, no key injection, or broken cloud-init.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack subnet show <subnet>
cloud-init status --long 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **DHCP and metadata**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 41 — Compute maintenance

### Concept

Disable scheduling, drain/migrate, patch/reboot, validate Nova/Neutron/storage, then re-enable.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack compute service set --disable compute01 nova-compute
openstack server list --host compute01 --all-projects 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Compute maintenance**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 42 — Live migration, cold migration, evacuation

### Concept

Live migration is planned running relocation, cold migration accepts downtime, and evacuation is failed-host recovery.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack server migrate <server> 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Live migration, cold migration, evacuation**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 43 — Add compute host

### Concept

A new compute is production-ready only after Nova, Placement, Neutron, storage, and a real validation VM succeed.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack compute service list
openstack hypervisor list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Add compute host**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 44 — Remove compute host

### Concept

Decommission only after disabling scheduling, draining all VMs, removing scheduling state/inventory, and securely wiping data/secrets.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack compute service set --disable compute01 nova-compute
openstack server list --host compute01 --all-projects 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Remove compute host**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 45 — Host aggregates and availability zones

### Concept

Aggregates drive operator scheduling metadata; availability zones expose meaningful placement domains to users.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack aggregate list
openstack availability zone list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Host aggregates and availability zones**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 46 — Resource overcommit

### Concept

CPU and storage may be overcommitted, but safe ratios require monitoring, workload knowledge, and failure-state capacity.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack hypervisor stats show 2>/dev/null || true
openstack quota show 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Resource overcommit**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 47 — Glance backend and compute image cache

### Concept

Image backend capacity and compute local image cache are separate resources and can fail independently.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack image list
df -h
du -sh /var/lib/nova/* 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Glance backend and compute image cache**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 48 — Cinder operations

### Concept

Cinder API/scheduler/service state must be combined with real backend capacity and compute connector health.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack volume service list
openstack volume list
openstack volume show <volume>
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Cinder operations**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 49 — External Ceph

### Concept

Ceph is an independent distributed system; OpenStack health does not imply Ceph capacity/latency health.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ceph -s 2>/dev/null || true
ceph df 2>/dev/null || true
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **External Ceph**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 50 — Kolla container inspection

### Concept

Container status, image, config mounts, service process, and downstream dependencies should all be checked.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
docker ps
docker inspect <container>
docker logs <container> | tail -100
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Kolla container inspection**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 51 — Kolla logs

### Concept

/var/log/kolla plus request IDs provide cross-service evidence and should be collected before restart.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
find /var/log/kolla -type f | head
grep -R 'req-' /var/log/kolla 2>/dev/null | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Kolla logs**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 52 — Evidence before restart

### Concept

Restarting first can hide the root cause; capture resource state, request ID, logs, DB/MQ, and network/storage evidence first.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
docker ps
openstack server show <server>
openstack --debug server show <server>
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Evidence before restart**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 53 — genconfig

### Concept

genconfig renders service configuration without applying it, allowing diff/review before change.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible genconfig -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **genconfig**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 54 — validate-config

### Concept

validate-config checks rendered service configuration and should be part of the change gate.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible validate-config -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **validate-config**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 55 — reconfigure

### Concept

reconfigure applies reviewed configuration changes and should be followed by API and end-to-end validation.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible reconfigure -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **reconfigure**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 56 — deploy-containers

### Concept

deploy-containers reconciles containers without regenerating service configuration and is appropriate for specific image/container workflows.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible deploy-containers -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **deploy-containers**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 57 — MariaDB/Galera HA

### Concept

Database quorum, replication, disk, connections, and latency are cloud-wide dependencies.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
docker ps | grep mariadb
docker logs mariadb 2>/dev/null | tail -100
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **MariaDB/Galera HA**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 58 — MariaDB recovery

### Concept

A completely stopped DB cluster may require supported Kolla recovery; normal restarts are not always safe.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible mariadb-recovery -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **MariaDB recovery**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 59 — RabbitMQ HA

### Concept

Cluster membership, queues, consumers, partitions, memory alarms, and disk alarms must all be healthy.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
docker ps | grep rabbit
docker logs rabbitmq 2>/dev/null | tail -100
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **RabbitMQ HA**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 60 — HAProxy health

### Concept

HAProxy backend health must be checked separately from VIP ownership.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
docker ps | grep haproxy
docker logs haproxy 2>/dev/null | tail -100
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **HAProxy health**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 61 — Keepalived/VRRP health

### Concept

VIP duplication, loss, or flapping can result from interface, firewall, priority, network, or IP conflicts.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ip addr
ip neigh
docker logs keepalived 2>/dev/null | tail -100
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Keepalived/VRRP health**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 62 — TLS lifecycle

### Concept

Certificate issuance, SAN/FQDN, trust, renewal, rotation, and expiry monitoring are API availability dependencies.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openssl s_client -connect <vip>:443 -servername <fqdn> </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **TLS lifecycle**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 63 — Service credential rotation

### Concept

Rotating internal secrets requires coordinated update of all consumers and should not be an ad-hoc file edit.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
grep -R '<credential-key>' /etc/kolla 2>/dev/null | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Service credential rotation**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 64 — Centralized logging and time

### Concept

Cross-service incident timelines require synchronized clocks and central searchable logs.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
chronyc sources -v
timedatectl
find /var/log/kolla -type f | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Centralized logging and time**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 65 — Request IDs

### Concept

Request IDs are the best key for following one API operation across Nova, Neutron, Cinder, and other logs.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack --debug server show <server>
grep -R 'req-' /var/log/kolla 2>/dev/null | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Request IDs**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 66 — Capacity monitoring

### Concept

Track quota, Placement/per-host fit, network IP pools, Cinder/Ceph capacity, and failure-state headroom.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack hypervisor stats show 2>/dev/null || true
openstack quota show 2>/dev/null || true
openstack floating ip list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Capacity monitoring**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 67 — In-series updates

### Concept

Updates within one release family differ from cross-series upgrades and should still use prechecks, staged images, and smoke tests.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible prechecks -i ./multinode
kolla-ansible pull -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **In-series updates**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 68 — Cross-series upgrades

### Concept

Release upgrades can change schemas, RPC, config, dependencies, and API behavior and require staging rehearsal and backups.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible prechecks -i ./multinode
kolla-ansible upgrade -i ./multinode
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Cross-series upgrades**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 69 — SLURP/skip-level upgrades

### Concept

Skip-level support exists only for documented release paths; arbitrary versions cannot be skipped safely.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
kolla-ansible --version
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **SLURP/skip-level upgrades**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 70 — Rollback reality

### Concept

After DB migrations, old containers may not understand the new schema, so recovery must be based on tested backup/restore or supported forward-fix paths.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
ls -l /etc/kolla
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Rollback reality**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 71 — Backup scope

### Concept

A usable backup includes Kolla inventory/config/secrets/TLS/SQL plus images, volumes, object data, and external storage state.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
find /etc/kolla -maxdepth 2 -type f | sort | head
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Backup scope**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 72 — DR restore order

### Concept

Restore physical/network base, DNS/time/TLS, DB/MQ, Keystone/VIP/APIs, networking/storage, computes, then tenant applications.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack service list
openstack compute service list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **DR restore order**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 73 — Daily and weekly operations

### Concept

Daily health checks and weekly hygiene/capacity reviews prevent gradual degradation from becoming incidents.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack service list
openstack compute service list
openstack volume service list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Daily and weekly operations**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 74 — Operational SLOs

### Concept

Measure authenticated API success and end-to-end VM/network/volume provisioning latency, not only container uptime.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack --debug server list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Operational SLOs**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


## Advanced Deep Dive 75 — Change validation matrix

### Concept

Each config change should map to targeted before/after tests and a full minimal smoke test.

An OpenStack operator should always separate five layers:

```text
1. Host infrastructure
2. Kolla/Ansible desired configuration
3. Container runtime and generated configuration
4. OpenStack service/API + DB/MQ dependencies
5. Tenant compute/network/storage data plane
```

A failure at one layer can appear as a symptom in another. The main skill is to identify the first failed dependency.

### Architecture / Mental Model

```text
Git / Inventory / /etc/kolla
            |
       Kolla Ansible
            |
       Linux Hosts
            |
    Container Runtime
            |
 OpenStack Services
   /       |       \
 DB       MQ      API/VIP
            |
  Compute / Network / Storage
            |
       Tenant Workload
```

### Commands / Configuration

```bash
openstack token issue
openstack server list
openstack network list
openstack volume list
```

### Expected Result

The output must match the intended inventory, node role, OpenStack release, project/region, and service state. For a production-ready result, validate not only that a container/process is up but that an authenticated API call and the relevant tenant data-plane transaction succeed.

### Why It Works

Kolla Ansible is declarative orchestration around a distributed OpenStack system. It can create containers and configuration consistently, but the running cloud still depends on databases, message queues, network paths, hypervisors, storage backends, certificates, DNS, NTP, and physical infrastructure.

### Real Production Example

A controller may show every container as `Up`, yet Nova server builds remain in `BUILD` because RabbitMQ has entered a disk alarm. The correct response is to find the messaging failure rather than restart every Nova container. The same dependency approach applies to **Change validation matrix**.

### Troubleshooting Workflow

```text
User symptom
  ↓
Capture exact command/resource/request ID
  ↓
Identify owning service
  ↓
API/VIP/HAProxy?
  ↓
DB / MQ?
  ↓
scheduler/controller/worker?
  ↓
compute/network/storage realization?
  ↓
physical/backend dependency?
  ↓
Correct smallest failed layer
  ↓
Repeat original user transaction
```

### Operational Safety

- Keep `/etc/kolla/passwords.yml`, SSH keys, TLS keys, and admin credentials out of normal Git.
- Never run `destroy` or broad `stop` as a troubleshooting experiment.
- Preserve DB/MQ quorum during controller maintenance.
- Disable scheduling before compute maintenance.
- Back up state before upgrades.
- Collect evidence before restart.

### Best Practices

- Version-control inventory and non-secret desired configuration.
- Use prechecks as a hard gate.
- Run a repeatable smoke test after deploy/reconfigure/upgrade.
- Capacity-plan failure and maintenance states.
- Record request IDs in incidents.
- Rehearse recovery before production emergencies.

---


# Enhanced OpenStack Deployment and Operations Labs

## Enhanced Lab 1 — Kolla and Kolla Ansible operating model

**Objective:** operate and troubleshoot **Kolla and Kolla Ansible operating model** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible --version
ansible -i ./multinode all -m ping
kolla-ansible prechecks -i ./multinode
docker ps
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 2 — Deployment node security

**Objective:** operate and troubleshoot **Deployment node security** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ls -l /etc/kolla
stat ~/.ssh/id_ed25519
git status
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 3 — All-in-one versus multinode

**Objective:** operate and troubleshoot **All-in-one versus multinode** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ansible-inventory -i ./multinode --graph 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 4 — Controller role

**Objective:** operate and troubleshoot **Controller role** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
docker ps | grep -E 'keystone|nova|neutron|glance|cinder|mariadb|rabbit|haproxy'
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 5 — Compute role

**Objective:** operate and troubleshoot **Compute role** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack compute service list
openstack hypervisor list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 6 — Network/gateway role

**Objective:** operate and troubleshoot **Network/gateway role** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack network agent list 2>/dev/null || true
openstack router list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 7 — Storage role

**Objective:** operate and troubleshoot **Storage role** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack volume service list
openstack volume type list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 8 — Management/API network

**Objective:** operate and troubleshoot **Management/API network** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ip -br addr
ip route
getent hosts controller01
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 9 — Overlay/tunnel network

**Objective:** operate and troubleshoot **Overlay/tunnel network** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ip -d link
ip route
ping -M do -s <size> <peer> 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 10 — Storage network

**Objective:** operate and troubleshoot **Storage network** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ip -br addr
ip route
ss -ntp | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 11 — Provider/external network

**Objective:** operate and troubleshoot **Provider/external network** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack network show public
ovs-vsctl show
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 12 — Physical NIC and VLAN planning

**Objective:** operate and troubleshoot **Physical NIC and VLAN planning** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ip -br link
ip -d link
ethtool <iface> 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 13 — MTU planning

**Objective:** operate and troubleshoot **MTU planning** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ip link show
ping -M do -s <size> <peer> 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 14 — DNS and NTP

**Objective:** operate and troubleshoot **DNS and NTP** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
getent hosts controller01
chronyc sources -v
timedatectl
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 15 — Python virtual environment

**Objective:** operate and troubleshoot **Python virtual environment** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
python3 -m venv ~/venvs/kolla
source ~/venvs/kolla/bin/activate
python -m pip list | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 16 — Stable Kolla Ansible installation

**Objective:** operate and troubleshoot **Stable Kolla Ansible installation** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
pip show kolla-ansible 2>/dev/null || true
kolla-ansible --version
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 17 — /etc/kolla structure

**Objective:** operate and troubleshoot **/etc/kolla structure** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
find /etc/kolla -maxdepth 2 -type f | sort | head -100
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 18 — Inventory as architecture-as-code

**Objective:** operate and troubleshoot **Inventory as architecture-as-code** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ansible-inventory -i ./multinode --graph 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 19 — Ansible reachability

**Objective:** operate and troubleshoot **Ansible reachability** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ansible -i ./multinode all -m ping
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 20 — globals.yml

**Objective:** operate and troubleshoot **globals.yml** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
grep -vE '^\s*(#|$)' /etc/kolla/globals.yml 2>/dev/null | head -100
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 21 — globals.d modular configuration

**Objective:** operate and troubleshoot **globals.d modular configuration** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
find /etc/kolla/globals.d -maxdepth 1 -type f -print 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 22 — passwords.yml lifecycle

**Objective:** operate and troubleshoot **passwords.yml lifecycle** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
stat /etc/kolla/passwords.yml 2>/dev/null || true
sha256sum /etc/kolla/passwords.yml 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 23 — kolla-genpwd

**Objective:** operate and troubleshoot **kolla-genpwd** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-genpwd
chmod 600 /etc/kolla/passwords.yml
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 24 — install-deps

**Objective:** operate and troubleshoot **install-deps** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible install-deps
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 25 — bootstrap-servers

**Objective:** operate and troubleshoot **bootstrap-servers** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible bootstrap-servers -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 26 — prechecks

**Objective:** operate and troubleshoot **prechecks** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible prechecks -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 27 — Image pull and local registry

**Objective:** operate and troubleshoot **Image pull and local registry** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible pull -i ./multinode
docker images | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 28 — deploy convergence

**Objective:** operate and troubleshoot **deploy convergence** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible deploy -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 29 — post-deploy and clouds.yaml

**Objective:** operate and troubleshoot **post-deploy and clouds.yaml** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible post-deploy -i ./multinode
export OS_CLOUD=admin
openstack token issue
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 30 — Service catalog validation

**Objective:** operate and troubleshoot **Service catalog validation** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack service list
openstack endpoint list
openstack catalog list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 31 — Keystone smoke test

**Objective:** operate and troubleshoot **Keystone smoke test** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack token issue
openstack project list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 32 — Glance smoke test

**Objective:** operate and troubleshoot **Glance smoke test** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack image list
openstack image show <image>
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 33 — Nova smoke test

**Objective:** operate and troubleshoot **Nova smoke test** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack compute service list
openstack hypervisor list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 34 — Placement and NoValidHost

**Objective:** operate and troubleshoot **Placement and NoValidHost** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack hypervisor list
openstack flavor show <flavor>
openstack aggregate list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 35 — Neutron smoke test

**Objective:** operate and troubleshoot **Neutron smoke test** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack network list
openstack subnet list
openstack router list
openstack port list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 36 — Provider network bridge mapping

**Objective:** operate and troubleshoot **Provider network bridge mapping** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack network show public
ovs-vsctl show
ip -br link
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 37 — OVN architecture

**Objective:** operate and troubleshoot **OVN architecture** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ovn-nbctl show 2>/dev/null || true
ovn-sbctl show 2>/dev/null || true
ovs-vsctl show
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 38 — Port binding

**Objective:** operate and troubleshoot **Port binding** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack port show <port-id>
openstack port list --server <server-id>
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 39 — Floating IP path

**Objective:** operate and troubleshoot **Floating IP path** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack floating ip list
openstack router list
openstack port list --server <server>
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 40 — DHCP and metadata

**Objective:** operate and troubleshoot **DHCP and metadata** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack subnet show <subnet>
cloud-init status --long 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 41 — Compute maintenance

**Objective:** operate and troubleshoot **Compute maintenance** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack compute service set --disable compute01 nova-compute
openstack server list --host compute01 --all-projects 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 42 — Live migration, cold migration, evacuation

**Objective:** operate and troubleshoot **Live migration, cold migration, evacuation** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack server migrate <server> 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 43 — Add compute host

**Objective:** operate and troubleshoot **Add compute host** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack compute service list
openstack hypervisor list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 44 — Remove compute host

**Objective:** operate and troubleshoot **Remove compute host** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack compute service set --disable compute01 nova-compute
openstack server list --host compute01 --all-projects 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 45 — Host aggregates and availability zones

**Objective:** operate and troubleshoot **Host aggregates and availability zones** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack aggregate list
openstack availability zone list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 46 — Resource overcommit

**Objective:** operate and troubleshoot **Resource overcommit** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack hypervisor stats show 2>/dev/null || true
openstack quota show 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 47 — Glance backend and compute image cache

**Objective:** operate and troubleshoot **Glance backend and compute image cache** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack image list
df -h
du -sh /var/lib/nova/* 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 48 — Cinder operations

**Objective:** operate and troubleshoot **Cinder operations** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack volume service list
openstack volume list
openstack volume show <volume>
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 49 — External Ceph

**Objective:** operate and troubleshoot **External Ceph** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ceph -s 2>/dev/null || true
ceph df 2>/dev/null || true
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 50 — Kolla container inspection

**Objective:** operate and troubleshoot **Kolla container inspection** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
docker ps
docker inspect <container>
docker logs <container> | tail -100
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 51 — Kolla logs

**Objective:** operate and troubleshoot **Kolla logs** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
find /var/log/kolla -type f | head
grep -R 'req-' /var/log/kolla 2>/dev/null | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 52 — Evidence before restart

**Objective:** operate and troubleshoot **Evidence before restart** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
docker ps
openstack server show <server>
openstack --debug server show <server>
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 53 — genconfig

**Objective:** operate and troubleshoot **genconfig** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible genconfig -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 54 — validate-config

**Objective:** operate and troubleshoot **validate-config** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible validate-config -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 55 — reconfigure

**Objective:** operate and troubleshoot **reconfigure** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible reconfigure -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 56 — deploy-containers

**Objective:** operate and troubleshoot **deploy-containers** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible deploy-containers -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 57 — MariaDB/Galera HA

**Objective:** operate and troubleshoot **MariaDB/Galera HA** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
docker ps | grep mariadb
docker logs mariadb 2>/dev/null | tail -100
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 58 — MariaDB recovery

**Objective:** operate and troubleshoot **MariaDB recovery** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible mariadb-recovery -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 59 — RabbitMQ HA

**Objective:** operate and troubleshoot **RabbitMQ HA** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
docker ps | grep rabbit
docker logs rabbitmq 2>/dev/null | tail -100
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 60 — HAProxy health

**Objective:** operate and troubleshoot **HAProxy health** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
docker ps | grep haproxy
docker logs haproxy 2>/dev/null | tail -100
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 61 — Keepalived/VRRP health

**Objective:** operate and troubleshoot **Keepalived/VRRP health** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ip addr
ip neigh
docker logs keepalived 2>/dev/null | tail -100
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 62 — TLS lifecycle

**Objective:** operate and troubleshoot **TLS lifecycle** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openssl s_client -connect <vip>:443 -servername <fqdn> </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 63 — Service credential rotation

**Objective:** operate and troubleshoot **Service credential rotation** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
grep -R '<credential-key>' /etc/kolla 2>/dev/null | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 64 — Centralized logging and time

**Objective:** operate and troubleshoot **Centralized logging and time** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
chronyc sources -v
timedatectl
find /var/log/kolla -type f | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 65 — Request IDs

**Objective:** operate and troubleshoot **Request IDs** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack --debug server show <server>
grep -R 'req-' /var/log/kolla 2>/dev/null | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 66 — Capacity monitoring

**Objective:** operate and troubleshoot **Capacity monitoring** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack hypervisor stats show 2>/dev/null || true
openstack quota show 2>/dev/null || true
openstack floating ip list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 67 — In-series updates

**Objective:** operate and troubleshoot **In-series updates** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible prechecks -i ./multinode
kolla-ansible pull -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 68 — Cross-series upgrades

**Objective:** operate and troubleshoot **Cross-series upgrades** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible prechecks -i ./multinode
kolla-ansible upgrade -i ./multinode
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 69 — SLURP/skip-level upgrades

**Objective:** operate and troubleshoot **SLURP/skip-level upgrades** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
kolla-ansible --version
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 70 — Rollback reality

**Objective:** operate and troubleshoot **Rollback reality** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
ls -l /etc/kolla
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 71 — Backup scope

**Objective:** operate and troubleshoot **Backup scope** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
find /etc/kolla -maxdepth 2 -type f | sort | head
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 72 — DR restore order

**Objective:** operate and troubleshoot **DR restore order** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack service list
openstack compute service list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 73 — Daily and weekly operations

**Objective:** operate and troubleshoot **Daily and weekly operations** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack service list
openstack compute service list
openstack volume service list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 74 — Operational SLOs

**Objective:** operate and troubleshoot **Operational SLOs** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack --debug server list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---

## Enhanced Lab 75 — Change validation matrix

**Objective:** operate and troubleshoot **Change validation matrix** in a disposable or explicitly authorized OpenStack lab.

### Procedure
1. Record inventory, node role, release, and current change ticket/lab goal.
2. Capture the before-state and a topology/dependency diagram.
3. Run the read-only commands below.
4. Record relevant resource UUIDs, service states, container names, and request IDs.
5. Make only one controlled lab change if required.
6. Validate API state and real tenant behavior.
7. Restore the original state.
8. Re-run the validation transaction.
9. Record failure symptom, root cause, and prevention.
10. Add the final workflow to a runbook.

```bash
openstack token issue
openstack server list
openstack network list
openstack volume list
```

**Safety:** do not run destructive Kolla actions, edit OpenStack databases manually, stop all quorum members, or wipe compute/storage hosts outside a disposable lab.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Design the Deployment Topology

Create a diagram for:

```text
1 deployment node
3 controllers
2 computes
1 storage system
```

Mark every control-plane and data-plane dependency.

### Lab 2 — Build the Network Plan

Document:

```text
management/API
overlay
storage
external/provider
VIP
DNS
NTP
MTU
VLANs
```

### Lab 3 — Install Kolla Ansible

```bash
python3 -m venv ~/venvs/kolla
source ~/venvs/kolla/bin/activate
pip install -U pip

pip install --upgrade \
  git+https://opendev.org/openstack/kolla-ansible@stable/2026.1

kolla-ansible install-deps
```

### Lab 4 — Build and Test Inventory

Create `multinode`, then:

```bash
ansible -i ./multinode all -m ping
```

Fix every failed node before proceeding.

### Lab 5 — Configure `/etc/kolla`

Create:

```text
globals.yml
passwords.yml
```

Set your real lab interfaces and VIP.

### Lab 6 — Generate and Protect Passwords

```bash
kolla-genpwd
chmod 600 /etc/kolla/passwords.yml
```

Create an encrypted backup plan.

### Lab 7 — Bootstrap Hosts

```bash
kolla-ansible bootstrap-servers -i ./multinode
```

Record which host-level changes were made.

### Lab 8 — Run Prechecks

```bash
kolla-ansible prechecks -i ./multinode
```

Intentionally break one lab prerequisite, observe the failure, then fix it.

### Lab 9 — Pull and Deploy

```bash
kolla-ansible pull -i ./multinode
kolla-ansible deploy -i ./multinode
```

Record failed/retried tasks and container counts.

### Lab 10 — Post Deploy and Validate Identity

```bash
kolla-ansible post-deploy -i ./multinode
export OS_CLOUD=admin

openstack token issue
openstack service list
openstack endpoint list
```

### Lab 11 — Build Initial Cloud Resources

Create manually:

```text
image
flavor
private network
subnet
router
external network
security group
keypair
VM
floating IP
```

### Lab 12 — HA VIP Test

In an HA lab:

1. identify VIP owner;
2. fail the active controller safely;
3. verify VIP moves;
4. validate APIs;
5. restore node.

### Lab 13 — HAProxy Backend Failure

Stop one API backend only in the lab.

Confirm:

```text
HAProxy marks it unhealthy
VIP/API remains available
```

### Lab 14 — Inspect Containers and Logs

```bash
docker ps
docker logs <container>
ls -R /var/log/kolla | head
```

Build a service-to-container/log map.

### Lab 15 — Compute Maintenance

1. disable `nova-compute`;
2. migrate lab workloads;
3. reboot;
4. validate network/libvirt/nova;
5. re-enable.

### Lab 16 — Add a Compute Node

Add it to inventory, bootstrap/deploy it, then verify:

```bash
openstack compute service list
openstack hypervisor list
```

### Lab 17 — Neutron Provider-Network Failure

Break one lab bridge/interface mapping and trace why floating IP connectivity fails. Restore and document.

### Lab 18 — Port Binding Failure

Create a controlled Neutron host/backend mismatch.

Inspect:

```bash
openstack port show <PORT_ID>
```

Correlate Nova and Neutron logs.

### Lab 19 — Cinder Volume Lifecycle

```bash
openstack volume create --size 5 testvol
openstack server add volume vm01 testvol
openstack server remove volume vm01 testvol
openstack volume delete testvol
```

### Lab 20 — Glance and Image Cache

Upload two images, launch repeated VMs, and observe backend/cache behavior.

### Lab 21 — Generate and Validate Configuration

```bash
kolla-ansible genconfig -i ./multinode
kolla-ansible validate-config -i ./multinode
```

Review generated changes before apply.

### Lab 22 — Reconfigure

Apply one harmless lab configuration change:

```bash
kolla-ansible reconfigure -i ./multinode
```

Run API health checks afterward.

### Lab 23 — RabbitMQ Failure Tabletop

Simulate one RabbitMQ-node outage and document:

```text
cluster status
queue behavior
API/backend symptoms
recovery
```

### Lab 24 — MariaDB Failure Tabletop

Stop one DB node in a disposable lab. Observe quorum/service behavior and explain why all nodes must not be stopped casually.

### Lab 25 — Capacity Dashboard

Build a table/dashboard for:

```text
vCPU
RAM
Placement
Cinder capacity
Ceph capacity
floating IPs
ports
API latency
DB/MQ health
```

### Lab 26 — Upgrade Plan

Write a staged plan covering:

```text
release notes
backup
Kolla tooling
inventory diff
password merge
pull
prechecks
upgrade
validation
rollback/recovery
```

### Lab 27 — Backup and Recovery Plan

Protect:

```text
/etc/kolla
passwords
SQL
TLS
custom configs
images
volumes
external storage
```

Define restore order.

### Lab 28 — Operations Troubleshooting Challenge

Analyze:

1. Keystone 401.
2. Keystone 403.
3. API VIP unreachable.
4. HAProxy backend down.
5. RabbitMQ blocked.
6. MariaDB degraded.
7. `NoValidHost`.
8. instance `ERROR`.
9. Neutron port binding failure.
10. floating IP unreachable.
11. Cinder attachment failure.
12. Glance upload failure.
13. compute service down.
14. overlay network failure.
15. certificate expiry.

For each:

```text
Symptom
Dependency Chain
Evidence
Root Cause
Correction
Verification
Prevention
```

---

## 6. Mini Project

# Mini Project — Production-Style OpenStack Private Cloud

Design or build:

```text
3 Controllers
3 Computes
1 Deployment Node
Cinder or external Ceph
HA API VIP
Provider + Overlay networking
```

Architecture:

```text
                        Users / APIs
                            |
                           VIP
                            |
                        HAProxy
                            |
           +----------------+----------------+
           |                |                |
      Controller01     Controller02     Controller03
           |                |                |
           +------- MariaDB / RabbitMQ ------+
                            |
                 +----------+----------+
                 |                     |
              Compute01             Compute02
                 |                     |
              KVM/OVN               KVM/OVN
                 \                     /
                  +------ Storage ----+
```

Required services:

```text
Keystone
Glance
Nova
Placement
Neutron
Cinder
Horizon
Heat
```

Deliverables:

```text
README.md
ARCHITECTURE.md
INVENTORY
GLOBALS/
NETWORK_PLAN.md
STORAGE_PLAN.md
HA.md
SECURITY.md
CAPACITY.md
BACKUP.md
MONITORING.md
UPGRADE.md
RUNBOOKS/
```

Required runbooks:

```text
RUNBOOK_API_DOWN.md
RUNBOOK_DB_FAILURE.md
RUNBOOK_RABBITMQ.md
RUNBOOK_COMPUTE_FAILURE.md
RUNBOOK_NOVALIDHOST.md
RUNBOOK_NEUTRON.md
RUNBOOK_FLOATING_IP.md
RUNBOOK_CINDER.md
RUNBOOK_UPGRADE.md
RUNBOOK_DR.md
```

---


# Expanded Capstone — Production-Style Kolla Ansible OpenStack Cloud

Design or build:

```text
Deployment01
Controller01 / Controller02 / Controller03
Compute01 / Compute02 / Compute03
External Ceph or resilient Cinder backend
Redundant provider-network connectivity
```

Required network planes:

```text
Out-of-Band
Management/API
Overlay/Tunnel
Storage
Provider/External
```

Required repository:

```text
openstack-kolla-config/
├── inventory/
│   ├── staging
│   └── production
├── globals.d/
│   ├── 10-network.yml
│   ├── 20-storage.yml
│   ├── 30-security.yml
│   └── 40-monitoring.yml
├── overrides/
├── docs/
└── runbooks/
```

Do not commit `passwords.yml`, private keys, or production credentials.

Build automated validation for:

```text
Keystone token
catalog/endpoints
Glance image
Nova compute/Placement
Neutron network/subnet/router/port
VM BUILD→ACTIVE
floating IP path
Cinder create/attach/detach
cloud-init metadata
```

Required failure tests:

```text
one controller down
VIP failover
one HAProxy backend down
Galera quorum loss tabletop
RabbitMQ disk alarm tabletop
one compute down
NoValidHost
Neutron port binding failure
provider network mapping failure
overlay MTU failure
Cinder backend failure
Ceph latency
TLS expiry tabletop
upgrade failure/recovery
```

For each failure, document:

```text
symptom
request ID
control plane affected
data plane affected
automatic behavior
operator action
rollback/recovery
verification
remaining risk
```


## 7. Recommended Resources

This course is designed to be self-contained for learning and lab work. For production, use the documentation matching the exact installed release.

Relevant official documentation families:

```text
OpenStack 2026.1 Installation Guides
OpenStack 2026.1 Administrator Guides
Kolla Ansible 2026.1
Kolla Quick Start
Kolla Multinode Deployment
Operating Kolla
Kolla Security
Nova Administration
Neutron Administration
Cinder Administration
Glance Administration
Keystone Administration
```

---

## 8. Certification Relevance

Relevant to:

```text
OpenStack Administrator
Private Cloud Engineer
Cloud Infrastructure Engineer
Platform Engineer
Linux Engineer
DevOps Engineer
SRE
Network Cloud Engineer
Storage Cloud Engineer
```

This course is the direct operational prerequisite for **43. OpenStack APIs**.

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Treat OpenStack as one service.  
  **Best practice:** follow the service dependency chain.

- **Mistake:** Deploy before DNS/NTP/network planning.  
  **Best practice:** make infrastructure correctness a precondition.

- **Mistake:** Ignore Kolla prechecks.  
  **Best practice:** fix the failed prerequisite.

- **Mistake:** Commit `passwords.yml`.  
  **Best practice:** keep secrets outside ordinary source control.

- **Mistake:** Use `destroy` during troubleshooting.  
  **Best practice:** understand that it is destructive.

- **Mistake:** Restart every container.  
  **Best practice:** identify whether the fault is API, DB, MQ, network, storage, or compute.

- **Mistake:** Diagnose `NoValidHost` as "Nova is down."  
  **Best practice:** inspect Placement, capacity, traits, and scheduling policy.

- **Mistake:** Use Horizon as the only health check.  
  **Best practice:** validate service APIs directly.

- **Mistake:** Treat floating IP as only a Neutron object.  
  **Best practice:** trace through provider network, NAT, security, and physical routing.

- **Mistake:** Patch all controllers simultaneously.  
  **Best practice:** preserve quorum and control-plane HA.

- **Mistake:** Cross-series upgrade without state backup.  
  **Best practice:** protect DB/config/secrets/certs and test upgrade first.

- **Mistake:** Back up only controllers.  
  **Best practice:** protect tenant images, volumes, and external storage too.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Kolla vs Kolla Ansible?

**Short answer:** Kolla provides service container images; Kolla Ansible deploys and operates them with Ansible.

### Q2. All-in-one vs multinode?

**Short answer:** All-in-one places roles on one host for evaluation; multinode separates roles for scale/HA.

### Q3. What runs on a controller?

**Short answer:** APIs, schedulers/control services, and typically HA/DB/message-queue components.

### Q4. What runs on a compute node?

**Short answer:** `nova-compute`, libvirt/KVM, and networking dataplane components.

### Q5. Why does Kolla use an external interface?

**Short answer:** To connect Neutron provider/external networks to the physical network.

### Q6. What is the internal VIP?

**Short answer:** A floating service endpoint address used for highly available APIs.

### Q7. Keepalived vs HAProxy?

**Short answer:** Keepalived provides VIP ownership/failover; HAProxy distributes traffic to healthy API backends.

### Q8. What is `globals.yml`?

**Short answer:** Main Kolla Ansible deployment configuration.

### Q9. What is `passwords.yml`?

**Short answer:** Sensitive generated service credentials for the deployment.

### Q10. What does `kolla-genpwd` do?

**Short answer:** Generates Kolla service passwords/secrets.

### Q11. What does `bootstrap-servers` do?

**Short answer:** Prepares target hosts with deployment prerequisites.

### Q12. What do `prechecks` do?

**Short answer:** Validate that hosts/configuration satisfy deployment requirements.

### Q13. What does `deploy` do?

**Short answer:** Deploys and starts configured OpenStack service containers.

### Q14. What does `post-deploy` do?

**Short answer:** Creates post-deployment client configuration such as `clouds.yaml`.

### Q15. What is Placement?

**Short answer:** Resource inventory/allocation service used by Nova scheduling.

### Q16. What is `NoValidHost`?

**Short answer:** No compute host satisfied the requested resources and scheduling constraints.

### Q17. What is port binding?

**Short answer:** Neutron mapping a logical port to a concrete host/dataplane.

### Q18. What is Cells v2?

**Short answer:** Nova architecture dividing compute infrastructure into cells for scale/failure isolation.

### Q19. What does `reconfigure` do?

**Short answer:** Applies changed OpenStack service configuration.

### Q20. What does `genconfig` do?

**Short answer:** Generates service configuration without applying it.

### Q21. What does `validate-config` do?

**Short answer:** Validates generated service configuration.

### Q22. Why are RabbitMQ and MariaDB critical?

**Short answer:** RabbitMQ carries service RPC/messages; MariaDB stores most control-plane state.

### Q23. 401 vs 403?

**Short answer:** 401 is authentication failure; 403 is authorization denial after identity is known.

### Q24. Why isn't a controller VM snapshot a complete backup?

**Short answer:** Tenant data and control-plane state also exist in DBs, secrets, images, volumes, and external storage.

### Q25. What is the best troubleshooting method?

**Short answer:** Trace the user request through identity, API, DB/MQ, scheduler/control service, and the compute/network/storage dataplane.

---

# Expanded Self-Assessment Bank

### Q1. Kolla vs Kolla Ansible?
**Answer:** Kolla provides images; Kolla Ansible deploys/operates them.

### Q2. Why protect the deployment node?
**Answer:** It has cloud-wide SSH/configuration/secret privileges.

### Q3. What is controller role?
**Answer:** APIs, control services, HA endpoints, DB, and MQ.

### Q4. What is compute role?
**Answer:** nova-compute, KVM/libvirt, and network dataplane.

### Q5. Why separate network planes?
**Answer:** Security, performance, troubleshooting, and failure-domain control.

### Q6. What does Keepalived do?
**Answer:** VIP ownership/failover.

### Q7. What does HAProxy do?
**Answer:** API load balancing and backend health selection.

### Q8. Why can VIP exist while API is unavailable?
**Answer:** All service backends may be unhealthy.

### Q9. Why is Galera quorum critical?
**Answer:** Most services need consistent SQL state.

### Q10. Why is RabbitMQ critical?
**Answer:** It carries distributed RPC and asynchronous work.

### Q11. What can RabbitMQ disk alarm cause?
**Answer:** Publishers block and cloud operations stall.

### Q12. Why doesn't docker ps prove health?
**Answer:** Container state is not end-to-end service health.

### Q13. Why avoid manual edits inside containers?
**Answer:** They are ephemeral and fight desired-state automation.

### Q14. What is globals.d?
**Answer:** Modular Kolla global configuration.

### Q15. Why is passwords.yml persistent state?
**Answer:** Running service credentials depend on it.

### Q16. What does bootstrap-servers do?
**Answer:** Prepares target hosts.

### Q17. Why fix prechecks before continuing?
**Answer:** They detect invalid prerequisites before partial deployment.

### Q18. Why pre-pull images?
**Answer:** Reduce change-window registry/network risk.

### Q19. Why rerun deploy after fixing root cause?
**Answer:** Kolla/Ansible converges desired state.

### Q20. What does post-deploy provide?
**Answer:** Client configuration such as clouds.yaml.

### Q21. What is a good smoke test?
**Answer:** An authenticated end-to-end resource create/network/boot/connect/storage transaction.

### Q22. What is NoValidHost?
**Answer:** Scheduler found no host satisfying all constraints.

### Q23. What is port binding?
**Answer:** Mapping a Neutron port to a concrete host/dataplane.

### Q24. Why is physnet mapping important?
**Answer:** It connects logical provider networks to real NIC/VLAN paths.

### Q25. Why does MTU matter?
**Answer:** Overlay encapsulation adds overhead.

### Q26. Why disable compute scheduling before maintenance?
**Answer:** Prevent new placement while draining.

### Q27. Live vs cold migration?
**Answer:** Running migration vs migration with downtime.

### Q28. What is evacuation?
**Answer:** Failed-compute recovery on another host.

### Q29. What must be tested on a new compute?
**Answer:** Nova/Placement, KVM, Neutron, storage, and a real VM.

### Q30. What is safe compute decommission order?
**Answer:** Disable, drain, verify zero VMs, remove state/inventory, wipe securely.

### Q31. Why can Glance API be healthy while builds fail?
**Answer:** Compute image cache/local disk or backend path can fail.

### Q32. Why can Cinder service be up while volume operations fail?
**Answer:** Real storage backend or compute connector can be broken.

### Q33. Why monitor Ceph independently?
**Answer:** It is a separate distributed system.

### Q34. Why capture request IDs?
**Answer:** Trace one transaction through Kolla logs.

### Q35. Why collect evidence before restart?
**Answer:** Restart can hide root cause or only mask dependency failures.

### Q36. What does genconfig do?
**Answer:** Renders config without applying.

### Q37. What does validate-config do?
**Answer:** Validates generated configuration.

### Q38. What does reconfigure do?
**Answer:** Applies configuration changes.

### Q39. What does deploy-containers do?
**Answer:** Reconciles containers without regenerating service config.

### Q40. Why is TLS lifecycle important?
**Answer:** Cert failure can break every API client.

### Q41. Why is credential rotation coordinated?
**Answer:** Many distributed consumers use the same internal secret.

### Q42. Quota vs capacity?
**Answer:** Tenant governance vs actual resource availability.

### Q43. Why can aggregate free RAM be misleading?
**Answer:** No single eligible host may satisfy a large/specialized request.

### Q44. In-series update vs cross-series upgrade?
**Answer:** Same release family refresh vs release/schema/RPC transition.

### Q45. What is SLURP?
**Answer:** Documented skip-level upgrade path for designated releases.

### Q46. Why can rollback be difficult?
**Answer:** Database migrations may be incompatible with old service containers.

### Q47. What must backup include?
**Answer:** Kolla config/secrets/SQL/TLS and tenant/back-end data.

### Q48. What is the correct DR mindset?
**Answer:** Restore verified dependencies in order, then tenant services.

### Q49. Why validate Horizon separately?
**Answer:** It is only a web client.

### Q50. What is the core operator troubleshooting chain?
**Answer:** API/VIP→DB/MQ→scheduler/controller→compute/network/storage→physical backend.


## Completion Checklist

- [ ] I understand all-in-one and multinode deployment.
- [ ] I understand controller/compute/network/storage roles.
- [ ] I can design management/overlay/storage/provider networks.
- [ ] I understand Kolla inventory and `/etc/kolla`.
- [ ] I understand VIP + Keepalived + HAProxy.
- [ ] I can run bootstrap/prechecks/pull/deploy/post-deploy.
- [ ] I can validate core OpenStack services.
- [ ] I understand Cells v2 and Placement.
- [ ] I can plan compute maintenance/add/remove.
- [ ] I understand OVN/OVS and port binding.
- [ ] I can troubleshoot floating IP/provider networks.
- [ ] I understand Glance/Cinder/Ceph operations.
- [ ] I can inspect containers and logs.
- [ ] I understand reconfigure/genconfig/validate-config.
- [ ] I understand DB/RabbitMQ HA.
- [ ] I understand TLS/secrets/RBAC.
- [ ] I understand updates/upgrades and SLURP concepts.
- [ ] I understand backup and DR scope.
- [ ] I can troubleshoot major OpenStack failures.
- [ ] I completed all 28 labs.
- [ ] I completed the Production-Style OpenStack Private Cloud project.
