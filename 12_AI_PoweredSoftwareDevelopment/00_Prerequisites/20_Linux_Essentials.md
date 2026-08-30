# 20. Linux Essentials

> Phase 5 — Linux System Administration

Linux Essentials is the foundation for all later Linux, Cloud, DevOps, Kubernetes, and Cybersecurity administration.

The objective is not to memorize hundreds of commands. The objective is to understand the Linux operating model:

```text
Hardware
   ↓
Linux Kernel
   ↓
System Services / Daemons
   ↓
Shell and Utilities
   ↓
Applications
   ↓
Users and Remote Administrators
```

You should finish this course able to enter an unfamiliar Linux server, understand what you are looking at, inspect its state, perform safe basic administration, and troubleshoot common problems.

This course uses Red Hat-family examples where possible because the next courses are Red Hat System Administration I–III, but most concepts apply broadly across Linux distributions.
## 1. Topic Title

**Linux Essentials**

## 2. Learning Objectives

- Explain Linux architecture, kernel space, user space, distributions, shells, and common system components.
- Use the Linux command line confidently and understand command syntax, options, arguments, quoting, expansion, and exit status.
- Navigate and manipulate the Linux filesystem safely.
- Understand the Filesystem Hierarchy Standard and the purpose of key directories.
- Manage files, links, ownership, permissions, users, and groups at a foundation level.
- Use pipes, redirection, text-processing tools, regular expressions, and search commands.
- Inspect and control processes, jobs, signals, system services, and basic systemd units.
- Install, update, query, and remove software packages using RPM/DNF concepts.
- Inspect storage devices, partitions, filesystems, mounts, swap, memory, and CPU.
- Configure and troubleshoot basic Linux networking and SSH.
- Read system logs, use `journalctl`, schedule tasks, and write small Bash automation scripts.
- Apply safe administration habits and basic security principles.

## 3. Prerequisites

Recommended prerequisites:

- Phase 1 — Operating Systems Fundamentals
- Phase 2 — Bash Shell Scripting
- Phase 4 — Networking
- Basic virtualization knowledge

You do not need prior professional Linux administration experience.

Recommended lab:

```text
Rocky Linux / AlmaLinux / RHEL-compatible VM
2 vCPU
4 GB RAM
30+ GB disk
```
## 4. Core Concepts Explanation

# Part 1 — What Linux Is

### 1. Linux vs GNU/Linux

Strictly speaking, **Linux** is the kernel.

A complete operating system normally includes:

- Linux kernel
- GNU utilities
- shell
- system libraries
- init/service manager
- package manager
- user applications
- configuration tools

That is why you sometimes see the term **GNU/Linux**.

In practical industry usage, "Linux" usually refers to the complete operating system distribution.
### 2. Linux Kernel

The kernel is the privileged core of the operating system.

Major responsibilities include:

- process scheduling
- memory management
- device drivers
- networking
- filesystems
- system calls
- security enforcement primitives
- hardware abstraction

Applications do not normally access hardware directly.

They request services through system calls.

Conceptually:

```text
Application
    |
    | system call
    v
Linux Kernel
    |
    v
Hardware / Device Driver
```
### 3. Kernel Space vs User Space

**Kernel space** has privileged access to memory and hardware.

**User space** contains ordinary processes such as:

- Bash
- SSH server
- Nginx
- Python
- system utilities
- databases

A crash in a user-space application normally does not crash the entire kernel.

A kernel-level failure can affect the entire system.
### 4. Linux Distributions

A Linux distribution packages the kernel with software, configuration conventions, repositories, and administrative tools.

Common families:

```text
Red Hat family:
RHEL
Rocky Linux
AlmaLinux
CentOS Stream
Fedora

Debian family:
Debian
Ubuntu
Linux Mint

SUSE family:
SLES
openSUSE
```

Important differences include:

- package format
- package manager
- release model
- support model
- default configuration
- security tooling
- software versions

Red Hat-family systems commonly use RPM packages and DNF.
Debian-family systems commonly use DEB packages and APT.
### 5. Distribution Identification

```bash
cat /etc/os-release
uname -a
uname -r
hostnamectl
```
Example:

```text
NAME="Rocky Linux"
VERSION="9.x"
ID="rocky"
```

`/etc/os-release` tells you the distribution.

`uname -r` tells you the running kernel version.

These are different pieces of information.
# Part 2 — Logging In, Shells, and the Terminal

### 6. Console, Terminal, Shell

These words are often confused.

**Terminal**
An interface through which text commands are entered.

**Shell**
A command interpreter.

Examples:
- Bash
- Zsh
- Fish

**Console**
Historically the local system terminal; modern usage can refer to virtual consoles or remote cloud consoles.

The shell reads a command, performs expansions, locates the executable or builtin, runs it, and returns an exit status.
### 7. Bash Prompt

```text
[ahmed@server01 ~]$
[root@server01 ~]#
```
Common prompt meanings:

```text
ahmed     -> current user
server01  -> hostname
~         -> home directory
$         -> normal user
#         -> root user
```

Never assume that `#` in documentation means you should copy the character itself. It often indicates a root shell.
### 8. Command Structure

```bash
ls -lah /var/log
```
Breakdown:

```text
ls        command
-lah      options
/var/log  argument
```

Another example:

```bash
cp -v source.txt /tmp/
```

The meaning of options depends on the command.
### 9. Getting Help

```bash
man ls
man chmod
man 5 passwd

ls --help
ip --help
apropos "copy files"
whatis passwd
```
Manual sections matter.

Examples:

```text
man 1 passwd   -> passwd command
man 5 passwd   -> /etc/passwd file format
```

Get used to reading documentation instead of searching only for copied commands.
### 10. Command History

```bash
history
history | tail
!! 
!123
Ctrl+r
```
Be careful: shell history can contain sensitive commands.

Never put secrets directly into commands when safer alternatives exist.
# Part 3 — Linux Filesystem Navigation

### 11. Root Directory `/`

Linux uses one unified directory tree beginning at:

```text
/
```

Unlike Windows drive-letter presentation, additional disks/filesystems are mounted somewhere inside this tree.

Example:

```text
/
├── boot
├── dev
├── etc
├── home
├── proc
├── root
├── run
├── tmp
├── usr
└── var
```
### 12. Absolute vs Relative Paths

```bash
# Absolute
cd /var/log

# Relative
cd ../tmp
```
Absolute path starts from `/`.

Relative path starts from the current directory.
### 13. `pwd`, `cd`, `ls`

```bash
pwd
ls
ls -l
ls -la
ls -lh
cd /etc
cd ..
cd ~
cd -
```
Useful behaviors:

```text
cd ~   -> home directory
cd ..  -> parent
cd -   -> previous directory
```

`ls -la` includes hidden names beginning with `.`.
### 14. Hidden Files

```bash
ls -la
```
A filename beginning with `.` is hidden by convention.

Examples:

```text
.bashrc
.profile
.ssh
```

Hidden does not mean encrypted or secure.
# Part 4 — Filesystem Hierarchy

### `/etc`

System-wide configuration files.

### `/home`

Home directories for ordinary users.

### `/root`

Home directory of root.

### `/var`

Variable data such as logs, spool files, caches, application state.

### `/usr`

Most user-space programs, libraries, documentation, shared read-only-style system content.

### `/tmp`

Temporary files; retention can vary.

### `/boot`

Bootloader/kernel-related files.

### `/dev`

Device nodes.

### `/proc`

Virtual filesystem exposing process and kernel information.

### `/sys`

Virtual filesystem exposing kernel/device model information.

### `/run`

Runtime state created after boot.

### `/opt`

Optional/add-on software.

### `/srv`

Service data in some layouts.

### `/mnt`

Traditional temporary mount point.

### `/media`

Common mount point for removable media.

### Inspecting Key Directories

```bash
ls -lah /etc
ls -lah /var/log
ls -lah /proc | head
ls -lah /dev | head
```
# Part 5 — Creating and Managing Files

### 15. `touch`

```bash
touch file1.txt
touch file2.txt file3.txt
```
`touch` creates an empty file if it does not exist, or updates timestamps if it does.
### 16. `mkdir`

```bash
mkdir project
mkdir -p project/logs/archive
```
`-p` creates parent directories as required.
### 17. `cp`

```bash
cp file1.txt backup.txt
cp -v file1.txt /tmp/
cp -r project/ project-backup/
cp -a project/ project-backup/
```
`-a` is useful for preserving attributes recursively when copying trees.

Always understand whether your source path ends with `/` because some tools treat source-directory contents differently depending on syntax.
### 18. `mv`

```bash
mv old.txt new.txt
mv report.txt /tmp/
```
`mv` can rename or move.
### 19. `rm`

```bash
rm file.txt
rm -i important.txt
rm -r testdir/
```
Be extremely cautious with recursive deletion.

Never run destructive examples such as:

```bash
rm -rf /
```

Even when safeguards exist, the command is conceptually catastrophic.
### 20. `rmdir`

```bash
rmdir emptydir
```
`rmdir` removes empty directories only.
# Part 6 — Inodes and Links

### 21. Inodes

A filesystem inode stores metadata about a file object.

Conceptually it includes information such as:

- permissions
- owner
- group
- timestamps
- file size
- pointers/extents to data blocks

The filename is a directory entry referring to an inode.

Inspect:
```bash
ls -li
stat file.txt
```
### 22. Hard Links

```bash
echo "hello" > original.txt
ln original.txt hardlink.txt
ls -li original.txt hardlink.txt
```
Hard links point to the same inode.

Deleting one filename does not delete the data as long as another hard link still references the inode.

Hard links normally cannot cross filesystems and are usually restricted for directories.
### 23. Symbolic Links

```bash
ln -s /var/log/messages latest-log
ls -l latest-log
readlink latest-log
```
A symbolic link is a separate file containing a path to another target.

Symlinks can:
- cross filesystems,
- point to directories,
- become broken if the target disappears.
### Hard vs Symbolic Links

```text
Hard link:
name1 ---> inode 123 ---> data
name2 ---^

Symbolic link:
link ---> "/path/to/target" ---> target inode ---> data
```
# Part 7 — Viewing and Editing Text

### 24. `cat`

Prints file contents and can concatenate files.

### 25. `less`

Interactive pager; better for large logs/files.

### 26. `head`

Shows first lines.

### 27. `tail`

Shows last lines; `tail -f` follows growing logs.

### 28. `wc`

Counts lines, words, bytes/characters depending on options.

```bash
cat /etc/os-release
less /var/log/messages
head -n 20 /etc/passwd
tail -n 50 /var/log/messages
tail -f /var/log/messages
wc -l /etc/passwd
```
### 29. Text Editors

You should learn at least one terminal editor.

Common choices:

```text
vi / vim
nano
```

Basic `vim` survival:

```text
i       insert mode
Esc     command mode
:w      save
:q      quit
:wq     save and quit
:q!     quit without saving
/search search
```

Example:

```bash
vim notes.txt
```
# Part 8 — Standard Streams, Redirection, and Pipes

### 30. Standard Input, Output, Error

```text
0 = stdin
1 = stdout
2 = stderr
```
### 31. Output Redirection

```bash
echo "hello" > file.txt
echo "second line" >> file.txt
```
`>` overwrites.

`>>` appends.
### 32. Error Redirection

```bash
ls /root 2> errors.txt
command > output.txt 2> errors.txt
command > all.txt 2>&1
```
### 33. Pipes

```bash
ps aux | grep ssh
cat /etc/passwd | wc -l
journalctl | grep -i error
```
A pipe connects stdout of one command to stdin of another.

Do not build long pipelines without understanding each stage.
# Part 9 — Searching and Processing Text

### 34. `grep`

Search lines matching patterns.

### 35. `sort`

Sort lines.

### 36. `uniq`

Remove/count adjacent duplicate lines.

### 37. `cut`

Extract delimited fields.

### 38. `tr`

Translate/delete characters.

### 39. `tee`

Write to stdout and a file simultaneously.

```bash
grep root /etc/passwd
grep -i error /var/log/messages
grep -R "PermitRootLogin" /etc/ssh/

cut -d: -f1 /etc/passwd
sort names.txt
sort names.txt | uniq -c
tr 'a-z' 'A-Z' < names.txt
ip address | tee network-state.txt
```
### 40. Basic Regular Expressions

```bash
grep '^root:' /etc/passwd
grep 'bash$' /etc/passwd
grep -E 'error|warning|critical' logfile.txt
```
Common basics:

```text
^     beginning of line
$     end of line
.     any single character
*     repetition
[]    character class
|     OR in extended regex
```
# Part 10 — Finding Files

### 41. `find`

```bash
find /etc -name "*.conf"
find /var/log -type f
find /home -user ahmed
find /tmp -type f -mtime +7
find . -type f -size +100M
```
`find` walks the filesystem and evaluates conditions.

Be careful combining `find` with destructive actions.
### 42. `locate`

```bash
locate sshd_config
```
`locate` searches a prebuilt database, so results can be stale.
### 43. `which`, `type`, `whereis`

```bash
which ssh
type cd
type ls
whereis bash
```
`type` is especially useful because it tells whether something is:
- builtin,
- alias,
- function,
- executable path.
# Part 11 — Users and Groups

### 44. User Identity

```bash
whoami
id
who
w
last
```
### 45. `/etc/passwd`

```bash
head /etc/passwd
```
Example format:

```text
ahmed:x:1000:1000:Ahmed:/home/ahmed:/bin/bash
```

Fields:

```text
username
password placeholder
UID
GID
comment
home directory
login shell
```

Password hashes are normally stored in `/etc/shadow`, not `/etc/passwd`.
### 46. `/etc/shadow`

```bash
sudo head /etc/shadow
```
Only privileged users should read this file.

It stores password-aging and hash-related information.
### 47. `/etc/group`

```bash
cat /etc/group
groups
getent group wheel
```
### 48. Creating Users

```bash
sudo useradd student1
sudo passwd student1
id student1
```
### 49. Modifying Users

```bash
sudo usermod -aG wheel student1
sudo usermod -s /bin/bash student1
```
The `-aG` combination is important.

Using `-G` without `-a` can replace supplementary group memberships.
### 50. Removing Users

```bash
sudo userdel student1
sudo userdel -r student1
```
`-r` also attempts to remove the user's home/mail files.

Use carefully.
### 51. Groups

```bash
sudo groupadd devops
sudo usermod -aG devops ahmed
getent group devops
```
# Part 12 — Ownership and Permissions

### 52. Permission Model

```text
-rwxr-x---
 ||| ||| |||
 ||| ||| +++ other
 ||| +++ group
 +++ owner
```
### 53. Read, Write, Execute

For files:

```text
r = read contents
w = modify contents
x = execute as program/script
```

For directories:

```text
r = list names
w = create/delete entries
x = traverse/access entries
```

Directory permissions are especially important and often misunderstood.
### 54. `chmod`

```bash
chmod u+x script.sh
chmod g-w file.txt
chmod o-r secret.txt

chmod 750 script.sh
chmod 640 config.conf
```
### 55. Numeric Permissions

```text
r = 4
w = 2
x = 1

7 = rwx
6 = rw-
5 = r-x
4 = r--

chmod 750:
owner = rwx
group = r-x
other = ---
```
### 56. `chown` and `chgrp`

```bash
sudo chown ahmed file.txt
sudo chown ahmed:devops file.txt
sudo chgrp devops file.txt
```
### 57. `umask`

```bash
umask
umask 027
```
`umask` removes permission bits from defaults.

Typical concept:

```text
files start conceptually from 666
directories from 777
```

With umask `022`:

```text
files -> 644
dirs  -> 755
```
### 58. SUID, SGID, Sticky Bit — Introduction

```bash
ls -l /usr/bin/passwd
ls -ld /tmp
```
Special bits:

**SUID**
Executable can run with effective owner identity.

**SGID**
Executable can run with effective group identity; on directories it can make new files inherit the directory group.

**Sticky bit**
On shared directories such as `/tmp`, restricts deletion so users cannot remove each other's files simply because the directory is writable.

These features have security implications and will be revisited later.
# Part 13 — Root and `sudo`

### 59. Root User

Root has UID 0 and extensive system privileges.

Root can:

- modify system configuration,
- manage users,
- install packages,
- manipulate devices/filesystems,
- control services.

That power makes mistakes dangerous.
### 60. `sudo`

```bash
sudo dnf update
sudo systemctl restart sshd
sudo cat /etc/shadow
```
`sudo` executes an authorized command with elevated privileges.

Advantages over staying logged in as root:

- accountability
- command-specific privilege
- reduced accidental exposure
- easier auditing
### 61. `su`

```bash
su -
sudo -i
```
`su -` starts a login shell as another user, commonly root.

`sudo -i` starts a root-like login shell through sudo policy.

Prefer least privilege instead of remaining root unnecessarily.
# Part 14 — Processes and Jobs

### 62. Process Concepts

A process is a running instance of a program.

Every process has information such as:

- PID
- PPID
- UID/GID
- memory
- CPU usage
- environment
- open files
- state
### 63. `ps`

```bash
ps
ps aux
ps -ef
ps -eo pid,ppid,user,%cpu,%mem,cmd --sort=-%cpu | head
```
### 64. `top`

```bash
top
```
`top` provides a live process/system view.

Common things to inspect:

- load average
- CPU
- memory
- process state
- highest consumers
### 65. `pgrep`, `pkill`

```bash
pgrep sshd
pgrep -a sshd
sudo pkill -HUP someprocess
```
### 66. Signals

Signals notify processes of events.

Common:

```text
SIGTERM  15  polite termination request
SIGKILL   9  forced kill, cannot be handled
SIGHUP    1  often reload/reopen depending on daemon
SIGINT    2  interrupt, often Ctrl+C
```

Prefer SIGTERM before SIGKILL.
```bash
kill -TERM 1234
kill -KILL 1234
kill -HUP 1234
```
### 67. Foreground and Background Jobs

```bash
sleep 300 &
jobs
fg %1
bg %1
Ctrl+Z
```
Interactive shell jobs are not the same thing as long-running system services.
### 68. `nice` and `renice`

```bash
nice -n 10 command
sudo renice 5 -p 1234
```
Niceness influences CPU scheduling priority.

It does not guarantee a fixed percentage of CPU.
# Part 15 — systemd and Services

### 69. Init System

Modern Red Hat-family distributions use **systemd** as PID 1 and service manager.

systemd manages:

- services
- sockets
- mounts
- timers
- targets
- device-related units
### 70. Service Units

```bash
systemctl status sshd
sudo systemctl start sshd
sudo systemctl stop sshd
sudo systemctl restart sshd
sudo systemctl reload sshd
sudo systemctl enable sshd
sudo systemctl disable sshd
sudo systemctl enable --now sshd
```
Important distinction:

```text
start   -> start now
enable  -> start automatically at boot according to unit dependencies
```

They are different operations.
### 71. Listing Units

```bash
systemctl list-units --type=service
systemctl list-unit-files --type=service
systemctl --failed
```
### 72. Unit Files

```bash
systemctl cat sshd
systemctl show sshd
```
Common unit locations include:

```text
/usr/lib/systemd/system/
/etc/systemd/system/
```

Administrator overrides belong under `/etc`.
### 73. Basic Custom Service Example

```ini
[Unit]
Description=Simple Demo Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/demo-service.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now demo.service
systemctl status demo.service
```
# Part 16 — Package Management

### 74. RPM

```bash
rpm -qa | head
rpm -q bash
rpm -qi bash
rpm -ql bash
rpm -qf /usr/bin/ssh
```
RPM is the package format/database foundation in Red Hat-family systems.

Avoid installing random RPM files without understanding dependencies and trust.
### 75. DNF

```bash
sudo dnf search nginx
sudo dnf info nginx
sudo dnf install nginx
sudo dnf remove nginx
sudo dnf update
dnf repolist
```
### 76. Repositories

```bash
dnf repolist
ls /etc/yum.repos.d/
```
Repositories provide package metadata and packages.

Production systems should use trusted, controlled repositories.
### 77. Package Verification

```bash
rpm -V bash
```
RPM verification compares installed files to package metadata.

Changed configuration files may be legitimate, so interpret results instead of assuming compromise.
# Part 17 — Storage Fundamentals

### 78. Block Devices

```bash
lsblk
lsblk -f
blkid
```
Typical devices:

```text
/dev/sda
/dev/sda1
/dev/nvme0n1
/dev/nvme0n1p1
```

A disk can contain partitions, and those partitions may contain filesystems, LVM physical volumes, swap, or other structures.
### 79. Filesystems

Common Linux filesystems:

- XFS
- ext4

Red Hat Enterprise Linux commonly uses XFS for many default filesystems.

