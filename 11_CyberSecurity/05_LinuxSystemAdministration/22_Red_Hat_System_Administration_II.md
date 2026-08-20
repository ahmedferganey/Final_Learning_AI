# 22. Red Hat System Administration II

> Phase 5 — Linux System Administration

Red Hat System Administration II moves from routine single-server administration into the deeper tasks expected of a full Linux administrator.

The current Red Hat RH134 course is based on **Red Hat Enterprise Linux 10.0** and includes:

- shell scripting and regular expressions,
- user and system scheduling,
- logging,
- SELinux,
- archives and secure file transfer,
- performance tuning,
- partitions/filesystems/swap,
- LVM,
- boot troubleshooting and root recovery,
- firewalld and SELinux network policy,
- NFS and automount,
- RHEL installation/Kickstart,
- Podman containers,
- image-based RHEL concepts.

This module expands those topics with commands, configuration examples, failure scenarios, and a larger system-administration project.
## 1. Topic Title

**Red Hat System Administration II**

## 2. Learning Objectives

- Write reliable Bash administration scripts using conditionals, loops, functions, regex, and exit-status handling.
- Schedule user and system tasks using cron, at-style concepts where available, and systemd timers.
- Analyze persistent logs and maintain correct system time.
- Diagnose and manage SELinux contexts, booleans, labels, and denials.
- Create and transfer compressed archives securely.
- Tune systems using tuned profiles, priorities, and evidence-based performance inspection.
- Partition additional disks, create filesystems and swap, and configure persistent mounts.
- Create, extend, and manage LVM storage safely.
- Control and troubleshoot the boot process and recover administrative access in a lab.
- Configure firewalld and coordinate network security with SELinux port policy.
- Mount NFS storage manually and through automount.
- Understand RHEL package-mode installation, Kickstart automation, Podman containers, and image-based RHEL concepts.

## 3. Prerequisites

Required:

- 20. Linux Essentials
- 21. Red Hat System Administration I
- Strong command-line confidence
- Users/groups/permissions
- systemd
- NetworkManager
- RPM/DNF
- SSH

Recommended lab additions:

```text
VM 1: rhel-admin01
VM 2: rhel-server02
Extra disk: 10–20 GB attached to VM 1
Private lab network between both VMs
```

All disk-partitioning, boot-recovery, and firewall experiments should be performed only in disposable or snapshotted lab VMs.
## 4. Core Concepts Explanation

# Part 1 — Shell Scripting and Command-Line Automation

### Script Structure

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

main() {
    echo "Host: $(hostname)"
    echo "Date: $(date --iso-8601=seconds)"
}

main "$@"
```
A production-oriented shell script should have:

- clear inputs,
- predictable output,
- explicit error handling,
- functions for coherent tasks,
- safe quoting,
- meaningful exit codes,
- no embedded secrets.
### Positional Parameters

```bash
#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <service>" >&2
    exit 2
fi

SERVICE=$1

systemctl status "$SERVICE"
```
### Conditionals

```bash
if systemctl is-active --quiet sshd; then
    echo "sshd is active"
else
    echo "sshd is not active"
fi
```
### Loops

```bash
for service in sshd crond NetworkManager; do
    if systemctl is-active --quiet "$service"; then
        printf '%-20s %s
' "$service" "active"
    else
        printf '%-20s %s
' "$service" "inactive"
    fi
done
```
### Functions and Return Codes

```bash
check_file() {
    local path=$1

    if [[ -r "$path" ]]; then
        return 0
    fi

    return 1
}

if check_file /etc/hosts; then
    echo "Readable"
else
    echo "Not readable" >&2
fi
```
# Part 2 — Regular Expressions for Administration

```bash
grep '^root:' /etc/passwd
grep -E '^(sshd|chronyd|crond)' services.txt
grep -E '^[0-9]{1,3}(\.[0-9]{1,3}){3}$' addresses.txt
```
Regular expressions match text patterns, not semantic data correctness.

For example, a regex that matches:

```text
999.999.999.999
```

does not prove it is a valid IPv4 address.

Use regex to find candidate text, then apply semantic validation where needed.
### sed and awk for Administration

```bash
sed -n '1,10p' /etc/passwd

awk -F: '{print $1, $3, $7}' /etc/passwd | head

df -P | awk 'NR>1 {print $5, $6}'
```
Use `awk` when field-oriented processing becomes awkward with repeated `cut`/`grep`.

Do not edit critical configuration with complex one-liners until the transformation is tested on a copy.
# Part 3 — Scheduling User Tasks

```bash
crontab -e
crontab -l
```
```cron
# Run a user report every day at 06:30
30 6 * * * /home/student/bin/report.sh >> /home/student/report.log 2>&1
```
Cron has a minimal environment compared with your interactive shell.

Therefore:
- use absolute paths,
- set required environment explicitly,
- redirect output,
- make scripts executable,
- test scripts manually first.
### One-Time Scheduling Concept

```bash
command -v at || true
```
Some RHEL environments may provide `at` for one-time jobs when the package/service is installed.

Always verify availability and organizational policy.
# Part 4 — Scheduling System Tasks

### systemd Timer Example

```ini
# /etc/systemd/system/health-report.service
[Unit]
Description=Generate health report

[Service]
Type=oneshot
ExecStart=/usr/local/sbin/health-report.sh
```
```ini
# /etc/systemd/system/health-report.timer
[Unit]
Description=Run health report every hour

