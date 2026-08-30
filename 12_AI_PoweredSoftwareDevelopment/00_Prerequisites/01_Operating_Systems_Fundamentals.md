# 1. Topic Title

## Operating Systems Fundamentals

An operating system (OS) is the control layer between computer hardware and applications.

A useful view is:

```text
Users
  ↓
Applications
  ↓
Libraries / Runtime
  ↓
System Calls
  ↓
Operating-System Kernel
  ↓
Drivers
  ↓
Hardware
```

For cloud, system administration, DevOps, and cybersecurity, it is not enough to know how to open applications or copy files. You need to understand how the OS represents and controls:

```text
Processes
Threads
Memory
Files
Users
Permissions
Devices
Services
Network resources
Logs
Security boundaries
```

This course develops those concepts using both Linux and Windows examples.

---

# 2. Learning Objectives

By the end of this topic, you should be able to:

1. Explain why an operating system exists.
2. Explain kernel space, user space, system calls, libraries, shells, drivers, and services.
3. Explain monolithic-kernel and microkernel concepts at a foundational level.
4. Explain process creation, states, PIDs, parent/child relationships, threads, scheduling, and context switching.
5. Explain CPU-bound versus I/O-bound workloads.
6. Explain virtual memory, pages, address spaces, paging, swap/page files, and memory pressure.
7. Explain stack, heap, executable/code, and shared-library memory regions conceptually.
8. Explain files, directories, absolute/relative paths, file metadata, links, mounts, volumes, and file-system types.
9. Explain users, groups, UIDs/GIDs, SIDs, permissions, ACLs, privilege, and least privilege.
10. Explain services/daemons and service managers.
11. Explain device drivers and device abstraction.
12. Explain the boot process from firmware to user environment.
13. Explain environment variables and process environments.
14. Explain standard input, output, and error streams.
15. Explain pipes and redirection.
16. Explain sockets and how the OS exposes networking to applications.
17. Inspect running processes, CPU, RAM, filesystems, services, network interfaces, sockets, and logs.
18. Compare common Linux and Windows management concepts.
19. Apply evidence-based troubleshooting.
20. Apply basic operational-security practices such as patching, least privilege, service minimization, and logging.

---

# 3. Prerequisites

You should understand the Computer Architecture introduction, especially:

```text
CPU
RAM
Storage
Privilege levels
Boot process
Interrupts
Input/Output
```

You should also have:

- Basic desktop-computer experience.
- Familiarity with files and folders.
- Basic exposure to a command prompt or terminal.

For the labs, use one of:

```text
Option A:
Windows + Ubuntu VM

Option B:
Linux primary machine + Windows VM

Option C:
Two isolated virtual machines
```

Virtual machines are strongly recommended when experimenting with services, permissions, startup behavior, and security settings.

---

# 4. Core Concepts Explanation

# Part 1 — Why an Operating System Exists

Without an OS, every application would need to know how to control the CPU, memory chips, disk controllers, keyboard, display, network card, USB controllers, and every other device directly.

The OS creates standardized abstractions.

```text
Application asks:
"Open file"

OS handles:
filesystem
disk driver
storage controller
permissions
cache
device communication
```

Instead of an application sending electrical commands to an SSD, it can call an operating-system interface such as:

```text
open()
read()
write()
close()
```

The OS therefore provides:

```text
Abstraction
Resource Management
Protection
Scheduling
Device Control
Storage
Networking
Security
Observability
```

---

# Part 2 — Resource Management

The OS manages limited hardware resources.

Example:

```text
8 CPU logical processors
16 GB RAM
1 TB SSD
1 network interface
```

But perhaps 150 processes are running.

The OS must decide:

```text
Which thread gets CPU time?
Which memory pages stay in RAM?
Which process can read a file?
Which program can bind to a network port?
Which process receives keyboard input?
```

The OS is effectively a resource manager plus a protection layer.

---

# Part 3 — Kernel

The kernel is the privileged core of the operating system.

It manages areas such as:

```text
Process scheduling
Memory management
Device drivers
Filesystem interfaces
Networking
Security enforcement
Interrupt handling
System calls
```

Conceptually:

```text
User Application
      ↓
System Call
      ↓
Kernel
      ↓
Hardware / Protected Resource
```

The kernel normally executes in a privileged CPU mode.

This is important because ordinary applications should not be able to:

- Reprogram hardware arbitrarily.
- Modify other processes' memory.
- Change page tables.
- Access every storage block.
- Disable system protection.

---

# Part 4 — User Space

User space contains ordinary applications and many background processes.

Examples:

```text
Web browser
PowerShell
Bash
Python
Text editor
Web server
Database
Monitoring agent
```

User-space processes have restricted access.

If an application needs a privileged OS service, it requests that service through a system call or higher-level library API.

---

# Part 5 — System Calls

A system call is a controlled transition from user-space code into kernel functionality.

Common categories include:

```text
Process:
create / terminate / wait

Files:
open / read / write / close

Memory:
map / allocate / protect

Networking:
socket / bind / connect / send / receive

Time:
sleep / timers

Security:
permissions / identity operations
```

Example mental model:

```text
Python:
data = open("file.txt").read()

       ↓ language/runtime/library

OS system calls:
open
read
close

       ↓

Kernel
       ↓
Filesystem
       ↓
Storage
```

The programmer usually does not invoke raw system calls directly. Libraries and runtimes provide friendlier APIs.

---

# Part 6 — Kernel Space vs User Space

The separation can be visualized as:

```text
+--------------------------------------+
| User Space                           |
|                                      |
| Browser  Python  Bash  PowerShell    |
| Web Server  Database  Applications   |
+-------------------↓------------------+
                    System Calls
+-------------------↓------------------+
| Kernel Space                         |
|                                      |
| Scheduler | Memory | Files | Network |
| Drivers   | Security | Interrupts     |
+-------------------↓------------------+
                    Hardware
```

Why this matters:

If one browser tab crashes, ideally:

```text
Browser Process
    ✗
```

not:

```text
Whole Operating System
    ✗
```

Isolation reduces failure impact.

It is also a core cybersecurity boundary.

---

# Part 7 — Operating-System Architectures

Operating systems may organize kernel functionality differently.

## Monolithic Kernel Concept

Many core services run in kernel space.

```text
User Apps
   ↓
Kernel:
scheduler
memory
filesystems
networking
drivers
```

Linux is commonly described as a monolithic kernel with modular capabilities.

## Microkernel Concept

A smaller kernel handles fundamental mechanisms while more services run in user space.

```text
Applications
   ↓
User-space services
   ↓
Small privileged kernel
```

The trade-off includes:

```text
Performance
Isolation
Complexity
Reliability
Communication overhead
```

Real operating systems may use hybrid designs, so these categories are architectural models rather than perfect boxes.

---

# Part 8 — Shell

A shell is a user interface to operating-system services.

Examples:

```text
Linux:
bash
zsh

Windows:
PowerShell
cmd.exe
```

A shell can:

- Launch processes.
- Connect commands.
- Manipulate files.
- Set environment variables.
- Automate tasks.