A filesystem organizes files/directories and metadata on block storage.
### 80. Mounting

```bash
findmnt
mount
df -h
```
A filesystem must be mounted somewhere in the directory tree before users/applications access it normally.
### 81. Temporary Mount Example

```bash
sudo mkdir -p /mnt/data
sudo mount /dev/sdb1 /mnt/data
findmnt /mnt/data
```
Do not run mount commands blindly. Confirm the device using `lsblk -f`.
### 82. `/etc/fstab` Introduction

```text
UUID=xxxx-xxxx  /data  xfs  defaults  0 0
```
`/etc/fstab` defines persistent mount configuration.

A broken `fstab` can affect boot, so validate carefully.
```bash
sudo mount -a
findmnt
```
### 83. Disk Usage

```bash
df -h
du -sh /var/log
du -xh /var | sort -h | tail
```
`df` reports filesystem free space.

`du` reports file/directory usage.

A full filesystem may be caused by:
- logs
- application data
- deleted-open files
- container images
- backups
### 84. Swap

```bash
swapon --show
free -h
```
Swap provides disk-backed virtual memory.

Heavy swap use can indicate memory pressure, but some swap use alone is not automatically a problem.
# Part 18 — CPU, Memory, and Hardware Inspection

### 85. CPU

```bash
lscpu
nproc
uptime
```
### 86. Memory

```bash
free -h
cat /proc/meminfo | head
```
Linux uses unused memory aggressively for caches.

Do not interpret "low free memory" as a problem without considering available memory and workload behavior.
### 87. Hardware

```bash
lspci
lsusb
lsblk
dmidecode
```
Some commands require root privileges.
# Part 19 — Linux Networking Essentials

### 88. Interface Inspection

```bash
ip link
ip address
ip -br address
```
### 89. Routing Table

```bash
ip route
ip -6 route
```
Example:

```text
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.50
```

This tells you:
- local subnet
- interface
- local source IP
- default gateway
### 90. Neighbor Table

```bash
ip neigh
ip -6 neigh
```
IPv4 entries are learned through ARP.
IPv6 entries are learned through NDP.
### 91. Connectivity Testing

```bash
ping -c 4 192.168.1.1
ping -c 4 8.8.8.8
traceroute 8.8.8.8
```
### 92. DNS Testing

```bash
cat /etc/resolv.conf
dig example.com
dig example.com A
dig example.com AAAA
getent hosts example.com
```
### 93. Socket Inspection

```bash
ss -tulpen
ss -tn
ss -lun
```
Example:

```text
LISTEN 0 128 0.0.0.0:22
```

means a process is listening on TCP port 22 on all IPv4 interfaces.
### 94. NetworkManager Introduction

```bash
nmcli device status
nmcli connection show
nmcli connection show --active
```
Red Hat-family systems commonly use NetworkManager for persistent network configuration.

Detailed `nmcli` configuration is covered more deeply in later Red Hat administration courses.
### 95. Hostname

```bash
hostname
hostnamectl
sudo hostnamectl set-hostname server01.lab.example
```
### 96. `/etc/hosts`

```text
127.0.0.1   localhost
192.168.50.20 app01.lab.example app01
```
`/etc/hosts` provides local static name mappings.

It does not replace DNS at scale.
# Part 20 — SSH Essentials

### 97. SSH

```bash
ssh user@192.168.1.20
ssh user@server01.lab.example
```
SSH provides encrypted remote shell access and can support:
- command execution
- file transfer
- tunneling
- port forwarding
### 98. SSH Keys

```bash
ssh-keygen -t ed25519
ssh-copy-id user@server01
ssh user@server01
```
Typical files:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
~/.ssh/authorized_keys
```

Protect private keys.
Never share the private key.
### 99. SSH Configuration

```text
Host labserver
    HostName 192.168.56.20
    User ahmed
    IdentityFile ~/.ssh/id_ed25519
```
```bash
ssh labserver
```
### 100. SSH Server

```bash
systemctl status sshd
sudo ss -tlnp | grep :22
sudo grep -E '^(PermitRootLogin|PasswordAuthentication)' /etc/ssh/sshd_config
```
Before restarting SSH remotely, validate configuration.

Depending on OpenSSH version:
```bash
sudo sshd -t
```
Keep an existing session open while testing changes so you do not lock yourself out.
# Part 21 — Basic Security Foundations

### 101. `firewalld` Introduction

```bash
systemctl status firewalld
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all
sudo firewall-cmd --list-services
```
`firewalld` manages host firewall policy using zones and services.

Detailed firewall administration is covered later.
### 102. SELinux Introduction

```bash
getenforce
sestatus
ls -Z /var/www 2>/dev/null
```
SELinux is a Mandatory Access Control system.

Modes:

```text
Enforcing
Permissive
Disabled
```

A common mistake is disabling SELinux whenever an application fails.

Better approach:

1. identify the denial,
2. understand required access,
3. fix labeling/policy/configuration correctly.

SELinux becomes a major topic in later Red Hat administration.
### 103. Security Principle — Least Privilege

Users and services should receive only the permissions required.

Examples:

Bad:
```text
chmod 777 everything
run application as root
open all firewall ports
```

Better:
```text
correct owner/group
minimum required permission
dedicated service account
specific firewall rule
```
# Part 22 — Logs and the Journal

### 104. Traditional Logs

```bash
ls -lah /var/log
sudo less /var/log/messages
sudo less /var/log/secure
```
Exact log filenames vary by distribution and configuration.
### 105. `journalctl`

```bash
journalctl
journalctl -b
journalctl -p err
journalctl -u sshd
journalctl --since "1 hour ago"
journalctl -f
```
### 106. Service Troubleshooting with Logs

```bash
systemctl status sshd
journalctl -u sshd --since "30 minutes ago"
ss -tlnp | grep :22
```
This combines:

- service manager state,
- logs,
- socket state.

That is much stronger than simply restarting the service repeatedly.
# Part 23 — Scheduling Tasks

### 107. `cron`

```bash
crontab -e
crontab -l
```
Example:

```cron
0 2 * * * /home/ahmed/scripts/backup.sh
```
Meaning:

```text
minute hour day-of-month month day-of-week command
0      2    *            *     *           run at 02:00 daily
```
### 108. systemd Timers Introduction

Modern Linux systems can schedule work using systemd timer units.

Concept:

```text
myjob.service
myjob.timer
```

Timers integrate with systemd logging and dependencies.

More advanced timer design comes later.
# Part 24 — Archives and Compression

### 109. `tar`

```bash
tar -cvf backup.tar project/
tar -tvf backup.tar
tar -xvf backup.tar
```
### 110. Compression

```bash
tar -czvf backup.tar.gz project/
tar -xzvf backup.tar.gz

gzip file.txt
gunzip file.txt.gz
```
Archive and compression are different concepts.

`tar` groups files.
gzip/xz/etc. compress data.
# Part 25 — Bash Administration Scripting

### 111. Shebang

```bash
#!/usr/bin/env bash
```
### 112. Variables

```bash
HOST=$(hostname)
DATE=$(date +%F)

echo "Host: $HOST"
echo "Date: $DATE"
```
### 113. Exit Status

```bash
ping -c 1 192.168.1.1 >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Gateway reachable"
else
    echo "Gateway unreachable"
fi
```
Cleaner:

```bash
if ping -c 1 192.168.1.1 >/dev/null 2>&1; then
    echo "Gateway reachable"
else
    echo "Gateway unreachable"
fi
```
### 114. Basic Health Script

```bash
#!/usr/bin/env bash

echo "=== System Health ==="

echo
echo "Hostname:"
hostname

echo
echo "Uptime:"
uptime

echo
echo "Memory:"
free -h

echo
echo "Disk:"
df -h /

echo
echo "IP Addresses:"
ip -br address

echo
echo "Default Route:"
ip route | grep '^default'
```
### 115. Safer Script Structure

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

log() {
    printf '%s %s\n' "$(date '+%F %T')" "$*"
}

require_command() {
    command -v "$1" >/dev/null 2>&1 || {
        log "ERROR: required command not found: $1"
        exit 1
    }
}

require_command ip
require_command df

log "Starting health check"

df -h /
ip -br address

log "Health check complete"
```
`set -e` is sometimes used too, but it has nuanced behavior. Do not use strict-mode options as a substitute for understanding exit statuses.
# Part 26 — Linux Boot Process Overview

### 116. Boot Stages

```text
Firmware (BIOS/UEFI)
        ↓
Bootloader (GRUB)
        ↓
Linux Kernel
        ↓
initramfs
        ↓
root filesystem
        ↓
systemd PID 1
        ↓
targets/services
        ↓
login
```
### 117. GRUB

GRUB is a common Linux bootloader.

It:
- loads the selected kernel,
- passes kernel command-line parameters,
- loads initramfs.

Do not edit bootloader configuration casually on production systems.
### 118. Kernel Command Line

```bash
cat /proc/cmdline
```
### 119. Current Boot Target

```bash
systemctl get-default
systemctl list-units --type=target
```
# Part 27 — Virtual Filesystems `/proc` and `/sys`

### 120. `/proc`

```bash
cat /proc/cpuinfo | head
cat /proc/meminfo | head
cat /proc/uptime
ls /proc/$$
```
`/proc` exposes process and kernel information.

`$$` in Bash is the shell PID.
### 121. `/sys`

```bash
ls /sys/class/net
ls /sys/block
```
`/sys` exposes kernel device and subsystem information.

Both `/proc` and `/sys` are virtual filesystems, not ordinary disk directories.
# Part 28 — Environment Variables and Shell Startup

### 122. Environment Variables

```bash
env
printenv
echo "$PATH"
echo "$HOME"
echo "$USER"
```
### 123. PATH

```bash
echo "$PATH"
which python
type ls
```
`PATH` controls where the shell searches for commands.

Avoid adding insecure writable directories to privileged PATHs.
### 124. Shell Startup Files

```text
~/.bashrc
~/.bash_profile
/etc/bashrc
/etc/profile
```
Exact startup behavior depends on:
- login vs non-login shell,
- interactive vs non-interactive shell,
- distribution configuration.
# Part 29 — Linux Troubleshooting Methodology

### 125. Troubleshoot by Evidence

Use a structured sequence:

```text
1. Define symptom
2. Determine scope
3. Check recent changes
4. Verify system state
5. Identify layer/component
6. Form hypothesis
7. Test one thing
8. Apply minimal fix
9. Verify
10. Document
```
### 126. Service Troubleshooting Example

Problem:

```text
SSH connection fails.
```

Do not immediately reinstall OpenSSH.

Check:

```bash
ip address
ip route
ping <server>
systemctl status sshd
ss -tlnp | grep :22
sudo firewall-cmd --list-all
getenforce
journalctl -u sshd
```

Possible causes:

- no IP connectivity,
- wrong route,
- sshd stopped,
- wrong bind address,
- port blocked by firewall,
- SELinux issue,
- invalid sshd configuration,
- wrong credentials.
### 127. Disk-Full Troubleshooting

```bash
df -h
df -i
du -xh /var | sort -h | tail -20
sudo lsof +L1
```
A filesystem can be "full" because of:

- bytes exhausted,
- inodes exhausted,
- deleted files still open,
- logs,
- database files,
- container layers,
- backups.
### 128. High CPU Troubleshooting

```bash
uptime
top
ps -eo pid,user,%cpu,%mem,cmd --sort=-%cpu | head
```
High load average does not always mean high CPU. Load can include tasks waiting on uninterruptible I/O.
### 129. Memory Troubleshooting

```bash
free -h
top
ps -eo pid,user,%mem,rss,cmd --sort=-%mem | head
journalctl -k | grep -i -E 'oom|out of memory'
```
### 130. Network Troubleshooting

```bash
ip -br address
ip route
ip neigh
ping -c 4 <gateway>
dig example.com
ss -tulpen
curl -I https://example.com
```
Separate:

```text
link
IP address
gateway
routing
DNS
firewall
socket
application
```

This mirrors Phase 4 networking methodology.

# Enhanced Engineering Layer — Linux Essentials

The original course already establishes the correct Linux foundation: kernel/user space, filesystems, permissions, users, processes, systemd, packages, storage, networking, SSH, logging, scheduling, Bash, boot, `/proc`, `/sys`, and troubleshooting. This enhanced layer preserves those topics and adds the deeper operating-system mental models, shell behavior, security controls, storage/network reasoning, and troubleshooting workflows needed before Red Hat System Administration I–III.

The goal is to make Linux predictable rather than command-driven.

## Mental Model 1 — From Command to Kernel

```text
Keyboard / SSH session
        ↓
Terminal
        ↓
Shell (Bash)
        ↓
Parsing + expansion
        ↓
Builtin OR executable
        ↓
Process
        ↓
System calls
        ↓
Linux kernel
        ↓
Filesystem / network / CPU / memory / devices
```

## Mental Model 2 — Everything Is State

```text
Configuration
      +
Running processes
      +
Kernel state
      +
Filesystem state
      +
Network state
      +
Logs
      =
Actual server behavior
```

Editing a configuration file changes **desired configuration**, not necessarily current runtime state.

## Mental Model 3 — Evidence Before Action

```text
Symptom
   ↓
Scope
   ↓
Relevant subsystem
   ↓
Observe state
   ↓
Form hypothesis
   ↓
Minimal change
   ↓
Verify
   ↓
Document
```

## Mental Model 4 — Privilege Boundary

```text
Normal user
   ↓ sudo policy
Privileged command
   ↓
Kernel permission checks
   ↓
DAC permissions
+ ACLs
+ capabilities
+ SELinux
+ namespace/cgroup limits
```

A Linux permission problem is not always solved by `chmod`.


### Enhanced Deep Dive — System Calls — How User Space Requests Kernel Services

Applications normally cannot directly access disks, create network packets, or allocate arbitrary physical memory. They request kernel services through system calls.

Common conceptual examples:
- `open()` / `read()` / `write()` for files
- `fork()` / `clone()` / `execve()` for process creation
- `socket()` / `connect()` / `bind()` for networking
- `mount()` for filesystem mounting

#### Diagram / Mental Model

```text
Python / Bash / Nginx
       ↓ libc/runtime
   system call boundary
       ↓
Linux Kernel
├─ VFS
├─ scheduler
├─ networking
├─ memory manager
└─ device drivers
```

#### Command / Bash Example

```bash
strace -o /tmp/trace.txt -f /bin/echo "hello"
head -n 20 /tmp/trace.txt
```

#### Why It Works / Why It Matters

`strace` makes the user-space/kernel boundary observable and becomes extremely useful for troubleshooting later.

#### Security Implication

Use tracing only on systems/processes you are authorized to inspect because traces can expose paths, arguments, environment data, or application secrets.



### Enhanced Deep Dive — Shell Builtins vs External Commands

Some commands execute inside the shell process itself, while others are separate executables.

Examples of common Bash builtins:
- `cd`
- `export`
- `read`
- `alias`
- `type`
- `jobs`

`cd` must be a shell builtin because an external child process cannot change the parent shell's working directory.

#### Command / Bash Example

```bash
type cd
type echo
type ls
command -V cd
command -V ls
```

#### Expected Behavior / Output

```text
cd is a shell builtin
ls is aliased to ... OR /usr/bin/ls
```

#### Why It Works / Why It Matters

This explains why command behavior can differ because of aliases, functions, builtins, or PATH resolution.



### Enhanced Deep Dive — Command Lookup Order

When Bash receives a command name, it may resolve it as:
- reserved word
- alias
- function
- builtin
- hashed command path
- executable found through `PATH`

Use `type -a` to see all matching interpretations.

#### Command / Bash Example

```bash
type -a ls
type -a python
hash
```

#### Why It Works / Why It Matters

If a command behaves unexpectedly, verify what is actually being executed before debugging the program itself.



### Enhanced Deep Dive — Exit Status Is the Shell's Success Contract

Linux commands report an integer exit status.

Convention:
- `0` → success
- non-zero → failure or alternate condition

The meaning of a particular non-zero value is command-specific.

#### Command / Bash Example

```bash
true
echo "$?"

false
echo "$?"

grep root /etc/passwd >/dev/null
echo "$?"
```

#### Why It Works / Why It Matters

Scripts, systemd, CI/CD systems, cron wrappers, and monitoring tools all depend on exit status.



### Enhanced Deep Dive — Shell Parsing Happens Before Execution

A shell command line is transformed before most programs see it.

A simplified Bash sequence includes:
- tokenization/parsing
- parameter expansion
- command substitution
- arithmetic expansion
- word splitting
- pathname expansion/globbing
- quote removal
- redirection setup
- execution

#### Diagram / Mental Model

```text
echo "$HOME"/*.log
      ↓
parameter expansion
      ↓
pathname expansion outside quoted glob
      ↓
final argument vector
      ↓
echo process/builtin
```

#### Why It Works / Why It Matters

Many 'command bugs' are actually shell-expansion bugs.



### Enhanced Deep Dive — Single Quotes, Double Quotes, and No Quotes

Quoting controls shell expansion.

**Single quotes `'...'`**
Preserve almost everything literally.

**Double quotes `"..."`**
Allow parameter and command substitution while preventing most word splitting and glob expansion.

**Unquoted**
Allows splitting and pathname expansion.

#### Command / Bash Example

```bash
name='server one'

printf '<%s>\n' $name
printf '<%s>\n' "$name"

echo '$HOME'
echo "$HOME"
```

#### Expected Behavior / Output

```text
Unquoted $name may become two arguments.
Quoted "$name" remains one argument.
'$HOME' prints the literal text $HOME.
```

#### Security Implication

Quote variable expansions unless intentional splitting/globbing is required. Unquoted data can cause dangerous path and argument handling.



### Enhanced Deep Dive — Globbing Is Not Regular Expressions

Shell globs and regular expressions are different languages.

Shell glob examples:
- `*.log`
- `file?.txt`
- `[abc]*`

Regular-expression tools such as `grep -E` use different syntax.

#### Command / Bash Example

```bash
printf '%s
' *.log
grep -E '^[a-z]+[0-9]+$' names.txt
```

#### Why It Works / Why It Matters

Confusing glob syntax with regex syntax leads to incorrect search and deletion commands.



### Enhanced Deep Dive — Brace Expansion

Brace expansion generates strings before pathname expansion.

Examples:

#### Command / Bash Example

```bash
echo file{1..5}.txt
mkdir -p lab/{logs,reports,backup}
```

#### Expected Behavior / Output

```text
file1.txt file2.txt file3.txt file4.txt file5.txt
```

#### Why It Works / Why It Matters

Useful for predictable command generation, but verify expanded paths before destructive operations.



### Enhanced Deep Dive — Command Substitution

Command substitution captures stdout and inserts it into another command.

Modern syntax:
`$(command)`.

#### Command / Bash Example

```bash
kernel=$(uname -r)
printf 'Kernel: %s\n' "$kernel"

today=$(date +%F)
touch "report-$today.txt"
```

#### Why It Works / Why It Matters

It connects command output to automation while remaining readable and nestable.



### Enhanced Deep Dive — Shell Variables vs Environment Variables

A shell variable exists in the current shell. An environment variable is exported to child processes.

`export` marks a variable for inheritance.

#### Diagram / Mental Model

```text
Parent Bash
APP_ENV=lab
   ↓ without export
Child process → does not inherit

Parent Bash
export APP_ENV=lab
   ↓
Child process → inherits APP_ENV
```

#### Command / Bash Example

```bash
APP_ENV=lab
bash -c 'echo "$APP_ENV"'

export APP_ENV
bash -c 'echo "$APP_ENV"'
```

#### Security Implication

Environment variables are convenient configuration, but they are not automatically secret storage.



### Enhanced Deep Dive — PATH Search and Privilege Safety

`PATH` is an ordered list of directories searched for executable commands.

If a writable or untrusted directory appears before system directories, a malicious executable with a trusted-looking name can be executed accidentally.

#### Command / Bash Example

```bash
printf '%s
' "$PATH" | tr ':' '
'
type -a ls
```

#### Security Implication

Privileged automation should use controlled PATH values and, for high-risk operations, explicit executable paths where appropriate.



### Enhanced Deep Dive — File Descriptors

A process refers to open files, pipes, sockets, terminals, and devices using integer file descriptors.

Conventional descriptors:
- 0 stdin
- 1 stdout
- 2 stderr

Additional files/sockets typically use 3 and above.

#### Diagram / Mental Model

```text
Process
├─ fd 0 → terminal input
├─ fd 1 → terminal output
├─ fd 2 → terminal error
├─ fd 3 → config file
└─ fd 4 → TCP socket
```

#### Command / Bash Example

```bash
ls -l /proc/$$/fd
```

