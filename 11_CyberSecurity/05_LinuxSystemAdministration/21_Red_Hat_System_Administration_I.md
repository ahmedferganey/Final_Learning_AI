# 21. Red Hat System Administration I

> Phase 5 — Linux System Administration

This module deepens Linux Essentials into **single-server Red Hat Enterprise Linux administration**.

It follows the current Red Hat System Administration I (RH124) learning scope while expanding each area with practical explanations, commands, troubleshooting logic, and labs.

The current Red Hat RH124 course is based on **Red Hat Enterprise Linux 10.0**. The examples below therefore use modern RHEL-family conventions such as:

- `systemd`
- `dnf`
- NetworkManager / `nmcli`
- OpenSSH
- RPM
- SELinux-aware administration
- Red Hat web console concepts

The objective is not to memorize command syntax. You should be able to administer one RHEL server confidently and explain why each configuration works.
## 1. Topic Title

**Red Hat System Administration I**

## 2. Learning Objectives

- Explain the Red Hat Enterprise Linux ecosystem and identify a RHEL system correctly.
- Use Bash, shell expansion, local documentation, and command-line tools efficiently.
- Navigate and manage the Linux filesystem with correct path, link, and permission semantics.
- Manage local users, groups, password-aging policy, sudo access, and file ownership.
- Install and update software with RPM and DNF and understand package repositories.
- Manage removable filesystems safely.
- Inspect, prioritize, signal, and troubleshoot processes.
- Control services and daemons with systemd.
- Inspect and configure TCP/IP networking with NetworkManager tools.
- Configure and secure SSH using host keys and user key authentication.
- Use a repeatable verification-and-troubleshooting workflow after every system change.

## 3. Prerequisites

Required:

- 20. Linux Essentials
- Phase 4 networking fundamentals
- Comfortable using Bash and `sudo`
- Ability to read Linux permissions and basic systemd output

Recommended lab:

```text
RHEL 10 / compatible lab where available
or
Rocky/Alma/RHEL-family VM for command practice

2 vCPU
4 GB RAM
30–40 GB disk
1 normal admin user
1 additional lab user
```

Where exact commands differ between RHEL releases or compatible distributions, use your installed system's manual pages and Red Hat documentation as the final authority.
## 4. Core Concepts Explanation

# Part 1 — Introduction to Red Hat Enterprise Linux

Red Hat Enterprise Linux is an enterprise Linux distribution with a lifecycle, tested package set, support model, security maintenance, certification ecosystem, and integration with Red Hat platforms.

A server administrator should distinguish:

```text
Linux kernel
    ↓
RHEL operating system
    ↓
Repositories/packages
    ↓
System services
    ↓
Applications/workloads
```

A kernel update is not the same thing as an operating-system release update.

Inspect the system:
```bash
cat /etc/redhat-release
cat /etc/os-release
uname -r
hostnamectl
rpm -q redhat-release 2>/dev/null || true
```
Useful questions when entering an unfamiliar server:

1. Which RHEL release is installed?
2. Which kernel is running?
3. Is the system registered/subscribed as expected?
4. Which repositories are enabled?
5. What is the hostname and network identity?
6. What services are running?
### Open Source, Linux Distributions, and the RHEL Ecosystem

Open source means the software source is available under its applicable licenses. Enterprise Linux adds tested integration, support lifecycle, certification, errata, and controlled software channels.

Red Hat-family relationships should be understood conceptually rather than treated as identical products.

In administration work, compatibility does not mean every subscription, repository, lifecycle, package, or support workflow is identical.
# Part 2 — Accessing the Command Line

### Shell Command Execution

```bash
date
hostname
whoami
id
pwd
printf 'User: %s
' "$USER"
```
The shell:

1. reads input,
2. parses syntax,
3. performs expansions,
4. applies redirection,
5. resolves the command,
6. executes it,
7. returns an exit status.

This matters because:

```bash
echo *.log
```

is not the same as passing the literal string `*.log`; Bash normally expands the wildcard before `echo` executes.
### Quoting and Expansion

```bash
NAME="RHEL Server"

echo $NAME
echo "$NAME"
echo '$NAME'
printf '%s
' "$NAME"

echo "Kernel: $(uname -r)"
echo "Result: $((20 + 22))"
```
Use double quotes around variable expansions unless you intentionally want word splitting or glob expansion.

Single quotes preserve literal text.

Command substitution:

```bash
$(command)
```

runs a command and substitutes its stdout.
### Shell Variables vs Environment Variables

```bash
LOCAL_VAR="only in current shell"
export REGION="me-central"

env | grep REGION
bash -c 'echo "$REGION"'
```
Child processes inherit exported environment variables, not every ordinary shell variable.
# Part 3 — Getting Help from Local Documentation

A professional administrator should be able to solve many tasks using documentation already present on the system.
```bash
man systemctl
man nmcli
man sshd_config
man 5 passwd
man 5 fstab

apropos "network connection"
whatis systemctl

systemctl --help
nmcli --help
```
### Manual Section Example

```bash
man 1 passwd
man 5 passwd
```
The first documents the `passwd` command.
The second documents the `/etc/passwd` file format.

Use `/pattern` inside `man` pages to search.
# Part 4 — Registering Systems for Red Hat Support

On subscription-managed Red Hat systems, registration connects a system to Red Hat services and content.

Inspect registration status in an appropriate authorized RHEL environment:
```bash
sudo subscription-manager status
sudo subscription-manager identity
sudo subscription-manager repos --list-enabled
```
Registration workflows depend on organization subscription policy and environment. Do not register training VMs using credentials or entitlements you are not authorized to use.

Key distinction:

```text
System registration
≠
Installing a package
≠
Enabling a repository
```

They are related but separate operations.
# Part 5 — AI-assisted Administration with RHEL Lightspeed

Current RH124 includes RHEL Lightspeed as an AI-assisted administration concept.

The correct operational mindset is:

```text
Question / observed issue
        ↓
AI suggestion
        ↓
Administrator verifies against:
- system state
- documentation
- change policy
- security requirements
        ↓
controlled execution
        ↓
verification
```

AI assistance should not replace:

- understanding the command,
- validating paths and devices,
- reviewing security impact,
- testing in nonproduction,
- confirming the result.

Never paste secrets, tokens, private configuration, or sensitive logs into an unapproved AI system.
# Part 6 — Navigating the Filesystem Hierarchy

```bash
pwd
ls -lah /
ls -lah /etc
ls -lah /var
findmnt
df -hT
```
Key RHEL locations:

```text
/etc       configuration
/home      ordinary user homes
/root      root home
/var       logs and variable application data
/usr       software, libraries, shared system content
/boot      bootloader/kernel files
/dev       device nodes
/proc      process/kernel virtual information
/sys       kernel/device virtual information
/run       runtime state
/tmp       temporary files
```

A path beginning with `/` is absolute.

A path such as:

```text
../logs/app.log
```

is relative to the current working directory.
### Path Resolution Example

```bash
mkdir -p ~/rh124/project/{conf,logs,data}
cd ~/rh124/project/conf

pwd
cd ../logs
pwd
cd -
```
# Part 7 — Managing Files from the Command Line

```bash
mkdir -p ~/rh124/files/archive

touch ~/rh124/files/report.txt

cp -v ~/rh124/files/report.txt ~/rh124/files/report.bak

mv ~/rh124/files/report.bak ~/rh124/files/archive/

ls -lah ~/rh124/files ~/rh124/files/archive
```
### Safe Removal

```bash
pwd
ls -lah

rm -i test.txt
rm -r test-directory/
```
Before recursive deletion:

```text
1. pwd
2. ls target
3. verify target path
4. remove only what is intended
```

Do not use `rm -rf` as a normal first-choice administrative habit.
### Links and File Metadata

```bash
echo "production=false" > app.conf

ln app.conf app.hardlink
ln -s app.conf app.symlink

ls -li app.conf app.hardlink app.symlink
stat app.conf
```
Hard link:
- same inode.