Example Linux:

```bash
ps aux
```

Example Windows:

```powershell
Get-Process
```

Both ask the OS for information about processes, but expose it differently.

---

# Part 9 — Program vs Process

A **program** is executable code stored on persistent storage.

A **process** is a running instance of that program.

```text
Storage:
python executable
        ↓ start
RAM:
Python Process
        ↓
CPU executes threads
```

Running the same program three times creates three processes:

```text
Program: browser

Process 1201
Process 1210
Process 1250
```

Each process has its own execution state and resources.

---

# Part 10 — Process Metadata

A process commonly has:

```text
PID
Parent PID
User/security identity
Virtual address space
Threads
Open files
Open sockets
Environment variables
Current working directory
CPU statistics
Memory statistics
Exit status
```

Linux example:

```bash
ps -o pid,ppid,user,state,%cpu,%mem,cmd -p $$
```

PowerShell:

```powershell
Get-Process -Id $PID | Format-List *
```

The exact fields differ, but the OS concept is the same.

---

# Part 11 — PID

PID means Process Identifier.

A PID uniquely identifies a running process within the current operating-system context.

Example:

```text
PID 1
PID 842
PID 9201
```

PIDs are reused after processes terminate, so a PID alone is not a permanent identity.

Linux:

```bash
echo $$
```

PowerShell:

```powershell
$PID
```

---

# Part 12 — Parent and Child Processes

Processes often create other processes.

```text
Shell
 ↓
Python process
 ↓
Child utility
```

Linux:

```bash
sleep 300 &
echo $!
ps -o pid,ppid,user,state,cmd -p $!
```

`PPID` identifies the parent.

Windows has parent-process relationships too, even though common administration tools expose them differently.

Cybersecurity relevance:

Process trees help analysts answer:

```text
Who launched this suspicious process?
```

Example:

```text
wordprocessor.exe
      ↓
powershell.exe
      ↓
unknown.exe
```

Such a chain may be interesting during incident investigation.

---

# Part 13 — Process States

A simplified process/thread state model:

```text
        +----------+
        |  Ready   |
        +----+-----+
             |
          scheduled
             ↓
        +----------+
        | Running  |
        +----+-----+
             |
   I/O wait  |  time slice expires
       ↓     |     ↓
   +---------+    Ready
   | Waiting |
   +----+----+
        |
  event complete
        ↓
       Ready
```

Common conceptual states:

- Running.
- Runnable/ready.
- Sleeping/waiting.
- Stopped.
- Terminated.

Linux process state letters commonly include values such as:

```text
R = running/runnable
S = interruptible sleep
D = uninterruptible sleep
T = stopped
Z = zombie
```

These details matter when troubleshooting CPU or I/O issues.

---

# Part 14 — Threads

A thread is an execution unit inside a process.

```text
Process
├── Thread 1
├── Thread 2
├── Thread 3
└── Shared memory/resources
```

Threads in the same process generally share:

- Address space.
- Open files.
- Code.
- Heap.

But each thread has its own:

- CPU execution state.
- Stack.
- Registers.

Threads make concurrent work possible but introduce synchronization complexity.

---

# Part 15 — CPU Scheduling

Many runnable threads compete for fewer CPUs.

Example:

```text
100 runnable threads
8 logical CPUs
```

The scheduler repeatedly decides which threads run.

Conceptually:

```text
CPU 0: A → C → D → A
CPU 1: B → E → B → F
```

The scheduling algorithm considers priorities, fairness, responsiveness, and system policies.

You do not normally need to know the exact algorithm at the fundamentals stage. You need to understand that CPU execution is **scheduled**, not permanently assigned to every process.

---

# Part 16 — Context Switching

When the CPU changes from one thread to another:

```text
Thread A running
      ↓
Save A registers/state
      ↓
Load B registers/state
      ↓
Thread B running
```

This is a context switch.

It enables multitasking, but it has overhead.

Very large numbers of runnable threads can therefore reduce performance because the system spends more time scheduling and switching.

Linux:

```bash
vmstat 1 5
```

Look at context-switch-related statistics such as `cs` on systems where displayed.

---

# Part 17 — CPU-Bound vs I/O-Bound Work

A CPU-bound task spends most of its time computing.

Examples:

```text
Compression
Video encoding
Cryptographic calculation
Large numerical processing
```

An I/O-bound task spends significant time waiting for:

```text
Disk
Network
Database
User input
```

Why this matters:

Adding CPU may significantly help CPU-bound workloads but may do little for a process waiting on a slow database.

A useful troubleshooting principle:

```text
Find what the workload is waiting for before adding resources.
```

---

# Part 18 — Process Priority

Operating systems can assign scheduling priorities.

Linux provides concepts such as nice values.

Example:

```bash
nice -n 10 command
```

Windows exposes process priority classes.

PowerShell example:

```powershell
Get-Process notepad | Select-Object Name, PriorityClass
```

Priority tuning should be used carefully. Increasing one process's priority can reduce resources available to others.

---

# Part 19 — Process Termination

A process may terminate:

- Normally.
- Due to an error.
- Because a user/service manager stops it.
- Because the OS kills it.
- Due to resource exhaustion.

Linux:

```bash
kill PID
```

A normal `kill` sends a termination signal by default.

Force kill:

```bash
kill -9 PID
```

Use force termination only when graceful termination fails because it prevents normal cleanup.

Windows:

```powershell
Stop-Process -Id <PID>
```

Force options also exist, but the same operational principle applies:

```text
Graceful stop first
Force only if necessary
```

---

# Part 20 — Zombie Process Concept

On Unix-like systems, a terminated child can briefly remain as a zombie until its parent collects the exit status.

```text
Child exits
   ↓
Exit information remains
   ↓
Parent calls wait()
   ↓
Entry removed
```

A zombie is not a running process consuming CPU. It is mostly a process-table record waiting for its parent to reap it.

Many zombies can indicate a parent-process bug.

---

# Part 21 — Memory Fundamentals

RAM stores active instructions and data.

A process does not usually work with raw physical RAM addresses directly. Instead, the operating system gives it a **virtual address space**.

```text
Process Virtual Address
       ↓
Page Tables / MMU
       ↓
Physical RAM
```

This abstraction provides:

- Isolation.
- Flexible memory allocation.
- Shared mappings.
- Paging.
- Protection.

---

# Part 22 — Virtual Address Space

Each process sees a logical address space.

Conceptually:

```text
Process A
0x0000 ... 0xFFFF

Process B
0x0000 ... 0xFFFF
```

The same-looking virtual address in two processes may map to completely different physical RAM.

This prevents processes from reading each other's memory by default.

---

# Part 23 — Memory Management Unit

The Memory Management Unit (MMU) is hardware that helps translate virtual addresses to physical addresses using page tables maintained by the OS.

```text
Virtual Address
      ↓
MMU
      ↓
Page Table
      ↓
Physical Frame
```

This is a direct connection between operating-system memory management and computer architecture.

---

# Part 24 — Page

Virtual memory is commonly divided into fixed-size pages.