[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
Persistent=true

[Install]
WantedBy=timers.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now health-report.timer

systemctl list-timers
systemctl status health-report.timer
```
systemd timers integrate with:
- dependencies,
- journal logging,
- service execution state.

Use them where they fit the operational model.
# Part 5 — Analyzing and Storing Logs

```bash
journalctl -b
journalctl -p warning
journalctl -u sshd
journalctl --since "2026-08-17 08:00"
journalctl --until "2026-08-17 10:00"
journalctl -f
```
### Persistent Journal

Journal persistence depends on configuration and storage.

Inspect:
```bash
journalctl --disk-usage
grep -v '^#' /etc/systemd/journald.conf | sed '/^$/d'
```
### Time Synchronization

```bash
timedatectl
systemctl status chronyd
chronyc sources -v
chronyc tracking
```
Correct time is essential for:

- TLS certificates,
- authentication,
- distributed logs,
- SIEM correlation,
- database consistency,
- incident response.
# Part 6 — Managing Security with SELinux

### DAC vs MAC

Traditional Unix permissions are **Discretionary Access Control (DAC)**.

SELinux adds **Mandatory Access Control (MAC)** policy.

Access effectively requires:

```text
Unix permissions allow
AND
SELinux policy allows
```
### Inspect SELinux

```bash
getenforce
sestatus
ls -Z /var/www 2>/dev/null
ps -eZ | head
```
### File Contexts

```bash
ls -Zd /var/www/html 2>/dev/null

matchpathcon /var/www/html/index.html 2>/dev/null || true
```
A common mistake:

```bash
cp file /var/www/html/
```

may produce a different SELinux label from creating/restoring the correct web content context.

Use:
```bash
sudo restorecon -Rv /var/www/html
```
### semanage fcontext

```bash
sudo semanage fcontext -a -t httpd_sys_content_t '/srv/web(/.*)?'
sudo restorecon -Rv /srv/web
```
`semanage` may come from an additional policy-management package depending on release/install profile.
### SELinux Booleans

```bash
getsebool -a | grep httpd | head

# Example only when required by architecture:
sudo setsebool -P httpd_can_network_connect on
```
Do not enable a Boolean just because its name sounds related. Understand the capability being granted.
### Diagnosing Denials

```bash
sudo ausearch -m AVC -ts recent
sudo journalctl | grep -i 'avc'
```
Troubleshooting order:

```text
1. Verify normal Unix permissions.
2. Verify expected SELinux mode.
3. Inspect labels.
4. Inspect AVC denial.
5. Fix context/boolean/policy requirement.
6. Keep SELinux enforcing.
```
# Part 7 — Archiving Files

```bash
tar -cvf etc-backup.tar /etc/hosts /etc/fstab
tar -tvf etc-backup.tar
tar -xvf etc-backup.tar

tar -czf configuration-$(date +%F).tar.gz /etc/hosts /etc/ssh/
```
Archive creation is not automatically a backup strategy.

A backup strategy also needs:
- separate storage,
- retention,
- integrity checks,
- restore testing,
- access control,
- encryption where required.
# Part 8 — Transferring Files Securely

```bash
scp report.txt student@server02:/tmp/

sftp student@server02
```
For directory synchronization where available:
```bash
rsync -av --progress ./reports/ student@server02:/srv/reports/
```
Use SSH host-key verification. Do not bypass host-key checks merely to make automation succeed.
# Part 9 — Tuning System Performance

```bash
uptime
top
free -h
vmstat 1 5
iostat 1 5 2>/dev/null || true
```
Performance troubleshooting begins with the bottleneck question:

```text
CPU?
memory?
disk I/O?
network?
application lock/contention?
external dependency?
```

Do not tune before measuring.
### tuned Profiles

```bash
systemctl status tuned 2>/dev/null || true
tuned-adm list 2>/dev/null || true
tuned-adm active 2>/dev/null || true
```
Availability/profile names depend on installed RHEL release and packages.

Choose profiles according to workload and vendor guidance, not because a name sounds "faster."
### Process Scheduling Priority

```bash
nice -n 10 command
sudo renice 5 -p 1234
```
# Part 10 — Managing Basic Storage

Use an **extra lab disk**, never the system disk for practice.
```bash
lsblk -f
sudo fdisk -l
```
### Partition with parted — Lab Example

```bash
# VERIFY /dev/sdb is the disposable lab disk first.
sudo parted /dev/sdb print
sudo parted /dev/sdb mklabel gpt
sudo parted /dev/sdb mkpart primary xfs 1MiB 4097MiB

lsblk /dev/sdb
```
These commands destroy/replace partition metadata on the selected disk. Use only a disposable lab disk.
### Create Filesystem

```bash
sudo mkfs.xfs /dev/sdb1

sudo mkdir -p /data
sudo mount /dev/sdb1 /data

findmnt /data
df -hT /data
```
### Persistent Mount

```bash
sudo blkid /dev/sdb1
```
```text
# /etc/fstab example
UUID=<filesystem-uuid>  /data  xfs  defaults  0 0
```
```bash
sudo umount /data
sudo mount -a
findmnt /data
```
`mount -a` is a critical validation step before reboot.
### Swap

```bash
# Example only on a dedicated lab partition
sudo mkswap /dev/sdb2
sudo swapon /dev/sdb2

swapon --show
free -h
```
# Part 11 — Managing Storage with LVM

LVM separates storage into layers:

```text
Physical device/partition
        ↓
Physical Volume (PV)
        ↓
Volume Group (VG)
        ↓
Logical Volume (LV)
        ↓
Filesystem / swap
        ↓
Mount point
```
### Create LVM Storage

```bash
# Example: /dev/sdc is an EMPTY lab disk.
sudo pvcreate /dev/sdc

sudo vgcreate vgdata /dev/sdc

sudo lvcreate -n lvapp -L 4G vgdata

sudo mkfs.xfs /dev/vgdata/lvapp

sudo mkdir -p /srv/appdata
sudo mount /dev/vgdata/lvapp /srv/appdata

pvs
vgs
lvs
```
### Extend LVM and XFS

```bash
sudo lvextend -L +2G /dev/vgdata/lvapp

sudo xfs_growfs /srv/appdata

lvs
df -hT /srv/appdata
```
Important:

Extending the logical volume does not automatically mean every filesystem grows.

The filesystem must also be expanded using the correct filesystem-specific tool, unless an integrated option/workflow is used.
### LVM Safety

Before destructive LVM operations:

```bash
pvs
vgs
lvs
lsblk -f
findmnt
```

Never run `pvremove`, `vgremove`, or `lvremove` from a copied tutorial on storage containing required data.
# Part 12 — Controlling and Troubleshooting the Boot Process

```text
UEFI/BIOS
   ↓
GRUB
   ↓
kernel + initramfs
   ↓
root filesystem
   ↓
systemd
   ↓
target/services
```
### Targets

```bash
systemctl get-default
systemctl list-units --type=target
```
### Kernel and Boot Information

```bash
uname -r
cat /proc/cmdline
ls -lh /boot
journalctl -b
journalctl -b -1
```
### Emergency / Rescue Concepts

Boot troubleshooting may require:
- rescue target,
- emergency target,
- kernel command-line changes,
- initramfs troubleshooting,
- repairing `/etc/fstab`,
- restoring SELinux labels.

Always practice in a VM with a snapshot.
# Part 13 — Recovering Superuser Access

Administrative recovery is a legitimate console-access procedure for systems you own/administer.

The exact RHEL 10 recovery procedure should be verified in current Red Hat documentation.

A common training workflow on RHEL-family systems has historically involved:

1. reboot to GRUB,
2. edit kernel command line,
3. use an emergency break such as `rd.break`,
4. remount the real root filesystem read-write,
5. chroot,
6. set a new password,
7. ensure SELinux relabeling where required,
8. reboot.

Because boot/recovery behavior can change by release, do not memorize old commands as universal truth.
```bash
# Example commands commonly used after reaching an authorized
# emergency shell in a disposable lab. Verify on your release.

mount -o remount,rw /sysroot
chroot /sysroot

passwd root

touch /.autorelabel

exit
exit
```
Never perform password-recovery procedures on systems you are not authorized to administer.
# Part 14 — Managing Network Security

### firewalld Zones and Services

```bash
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all

sudo firewall-cmd --get-services
```
### Allow a Service

```bash
sudo firewall-cmd --add-service=http
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload
sudo firewall-cmd --list-services
```
Runtime and permanent configuration are distinct.

Design the desired persistent policy instead of accumulating ad hoc runtime changes.
### Custom Port

```bash
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```
### SELinux Network Port Labeling

```bash
sudo semanage port -l | grep http_port_t

# Example when a web server is intentionally configured for TCP/8088:
sudo semanage port -a -t http_port_t -p tcp 8088
```
For a service to work on a custom port, multiple layers may need alignment:

```text
application listens
AND
SELinux permits service domain to bind that port type
AND
firewall allows network traffic
AND
network route exists
```
# Part 15 — Accessing Network-attached Storage with NFS

### NFS Client Discovery

```bash
showmount -e server02 2>/dev/null || true
```
### Manual Mount

```bash
sudo mkdir -p /mnt/shared

sudo mount -t nfs server02:/srv/shared /mnt/shared

findmnt /mnt/shared
```
### Persistent NFS Mount

```text
server02:/srv/shared  /mnt/shared  nfs  defaults,_netdev  0 0
```
`_netdev` communicates that the filesystem depends on network availability.
### Automounter Concept

Autofs mounts network filesystems on demand rather than keeping every remote mount continuously active.

This can improve resilience and reduce unnecessary mounts for many user/home/share environments.

Exact autofs maps are covered in lab practice and may vary by site architecture.
# Part 16 — Installing Red Hat Enterprise Linux

Current RH134 covers package-mode RHEL installation interactively and with Kickstart.

An automated installation separates:

```text
boot/install environment
      ↓
installation source
      ↓
Kickstart instructions
      ↓
disk/network/package/user configuration
      ↓
installed system
```
### Kickstart Structure — Educational Example

```text
# Simplified teaching example — validate against current RHEL 10 docs.

lang en_US.UTF-8
keyboard us
timezone UTC --utc

network --bootproto=dhcp --device=link --activate

rootpw --lock
user --name=admin --groups=wheel --password=<securely-generated-value>

autopart

%packages
@core
%end

%post
echo "Installed by Kickstart" > /etc/motd
%end
```
Do not store reusable plaintext passwords in Kickstart files.

Kickstart can partition disks automatically, so always test in disposable VMs before broad deployment.
# Part 17 — Managing Containers with Podman

Podman runs OCI-compatible containers and is daemonless in normal architecture.

Core concepts:

```text
image
  ↓
container
  ↓
processes + isolated namespaces/cgroups
```

A container is not a virtual machine.
```bash
podman info
podman images
podman ps
podman ps -a
```
### Pull and Run

```bash
podman pull registry.access.redhat.com/ubi10/ubi 2>/dev/null || true

podman run --rm   registry.access.redhat.com/ubi10/ubi   cat /etc/os-release
```
Image naming/availability depends on registry access and release. Use an image you are authorized to pull.
### Rootless Containers

Podman supports rootless operation.

This reduces the need for privileged container administration and fits least-privilege design.

Inspect:
```bash
podman unshare id
```
### Volumes and Ports

```bash
mkdir -p ~/container-content
echo "hello" > ~/container-content/index.html

# Example syntax; choose an available web image in your lab.
podman run --rm -d   --name webdemo   -p 8080:8080   -v ~/container-content:/var/www/html:Z   <approved-web-image>
```
`:Z` requests an SELinux relabel appropriate for private container use on supported systems.

The application inside the selected image must actually listen on the expected container port.
# Part 18 — Image-based Red Hat Enterprise Linux

Current RH134 also introduces image-based RHEL management.

Traditional package mode modifies an installed system through package transactions.

Image mode treats the operating-system deployment more like a managed, versioned system image.

Conceptual comparison:

```text
Package mode:
running system + package transactions

Image mode:
build/compose OS image
        ↓
deploy image
        ↓
update by deploying a new image version
```

Benefits can include:
- repeatability,
- immutable-style deployment patterns,
- easier rollback/version control,
- alignment with container/CI workflows.

Exact tooling evolves quickly, so use current RHEL image-mode documentation for implementation.
# Part 19 — Integrated RHCSA-style Troubleshooting

### Storage Failure Example

```text
Symptom:
System enters emergency mode after editing /etc/fstab.

Investigation:
1. read boot journal
2. inspect /etc/fstab
3. verify UUID with blkid
4. verify filesystem exists
5. test mount manually
6. run mount -a
7. reboot only after validation
```
### Web Service on Custom Port Example

```text
Requirement:
HTTP service should listen on TCP/8088.

Need:
1. app config -> 8088
2. SELinux -> http_port_t includes 8088
3. firewalld -> allow 8088/tcp
4. service -> reload/restart
5. ss -> verify LISTEN
6. curl -> verify locally
7. remote client -> verify network path
```

# Enhanced Deep-Study Layer — RH134 / Full Linux Administration

The original RH134-aligned content is preserved. This section expands it into a deeper administration guide covering robust Bash automation, scheduling, logging, SELinux, storage, LVM, boot recovery, firewalld, NFS, installation automation, Podman, performance troubleshooting, and integrated incident workflows.

The governing model is:

```text
Desired state
    ↓
Persistent configuration
    ↓
Service/kernel activation
    ↓
Runtime state
    ↓
Logs + metrics
    ↓
Verification
    ↓
Persistence/reboot test
```

For dangerous tasks such as storage, boot recovery, and firewall/network changes, use:

```text
Identify target
    ↓
Capture current state
    ↓
Validate rollback
    ↓
Change one layer
    ↓
Verify before reboot
```

---

## Enhanced Deep Dive 1 — Bash Script as a Small Program

A production-oriented Bash script should have:

```text
clear input
explicit output
functions
safe quoting
meaningful exit status
cleanup
logging
no embedded secrets
```

Example skeleton:

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

readonly PROGRAM=${0##*/}

log() {
    printf '%s [%s] %s\n' \
        "$(date '+%F %T')" \
        "$PROGRAM" \
        "$*"
}

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 1
}

main() {
    log "starting"
}

main "$@"
```

Why not depend only on:

```bash
set -e
```

Because Bash `errexit` has context-dependent behavior around conditionals, pipelines, command substitutions, and lists.

Explicit error handling is easier to reason about.

---

## Enhanced Deep Dive 2 — `getopts` for Administration Scripts

A script often needs options rather than one positional parameter.

Example:

```bash
#!/usr/bin/env bash

service=""
verbose=0

while getopts ":s:v" opt; do
    case "$opt" in
        s)
            service=$OPTARG
            ;;
        v)
            verbose=1
            ;;
        :)
            printf 'Option -%s requires an argument\n' "$OPTARG" >&2
            exit 2
            ;;
        \?)
            printf 'Unknown option: -%s\n' "$OPTARG" >&2
            exit 2
            ;;
    esac
done

shift $((OPTIND - 1))

if [[ -z "$service" ]]; then
    printf 'Usage: %s -s SERVICE [-v]\n' "$0" >&2
    exit 2
fi
```

Use `2` commonly for command-line usage errors in your own scripts if that convention fits your design.

Document your exit-code contract.

---

## Enhanced Deep Dive 3 — Safe Temporary Files with `mktemp` and `trap`

Unsafe:

```bash
tmp=/tmp/report.txt
```

Problems:

```text
name collision
symlink/race problem
wrong user ownership
stale old data
```

Safer:

```bash
tmpdir=$(mktemp -d) || exit 1

cleanup() {
    rm -rf -- "$tmpdir"
}

trap cleanup EXIT INT TERM
```

Mental model:

```text
script starts
   ↓
unique temporary workspace
   ↓
work
   ↓
normal exit / interrupt / failure
   ↓
trap
   ↓
cleanup
```

Temporary files can contain sensitive logs/configuration. Use restrictive permissions.

---

## Enhanced Deep Dive 4 — Bash Arrays Instead of Command Strings

Bad:

```bash
packages="curl rsync vim"
sudo dnf install -y $packages
```

Better:

```bash
packages=(
    curl
    rsync
    vim
)

sudo dnf install -y "${packages[@]}"
```

Array expansion preserves argument boundaries.

Avoid:

```bash
eval "$user_supplied_command"
```

because `eval` reparses text as shell syntax and is dangerous with untrusted input.

---

## Enhanced Deep Dive 5 — Regular Expressions for Administration

Extended-regex building blocks:

```text
^        start
$        end
.        any character
[...]    character class
(...)    group
|        alternation
*        zero or more
+        one or more
?        zero or one
{m,n}    repetition range
```

Example:

```bash
grep -E \
'^(PermitRootLogin|PasswordAuthentication)[[:space:]]+' \
sshd_config
```

This is safer than a loose search:

```bash
grep Password sshd_config
```

because loose patterns can match:

```text
comments
different directives
example text
```

---

## Enhanced Deep Dive 6 — Regex Is Not Semantic Validation

This regex:

```text
^[0-9]{1,3}(\.[0-9]{1,3}){3}$
```

can match:

```text
999.999.999.999
```

Text shape:

```text
looks like four decimal components
```

Semantic meaning:

```text
each IPv4 octet must be 0..255
```

Therefore:

```text
regex candidate selection
        ↓
semantic parser/range validation
```

Use the correct tool/library when data correctness matters.

---

## Enhanced Deep Dive 7 — `awk` as an Administration Language

`awk` processes records and fields.

Built-ins:

```text
NR current record number
NF number of fields
$1 first field
$NF last field
FS input field separator
OFS output separator
```

Example account report:

```bash
awk -F: '
BEGIN {
    OFS=","
    print "user","uid","shell"
}
{
    print $1,$3,$7
}
' /etc/passwd
```

Filesystem threshold report:

```bash
df -P |
awk '
NR > 1 {
    usage=$5
    gsub("%","",usage)

    if (usage >= 80) {
        print "WARNING:", $6, usage "%"
    }
}'
```

---

## Enhanced Deep Dive 8 — `sed` Safe-Editing Workflow

Do not experiment with a critical file using `sed -i` first.

Workflow:

```text
copy
  ↓
transform to new file
  ↓
diff
  ↓
validate configuration
  ↓
replace/apply
```

Example:

```bash
cp demo.conf demo.conf.before

sed -E \
's/^Port[[:space:]]+.*/Port 2222/' \
demo.conf.before \
> demo.conf.after

diff -u demo.conf.before demo.conf.after
```

A correct textual substitution does not guarantee a valid service configuration.

Run the service-specific validator afterward.

---

## Enhanced Deep Dive 9 — Cron Environment and Why Manual Tests Can Lie

User cron format:

```text
minute hour day-of-month month day-of-week command
```

Example:

```cron
30 6 * * * /home/student/bin/report.sh >>/home/student/report.log 2>&1
```

Cron often has a smaller environment than an interactive shell.

Possible differences:

```text
PATH
HOME
SHELL
working directory
locale
environment variables
SSH agent
```

Safer cron:

```cron
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin

30 6 * * * /home/student/bin/report.sh >>/home/student/report.log 2>&1
```

Use absolute paths inside critical scripts where appropriate.

---

## Enhanced Deep Dive 10 — System Cron and `/etc/cron.d`

A user crontab line:

```cron
15 2 * * * /home/user/task.sh
```

An `/etc/cron.d` entry includes the account:

```cron
15 2 * * * root /usr/local/sbin/task.sh
```

This extra field is important.

Do not copy a user-crontab line directly into `/etc/cron.d`.

---

## Enhanced Deep Dive 11 — systemd Timers: When vs What

A timer controls **when**.

A service controls **what**.

```text
health-report.timer
        ↓ activation
health-report.service
        ↓ ExecStart
/usr/local/sbin/health-report.sh
        ↓
exit status + journal
```

Example service:

```ini
[Unit]
Description=Generate health report

[Service]
Type=oneshot
ExecStart=/usr/local/sbin/health-report.sh
```

Timer:

```ini
[Unit]
Description=Schedule health report

[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
Persistent=true

[Install]
WantedBy=timers.target
```

Always test the `.service` manually before debugging the `.timer`.

---

## Enhanced Deep Dive 12 — `OnCalendar` and `systemd-analyze calendar`

Calendar timers are easier to verify than guess.

```bash
systemd-analyze calendar 'Mon..Fri 02:00'
```

This can show:

```text
normalized form
next occurrence
time until next run
```

Inspect timers:

```bash
systemctl list-timers --all
```

For calendar jobs, `Persistent=true` can help catch missed activations after downtime according to the timer design.

---

## Enhanced Deep Dive 13 — Journald Structured Metadata

Journal entries contain message text and fields.

Examples:

```text
_SYSTEMD_UNIT
_PID
_UID
_COMM
priority
boot ID
```

Commands:

```bash
journalctl _SYSTEMD_UNIT=sshd.service -b
journalctl _UID=0 --since today
journalctl -p warning..alert -b
journalctl -o verbose -n 1
```

This is more precise than:

```bash
journalctl | grep something
```

when a structured field exists.

---

## Enhanced Deep Dive 14 — Journal Persistence and Retention

Questions:

```text
Are previous boots retained?
How much disk is used?
What are storage limits?
Are logs forwarded centrally?
```

Inspect:

```bash
journalctl --list-boots
journalctl --disk-usage

grep -E \
'^(Storage|SystemMaxUse|RuntimeMaxUse)=' \
/etc/systemd/journald.conf \
2>/dev/null || true
```

Incident-response value depends on retention.

---

## Enhanced Deep Dive 15 — rsyslog and Central Logging Awareness

Possible architecture:

```text
application/kernel
       ↓
journald
       ↓
optional forwarding
       ↓
rsyslog
       ↓
local text files
and/or
remote collector / SIEM
```

Why centralize?

```text
host fails
host compromised
disk corrupted
investigator needs cross-host timeline
```

Central logging should consider:

```text
transport security
buffering
server authentication
retention
clock synchronization
access control
```

---

## Enhanced Deep Dive 16 — Log Rotation

Do not manage growing logs by randomly deleting active files.

`logrotate` can:

```text
rotate
compress
retain generations
create/recreate
run postrotate hooks
```

Inspect:

```bash
cat /etc/logrotate.conf
ls /etc/logrotate.d

logrotate -d /etc/logrotate.conf 2>/dev/null | head -n 60
```

If a process keeps an old deleted logfile open:

```bash
sudo lsof +L1
```

can expose it.

---

## Enhanced Deep Dive 17 — Chrony: Time Service vs Actual Synchronization

`chronyd` running does not prove the clock is synchronized correctly.

Inspect:

```bash
timedatectl
chronyc sources -v
chronyc tracking
```

Questions:

```text
Is a source selected?
Is it reachable?
What is the offset?
What is the reference?
Is the clock synchronized?
```

Accurate time is important for:

```text
TLS
Kerberos-style authentication
logs
SIEM
distributed systems
database consistency
certificates
```

---

## Enhanced Deep Dive 18 — SELinux Decision Model

Traditional permissions:

```text
DAC
```

SELinux:

```text
MAC
```

Both must allow.

Simplified SELinux check:

```text
process subject
type=httpd_t
       ↓ requests read
file object
type=httpd_sys_content_t
       ↓
policy checks:
subject type
object type
object class
requested permission
       ↓
allow or deny
```

Inspect:

```bash
getenforce
sestatus
ps -eZ | head
ls -Z /var/www 2>/dev/null
```

---

## Enhanced Deep Dive 19 — `chcon` vs Persistent File Context Rules

`chcon` changes a current label.

It does not define the persistent policy mapping.

Persistent approach:

```bash
sudo semanage fcontext \
  -a \
  -t httpd_sys_content_t \
  '/srv/web(/.*)?'

sudo restorecon -Rv /srv/web
```

Model:

```text
semanage fcontext
→ expected label rule

restorecon
→ apply expected label
```

A future relabel can undo an ad-hoc `chcon`.

---

## Enhanced Deep Dive 20 — SELinux Booleans

A Boolean activates/deactivates a predefined policy capability.

Inspect:

```bash
getsebool -a | grep '^httpd_' | head

semanage boolean -l |
grep httpd |
head
```

Example conceptual capability:

```text
web service allowed to make outbound network connections
```

Do not enable every Boolean containing the application name.

Every enabled capability broadens the allowed behavior of the confined domain.

---

## Enhanced Deep Dive 21 — SELinux AVC Troubleshooting

Workflow:

```text
normal Unix permissions correct?
    ↓
expected SELinux mode?
    ↓
file/process labels correct?
    ↓
AVC denial?
    ↓
existing correct type?
    ↓
needed Boolean?
    ↓
only then consider custom policy
```

Commands:

```bash
ausearch -m AVC -ts recent 2>/dev/null | tail -n 50

journalctl |
grep -i 'avc:.*denied' |
tail
```

If available:

```bash
ausearch -m AVC -ts recent |
audit2why
```

Do not make `audit2allow` your first response. The denial can indicate:

```text
wrong path
wrong label
wrong configuration
or actual unwanted behavior
```

---

## Enhanced Deep Dive 22 — Tar Archives and Safe Extraction

Create relative-path archive:

```bash
tar -czf config-backup.tar.gz \
  -C /etc \
  hosts ssh
```

Inspect before extraction:

```bash
tar -tzf config-backup.tar.gz
```

Restore into a test directory:

```bash
mkdir restore-test

tar -xzf config-backup.tar.gz \
  -C restore-test
```

Do not extract an untrusted archive as root without inspecting paths and symlinks.

Archive:

```text
bundles content
```

Backup:

```text
independent recoverable copy
+
retention
+
restore test
+
access control
```

---

## Enhanced Deep Dive 23 — Compression Is Not Encryption

Common compression families:

```text
gzip
bzip2
xz
zstd
```

Trade-offs:

```text
CPU
compression speed
decompression speed
compression ratio
memory
```

Compression:

```text
reduces size
```

It does **not** provide:

```text
confidentiality
authentication
trusted origin
```

---

## Enhanced Deep Dive 24 — rsync and the Trailing Slash

These can produce different directory layouts:

```bash
rsync -a src/ dest/
```

vs:

```bash
rsync -a src dest/
```

Concept:

```text
src/
→ contents of src

src
→ src directory itself
```

Always preview deletion-oriented sync:

```bash
rsync -av --dry-run --delete \
  source/ destination/
```

Treat `--delete` as destructive.

---

## Enhanced Deep Dive 25 — Performance Troubleshooting: Measure Before Tuning

Use the resource model:

```text
CPU
memory
disk I/O
network
application locks
external services
```

For each resource ask:

```text
utilization?
saturation/queue?
errors?
```

Commands:

```bash
uptime
top
vmstat 1 5
free -h
iostat -xz 1 3 2>/dev/null || true
ss -s
```

Do not choose a tuned profile because the name sounds fast.

---

## Enhanced Deep Dive 26 — CPU Categories

Common CPU categories:

```text
user
system
idle
I/O wait
steal
```

Inspect:

```bash
top
vmstat 1 5
mpstat -P ALL 1 3 2>/dev/null || true
```

Interpretation examples:

```text
high user
→ application CPU work

high system
→ kernel/system-call work

high wa
→ tasks waiting for I/O

high steal
→ virtualized CPU contention
```

---

## Enhanced Deep Dive 27 — Memory: Available, Cache, Swap, OOM

Linux uses unused RAM as cache.

Inspect:

```bash
free -h

grep -E \
'MemTotal|MemAvailable|Cached|Swap' \
/proc/meminfo

ps -eo pid,user,rss,%mem,cmd \
--sort=-rss |
head

journalctl -k |
grep -i -E \
'oom|out of memory|killed process'
```

Low `free` alone is not proof of memory pressure.

More useful questions:

```text
MemAvailable?
swap-in/out?
OOM events?
largest RSS?
cgroup limit?
```

---

## Enhanced Deep Dive 28 — Disk Performance: Throughput, IOPS, Latency, Queue

A disk can be:

```text
not full
```

but still slow.

Metrics:

```text
throughput
IOPS
latency
queue depth
utilization
```

Inspect:

```bash
iostat -xz 1 3
vmstat 1 5
```

Application response time often follows storage latency.

---

## Enhanced Deep Dive 29 — tuned Profiles

Inspect:

```bash
tuned-adm list 2>/dev/null || true
tuned-adm active 2>/dev/null || true
tuned-adm recommend 2>/dev/null || true
```

Correct workflow:

```text
baseline
 ↓
identify workload
 ↓
choose justified profile
 ↓
measure
 ↓
compare
 ↓
document
```

A throughput-oriented profile can make latency or power behavior worse for another workload.

---

## Enhanced Deep Dive 30 — Storage Safety: Identify the Target Before Partitioning

Before any destructive command:

```bash
lsblk -o \
NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS,MODEL,SERIAL

findmnt

pvs 2>/dev/null || true
vgs 2>/dev/null || true
lvs 2>/dev/null || true

swapon --show
```

Do not identify a disk only as:

```text
/dev/sdb
```

Device naming can differ by environment.

Use:

```text
size
model
serial
existing filesystem
mounts
LVM membership
```

to prove identity.

---

## Enhanced Deep Dive 31 — GPT, Partition, Filesystem, Mount Point

These layers are different:

```text
disk
  ↓
partition table (GPT)
  ↓
partition
  ↓
filesystem
  ↓
mount point
  ↓
files
```

Example:

```text
/dev/sdb
→ GPT
→ /dev/sdb1
→ XFS
→ /data
```

Creating a partition does not create a filesystem.

Creating a filesystem does not mount it.

Mounting it temporarily does not make it persistent.

---

## Enhanced Deep Dive 32 — Persistent Mount Workflow

Safe sequence:

```text
create filesystem
    ↓
identify UUID
    ↓
create mount point
    ↓
mount manually
    ↓
verify
    ↓
write fstab
    ↓
unmount
    ↓
mount -a
    ↓
verify
    ↓
only then reboot
```

Commands:

```bash
blkid /dev/<verified-partition>

sudo mount -a

findmnt /data

findmnt --verify 2>/dev/null || true
```

`mount -a` is a critical pre-reboot test.

---

## Enhanced Deep Dive 33 — Swap Layers

Swap can be provided by:

```text
partition
LVM logical volume
swap file
```

depending on system design/support.

General workflow:

```text
allocate storage
   ↓
mkswap
   ↓
swapon
   ↓
verify
   ↓
fstab if persistent
```

Inspect:

```bash
swapon --show
cat /proc/swaps
free -h
```

Swap is much slower than RAM.

It can help absorb transient pressure but should not be used to hide a persistent memory-capacity problem.

---

## Enhanced Deep Dive 34 — LVM Physical Extents

LVM model:

```text
disk/partition
    ↓
PV
    ↓
VG
    ↓
LV
    ↓
filesystem
    ↓
mount
```

A VG is divided into fixed-size allocation units:

```text
physical extents
```

Inspect:

```bash
pvs -o +pv_pe_count,pv_pe_alloc_count
vgs
lvs -a -o +devices
```

Logical volumes consume extents from the VG.

---

## Enhanced Deep Dive 35 — Growing LVM and Filesystem Are Separate

Example:

```bash
sudo lvextend \
  -L +2G \
  /dev/vgdata/lvapp
```

Now the block device is larger.

The XFS filesystem can still have its old size.

Grow:

```bash
sudo xfs_growfs /srv/appdata
```

Verify both:

```bash
lvs
df -hT /srv/appdata
```

Mental model:

```text
LV size
≠
filesystem size
```

until both layers are expanded.

---

## Enhanced Deep Dive 36 — LVM `--resizefs` Awareness

Some LVM operations can call filesystem resize helpers:

```bash
lvextend -r ...
```

where supported.

Even with integrated resizing, understand and verify:

```text
block layer
filesystem layer
```

Do not treat the combined option as magic.

---

## Enhanced Deep Dive 37 — LVM Snapshots

Snapshot concept:

```text
origin LV
   ↓ snapshot created
unchanged blocks shared
changed old blocks copied
```

Snapshot is useful for:

```text
testing
short rollback workflows
some backup workflows
```

But:

```text
snapshot
≠
independent backup
```

If snapshot storage fills, the snapshot can become invalid/unusable depending on type/configuration.

Database/application consistency may require quiescing the application.

---

## Enhanced Deep Dive 38 — Boot Chain

```text
Firmware
   ↓
GRUB
   ↓
Kernel
   ↓
initramfs
   ↓
root filesystem
   ↓
systemd PID 1
   ↓
targets
   ↓
services
   ↓
login / SSH
```

Troubleshooting question:

```text
At which stage did boot stop?
```

Examples:

```text
No GRUB
→ bootloader/firmware layer

Kernel panic before root
→ kernel/initramfs/storage layer

Emergency mode after root
→ fstab/systemd/dependency/config layer
```

---

## Enhanced Deep Dive 39 — GRUB and Kernel Command Line

Inspect:

```bash
cat /proc/cmdline

grubby --default-kernel \
2>/dev/null || true

grubby --info=ALL \
2>/dev/null |
head -n 80 || true
```

Kernel arguments can control:

```text
root storage
console
recovery
debugging
SELinux recovery behavior
```

Temporary recovery parameters should be removed afterward.

---

## Enhanced Deep Dive 40 — initramfs and `dracut`

initramfs is early userspace.

It can contain:

```text
storage drivers
LVM tools
filesystem modules
encryption tools
root-device discovery config
```

Inspect:

```bash
lsinitrd 2>/dev/null | head -n 80
```

RHEL-family systems commonly use `dracut` tooling for initramfs generation.

If the root disk cannot be found before normal systemd startup, inspect this layer.

---

## Enhanced Deep Dive 41 — Broken fstab and Emergency Mode

Typical incident:

```text
wrong UUID in /etc/fstab
       ↓
mount unit fails
       ↓
boot dependency fails
       ↓
emergency/recovery state
```

Recovery:

```text
console access
  ↓
read journal
  ↓
inspect fstab
  ↓
verify blkid
  ↓
fix one entry
  ↓
mount -a
  ↓
continue/reboot
```

Practice in snapshots only.

---

## Enhanced Deep Dive 42 — Superuser Recovery and Console Security

Console recovery is powerful because it can bypass normal remote authentication.

Therefore hypervisor/physical console access is a security boundary.

Release-specific recovery may involve:

```text
GRUB edit
early shell
remount real root RW
chroot
passwd
SELinux relabel if required
reboot
```

Use current installed-release documentation for exact procedure.

Never perform account-recovery procedures on systems you do not administer.

---

## Enhanced Deep Dive 43 — firewalld Zones

A firewalld zone expresses a trust/policy context.

A zone can be associated with:

```text
interfaces
source networks
```

and can permit:

```text
services
ports
protocols
rich rules
```

Inspect:

```bash
firewall-cmd --get-active-zones
firewall-cmd --get-default-zone
firewall-cmd --list-all
firewall-cmd --get-services
```

A rule in the wrong zone can appear correct but never match the intended traffic.

---

## Enhanced Deep Dive 44 — Runtime vs Permanent firewalld

Safe pattern:

```text
understand current zone
   ↓
make runtime change
   ↓
test
   ↓
make permanent
   ↓
reload
   ↓
retest
```

Commands:

```bash
sudo firewall-cmd --add-service=http

sudo firewall-cmd --list-services

sudo firewall-cmd \
  --permanent \
  --add-service=http

sudo firewall-cmd --reload

sudo firewall-cmd --list-services
```

Do not open broad ports simply to "see if it works".

---

## Enhanced Deep Dive 45 — Rich Rules and Management-Source Restriction

Rich rules can express source-aware policy.

Use cases:

```text
SSH only from management subnet
allow one service from partner subnet
log/reject selected traffic
```

Inspect documentation:

```bash
man firewalld.richlanguage
```

Example architecture:

```text
management subnet
192.0.2.0/24
      ↓ SSH allowed
server

all other sources
      ↓ SSH denied
```

Use only approved lab networks in exercises.

---

## Enhanced Deep Dive 46 — firewalld and nftables Awareness

Modern firewalld commonly programs a lower-level packet filtering engine such as nftables.

Operational principle:

```text
if firewalld owns host firewall policy
→ manage it through firewall-cmd
```

Mixing unrelated low-level rules with firewalld can create:

```text
confusing runtime state
nonpersistent changes
unexpected reload behavior
```

Understand ownership of the policy.

---

## Enhanced Deep Dive 47 — Custom Application Port: Four Required Layers

For a web service on TCP/8088:

```text
1. application configured for 8088
2. SELinux allows web domain to bind that port type
3. firewalld permits incoming TCP/8088
4. route/client path reaches server
```

Verify:

```bash
ss -lntp |
grep ':8088'

semanage port -l |
grep http_port_t \
2>/dev/null || true

firewall-cmd --list-all

curl -v \
http://127.0.0.1:8088/
```

Opening the firewall does not create a listening application.

---

## Enhanced Deep Dive 48 — NFS Request Path

```text
client application
      ↓
VFS
      ↓
NFS client
      ↓
network route/firewall
      ↓
NFS server
      ↓
export policy
      ↓
server filesystem permissions
```

A mounted share can still deny access because of:

```text
server filesystem ownership
UID/GID mapping
export options
SELinux
application policy
```

---

## Enhanced Deep Dive 49 — NFS Exports

Server export example:

```text
/srv/shared 192.0.2.0/24(rw,sync)
```

Inspect:

```bash
exportfs -v
showmount -e localhost
```

Security questions:

```text
Which clients?
Read-only or read-write?
Root handling?
Identity consistency?
Firewall?
SELinux?
```

Avoid:

```text
export writable filesystem to everyone
```

without strong justification.

---

## Enhanced Deep Dive 50 — Autofs

Autofs model:

```text
user accesses /shares/team
       ↓
autofs sees trigger
       ↓
mount remote NFS
       ↓
user accesses files
       ↓
idle timeout
       ↓
unmount
```

Benefits:

```text
on-demand remote dependency
reduced always-mounted shares
useful for many user/home paths
```

Troubleshooting layers:

```text
map syntax
automount service
DNS
route
NFS server
export
permissions
```

---

## Enhanced Deep Dive 51 — Kickstart as Installation-as-Code

Kickstart can declare:

```text
language
timezone
network
disk layout
packages
users
post-install actions
```

Architecture:

```text
installer boot
    ↓
installation source
    ↓
Kickstart
    ↓
storage/network/packages/users
    ↓
installed host
```

Storage commands are highly destructive.

Never test broad automatic disk selection against systems with valuable disks.

Do not store reusable plaintext passwords in a Git repository.

---

## Enhanced Deep Dive 52 — Podman: Image, Container, Process

```text
OCI image
  ↓ create
container runtime state
  ↓
process(es)
+
namespaces
+
cgroups
+
mounts
```

A container is not a VM.

It normally shares the host kernel.

Inspect:

```bash
podman info
podman images
podman ps
podman ps -a
```

---

## Enhanced Deep Dive 53 — Rootless Podman

Rootless Podman lets a normal user run containers without a rootful daemon.

Inspect:

```bash
podman unshare id 2>/dev/null || true

grep "^$USER:" \
/etc/subuid \
/etc/subgid \
2>/dev/null || true
```

User namespaces can map container UIDs to subordinate host UID ranges.

Rootless reduces privilege but does not make untrusted images automatically safe.

---

## Enhanced Deep Dive 54 — Podman Port Publishing

Example:

```text
-p 8080:80
```

means:

```text
host TCP/8080
       ↓
container networking/NAT
       ↓
container TCP/80
       ↓
application
```

Troubleshooting:

```text
container running?
app listening inside?
publish mapping exists?
host listener/NAT correct?
firewall allows host port?
SELinux policy okay?
```

---

## Enhanced Deep Dive 55 — Podman Bind Mounts and SELinux

Example:

```bash
podman run --rm \
  -v "$HOME/site:/content:Z" \
  <approved-image> \
  ls -l /content
```

`:Z` requests a private container-oriented relabel in applicable SELinux environments.

Do not relabel broad sensitive host paths such as:

```text
/etc
/home
/
```

simply to satisfy a container.

Create a dedicated application content directory.

---

## Enhanced Deep Dive 56 — Image-Based RHEL Concept

Traditional package mode:

```text
running OS
   ↓
dnf/rpm transactions
   ↓
files change in place
```

Image-oriented model:

```text
source/config
    ↓
OS image build
    ↓
versioned image
    ↓
deploy
    ↓
host boots desired image
```

Benefits can include:

```text
repeatability
versioning
rollback
alignment with CI pipelines
```

Trade-offs include understanding:

```text
image lifecycle
mutable/persistent data
configuration injection
deployment rollback
```

---

## Enhanced Deep Dive 57 — Integrated RHCSA Troubleshooting Matrix

```text
Symptom                         First subsystem questions
----------------------------------------------------------------
Cannot login                    user/PAM/SSH/account state
Service unavailable             systemd/config/socket
Remote service unreachable      route/firewall/SELinux/listener
Disk full                       df/du/inodes/open-deleted/LVM
Boot emergency                  fstab/storage/systemd/initramfs
NFS mount fails                 route/server/export/firewall
Container unavailable           image/process/port/mount/SELinux
Timer not running               service/timer/schedule/journal
```

The best command is the one that tests your current hypothesis.

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Defensive Bash Framework

Write a script using:

```text
functions
getopts
mktemp
trap
set -u
pipefail
logging
meaningful exit codes
```

Do not use `eval`.

## Enhanced Lab 2 — Service Inspector Script

Accept:

```text
-s SERVICE
-v
```

Report:

```text
service state
main PID
listener
recent journal
enabled state
```

## Enhanced Lab 3 — Regex Precision

Build a synthetic `sshd_config`.

Match only active target directives, not comments or similar names.

## Enhanced Lab 4 — awk Disk Report

Create a filesystem report that warns above a configurable threshold.

## Enhanced Lab 5 — sed Safe Configuration Change

Transform a copy, inspect `diff`, validate, and only then apply to a lab service.

## Enhanced Lab 6 — Cron Environment

Create a job that writes its environment.

Compare with interactive Bash.

## Enhanced Lab 7 — `/etc/cron.d`

Create a safe system job and document why the explicit user field exists.

## Enhanced Lab 8 — systemd Timer

Create a oneshot service and timer.

Test service independently before scheduling.

## Enhanced Lab 9 — Calendar Timer

Use:

```bash
systemd-analyze calendar
```

to verify five schedules.

## Enhanced Lab 10 — Journal Query Matrix

Build queries by:

```text
boot
unit
UID
PID
priority
time window
```

## Enhanced Lab 11 — Journal Persistence

Determine whether logs survive reboot and document retention.

## Enhanced Lab 12 — Logrotate

Create a lab application logfile and policy.

Test using debug/forced rotation.

## Enhanced Lab 13 — Chrony

Document sources and tracking.

Temporarily isolate network in the lab and explain what changes.

## Enhanced Lab 14 — SELinux Process/File Type Map

Choose a confined service and map:

```text
process domain
content type
config type
log type
port type
```

where visible.

## Enhanced Lab 15 — Persistent SELinux Content Label

Serve content from `/srv/web`.

Use:

```text
semanage fcontext
restorecon
```

Do not disable SELinux.

## Enhanced Lab 16 — SELinux Boolean

Choose one Boolean, explain exact capability, test in lab only if architecture requires it, then revert.

## Enhanced Lab 17 — AVC Troubleshooting

Create a safe mislabeled-content denial and diagnose from audit evidence.

## Enhanced Lab 18 — Tar Restore Test

Archive, list, checksum, extract into another directory, compare result.

## Enhanced Lab 19 — Compression Comparison

Compare available gzip/xz/zstd tools on a generated dataset.

Record time/size without declaring one universally best.

## Enhanced Lab 20 — rsync Trailing Slash

Demonstrate:

```text
src/
src
```

and run a dry-run before `--delete`.

## Enhanced Lab 21 — CPU Baseline

Collect:

```text
uptime
top
vmstat
mpstat
```

at idle and under safe CPU load.

## Enhanced Lab 22 — Memory Baseline

Collect:

```text
free
MemAvailable
swap
largest RSS
OOM evidence
```

## Enhanced Lab 23 — Disk Performance

Use:

```text
iostat
vmstat
```

during a controlled copy.

## Enhanced Lab 24 — tuned

Inspect active/recommended profiles and write a justification before changing anything.

## Enhanced Lab 25 — Disk Identity Checklist

Attach two extra disks and identify each from:

```text
size
model
serial
FSTYPE
mount
LVM
```

## Enhanced Lab 26 — GPT Partition

Partition only a disposable empty disk using aligned boundaries.

## Enhanced Lab 27 — Filesystem + fstab

Create XFS, mount manually, add UUID to fstab, test `mount -a`, reboot, verify.

## Enhanced Lab 28 — Swap

Create persistent swap on a disposable LV or partition and verify after reboot.

## Enhanced Lab 29 — LVM Build

Create:

```text
PV
VG
LV
XFS
mount
```

and document each layer.

## Enhanced Lab 30 — LVM Extend

Extend the LV first.

Show filesystem unchanged.

Then grow filesystem and verify.

## Enhanced Lab 31 — LVM Snapshot

Create a small snapshot, modify origin, inspect, and remove it.

Document why snapshot is not independent backup.

## Enhanced Lab 32 — Boot Chain

Map the actual VM:

```text
firmware
GRUB
kernel
initramfs
root
systemd
```

## Enhanced Lab 33 — Kernel Command Line

Explain every current `/proc/cmdline` parameter you can safely identify.

## Enhanced Lab 34 — initramfs

Use `lsinitrd` and identify modules/config relevant to root storage.

## Enhanced Lab 35 — Broken fstab Recovery

Snapshot VM.

Introduce one controlled bad mount.

Recover through console.

Run `mount -a` before reboot.

## Enhanced Lab 36 — Root Recovery

Use only an authorized disposable VM.

Follow release-appropriate docs and document SELinux relabel behavior.

## Enhanced Lab 37 — firewalld Zones

Map interfaces to zones and compare runtime/permanent state.

## Enhanced Lab 38 — Runtime-First Firewall Change

Open a test service at runtime, verify, then persist, reload, reverify.

## Enhanced Lab 39 — Rich Rule

Allow SSH from only a lab management subnet.

Test and remove after exercise.

## Enhanced Lab 40 — Custom Web Port

Align:

```text
web config
SELinux port type
firewalld
listener
curl
```

## Enhanced Lab 41 — NFS Server

Export a lab directory only to the private lab network.

Verify with `exportfs -v`.

## Enhanced Lab 42 — NFS Client

Mount manually, inspect options, test permissions.

## Enhanced Lab 43 — Autofs

Configure an on-demand share if package is available.

Observe mount on access and idle unmount.

## Enhanced Lab 44 — Kickstart Review

Create a disposable-VM Kickstart.

Document:

```text
disk selection
network
packages
users
secret handling
post section
```

## Enhanced Lab 45 — Podman Image Inspection

Pull an approved image, inspect metadata, and run a one-shot command.

## Enhanced Lab 46 — Rootless Podman

Run rootlessly and inspect namespace/user mapping.

## Enhanced Lab 47 — Podman Web Service

Publish a high host port and verify each layer.

## Enhanced Lab 48 — Podman SELinux Volume

Mount a dedicated content directory using appropriate SELinux volume labeling.

## Enhanced Lab 49 — Podman Failure Matrix

Break separately:

```text
image name
command
bind path
volume label
host port
container port
```

## Enhanced Lab 50 — Image-Mode Architecture

Write a comparison of:

```text
package mode
image mode
```

including update/rollback/persistent-state implications.

## Enhanced Lab 51 — Integrated RH134 Challenge

Complete at least 15 tasks across:

```text
script
timer
journal
SELinux
storage
LVM
fstab
swap
firewalld
NFS
Podman
boot
```

Reboot and verify persistence.



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Shell Automation

1. Write a script that validates required commands.
2. Accept a service name as an argument.
3. Report service state, PID, sockets, and recent logs.
4. Use functions and meaningful exit codes.

### Lab 2 — Regex Administration

1. Extract failed SSH events from synthetic or lab logs.
2. Extract usernames and source addresses.
3. Use grep/awk to count repeated events.
4. Explain where regex validation is insufficient.

### Lab 3 — Scheduling

1. Schedule a user report with cron.
2. Create a systemd oneshot service and timer.
3. Compare logging and environment behavior.

### Lab 4 — SELinux

1. Install/configure a lab web service.
2. Serve content from a nonstandard directory.
3. Observe access failure.
4. Use SELinux logs/context inspection.
5. Apply persistent `semanage fcontext` rule and `restorecon`.
6. Verify without disabling SELinux.

### Lab 5 — LVM

1. Attach an empty disk.
2. Create PV, VG, LV.
3. Create XFS filesystem.
4. Mount persistently.
5. Extend LV and filesystem.
6. Verify with `pvs`, `vgs`, `lvs`, `df`, `findmnt`.

### Lab 6 — Swap

1. Create a small lab swap LV or partition.
2. Enable it.
3. Add persistent configuration.
4. Verify `swapon --show`.
5. Remove it cleanly after the lab if desired.

### Lab 7 — Boot Troubleshooting

1. Snapshot VM.
2. Create an intentionally incorrect lab fstab mount.
3. Reboot into the resulting troubleshooting state if safe.
4. Repair the entry.
5. Validate with `mount -a`.
6. Document recovery.

### Lab 8 — Root Recovery

1. Use a disposable VM with console access.
2. Follow the documented RHEL-family recovery workflow.
3. Reset a lab root password.
4. Handle SELinux relabeling if required.
5. Verify login after reboot.

### Lab 9 — firewalld + SELinux Port

1. Configure a web service on nonstandard port.
2. Add SELinux port labeling.
3. Add firewalld rule.
4. Verify with `ss`, `curl`, `firewall-cmd`, and `semanage port -l`.

### Lab 10 — NFS

1. Use two VMs.
2. Export a lab directory from server02 if your environment permits.
3. Mount from admin01.
4. Configure persistence.
5. Test automount concept if autofs is installed.

### Lab 11 — Kickstart Review

1. Create a Kickstart file for a disposable VM.
2. Validate its structure using current tools/docs available in your environment.
3. Ensure no plaintext reusable secrets are committed.
4. Perform an automated installation if lab infrastructure supports it.

### Lab 12 — Podman

1. Pull an approved test image.
2. Run interactively.
3. Run detached service.
4. Map a port.
5. Mount a labeled volume.
6. Inspect logs and stop/remove cleanly.

### Lab 13 — Integrated RHCSA Challenge

1. Create eight tasks across users, permissions, SELinux, storage, services, firewall, networking, and scheduling.
2. Complete them without web search using man pages and notes.
3. Reboot.
4. Verify all required state persists.

## 6. Mini Project

# Mini Project — Production-style RHEL Services Node

Build a RHEL-family VM with:

```text
rhel-services01.lab.example
```

## Storage
Extra disk:
- LVM VG `vgservices`
- LV `lvdata`
- XFS at `/srv/services`
- persistent mount

## Security
- SELinux enforcing
- firewalld enabled
- service only on required ports
- no 777 permissions

## Application
Run a simple web service:
- from package mode or Podman,
- nondefault content directory,
- test a custom TCP port,
- configure SELinux correctly.

## Scheduling
- systemd timer generates daily health report.

## Logs
- preserve service/journal troubleshooting commands.

## NFS
Mount one lab NFS share from a second VM.

## Automation
Write:
```text
/usr/local/sbin/server-audit.sh
```

Report:
- failed units
- filesystem usage
- LVM state
- SELinux mode
- firewall services
- listening sockets
- last 20 service log lines
- time synchronization state

## Failure Scenarios
1. wrong fstab UUID,
2. SELinux wrong context,
3. missing firewall port,
4. service inactive,
5. LV full simulation,
6. NFS server unavailable,
7. timer disabled,
8. Podman port mismatch.

Document each as:
```text
Symptom
Evidence
Root cause
Fix
Verification
Persistence check
```

# Expanded Capstone — Production-Style RHEL Services Node

Build two VMs:

```text
rhel-services01.lab.example
rhel-storage02.lab.example
```

Architecture:

```text
Admin
  |
  +------ SSH ------> rhel-services01
  |                    ├─ systemd
  |                    ├─ timer
  |                    ├─ LVM/XFS
  |                    ├─ SELinux enforcing
  |                    ├─ firewalld
  |                    ├─ web/Podman service
  |                    └─ NFS client
  |
  +------ SSH ------> rhel-storage02
                       └─ NFS export
```

## Storage Design

```text
extra disk
   ↓
PV
   ↓
VG vgservices
   ↓
LV lvdata
   ↓
XFS
   ↓
/srv/services
```

Requirements:

```text
persistent mount
mount -a pre-reboot validation
LV extension
filesystem extension
swap exercise
optional snapshot exercise
```

## Security

Keep:

```text
SELinux enforcing
firewalld active
least privilege
no 777
```

If web content is under `/srv/services/web`:

```text
persistent SELinux file-context mapping
restorecon
```

If using a custom port:

```text
application listens
SELinux port mapping correct
firewalld permits
route works
```

## Automation

Create:

```text
/usr/local/sbin/server-audit.sh
```

Requirements:

```text
getopts
functions
mktemp
trap
explicit exit codes
```

Report:

```text
failed units
filesystem use
inode use
LVM
swap
SELinux
firewall
listeners
chrony
latest service errors
```

Run through a systemd timer.

## NFS

On `rhel-storage02`:

```text
/srv/shared
```

Export only to the lab network.

On services node:

```text
manual mount
persistent or autofs design
```

## Podman

Run a rootless service using:

```text
approved image
high host port
dedicated bind content
correct SELinux label
```

No privileged container mode.

## Boot Recovery

In a snapshot:

```text
break one fstab entry
reboot
recover through console
inspect logs
repair
mount -a
reboot
```

## Failure Matrix

At least 20:

```text
cron PATH
timer disabled
journal nonpersistent
chrony source failure
wrong SELinux context
missing required Boolean
wrong firewalld zone
missing SELinux custom port
wrong fstab UUID
filesystem full
no VG free extents
swap missing after reboot
NFS export denied
NFS server unavailable
autofs map error
Podman wrong published port
Podman bad volume label
invalid service config
package/repository issue
script wrong exit code
```

Record:

```text
Symptom
Evidence
Layer
Root cause
Fix
Verification
Persistence
Prevention
```


## 7. Recommended Resources

Primary references:

- Red Hat System Administration II (RH134) official course outline.
- Red Hat Enterprise Linux 10 documentation:
  - storage,
  - SELinux,
  - firewalld,
  - boot and recovery,
  - systemd,
  - NFS,
  - Podman,
  - image mode,
  - Kickstart/installation.
- `man` pages for `lvm`, `firewall-cmd`, `semanage`, `restorecon`, `podman`, `systemd.timer`.
## 8. Certification Relevance

RH134 is the second half of Red Hat's RHCSA training path.

The current RH134 course is based on RHEL 10 and Red Hat recommends RHCSA EX200 or the automation course after completing RH124 + RH134.

For self-study, focus on:
- persistence after reboot,
- accurate task interpretation,
- verification,
- SELinux/firewall/storage troubleshooting,
- fast use of local documentation.
## 9. Common Mistakes & Best Practices

- **Mistake:** Partitioning the wrong disk.
  - **Best practice:** Always verify `lsblk -f` and device identity before destructive commands.
- **Mistake:** Editing fstab then rebooting immediately.
  - **Best practice:** Test with `mount -a` first.
- **Mistake:** Growing an LV but not the filesystem.
  - **Best practice:** Verify both LVM size and filesystem size.
- **Mistake:** Disabling SELinux to solve access errors.
  - **Best practice:** Diagnose labels/booleans/AVCs and keep enforcing.
- **Mistake:** Opening a firewall port without confirming a service listens.
  - **Best practice:** Verify application socket and firewall separately.
- **Mistake:** Assuming cron has your interactive environment.
  - **Best practice:** Use absolute paths and explicit environment.
- **Mistake:** Running containers as root automatically.
  - **Best practice:** Prefer rootless Podman where appropriate.
- **Mistake:** Treating performance tuning as guesswork.
  - **Best practice:** Measure before changing profiles/priorities.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the current official RH134 base version?

**Short answer:** Red Hat Enterprise Linux 10.0.

### Q2. What is the difference between cron and a systemd timer?

**Short answer:** Both schedule tasks; systemd timers integrate with systemd units, dependencies, and journal logging.

### Q3. Why is time synchronization critical?

**Short answer:** Logs, certificates, authentication, and distributed systems depend on accurate time.

### Q4. What does SELinux add beyond Unix permissions?

**Short answer:** Mandatory Access Control policy.

### Q5. What does `restorecon` do?

**Short answer:** Restores expected SELinux file contexts according to policy rules.

### Q6. What does `semanage fcontext` do?

**Short answer:** Creates persistent file-context mapping policy.

### Q7. What is a PV?

**Short answer:** LVM Physical Volume.

### Q8. What is a VG?

**Short answer:** LVM Volume Group.

### Q9. What is an LV?

**Short answer:** LVM Logical Volume.

### Q10. Why run `mount -a` after editing fstab?

**Short answer:** Validate persistent mount definitions before reboot.

### Q11. What does firewalld control?

**Short answer:** Host network filtering policy through zones/services/ports/rules.

### Q12. Why might a custom HTTP port fail even if firewalld allows it?

**Short answer:** SELinux may not allow the web-service domain to bind the port, or the app may not listen.

### Q13. What is NFS?

**Short answer:** Network File System for shared filesystem access over the network.

### Q14. What is Kickstart?

**Short answer:** Automated RHEL installation configuration.

### Q15. What is Podman?

**Short answer:** A daemonless OCI container management tool.

### Q16. What is image-based RHEL conceptually?

**Short answer:** Managing OS deployments as versioned system images rather than only in-place package transactions.

### Q17. What is the most important RH134 storage safety rule?

**Short answer:** Know exactly which device/filesystem/LV you are modifying before destructive commands.


# Enhanced Self-Assessment Bank

### Q1. Why avoid relying only on `set -e`?
**Answer:** Bash errexit has context-dependent exceptions; explicit error handling is more predictable.

### Q2. Why use `getopts`?
**Answer:** Structured short-option parsing.

### Q3. Why use `mktemp`?
**Answer:** Safely create unique temporary files/directories.

### Q4. Why use `trap`?
**Answer:** Run cleanup or other logic when a script exits or receives selected signals.

### Q5. Why use arrays for command arguments?
**Answer:** Preserve argument boundaries.

### Q6. Why avoid `eval` with untrusted input?
**Answer:** It reparses data as shell commands.

### Q7. What do `^` and `$` do in regex?
**Answer:** Start- and end-of-line anchors.

### Q8. Does regex prove an IPv4 address is valid?
**Answer:** Not necessarily; semantic validation is separate.

### Q9. What is `NR` in awk?
**Answer:** Current record number.

### Q10. Why test sed on a copy?
**Answer:** Avoid corrupting critical configuration.

### Q11. Is cron environment identical to interactive Bash?
**Answer:** Usually no.

### Q12. What extra field exists in `/etc/cron.d`?
**Answer:** The user account.

### Q13. Timer vs service?
**Answer:** Timer defines when; service defines what executes.

### Q14. What does `systemd-analyze calendar` help with?
**Answer:** Validate/interpret calendar timer expressions.

### Q15. Why structured journal fields?
**Answer:** More precise filtering than free-text grep.

### Q16. Why log persistence?
**Answer:** Preserve previous-boot and incident evidence.

### Q17. What can rsyslog do?
**Answer:** Route/store/forward logs, including remote collection.

### Q18. What does logrotate do?
**Answer:** Rotate, retain, compress, and manage text log lifecycle.

### Q19. Why is time synchronization critical?
**Answer:** TLS, authentication, logs, SIEM, and distributed systems depend on accurate time.

### Q20. DAC vs SELinux MAC?
**Answer:** Traditional discretionary permissions vs mandatory policy.

### Q21. What is a SELinux subject?
**Answer:** Usually a process/domain with a security context.

### Q22. `chcon` vs `semanage fcontext`?
**Answer:** chcon changes current label; semanage defines persistent expected mapping.

### Q23. What does `restorecon` do?
**Answer:** Applies expected SELinux label from policy mappings.

### Q24. What is a SELinux Boolean?
**Answer:** Switch enabling/disabling a predefined policy capability.

### Q25. Should `audit2allow` be first fix?
**Answer:** No; diagnose incorrect labels/configuration first.

### Q26. Is a tar archive automatically a backup?
**Answer:** No.

### Q27. Does compression encrypt?
**Answer:** No.

### Q28. Why does rsync trailing slash matter?
**Answer:** It changes whether the source directory itself or only its contents are copied.

### Q29. What should performance tuning begin with?
**Answer:** Measurement and bottleneck identification.

### Q30. What can high I/O wait indicate?
**Answer:** CPU tasks waiting on I/O.

### Q31. Does low `free` memory prove pressure?
**Answer:** No; inspect MemAvailable/cache/swap/OOM evidence.

### Q32. What does iostat help inspect?
**Answer:** Disk utilization, throughput, queueing, and latency-related metrics.

### Q33. Should tuned be changed without baseline?
**Answer:** No.

### Q34. First storage safety rule?
**Answer:** Prove the exact target device before destructive commands.

### Q35. GPT is a filesystem?
**Answer:** No; it is a partition-table format.

### Q36. Why use UUID in fstab?
**Answer:** Stable filesystem identity.

### Q37. Why `mount -a` before reboot?
**Answer:** Validate persistent mount definitions.

### Q38. Swap setup stages?
**Answer:** Allocate, mkswap, swapon, persist if needed, verify.

### Q39. PV/VG/LV?
**Answer:** Physical Volume, Volume Group, Logical Volume.

### Q40. What are LVM extents?
**Answer:** Fixed-size allocation units in the volume group.

### Q41. Does LV growth automatically grow XFS?
**Answer:** Not unless filesystem growth is also performed or integrated.

### Q42. Is an LVM snapshot an independent backup?
**Answer:** No.

### Q43. Boot chain?
**Answer:** Firmware → GRUB → kernel/initramfs → root FS → systemd.

### Q44. What is initramfs?
**Answer:** Early userspace used to reach the real root filesystem.

### Q45. What commonly builds initramfs on RHEL-family systems?
**Answer:** dracut.

### Q46. Why can bad fstab cause emergency mode?
**Answer:** Required mount units fail during boot.

### Q47. Why is console access security-sensitive?
**Answer:** Recovery paths can provide full administrative control.

### Q48. What is a firewalld zone?
**Answer:** Policy/trust context associated with interfaces/sources.

### Q49. Runtime vs permanent firewall?
**Answer:** Active current rules vs persistent configuration.

### Q50. Opening firewall starts the application?
**Answer:** No.

### Q51. Custom service port needs which layers?
**Answer:** Application listener, SELinux permission where relevant, firewall, route/network.

### Q52. What is NFS?
**Answer:** Network filesystem service/protocol.

### Q53. Why autofs?
**Answer:** Mount remote resources on demand.

### Q54. Why is Kickstart dangerous?
**Answer:** Automated storage/user configuration can destroy disks or expose credentials if wrong.

### Q55. Image vs container?
**Answer:** Image is template; container is runtime instance/process state.

### Q56. Benefit of rootless Podman?
**Answer:** Normal container operation without host-root daemon privileges.

### Q57. What does `-p 8080:80` mean?
**Answer:** Host TCP/8080 is published to container TCP/80.

### Q58. What does `:Z` mean conceptually?
**Answer:** Request private SELinux relabel suitable for container bind content.

### Q59. Is a container a VM?
**Answer:** No; it normally shares the host kernel.

### Q60. What is image-based OS management?
**Answer:** Build/deploy/version operating-system images instead of relying only on in-place package changes.

### Q61. Best RH134 troubleshooting principle?
**Answer:** Identify the owning subsystem and collect evidence before changing state.


## Completion Checklist

- [ ] I can write useful Bash admin scripts.
- [ ] I can use regex/awk/sed for real administration tasks.
- [ ] I can schedule user and system jobs.
- [ ] I can troubleshoot SELinux without disabling it.
- [ ] I can create/mount persistent filesystems safely.
- [ ] I can create and extend LVM.
- [ ] I can troubleshoot boot/fstab problems in a VM.
- [ ] I can coordinate application, SELinux, and firewalld network policy.
- [ ] I can use NFS and Podman at administration level.
- [ ] I understand Kickstart and image-mode RHEL concepts.
- [ ] I completed all labs and the services-node mini project.