Symbolic link:
- separate inode containing a target path.

This difference matters when configuration links, log links, and filesystem boundaries are involved.
# Part 8 — Editing Text Files

System administration is largely configuration-file administration.

You should be comfortable with at least one terminal editor.

With Vim:
```text
i           insert
Esc         command mode
:w          save
:q          quit
:wq         save and quit
:q!         discard changes and quit
/pattern    search
dd          delete current line
u           undo
```
### Configuration Editing Workflow

```bash
sudo cp -a /etc/ssh/sshd_config /etc/ssh/sshd_config.before-rh124-lab

sudo vim /etc/ssh/sshd_config

sudo sshd -t
```
Good workflow:

```text
backup
→ edit
→ syntax validation
→ controlled reload/restart
→ verify
→ inspect logs
```
# Part 9 — Redirecting Shell Input and Output

```bash
hostname > host.txt
uname -r >> host.txt

find /etc -name "*.conf" > config-files.txt 2> find-errors.txt

systemctl --failed | tee failed-services.txt
```
Streams:

```text
0 stdin
1 stdout
2 stderr
```

Examples:

```bash
command > file        # stdout overwrite
command >> file       # stdout append
command 2> file       # stderr
command > file 2>&1   # both into same file
```
### Pipeline Example

```bash
rpm -qa | sort | grep -i openssh
ps -eo user,pid,%cpu,%mem,cmd --sort=-%cpu | head
journalctl -u sshd | grep -i failed
```
A pipeline passes data between commands. Test each stage separately before debugging a large pipeline.
# Part 10 — Managing Local Users and Groups

### User Account Files

```bash
getent passwd
getent group
sudo getent shadow root
```
Important account databases include:

```text
/etc/passwd
/etc/shadow
/etc/group
/etc/gshadow
```

Prefer `getent` where appropriate because it can also work with configured name-service sources beyond local files.
### Create and Manage Users

```bash
sudo groupadd operations

sudo useradd -m -c "Operations Student" -G operations student1
sudo passwd student1

id student1
getent passwd student1
getent group operations
```
### Password Aging

```bash
sudo chage -l student1
sudo chage -M 90 -m 1 -W 7 student1
sudo chage -d 0 student1
```
Concepts:

- minimum password age,
- maximum password age,
- warning period,
- forced password change.

Do not apply arbitrary aging policies without organizational requirements.
### Lock and Unlock

```bash
sudo passwd -l student1
sudo passwd -u student1
```
### Administrative Access with sudo

```bash
sudo -l
sudo visudo
```
Never edit `/etc/sudoers` with an ordinary editor when `visudo` is available because syntax errors can break administrative access.

Prefer group or drop-in policy where appropriate:

```text
/etc/sudoers.d/
```
# Part 11 — Controlling Access to Files

```bash
mkdir -p ~/rh124/secure
touch ~/rh124/secure/app.conf

chmod 640 ~/rh124/secure/app.conf
ls -l ~/rh124/secure/app.conf

sudo chown root:operations ~/rh124/secure/app.conf
```
Mode `640`:

```text
owner: rw-
group: r--
other: ---
```

Do not solve permission errors with:

```text
chmod 777
```

Instead identify:
- required owner,
- required group,
- required read/write/execute access.
### Directory Permission Semantics

For directories:

```text
r = list directory names
w = create/remove entries
x = traverse/access names
```

Example:

A user may know that `/secure/report.txt` exists, but without execute permission on `/secure`, they cannot traverse the path normally.
### Special Permissions Review

```bash
ls -ld /tmp
ls -l /usr/bin/passwd
```
Sticky bit on shared directories and SUID/SGID on selected executables/directories have significant security implications. Do not add special bits casually.
# Part 12 — Installing and Updating Software with RPM and DNF

### Query Packages

```bash
rpm -q bash
rpm -qi bash
rpm -ql bash
rpm -qf /usr/bin/ssh

dnf search nginx
dnf info nginx
dnf list installed
dnf repolist
```
### Install and Update

```bash
sudo dnf install nginx
sudo dnf update nginx
sudo dnf remove nginx
```
DNF:
- resolves dependencies,
- uses repository metadata,
- records transactions.

Inspect transaction history:
```bash
dnf history
dnf history info
```
### Package vs Service

Installing `httpd` does not necessarily mean it is:

- running,
- enabled at boot,
- allowed through firewall,
- correctly configured.

Verification example:
```bash
rpm -q httpd
systemctl status httpd
ss -tlnp | grep ':80'
```
# Part 13 — Flatpak Applications

Current RH124 includes Flatpak for desktop/application delivery.

Flatpak is different from RPM package administration. It uses application runtimes and repositories/remotes for sandbox-oriented desktop application distribution.

Inspect:
```bash
flatpak --version
flatpak remotes
flatpak list
```
If Flatpak is not installed or relevant on your server image, learn the concept but do not force it into a server-only environment.
# Part 14 — Accessing Removable Media

```bash
lsblk -f
blkid
findmnt

sudo mkdir -p /mnt/labmedia
sudo mount /dev/sdb1 /mnt/labmedia

findmnt /mnt/labmedia

sudo umount /mnt/labmedia
```
Critical safety rule:

Never copy a device name such as `/dev/sdb1` from a tutorial without checking your own `lsblk -f` output. Device names differ between systems.

Before unmounting:
- leave the mounted directory,
- ensure processes are not using it.
# Part 15 — Monitoring and Managing Linux Processes

```bash
ps aux
ps -ef

ps -eo pid,ppid,user,stat,%cpu,%mem,cmd --sort=-%cpu | head

top

pgrep -a sshd
```
### Process States

Common `ps` state letters include concepts such as:

```text
R  running/runnable
S  interruptible sleep
D  uninterruptible sleep
T  stopped/traced
Z  zombie
```

A zombie is already terminated but still has an unreaped process-table entry. Killing the zombie itself does not solve the parent-process problem.
### Signals

```bash
kill -TERM 1234
kill -HUP 1234
kill -KILL 1234
```
Use SIGKILL only when graceful mechanisms fail. A process receiving SIGKILL cannot cleanly flush state or release resources through its own handlers.
### Jobs and Priorities

```bash
sleep 600 &
jobs

nice -n 10 some-command
sudo renice 5 -p 1234
```
# Part 16 — Controlling Services and Daemons

```bash
systemctl status sshd

sudo systemctl start sshd
sudo systemctl stop sshd
sudo systemctl restart sshd
sudo systemctl reload sshd

sudo systemctl enable sshd
sudo systemctl enable --now sshd

systemctl is-active sshd
systemctl is-enabled sshd
systemctl --failed
```
Distinguish:

```text
active/inactive = runtime state
enabled/disabled = boot activation policy
```
### Unit Dependencies

```bash
systemctl list-dependencies sshd.service
systemctl cat sshd.service
systemctl show sshd.service
```
# Part 17 — Introduction to Networking

On a RHEL server, basic network troubleshooting should always separate:

```text
link
↓
IP address
↓
local subnet
↓
default route
↓
DNS
↓
transport port
↓
application
```
```bash
ip -br link
ip -br address
ip route
ip neigh

ping -c 3 192.168.1.1
dig example.com
ss -tulpen
```
### Troubleshooting Example

```text
Problem:
curl https://example.com fails.

Check:
1. ip link
2. ip address
3. ip route
4. ping gateway
5. dig example.com
6. curl -v https://example.com
7. firewall/proxy/application policy
```
# Part 18 — Managing Network Configuration

RHEL uses NetworkManager as the primary network configuration service in modern releases.

Key objects:

```text
device       = interface visible to the OS
connection   = NetworkManager configuration profile
```
```bash
nmcli device status
nmcli connection show
nmcli connection show --active
```
### Create a Static IPv4 Connection