Physical memory is divided into corresponding frames.

Conceptually:

```text
Virtual Pages
P0 P1 P2 P3
      ↓ mappings
Physical Frames
F7 F2 F9 F1
```

Pages do not need to be physically contiguous.

---

# Part 25 — Page Fault

A page fault occurs when a process accesses a page requiring OS intervention.

This does not always mean an error.

Examples:

- Page not yet mapped.
- Page needs to be loaded from disk-backed storage.
- Copy-on-write action required.
- Illegal access causing an access violation/segmentation fault.

Simplified:

```text
CPU accesses page
      ↓
Mapping unavailable
      ↓
Page fault
      ↓
Kernel handles
      ↓
Continue or terminate
```

---

# Part 26 — Paging and Swap

Under memory pressure, the OS may move less-active pages to disk-backed swap/pagefile storage.

Linux:

```text
Swap
```

Windows:

```text
Page file
```

Because disk is much slower than RAM:

```text
RAM access
  ↓ much faster
SSD / page file
```

Heavy paging can cause severe performance degradation.

---

# Part 27 — Memory Pressure

Memory pressure occurs when active memory demand approaches or exceeds available physical memory.

Possible OS responses:

```text
Reclaim filesystem cache
Compress memory on some systems
Page memory to disk
Terminate processes under extreme conditions
```

Do not interpret high RAM usage automatically as a problem.

Operating systems intentionally use spare RAM as cache.

The better questions are:

```text
Is the system paging heavily?
Is application latency increasing?
Is available memory critically low?
Is the system reclaiming aggressively?
```

---

# Part 28 — Stack

Each thread typically has a stack used for:

- Function calls.
- Local variables.
- Return addresses.
- Temporary execution state.

Conceptually:

```text
Thread Stack
+----------------+
| function C     |
| function B     |
| function A     |
+----------------+
```

A stack usually grows/shrinks automatically as functions are entered and returned from.

---

# Part 29 — Heap

The heap is a region used for dynamically allocated memory.

Example conceptual code:

```text
Create object
      ↓
Memory allocated from heap
      ↓
Object used
      ↓
Memory released / garbage collected
```

Languages differ in how heap memory is managed.

C/C++ commonly require explicit allocation/deallocation.

Languages such as Java, Python, and JavaScript runtimes use garbage collection or automatic memory management mechanisms.

---

# Part 30 — Memory Leak

A memory leak occurs when memory is no longer useful but remains allocated/referenced.

```text
Memory usage:
200 MB
400 MB
800 MB
1.6 GB
...
```

Symptoms:

- Increasing resident memory.
- Paging.
- Slow performance.
- Out-of-memory termination.

The solution is not simply "add more RAM." You must identify why memory grows.

---

# Part 31 — RAM vs Storage

RAM:

```text
Fast
Volatile
Active work
Limited capacity
```

Storage:

```text
Slower
Persistent
Files/data
Larger capacity
```

Example:

```text
Program on SSD
      ↓ load
Program in RAM
      ↓
CPU executes
```

This distinction is fundamental.

---

# Part 32 — Filesystem

A filesystem organizes persistent data and metadata.

It manages concepts such as:

```text
Files
Directories
Names
Metadata
Permissions
Free space
Allocation
Timestamps
Links
```

Common examples:

Linux:

```text
ext4
XFS
Btrfs
```

Windows:

```text
NTFS
ReFS
```

Different filesystems provide different capabilities and design trade-offs.

---

# Part 33 — Linux Filesystem Hierarchy

Linux exposes one directory tree starting at `/`.

```text
/
├── bin / usr/bin
├── etc
├── home
├── var
├── tmp
├── dev
├── proc
├── sys
└── mnt
```

Important examples:

```text
/etc     configuration
/home    user home directories
/var     variable application/system data
/tmp     temporary files
/dev     device interfaces
/proc    process/kernel virtual information
/sys     device/kernel interfaces
```

Exact layouts vary by distribution.

---

# Part 34 — Windows Storage Namespace

Windows commonly exposes drive letters:

```text
C:\
D:\
```

But internally Windows also uses volumes and mount points.

Examples:

```text
C:\Windows
C:\Users
C:\Program Files
```

PowerShell:

```powershell
Get-Volume
Get-Disk
Get-Partition
```

---

# Part 35 — Absolute vs Relative Path

Absolute path begins from the filesystem root/drive.

Linux:

```text
/etc/ssh/sshd_config
```

Windows:

```text
C:\Windows\System32
```

Relative path begins from current working directory.

Linux:

```text
./logs/app.log
```

PowerShell:

```text
.\logs\app.log
```

Check current directory:

Linux:

```bash
pwd
```

PowerShell:

```powershell
Get-Location
```

---

# Part 36 — File Metadata

Files have metadata beyond their contents.

Examples:

```text
Owner
Permissions
Size
Timestamps
Type
Attributes
Security descriptor
```

Linux:

```bash
stat file.txt
```

Windows PowerShell:

```powershell
Get-Item .\file.txt | Format-List *
```

---

# Part 37 — Linux Permissions

Traditional Unix permissions are:

```text
r = read
w = write
x = execute
```

Applied to:

```text
owner
group
others
```

Example:

```text
-rw-r-----
```

Breakdown:

```text
owner: rw-
group: r--
other: ---
```

Numeric form:

```text
r = 4
w = 2
x = 1
```

Therefore:

```text
6 = 4+2 = rw-
4 = r--
0 = ---
```

Example:

```bash
chmod 640 file.txt
```

Means:

```text
Owner = rw-
Group = r--
Others = ---
```

---

# Part 38 — Directory Permissions

Directory permissions have special meaning.

For directories:

```text
r = list names
w = create/delete entries
x = traverse/access items
```

A user may be able to know a filename exists but not traverse the directory, depending on the permission combination.

Directory permissions should therefore not be interpreted exactly like file permissions.

---

# Part 39 — Linux Ownership

Linux tracks a file owner and group.

Inspect:

```bash
ls -l
```

Change owner:

```bash
sudo chown user:group file
```

Do not use `sudo` blindly. Ownership changes affect security and application behavior.

---

# Part 40 — Windows ACLs

Windows typically uses Access Control Lists (ACLs).

An ACL contains Access Control Entries (ACEs) defining permissions for identities.

Conceptually:

```text
File
 ↓
ACL
├── User A → Read
├── Group B → Modify
└── Administrators → Full Control
```

PowerShell:

```powershell
Get-Acl C:\path\file.txt | Format-List
```

Windows permissions can inherit from parent folders.

---

# Part 41 — UID, GID, and SID

Linux commonly represents identities internally as numeric:

```text
UID = User Identifier
GID = Group Identifier
```

View:

```bash
id
```

Windows uses Security Identifiers:

```text
SID
```

PowerShell:

```powershell
whoami /user
```

Human-readable usernames are mappings to internal security identities.

---

# Part 42 — Least Privilege

Least privilege means:

> Give a user, process, service, or application only the permissions required for its task.

Bad pattern:

```text
Web application
   ↓
Database administrator account
```

Better:

```text
Web application
   ↓
Database account allowed only required tables/actions
```

Least privilege reduces impact if the application is compromised.

---

# Part 43 — sudo and UAC

Linux commonly uses `sudo` for controlled privilege elevation.

```bash
sudo command
```

Windows uses User Account Control and administrator tokens.

The important security idea is:

```text
Normal work → normal privilege
Administrative operation → temporary elevation
```

Do not remain permanently in high-privilege sessions unnecessarily.

---

# Part 44 — File Links

Unix-like systems commonly support hard links and symbolic links.

Symbolic link:

```text
link → target path
```

Example:

```bash
ln -s /var/log/app.log current.log
```

A symbolic link can point across filesystems and can become broken if the target disappears.

A hard link references the same underlying filesystem object/inode within supported constraints.

Links are useful but can create security/troubleshooting complexity when paths are misunderstood.

---

# Part 45 — Mounting

Linux attaches filesystems into the directory tree at mount points.

```text
Disk filesystem
      ↓ mounted at
/mnt/data
```

Inspect:

```bash
findmnt
df -h
lsblk
```

Windows similarly associates volumes with drive letters or mount points.

A storage device is not necessarily usable until:

```text
Partitioned
Formatted
Mounted / assigned
```

---

# Part 46 — Disk Capacity vs Filesystem Space

A disk may contain multiple partitions/volumes.

```text
1 TB Disk
├── 100 GB System
├── 800 GB Data
└── remaining space
```

Therefore:

```text
Disk size
≠
Filesystem free space
```

Linux:

```bash
lsblk
df -h
```

Windows:

```powershell
Get-Disk
Get-Partition
Get-Volume
```

---

# Part 47 — Inodes Awareness

Unix-like filesystems use structures such as inodes to store file metadata and references to data blocks.

A filesystem can theoretically run out of inodes even when storage capacity remains.

Inspect on Linux:

```bash
df -i
```

This can happen when millions of very small files are created.

---

# Part 48 — Device Drivers

A device driver allows the OS to control hardware.

```text
Application
   ↓
Kernel API
   ↓
Device Driver
   ↓
Hardware
```

Drivers translate generic OS operations into device-specific operations.

Driver problems can cause:

- Device not detected.
- Performance issues.
- Crashes.
- Security vulnerabilities.

---

# Part 49 — Device Abstraction

Applications do not normally need to know the exact hardware model.

Example:

```text
Application writes file
      ↓
Filesystem
      ↓
Block I/O layer
      ↓
Storage driver
      ↓
NVMe/SATA device
```

This abstraction is a major function of the OS.

---

# Part 50 — Interrupts and the OS

Hardware devices notify the processor through interrupts.

Example:

```text
Network packet arrives
      ↓
NIC raises interrupt
      ↓
Kernel interrupt handling
      ↓
Packet enters network stack
      ↓
Application receives data
```

Without interrupts, the CPU would have to constantly poll devices.

---

# Part 51 — DMA Awareness

Direct Memory Access allows some devices to transfer data to/from memory with less direct CPU copying.

Conceptually:

```text
Storage/NIC
   ↕
Memory
```

while CPU coordinates rather than manually copying every byte.

DMA improves I/O efficiency but also requires hardware/OS security controls.

---

# Part 52 — Service / Daemon

A service is a long-running background program.

Linux commonly uses the term daemon.

Examples:

```text
SSH server
Web server
Database
DNS server
Logging daemon
Time synchronization
```

Windows background services are managed by the Service Control Manager.

---

# Part 53 — systemd Awareness

Many Linux distributions use `systemd`.

Useful commands:

```bash
systemctl status ssh
systemctl start ssh
systemctl stop ssh
systemctl restart ssh
systemctl enable ssh
systemctl disable ssh
```

Meaning:

```text
start/stop = current runtime state
enable/disable = boot startup configuration
```

A service can be:

```text
enabled but currently stopped
disabled but manually running
```

These are different concepts.

---

# Part 54 — Windows Services

PowerShell:

```powershell
Get-Service
```

Inspect one:

```powershell
Get-Service -Name Spooler | Format-List *
```

Start/stop where authorized:

```powershell
Start-Service -Name <service>
Stop-Service -Name <service>
```

Before stopping a service, understand its purpose and dependencies.

---

# Part 55 — Service Minimization

Every unnecessary network-facing or privileged service adds:

```text
Code
Attack surface
Patch requirement
Configuration
Operational complexity
```

Security baseline principle:

```text
If the service is not required:
do not run it.
```

But do not disable unknown services blindly. First identify purpose and dependencies.

---

# Part 56 — Environment Variables

Environment variables provide process-level configuration.

Linux:

```bash
echo "$PATH"
env | sort
```

PowerShell:

```powershell
$env:PATH
Get-ChildItem Env:
```

Child processes typically inherit a copy of their parent's environment.

Example:

```text
Shell ENV
   ↓ launches
Python Process ENV
```

Changing a shell variable does not automatically modify already-running unrelated processes.

---

# Part 57 — PATH

`PATH` is a list of directories the shell searches for executable commands.

Linux:

```bash
echo "$PATH"
which python3
```

PowerShell:

```powershell
$env:PATH
Get-Command python
```

If a command exists but its directory is not in PATH, the shell may report that the command cannot be found.

Cybersecurity relevance:

An unsafe PATH can cause a malicious executable to be found before the intended command.

---

# Part 58 — Standard Streams

Processes commonly have:

```text
stdin  = standard input
stdout = standard output
stderr = standard error
```

Example:

```text
Keyboard / pipe → stdin
Program output  → stdout
Errors          → stderr
```

These abstractions make command pipelines possible.

---

# Part 59 — Redirection

Linux shell example:

```bash
command > output.txt
```

Redirect standard error:

```bash
command 2> errors.txt
```

Append:

```bash
command >> output.txt
```

PowerShell also supports redirection concepts.

Be careful when redirecting because `>` commonly overwrites the target file.

---

# Part 60 — Pipes

A pipe connects one process's output to another process's input.

Linux:

```bash
ps aux | grep ssh
```

Conceptually:

```text
ps stdout
   ↓ pipe
grep stdin
```

PowerShell:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

PowerShell pipes rich objects rather than only plain text in many cmdlets.

---

# Part 61 — Operating-System Networking

The OS implements a network stack.

Applications use sockets rather than directly controlling the NIC.

```text
Application
   ↓
Socket API
   ↓
TCP / UDP
   ↓
IP
   ↓
Network Driver
   ↓
NIC
```

This abstraction is foundational for later networking.

---

# Part 62 — Socket

A socket is an endpoint for network communication.

A server commonly:

```text
create socket
bind address/port
listen
accept
read/write
```

A client commonly:

```text
create socket
connect
read/write
```

Example:

```text
Web Server:
0.0.0.0:8080
```

means the application is listening on TCP/UDP semantics depending on the socket and may accept connections through interfaces represented by that wildcard binding.

---

# Part 63 — Port

A port identifies an application endpoint within a host's transport layer.

Example:

```text
IP: 192.0.2.10
Port: 443
```