#### Why It Works / Why It Matters

Redirection is fundamentally about changing which object a file descriptor points to.



### Enhanced Deep Dive — Redirection Order Matters

These are not always equivalent:

`command >file 2>&1`
and
`command 2>&1 >file`

Redirections are processed left to right.

#### Diagram / Mental Model

```text
command >file 2>&1
stdout → file
stderr → current stdout → file

command 2>&1 >file
stderr → current stdout (terminal)
stdout → file
```

#### Why It Works / Why It Matters

Understanding descriptor duplication prevents missing logs and confusing script behavior.



### Enhanced Deep Dive — Here Documents

A here-document feeds multiline text to a command's stdin.

Quoted delimiters can suppress expansion.

#### Command / Bash Example

```bash
cat <<'EOF' > example.conf
$HOME remains literal here
line2=value
EOF
```

#### Why It Works / Why It Matters

Here-documents are useful for generated configuration and automation.



### Enhanced Deep Dive — `tee` with Privileged Files

Redirection is performed by your current shell before `sudo` runs.

Therefore:

`sudo echo value > /root/file`

still attempts the redirection as the normal user.

Use `sudo tee` when appropriate.

#### Command / Bash Example

```bash
printf '%s
' 'example=value' | sudo tee /etc/example.conf >/dev/null
```

#### Why It Works / Why It Matters

This explains a common sudo/redirection confusion.



### Enhanced Deep Dive — Filesystem Names and Inodes

A directory maps names to inode numbers. The inode stores filesystem metadata and points to file data.

Renaming a file within the same filesystem generally changes directory entries rather than rewriting its entire data content.

#### Diagram / Mental Model

```text
Directory entry:
report.txt ──> inode 8123
                 ├─ owner
                 ├─ mode
                 ├─ timestamps
                 ├─ size
                 └─ data extents
```

#### Command / Bash Example

```bash
ls -li report.txt
stat report.txt
```

#### Why It Works / Why It Matters

This mental model explains hard links, deleted-open files, inode exhaustion, and rename behavior.



### Enhanced Deep Dive — Deleted but Open Files

Deleting a pathname removes a directory entry. If a process still has the inode open, the filesystem blocks remain allocated until the final open reference is closed.

This creates the classic condition:

`df` says full, but `du` cannot find the space.

#### Diagram / Mental Model

```text
logfile name deleted
        ↓
directory entry gone
        ↓
process fd still points to inode
        ↓
blocks remain allocated
```

#### Command / Bash Example

```bash
sudo lsof +L1
```

#### Why It Works / Why It Matters

Restarting/reloading the responsible process can release the space after proper application handling.



### Enhanced Deep Dive — Inode Exhaustion

A filesystem can run out of inodes even when many bytes remain free.

This happens when an enormous number of small files consume all available inode structures on filesystems with finite inode allocation.

#### Command / Bash Example

```bash
df -h
df -i
```

#### Troubleshooting

If file creation fails with 'No space left on device', check both byte capacity and inode capacity.



### Enhanced Deep Dive — Mount Points Hide Underlying Directory Contents

When a filesystem is mounted on a non-empty directory, the mounted filesystem's root becomes visible at that path and the original directory contents are hidden until unmounted.

#### Diagram / Mental Model

```text
Before mount:
/data
├─ old-a
└─ old-b

mount /dev/sdb1 /data

Visible:
/data
├─ filesystem-b-file1
└─ filesystem-b-file2

old-a/old-b still exist underneath but are hidden.
```

#### Why It Works / Why It Matters

This explains surprising 'missing files' after mounts.



### Enhanced Deep Dive — Filesystem vs Block Device vs Mount Point

These are distinct layers:

- block device: storage interface such as `/dev/sdb1`
- filesystem: data structure such as XFS/ext4 created on storage
- mount point: directory where the filesystem becomes visible

#### Diagram / Mental Model

```text
/dev/sdb1
   ↓ mkfs
XFS filesystem
   ↓ mount
/data
   ↓
files/directories
```

#### Why It Works / Why It Matters

Many storage mistakes come from treating these as interchangeable concepts.



### Enhanced Deep Dive — UUIDs and Labels

Device names such as `/dev/sdb1` can change as hardware discovery order changes. UUIDs and filesystem labels provide more stable identifiers for persistent mounts.

#### Command / Bash Example

```bash
lsblk -f
blkid
findmnt -no SOURCE,TARGET,FSTYPE,OPTIONS /
```

#### Why It Works / Why It Matters

Persistent `/etc/fstab` entries usually benefit from stable filesystem identifiers.



### Enhanced Deep Dive — `/etc/fstab` Fields

An `fstab` line normally includes:

1. source
2. mount point
3. filesystem type
4. options
5. dump field
6. filesystem-check order field

Example:

#### Command / Bash Example

```bash
sudo mount -a
findmnt /data
```

#### Configuration Example

```text
UUID=aaaa-bbbb  /data  xfs  defaults,noatime  0  0
```

#### Security Implication

Validate with `mount -a` before rebooting. A malformed persistent mount can cause boot or service failures.



### Enhanced Deep Dive — Mount Options as Security/Behavior Controls

Common mount options include:
- `ro` / `rw`
- `noexec`
- `nosuid`
- `nodev`
- `noatime`
- filesystem-specific options

They influence behavior but are not complete security boundaries.

#### Why It Works / Why It Matters

A file can have execute permissions yet fail to run on a filesystem mounted `noexec`.



### Enhanced Deep Dive — Hard-Link Count and Directory Links

The inode's link count shows how many hard directory entries refer to it.

For ordinary files:
- create hard link → count increases
- remove one name → count decreases
- storage is freed when link count reaches zero **and** no process keeps it open

#### Command / Bash Example

```bash
ln original hard2
stat -c '%h %n' original hard2
rm original
stat -c '%h %n' hard2
```

#### Why It Works / Why It Matters

Unix deletion is reference-count-like rather than 'erase the bytes immediately'.



### Enhanced Deep Dive — Symlink Resolution and Broken Links

A symbolic link stores a pathname. That target pathname is resolved when accessed.

Relative symlinks are interpreted relative to the directory containing the symlink, not your current shell directory.

#### Command / Bash Example

```bash
ln -s ../shared/config.ini app/config.ini
readlink app/config.ini
readlink -f app/config.ini
```

#### Why It Works / Why It Matters

Relative links can remain valid when a whole directory tree is moved together.



### Enhanced Deep Dive — Directory Execute Permission

Directory permissions differ from file permissions.

- `r` → list directory entry names
- `w` → create/delete/rename entries, subject to other rules
- `x` → traverse/search the directory

A user may know a filename but be unable to access it without execute permission on every parent directory.

#### Command / Bash Example

```bash
namei -l /srv/app/config/settings.conf
```

#### Why It Works / Why It Matters

`namei -l` is extremely useful for diagnosing parent-directory permission failures.



### Enhanced Deep Dive — Deleting a File Depends on Directory Permissions

Deleting a file usually requires write+execute permission on the containing directory, not write permission on the file itself.

That is why a user can sometimes delete a read-only file from a directory they own.

#### Diagram / Mental Model

```text
Directory permissions control directory entry removal.

file.txt mode 0444
parent dir mode allows user write+execute
→ user may remove file entry
```

#### Why It Works / Why It Matters

Filesystem authorization operates on both the file object and its containing directory.



### Enhanced Deep Dive — Access Control Lists — ACL Foundation

Traditional owner/group/other permissions can be extended using POSIX ACLs to grant specific users/groups additional rights.

Commands:
- `getfacl`
- `setfacl`

#### Command / Bash Example

```bash
getfacl shared.txt

setfacl -m u:student1:rw shared.txt
getfacl shared.txt
```

#### Why It Works / Why It Matters

ACLs avoid creating overly broad permissions merely to support one exceptional user.

#### Security Implication

ACL masks can limit effective ACL permissions. Always inspect the final `getfacl` output.



### Enhanced Deep Dive — Default ACLs on Directories

A directory default ACL defines ACL entries inherited by newly created children.

This is useful for shared team directories.

#### Command / Bash Example

```bash
sudo setfacl -m d:g:devops:rwx /srv/devops
getfacl /srv/devops
```

#### Why It Works / Why It Matters

Default ACLs are more reliable than repeatedly fixing permissions manually.



### Enhanced Deep Dive — SGID Shared Directories

Setting SGID on a directory causes newly created files/subdirectories to inherit the directory's group rather than each creator's primary group.

Combine with suitable umask/default ACL for collaborative directories.

#### Command / Bash Example

```bash
sudo chgrp devops /srv/devops
sudo chmod 2770 /srv/devops
ls -ld /srv/devops
```

#### Expected Behavior / Output

```text
drwxrws--- ...
```

#### Why It Works / Why It Matters

This is a common team-directory pattern.



### Enhanced Deep Dive — Sticky Bit on Shared Writable Directories

A sticky directory allows multiple users to create entries while restricting who can delete/rename another user's files.

`/tmp` is the classic example.

#### Command / Bash Example

```bash
ls -ld /tmp
```

#### Expected Behavior / Output

```text
drwxrwxrwt ...
```

#### Why It Works / Why It Matters

World-writable without sticky protection would allow users to remove each other's files.



### Enhanced Deep Dive — SUID and Privilege Transition

SUID on an executable can cause the process effective UID to become the executable file owner's UID.

`/usr/bin/passwd` historically demonstrates why some tightly controlled privileged helper is needed to update protected authentication data.

#### Command / Bash Example

```bash
ls -l /usr/bin/passwd
```

#### Security Implication

SUID programs increase privilege-escalation risk. Do not create custom SUID programs casually.



### Enhanced Deep Dive — Linux Capabilities — Breaking Up Root Privilege

Linux capabilities divide some root powers into narrower privileges.

Example:
a network program may need permission to bind a privileged port without needing every root capability.

#### Command / Bash Example

```bash
getcap -r /usr/bin /usr/sbin 2>/dev/null | head
```

#### Why It Works / Why It Matters

Capabilities support least privilege beyond the all-or-nothing root model.

#### Security Implication

Capabilities can still grant powerful kernel privileges; inventory and review them.



### Enhanced Deep Dive — `sudoers` and `visudo`

`sudo` authorization is controlled by sudoers policy.

Use `visudo` because it validates syntax before installing changes.

#### Command / Bash Example

```bash
sudo visudo
sudo -l
```

#### Configuration Example

```text
%ops ALL=(root) /usr/bin/systemctl restart nginx
```

#### Why It Works / Why It Matters

Command-specific delegation is safer than granting unrestricted root shells.

#### Security Implication

Beware commands that themselves provide shell escapes or arbitrary file editing; a narrow-looking sudo rule can become equivalent to root.



### Enhanced Deep Dive — User Database Through NSS / `getent`

Commands such as `getent passwd` consult the configured Name Service Switch sources, not only local files.

Accounts may come from:
- local `/etc/passwd`
- LDAP
- SSSD/Active Directory integration
- other configured sources

#### Command / Bash Example

```bash
getent passwd
getent passwd "$USER"
grep '^passwd:' /etc/nsswitch.conf
```

#### Why It Works / Why It Matters

`grep /etc/passwd` can miss centrally managed identities.



### Enhanced Deep Dive — UID/GID Are the Real Ownership Identifiers

Files store numeric UID/GID ownership. User/group names are resolved for display.

If an account is deleted and later the UID is reused, old files can appear to belong to the new account.

#### Command / Bash Example

```bash
stat -c '%u %g %U %G %n' somefile
find / -xdev -nouser -o -nogroup 2>/dev/null | head
```

#### Security Implication

Review orphaned files and avoid careless UID reuse on sensitive systems.



### Enhanced Deep Dive — Password Aging

Linux account policy can track:
- last password change
- minimum/maximum age
- warning period
- inactivity/expiry

Use `chage` to inspect/manage local-account aging.

#### Command / Bash Example

```bash
sudo chage -l student1
```

#### Why It Works / Why It Matters

Password lifecycle is independent from filesystem permissions.



### Enhanced Deep Dive — Process Creation: Fork/Exec Mental Model

Unix process creation is conceptually split into:
- duplicate/create execution context (`fork`/`clone`)
- replace process image with a new program (`execve`)

Shells use this model to launch external commands.

#### Diagram / Mental Model

```text
Bash PID 1000
   ↓ fork
Child PID 1200
   ↓ execve("/usr/bin/ls")
ls process PID 1200
   ↓ exit
Bash receives exit status
```

#### Why It Works / Why It Matters

This explains parent/child relationships and why environment/file descriptors can be inherited.



### Enhanced Deep Dive — Process States

Common Linux process-state letters include:
- `R` running/runnable
- `S` interruptible sleep
- `D` uninterruptible sleep, often I/O-related
- `T` stopped/traced
- `Z` zombie

State interpretation is essential for load troubleshooting.

#### Command / Bash Example

```bash
ps -eo pid,ppid,state,wchan:24,cmd | head -n 30
```

#### Why It Works / Why It Matters

A high load average can include tasks in uninterruptible `D` state, not only CPU-heavy tasks.



### Enhanced Deep Dive — Zombie Processes

A zombie is a process that has exited but whose parent has not yet collected its exit status.

The zombie consumes very little memory but occupies a process-table entry.

#### Diagram / Mental Model

```text
Child exits
   ↓
kernel stores exit status
   ↓
parent has not wait()ed yet
   ↓
Z state
```

#### Troubleshooting

Fix the parent process behavior or restart the responsible service if appropriate. Killing the zombie itself is not meaningful because it has already exited.



### Enhanced Deep Dive — Orphan Processes

If a parent exits while a child keeps running, the child is re-parented to a suitable subreaper such as systemd/PID 1 depending on process hierarchy and service management.

#### Why It Works / Why It Matters

Orphan is not the same as zombie.



### Enhanced Deep Dive — Open Files and `lsof`

Linux treats sockets, pipes, regular files, devices, and many resources as file-descriptor-backed objects.

`lsof` maps processes to these open resources.

#### Command / Bash Example

```bash
sudo lsof -p $$
sudo lsof -iTCP -sTCP:LISTEN
```

#### Why It Works / Why It Matters

This connects process troubleshooting with storage and network troubleshooting.



### Enhanced Deep Dive — Process Environment

A process receives an environment at creation time. Changing an environment variable in your current shell does not modify the already-running service's environment.

Inspect:

#### Command / Bash Example

```bash
tr ' ' '
' < /proc/$$/environ | head
```

#### Security Implication

Environment inspection may reveal credentials/tokens; restrict access and do not paste sensitive output into tickets.



### Enhanced Deep Dive — Signals Are Requests, Not Universal Commands

Applications choose how to handle many signals.

- SIGTERM often means graceful shutdown
- SIGHUP often means reload, but not universally
- SIGKILL cannot be caught

#### Why It Works / Why It Matters

Always consult the application's documentation before assuming SIGHUP means reload.



### Enhanced Deep Dive — Load Average

Load average represents the average number of tasks runnable or in certain uninterruptible wait states over 1, 5, and 15 minutes.

Interpret relative to CPU count and workload.

#### Command / Bash Example

```bash
uptime
cat /proc/loadavg
nproc
```

#### Why It Works / Why It Matters

Load 4 on a 2-CPU machine differs from load 4 on a 32-CPU machine.



### Enhanced Deep Dive — CPU Time Categories

Linux CPU statistics distinguish categories such as:
- user
- system/kernel
- idle
- I/O wait
- steal time in virtualized systems

Tools such as `top`, `vmstat`, and `mpstat` expose parts of this view.

#### Command / Bash Example

```bash
top
vmstat 1 5
```

#### Why It Works / Why It Matters

100% CPU and 100% I/O wait indicate different bottlenecks.



### Enhanced Deep Dive — Memory: Free vs Available

Linux deliberately uses RAM for page cache.

`free` can look low while `available` remains healthy because cache can be reclaimed.

#### Diagram / Mental Model

```text
RAM
├─ application memory
├─ kernel memory
├─ page cache
└─ reclaimable cache

"free" alone is not the health metric.
```

#### Command / Bash Example

```bash
free -h
grep -E 'MemTotal|MemAvailable|Cached|Swap' /proc/meminfo
```

#### Why It Works / Why It Matters

Do not clear caches as a normal 'optimization'.



### Enhanced Deep Dive — OOM Killer Awareness

When the kernel cannot satisfy memory allocation under severe pressure, the Out-Of-Memory logic can select processes for termination.

Evidence appears in kernel logs.

#### Command / Bash Example

```bash
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

#### Troubleshooting

Investigate memory demand, leaks, limits, swap, and workload design rather than simply restarting the killed process.



### Enhanced Deep Dive — Virtual Memory and Swap

Processes use virtual address spaces. The kernel maps pages to RAM and may move eligible pages to swap depending on pressure and policy.

Swap can prevent abrupt failure during transient pressure but is much slower than RAM.

#### Why It Works / Why It Matters

Some swap use is not automatically a fault; sustained heavy swap-in/out with latency is a stronger warning.



### Enhanced Deep Dive — Cgroups Awareness

Control groups organize processes and apply resource accounting/limits for CPU, memory, I/O, and other controllers.

systemd services and containers commonly use cgroups.

#### Diagram / Mental Model

```text
Linux processes
   ↓ grouped
cgroup
├─ CPU accounting/limits
├─ memory limits
└─ I/O controls
```

#### Command / Bash Example

```bash
systemd-cgls
systemctl status sshd
```

#### Why It Works / Why It Matters

This becomes essential for systemd services, Docker, Kubernetes, and resource troubleshooting.



### Enhanced Deep Dive — Namespaces Awareness

Linux namespaces isolate views of resources such as:
- process IDs
- mounts
- networks
- hostnames
- users
- IPC

Containers combine namespaces with cgroups and filesystem mechanisms.

#### Diagram / Mental Model

```text
Same kernel
├─ namespace A → its own process/network view
└─ namespace B → different isolated view
```

#### Why It Works / Why It Matters

Containers are not separate kernels in the ordinary container model.



### Enhanced Deep Dive — systemd Unit Types

systemd manages more than services.

Common unit types:
- `.service`
- `.socket`
- `.timer`
- `.mount`
- `.target`
- `.path`
- `.device`

#### Command / Bash Example

```bash
systemctl list-units --type=socket
systemctl list-units --type=timer
systemctl list-units --type=mount
```

#### Why It Works / Why It Matters

systemd is a dependency/service orchestration system, not only a start/stop wrapper.



### Enhanced Deep Dive — `systemctl status` vs `is-active` vs `is-enabled`

These answer different questions.

- `status` → detailed runtime state
- `is-active` → is it currently active?
- `is-enabled` → is it configured for activation at boot/dependency?
- `is-failed` → failed state?

#### Command / Bash Example

```bash
systemctl is-active sshd
systemctl is-enabled sshd
systemctl is-failed sshd
```

#### Why It Works / Why It Matters

Enabled does not mean running; running does not mean enabled.



### Enhanced Deep Dive — systemd Dependencies and Ordering

Two important concepts differ:

**Requirement/dependency**
Whether another unit is needed/wanted.

**Ordering**
Whether a unit should start before/after another.

`After=` does not automatically mean `Requires=`.

#### Diagram / Mental Model

```text
Requires/Wants → dependency relationship