```bash
sudo nmcli connection add   type ethernet   ifname enp1s0   con-name static-lab   ipv4.method manual   ipv4.addresses 192.168.56.20/24   ipv4.gateway 192.168.56.1   ipv4.dns "192.168.56.1 1.1.1.1"

sudo nmcli connection up static-lab
```
Do not run this blindly over your only remote management connection. Changing the active interface can disconnect you.

Verification:
```bash
ip -br address
ip route
cat /etc/resolv.conf
nmcli connection show static-lab
```
### Modify an Existing Connection

```bash
sudo nmcli connection modify static-lab ipv4.dns "192.168.56.53"
sudo nmcli connection up static-lab
```
# Part 19 — Configuring and Securing SSH

### SSH Host Keys vs User Keys

**Host key**
Identifies the SSH server.

**User key pair**
Authenticates a user.

Client first-time connection:
```text
Client
  |
  | receives server host key
  v
known_hosts check
  |
  | user authentication
  v
password or public-key authentication
```
### Generate a User Key

```bash
ssh-keygen -t ed25519 -C "rh124-lab"
ssh-copy-id student1@server02
ssh student1@server02
```
### Inspect Known Hosts

```bash
ls -la ~/.ssh
ssh-keygen -F server02
```
### SSH Server Configuration

```bash
sudo cp -a /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

sudo vim /etc/ssh/sshd_config

sudo sshd -t
sudo systemctl reload sshd
sudo journalctl -u sshd --since "10 minutes ago"
```
Safe remote-change rule:

Keep the current SSH session open while testing a second connection.

Do not disable password login until key authentication has been verified for the required administrative users.
# Part 20 — Comprehensive Administration Workflow

A professional change should look like:

```text
Requirement
   ↓
Inspect current state
   ↓
Back up important config
   ↓
Make smallest necessary change
   ↓
Validate syntax
   ↓
Apply/reload
   ↓
Verify runtime behavior
   ↓
Inspect logs
   ↓
Document
```

Example: change SSH policy.

```bash
sudo cp -a /etc/ssh/sshd_config /etc/ssh/sshd_config.prechange
sudo vim /etc/ssh/sshd_config
sudo sshd -t
sudo systemctl reload sshd
systemctl status sshd
ss -tlnp | grep ':22'
journalctl -u sshd --since "5 minutes ago"
```

# Enhanced Deep-Study Layer — RH124 / Single-Server RHEL Administration

The original course content is preserved. This section expands it into a deeper administration guide with operating-system internals, safer command patterns, diagrams, verification steps, troubleshooting methods, and security reasoning.

A system change should follow this model:

```text
Requirement
    ↓
Inspect current state
    ↓
Identify the subsystem that owns the state
    ↓
Back up / plan rollback
    ↓
Make the smallest necessary change
    ↓
Validate syntax or structure
    ↓
Apply / reload / restart only when required
    ↓
Verify runtime state
    ↓
Verify persistence
    ↓
Inspect logs
    ↓
Document
```

A Linux administrator should always be able to answer:

```text
What changed?
Where is it stored?
What process/kernel subsystem consumes it?
Is the change active now?
Will it survive reboot?
What proves success?
How do I undo it?
```

---

## Enhanced Deep Dive 1 — RHEL Identity: OS Release, Kernel, Architecture, and Host Identity

Several identifiers describe one server and they are not interchangeable.

```text
RHEL host
├── Distribution release
├── Running kernel
├── Installed kernel packages
├── CPU architecture
├── Hostname
├── Machine ID
└── Registration/subscription identity where used
```

Inspect:

```bash
cat /etc/os-release
cat /etc/redhat-release
uname -r
uname -m
hostnamectl
cat /etc/machine-id
rpm -q kernel
```

Example interpretation:

```text
/etc/os-release
→ which operating-system release/package ecosystem is installed

uname -r
→ the kernel currently executing

rpm -q kernel
→ kernel packages present on disk
```

This matters because a new kernel may be installed but not active until reboot.

### Practical troubleshooting example

Suppose:

```bash
rpm -q kernel
```

shows:

```text
kernel-A
kernel-B
```

but:

```bash
uname -r
```

shows `kernel-A`.

The newer kernel may be installed but the host is still running the older kernel.

Do not say "the kernel update did not install" until you distinguish **installed state** from **running state**.

---

## Enhanced Deep Dive 2 — RPM Package Identity: NEVRA

RPM package identity is richer than a package name.

Conceptually:

```text
Name-[Epoch:]Version-Release.Architecture
```

Often summarized as:

```text
N E V R A
```

Inspect:

```bash
rpm -q bash
rpm -q --qf '%{NAME}\n%{EPOCHNUM}\n%{VERSION}\n%{RELEASE}\n%{ARCH}\n' bash
```

Why the fields matter:

```text
Name
→ logical software package

Epoch
→ special RPM version-order override

Version
→ upstream software version

Release
→ distribution packaging revision

Architecture
→ x86_64, aarch64, noarch, ...
```

A packaging/security update can change the RPM release even if the upstream application version looks familiar.

---

## Enhanced Deep Dive 3 — Registration, Repository, DNF, and RPM Are Separate Layers

Do not treat "RHEL registration" and "package installation" as the same operation.

```text
Registration / entitlement
        ↓
Repository availability
        ↓
Repository metadata
        ↓
DNF dependency solver
        ↓
RPM transaction
        ↓
Installed files and RPM database
```

Useful commands:

```bash
sudo subscription-manager status 2>/dev/null || true
sudo subscription-manager identity 2>/dev/null || true

dnf repolist
dnf repolist -v
dnf makecache
dnf history
rpm -qa | head
```

### DNF failure decision tree

```text
dnf install fails
    ↓
Can DNS/network reach repository?
    ↓
Is expected repository enabled?
    ↓
Can metadata be downloaded?
    ↓
Does package exist?
    ↓
Can dependencies be solved?
    ↓
Does GPG verification succeed?
    ↓
Can RPM transaction write to disk?
```

Do not disable signature checks simply because package installation fails.

---

## Enhanced Deep Dive 4 — Bash Command Resolution

When you type a command, Bash may execute:

```text
alias
function
builtin
external executable
```

Inspect:

```bash
type -a cd
type -a echo
type -a ls
type -a python 2>/dev/null || true
command -V systemctl
```

Why this matters:

```text
interactive shell:
ls → alias with color options

script/noninteractive shell:
ls → /usr/bin/ls
```

Different command resolution can create "works in my terminal" problems.

---

## Enhanced Deep Dive 5 — Bash Parsing and Expansion Order

The program does not receive exactly what you typed.

A simplified model:

```text
Typed command
   ↓
Bash parses shell syntax
   ↓
Parameter expansion
   ↓
Command substitution
   ↓
Arithmetic expansion
   ↓
Word splitting
   ↓
Pathname expansion / globbing
   ↓
Redirections
   ↓
Command lookup
   ↓
Program receives final arguments
```

Example:

```bash
name='server one'

printf '<%s>\n' $name
printf '<%s>\n' "$name"
```

Unquoted:

```text
<server>
<one>
```

Quoted:

```text
<server one>
```

This is why:

```bash
"$variable"
```

should normally be your default.

---

## Enhanced Deep Dive 6 — Wildcards / Globbing vs Regular Expressions

Shell globbing is not regex.

```text
Glob:   *.log
Regex:  .*\.log$
```

Common globs:

```text
*        zero or more characters
?        one character
[a-z]    one character from range
[!0-9]   one character not in set
```

Example:

```bash
printf '%s\n' *.conf
printf '%s\n' file?.txt
printf '%s\n' server[1-4].log
```

A glob is normally expanded by Bash before the target command executes.

```text
rm *.tmp
   ↓ shell expansion
rm a.tmp b.tmp c.tmp
```

Therefore always verify destructive wildcard operations:

```bash
printf '%s\n' *.tmp
```

before:

```bash
rm -- *.tmp
```

in a controlled directory.