Together:

```text
192.0.2.10:443
```

The operating system maps incoming transport traffic to the socket owned by a process.

---

# Part 64 — Listening Socket Inspection

Linux:

```bash
ss -tulpn
```

Windows:

```powershell
Get-NetTCPConnection -State Listen
```

or:

```powershell
netstat -ano
```

These commands help answer:

```text
Which ports are listening?
Which process owns the socket?
Which addresses are exposed?
```

---

# Part 65 — Loopback

Loopback is the host talking to itself.

Common IPv4 address:

```text
127.0.0.1
```

Common IPv6 loopback:

```text
::1
```

A service listening only on loopback:

```text
127.0.0.1:8080
```

is generally not directly reachable from remote hosts.

A service listening on all IPv4 interfaces:

```text
0.0.0.0:8080
```

may be reachable depending on firewall, routing, and network configuration.

---

# Part 66 — Boot Process

A simplified boot sequence:

```text
Power On
  ↓
BIOS / UEFI
  ↓
Bootloader / Boot Manager
  ↓
Kernel
  ↓
Drivers / Core Subsystems
  ↓
Initial User-Space Process / Service Manager
  ↓
Services
  ↓
Login / GUI
```

The exact sequence varies by operating system.

---

# Part 67 — Firmware

Firmware begins system initialization before the OS runs.

Modern PCs commonly use UEFI.

Firmware tasks include:

- Hardware initialization.
- Boot device selection.
- Loading a boot manager.
- Security features such as Secure Boot.

A broken boot does not automatically mean the operating-system kernel itself is corrupted. The failure may occur earlier.

---

# Part 68 — Bootloader

The bootloader/boot manager locates and loads the OS kernel and associated startup components.

Linux environments commonly use bootloaders such as GRUB.

Windows uses Windows Boot Manager and OS loader components.

Troubleshooting sequence:

```text
Power?
Firmware?
Boot device?
Boot manager?
Kernel?
Root/system volume?
Services?
```

---

# Part 69 — Secure Boot Awareness

Secure Boot uses firmware trust mechanisms to verify approved boot components.

Conceptually:

```text
Firmware trust
   ↓ verifies
Boot component
   ↓ verifies/loads
OS
```

It helps defend against unauthorized boot-level code.

Do not disable Secure Boot merely to solve an installation problem without understanding the security consequence.

---

# Part 70 — Logging

Logs provide evidence of system and application activity.

Categories include:

```text
Kernel
System
Authentication
Security/Audit
Service
Application
Hardware
Network
```

A troubleshooting principle:

```text
Evidence before configuration change.
```

---

# Part 71 — Linux Journal

Many Linux systems using systemd expose logs through `journalctl`.

Examples:

```bash
journalctl -b
journalctl -b --priority=warning
journalctl --since "30 minutes ago"
journalctl -u ssh
```

Meaning:

```text
-b = current boot
-u = unit/service
```

Use filters to reduce noise.

---

# Part 72 — Windows Event Logs

Windows records events into logs such as:

```text
System
Application
Security
```

PowerShell:

```powershell
Get-WinEvent -LogName System -MaxEvents 20
```

Filter example:

```powershell
Get-WinEvent -FilterHashtable @{
    LogName='System'
    Level=2
    StartTime=(Get-Date).AddHours(-1)
}
```

Do not interpret every warning as a critical failure. Context matters.

---

# Part 73 — Monitoring CPU

Linux:

```bash
top
ps aux --sort=-%cpu | head
vmstat 1 5
```

Windows:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Counter '\Processor(_Total)\% Processor Time'
```

Questions to ask:

```text
Is CPU actually saturated?
One process or many?
One core or all cores?
Short spike or sustained?
CPU-bound or waiting elsewhere?
```

---

# Part 74 — Monitoring Memory

Linux:

```bash
free -h
vmstat 1 5
```

Windows:

```powershell
Get-Counter '\Memory\Available MBytes'
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10
```

Do not consider "used RAM" alone.

Investigate:

```text
Available memory
Paging
Process growth
Swap/page-file activity
Performance symptoms
```

---

# Part 75 — Monitoring Storage

Linux:

```bash
lsblk
df -h
df -i
```

Windows:

```powershell
Get-Disk
Get-Volume
```

Check:

```text
Capacity
Free space
Filesystem
Mount/drive
Read-only state
Inode usage on relevant Unix filesystems
```

Storage-full events can cause:

- Application errors.
- Database failures.
- Logging failures.
- Package-install failures.
- System instability.

---

# Part 76 — Monitoring Network Configuration

Linux:

```bash
ip addr
ip route
```

Windows:

```powershell
Get-NetIPConfiguration
Get-NetRoute
```

Identify:

```text
IP address
Prefix/subnet
Default gateway
DNS servers
Interface status
```

These become prerequisites for networking.

---

# Part 77 — Firewall Awareness

The OS often integrates host firewall controls.

Linux may use frameworks/tools such as:

```text
nftables
firewalld
ufw
```

depending on distribution.

Windows:

```powershell
Get-NetFirewallProfile
```

A service can be listening correctly while still unreachable because the firewall blocks traffic.

Troubleshooting should therefore separate:

```text
Application listening?
Host firewall?
Network route?
Remote firewall?
```

---

# Part 78 — Patching

Operating systems and installed software contain vulnerabilities and defects.

Patching reduces exposure.

Linux update tools vary by distribution.

Examples:

```bash
sudo apt update
apt list --upgradable
```

Red Hat-family systems use different package managers.

Windows uses Windows Update and enterprise update-management mechanisms.

Before patching production systems:

```text
Review
Backup/recovery
Test
Schedule
Apply
Verify
Rollback plan
```

---

# Part 79 — Package Manager Awareness

Package managers install, update, and remove software while tracking dependencies.

Debian/Ubuntu:

```bash
apt
dpkg
```

Red Hat-family:

```bash
dnf
rpm
```

Windows may use:

```text
Windows Update
winget
MSI/package mechanisms
```

Do not download random binaries from untrusted sources when trusted repositories are available.

---

# Part 80 — Troubleshooting Method

Use a structured sequence:

```text
1. Observe
2. Define symptom precisely
3. Establish scope
4. Collect evidence
5. Form hypothesis
6. Change one variable
7. Test
8. Verify
9. Roll back if needed
10. Document
```

Example:

Bad approach:

```text
Website slow
→ restart server
→ clear logs
→ disable firewall
```

Better approach:

```text
Website slow
→ check latency
→ identify affected endpoints
→ inspect CPU/memory
→ inspect DB latency
→ inspect logs
→ test one hypothesis
```

---

# Part 81 — Baseline

A baseline records normal system behavior.

Examples:

```text
Normal CPU
Normal memory
Normal disk usage
Normal running services
Normal open ports
Normal event rate
Normal boot time
```

Without a baseline, it is harder to know whether observed behavior is abnormal.

---

# Part 82 — Change Control

Before administrative changes:

```text
Record current state
Record reason
Record exact change
Know rollback
Apply change
Verify
Document result
```

This is useful even in a home lab because it builds production habits.

---

# Part 83 — Security Baseline

A foundational OS security baseline includes:

```text
Supported OS version
Current patches
Host firewall
Least privilege
Minimal services
Secure authentication
Protected logs
Secure boot where appropriate
Disk encryption where appropriate
Backups
Monitoring
```

Security is not one setting. It is a set of controls working together.

---

# Part 84 — Malware and Process Awareness

Malware still runs within operating-system concepts.

Analysts examine:

```text
Process tree
Parent process
Command line
User identity
Open network sockets
Files created
Persistence mechanism
Memory behavior
Logs
```

Example suspicious sequence:

```text
Office application
     ↓