Before/After → startup ordering relationship
```

#### Why It Works / Why It Matters

Incorrect dependencies create fragile services that start before required resources exist.



### Enhanced Deep Dive — `daemon-reload`

After creating or modifying unit files, systemd must reload its manager configuration.

`daemon-reload` does not necessarily restart the service.

#### Command / Bash Example

```bash
sudo systemctl daemon-reload
sudo systemctl restart demo.service
```

#### Why It Works / Why It Matters

Reloading manager configuration and restarting a unit are separate actions.



### Enhanced Deep Dive — systemd Drop-In Overrides

Do not edit vendor unit files under `/usr/lib/systemd/system` for local customization.

Use drop-in overrides under `/etc/systemd/system/<unit>.d/`.

#### Command / Bash Example

```bash
sudo systemctl edit sshd.service
systemctl cat sshd.service
```

#### Why It Works / Why It Matters

Package upgrades can replace vendor unit files, while administrator overrides remain separate.



### Enhanced Deep Dive — systemd Targets

Targets group units into operational states such as multi-user or graphical operation.

Targets replace many historical SysV runlevel use cases.

#### Command / Bash Example

```bash
systemctl get-default
systemctl list-dependencies multi-user.target
```

#### Why It Works / Why It Matters

Boot is a dependency graph, not a simple fixed sequential script list.



### Enhanced Deep Dive — systemd Timers vs Cron

Timers can provide:
- dependency integration
- persistent catch-up behavior when configured
- journal logging
- randomized delays
- calendar and monotonic schedules

Cron is simple and universal, but timers integrate more deeply with systemd.

#### Command / Bash Example

```bash
systemctl list-timers
```

#### Why It Works / Why It Matters

Choose the scheduling system that fits observability and dependency requirements.



### Enhanced Deep Dive — Journald Structure

The journal stores structured metadata along with messages, such as:
- unit
- PID
- boot ID
- priority
- executable
- UID

Filtering can use these fields.

#### Command / Bash Example

```bash
journalctl -u sshd
journalctl _PID=1
journalctl -b -1
journalctl --since yesterday --until today
```

#### Why It Works / Why It Matters

Structured filtering is much stronger than blindly grepping a huge log.



### Enhanced Deep Dive — Persistent vs Volatile Journal Awareness

Depending on configuration/distribution, journal data may be stored persistently under `/var/log/journal` or only in volatile runtime storage.

Check configuration before assuming previous-boot logs are available.

#### Command / Bash Example

```bash
journalctl --list-boots
ls -ld /var/log/journal 2>/dev/null
```

#### Why It Works / Why It Matters

Incident investigation depends on retention.



### Enhanced Deep Dive — Log Rotation

Logs cannot grow forever. `logrotate` commonly rotates, compresses, retains, and removes old text logs according to policy.

Applications may need to reopen log files after rotation.

#### Command / Bash Example

```bash
ls /etc/logrotate.d/
cat /etc/logrotate.conf
```

#### Why It Works / Why It Matters

Deleting active logs manually can create deleted-open-file disk consumption.



### Enhanced Deep Dive — RPM Package Identity and Ownership

RPM tracks package metadata and installed file ownership.

Useful questions:
- Is package installed?
- What files belong to it?
- Which package owns this file?
- Has a packaged file changed?

#### Command / Bash Example

```bash
rpm -q openssh-server
rpm -ql openssh-server | head
rpm -qf /usr/sbin/sshd
rpm -V openssh-server
```

#### Why It Works / Why It Matters

Package metadata is a troubleshooting and integrity baseline.



### Enhanced Deep Dive — DNF Dependency Resolution

DNF resolves package dependencies and repository metadata.

Installing an RPM directly with low-level tools can bypass normal dependency resolution workflows.

#### Command / Bash Example

```bash
dnf repoquery --requires bash | head
dnf history
```

#### Why It Works / Why It Matters

Package-manager history can help identify recent software changes during troubleshooting.



### Enhanced Deep Dive — Repository Trust and GPG Signatures

Package repositories and RPM signatures help establish software provenance/integrity.

Do not disable signature checking merely to install an unknown package.

#### Command / Bash Example

```bash
rpm -q gpg-pubkey
dnf repolist -v
```

#### Security Implication

Third-party repositories expand the software supply-chain trust boundary.



### Enhanced Deep Dive — Package Install Does Not Equal Service Enablement

Software lifecycle stages are separate:

```text
package available
   ↓ install
files placed
   ↓ configure
service start
   ↓ enable
service boot persistence
```

#### Why It Works / Why It Matters

Troubleshooting must determine which stage is missing.



### Enhanced Deep Dive — Partition Tables — GPT vs MBR Awareness

A physical/virtual disk can contain a partition table.

Modern systems commonly use GPT. Older systems may use MBR/DOS partition tables.

Partitions then hold filesystems, swap, LVM PVs, or other structures.

#### Diagram / Mental Model

```text
/dev/sdb
├─ partition table GPT
├─ /dev/sdb1 → filesystem
└─ /dev/sdb2 → LVM PV
```

#### Why It Works / Why It Matters

Do not format a whole device until you understand its existing partition/storage role.



### Enhanced Deep Dive — LVM Foundation

Logical Volume Manager adds an abstraction layer:

- PV — Physical Volume
- VG — Volume Group
- LV — Logical Volume

Filesystem is then created on the LV.

#### Diagram / Mental Model

```text
/dev/sdb1 ─┐
/dev/sdc1 ─┴─> VG data
              ├─ LV logs
              └─ LV app
```

#### Why It Works / Why It Matters

LVM supports flexible allocation and later resizing; detailed administration belongs in RHCSA-oriented courses.



### Enhanced Deep Dive — Filesystem Creation Is Destructive

`mkfs` creates a new filesystem structure and can destroy accessibility to existing data on the selected device.

Always identify the correct block device first.

#### Command / Bash Example

```bash
lsblk -f
blkid
findmnt
```

#### Security Implication

Never run `mkfs` on an unknown device or production disk without a verified change plan and backup.



### Enhanced Deep Dive — XFS vs ext4 Foundation

Both are mature Linux filesystems.

At a high level:
- XFS is commonly used by Red Hat-family defaults and scales well for large filesystems.
- ext4 is broadly used and supports online growth and offline shrinking under specific workflows.
- XFS supports growth but not ordinary shrinking.

Exact feature/support details depend on OS release.

#### Why It Works / Why It Matters

Filesystem choice affects recovery, resize, tooling, and operational procedures.



### Enhanced Deep Dive — Filesystem Usage vs Directory Usage

`df` asks the filesystem how many blocks are used/free.

`du` walks visible directory entries and sums file usage.

They can disagree due to:
- deleted-open files
- hidden files under mount points
- reserved blocks/features
- snapshots/metadata

#### Why It Works / Why It Matters

Use both rather than assuming one is 'wrong'.



### Enhanced Deep Dive — I/O Observation

Storage performance problems require more than free-space checks.

Useful foundation tools:
- `iostat` when sysstat is installed
- `vmstat`
- `/proc/diskstats`

#### Command / Bash Example

```bash
vmstat 1 5
iostat -xz 1 3 2>/dev/null || true
```

#### Why It Works / Why It Matters

A filesystem can have plenty of free space but still suffer latency or device saturation.



### Enhanced Deep Dive — Kernel Modules

Many drivers/features can be built as loadable kernel modules.

Inspect:

#### Command / Bash Example

```bash
lsmod | head
modinfo xfs 2>/dev/null | head
```

#### Why It Works / Why It Matters

Hardware and network/filesystem support may depend on loaded modules.

#### Security Implication

Loading/unloading kernel modules is privileged and can destabilize a system; later hardening may restrict module loading.



### Enhanced Deep Dive — `sysctl` and Kernel Runtime Parameters

Many kernel settings are exposed through `/proc/sys` and managed using `sysctl`.

Inspect:

#### Diagram / Mental Model

```text
/etc/sysctl.conf + /etc/sysctl.d/*.conf
             ↓
          sysctl
             ↓
        /proc/sys/*
             ↓
        kernel setting
```

#### Command / Bash Example

```bash
sysctl kernel.hostname
sysctl net.ipv4.ip_forward
```

#### Security Implication

Do not copy Internet tuning values blindly. Kernel parameters can affect security, routing, memory, and performance.



### Enhanced Deep Dive — Network Configuration: Runtime vs Persistent

Commands such as `ip address add` modify runtime kernel networking state.

NetworkManager connection profiles provide persistent configuration on Red Hat-family systems.

A reboot may erase temporary `ip` changes.

#### Diagram / Mental Model

```text
nmcli connection profile
       ↓ activation
NetworkManager
       ↓
kernel interface/address/route state
```

#### Command / Bash Example

```bash
nmcli device status
nmcli connection show
ip -br address
ip route
```

#### Why It Works / Why It Matters

Always know whether you changed runtime state, persistent configuration, or both.



### Enhanced Deep Dive — Network Interface Administrative vs Operational State

An interface can be:
- administratively enabled/disabled
- carrier/link up/down
- configured/unconfigured at Layer 3

`ip link` and NetworkManager expose different aspects.

#### Command / Bash Example

```bash
ip -details link show
nmcli device status
```

#### Why It Works / Why It Matters

An interface being `UP` does not guarantee IP connectivity.



### Enhanced Deep Dive — Host Route Lookup

The host chooses a route before ARP/NDP.

Use:

#### Diagram / Mental Model

```text
Destination
   ↓
host route table
   ├─ local subnet → resolve destination neighbor
   └─ remote       → resolve next-hop gateway
```

#### Command / Bash Example

```bash
ip route get 8.8.8.8
ip route get 192.168.1.50
```

#### Why It Works / Why It Matters

This connects Linux administration directly to the networking phase.



### Enhanced Deep Dive — Neighbor Cache States

`ip neigh` can show states such as:
- REACHABLE
- STALE
- DELAY
- PROBE
- INCOMPLETE
- FAILED

These indicate neighbor-resolution lifecycle, not application health.

#### Command / Bash Example

```bash
ip neigh show
```

#### Troubleshooting

`INCOMPLETE` or `FAILED` for a local next hop can indicate Layer-2/VLAN/ARP/NDP reachability problems.



### Enhanced Deep Dive — DNS Resolution Stack

Linux applications may resolve names through libc/NSS, local files, systemd-resolved where used, DNS servers, and other configured sources.

`getent hosts` tests the system's normal name-service path better than `dig` alone in some troubleshooting cases.

#### Diagram / Mental Model

```text
Application
   ↓ getaddrinfo()
NSS configuration
   ├─ /etc/hosts
   └─ DNS resolver
```

#### Command / Bash Example

```bash
grep '^hosts:' /etc/nsswitch.conf
getent ahosts example.com
dig example.com
```

#### Why It Works / Why It Matters

`dig` can succeed while an application still behaves differently because the application's resolver path differs.



### Enhanced Deep Dive — Listening Socket Binding

A service can bind:
- loopback only
- one interface address
- all IPv4 addresses
- all IPv6 addresses

Examples:
- `127.0.0.1:8080` → local only
- `0.0.0.0:8080` → all IPv4 interfaces

#### Command / Bash Example

```bash
ss -lntp
```

#### Why It Works / Why It Matters

A service may be active but unreachable remotely because it listens only on loopback.



### Enhanced Deep Dive — TCP Connection States on Linux

`ss -tan` can reveal connection lifecycle such as:
- LISTEN
- SYN-SENT
- SYN-RECV
- ESTAB
- FIN-WAIT
- TIME-WAIT

These states help isolate whether a connection reaches the server.

#### Command / Bash Example

```bash
ss -tan
ss -tan state established
```

#### Why It Works / Why It Matters

A SYN-SENT connection suggests the client has not completed the handshake; ESTAB proves transport succeeded.



### Enhanced Deep Dive — `curl` as an Application-Layer Test

After IP, route, DNS, and socket checks, `curl` tests HTTP/HTTPS application behavior.

Use verbose mode to inspect connection and TLS progress.

#### Command / Bash Example

```bash
curl -I https://example.com
curl -v https://example.com/ -o /dev/null
```

#### Why It Works / Why It Matters

`ping` success does not prove an HTTPS service works.



### Enhanced Deep Dive — SSH Host Keys and `known_hosts`

SSH authenticates the server using a host key.

The client records trusted host-key information in `~/.ssh/known_hosts`.

A changed host key can indicate:
- legitimate server rebuild/rekey
- DNS/IP reassignment
- or possible interception

#### Command / Bash Example

```bash
ssh-keygen -F server01.lab.example
```

#### Security Implication

Do not blindly delete a host-key warning without verifying the server's new fingerprint through a trusted channel.



### Enhanced Deep Dive — SSH User Key Pair

A user SSH key pair has:
- private key — secret
- public key — distributable

The server stores approved public keys in `authorized_keys`.

#### Diagram / Mental Model

```text
Client private key
     ↓ proves possession
SSH protocol challenge/signature
     ↓
Server compares against authorized public key
```

#### Security Implication

Protect private keys with filesystem permissions and, where appropriate, a passphrase/agent.



### Enhanced Deep Dive — `ssh-agent` Awareness

An SSH agent can hold decrypted key material in memory so you do not repeatedly type a passphrase.

It can also be forwarded, but agent forwarding extends trust to the remote system and should be used cautiously.

#### Command / Bash Example

```bash
ssh-add -l
```

#### Security Implication

Do not enable agent forwarding globally without a clear need.



### Enhanced Deep Dive — SCP, SFTP, and `rsync` Awareness

SSH can transport file-management protocols/tools.

Examples:
- `scp`
- `sftp`
- `rsync -e ssh`

For repeated directory synchronization, `rsync` can be more efficient than copying everything again.

#### Command / Bash Example

```bash
rsync -av --dry-run ./reports/ user@server:/srv/reports/
```

#### Why It Works / Why It Matters

Use `--dry-run` before large synchronization or deletion-oriented operations.



### Enhanced Deep Dive — SSH Server Hardening Foundation

A secure SSH baseline considers:
- root login policy
- password authentication policy
- public-key authentication
- allowed users/groups
- management firewall scope
- idle/session policy
- current cryptographic defaults

#### Command / Bash Example

```bash
sudo sshd -t
sudo sshd -T | head
```

#### Security Implication

Validate the effective configuration and keep a recovery session/console before remote changes.



### Enhanced Deep Dive — firewalld Zones

firewalld associates network interfaces/sources with zones that express trust policy.

A service allowed in one zone is not necessarily allowed in another.

#### Command / Bash Example

```bash
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --list-all
```

#### Why It Works / Why It Matters

Firewall troubleshooting requires knowing the active zone for the interface/source.



### Enhanced Deep Dive — Runtime vs Permanent firewalld Rules

firewalld can maintain runtime policy separately from persistent configuration.

A runtime rule may disappear after reload/reboot unless made permanent.

#### Command / Bash Example

```bash
sudo firewall-cmd --add-service=http
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

#### Security Implication

Do not open broad ports merely to test. Prefer specific services/sources and remove temporary lab rules.



### Enhanced Deep Dive — SELinux: DAC and MAC Are Separate

Traditional Unix permissions are Discretionary Access Control (DAC).

SELinux adds Mandatory Access Control (MAC) decisions using security contexts and policy.

An operation must pass both.

#### Diagram / Mental Model

```text
Process requests file access
       ↓
DAC permissions/ACL
       ↓ allow?
SELinux policy/context
       ↓ allow?
Kernel permits access
```

#### Why It Works / Why It Matters

`chmod 777` cannot override an SELinux denial.



### Enhanced Deep Dive — SELinux Context Fields

A context commonly appears as:

`user:role:type:level`

For routine administration, the **type** is often the most important field.

#### Command / Bash Example

```bash
ls -Z /var/www 2>/dev/null
ps -eZ | head
```

#### Why It Works / Why It Matters

Services are usually allowed to access objects carrying expected types.



### Enhanced Deep Dive — SELinux Label Troubleshooting

If a file is moved from an unusual location into a service directory, it can retain the wrong context.

Preferred remediation often uses:
- defined file-context policy
- `restorecon`

rather than disabling SELinux.

#### Command / Bash Example

```bash
sudo restorecon -Rv /var/www/html 2>/dev/null
```

#### Security Implication

Do not blindly use broad custom policy generators before understanding the denial.



### Enhanced Deep Dive — SELinux Denial Evidence

SELinux denials are commonly logged through audit mechanisms.

Foundation investigation:

#### Command / Bash Example

```bash
sudo ausearch -m AVC -ts recent 2>/dev/null | tail -n 20
journalctl | grep -i 'avc:  denied' | tail
```

#### Why It Works / Why It Matters

Evidence distinguishes a real policy denial from ordinary file permissions or application errors.



### Enhanced Deep Dive — Boot Process — UEFI/BIOS to Userspace

The boot process crosses several distinct trust/execution stages.

A simplified modern path:

#### Diagram / Mental Model

```text
Firmware BIOS/UEFI
      ↓
Boot manager / GRUB
      ↓
Kernel image
      ↓
initramfs
      ↓
discover storage / root FS
      ↓
switch to real root filesystem
      ↓
systemd PID 1
      ↓
targets/services
      ↓
login/SSH
```

#### Why It Works / Why It Matters

A boot failure must be located at the correct stage.



### Enhanced Deep Dive — initramfs Purpose

The initramfs is a temporary early userspace containing tools/drivers needed before the real root filesystem is available.

It can include:
- storage drivers
- LVM support
- encryption support
- filesystem modules

#### Command / Bash Example

```bash
lsinitrd 2>/dev/null | head
```

#### Why It Works / Why It Matters

If root storage cannot be discovered early, the system may fail before systemd reaches normal targets.



### Enhanced Deep Dive — Kernel Command Line

Bootloader-provided kernel parameters can control:
- root device
- console
- debugging
- SELinux mode
- systemd target/emergency behavior
- device-specific settings

#### Command / Bash Example

```bash
cat /proc/cmdline
```

#### Security Implication

Temporary boot parameters can weaken security; document and revert diagnostic overrides.



### Enhanced Deep Dive — Rescue and Emergency Modes Awareness

systemd provides reduced boot targets for recovery.

**rescue**
Minimal services with local recovery shell.

**emergency**
Even more minimal environment, useful when normal mounts/services fail.

Use console/recovery access carefully.

#### Why It Works / Why It Matters

These modes are recovery mechanisms, not normal operating states.



### Enhanced Deep Dive — `/proc` Is a Live Kernel/Process View

Files under `/proc` are generated by the kernel.

Examples:
- `/proc/<PID>/cmdline`
- `/proc/<PID>/fd`
- `/proc/<PID>/status`
- `/proc/meminfo`
- `/proc/net/*`

#### Command / Bash Example

```bash
cat /proc/$$/status | head
ls -l /proc/$$/fd
```

#### Why It Works / Why It Matters

Reading `/proc` can answer questions without special application tooling.



### Enhanced Deep Dive — `/sys` and the Device Model

sysfs exposes structured kernel device/class/subsystem information.

Examples:
- network interfaces
- block devices
- PCI devices
- power/state information

#### Command / Bash Example

```bash
ls /sys/class/net
ls /sys/class/block
readlink -f /sys/class/net/*/device 2>/dev/null | head
```

#### Why It Works / Why It Matters

Tools such as udev and system managers rely on this device model.



### Enhanced Deep Dive — udev Awareness

udev handles userspace device-event management and device-node naming based on kernel events and rules.

When hardware appears:

#### Diagram / Mental Model

```text
Kernel detects device
       ↓
uevent
       ↓
udev
       ↓
rules
       ↓
device node / permissions / symlink
```

#### Why It Works / Why It Matters

Persistent disk/network naming is not arbitrary; device-event rules participate.



### Enhanced Deep Dive — Shell Startup: Login vs Interactive

Different Bash startup files are used depending on whether the shell is:
- login/non-login
- interactive/non-interactive

This explains why an environment variable or alias can work in SSH login but fail in cron/systemd.

#### Why It Works / Why It Matters

Automation should not depend on interactive shell startup files unless explicitly designed.



### Enhanced Deep Dive — Cron Has a Minimal Environment

Cron jobs often receive a smaller/different environment than your interactive shell.

Use:
- absolute paths
- controlled PATH
- explicit working directories
- logging

#### Configuration Example

```text
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin

0 2 * * * /opt/linux-lab/scripts/daily-health.sh >>/var/log/lab-health.log 2>&1
```

#### Why It Works / Why It Matters

A script that works manually can fail in cron because of environment differences.



### Enhanced Deep Dive — Bash Functions for Administration

Functions group reusable logic and return exit statuses.

Example:

#### Command / Bash Example

```bash
check_command() {
    command -v "$1" >/dev/null 2>&1
}

if ! check_command ss; then
    printf 'ERROR: ss is missing\n' >&2
    exit 1
fi
```

#### Why It Works / Why It Matters

Small reusable functions make operational scripts easier to test and maintain.



### Enhanced Deep Dive — Arrays in Bash

Arrays help avoid unsafe string-concatenation when building command argument lists.

Example:

#### Command / Bash Example

```bash
files=(/var/log/messages /var/log/secure)

for file in "${files[@]}"; do
    if [[ -r "$file" ]]; then
        printf '%s\n' "$file"
    fi