---

## Enhanced Deep Dive 7 — Exit Status and Command Control

Commands return an exit status.

Convention:

```text
0      success
nonzero failure / alternate result
```

Inspect:

```bash
true
echo "$?"

false
echo "$?"
```

`&&` runs the next command only after success:

```bash
mkdir -p /tmp/report &&
printf 'directory ready\n'
```

`||` runs the next command after failure:

```bash
systemctl is-active --quiet sshd ||
printf 'sshd is not active\n'
```

For important administration logic, prefer a clear `if`:

```bash
if systemctl is-active --quiet sshd; then
    echo "active"
else
    echo "inactive"
fi
```

---

## Enhanced Deep Dive 8 — Local Documentation as an Administration Skill

Use several help systems.

```text
Bash builtin
→ help

Command/file/system call
→ man

Search manual database
→ apropos / man -k

Short description
→ whatis

GNU manual
→ info

Installed package docs
→ rpm -qd
```

Examples:

```bash
help cd

man 1 passwd
man 5 passwd
man 5 fstab
man 5 sshd_config

apropos "network connection"
whatis systemctl

rpm -qd bash | head
info coreutils 2>/dev/null || true
```

Manual sections matter:

```text
1 user commands
2 system calls
3 library calls
4 devices
5 file formats
8 administration commands
```

---

## Enhanced Deep Dive 9 — Linux Filesystem Hierarchy as Operational Responsibility

Think about purpose, not memorization.

```text
/
├── /etc    host configuration
├── /var    variable state/logs/cache
├── /usr    installed software/shareable data
├── /run    volatile runtime state
├── /home   user homes
├── /root   root home
├── /boot   boot files/kernel/initramfs
├── /dev    device nodes
├── /proc   process/kernel virtual data
├── /sys    kernel/device virtual data
├── /srv    service data in some designs
└── /opt    optional application trees
```

Why location matters:

```text
configuration backup policy
SELinux default labels
filesystem/mount design
package ownership
log rotation
boot behavior
```

---

## Enhanced Deep Dive 10 — Path Resolution and Parent Directory Execute Permission

Linux resolves:

```text
/srv/app/config/app.conf
```

component by component.

```text
/
↓
srv
↓
app
↓
config
↓
app.conf
```

A user needs directory traversal permission through the path.

Useful command:

```bash
namei -l /srv/app/config/app.conf
```

A file can have:

```text
-rw-r--r--
```

and still be inaccessible if a parent directory denies `x`.

### Troubleshooting sequence

```bash
id
namei -l /path/to/file
ls -l /path/to/file
getfacl /path/to/file 2>/dev/null || true
```

Do not jump directly to:

```bash
chmod 777
```

---

## Enhanced Deep Dive 11 — Inodes, Directory Entries, Hard Links, and Delete Semantics

Simplified filesystem model:

```text
Directory
app.conf ──────> inode 8123
                  ├── UID
                  ├── GID
                  ├── permissions
                  ├── timestamps
                  ├── size
                  └── data extents
```

Hard link:

```bash
printf 'demo\n' > app.conf
ln app.conf app.hard

ls -li app.conf app.hard
```

Both names point to the same inode.

Delete one:

```bash
rm app.conf
cat app.hard
```

Data remains because another directory entry still references the inode.

A file's storage is normally reclaimable only after:

```text
link count becomes zero
AND
no process still holds the file open
```

This explains deleted-but-open logs.

Inspect:

```bash
sudo lsof +L1
```

---

## Enhanced Deep Dive 12 — Symbolic Links

A symlink stores a target path.

```bash
ln -s ../shared/app.conf current/app.conf

readlink current/app.conf
readlink -f current/app.conf
```

Relative symlink resolution is based on the directory containing the link.

```text
current/app.conf
contains:
../shared/app.conf
```

This is useful when moving an entire application tree while preserving relative relationships.

---

## Enhanced Deep Dive 13 — Safe Filenames and `--`

A filename can begin with `-`.

Example:

```bash
touch -- -danger
```

Unsafe:

```bash
rm -danger
```

Safer:

```bash
rm -- -danger
```

`--` tells many commands:

```text
stop parsing options
everything after this is an operand/filename
```

Scripts handling arbitrary filenames should also avoid parsing `ls` output.

---

## Enhanced Deep Dive 14 — File Descriptors and I/O Redirection

Every process normally starts with:

```text
fd 0 → stdin
fd 1 → stdout
fd 2 → stderr
```

Redirection changes those descriptors.

```bash
find /etc -maxdepth 1 -type f \
  > normal.txt \
  2> errors.txt
```

Mental model:

```text
find process
├── fd1 → normal.txt
└── fd2 → errors.txt
```

### Redirection order

These differ:

```bash
command > all.log 2>&1
```

and:

```bash
command 2>&1 > only-stdout.log
```

Redirections are applied left-to-right.

---

## Enhanced Deep Dive 15 — Pipelines and `pipefail`

Pipeline:

```bash
journalctl -u sshd |
grep -i failed |
tail
```

Data flow:

```text
journalctl stdout
      ↓
grep stdin/stdout
      ↓
tail stdin/stdout
      ↓
terminal
```

Without `pipefail`, an early command can fail while the last command succeeds.

Example:

```bash
set -o pipefail

grep root /does/not/exist |
wc -l

echo "$?"
```

This matters in automation and monitoring scripts.

---

## Enhanced Deep Dive 16 — Identity: NSS, UID, GID, and `getent`

Linux access control uses numeric UIDs and GIDs.

Names are resolved for humans.

```bash
id
getent passwd "$USER"
getent group wheel
```

NSS configuration:

```bash
grep '^passwd:' /etc/nsswitch.conf
grep '^group:' /etc/nsswitch.conf
```

Possible identity sources include:

```text
files
SSSD
LDAP
directory services
other configured providers
```

Therefore:

```bash
grep user /etc/passwd
```

does not always answer:

```text
Does Linux know this user?
```

`getent` is often the better question.

---

## Enhanced Deep Dive 17 — Primary and Supplementary Groups

A process can have:

```text
UID
primary GID
supplementary GIDs
```

Example:

```bash
id student1
```

A user's primary group commonly affects the default group owner of files they create.

Supplementary groups provide access to additional group-owned resources.

After changing group membership:

```bash
sudo usermod -aG operations student1
```

an already running login session may retain the old group list.

Re-authenticate/re-login before concluding that group management failed.

---

## Enhanced Deep Dive 18 — Password Aging, Account Locking, and Login Shells

Independent account controls include:

```text
password state
password age
account expiration
login shell
SSH/PAM policy
sudo authorization
```

Inspect:

```bash
passwd -S student1
chage -l student1
getent passwd student1
```

A password lock is not the same as:

```text
delete account
expire account
remove SSH keys
remove tokens
remove sudo rights
```

Offboarding is a broader access-lifecycle process.

---

## Enhanced Deep Dive 19 — sudo and Least Privilege

Inspect permitted commands:

```bash
sudo -l
```

Edit policy safely:

```bash
sudo visudo
```

or use validated drop-ins:

```text
/etc/sudoers.d/
```

Example principle:

```text
operations group
→ may restart one approved service
→ may not open unrestricted root shell
```

Be careful: some commands that look narrow can execute shell escapes.

Editors, pagers, interpreters, or programs that launch other commands can accidentally turn a "specific command" rule into broad root access.

---

## Enhanced Deep Dive 20 — Permissions, Umask, SGID, Sticky Bit, ACL

### Umask

Common creation model:

```text
regular file base 666
directory base    777
```

With:

```bash
umask 022
```

typical results:

```text
file      644
directory 755
```

Inspect:

```bash
umask
umask -S
```

### SGID directory

```bash
sudo chgrp operations /srv/operations
sudo chmod 2770 /srv/operations
```

New files inherit the directory group.

### Sticky directory

```bash
ls -ld /tmp
```

Typical:

```text
drwxrwxrwt
```

Users can create files but normally cannot remove another user's entries.

### ACL

```bash
getfacl /srv/operations

sudo setfacl -m u:student1:rx /srv/operations
getfacl /srv/operations
```

Remember the ACL mask can limit effective named-user/group permissions.

---

## Enhanced Deep Dive 21 — RPM Ownership and Verification

Find package owner:

```bash
rpm -qf /usr/bin/ssh
```

List files:

```bash
rpm -ql openssh-clients | head
```

Verify package-managed content:

```bash
rpm -V openssh-clients
```

RPM verification compares current filesystem metadata/content with package database expectations.

A difference can mean:

```text
legitimate admin change
application-generated change
corruption
unexpected modification
```

It is evidence, not automatic proof of compromise.

---

## Enhanced Deep Dive 22 — DNF Transactions and Repository Trust

Useful commands:

```bash
dnf repolist
dnf info nginx
dnf list installed
dnf history
dnf history info last
```

Repository trust questions:

```text
Who operates this repository?
Is package signature verification enabled?
Is it required by support policy?
Is it vendor, organization, or third party?
```

Every extra repository expands the software supply-chain trust boundary.

---

## Enhanced Deep Dive 23 — Removable Media: Correct State Sequence

```text
device attached
   ↓
identify block device
   ↓
identify filesystem
   ↓
mount point
   ↓
mount
   ↓
verify
   ↓
use
   ↓
check open processes
   ↓
unmount
```

Commands:

```bash
lsblk -f
blkid
findmnt

sudo mount /dev/<verified-partition> /mnt/labmedia

lsof +f -- /mnt/labmedia 2>/dev/null || true

sudo umount /mnt/labmedia
```

Never copy `/dev/sdb1` blindly from a tutorial.

---

## Enhanced Deep Dive 24 — Process Tree, States, Signals, and Priorities

Inspect:

```bash
ps -eo pid,ppid,user,state,ni,%cpu,%mem,cmd --forest
top
pgrep -a sshd
```

Common states:

```text
R running/runnable
S interruptible sleep
D uninterruptible sleep
T stopped
Z zombie
```

A zombie has already exited. It is waiting for the parent to collect the exit status.

Signals:

```text
SIGTERM graceful termination request
SIGHUP  application-specific, often reload
SIGINT  interrupt
SIGSTOP stop
SIGCONT continue
SIGKILL immediate kernel termination
```

Commands:

```bash
kill -TERM <pid>
kill -STOP <pid>
kill -CONT <pid>
kill -KILL <pid>
```

Use KILL last.

Niceness:

```bash
nice -n 10 command
renice 15 -p <pid>
```

Nice is a scheduler preference, not a hard CPU quota.

---

## Enhanced Deep Dive 25 — systemd Units, Dependencies, Drop-Ins, and State

A service is only one unit type.

```text
.service
.socket
.timer
.mount
.target
.path
.device
```

Inspect:

```bash
systemctl cat sshd.service
systemctl show sshd.service
systemctl list-dependencies sshd.service
```

### Active vs enabled

```text
active
→ running now

enabled
→ boot/dependency activation policy
```

Commands:

```bash
systemctl is-active sshd
systemctl is-enabled sshd
```

### Drop-in override

Prefer:

```bash
sudo systemctl edit sshd.service
```

over modifying the vendor unit directly.

Mental model:

```text
vendor unit
+
administrator drop-in
=
effective unit
```

After editing a unit definition:

```bash
sudo systemctl daemon-reload
```

This is different from restarting the service.

---

## Enhanced Deep Dive 26 — Service Troubleshooting Workflow

Do not restart repeatedly without evidence.

```text
Service unavailable
    ↓
Package installed?
    ↓
Config syntax valid?
    ↓
systemd active?
    ↓
Journal error?
    ↓
Socket listening?
    ↓
Firewall/network?
    ↓
SELinux?
    ↓
Application health?
```

Example SSH investigation:

```bash
rpm -q openssh-server
sudo sshd -t

systemctl status sshd --no-pager
journalctl -u sshd -b --no-pager | tail -n 100

ss -lntp | grep ':22'
```

Capture logs before a restart if the failure is important.

---

## Enhanced Deep Dive 27 — Linux Networking Layer Model

Use the same networking discipline from Phase 4.

```text
interface/device
   ↓
carrier/link
   ↓
IP address/prefix
   ↓
route
   ↓
ARP/NDP neighbor
   ↓
DNS
   ↓
TCP/UDP socket
   ↓
application
```

Commands:

```bash
ip -br link
ip -br address
ip route
ip -6 route
ip neigh

getent hosts example.com
ss -tulpen
```

Never troubleshoot DNS first when the interface has no address.

---

## Enhanced Deep Dive 28 — NetworkManager Device vs Connection

```text
Device
→ actual interface known to OS

Connection
→ saved NetworkManager configuration profile
```

One device can have multiple profiles.

Example:

```text
enp1s0
├── office-dhcp
└── lab-static
```

Inspect:

```bash
nmcli device status
nmcli connection show
nmcli connection show --active
nmcli device show enp1s0
```

Activation model:

```text
connection profile
      ↓
NetworkManager
      ↓
kernel device state
├── address
├── route
└── resolver-related config
```

A temporary `ip address add` change is not the same as a persistent NetworkManager profile.

---

## Enhanced Deep Dive 29 — Static Network Profile Safely

Before changing the only remote interface:

```text
STOP
```

Use console/OOB access or another interface.

Typical sequence:

```bash
nmcli device status
nmcli connection show --active
```

Create a **lab** profile:

```bash
sudo nmcli connection add \
  type ethernet \
  ifname enp2s0 \
  con-name rh124-static \
  ipv4.method manual \
  ipv4.addresses 192.0.2.20/24 \
  ipv4.gateway 192.0.2.1 \
  ipv4.dns 192.0.2.53
```

Inspect before activation:

```bash
nmcli connection show rh124-static
```

Activate:

```bash
sudo nmcli connection up rh124-static
```

Verify:

```bash
ip -br address
ip route
nmcli device show enp2s0
getent hosts example.com
```

Use addresses appropriate to your isolated lab.

---

## Enhanced Deep Dive 30 — Host Routing

Linux hosts route packets too.

Inspect:

```bash
ip route
ip route get 8.8.8.8
```

Model:

```text
destination IP
    ↓
route table lookup
    ↓
local subnet?
 ├── yes → resolve destination with ARP/NDP
 └── no  → resolve next-hop gateway
```

For a remote destination:

```text
IP destination
= remote server

Ethernet destination
= local gateway MAC
```

This distinction is critical.

---

## Enhanced Deep Dive 31 — DNS: NSS, `/etc/hosts`, and Resolver State

Applications often call:

```text
getaddrinfo()
```

rather than speaking DNS directly.

NSS controls lookup sources.

```bash
grep '^hosts:' /etc/nsswitch.conf
getent ahosts example.com
cat /etc/resolv.conf
nmcli device show | grep -E 'IP4.DNS|IP6.DNS'
```

If `/etc/resolv.conf` changes are overwritten, determine which service manages it instead of repeatedly editing generated state.

---

## Enhanced Deep Dive 32 — SSH Architecture

SSH connection:

```text
DNS/IP
  ↓
TCP connection
  ↓
server host key
  ↓
known_hosts validation
  ↓
user authentication
  ↓
account/PAM policy
  ↓
session
```

Two key concepts:

```text
Host key
→ authenticates the server

User key pair
→ authenticates the user
```