Command shell
     ↓
Script interpreter
     ↓
Unknown executable
     ↓
Outbound network connection
```

The sequence itself is not automatic proof of malware, but it is evidence worth investigating in the correct context.

---

# Part 85 — Persistence Awareness

Programs can configure themselves to start automatically.

Common categories:

Linux:

```text
systemd service
cron
shell startup
desktop autostart
```

Windows:

```text
Services
Scheduled Tasks
Startup entries
Registry-based startup mechanisms
```

Cybersecurity analysts inspect persistence because malware may attempt to survive reboots.

Defensive rule:

```text
Know what should start automatically on your machines.
```

---

# Part 86 — OS Virtualization Connection

Virtual machines contain guest operating systems.

```text
Physical Hardware
      ↓
Hypervisor
 ┌────┴────┐
 ↓         ↓
Guest OS  Guest OS
```

Inside each guest:

```text
Processes
Virtual memory
Filesystems
Services
Users
Network stack
```

The guest OS behaves similarly to a physical machine, but devices are often virtualized.

---

# Part 87 — Container Connection

Containers do **not** normally contain an independent kernel.

```text
Host Kernel
├── Container A processes
├── Container B processes
└── Host processes
```

Namespaces and cgroups provide isolation/resource control.

This is why Linux OS fundamentals are essential before Docker and Kubernetes.

---

# Part 88 — Cloud Connection

A cloud virtual machine is still an operating-system instance.

Cloud automation may create it in seconds, but inside it still has:

```text
Kernel
Processes
Memory
Filesystems
Services
Users
Network stack
Logs
```

Therefore traditional OS administration remains relevant in cloud environments.

---

# Part 89 — Incident Response Connection

During incident response, OS evidence may include:

```text
Processes
Services
Users
Logins
Network connections
Open files
Scheduled tasks
Logs
Startup mechanisms
Memory
Filesystem timestamps
```

Good OS fundamentals make security investigation much easier.

---

# Part 90 — Final Operating-System Mental Model

Remember this layered view:

```text
Applications
    ↓
Libraries / Runtime
    ↓
System Calls
    ↓
Kernel
├── Scheduler
├── Memory Manager
├── Filesystems
├── Network Stack
├── Security
└── Drivers
    ↓
Hardware
```

And this operational view:

```text
User starts process
      ↓
OS creates process
      ↓
Scheduler gives CPU
      ↓
Virtual memory maps RAM
      ↓
Process opens files/sockets
      ↓
Kernel enforces permissions
      ↓
Drivers communicate with devices
      ↓
Logs record events
```

If you understand these two diagrams, you have the foundation required for Linux administration, Windows administration, networking, virtualization, cloud computing, containers, and cybersecurity.

---

# 5. Hands-on Lab / Practical Exercises

## Lab 1 — Build a Complete OS Inventory

### Linux

```bash
cat /etc/os-release
uname -a
uname -m
lscpu
free -h
lsblk -f
df -h
ip addr
ip route
```

Record:

```text
OS
Kernel
Architecture
CPU
RAM
Storage
Filesystems
IP addresses
Default route
```

### Windows

```powershell
Get-ComputerInfo |
Select-Object WindowsProductName,WindowsVersion,OsBuildNumber,OsArchitecture

Get-CimInstance Win32_Processor |
Select-Object Name,NumberOfCores,NumberOfLogicalProcessors

Get-CimInstance Win32_ComputerSystem |
Select-Object TotalPhysicalMemory

Get-Disk
Get-Volume
Get-NetIPConfiguration
```

### Expected Learning

You should be able to point to the equivalent concept in both operating systems.

---

## Lab 2 — Observe Your Shell Process

Linux:

```bash
echo $$
ps -p $$ -o pid,ppid,user,state,cmd
```

Windows:

```powershell
$PID
Get-Process -Id $PID
```

Explain:

```text
PID
Owner
Parent
Command
```

---

## Lab 3 — Parent/Child Process Tree

Linux:

```bash
sleep 300 &
PID=$!
ps -o pid,ppid,user,state,cmd -p "$PID"
pstree -p | head -50
kill "$PID"
```

Expected behavior:

```text
sleep process appears
has a parent
terminates after kill
```

---

## Lab 4 — Process State

Linux:

```bash
ps -eo pid,ppid,state,%cpu,%mem,cmd | head -30
```

Identify examples of:

```text
R
S
D if present
T if intentionally created in lab
```

Do not force processes into unusual states on production machines.

---

## Lab 5 — CPU Observation

Linux:

```bash
top
vmstat 1 5
```

Windows:

```powershell
Get-Counter '\Processor(_Total)\% Processor Time' -SampleInterval 1 -MaxSamples 5
```

Open several applications and observe.

Write:

```text
Baseline CPU
Peak CPU
Top process
Was the spike sustained?
```

---

## Lab 6 — Memory Observation

Linux:

```bash
free -h
vmstat 1 5
```

Windows:

```powershell
Get-Counter '\Memory\Available MBytes' -SampleInterval 1 -MaxSamples 5
```

Record:

```text
Total
Available
Swap/Page file concept
Largest process
```

Explain why "used RAM" alone is not enough.

---

## Lab 7 — Observe Process Memory

Linux:

```bash
ps aux --sort=-%mem | head
```

Windows:

```powershell
Get-Process |
Sort-Object WorkingSet64 -Descending |
Select-Object -First 10 Name,Id,WorkingSet64
```

Identify the top consumers.

Do not terminate them merely because they are large.

---

## Lab 8 — Filesystem Capacity

Linux:

```bash
lsblk
df -h
df -i
```

Windows:

```powershell
Get-Disk
Get-Partition
Get-Volume
```

Create a table:

```text
Device
Volume
Filesystem
Total
Free
Mount/Drive
```

---

## Lab 9 — Absolute and Relative Paths

Linux:

```bash
mkdir -p ~/phase1/os-lab/dir1
cd ~/phase1/os-lab
pwd
touch dir1/example.txt
ls ./dir1
ls "$HOME/phase1/os-lab/dir1"
```

PowerShell:

```powershell
New-Item -ItemType Directory "$HOME\phase1\os-lab\dir1" -Force
Set-Location "$HOME\phase1\os-lab"
New-Item ".\dir1\example.txt" -ItemType File
Get-ChildItem ".\dir1"
```

Explain which paths are absolute and relative.

---

## Lab 10 — Linux Permissions

```bash
cd ~/phase1/os-lab
echo "confidential" > data.txt
chmod 640 data.txt
ls -l data.txt
stat data.txt
```

Explain:

```text
6 = rw-
4 = r--
0 = ---
```

---

## Lab 11 — Directory Permissions

On a disposable Linux lab:

```bash
mkdir permissions-demo
touch permissions-demo/file.txt
chmod 700 permissions-demo
ls -ld permissions-demo
```

Explain how directory execute permission controls traversal.

---

## Lab 12 — Windows ACL Inspection

```powershell
New-Item -ItemType Directory "$HOME\phase1\acl-lab" -Force
Set-Content "$HOME\phase1\acl-lab\data.txt" "confidential"
Get-Acl "$HOME\phase1\acl-lab\data.txt" | Format-List
```

Record:

```text
Owner
Access rules
Inheritance
```

Do not remove ACL entries blindly.

---

## Lab 13 — Identity

Linux:

```bash
whoami
id
groups
```

Windows:

```powershell
whoami
whoami /user
whoami /groups
```

Compare:

```text
Username
UID/SID
Groups
```

---

## Lab 14 — Environment Variables

Linux:

```bash
env | sort | head -30
echo "$PATH"
which python3 2>/dev/null
```

Windows:

```powershell
Get-ChildItem Env: | Sort-Object Name | Select-Object -First 30
$env:PATH
Get-Command powershell
```

Explain what PATH does.

---

## Lab 15 — Pipes and Redirection

Linux:

```bash
ps aux | sort -k3 -nr | head > top-processes.txt
cat top-processes.txt
```

PowerShell:

```powershell
Get-Process |
Sort-Object CPU -Descending |
Select-Object -First 10 |
Out-File "$HOME\top-processes.txt"

