# Phase 5 — Linux System Administration

This phase follows Phase 4 — Networking and begins the Linux administration path.

## Phase 5 Course Order

1. **20. Linux Essentials**
2. **21. Red Hat System Administration I**
3. **22. Red Hat System Administration II**
4. **23. Red Hat System Administration III**
5. **24. Linux Web Server Administration**
6. **25. Red Hat High Availability Clustering**

## Dependency Flow

```text
20. Linux Essentials
        ↓
21. Red Hat System Administration I
        ↓
22. Red Hat System Administration II
        ↓
23. Red Hat System Administration III
        ↓
24. Linux Web Server Administration
        ↓
25. Red Hat High Availability Clustering
```

## Current Generated Material

- [x] 20. Linux Essentials
- [x] 21. Red Hat System Administration I
- [x] 22. Red Hat System Administration II
- [x] 23. Red Hat System Administration III
- [x] 24. Linux Web Server Administration
- [x] 25. Red Hat High Availability Clustering

**Phase 5 is now complete.**


## Why Linux Comes After Networking

A Linux server is rarely isolated.

As soon as Linux is used in Cloud, DevOps, Cybersecurity, Kubernetes, or enterprise infrastructure, the administrator must understand:

- IP addressing
- routes
- DNS
- ports
- TCP/UDP
- SSH
- firewalls
- services
- logs
- web servers
- storage
- permissions
- process management

The networking knowledge from Phase 4 will therefore be used repeatedly throughout Phase 5.

## Recommended Lab Environment

Use one of the following:

- RHEL-compatible Linux VM
- Rocky Linux
- AlmaLinux
- CentOS Stream
- Fedora
- Ubuntu for comparison

Because later courses are Red Hat oriented, a **RHEL-compatible VM** is recommended for the primary lab.

Suggested VM:

```text
CPU:      2 vCPU
Memory:   4 GB
Disk:     30–40 GB
Network:  NAT + optional Host-Only adapter
User:     non-root admin account with sudo access
```

## Study Method

Do not read Linux material passively.

For every topic:

1. Read the explanation.
2. Run the commands.
3. Inspect the output.
4. Change something deliberately.
5. Observe the effect.
6. Break the configuration in a safe VM.
7. Recover it.
8. Explain the result in your own words.
9. Save useful commands in your notes.
10. Never memorize a command without understanding what it changes.

## Important Safety Rule

Run destructive commands only in a disposable VM or clearly controlled lab.

Commands such as:

```bash
rm -rf
dd
mkfs
fdisk
parted
lvremove
vgremove
userdel -r
chmod -R
chown -R
```

can destroy data or make a system unusable if used incorrectly.

Always verify:

```bash
pwd
ls
lsblk
findmnt
```

before making destructive changes.

## Exit Criteria for Linux Essentials

Before moving to Red Hat System Administration I, you should be able to:

- navigate the Linux filesystem confidently;
- explain `/`, `/home`, `/etc`, `/var`, `/usr`, `/tmp`, `/boot`, `/dev`, `/proc`, and `/sys`;
- create, move, copy, inspect, search, and delete files safely;
- use pipes and redirection;
- manage users, groups, ownership, and permissions at a basic level;
- explain processes, jobs, signals, and services;
- install and query packages;
- inspect disks, filesystems, mounts, memory, and CPU;
- configure and troubleshoot basic IPv4 networking;
- use SSH securely;
- inspect logs and the system journal;
- schedule simple commands;
- write small Bash administration scripts;
- perform basic troubleshooting using evidence rather than random commands.

## Current Red Hat Training Alignment

As of August 2026:

- Red Hat System Administration I (RH124) is based on Red Hat Enterprise Linux 10.0.
- Red Hat System Administration II (RH134) is based on Red Hat Enterprise Linux 10.0.
- The modern automation-stage course is Red Hat Enterprise Linux Automation with Ansible (AU294/RH294 path), based on RHEL 10 and Ansible Core 2.16 with development tooling aligned to Red Hat Ansible Automation Platform 2.5 and 2.6.

This curriculum preserves the requested name **23. Red Hat System Administration III** and treats it as the Linux Automation with Ansible stage.

## Completed Phase 5 Dependency Flow

```text
20. Linux Essentials
        ↓
21. Red Hat System Administration I
        ↓
22. Red Hat System Administration II
        ↓
23. Red Hat System Administration III
        ↓
24. Linux Web Server Administration
        ↓
25. Red Hat High Availability Clustering
```

## Phase 5 Capstone Recommendation

Combine the material into one lab environment:

```text
Ansible Control Node
        |
        +------ node1 ----+
        |                 |
        +------ node2 ----+---- Pacemaker HA Web Service
                          |
                     Shared Storage
                          |
                       Client
```

The capstone should demonstrate:

- Linux baseline configuration
- users/groups/permissions
- DNF and systemd
- NetworkManager
- SSH key management
- SELinux
- firewalld
- LVM/storage
- Bash automation
- Ansible automation
- Apache/NGINX
- TLS
- reverse proxying
- Pacemaker/Corosync
- quorum
- fencing
- active/passive service failover
- troubleshooting and runbooks