Client:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
~/.ssh/known_hosts
~/.ssh/config
```

Server-side user authorization:

```text
~/.ssh/authorized_keys
```

Never copy the private user key to the server.

---

## Enhanced Deep Dive 33 — SSH Host-Key Changes

A host-key warning can mean:

```text
legitimate reinstall
legitimate rekey
IP reassigned
DNS wrong
or possible interception
```

Safe process:

```text
1. stop
2. identify expected server
3. verify fingerprint through console/trusted inventory
4. verify DNS/IP
5. update known_hosts only after verification
```

Commands:

```bash
ssh-keygen -F app01.lab.example
ssh-keygen -R app01.lab.example
```

`ssh-keygen -R` removes a stored key; it does **not** prove the replacement key is trustworthy.

---

## Enhanced Deep Dive 34 — SSH Client Configuration

Example:

```text
Host app01
    HostName app01.lab.example
    User admin1
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60
```

Inspect effective config:

```bash
ssh -G app01 | head -n 50
```

Connect:

```bash
ssh app01
```

This reduces copied long command lines and makes automation clearer.

---

## Enhanced Deep Dive 35 — Single-Server Baseline

Before major changes, record:

```text
OS/kernel
time
users/groups
repositories/packages
mounts/filesystem use
network
listeners
services
failed units
recent errors
```

Commands:

```bash
cat /etc/os-release
uname -r
timedatectl

lsblk -f
findmnt
df -hT

ip -br address
ip route
ss -tulpen

systemctl --failed
journalctl -p err -b --no-pager | tail -n 50
```

A baseline answers:

```text
What changed since the system was healthy?
```

---

## Enhanced Deep Dive 36 — Permission-Denied Decision Tree

```text
permission denied
   ↓
correct UID/GID?
   ↓
parent path x permission?
   ↓
mode bits?
   ↓
ACL?
   ↓
mount ro/noexec?
   ↓
SELinux?
   ↓
service sandbox/capabilities?
```

Commands:

```bash
id
namei -l /path/to/object
getfacl /path/to/object 2>/dev/null || true
findmnt -T /path/to/object
getenforce 2>/dev/null || true
```

This is why:

```bash
chmod 777
```

is not professional troubleshooting.

---

## Enhanced Deep Dive 37 — Runtime State vs Persistent State

Examples:

```text
systemctl start service
→ runtime

systemctl enable service
→ persistent boot activation policy

ip address add ...
→ runtime

NetworkManager profile
→ persistent intent

mount /dev/... /data
→ runtime

/etc/fstab
→ persistent mount intent
```

A correct change report should explicitly state:

```text
current state verified
persistent state verified
reboot behavior understood
```

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — System Identity Baseline

Create `RH124_SYSTEM_IDENTITY.md`.

Include:

```bash
cat /etc/os-release
uname -r
uname -m
hostnamectl
rpm -q kernel
```

Explain the meaning of every line.

## Enhanced Lab 2 — Package NEVRA

Choose 10 installed packages.

Record:

```text
name
epoch
version
release
architecture
five important files
```

Use `rpm -q`, `rpm -ql`, and query formatting.

## Enhanced Lab 3 — Bash Expansion

Create filenames with:

```text
spaces
wildcards
leading dash
```

Practice quoting, globs, `--`, arrays, and command substitution.

## Enhanced Lab 4 — Exit Status

Create a script checking five commands and reporting each exit code.

Then rewrite using `if` statements.

## Enhanced Lab 5 — Local Documentation

Solve 15 administration questions using only:

```text
help
man
apropos
whatis
info
rpm package docs
```

## Enhanced Lab 6 — Path Traversal

Create nested directories and remove execute permission from one parent for a test user.

Use:

```bash
namei -l
```

to locate the failure.

## Enhanced Lab 7 — Hard Links and Inodes

Create:

```text
original
hard1
hard2
```

Record inode/link count, remove names one by one, and explain data lifetime.

## Enhanced Lab 8 — Symlink Resolution

Create relative and absolute symlinks.

Move the containing tree and compare behavior.

## Enhanced Lab 9 — File Descriptors

Generate stdout and stderr.

Test:

```bash
>file 2>&1
```

versus:

```bash
2>&1 >file
```

Explain every descriptor.

## Enhanced Lab 10 — Pipeline Failure

Demonstrate a failure hidden by a successful final pipeline stage.

Enable:

```bash
set -o pipefail
```

and compare.

## Enhanced Lab 11 — NSS

Compare:

```bash
grep /etc/passwd
getent passwd
```

Inspect `nsswitch.conf`.

## Enhanced Lab 12 — User Lifecycle

Create a lab user.

Practice:

```text
group membership
password aging
password lock
account expiration
shell change
clean removal
```

## Enhanced Lab 13 — sudo Policy

Create a safe `/etc/sudoers.d/` lab rule using `visudo`.

Analyze whether the permitted program has a shell escape.

## Enhanced Lab 14 — Umask

Test:

```text
022
027
077
```

Predict file/directory modes before creation.

## Enhanced Lab 15 — Shared Operations Directory

Create `/srv/operations`.

Use:

```text
group ownership
SGID
precise mode
optional default ACL
```

Test with two users.

## Enhanced Lab 16 — ACL Mask

Create an ACL granting access, then deliberately limit it using the mask.

Use `getfacl` to explain effective rights.

## Enhanced Lab 17 — RPM Ownership

Choose 15 executables.

Identify their owning packages and inspect package verification output.

## Enhanced Lab 18 — DNF History

Install and remove a harmless package.

Reconstruct the change from `dnf history`.

## Enhanced Lab 19 — Repository Trust

Document every enabled repository:

```text
source
GPG checking
vendor/third-party
purpose
```

## Enhanced Lab 20 — Removable Storage

Use a disposable extra virtual disk/filesystem.

Perform:

```text
identify
mount
verify
use
check open processes
unmount
```

## Enhanced Lab 21 — Process Tree

Start a nested Bash/background process tree and draw PID/PPID relationships.

## Enhanced Lab 22 — Process States and Signals

Use controlled processes to observe:

```text
S
T
TERM
STOP
CONT
KILL
```

## Enhanced Lab 23 — Nice/Renice

Run controlled CPU tasks with different niceness values.

Explain that nice is not a hard CPU quota.

## Enhanced Lab 24 — systemd Unit Anatomy

Choose three services.

Record:

```text
unit path
drop-ins
ExecStart
dependencies
ordering
active state
enabled state
```

## Enhanced Lab 25 — systemd Drop-In

Create a harmless service override with:

```bash
systemctl edit
```

Verify the effective unit and remove the override afterward.

## Enhanced Lab 26 — Journal-First Troubleshooting

Break a safe demo service.

Collect:

```text
status
journal
config validation
socket state
```

before fixing it.

## Enhanced Lab 27 — Linux Network Map

For one interface, document:

```text
device state
active profile
MAC
IPv4
IPv6
routes
neighbors
DNS
listeners
```

## Enhanced Lab 28 — NetworkManager Profiles

On a second lab NIC, create:

```text
DHCP profile
static profile
```

Activate each and compare runtime state.

## Enhanced Lab 29 — Route Lookup

Use `ip route get` for:

```text
loopback
local subnet
remote/default route
```

Explain the next hop.

## Enhanced Lab 30 — DNS Resolution

Compare:

```bash
getent hosts
cat /etc/resolv.conf
nmcli device show
dig
```

where available.

## Enhanced Lab 31 — SSH Host Identity

Record server host-key fingerprint from console and verify first SSH connection.

## Enhanced Lab 32 — SSH User Authentication

Generate Ed25519 key with passphrase, install only the public key on server, and verify.

## Enhanced Lab 33 — SSH Failure Matrix

Create safe failures:

```text
bad DNS
wrong key
wrong authorized_keys permission
locked account
listener stopped
```

Classify each failure layer.

## Enhanced Lab 34 — Baseline Script

Write a safe script producing:

```text
OS/kernel
filesystems
network
listeners
failed units
recent errors
```

with timestamp and clear exit status.

## Enhanced Lab 35 — Permission Troubleshooting Challenge

Create five failures involving:

```text
owner
group
parent x
mode
ACL
```

Solve without `777`.

## Enhanced Lab 36 — Persistence Audit

Classify 20 commands/settings into:

```text
runtime-only
persistent
both
```

Include systemd, NetworkManager, mounts, users, packages, and environment.

## Enhanced Lab 37 — Integrated RH124 Failure Challenge

Create at least 10 safe faults across:

```text
users
groups
permissions
service state
DNF
NetworkManager
DNS
SSH
systemd
```

For each write:

```text
Symptom
Evidence
Root cause
Minimal fix
Verification
Persistence check
```



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — RHEL Baseline

1. Record `/etc/os-release`, kernel, hostname, CPU, memory, IP addresses, routes, and enabled repositories.
2. Create `RH124_BASELINE.md`.
3. Explain the difference between OS version and kernel version.

### Lab 2 — Command Line and Documentation

1. Use `man`, `apropos`, `whatis`, and `--help` to solve five tasks without web search.
2. Document which manual sections you used.
3. Use shell expansion, quoting, and command substitution in a small report.

### Lab 3 — Files and Links

1. Build a directory tree.
2. Create, copy, move, and remove files.
3. Create hard and symbolic links.
4. Compare inode numbers and behavior after deleting targets.

### Lab 4 — Text and Redirection

1. Create a report using stdout and stderr redirection.
2. Build pipelines using `grep`, `sort`, `cut`, and `tee`.
3. Save command errors separately from normal output.

### Lab 5 — Users and Groups

1. Create `developers` and `operations` groups.
2. Create two users.
3. Configure supplementary membership.
4. Configure password-aging policy.
5. Verify with `id`, `getent`, and `chage -l`.

### Lab 6 — Permissions

1. Create a shared operations directory.
2. Configure correct owner/group.
3. Use SGID on the directory where appropriate.
4. Set permissions without using 777.
5. Test access using two users.

### Lab 7 — Software Management

1. Search for a package with DNF.
2. Inspect information.
3. Install it.
4. Identify package-owned files.
5. Review DNF history.
6. Remove it.

### Lab 8 — Processes

1. Start controlled background processes.
2. Inspect PID/PPID/state.
3. Change niceness.
4. Send TERM and KILL in separate tests.
5. Explain what changed.

### Lab 9 — systemd

1. Inspect a service unit.
2. Start/stop/restart it.
3. Enable/disable it.
4. Use `is-active`, `is-enabled`, and `--failed`.
5. Inspect logs after each action.

### Lab 10 — NetworkManager

1. Create a host-only second interface in the VM if possible.
2. Create a NetworkManager connection profile.
3. Assign static IPv4.
4. Configure gateway/DNS only where appropriate.
5. Verify routes and resolver behavior.

### Lab 11 — SSH Key Authentication

1. Use two VMs.
2. Generate Ed25519 key pair.
3. Install public key on server.
4. Verify host key prompt.
5. Log in using key authentication.
6. Inspect server logs.

### Lab 12 — Integrated Broken-Server Challenge

1. Introduce five safe faults: stopped service, wrong file permissions, user missing a group, inactive connection profile, SSH configuration syntax error in a copied lab file.
2. Troubleshoot each using evidence.
3. Write root cause and prevention.

## 6. Mini Project

# Mini Project — Provision a Single RHEL Application Server

Build:

```text
app01.lab.example
```

Requirements:

### Identity
- static hostname,
- administrative user,
- `appops` group.

### Directory structure
```text
/opt/app/
/opt/app/config/
/opt/app/logs/
/opt/app/data/
```

### Permissions
- root owns configuration,
- app operations group has only required access,
- no 777 permissions.

### Software
Install an HTTP service or another safe test service.

Verify:
```bash
rpm -q <package>
systemctl status <service>
ss -tlnp
```

### Network
Configure a lab static IP through NetworkManager.

Document:
- address,
- prefix,
- gateway,
- DNS,
- routes.

### SSH
- key authentication for administrator,
- validate server config,
- preserve working access during changes.

### Operations
Create:
```text
SERVER_BUILD.md
USER_POLICY.md
NETWORK.md
PACKAGE_LIST.md
SERVICE_STATUS.md
SSH_POLICY.md
TROUBLESHOOTING.md
```

### Failure Tests
Break and recover:
1. service stopped,
2. wrong directory group,
3. missing execute/traverse permission,
4. wrong DNS setting,
5. SSH config validation failure.

Use:
```text
Symptom
Evidence
Root cause
Fix
Verification
Prevention
```

# Expanded Capstone — Build and Operate `app01.lab.example`

Extend the original mini project into a full single-server administration exercise.

## Target

```text
Admin workstation
       |
       | SSH key
       v