Get-Content "$HOME\top-processes.txt"
```

Explain each pipeline stage.

---

## Lab 16 — Service Inspection

Linux:

```bash
systemctl --type=service --state=running | head -30
```

Inspect one:

```bash
systemctl status <service>
```

Windows:

```powershell
Get-Service |
Where-Object Status -eq Running |
Select-Object -First 30
```

Choose five services and record:

```text
Name
Purpose
Startup behavior
Running state
Dependencies
Security exposure
```

---

## Lab 17 — Listening Ports

Linux:

```bash
ss -tulpn
```

Windows:

```powershell
Get-NetTCPConnection -State Listen |
Sort-Object LocalPort
```

Record:

```text
Local address
Port
Protocol
Owning process if available
Expected?
```

Do not assume every listening port is dangerous.

---

## Lab 18 — Loopback vs All Interfaces

If you have a test application, bind it first to:

```text
127.0.0.1
```

then compare with:

```text
0.0.0.0
```

Observe with:

Linux:

```bash
ss -ltn
```

Windows:

```powershell
Get-NetTCPConnection -State Listen
```

Explain why network exposure differs.

---

## Lab 19 — Routes

Linux:

```bash
ip route
```

Windows:

```powershell
Get-NetRoute |
Sort-Object DestinationPrefix
```

Identify:

```text
Default route
Local network route
Loopback/local routes
```

---

## Lab 20 — Linux Logs

```bash
journalctl -b --priority=warning
journalctl --since "30 minutes ago"
```

Select one event.

Write:

```text
Timestamp
Component
Message
Impact
Additional evidence needed
```

Do not "fix" it until you understand it.

---

## Lab 21 — Windows Event Logs

```powershell
Get-WinEvent -LogName System -MaxEvents 30
Get-WinEvent -LogName Application -MaxEvents 30
```

Pick one warning/error and perform the same evidence analysis.

---

## Lab 22 — Boot Evidence

Linux:

```bash
journalctl -b | head -100
```

Windows:

```powershell
Get-WinEvent -FilterHashtable @{
    LogName='System'
    StartTime=(Get-Date).Date
} -MaxEvents 100
```

Find events associated with the current boot.

---

## Lab 23 — Package Inventory

Linux:

```bash
dpkg -l | head
```

or on an RPM-based system:

```bash
rpm -qa | head
```

Windows:

```powershell
winget list
```

if available.

Explain why software inventory matters for patching and security.

---

## Lab 24 — Update Awareness

On an authorized lab machine only:

Ubuntu/Debian-style:

```bash
sudo apt update
apt list --upgradable
```

Do not automatically upgrade a production machine without a change/recovery plan.

Windows:

Use Windows Update interface or enterprise tooling to inspect update status.

---

## Lab 25 — Build a Baseline

Capture:

```text
Top 10 CPU processes
Top 10 memory processes
Running services
Listening ports
Disk usage
Memory availability
Network configuration
Recent system warnings
```

Save the report.

Repeat later and compare.

---

# 6. Mini Project

## Mini Project — Windows/Linux Operating-System Health and Security Baseline

Create a professional baseline report for one Linux machine and, if available, one Windows machine.

## 1. System Inventory

Record:

```text
Hostname
OS
OS build/version
Kernel
Architecture
CPU
Cores
Logical processors
RAM
Storage
Filesystems
Network interfaces
Firmware type if available
```

## 2. Process Baseline

Record:

```text
Top 10 CPU processes
Top 10 memory processes
Parent process information where relevant
User identity
Command line
```

Do not kill unfamiliar processes. Investigate first.

## 3. Service Baseline

Choose at least 10 important services.

For each:

```text
Name
Purpose
Running state
Startup state
Network exposure
Dependencies
Required?
```

## 4. Network Baseline

Record:

```text
IP addresses
Default gateway
DNS
Listening TCP ports
Listening UDP ports
Owning process
Host firewall status
```

## 5. Memory Baseline

Record:

```text
Total RAM
Available RAM
Swap/page file
Top consumers
Evidence of paging
```

## 6. Storage Baseline

Record:

```text
Disk
Partition/volume
Filesystem
Mount point/drive
Total
Free
Inode usage on Linux where relevant
```

## 7. Identity and Permissions

Record:

```text
Current user
UID/SID
Group membership
Privilege model
Example file permission / ACL
```

## 8. Logs

Collect:

```text
5 recent warnings/errors
Source
Timestamp
Impact
Hypothesis
Additional evidence
```

Do not clear or alter logs.

## 9. Security Baseline

Evaluate:

```text
Patch status
Firewall
Least privilege
Unnecessary services
Unexpected listeners
Secure Boot awareness
Disk encryption awareness
Logging
Backup status
```

## 10. Final Risk Summary

Classify observations:

```text
Critical
High
Medium
Low
Informational
```

For every recommended change include:

```text
Reason
Evidence
Expected effect
Rollback
Verification
```

---

# 7. Recommended Resources

This Markdown is designed to be sufficient for the fundamentals learning path.

For deeper implementation details, prefer current official documentation:

- Microsoft Learn for Windows architecture and Windows administration.
- Microsoft Windows Server technical documentation.
- Linux kernel documentation.
- Red Hat Enterprise Linux documentation.
- The documentation of the Linux distribution used in your lab.

Use vendor documentation primarily when command behavior, configuration syntax, security defaults, or version-specific details matter.

---

# 8. Certification Relevance

Operating-system fundamentals support later preparation for:

## RHCSA

Directly relevant concepts:

```text
Users/groups
Permissions
Processes
systemd
Storage
Filesystems
Networking
Logs
Packages
Security
```

## CKA

Kubernetes runs on operating-system fundamentals:

```text
Linux processes
Namespaces/cgroups
Networking
Filesystems
Services
Resource management
Logs
```

## AWS / Azure / Google Cloud

Cloud instances still contain operating systems.

You must understand:

```text
CPU
RAM
Disk
Processes
Services
Patching
Networking
Identity
Logs
```

## Cybersecurity

These concepts are prerequisites for:

```text
Incident response
Endpoint security
Privilege escalation concepts
Persistence analysis
Malware behavior
Forensics
Security hardening
Vulnerability assessment
```

---

# 9. Common Mistakes & Best Practices

## Common Mistakes

- Memorizing commands without understanding the OS model.
- Running permanently as root/Administrator.
- Killing a process before determining why it is consuming resources.
- Treating high RAM utilization as automatically bad.
- Ignoring paging and only looking at memory percentage.
- Confusing disk capacity with filesystem free space.
- Confusing a program with a process.
- Confusing a process with a service.
- Treating every warning log as an emergency.
- Clearing logs before an investigation.
- Disabling firewalls or security controls to "make it work."
- Force-killing services before attempting graceful shutdown.
- Installing software from untrusted sources.
- Exposing services on all interfaces unnecessarily.
- Changing permissions to `777` instead of fixing ownership/access properly.
- Using administrator credentials for ordinary applications.
- Disabling unknown services without understanding dependencies.
- Making several troubleshooting changes at once.

## Best Practices

- Understand the concept before memorizing the command.
- Use least privilege.
- Capture baseline state.
- Use logs and measurements as evidence.
- Make one change at a time.
- Prefer graceful process/service termination.
- Keep supported systems patched.
- Remove or disable unnecessary services only after dependency review.
- Expose only required network listeners.
- Use specific file permissions rather than overly broad access.
- Record changes and rollback procedures.
- Test risky changes in VMs.
- Monitor CPU, memory, disk, and network together.
- Investigate parent/child process relationships during incidents.
- Preserve logs during security or reliability investigations.
- Automate repeatable administration only after understanding the manual behavior.

---

# 10. Self-Assessment Questions (with short answers)

1. **What is the main role of an operating system?**  
   Manage hardware resources and provide protected abstractions/services to users and applications.

2. **What is the kernel?**  
   The privileged core responsible for scheduling, memory, filesystems, devices, networking, security, and system calls.

3. **What is user space?**  
   The lower-privilege environment where normal applications and many services run.

4. **What is a system call?**  
   A controlled request from user-space software for a kernel service.

5. **Program vs process?**  
   A program is stored executable code; a process is a running instance with state and resources.

6. **What is a PID?**  
   Process identifier for a currently running process.

7. **What is a parent process?**  
   A process that created another process.

8. **What is a thread?**  
   An execution unit within a process sharing the process's memory/resources.

9. **What is a context switch?**  
   Saving one thread's CPU state and loading another's.

10. **CPU-bound vs I/O-bound?**  
    CPU-bound spends most time computing; I/O-bound spends much time waiting for disk/network/etc.

11. **What is virtual memory?**  
    Per-process address-space abstraction mapped by the OS/MMU to physical memory and other backing storage.

12. **What is a page?**  
    Fixed-size unit used in virtual-memory management.

13. **What is a page fault?**  
    CPU exception requiring the OS to resolve a memory-page access.

14. **What is swap/page file?**  
    Disk-backed storage used as part of virtual-memory management.

15. **Why is high RAM usage not automatically bad?**  
    The OS intentionally uses spare RAM for caches; paging and performance symptoms matter more.

16. **Stack vs heap?**  
    Stack supports thread call/local execution state; heap supports dynamic allocations.

17. **What is a memory leak?**  
    Memory remains retained despite no longer being useful.

18. **What is a filesystem?**  
    Structure for storing files, directories, metadata, permissions, and allocation information.

19. **Absolute path?**  
    Path beginning at filesystem root or drive root.

20. **Relative path?**  
    Path interpreted from the current working directory.

21. **What does Linux permission `640` mean?**  
    Owner read/write, group read, others none.

22. **What does execute permission mean on a directory?**  
    Ability to traverse/access entries in the directory path.

23. **What is an ACL?**  
    List of access rules associated with an object.

24. **UID/GID?**  
    Numeric Linux user/group identifiers.

25. **SID?**  
    Windows security identifier.

26. **What is least privilege?**  
    Grant only the rights required for the task.

27. **What is a daemon/service?**  
    Long-running background process providing a system/application function.

28. **systemctl start vs enable?**  
    Start affects current runtime; enable configures startup at boot.

29. **What is a device driver?**  
    Software enabling the OS to control a specific hardware device/class.

30. **What is an interrupt?**  
    Hardware/software mechanism requesting CPU/kernel attention.

31. **What is DMA?**  
    Mechanism allowing devices to transfer data to/from memory with reduced direct CPU copying.

32. **What is PATH?**  
    Search path used by shells to locate executable commands.

33. **stdin/stdout/stderr?**  
    Standard input, standard output, and standard error streams.

34. **What is a pipe?**  
    Connects one command/process output to another's input.

35. **What is a socket?**  
    OS endpoint for network communication.

36. **What does `127.0.0.1` represent?**  
    IPv4 loopback interface.

37. **What does listening on `0.0.0.0` usually mean?**  
    Listen on all available IPv4 interfaces, subject to firewall/routing.

38. **What is a bootloader?**  
    Component that locates/loads the operating-system kernel/startup environment.

39. **What is Secure Boot?**  
    Firmware trust mechanism for verifying authorized boot components.

40. **Why inspect logs before changing configuration?**  
    Logs provide evidence needed to build/test a hypothesis.

41. **What is a baseline?**  
    Record of normal system configuration and behavior.

42. **Why not force-kill first?**  
    The application cannot perform normal cleanup and state flushing.

43. **Why minimize services?**  
    Reduce attack surface, maintenance, and resource usage.

44. **What is a listening port?**  
    Network endpoint where a process waits for incoming connections/traffic.

45. **What is paging pressure?**  
    Heavy reclaim/page movement due to insufficient physical memory for active workloads.

46. **What is a mount point?**  
    Directory/location where a filesystem becomes accessible.

47. **Why can a filesystem run out despite free disk space?**  
    It may exhaust metadata such as inodes or hit quota/other constraints.

48. **Why are process trees useful in cybersecurity?**  
    They reveal process ancestry and potentially suspicious launch chains.

49. **What is the safest troubleshooting pattern?**  
    Observe → evidence → hypothesis → one change → verify → document/rollback.

50. **Why are OS fundamentals essential for containers/cloud?**  
    Containers and cloud instances still rely on processes, memory, networking, filesystems, identities, and kernel behavior.