done
```

#### Security Implication

Quoted array expansion preserves argument boundaries.



### Enhanced Deep Dive — `[[ ... ]]` vs `[ ... ]` Foundation

Bash provides both the traditional `test`/`[` form and the more capable `[[ ... ]]` conditional syntax.

`[[ ... ]]` avoids some word-splitting/pathname-expansion surprises in Bash scripts.

#### Command / Bash Example

```bash
if [[ -f "$config" && -r "$config" ]]; then
    echo "Readable config"
fi
```

#### Why It Works / Why It Matters

Use syntax intentionally and remember `[[` is shell-specific, not POSIX `/bin/sh` syntax.



### Enhanced Deep Dive — Pipeline Exit Status and `pipefail`

Normally a pipeline's status is often the status of the final command.

This can hide failure in an earlier stage.

`set -o pipefail` makes the pipeline fail when an earlier component fails under Bash's rules.

#### Command / Bash Example

```bash
set -o pipefail
grep pattern missing-file | wc -l
echo "$?"
```

#### Why It Works / Why It Matters

Important for monitoring/backup scripts where a partial pipeline must not appear successful.



### Enhanced Deep Dive — Safer Temporary Files

Predictable filenames under `/tmp` can collide or be manipulated by other users.

Use `mktemp`.

#### Command / Bash Example

```bash
tmpfile=$(mktemp)
trap 'rm -f "$tmpfile"' EXIT
printf 'temporary data\n' > "$tmpfile"
```

#### Security Implication

Secure temporary-file creation reduces race and symlink attacks.



### Enhanced Deep Dive — `trap` for Cleanup

`trap` lets a script react to shell exit/signals and perform cleanup.

#### Command / Bash Example

```bash
workdir=$(mktemp -d)

cleanup() {
    rm -rf -- "$workdir"
}

trap cleanup EXIT
```

#### Why It Works / Why It Matters

Cleanup should happen even when the script exits early.



### Enhanced Deep Dive — `find -exec` and `xargs` Safely

Filenames can contain spaces, tabs, newlines, and leading dashes.

Safer patterns avoid parsing `ls` output.

#### Command / Bash Example

```bash
find /var/tmp -type f -name '*.tmp' -print0 |
    xargs -0 -r ls -l --
```

#### Why It Works / Why It Matters

NUL-delimited processing preserves arbitrary filename boundaries.



### Enhanced Deep Dive — `sed` and `awk` Foundation

Linux administrators frequently use stream processors.

`sed` is strong for line-oriented transformations.

`awk` is strong for field-oriented records and simple reporting.

#### Command / Bash Example

```bash
printf '%s\n' 'server=old' | sed 's/old/new/'

awk -F: '{print $1, $3}' /etc/passwd | head
```

#### Why It Works / Why It Matters

These tools reduce the need for fragile long grep/cut pipelines.



### Enhanced Deep Dive — Checksums

Hash functions such as SHA-256 produce a digest useful for detecting accidental or unauthorized file changes.

They do not prove who created the file unless paired with a trusted signature/source.

#### Command / Bash Example

```bash
sha256sum important.conf
```

#### Security Implication

A checksum from the same untrusted source as a download does not establish authenticity.



### Enhanced Deep Dive — Backup Is Not Archive

An archive bundles files. A backup is a recoverability strategy.

A real backup plan includes:
- independent copy
- retention
- restore testing
- protection from the same failure domain

#### Diagram / Mental Model

```text
tar.gz on same disk
= archive

backup copy on independent protected storage
+ retention
+ restore test
= backup strategy
```

#### Why It Works / Why It Matters

A tar file stored beside the source does not protect against disk loss.



### Enhanced Deep Dive — File Synchronization with `rsync`

`rsync` copies only required differences and can preserve metadata.

Important options can include:
- `-a` archive mode
- `-v` verbose
- `--delete` remove destination files absent from source
- `--dry-run` preview

#### Command / Bash Example

```bash
rsync -av --dry-run /srv/data/ /backup/data/
```

#### Security Implication

Treat `--delete` as destructive. Always verify source/destination direction and run a dry-run first.



### Enhanced Deep Dive — Troubleshooting Permission Denied as a Decision Tree

A permission error can be caused by many layers.

#### Diagram / Mental Model

```text
Permission denied
   ↓
Correct user/group?
   ↓
File mode?
   ↓
Parent directory x permission?
   ↓
ACL mask/entry?
   ↓
mount noexec/ro?
   ↓
SELinux denial?
   ↓
service sandbox/capability?
```

#### Command / Bash Example

```bash
id
namei -l /path/to/file
getfacl /path/to/file
findmnt -T /path/to/file
getenforce
```

#### Why It Works / Why It Matters

`chmod 777` only changes one layer and can create a security problem without fixing the real cause.



### Enhanced Deep Dive — Troubleshooting Service Failure as a Decision Tree

Use state and evidence rather than repeated restarts.

#### Diagram / Mental Model

```text
Service unavailable
   ↓
Package installed?
   ↓
Config valid?
   ↓
systemd active?
   ↓
journal errors?
   ↓
socket listening?
   ↓
firewall?
   ↓
SELinux?
   ↓
route/DNS?
   ↓
application health?
```

#### Command / Bash Example

```bash
rpm -q openssh-server
sudo sshd -t
systemctl status sshd
journalctl -u sshd -b
ss -lntp
sudo firewall-cmd --list-all
getenforce
```

#### Why It Works / Why It Matters

Each command answers a specific question.



### Enhanced Deep Dive — Troubleshooting Disk Space

Use several measurements:

#### Diagram / Mental Model

```text
df -h → filesystem blocks
df -i → inode counts
du    → visible directory usage
lsof +L1 → deleted-open files
findmnt → mount topology
```

#### Why It Works / Why It Matters

Disk-full incidents often become worse when operators delete files before identifying which filesystem is actually full.



### Enhanced Deep Dive — Troubleshooting CPU/Load

A structured workflow:

1. confirm CPU count/load
2. inspect top processes
3. distinguish user/system/iowait
4. inspect process state
5. inspect logs/recent changes
6. determine whether CPU or I/O is the bottleneck

#### Command / Bash Example

```bash
uptime
nproc
top
ps -eo pid,ppid,state,%cpu,%mem,cmd --sort=-%cpu | head
vmstat 1 5
```

#### Why It Works / Why It Matters

High load and high CPU are related but not identical.



### Enhanced Deep Dive — Troubleshooting Memory

Use:
- `free -h`
- process RSS
- swap activity
- OOM logs
- cgroup/service limits where relevant

#### Command / Bash Example

```bash
free -h
ps -eo pid,user,rss,%mem,cmd --sort=-rss | head
journalctl -k | grep -i -E 'oom|out of memory'
```

#### Why It Works / Why It Matters

A process can fail due to a cgroup limit even when host-wide free memory exists.



### Enhanced Deep Dive — Troubleshooting Network Layer by Layer

Use the same model learned in Phase 4.

#### Diagram / Mental Model

```text
Interface/link
   ↓
IP address
   ↓
Route
   ↓
Neighbor ARP/NDP
   ↓
DNS
   ↓
TCP/UDP socket
   ↓
Firewall/SELinux
   ↓
Application
```

#### Command / Bash Example

```bash
ip -br link
ip -br address
ip route
ip neigh
getent hosts example.com
ss -tulpen
curl -v https://example.com/
```

#### Why It Works / Why It Matters

Do not change DNS when the interface has no address; do not restart the application when the route is missing.



### Enhanced Deep Dive — Baseline Before Troubleshooting

A baseline records what 'healthy' looked like.

Useful data:
- OS/kernel
- hostname
- interfaces/routes
- mount layout
- filesystem utilization
- enabled/running services
- listening sockets
- package versions
- CPU/memory

#### Why It Works / Why It Matters

Without a baseline, every unusual observation looks suspicious.



### Enhanced Deep Dive — Change History

Many incidents follow recent changes.

Check:
- `dnf history`
- shell history with caution
- configuration-management logs
- system journal
- deployment records

#### Security Implication

Shell history is incomplete evidence and may contain secrets. It is not a forensic audit log.



### Enhanced Deep Dive — Linux Security Layer Map

A service request can be restricted by several independent controls.

#### Diagram / Mental Model

```text
Network packet
   ↓
host firewall
   ↓
socket/listener
   ↓
process identity
   ↓
filesystem DAC
   ↓
ACL
   ↓
SELinux
   ↓
capabilities/cgroup/systemd sandbox
   ↓
application authorization
```

#### Why It Works / Why It Matters

Security troubleshooting must identify the exact layer denying access.



### Enhanced Deep Dive — Containers as a Linux Concept Bridge

Containers later in the curriculum depend on Linux primitives already introduced here:

- namespaces → isolation
- cgroups → resource control
- capabilities → reduced privilege
- filesystems/mounts → container root filesystem
- networking → veth/bridges/routes
- processes → container workload

#### Diagram / Mental Model

```text
Container
├─ process namespace
├─ network namespace
├─ mount namespace
├─ cgroup limits
└─ capability set
       ↓
same Linux kernel
```

#### Why It Works / Why It Matters

Strong Linux fundamentals make Docker/Kubernetes behavior much easier to understand.



### Enhanced Deep Dive — Linux in Cybersecurity

The same Linux primitives become security evidence:

- users/groups → identity
- processes → malicious execution/investigation
- sockets → network exposure
- logs → event reconstruction
- package database → software inventory
- hashes → integrity
- permissions/ACL/SELinux → access control
- systemd → persistence/services
- cron/timers → scheduled persistence/automation

#### Security Implication

Security analysis should use authorized systems and preserve evidence carefully when an incident is suspected.



### Enhanced Deep Dive — Final Linux Administration Mental Model

When entering an unfamiliar Linux server, inspect in this order:

1. Who/where am I?
2. What OS/kernel is this?
3. What is running?
4. What is listening?
5. What storage is mounted?
6. What network addresses/routes exist?
7. What failed?
8. What changed?
9. What do logs say?
10. What security controls apply?

#### Command / Bash Example

```bash
whoami
hostnamectl
cat /etc/os-release
uname -r
systemctl --failed
ps -ef
ss -tulpen
lsblk -f
findmnt
ip -br address
ip route
journalctl -p err -b
getenforce
```

#### Why It Works / Why It Matters

This produces orientation before modification.




# Course 102 Coverage Audit and Added Missing/Weak Topics

The lecture list supplied for **Course 102 — Understanding Linux** contains 28 lecture topics. The existing Linux Essentials material already covers the full topic list at a conceptual level. The following additions make several topics that were previously implicit or comparatively brief **explicit and deeper**, especially wildcards, composite commands, process monitoring, file-handling internals, Linux devices/drivers, filesystem internals, virtual filesystems, and Linux networking applications.

## Coverage Map

| Course 102 Lecture | Coverage in This Course | Status |
|---|---|---|
| 1. Course Overview | Topic, objectives, prerequisites, architecture, completion checklist | Covered |
| 2. Unwrapping Linux | Linux vs GNU/Linux, kernel, user space, distributions, boot architecture | Covered |
| 3. Basic Concepts and Commands | Shell, command syntax, paths, navigation, files, help, command lookup | Covered |
| 4. Using Wild Cards | Globbing section plus expanded wildcard deep dive below | Covered + Expanded |
| 5. File Handling Internals | Inodes, links, descriptors, open files, deletion semantics; expanded below | Covered + Expanded |
| 6. Seeking Help | `man`, manual sections, `apropos`, `whatis`, `--help`; expanded below | Covered + Expanded |
| 7. Simple Utilities | `cat`, `less`, `head`, `tail`, `wc`, `sort`, `uniq`, `cut`, `tr`, `tee` | Covered |
| 8. Composite Commands | Pipes/redirection existed; command lists/grouping/subshells added below | Covered + Expanded |
| 9. Input Output Internals | stdin/stdout/stderr, descriptors, redirection order, pipelines, `tee` | Covered |
| 10. Learning About the Shell | builtins, parsing, quoting, history, startup, PATH, expansion | Covered |
| 11. Environment Variables | shell variables, export/inheritance, PATH, startup files | Covered |
| 12. Basic Text Handling | grep, cut, sort, uniq, tr, tee, sed, awk | Covered |
| 13. Regular Expressions | basic regex and extended-regex usage | Covered |
| 14. Users and Permissions | passwd/shadow/group, UID/GID, chmod/chown, ACLs, sudo, special bits | Covered |
| 15. Process Management Part 1 | PID/PPID, ps, jobs, signals, nice/renice | Covered |
| 16. Process Management Part 2 | process creation, states, zombies, orphans, open files | Covered |
| 17. Process Monitoring | `top`, `ps`, load, memory, I/O; additional tools added below | Covered + Expanded |
| 18. Process Life Cycle | fork/exec, parent/child, exit status, zombie/orphan lifecycle | Covered |
| 19. Using Signals | SIGTERM, SIGKILL, SIGHUP, SIGINT and application-specific handling | Covered |
| 20. Networking in Linux — Basic Concepts | links, addresses, routes, neighbors, DNS, NetworkManager | Covered |
| 21. Networking in Linux — Applications | SSH, curl, DNS tools, sockets; application toolkit expanded below | Covered + Expanded |
| 22. Package Management | RPM, DNF, repositories, signatures, package verification/history | Covered |
| 23. Searching for Files | find, locate, which, type, whereis, safe find/xargs | Covered |
| 24. Archiving and Compression | tar, gzip, archive vs backup, rsync | Covered |
| 25. Devices and Device Drivers | hardware, kernel modules, udev, `/sys`; device-file internals added below | Covered + Expanded |
| 26. FileSystems in Linux Part 1 | hierarchy, block devices, filesystem vs mount point, XFS/ext4 | Covered |
| 27. FileSystems in Linux Part 2 | fstab, mount options, LVM foundation, disk usage; internals added below | Covered + Expanded |
| 28. Virtual FileSystems | `/proc`, `/sys`; tmpfs/devtmpfs/cgroupfs added below | Covered + Expanded |

---

## Added Deep Dive — Wildcards and Shell Globbing in Detail

A **wildcard/glob** is expanded by the shell **before** the target program runs.

```text
Command typed:

cp *.log /backup/

        ↓ Bash pathname expansion

cp app.log access.log error.log /backup/

        ↓ exec

cp receives the expanded filenames
```

The `cp` program does not normally interpret `*.log`; Bash does.

### Main glob operators

```text
*        zero or more characters
?        exactly one character
[abc]    one character from the set
[a-z]    one character from the range
[!0-9]   one character NOT in the set
```

Examples:

```bash
printf '%s\n' *.conf
printf '%s\n' file?.txt
printf '%s\n' server[1-4].log
printf '%s\n' [!0-9]*.txt
```

Suppose:

```text
file1.txt
file2.txt
file10.txt
fileA.txt
```

Then:

```bash
printf '%s\n' file?.txt
```

matches:

```text
file1.txt
file2.txt
fileA.txt
```

but not:

```text
file10.txt
```

because `?` represents exactly one character.

### Hidden files and globs

Ordinary `*` does not normally match leading-dot names.

```text
*
```

does not normally include:

```text
.bashrc
.ssh
.config
```

Inspect safely with:

```bash
printf '%s\n' .*
```

Be careful because dot-file patterns can behave unexpectedly across shells/settings.

### Unmatched globs

By default, Bash can leave an unmatched glob unchanged:

```bash
printf '%s\n' *.does-not-exist
```

may print:

```text
*.does-not-exist
```

Bash options can alter this behavior:

```bash
shopt -s nullglob
shopt -s failglob
```

Conceptually:

```text
default:
no matches → pattern can remain literal

nullglob:
no matches → expands to nothing

failglob:
no matches → shell reports error
```

This matters greatly in scripts.

Bad:

```bash
for file in *.log; do
    process "$file"
done
```

If no log exists, the literal string `*.log` may be processed.

Safer Bash pattern:

```bash
shopt -s nullglob

logs=( *.log )

for file in "${logs[@]}"; do
    printf 'Processing: %s\n' "$file"
done
```

### Globbing vs regex

```text
Shell glob:
*.log

Regex:
.*\.log$
```

They are different pattern languages.

---

## Added Deep Dive — Composite Commands, Lists, Grouping, and Subshells

Linux shell work frequently combines commands.

### Sequential list: `;`

```bash
date ; hostname ; uptime
```

Each command is attempted in sequence regardless of whether the previous command succeeded.

```text
command1
   ↓
command2
   ↓
command3
```

### AND list: `&&`

Run the next command only if the previous command succeeds.

```bash
mkdir -p backup &&
cp important.conf backup/
```

Mental model:

```text
command1
   ↓
exit status 0?
 ├─ yes → command2
 └─ no  → stop this AND chain
```

This is useful for dependent operations.

### OR list: `||`

Run the next command only if the previous command fails.

```bash
systemctl is-active nginx ||
echo "nginx is not active"
```

Mental model:

```text
command1
   ↓
success?
 ├─ yes → skip command2
 └─ no  → command2
```

### Combining `&&` and `||`

```bash
test -f /etc/hosts &&
echo "hosts exists" ||
echo "hosts missing"
```

Do not treat this as a universal ternary operator because unexpected command failures in the middle can change behavior.

For scripts, `if` is usually clearer:

```bash
if [[ -f /etc/hosts ]]; then
    echo "hosts exists"
else
    echo "hosts missing"
fi
```

### Background execution: `&`

```bash
sleep 300 &
```

The shell starts the command without waiting for normal completion.

Inspect:

```bash
jobs
ps -f
```

### Pipeline: `|`

```bash
ps -ef |
grep '[s]shd'
```

Conceptually:

```text
ps stdout
   ↓ pipe
grep stdin
   ↓
terminal
```

### Command grouping with braces

```bash
{
    date
    hostname
    uptime
} > system-summary.txt
```

The group runs in the **current shell context**.

This is useful when applying one redirection to several commands.

### Subshell grouping with parentheses

```bash
(
    cd /var/log || exit
    pwd
    ls
)

pwd
```

The parent shell's working directory is unchanged because the grouped commands run in a subshell.

```text
Parent shell cwd=/home/user
        ↓
      subshell
      cd /var/log
      work
      exit
        ↓
Parent still cwd=/home/user
```

### Practical comparison

```bash
x=1

{ x=2; }
echo "$x"
```

prints:

```text
2
```

But:

```bash
x=1

( x=2 )
echo "$x"
```

prints:

```text
1
```

because the assignment happened in the subshell.

---

## Added Deep Dive — Seeking Help Like a Linux Administrator

Use documentation in layers rather than searching only for ready-made commands.

### Shell builtin help

```bash
help cd
help export
help printf
```

This is better than `man` for many Bash builtins.

### Manual pages

```bash
man ls
man chmod
man systemctl
```

### Manual sections

Common sections include:

```text
1  user commands
2  system calls
3  library calls
4  devices/special files
5  file formats/configuration
7  conventions/miscellaneous
8  system-administration commands
```

Examples:

```bash
man 1 passwd
man 5 passwd
man 2 open
man 5 fstab
```

The same word can refer to different concepts depending on section.

### Search manual database

```bash
apropos filesystem
man -k filesystem
whatis passwd
```

### GNU Info documentation

Some GNU tools provide deeper Info manuals:

```bash
info coreutils
info bash
```

### Package documentation

On RPM systems:

```bash
rpm -qd bash
rpm -ql bash | grep -E '/(doc|man)/'
```

### Discover command syntax safely

```bash
command --help
```

Example:

```bash
find --help
ip --help
```

Recommended troubleshooting sequence:

```text
What command/object is this?
       ↓
type / command -V
       ↓
--help / help builtin
       ↓
man
       ↓
apropos / man -k
       ↓
package documentation
       ↓
official project/vendor docs
```

---

## Added Deep Dive — File Handling Internals: Path → Dentry → Inode → Open File → Descriptor

A pathname is not the file object itself.

A simplified Linux file-open path is:

```text
Application:
open("/var/log/app.log")
         ↓
Kernel VFS path lookup
         ↓
directory entries / dentries
         ↓
inode
         ↓
filesystem-specific operations
         ↓
open-file description
         ↓
process file descriptor
```

### Conceptual objects

```text
Pathname
/var/log/app.log
       ↓
Dentry cache / directory entry
       ↓
Inode
├─ ownership
├─ permissions
├─ timestamps
├─ size
└─ data-block/extents metadata
       ↓
Open file description
├─ current file offset
├─ open flags
└─ reference to inode
       ↓
fd 3 in process
```

### Two descriptors can refer to one open file description

Shell redirection and `dup`-style behavior can cause multiple descriptors to refer to the same underlying open description.

```text
fd 1 ─┐
      ├──> open file description ──> inode
fd 2 ─┘
```

This is conceptually what happens after:

```bash
command >all.log 2>&1
```

### File offset

Programs read/write using an offset.

Conceptually:

```text
File:
ABCDEFGHIJK...

offset = 0
read 4 → ABCD
offset = 4
next read → EFGH
```

Programs can reposition using `lseek()` where supported.

### `stat`

Inspect inode-level metadata:

```bash
stat /etc/hosts
```

### `lsof`

Inspect open-file relationships:

```bash
sudo lsof /var/log/messages 2>/dev/null
sudo lsof -p "$$"
```

### Why deletion may not release blocks

```text
directory entry removed
       ↓
inode link count reaches 0
       ↓
BUT process still references open file
       ↓
data remains allocated
       ↓
last descriptor closes
       ↓
kernel can reclaim storage
```

This is why:

```bash
sudo lsof +L1
```

is important during disk-full incidents.

---

## Added Deep Dive — Process Monitoring Toolkit

`ps` and `top` are foundations, but administrators commonly combine several tools.

### Process tree

```bash
pstree -p
ps -ef --forest
```

Mental model:

```text
systemd(1)
├─ sshd
│  └─ sshd
│     └─ bash
│        └─ vim
└─ crond
```

Parent/child structure often reveals how a process was launched.

### Repeated observation with `watch`

```bash
watch -n 2 'ps -eo pid,ppid,state,%cpu,%mem,cmd --sort=-%cpu | head'
```

`watch` reruns a command periodically.

### Per-process statistics with `pidstat`

If `sysstat` is installed:

```bash
pidstat 1 5
pidstat -r 1 5
pidstat -d 1 5
```

Conceptually:

```text
pidstat
├─ CPU per process
├─ memory/page faults
└─ I/O rates
```

### Process memory maps

```bash
pmap -x <PID> | head
```

This shows virtual-memory mappings for a process.

### Open files and sockets

```bash
sudo lsof -p <PID>
ls -l /proc/<PID>/fd
```

### Thread-level view

```bash
ps -eLf | head
top -H -p <PID>
```

A process may contain many threads.

```text
Process PID 2000
├─ thread 2000
├─ thread 2001
├─ thread 2002
└─ thread 2003
```

A single hot thread can saturate one CPU core even if the whole machine appears lightly loaded.

---

## Added Deep Dive — Devices, Device Files, Major/Minor Numbers, and Drivers

Linux represents many devices through special files under `/dev`.

### Main device-file categories

```text
Block device
→ random-access storage-like devices
→ disks, partitions, logical volumes

Character device
→ byte/stream-oriented devices
→ terminals, serial interfaces, special kernel devices
```

Inspect:

```bash
ls -l /dev/null /dev/zero /dev/random /dev/sda 2>/dev/null
```

The first character indicates file type:

```text
b  block device
c  character device
-  regular file
d  directory
l  symbolic link
```

### Major and minor numbers

For device nodes, `ls -l` can show two numbers instead of ordinary byte size.

Conceptually:

```text
major number
→ identifies kernel driver/device class

minor number
→ identifies a particular device/instance handled by that driver
```

Inspect:

```bash
ls -l /dev/null
stat /dev/null
```

### Important special devices

```text
/dev/null
→ discards written data
→ reads return EOF

/dev/zero
→ supplies zero bytes

/dev/random
/dev/urandom
→ kernel random-number interfaces

/dev/tty
→ current controlling terminal in suitable contexts
```

Examples:

```bash
printf 'discard me\n' > /dev/null

head -c 16 /dev/zero | od -An -t x1
```

Do not dump unlimited `/dev/zero` or random streams to disk.

### Driver relationship

```text
Hardware
   ↓
kernel driver
   ↓
kernel device model
   ↓
sysfs `/sys`
   ↓
udev event/rules
   ↓
device node / symlink in `/dev`
```

Inspect:

```bash
lsmod | head
lspci -k
lsusb
udevadm info --query=all --name=/dev/null
```

### devtmpfs

Modern Linux commonly uses a kernel-populated `devtmpfs` mounted on `/dev`, with udev adding policy, permissions, and stable names.

Check:

```bash
findmnt /dev
```

---

## Added Deep Dive — Filesystem Internals and the Linux VFS

Linux supports many filesystem implementations through a common kernel abstraction called the **Virtual Filesystem Switch/Virtual Filesystem layer (VFS)**.

```text
Application
   ↓
open/read/write/stat
   ↓
Linux VFS
   ├─ XFS
   ├─ ext4
   ├─ tmpfs
   ├─ NFS
   └─ procfs
```

Applications use common system-call interfaces even though the underlying filesystems behave differently.

### Core conceptual filesystem structures

```text
Superblock
→ filesystem-wide metadata/state

Inode
→ metadata for one filesystem object

Dentry
→ pathname-component lookup/cache object

Data blocks/extents
→ actual file content/storage mapping
```

Simplified lookup:

```text
/path/to/file
   ↓
dentry "path"
   ↓
dentry "to"
   ↓
dentry "file"
   ↓
inode
   ↓
file data
```

### Superblock

The superblock describes important filesystem-level information, conceptually including:

- filesystem type
- block geometry
- state
- feature flags
- allocation metadata

Filesystem-specific inspection tools differ.

Examples:

```bash
xfs_info / 2>/dev/null || true
sudo tune2fs -l /dev/<ext4-device> 2>/dev/null | head
```

Only run filesystem-specific tools against the correct filesystem/device.

### Journaling

Filesystems such as XFS and ext4 use journaling mechanisms to improve metadata consistency after crashes.

Simplified concept:

```text
planned metadata update
       ↓
journal/log records enough intent/state
       ↓
filesystem update
       ↓
commit/recovery semantics
```

Journaling is **not a backup**.

### Buffered I/O and page cache

Ordinary writes often flow through the kernel page cache.

```text
Application write()
      ↓
page cache
      ↓
kernel writeback
      ↓
storage device
```

That is why a successful `write()` does not always mean physical storage has completed every persistence step.

### `sync` and `fsync` awareness

```bash
sync
```

asks the kernel to flush pending filesystem writes system-wide.

Applications can use `fsync()` for stronger durability requirements on specific files/descriptors.

Do not repeatedly run `sync` as a performance habit.

---

## Added Deep Dive — Virtual Filesystems Beyond `/proc` and `/sys`

A virtual filesystem exposes kernel/runtime state through the filesystem API rather than representing ordinary persistent disk data.

### `/proc` — procfs

```text
/proc
├─ process information
├─ CPU/memory information
├─ kernel parameters
└─ runtime statistics
```

Examples:

```bash
cat /proc/cpuinfo | head
cat /proc/meminfo | head
cat /proc/$$/status | head
```

### `/sys` — sysfs

Represents kernel device/class/subsystem information.

```bash
ls /sys/class/net
ls /sys/class/block
```

### `/dev` — commonly devtmpfs

Provides device nodes and device-related runtime names.

```bash
findmnt /dev
```

### `/run` — commonly tmpfs

Stores volatile runtime state needed after boot.

Typical examples:

```text
/run
├─ PID/runtime files
├─ sockets
├─ lock/runtime state
└─ service-manager state
```

Inspect:

```bash
findmnt /run
```

### `tmpfs`

`tmpfs` stores filesystem data in memory-backed virtual memory rather than on an ordinary persistent disk filesystem.

Example:

```bash
findmnt -t tmpfs
```

Important:

```text
tmpfs data
→ generally volatile
→ disappears across reboot/unmount
```

but memory pages can interact with swap according to kernel behavior.

### cgroup filesystem

Control groups are exposed through a filesystem-like hierarchy, commonly cgroup v2:

```bash
findmnt -t cgroup2
ls /sys/fs/cgroup | head
```

Conceptually:

```text
/sys/fs/cgroup
       ↓
cgroup hierarchy
       ↓
CPU / memory / process resource controls
```

### Why virtual filesystems matter

They make kernel state inspectable using familiar file-oriented tools:

```text
cat
ls
find
readlink
stat
```

But writing to some virtual-filesystem files can alter kernel state, so do not assume everything under `/proc` or `/sys` is read-only.

---

## Added Deep Dive — Linux Networking Applications Toolkit

The basic networking layer tells you whether the host has addresses/routes. The application layer tells you whether actual services function.

Use this progression:

```text
Link
 ↓
IP
 ↓
Route
 ↓
Neighbor
 ↓
DNS
 ↓
TCP/UDP
 ↓
TLS/application protocol
```

### DNS

```bash
getent hosts example.com
dig example.com
dig example.com A
dig example.com AAAA
```

`getent` tests the system's normal NSS resolution path, while `dig` queries DNS behavior more directly.

### HTTP/HTTPS

```bash
curl -I https://example.com
curl -v https://example.com/ -o /dev/null
```

### Download awareness

If installed:

```bash
wget --spider https://example.com/
```

`--spider` checks availability without normal downloading.

### SSH

```bash
ssh -v user@server
```

Verbose SSH can show:

```text
name resolution
TCP connection
host-key negotiation
authentication methods
session setup
```

### TCP port testing with `nc` / `ncat`

On authorized systems:

```bash
nc -vz 127.0.0.1 22
```

or, depending on distribution:

```bash
ncat -vz 127.0.0.1 22
```

This checks whether a TCP connection can be established.

Do not use port-scanning options against systems you do not own or have authorization to test.

### Listening services

```bash
ss -lntup
```

Mental model:

```text
Service installed
   ↓
process running
   ↓
socket bound
   ↓
firewall permits
   ↓
route exists
   ↓
remote client can connect
```

Every step must be valid.

---

## Added Practical Exercises for Course 102 Alignment

### Alignment Lab 1 — Wildcards

Create:

```text
file1.txt
file2.txt
file10.txt
fileA.txt
.log1
.log2
```

Predict the result **before** running:

```bash
printf '%s\n' file?.txt
printf '%s\n' file[0-9].txt
printf '%s\n' file[!A-Z].txt
printf '%s\n' *
```

Then verify.

### Alignment Lab 2 — Composite Commands

Compare:

```bash
false ; echo "runs"
false && echo "does not run"
false || echo "runs because first failed"
```

Then compare brace grouping and subshell grouping by changing `pwd` and a variable.

### Alignment Lab 3 — File Internals

1. Create a file.
2. Record inode number.
3. Create hard link.
4. Open it using `tail -f`.
5. Delete both pathnames from another shell.
6. Inspect `lsof +L1`.
7. Stop `tail`.
8. Observe storage/reference behavior.

Use only a small disposable lab file.

### Alignment Lab 4 — Device Model

Inspect:

```bash
ls -l /dev/null /dev/zero /dev/random
stat /dev/null
lsmod | head
lspci -k
findmnt /dev
```

Explain block vs character devices and major/minor numbers.

### Alignment Lab 5 — VFS and Virtual Filesystems

Run:

```bash
findmnt -t proc,sysfs,tmpfs,devtmpfs,cgroup2
```

For every mounted virtual filesystem explain:

```text
What state does it expose?
Is it persistent?
Which kernel/userspace component uses it?
What risk exists if it is modified?
```

### Alignment Lab 6 — Process Monitoring

Start one harmless workload in the lab and inspect it with:

```bash
ps
pstree
top
watch
pidstat
lsof
pmap
```

Use only tools installed on your VM.

### Alignment Lab 7 — Networking Applications

For your own lab server:

```bash
ip route get <server-ip>
getent hosts <server-name>
nc -vz <server-ip> 22
ssh -v user@<server-name>
```

Explain exactly which networking layer each command tests.



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Linux Orientation

1. Install a RHEL-compatible VM.
2. Create a non-root administrative user.
3. Identify distribution and kernel version.
4. Inspect hostname, CPU, RAM, block devices, and IP addresses.
5. Save the results into `system-baseline.txt`.

### Lab 2 — Filesystem Navigation

1. Create `/home/<user>/linux-labs`.
2. Create nested directories for `files`, `logs`, `scripts`, and `backup`.
3. Practice absolute and relative navigation.
4. Create hidden files.
5. Use `tree` if available or `find` to display the structure.

### Lab 3 — Files and Links

1. Create several files.
2. Copy, move, and rename them.
3. Create one hard link and one symbolic link.
4. Compare inode numbers.
5. Delete the original target and observe hard-link vs symlink behavior.

### Lab 4 — Text Processing

1. Copy `/etc/passwd` to your lab directory.
2. Extract usernames with `cut`.
3. Filter Bash users with `grep`.
4. Sort usernames.
5. Count them with `wc`.
6. Build a pipeline that produces a clean report.

### Lab 5 — Users and Groups

1. Create group `linuxlab`.
2. Create users `student1` and `student2`.
3. Add both to the group.
4. Create a shared directory.
5. Set ownership and permissions so group members can collaborate.
6. Test access from both users.

### Lab 6 — Permissions

1. Create files with permissions 600, 640, 644, 750, and 755.
2. Explain each mode.
3. Change umask and create new files/directories.
4. Inspect the result.
5. Create a sticky-bit shared directory in the lab and test deletion behavior.

### Lab 7 — Process Management

1. Start several `sleep` processes.
2. Find them with `ps` and `pgrep`.
3. Move a foreground job to background.
4. Send SIGTERM to one.
5. Send SIGKILL to another.
6. Explain the difference.

### Lab 8 — systemd

1. Inspect `sshd` or another safe service.
2. Stop/start/restart it in the VM.
3. Enable/disable it.
4. Inspect its journal.
5. Create a simple demo service that runs a script.

### Lab 9 — Package Management

1. Search for a package.
2. Inspect package information.
3. Install it.
4. List installed files.
5. Identify which package owns one executable.
6. Remove the package.

### Lab 10 — Storage Observation

1. Inspect disks with `lsblk -f`.
2. Inspect mounted filesystems.
3. Compare `df` and `du`.
4. Inspect swap.
5. Do not repartition the system disk in this essentials lab.

### Lab 11 — Linux Networking

1. Record IP addresses.
2. Record routes.
3. Identify default gateway.
4. Inspect neighbor table.
5. Resolve DNS.
6. Inspect listening sockets.
7. Use `curl` to test an HTTP/HTTPS endpoint.

### Lab 12 — SSH

1. Create a second VM or use an approved lab host.
2. Generate an Ed25519 key.
3. Copy the public key.
4. Connect by SSH.
5. Create an SSH config alias.
6. Inspect SSH server logs.

### Lab 13 — Logs

1. Use `journalctl -b`.
2. Filter by priority.
3. Filter one service.
4. Follow logs live.
5. Trigger a safe event such as SSH login and locate it.

### Lab 14 — Scheduling

1. Create a script that writes date/hostname to a file.
2. Schedule it with cron.
3. Verify output.
4. Remove the cron entry after the lab.

### Lab 15 — Health Script

1. Write a Bash script that reports hostname, uptime, memory, disk, IP addresses, default route, and failed services.
2. Add timestamped output.
3. Redirect the report to a file.
4. Handle missing commands defensively.

### Lab 16 — Troubleshooting Challenge

1. Create five safe faults in a disposable VM or lab copy: stopped service, wrong permission, full temporary test filesystem or quota-like simulation, bad DNS entry, removed route.
2. Troubleshoot one at a time.
3. Write symptom, evidence, cause, fix, verification.


## Enhanced Hands-on Lab Sequence

### Enhanced Lab 1 — System Call Trace

Use `strace` on `echo`, `cat`, and `ls` in your disposable VM. Identify `openat`, `read`, `write`, and `execve` calls.

### Enhanced Lab 2 — Builtin vs Executable

Use `type -a` on 20 commands and classify builtin, alias, function, or executable.

### Enhanced Lab 3 — Exit Status

Create a table of exit statuses for `true`, `false`, `grep` match/no-match, missing file, and a successful command.

### Enhanced Lab 4 — Quoting

Create filenames and variable values containing spaces; compare quoted vs unquoted expansions.

### Enhanced Lab 5 — Globs vs Regex

Solve 20 matching exercises using shell globs and `grep -E` separately.

### Enhanced Lab 6 — Brace Expansion

Generate a lab directory tree with brace expansion and verify before creation.

### Enhanced Lab 7 — Command Substitution

Build a timestamped report filename from `hostname` and `date`.

### Enhanced Lab 8 — Environment Inheritance

Demonstrate shell variable vs exported environment variable using a child Bash process.

### Enhanced Lab 9 — PATH Audit

Print PATH one directory per line and identify any user-writable entries.

### Enhanced Lab 10 — File Descriptors

Inspect `/proc/$$/fd`, then redirect stdout/stderr and observe descriptor targets.

### Enhanced Lab 11 — Redirection Order

Run a command producing stdout and stderr and compare `>file 2>&1` with `2>&1 >file`.

### Enhanced Lab 12 — Here Document

Generate a safe local configuration file using a quoted here-doc.

### Enhanced Lab 13 — sudo + tee

In your lab, write one controlled root-owned test file using `sudo tee` and explain why direct redirection behaves differently.

### Enhanced Lab 14 — Inodes

Create, rename, and hard-link a file while recording inode and link count.

### Enhanced Lab 15 — Deleted-Open File

Create a safe small file held open by a process, delete the name, observe with `lsof +L1`, then release it.

### Enhanced Lab 16 — Inode Capacity

Inspect `df -i` on every mounted filesystem and explain the result.

### Enhanced Lab 17 — Mount Hiding

Use a disposable mount/tmpfs if available to demonstrate a mount hiding existing directory contents.

### Enhanced Lab 18 — Storage Layers

Draw block device → partition → filesystem → mount point for your VM.

### Enhanced Lab 19 — UUID and Labels

Map every mounted filesystem to source, UUID, type, and target.

### Enhanced Lab 20 — fstab Reading

Explain each field of every non-comment `/etc/fstab` line without modifying production mounts.

### Enhanced Lab 21 — Mount Options

Inspect `findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS` and explain five options.

### Enhanced Lab 22 — Symlink Resolution

Create relative and absolute symlinks, move parent directories, and document behavior.

### Enhanced Lab 23 — Directory Permissions

Build a matrix showing effects of directory r/w/x combinations.

### Enhanced Lab 24 — Deletion Permissions

Demonstrate that a read-only file can be deleted when parent directory permissions allow it.

### Enhanced Lab 25 — ACL

Grant one user access to a file with `setfacl` without changing the owning group.

### Enhanced Lab 26 — Default ACL

Build a shared directory where new files inherit a team ACL.

### Enhanced Lab 27 — SGID Team Directory

Create a group-collaboration directory using SGID and a controlled umask.

### Enhanced Lab 28 — Sticky Directory

Create a shared sticky directory and test cross-user deletion behavior.

### Enhanced Lab 29 — SUID Inspection

List SUID/SGID files on the VM and explain why they deserve security review; do not create new SUID binaries.

### Enhanced Lab 30 — Capabilities

Inspect file capabilities with `getcap` and map each found capability to its purpose.

### Enhanced Lab 31 — sudo Policy

Use `sudo -l` and create a lab-only command-specific sudoers rule with `visudo` if permitted.

### Enhanced Lab 32 — NSS/getent

Compare `/etc/passwd` output to `getent passwd` and explain why results may differ.

### Enhanced Lab 33 — UID/GID

Create a user/file, inspect numeric ownership, then remove the user and observe orphaned ownership in the lab.

### Enhanced Lab 34 — Password Aging

Inspect account aging using `chage -l` and document each field.

### Enhanced Lab 35 — Process Tree

Run nested shells/processes and inspect PID/PPID using `ps --forest`.

### Enhanced Lab 36 — Process States

Identify R/S/D/T/Z meanings and observe at least S and T safely.

### Enhanced Lab 37 — Zombie Demonstration

Use a small safe lab program/script if available to create a short-lived zombie and explain parent reaping.

### Enhanced Lab 38 — Open Files

Use `lsof` to map one process to files and one listening socket.

### Enhanced Lab 39 — Process Environment

Inspect a test process environment without storing secrets in the exercise.

### Enhanced Lab 40 — Signals

Test SIGTERM, SIGHUP on a safe lab process that handles it, and SIGKILL last.

### Enhanced Lab 41 — Load

Record load average and CPU count under idle and a brief safe CPU test.

### Enhanced Lab 42 — CPU Categories

Use `vmstat`/`top` to distinguish user/system/idle/iowait fields.

### Enhanced Lab 43 — Memory

Explain `free`, `available`, cache, and swap from the VM's output.

### Enhanced Lab 44 — OOM Evidence

Search kernel logs for OOM events and document what you would collect if one existed.

### Enhanced Lab 45 — Cgroups

Use `systemd-cgls` to locate sshd or another service in the cgroup tree.

### Enhanced Lab 46 — Namespaces

Inspect namespace links under `/proc/$$/ns/` and explain each name at a high level.

### Enhanced Lab 47 — Unit Types

List service/socket/timer/mount units and give one example use for each.

### Enhanced Lab 48 — Active vs Enabled

Find one active+enabled, one inactive+enabled, and one active+disabled unit if available.

### Enhanced Lab 49 — systemd Dependencies

Use `systemctl list-dependencies` and distinguish ordering from requirement.

### Enhanced Lab 50 — Drop-In Override

Create a safe override for a demo service using `systemctl edit`.

### Enhanced Lab 51 — Timer

Create a demo systemd timer that writes a timestamp to a lab file.

### Enhanced Lab 52 — Journal Metadata

Filter the journal by unit, boot, PID, priority, and time range.

### Enhanced Lab 53 — Journal Persistence

Check whether your VM keeps previous-boot journal data.

### Enhanced Lab 54 — Logrotate

Read one logrotate policy and explain rotation, retention, compression, and postrotate behavior.

### Enhanced Lab 55 — RPM Ownership

Pick ten executables and find their owning packages.

### Enhanced Lab 56 — RPM Verification

Verify a package, then interpret configuration-file changes carefully.

### Enhanced Lab 57 — DNF History

Inspect recent package transactions and identify install/update/remove actions.

### Enhanced Lab 58 — Repository Trust

List enabled repositories and package signing keys; document trust boundaries.

### Enhanced Lab 59 — GPT/MBR

Inspect disk partition-table type using `lsblk`, `fdisk -l`, or `parted -l` without modifying disks.

### Enhanced Lab 60 — LVM Map

If your VM uses LVM, map PV→VG→LV→filesystem. Otherwise draw the model.

### Enhanced Lab 61 — Filesystem Safety

Write a pre-flight checklist that must be satisfied before any `mkfs` command.

### Enhanced Lab 62 — XFS/ext4

Compare filesystem type and resize implications for the filesystems present in your VM.

### Enhanced Lab 63 — df vs du

Compare `df` and `du` for `/var` and explain why they can differ.

### Enhanced Lab 64 — I/O Observation

Use `vmstat` and optionally `iostat` during a small file copy and interpret activity.

### Enhanced Lab 65 — Kernel Modules

Inspect loaded modules and use `modinfo` on one module.

### Enhanced Lab 66 — sysctl

Inspect ten kernel settings and identify which are networking/security/performance related; do not change them yet.

### Enhanced Lab 67 — Runtime vs Persistent Network

Compare `ip` runtime state with NetworkManager connection profiles.

### Enhanced Lab 68 — Link State

Identify admin state, carrier state, addresses, and NetworkManager state for each interface.

### Enhanced Lab 69 — Route Lookup

Use `ip route get` for local subnet, default-route destination, and loopback.

### Enhanced Lab 70 — Neighbor States

Inspect neighbor table before/after pinging the gateway.

### Enhanced Lab 71 — Resolver Path

Compare `/etc/hosts`, `getent hosts`, and `dig` for a test name.

### Enhanced Lab 72 — Socket Binding

Run a local HTTP server bound to 127.0.0.1, then 0.0.0.0, and compare `ss` output.

### Enhanced Lab 73 — TCP States

Make a local SSH/HTTP connection and identify LISTEN/ESTAB/TIME-WAIT states.

### Enhanced Lab 74 — curl Layer Test

Use `curl -v` against a local service and explain DNS/connect/TLS/HTTP stages where applicable.

### Enhanced Lab 75 — SSH Host Key

Record and verify your lab server host-key fingerprint through the VM console before first SSH login.

### Enhanced Lab 76 — SSH User Key

Generate an Ed25519 key with a passphrase and configure lab access.

### Enhanced Lab 77 — ssh-agent

Load a test key into an agent and inspect it using `ssh-add -l`.

### Enhanced Lab 78 — rsync Dry Run

Create a local source/destination tree and use `rsync --dry-run` before synchronizing.

### Enhanced Lab 79 — SSH Hardening

Use `sshd -T` to inspect effective settings; make only reversible lab changes.

### Enhanced Lab 80 — firewalld Zones

Map each interface to its active zone and list allowed services.

### Enhanced Lab 81 — Firewall Runtime/Permanent

Add a temporary lab service rule, verify, remove it, then explain permanent behavior.

### Enhanced Lab 82 — SELinux Context

Compare process and file contexts for sshd or a web service.

### Enhanced Lab 83 — SELinux Label Repair

Create a mislabeled lab copy and use `restorecon` where safe/appropriate.

### Enhanced Lab 84 — SELinux Evidence

Search for recent AVC denials and explain the evidence fields if present.

### Enhanced Lab 85 — Boot Map

Create a diagram of your VM's boot chain from firmware to systemd target.

### Enhanced Lab 86 — initramfs

Inspect initramfs contents using `lsinitrd` if available.

### Enhanced Lab 87 — Kernel Command Line

Explain every parameter currently present in `/proc/cmdline`.

### Enhanced Lab 88 — Recovery Modes

Document how you would reach rescue/emergency mode from an out-of-band console without actually disrupting the VM.

### Enhanced Lab 89 — /proc

Inspect status, fd, maps, cmdline, and environment of your shell process.

### Enhanced Lab 90 — /sys

Trace one network interface and one block device through sysfs.

### Enhanced Lab 91 — udev

Use `udevadm info` on one block/network device and identify persistent properties.

### Enhanced Lab 92 — Shell Startup

Determine which Bash startup files run for login vs interactive shells in your VM.

### Enhanced Lab 93 — Cron Environment

Create a cron job that records its environment, compare to your interactive shell, then remove it.

### Enhanced Lab 94 — Bash Function

Write reusable `check_command`, `log`, and `fail` functions.

### Enhanced Lab 95 — Bash Arrays

Build a health-check list using quoted array iteration.

### Enhanced Lab 96 — Conditional Syntax

Rewrite five `[ ... ]` tests using `[[ ... ]]` and explain portability.

### Enhanced Lab 97 — pipefail

Demonstrate how an earlier pipeline failure can be hidden without `pipefail`.

### Enhanced Lab 98 — mktemp + trap

Create a safe temp workspace that always cleans up.

### Enhanced Lab 99 — find/xargs Safety

Process filenames containing spaces with `-print0`/`-0`.

### Enhanced Lab 100 — sed/awk

Parse `/etc/passwd` into a username/UID report using `awk`; transform a lab config with `sed`.

### Enhanced Lab 101 — Checksums

Hash a configuration copy, modify it, and verify the digest changes.

### Enhanced Lab 102 — Backup vs Archive

Create an archive, copy it to independent lab storage if available, and perform a restore test.

### Enhanced Lab 103 — Permission Runbook

Diagnose five permission-denied scenarios using `id`, `namei`, `getfacl`, `findmnt`, and SELinux evidence.

### Enhanced Lab 104 — Service Runbook

Break a demo service safely and recover using package/config/systemd/journal/socket/firewall checks.

### Enhanced Lab 105 — Disk Runbook

Create a small disposable filesystem or file-backed loop lab and diagnose byte/inode/open-file pressure.

### Enhanced Lab 106 — CPU Runbook

Create a controlled short CPU load and collect `uptime`, `top`, `ps`, `vmstat`.

### Enhanced Lab 107 — Memory Runbook

Analyze host memory, swap, top processes, and cgroup service limits.

### Enhanced Lab 108 — Network Runbook

Break one safe network setting in a clone/snapshot and follow link→IP→route→neighbor→DNS→socket→app.

### Enhanced Lab 109 — Baseline

Generate a before-change system baseline in Markdown.

### Enhanced Lab 110 — Security Layer Map

For SSH access, map firewall→socket→process identity→DAC→SELinux→application authentication.

### Enhanced Lab 111 — Container Bridge

Inspect namespaces/cgroups on the host and explain how they become container primitives.

### Enhanced Lab 112 — Capstone

Complete the expanded Linux Administration Server capstone.


## 6. Mini Project

# Mini Project — Build and Baseline a Linux Administration Server

Create one RHEL-compatible VM called:

```text
linux-admin01.lab.example
```

## Requirements

### Identity

- Set hostname.
- Create a non-root administrator.
- Create an operations group.
- Document UID/GID.

### Filesystem

Create:

```text
/opt/linux-lab/
/opt/linux-lab/scripts/
/opt/linux-lab/reports/
/opt/linux-lab/archive/
```

Assign controlled ownership and permissions.

### Packages

Install:

- one troubleshooting tool,
- one text utility,
- one web/client utility such as `curl` if not present.

Record:

```bash
rpm -q <package>
```

### Networking

Document:

- IPv4 address
- IPv6 address if available
- default gateway
- DNS servers
- routes
- listening sockets

### SSH

- enable SSH,
- use key-based authentication,
- create a client SSH alias,
- validate the configuration before restarting sshd.

### Logging

Create a troubleshooting checklist using:

```bash
systemctl status
journalctl
ss
ip
df
free
ps
```

### Automation

Create:

```text
/opt/linux-lab/scripts/daily-health.sh
```

The script must report:

- hostname
- date
- uptime
- CPU/load
- memory
- root filesystem usage
- top 5 processes by CPU
- top 5 processes by memory
- IP addresses
- default route
- DNS lookup test
- failed systemd services

Save reports to:

```text
/opt/linux-lab/reports/
```

### Scheduling

Schedule the report to run daily in the lab.

### Backup

Archive reports:

```bash
tar -czf reports-$(date +%F).tar.gz reports/
```

### Troubleshooting Tests

Break and fix:

1. Stop SSH.
2. Remove read permission from a test config file.
3. Create a bad hostname entry in a lab file.
4. Create a DNS resolution failure.
5. Add a wrong test route and remove it.
6. Fill a small disposable test filesystem or directory quota simulation if available.

For every incident:

```text
Symptom:
Commands used:
Evidence:
Root cause:
Fix:
Verification:
```

## Deliverables

```text
README.md
SYSTEM_BASELINE.md
USERS_AND_GROUPS.md
PERMISSIONS.md
NETWORK.md
SERVICES.md
TROUBLESHOOTING.md
daily-health.sh
```

## Expanded Capstone — Linux Administration, Security, and Troubleshooting Baseline

Extend the original `linux-admin01.lab.example` project.

### Target Architecture

```text
Administrator Workstation
        |
        | SSH key
        v
linux-admin01.lab.example
├── systemd
├── journald
├── NetworkManager
├── firewalld
├── SELinux
├── operations users/groups
├── /opt/linux-lab
├── scheduled health reporting
└── protected backup/report directory
```

### Directory Layout

```text
/opt/linux-lab/
├── scripts/
│   ├── daily-health.sh
│   ├── collect-network.sh
│   └── collect-storage.sh
├── reports/
├── archive/
├── config/
└── tmp/
```

Use ownership, SGID/default ACLs, and a restrictive umask rather than `chmod 777`.

### Identity

Create:

```text
group: linuxops
users: admin1, operator1
```

Design:

```text
admin1
→ sudo rights required for administration

operator1
→ read system reports
→ no unrestricted root shell
```

Document:

```text
UID
primary GID
supplementary groups
sudo policy
password/key policy
```

### SSH

Requirements:

```text
Ed25519 user key
server host-key fingerprint documented
client SSH alias
sshd config validated with sshd -t
effective config reviewed with sshd -T
root-login policy documented
password-auth policy documented
firewalld scope documented
```

Keep a console or existing SSH session open during any lab changes.

### Filesystem / Permissions

Implement:

```text
/opt/linux-lab/scripts
owner root
group linuxops
mode appropriate for controlled script editing/execution

/opt/linux-lab/reports
group linuxops
SGID/default ACL
operators can read reports

/opt/linux-lab/archive
restricted write access
```

Document:
- mode
- ACL
- SELinux context
- mount options affecting the path

### Storage Report

Create a script that captures:

```bash
lsblk -f
findmnt
df -hT
df -i
swapon --show
```

If the VM uses LVM, also include:

```text
PV → VG → LV → filesystem → mount point
```

Do not repartition or format the system disk.

### Network Report

Collect:

```bash
ip -br link
ip -br address
ip route
ip -6 route
ip neigh
nmcli device status
nmcli connection show --active
ss -tulpen
getent hosts example.com
```

Explain:
- runtime vs persistent state
- loopback-only vs wildcard socket binding
- default route
- resolver path

### Security Baseline

Document:

```text
sudo policy
firewalld active zone
open/listening sockets
SELinux mode
important SELinux contexts
SUID/SGID inventory
file capabilities inventory
SSH effective settings
enabled repositories
```

Do not weaken SELinux or firewall controls to make the project easier.

### systemd Service

Create a small safe health collector service:

```text
/etc/systemd/system/linux-health.service
```

Use:
- non-root service account if practical
- explicit executable path
- clear exit status
- journald logging

Then create:

```text
linux-health.timer
```

to schedule execution.

### Health Script

`daily-health.sh` must report:

```text
Timestamp
Distribution
Kernel
Hostname
Uptime
Load average
CPU count
Memory
Swap
Top CPU processes
Top memory processes
Filesystem capacity
Inode capacity
Deleted-open files
Block devices
Mounts
IP addresses
Routes
Neighbor table
DNS test
Listening sockets
Failed systemd units
Recent high-priority journal events
firewalld active zone
SELinux state
```

Use functions and quoted variables.

Recommended skeleton:

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

readonly REPORT_DIR="/opt/linux-lab/reports"

log() {
    printf '%s %s\n' "$(date '+%F %T')" "$*"
}

require_cmd() {
    command -v "$1" >/dev/null 2>&1 || {
        printf 'Missing command: %s\n' "$1" >&2
        return 1
    }
}
```

Do not use `set -e` as a substitute for deliberate error handling.

### Archive and Restore Test

Create an archive of reports, then perform a restore test into a different directory.

Document:

```text
archive creation
checksum
copy/backup location
restore
verification
```

### Troubleshooting Fault Matrix

In a disposable VM/snapshot, inject at least 15 safe faults:

```text
1. stopped service
2. disabled service
3. invalid demo-service configuration
4. service listening only on 127.0.0.1
5. firewalld service not allowed
6. wrong file owner
7. missing directory execute permission
8. ACL mask blocks expected access
9. wrong SELinux context on a lab file
10. full small disposable filesystem
11. inode exhaustion in a tiny disposable lab filesystem if practical
12. deleted-open lab file
13. missing default route in a disposable network clone
14. wrong DNS resolver
15. stale/wrong /etc/hosts lab entry
16. cron PATH problem
17. expired/locked test account
18. SSH authorized_keys permission problem
19. wrong systemd unit dependency
20. bad fstab entry tested safely with `mount -a`, not reboot
```

For every incident, record:

```text
Symptom
Scope
Recent change
Evidence
Subsystem/layer
Hypothesis
Command used to test hypothesis
Root cause
Minimal fix
Verification
Preventive control
```

### Deliverables

```text
README.md
SYSTEM_ARCHITECTURE.md
SYSTEM_BASELINE.md
IDENTITY_AND_SUDO.md
FILESYSTEM_AND_PERMISSIONS.md
ACL_AND_SPECIAL_BITS.md
STORAGE.md
NETWORK.md
SSH.md
SYSTEMD.md
LOGGING.md
SECURITY_BASELINE.md
PACKAGE_BASELINE.md
TROUBLESHOOTING_RUNBOOK.md
FAULT_INJECTION_REPORT.md
BACKUP_RESTORE_TEST.md
daily-health.sh
collect-network.sh
collect-storage.sh
linux-health.service
linux-health.timer
```


## 7. Recommended Resources

Prioritize official or high-quality references:

- Red Hat Enterprise Linux documentation.
- Red Hat product documentation for system administration.
- GNU Bash Reference Manual.
- GNU Coreutils documentation.
- `man` pages on the system.
- systemd official/manual documentation available through `man systemd`, `man systemctl`, and unit-specific pages.
- OpenSSH manual pages.
- NetworkManager documentation.
- Linux kernel documentation for deeper `/proc` and `/sys` topics.

The most important resource on a Linux system is often:

```bash
man <command>
```
## 8. Certification Relevance

Linux Essentials prepares you for later Red Hat administration work but is not a substitute for RHCSA-level training.

The skills here support:

- RHCSA
- Linux server administration
- Docker
- Kubernetes
- Ansible
- OpenShift
- DevOps
- cloud engineering
- cybersecurity
- SOC and incident response
- penetration-testing lab environments

If you cannot confidently use Linux from the command line, later infrastructure and security phases will be significantly harder.
## 9. Common Mistakes & Best Practices

- **Mistake:** Running every command with sudo.
  - **Best practice:** Use normal-user privileges until elevation is actually required.
- **Mistake:** Memorizing commands without reading output.
  - **Best practice:** Explain what each field means and verify the effect.
- **Mistake:** Using `chmod 777` to fix permission problems.
  - **Best practice:** Determine the correct owner, group, and minimum permissions.
- **Mistake:** Deleting files before verifying the working directory.
  - **Best practice:** Run `pwd` and `ls` before destructive operations.
- **Mistake:** Editing system config without making a backup.
  - **Best practice:** Copy or version important configuration before changes.
- **Mistake:** Restarting services repeatedly instead of reading logs.
  - **Best practice:** Use `systemctl status` and `journalctl` first.
- **Mistake:** Using SIGKILL as the first choice.
  - **Best practice:** Try graceful termination with SIGTERM.
- **Mistake:** Assuming low free memory means Linux is out of memory.
  - **Best practice:** Inspect available memory, cache behavior, swap, and OOM evidence.
- **Mistake:** Assuming a full disk always means large files.
  - **Best practice:** Check both `df -h` and `df -i`, plus deleted-open files.
- **Mistake:** Disabling SELinux when something fails.
  - **Best practice:** Investigate denials and correct policy/labels/configuration.
- **Mistake:** Using password SSH only forever.
  - **Best practice:** Learn key-based authentication and protect private keys.
- **Mistake:** Changing SSH remotely without validation.
  - **Best practice:** Run `sshd -t` and keep an existing session open.
- **Mistake:** Confusing package install with service start.
  - **Best practice:** Installing software and starting/enabling a service are separate operations.
- **Mistake:** Ignoring exit status in scripts.
  - **Best practice:** Check command success and fail clearly.
- **Mistake:** Copying commands from the Internet without understanding paths/devices.
  - **Best practice:** Verify commands against your distribution and lab state.


### Additional Common Mistakes & Best Practices

- **Mistake:** Treating every command as an external executable.
  - **Best practice:** Use `type -a` to identify aliases, functions, builtins, and executables.
- **Mistake:** Ignoring exit status.
  - **Best practice:** Make success/failure explicit in scripts and operations.
- **Mistake:** Leaving variable expansions unquoted.
  - **Best practice:** Quote unless splitting/globbing is intentional.
- **Mistake:** Confusing shell globs and regular expressions.
  - **Best practice:** Know which matching language each tool uses.
- **Mistake:** Assuming deleted files always free space immediately.
  - **Best practice:** Check `lsof +L1`.
- **Mistake:** Looking only at `df -h`.
  - **Best practice:** Also inspect `df -i`, `du`, and mount topology.
- **Mistake:** Editing vendor systemd units directly.
  - **Best practice:** Use drop-in overrides under `/etc`.
- **Mistake:** Treating enabled as running.
  - **Best practice:** Check both `is-active` and `is-enabled`.
- **Mistake:** Restarting before reading logs.
  - **Best practice:** Capture state/evidence first.
- **Mistake:** Adding random repositories to get one package.
  - **Best practice:** Treat repositories as supply-chain trust decisions.
- **Mistake:** Running `mkfs` based only on a guessed device name.
  - **Best practice:** Verify with `lsblk`, `blkid`, and `findmnt`.
- **Mistake:** Treating low `free` memory as failure.
  - **Best practice:** inspect `available`, cache, swap, OOM evidence, and workload.
- **Mistake:** Assuming a service listening on 127.0.0.1 is remotely reachable.
  - **Best practice:** inspect socket bind addresses.
- **Mistake:** Treating `dig` as the entire application resolver path.
  - **Best practice:** compare `getent`, NSS, hosts, and DNS.
- **Mistake:** Deleting SSH `known_hosts` entries without verification.
  - **Best practice:** validate the changed host key fingerprint.
- **Mistake:** Disabling firewall/SELinux during troubleshooting and forgetting to restore it.
  - **Best practice:** identify and fix the actual policy mismatch.
- **Mistake:** Using cron without explicit paths/environment.
  - **Best practice:** assume a minimal environment.
- **Mistake:** Parsing filenames from `ls`.
  - **Best practice:** use `find -print0`, arrays, and safe argument handling.
- **Mistake:** Calling a same-disk tar archive a backup.
  - **Best practice:** include independent storage and restore testing.
- **Mistake:** Automating before validating.
  - **Best practice:** collect baseline, render/diff changes, verify assertions, and keep rollback.


## 10. Self-Assessment Questions (with short answers)

### Q1. What is Linux technically?

**Short answer:** The operating-system kernel.

### Q2. What is a Linux distribution?

**Short answer:** A packaged operating system combining the Linux kernel with utilities, libraries, package management, configuration, and applications.

### Q3. What is kernel space?

**Short answer:** Privileged execution context where the kernel operates.

### Q4. What is user space?

**Short answer:** Where ordinary applications and system services run.

### Q5. What command shows the current directory?

**Short answer:** `pwd`.

### Q6. What is an absolute path?

**Short answer:** A path beginning from `/`.

### Q7. What does `~` usually represent?

**Short answer:** The current user's home directory.

### Q8. What is `/etc` primarily for?

**Short answer:** System-wide configuration.

### Q9. What is `/var` primarily for?

**Short answer:** Variable data such as logs and application state.

### Q10. What is `/proc`?

**Short answer:** A virtual filesystem exposing process and kernel information.

### Q11. What is an inode?

**Short answer:** Filesystem metadata object representing a file, separate from its directory name.

### Q12. Difference between hard and symbolic links?

**Short answer:** Hard links reference the same inode; symlinks store a path to another target.

### Q13. What does `>` do?

**Short answer:** Redirects stdout and overwrites the target file.

### Q14. What does `>>` do?

**Short answer:** Appends stdout.

### Q15. What does `2>` redirect?

**Short answer:** Standard error.

### Q16. What does a pipe do?

**Short answer:** Connects one command's stdout to another command's stdin.

### Q17. What is UID 0?

**Short answer:** Root.

### Q18. What does `id` show?

**Short answer:** User ID, primary group, and supplementary groups.

### Q19. What does permission 750 mean?

**Short answer:** Owner rwx, group r-x, others no permissions.

### Q20. What does `umask` do?

**Short answer:** Removes permission bits from default file/directory creation modes.

### Q21. What does the sticky bit do on a shared directory?

**Short answer:** Restricts deletion/rename so users cannot remove others' files simply because the directory is writable.

### Q22. What is a PID?

**Short answer:** Process identifier.

### Q23. Why prefer SIGTERM before SIGKILL?

**Short answer:** SIGTERM allows graceful cleanup; SIGKILL cannot be handled.

### Q24. What is systemd?

**Short answer:** The service/system manager and PID 1 on many modern Linux systems.

### Q25. Difference between `systemctl start` and `enable`?

**Short answer:** Start affects current state; enable configures boot-time activation.

### Q26. What is RPM?

**Short answer:** The package format/database foundation used by Red Hat-family distributions.

### Q27. What is DNF?

**Short answer:** A higher-level package manager for RPM-based systems.

### Q28. What does `lsblk` show?

**Short answer:** Block devices and their hierarchy.

### Q29. What does `df` show?

**Short answer:** Filesystem usage/free space.

### Q30. What does `du` show?

**Short answer:** Disk usage by files/directories.

### Q31. What does `free -h` show?

**Short answer:** Memory and swap usage in human-readable format.

### Q32. What command displays Linux routes?

**Short answer:** `ip route`.

### Q33. What command displays neighbor/ARP/NDP cache?

**Short answer:** `ip neigh`.

### Q34. What command displays listening sockets?

**Short answer:** `ss -tulpen`.

### Q35. What does `dig` test?

**Short answer:** DNS resolution/records.

### Q36. What is SSH?

**Short answer:** Encrypted remote shell and transport protocol.

### Q37. What is the private SSH key?

**Short answer:** The secret half of a key pair and must be protected.

### Q38. What does `journalctl -u sshd` show?

**Short answer:** Journal entries for the sshd service.

### Q39. What is cron used for?

**Short answer:** Scheduling recurring commands/jobs.

### Q40. What is the best Linux troubleshooting principle?

**Short answer:** Collect evidence, isolate the component/layer, change one thing, verify, and document.


## Enhanced Self-Assessment Questions

### Enhanced Q1. What is a system call?

**Short answer:** A controlled request from user space to the kernel for an operating-system service.

### Enhanced Q2. Why must `cd` be a shell builtin?

**Short answer:** A child process cannot change the parent shell's working directory.

### Enhanced Q3. What does `type -a` show?

**Short answer:** All known command interpretations such as aliases, functions, builtins, and executables.

### Enhanced Q4. What does exit status 0 conventionally mean?

**Short answer:** Success.

### Enhanced Q5. Why quote `"$var"`?

**Short answer:** To preserve the value as one argument and prevent unintended splitting/globbing.

### Enhanced Q6. Globbing vs regex?

**Short answer:** Globbing is shell pathname matching; regex is a separate pattern language used by tools such as grep.

### Enhanced Q7. What does `export` do?

**Short answer:** Marks a shell variable for inheritance by child processes.

### Enhanced Q8. What is PATH?

**Short answer:** Ordered list of directories searched for commands.

### Enhanced Q9. Why can an unsafe PATH be dangerous?

**Short answer:** An untrusted executable can be selected before the intended system command.

### Enhanced Q10. What is a file descriptor?

**Short answer:** An integer handle a process uses for an open file/socket/pipe/device.

### Enhanced Q11. Why does redirection order matter?

**Short answer:** File descriptors are reassigned left-to-right.

### Enhanced Q12. What does a here-document provide?

**Short answer:** Multiline data to a command's standard input.

### Enhanced Q13. Why may `sudo echo x > /root/file` fail?

**Short answer:** The current shell performs `>` before sudo executes echo.

### Enhanced Q14. What maps a filename to inode?

**Short answer:** A directory entry.

### Enhanced Q15. Why can deleted data still use disk space?

**Short answer:** An open file descriptor can keep the inode/data referenced.

### Enhanced Q16. What does `df -i` measure?

**Short answer:** Filesystem inode usage.

### Enhanced Q17. What happens to underlying files when another filesystem is mounted over their directory?

**Short answer:** They become hidden until the mount is removed.

### Enhanced Q18. Block device vs filesystem?

**Short answer:** Block device is storage; filesystem is the structure organizing files on storage.

### Enhanced Q19. Why use filesystem UUID in fstab?

**Short answer:** It is usually more stable than discovery-dependent device names.

### Enhanced Q20. What does mount `noexec` affect?

**Short answer:** Execution from that mounted filesystem.

### Enhanced Q21. When is file storage freed after unlink?

**Short answer:** When link count is zero and no process keeps it open.

### Enhanced Q22. Relative symlink target is interpreted relative to what?

**Short answer:** The directory containing the symlink.

### Enhanced Q23. Directory execute permission means?

**Short answer:** Traverse/search the directory.

### Enhanced Q24. What controls deleting an ordinary file?

**Short answer:** Primarily write+execute permission on its parent directory, subject to sticky/ACL/SELinux rules.

### Enhanced Q25. What is a POSIX ACL?

**Short answer:** Extended per-user/per-group file permission entries beyond owner/group/other.

### Enhanced Q26. Default ACL purpose?

**Short answer:** Define ACLs inherited by newly created children.

### Enhanced Q27. SGID on a directory?

**Short answer:** New entries inherit the directory's group.

### Enhanced Q28. Sticky bit on a directory?

**Short answer:** Restricts deletion/rename of others' entries in shared writable directories.

### Enhanced Q29. What is SUID?

**Short answer:** Executable can run with effective UID of file owner.

### Enhanced Q30. What are Linux capabilities?

**Short answer:** Fine-grained kernel privileges split from all-or-nothing root.

### Enhanced Q31. Why use visudo?

**Short answer:** Validate sudoers syntax before installing policy.

### Enhanced Q32. Why use `getent passwd`?

**Short answer:** It follows NSS and can include centralized identities.

### Enhanced Q33. What does a file actually store for owner?

**Short answer:** Numeric UID/GID.

### Enhanced Q34. What does `chage` manage?

**Short answer:** Local account password aging/expiry metadata.

### Enhanced Q35. fork/exec model?

**Short answer:** Create child execution context, then replace it with a new program.

### Enhanced Q36. What is process state D?

**Short answer:** Uninterruptible sleep, often waiting on I/O.

### Enhanced Q37. What is a zombie?

**Short answer:** Exited process whose parent has not collected its exit status.

### Enhanced Q38. Orphan vs zombie?

**Short answer:** Orphan's parent exited while child lives; zombie has already exited.

### Enhanced Q39. What does lsof show?

**Short answer:** Open resources associated with processes.

### Enhanced Q40. Does changing your shell environment modify an already-running service?

**Short answer:** No.

### Enhanced Q41. Why SIGTERM before SIGKILL?

**Short answer:** Allows the process to clean up gracefully.

### Enhanced Q42. What is load average?

**Short answer:** Average count of runnable and certain uninterruptible tasks over time windows.

### Enhanced Q43. Why compare load with CPU count?

**Short answer:** Same load value has different meaning on different CPU capacities.

### Enhanced Q44. What is MemAvailable?

**Short answer:** Estimate of memory available for new work without heavy swapping.

### Enhanced Q45. What is OOM killer?

**Short answer:** Kernel mechanism that can terminate processes under severe memory exhaustion.

### Enhanced Q46. What are cgroups?

**Short answer:** Kernel resource accounting/limiting groups used by systemd and containers.

### Enhanced Q47. What are namespaces?

**Short answer:** Kernel isolation of resource views such as PID, network, mount, user.

### Enhanced Q48. Name three systemd unit types besides service.

**Short answer:** socket, timer, mount, target, path, device.

### Enhanced Q49. Active vs enabled?

**Short answer:** Active is runtime state; enabled is boot/dependency activation configuration.

### Enhanced Q50. Does `After=` imply `Requires=`?

**Short answer:** No.

### Enhanced Q51. What does daemon-reload do?

**Short answer:** Reloads systemd manager unit configuration.

### Enhanced Q52. Why use systemd drop-ins?

**Short answer:** Keep local overrides separate from vendor files.

### Enhanced Q53. What is a systemd target?

**Short answer:** Grouping/synchronization unit representing an operating-state goal.

### Enhanced Q54. Why use systemd timer instead of cron sometimes?

**Short answer:** Better dependency integration, journaling, persistence options, and scheduling features.

### Enhanced Q55. What does `journalctl -b -1` mean?

**Short answer:** Journal from previous boot when retained.

### Enhanced Q56. Why does journal persistence matter?

**Short answer:** Previous-boot incident evidence may otherwise be lost.

### Enhanced Q57. What is logrotate?

**Short answer:** Policy/tooling for rotating, compressing, retaining, and removing logs.

### Enhanced Q58. What does `rpm -qf` answer?

**Short answer:** Which installed package owns a file.

### Enhanced Q59. Why inspect `dnf history`?

**Short answer:** Identify package changes and recent transactions.

### Enhanced Q60. Why are third-party repos security-sensitive?

**Short answer:** They become trusted software supply-chain sources.

### Enhanced Q61. Install package means service runs?

**Short answer:** No.

### Enhanced Q62. GPT vs filesystem?

**Short answer:** GPT is partition table; filesystem is created on a block region/device.

### Enhanced Q63. PV/VG/LV?

**Short answer:** Physical Volume, Volume Group, Logical Volume in LVM.

### Enhanced Q64. Why is mkfs dangerous?

**Short answer:** It creates a filesystem and can destroy access to existing data.

### Enhanced Q65. XFS shrinking?

**Short answer:** Ordinary XFS shrinking is not supported; plan capacity accordingly.

### Enhanced Q66. Why can df and du disagree?

**Short answer:** Deleted-open files, hidden mounts, metadata, reservations, snapshots, etc.

### Enhanced Q67. What does iostat help observe?

**Short answer:** Device I/O utilization/latency metrics.

### Enhanced Q68. What is a kernel module?

**Short answer:** Loadable kernel code commonly providing drivers/features.

### Enhanced Q69. What does sysctl manage?

**Short answer:** Runtime kernel parameters exposed largely through /proc/sys.

### Enhanced Q70. Runtime `ip` change vs nmcli profile?

**Short answer:** Runtime kernel state may disappear; NetworkManager profile is persistent intent.

### Enhanced Q71. Interface UP proves connectivity?

**Short answer:** No.

### Enhanced Q72. What does `ip route get` do?

**Short answer:** Shows route/source/next-hop decision for a destination.

### Enhanced Q73. Neighbor INCOMPLETE means?

**Short answer:** Neighbor resolution has not completed.

### Enhanced Q74. Why use `getent hosts`?

**Short answer:** Tests normal NSS resolver path used by many applications.

### Enhanced Q75. 127.0.0.1 listener reachable remotely?

**Short answer:** No, it is loopback-only.

### Enhanced Q76. What does TCP ESTAB prove?

**Short answer:** Transport handshake completed.

### Enhanced Q77. Why use curl after ping?

**Short answer:** Tests application/HTTP/TLS rather than only ICMP reachability.

### Enhanced Q78. What is SSH known_hosts?

**Short answer:** Client database of server host-key identities.

### Enhanced Q79. Why not ignore changed SSH host key?

**Short answer:** Could indicate rebuild or interception and must be verified.

### Enhanced Q80. Private SSH key sharing?

**Short answer:** Never share it.

### Enhanced Q81. What is ssh-agent?

**Short answer:** Process that holds usable private-key credentials for SSH authentication.

### Enhanced Q82. Why rsync dry-run?

**Short answer:** Preview changes before modifying destination.

### Enhanced Q83. What does firewalld zone represent?

**Short answer:** Policy/trust grouping applied to interfaces/sources.

### Enhanced Q84. Runtime vs permanent firewalld?

**Short answer:** Runtime active now; permanent persists after reload/reboot.

### Enhanced Q85. DAC vs SELinux MAC?

**Short answer:** Traditional discretionary permissions vs mandatory policy/context enforcement.

### Enhanced Q86. Can chmod 777 override SELinux?

**Short answer:** No.

### Enhanced Q87. What is SELinux type?

**Short answer:** Context field commonly used by policy to classify subjects/objects.

### Enhanced Q88. Why restorecon?

**Short answer:** Restore expected SELinux file labels from policy.

### Enhanced Q89. What is initramfs?

**Short answer:** Early userspace used to load drivers/storage and reach the real root filesystem.

### Enhanced Q90. Why inspect /proc/cmdline?

**Short answer:** See kernel parameters supplied at boot.

### Enhanced Q91. What is rescue target?

**Short answer:** Reduced recovery operating mode.

### Enhanced Q92. What is `/proc`?

**Short answer:** Virtual filesystem exposing live process/kernel state.

### Enhanced Q93. What is `/sys`?

**Short answer:** Virtual filesystem representing kernel devices/classes/subsystems.

### Enhanced Q94. What is udev?

**Short answer:** Userspace device-event manager creating/managing device nodes/rules.

### Enhanced Q95. Why cron scripts fail despite working manually?

**Short answer:** Cron has different/minimal environment, PATH, cwd, permissions.

### Enhanced Q96. Why use arrays in Bash?

**Short answer:** Preserve argument boundaries without unsafe string concatenation.

### Enhanced Q97. What does pipefail change?

**Short answer:** Makes earlier pipeline failures contribute to pipeline failure status.

### Enhanced Q98. Why use mktemp?

**Short answer:** Safely create unique temp files/directories.

### Enhanced Q99. What does trap EXIT help with?

**Short answer:** Cleanup on script exit.

### Enhanced Q100. Why avoid parsing ls?

**Short answer:** Filenames can contain whitespace/newlines and output is presentation-oriented.

### Enhanced Q101. sed vs awk?

**Short answer:** sed excels at stream transformations; awk at field/record processing.

### Enhanced Q102. What does SHA-256 checksum prove?

**Short answer:** Content digest/integrity comparison, not source authenticity alone.

### Enhanced Q103. Archive vs backup?

**Short answer:** Archive bundles data; backup adds independent recoverable copy/retention/restore testing.

### Enhanced Q104. Best permission-denied workflow?

**Short answer:** Check identity → parent path → mode/ACL → mount → SELinux → service sandbox/capabilities.

### Enhanced Q105. Best service troubleshooting workflow?

**Short answer:** Package/config → systemd/journal → socket → firewall/SELinux → network/application.

### Enhanced Q106. Best disk-full workflow?

**Short answer:** df blocks + df inodes + du + lsof deleted-open + mount topology.

### Enhanced Q107. Best Linux troubleshooting rule?

**Short answer:** Collect evidence, isolate subsystem, change minimally, verify, document.


## Extended Troubleshooting Scenarios

### Scenario 1 — Command Not Found

```bash
mytool
bash: mytool: command not found
```
Check:

```bash
type mytool
which mytool
echo "$PATH"
dnf provides '*/mytool'
```

Possible causes:
- package not installed,
- executable not in PATH,
- typo,
- no execute permission,
- shell alias/function expectation mismatch.
### Scenario 2 — Permission Denied

```text
bash: ./script.sh: Permission denied
```
```bash
ls -l script.sh
namei -l ./script.sh
getenforce
mount | grep "$(df --output=target . | tail -1)"
```
Possible causes:
- execute bit missing,
- parent-directory traverse permission missing,
- filesystem mounted `noexec`,
- SELinux denial,
- wrong interpreter/shebang.
### Scenario 3 — Service Is Running but Port Is Closed

```bash
systemctl status myservice
ss -tlnp
journalctl -u myservice
sudo firewall-cmd --list-all
```
"Active" does not prove:
- correct bind address,
- correct port,
- firewall permission,
- application health,
- remote route reachability.
### Scenario 4 — DNS Fails but Ping by IP Works

```bash
ping -c 2 8.8.8.8
dig example.com
cat /etc/resolv.conf
ip route
```
Interpretation:

IP routing works.
Name resolution is the likely failing component.

Check resolver address, DNS reachability, firewall, and resolver service.
### Scenario 5 — Filesystem Full

```bash
df -h
df -i
du -xh /var | sort -h | tail
sudo lsof +L1
```
Do not immediately delete random logs.

Identify:
- which filesystem,
- whether bytes or inodes are exhausted,
- which files/directories consume space,
- whether deleted files remain open.
## Final Completion Checklist

- [ ] I can explain Linux kernel, user space, distributions, shell, and services.
- [ ] I can navigate the filesystem without relying on a GUI.
- [ ] I can explain the purpose of major Linux directories.
- [ ] I can create, copy, move, delete, search, and inspect files safely.
- [ ] I understand inodes, hard links, and symbolic links.
- [ ] I can use pipes, redirection, grep, cut, sort, uniq, find, and regular expressions.
- [ ] I can manage users, groups, ownership, permissions, and umask.
- [ ] I can inspect and control processes and signals.
- [ ] I can manage services with systemctl.
- [ ] I can install and query packages with DNF/RPM.
- [ ] I can inspect storage, mounts, CPU, memory, and swap.
- [ ] I can inspect Linux networking, routes, neighbors, DNS, and sockets.
- [ ] I can use SSH keys.
- [ ] I can inspect logs and the journal.
- [ ] I can schedule simple recurring jobs.
- [ ] I can write a basic Bash health-check script.
- [ ] I can troubleshoot services, storage, memory, CPU, DNS, and network issues using evidence.
- [ ] I completed all labs and the Linux Administration Server mini project.


## Enhanced Final Completion Checklist

- [ ] I can explain system calls and the user/kernel boundary.
- [ ] I understand shell parsing, quoting, globbing, command substitution, variables, environment, and PATH.
- [ ] I understand exit status, file descriptors, pipelines, redirection order, and here-documents.
- [ ] I can explain directory entries, inodes, hard links, symlinks, deleted-open files, and inode exhaustion.
- [ ] I understand block devices, filesystems, mount points, UUIDs, fstab, and mount options.
- [ ] I understand directory permissions, ACLs, SGID directories, sticky bit, SUID, and capabilities.
- [ ] I can explain sudo policy and use `visudo` safely.
- [ ] I understand NSS, UID/GID identity, account aging, and orphaned ownership.
- [ ] I understand process creation, states, zombies, signals, open files, load, memory, swap, and OOM evidence.
- [ ] I understand cgroups and namespaces at foundation level.
- [ ] I can explain systemd unit types, dependencies, targets, overrides, timers, and journal filtering.
- [ ] I understand RPM/DNF package identity, dependency resolution, history, and repository trust.
- [ ] I understand partition tables, LVM foundations, XFS/ext4 awareness, and destructive filesystem operations.
- [ ] I can inspect kernel modules and sysctl state.
- [ ] I distinguish runtime Linux network state from persistent NetworkManager configuration.
- [ ] I can troubleshoot route, neighbor, DNS, sockets, and HTTP layer by layer.
- [ ] I understand SSH host keys, user keys, agents, configuration, and hardening foundations.
- [ ] I understand firewalld runtime/permanent policy and SELinux DAC/MAC layering.
- [ ] I can explain firmware → bootloader → kernel → initramfs → systemd boot stages.
- [ ] I can use `/proc`, `/sys`, and udev information for system inspection.
- [ ] I can write safer Bash using functions, arrays, quoting, pipefail, mktemp, and trap.
- [ ] I can distinguish archive, synchronization, checksum, and actual backup strategy.
- [ ] I can troubleshoot permission, service, storage, CPU, memory, and network incidents using evidence.
- [ ] I completed the enhanced labs and expanded Linux Administration Server capstone.