app01.lab.example
├── RHEL-family system
├── NetworkManager
├── systemd
├── RPM / DNF
├── appops group
├── /opt/app hierarchy
├── test service
└── administration documentation
```

## Required Files

```text
README.md
SYSTEM_BASELINE.md
PACKAGE_BASELINE.md
REPOSITORY_POLICY.md
IDENTITY_POLICY.md
PERMISSIONS.md
NETWORK_PROFILE.md
SYSTEMD_SERVICE_MAP.md
SSH_POLICY.md
CHANGE_LOG.md
TROUBLESHOOTING_RUNBOOK.md
```

## Build Steps

### 1. System identity

Record:

```bash
cat /etc/os-release
uname -r
hostnamectl
```

### 2. Users and groups

Create:

```text
group appops
admin user
operator user
```

Use least privilege.

### 3. Directory tree

```text
/opt/app/
├── config/
├── data/
├── logs/
└── reports/
```

Define:

```text
owner
group
mode
SGID/default ACL only where justified
```

### 4. Software

Install one safe service.

Record:

```text
package NEVRA
package-owned executable
service unit
listener
```

### 5. Networking

Use a noncritical lab interface/profile.

Document:

```text
device
connection profile
address
prefix
gateway
DNS
route
```

### 6. SSH

Configure user public-key authentication.

Document:

```text
host-key fingerprint
user public key fingerprint
known_hosts verification
server configuration validation
```

### 7. systemd

Verify:

```text
active
enabled
unit path
journal
socket
```

### 8. Baseline script

Collect:

```text
OS
kernel
filesystem usage
network
routes
listeners
failed units
recent high-priority journal events
```

### 9. Reboot persistence test

After reboot verify:

```text
hostname
user/group policy
package
service enablement
network profile
directory permissions
SSH access
```

## Failure Injection

At least 12:

```text
wrong file owner
missing parent execute permission
ACL mask restriction
missing group membership
locked user
service stopped
service disabled
bad copied config
inactive NetworkManager profile
bad lab DNS
wrong authorized_keys permissions
stale known_hosts entry on a disposable VM
```

For each:

```text
Symptom
Expected state
Evidence
Subsystem
Root cause
Fix
Verification
Persistence result
Prevention
```


## 7. Recommended Resources

Primary resources:

- Red Hat System Administration I (RH124) official course outline.
- Red Hat Enterprise Linux 10 documentation.
- Red Hat DNF/software-management documentation.
- NetworkManager documentation and `nmcli` manual pages.
- OpenSSH manual pages.
- systemd manual pages.
- GNU Bash and Coreutils manuals.
- Local `man` documentation.

Use your installed release documentation for version-specific details.
## 8. Certification Relevance

RH124 is the first half of Red Hat's RHCSA training path.

The current Red Hat RH124 offering is based on RHEL 10 and is followed by RH134.

Skills here support:
- RHCSA preparation,
- Linux operations,
- cloud VM administration,
- DevOps,
- OpenShift/Kubernetes node administration,
- cybersecurity tooling and incident response.
## 9. Common Mistakes & Best Practices

- **Mistake:** Editing system files without a rollback copy.
  - **Best practice:** Back up important configuration and validate before reload.
- **Mistake:** Using 777 for permissions.
  - **Best practice:** Use correct owner/group and minimum required mode.
- **Mistake:** Changing the only remote interface over SSH.
  - **Best practice:** Use console/second interface or a safe rollback plan.
- **Mistake:** Disabling SSH passwords before validating keys.
  - **Best practice:** Verify a second key-authenticated session first.
- **Mistake:** Assuming installing a package starts its service.
  - **Best practice:** Verify package, service, socket, firewall, and application separately.
- **Mistake:** Using root for normal work.
  - **Best practice:** Use a normal account and sudo only when required.
- **Mistake:** Ignoring DNF transaction history.
  - **Best practice:** Use it to understand package changes.
- **Mistake:** Restarting services without checking configuration syntax.
  - **Best practice:** Use service-specific validation tools first.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the current official RH124 base version?

**Short answer:** Red Hat Enterprise Linux 10.0.

### Q2. What is the difference between an OS release and kernel version?

**Short answer:** The OS release describes the distribution version; the kernel version identifies the running Linux kernel build.

### Q3. What is command substitution?

**Short answer:** `$(command)` captures stdout for use in another command.

### Q4. Why use local manual pages?

**Short answer:** They match installed tools and provide authoritative syntax/options.

### Q5. What does `getent passwd` provide?

**Short answer:** Account information through configured name-service sources.

### Q6. Why use `visudo`?

**Short answer:** It validates sudoers syntax before installation.

### Q7. What is the difference between `start` and `enable`?

**Short answer:** Start changes current runtime state; enable configures boot-time activation.

### Q8. What does `rpm -qf /path` do?

**Short answer:** Identifies which installed RPM owns the file.

### Q9. What does DNF add beyond raw RPM installation?

**Short answer:** Repository metadata, dependency resolution, transactions, and higher-level package management.

### Q10. What is the difference between a NetworkManager device and connection?

**Short answer:** Device is the network interface; connection is a configuration profile.

### Q11. What does `ss -tulpen` help inspect?

**Short answer:** Listening TCP/UDP sockets and related process information.

### Q12. What is an SSH host key?

**Short answer:** A key identifying the SSH server.

### Q13. What is a user SSH key pair for?

**Short answer:** Authenticating a user to an SSH server.

### Q14. Why run `sshd -t`?

**Short answer:** Validate SSH server configuration syntax before reload/restart.

### Q15. What is the correct administration pattern after a change?

**Short answer:** Validate, apply, verify runtime behavior, inspect logs, document.


# Enhanced Self-Assessment Bank

### Q1. OS release vs running kernel?
**Answer:** Distribution release describes the installed OS release; `uname -r` identifies the kernel currently executing.

### Q2. What is NEVRA?
**Answer:** RPM Name, Epoch, Version, Release, Architecture.

### Q3. Does registration itself install a package?
**Answer:** No. Registration/content access, repository configuration, DNF solving, and RPM installation are separate layers.

### Q4. Why use `type -a`?
**Answer:** To see whether Bash resolves a command as alias, function, builtin, or executable.

### Q5. Exit status 0 means?
**Answer:** Conventionally success.

### Q6. Why quote `"$var"`?
**Answer:** Preserve the value as one argument and avoid unintended splitting/globbing.

### Q7. Glob vs regex?
**Answer:** Globs are shell pathname patterns; regex is a different text-pattern language.

### Q8. What does `man 5 fstab` describe?
**Answer:** The `/etc/fstab` file format.

### Q9. What does `namei -l` help diagnose?
**Answer:** Ownership/permission along every component of a path.

### Q10. Filename vs inode?
**Answer:** A directory entry name refers to an inode containing metadata and data mapping.

### Q11. Hard link?
**Answer:** Another directory entry referring to the same inode.

### Q12. Symlink?
**Answer:** A separate object storing a target path.

### Q13. Why use `--` before a filename?
**Answer:** To stop option parsing for names beginning with `-`.

### Q14. Standard descriptors?
**Answer:** stdin 0, stdout 1, stderr 2.

### Q15. Why does redirection order matter?
**Answer:** Descriptor assignments are processed left-to-right.

### Q16. What does `pipefail` do?
**Answer:** Makes failures in earlier pipeline stages affect pipeline status.

### Q17. Why `getent passwd`?
**Answer:** It queries configured NSS identity sources, not only `/etc/passwd`.

### Q18. Primary vs supplementary group?
**Answer:** One primary GID plus additional group memberships used for access.

### Q19. Why may new group membership require re-login?
**Answer:** Existing processes can retain their original supplementary group set.

### Q20. Password lock equals account deletion?
**Answer:** No.

### Q21. What is umask?
**Answer:** A mask that removes permissions from an application's requested creation mode.

### Q22. SGID on directory?
**Answer:** New children normally inherit the directory group.

### Q23. Sticky directory?
**Answer:** Restricts users from deleting/renaming other users' entries in a shared writable directory.

### Q24. ACL mask?
**Answer:** Limits effective permissions for the ACL group class and named entries.

### Q25. Why `visudo`?
**Answer:** It validates sudoers syntax before installing policy.

### Q26. What does `rpm -qf` do?
**Answer:** Finds the installed package owning a file.

### Q27. What does `rpm -V` do?
**Answer:** Verifies package-managed files against RPM metadata expectations.

### Q28. Why is repository trust important?
**Answer:** Repositories are software supply-chain sources.

### Q29. Does installing a package mean its service is running?
**Answer:** No.

### Q30. What is PPID?
**Answer:** Parent process ID.

### Q31. What is a zombie?
**Answer:** Exited process whose parent has not yet collected its exit status.

### Q32. Why SIGTERM before SIGKILL?
**Answer:** TERM allows graceful cleanup; KILL does not.

### Q33. Nice is a hard CPU limit?
**Answer:** No.

### Q34. systemd active vs enabled?
**Answer:** Active is runtime; enabled is persistent boot/dependency activation policy.

### Q35. When is `daemon-reload` needed?
**Answer:** After changing systemd unit definitions/drop-ins.

### Q36. Does `After=` imply `Requires=`?
**Answer:** No.

### Q37. Why inspect logs before restarting?
**Answer:** Restart may remove/change transient evidence.

### Q38. NetworkManager device vs connection?
**Answer:** Device is the interface; connection is saved configuration profile.

### Q39. What does `ip route get` show?
**Answer:** The route/source/next-hop selected for a destination.

### Q40. For a remote IP, what MAC does the host need?
**Answer:** The local next-hop gateway MAC.

### Q41. Why can `/etc/resolv.conf` changes disappear?
**Answer:** It may be generated by NetworkManager or another resolver manager.

### Q42. SSH host key authenticates whom?
**Answer:** The SSH server.

### Q43. SSH user key authenticates whom?
**Answer:** The user to the server.

### Q44. Where are approved public keys stored?
**Answer:** Commonly in `~/.ssh/authorized_keys`.

### Q45. Should a changed host key be blindly removed?
**Answer:** No; verify the new fingerprint through a trusted channel first.

### Q46. Why keep an existing SSH session during server config changes?
**Answer:** It provides recovery access while testing a second connection.

### Q47. Does `systemctl start` make a service persistent at boot?
**Answer:** No.

### Q48. Does `ip address add` normally create persistent NetworkManager config?
**Answer:** No.

### Q49. What is the core troubleshooting pattern?
**Answer:** Observe → isolate subsystem → form hypothesis → minimal change → verify.

### Q50. When is a Linux change complete?
**Answer:** When runtime state, required persistence, logs, and rollback/documentation have been verified.


## Completion Checklist

- [ ] I can identify RHEL and kernel versions.
- [ ] I can solve unfamiliar command questions with local documentation.
- [ ] I can manage files, links, text, pipes, and redirection.
- [ ] I can manage local users/groups/password aging.
- [ ] I can configure file ownership and permissions without 777.
- [ ] I can query and manage software through RPM/DNF.
- [ ] I can inspect/control processes and services.
- [ ] I can create and verify NetworkManager profiles.
- [ ] I can configure SSH key authentication safely.
- [ ] I completed all labs and the single-server mini project.
