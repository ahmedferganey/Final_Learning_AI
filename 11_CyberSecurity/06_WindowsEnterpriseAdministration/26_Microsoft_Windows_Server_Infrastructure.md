# 26. Microsoft Windows Server Infrastructure

> Phase 6 — Windows Enterprise Administration

This course teaches Windows Server as an infrastructure operating system.

The central mental model is:

```text
Hardware / Hypervisor
        ↓
Windows Kernel
        ↓
Drivers + Windows Services
        ↓
Server Roles / Features
        ↓
Management Interfaces
        ↓
Applications and Users
```

The material deliberately combines GUI concepts with PowerShell. PowerShell is emphasized because modern Windows administration, automation, cloud operations, security engineering, and Active Directory all benefit from repeatable command-based administration.

---

## 1. Topic Title

**Microsoft Windows Server Infrastructure**

---

## 2. Learning Objectives

By the end of the course, you should be able to:

- Explain Windows Server architecture, editions, installation options, roles, features, services, and management surfaces.
- Administer servers with Server Manager, Windows Admin Center, MMC consoles, PowerShell, and remote-management tools.
- Manage local users, groups, UAC, privileges, NTFS permissions, and service identities.
- Configure disks, GPT partitions, NTFS/ReFS volumes, Storage Spaces concepts, quotas, and SMB file services.
- Explain the interaction between SMB share permissions and NTFS permissions.
- Manage services, processes, scheduled tasks, Event Logs, and registry configuration.
- Configure IPv4/IPv6, routes, DNS client settings, DNS Server, and DHCP Server.
- Configure Windows Defender Firewall and troubleshoot network access by layer.
- Use WinRM, PowerShell Remoting, Windows Admin Center, and RDP securely.
- Install and manage Hyper-V at foundation level.
- Understand Windows Server backup, recovery, performance monitoring, security baselines, patching, and structured troubleshooting.

---

## 3. Prerequisites

Recommended:

- Operating Systems Fundamentals
- Computer Networks Fundamentals
- Phase 4 — Networking
- Basic PowerShell familiarity is useful but not required

Recommended VM:

```text
Name: WIN-SRV01
OS: Windows Server 2025
CPU: 2–4 vCPU
RAM: 4–8 GB
OS Disk: 60 GB
Data Disk: 20 GB disposable lab disk
NIC: isolated lab network
```

Take a checkpoint before destructive storage, firewall, or registry exercises.

---

## 4. Core Concepts Explanation

# Part 1 — Windows Server Architecture

### 1. Windows Server as an Infrastructure Operating System

Windows Server is designed to host infrastructure roles.

```text
Windows Server
   |
   +-- File Server
   +-- DNS Server
   +-- DHCP Server
   +-- Hyper-V
   +-- Web Server
   +-- Active Directory Domain Services
```

A server should normally run only the roles required by its architecture.

This reduces:

```text
unneeded software
       ↓
unneeded services
       ↓
unneeded listening ports
       ↓
attack surface + maintenance work
```

Inspect the OS:

```powershell
Get-ComputerInfo |
    Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
```

Inspect hostname:

```powershell
hostname
Get-ComputerInfo -Property CsName
```

### 2. Windows Server Editions

Current Windows Server editions include families such as:

```text
Standard
Datacenter
Datacenter: Azure Edition
```

Think in terms of workload requirements:

```text
General server / lighter virtualization
              ↓
          Standard

Heavy virtualization / advanced datacenter capabilities
              ↓
          Datacenter

Azure-specific integration scenarios
              ↓
  Datacenter: Azure Edition
```

Do not choose an edition only by name. Review current feature and licensing requirements before production design.

### 3. Desktop Experience vs Server Core

Visual comparison:

```text
Desktop Experience
------------------
GUI shell
Server Manager
local MMC tools
PowerShell
remote management

Server Core
-----------
minimal local GUI
PowerShell
command line
remote Server Manager
Windows Admin Center
remote MMC where supported
```

Server Core is not "a weaker Windows Server." It supports many important infrastructure roles while reducing local graphical components.

Inspect installation type:

```powershell
Get-ComputerInfo |
    Select-Object WindowsInstallationType
```

Inspect supported/installed roles:

```powershell
Get-WindowsFeature |
    Where-Object InstallState -eq 'Installed'
```

### 4. Kernel, Services, and Roles

Visualize the dependency:

```text
Hardware
   ↓
Windows kernel
   ↓
Service Control Manager
   ↓
Windows services
   ↓
Server role
```

Example:

```text
DNS Server role
     ↓
DNS service
     ↓
UDP/TCP 53 socket
     ↓
client queries
```

This matters during troubleshooting because a role being installed does **not** mean its service is healthy or reachable.

---

# Part 2 — Windows Server Management Tools

### 5. Server Manager

Server Manager can manage:

```text
Local Server
All Servers
Roles
Services
Events
Performance
Add Roles and Features
```

Architecture:

```text
Administrator
      |
Server Manager
      |
      +-- WIN-SRV01
      +-- WIN-SRV02
      +-- remote role management
```

Equivalent command-driven mindset:

```powershell
Get-WindowsFeature
Get-Service
Get-WinEvent
Get-NetIPConfiguration
Get-Volume
```

### 6. Windows Admin Center

Conceptual architecture:

```text
Administrator Browser
        |
       HTTPS
        |
Windows Admin Center Gateway
        |
  management protocols
        |
+-------+-------+
|               |
Server A     Server B
```

It can expose tools for:

- services
- processes
- Event Logs
- storage
- certificates
- firewall
- Hyper-V
- updates
- PowerShell

Windows Admin Center is a management surface, not a replacement for understanding the underlying operating system.

### 7. MMC Snap-ins

Common management consoles:

```powershell
compmgmt.msc
eventvwr.msc
services.msc
taskschd.msc
diskmgmt.msc
wf.msc
```

Mental model:

```text
MMC Console
    ↓
Snap-in
    ↓
Windows service/API/configuration
```

Learn the PowerShell equivalent whenever possible.

---

# Part 3 — PowerShell Administration

### 8. PowerShell Works with Objects

Example:

```powershell
Get-Service |
    Where-Object Status -eq 'Running' |
    Select-Object Name, DisplayName, Status
```

Visualization:

```text
Get-Service
    |
    | ServiceController objects
    v
Where-Object
    |
    | filtered objects
    v
Select-Object
```

Unlike a text-only shell, properties remain structured.

Inspect object properties:

```powershell
Get-Service | Get-Member
```

### 9. Command Discovery

```powershell
Get-Command *NetIPAddress*
Get-Command -Noun Service
Get-Help Get-NetIPAddress -Full
Get-Help New-SmbShare -Examples
```

Workflow:

```text
I need to manage networking
        ↓
Get-Command *Net*
        ↓
Get-Help cmdlet
        ↓
test safely
        ↓
Get-* verify state
```

### 10. Filtering and Sorting

```powershell
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 10 Name, Id, CPU
```

Stopped services:

```powershell
Get-Service |
    Where-Object Status -eq 'Stopped' |
    Select-Object Name, StartType
```

### 11. Exporting Administration Data

```powershell
Get-Service |
    Select-Object Name, Status, StartType |
    Export-Csv C:\Admin\Services.csv -NoTypeInformation
```

JSON:

```powershell
Get-NetIPConfiguration |
    ConvertTo-Json -Depth 4 |
    Set-Content C:\Admin\Network.json
```

### 12. CIM

```powershell
Get-CimInstance Win32_OperatingSystem
Get-CimInstance Win32_ComputerSystem
Get-CimInstance Win32_LogicalDisk
```

Example report:

```powershell
Get-CimInstance Win32_LogicalDisk |
    Select-Object DeviceID,
        @{N='SizeGB';E={[math]::Round($_.Size/1GB,2)}},
        @{N='FreeGB';E={[math]::Round($_.FreeSpace/1GB,2)}}
```

---

# Part 4 — Roles and Features

### 13. Roles vs Features

Role:

```text
major server function
```

Examples:

```text
DNS
DHCP
Hyper-V
AD DS
File Server
```

Feature:

```text
supporting capability/component
```

Inspect:

```powershell
Get-WindowsFeature
```

Install:

```powershell
Install-WindowsFeature DNS -IncludeManagementTools
```

Verify:

```powershell
Get-WindowsFeature DNS
```

### 14. Add Roles and Features Workflow

```text
Requirement
   ↓
Dependencies reviewed
   ↓
Install role
   ↓
Post-install configuration
   ↓
Service state
   ↓
Firewall/network state
   ↓
Functional verification
```

Installing a role is only one part of the workflow.

### 15. Remove Unnecessary Roles

```powershell
Uninstall-WindowsFeature <FeatureName>
```

Before removing:

```text
Application dependency?
Role dependency?
Remote management dependency?
Recovery plan?
```

---

# Part 5 — Local Users, Groups, and UAC

### 16. Local Users

Inspect:

```powershell
Get-LocalUser
```

Create a lab account:

```powershell
$Password = Read-Host "Password" -AsSecureString

New-LocalUser `
    -Name "OpsUser" `
    -Password $Password `
    -FullName "Operations User"
```

### 17. Local Groups

```powershell
Get-LocalGroup
Get-LocalGroupMember Administrators
```

Add to a restricted group:

```powershell
Add-LocalGroupMember `
    -Group "Remote Desktop Users" `
    -Member "OpsUser"
```

Visual:

```text
User
  ↓ membership
Group
  ↓ permissions/rights
Resource
```

### 18. Built-in Administrator

Bad operational model:

```text
everyone shares Administrator password
```

Better:

```text
named admin accounts
       ↓
least privilege
       ↓
UAC elevation
       ↓
auditable actions
```

### 19. UAC

Concept:

```text
Admin account logs in
        ↓
standard user token
        ↓
normal applications

When elevation needed:
        ↓
UAC consent
        ↓
elevated process
```

Administrators are not supposed to run every process elevated all day.

### 20. Service Accounts

Possible Windows service identities:

```text
LocalSystem
LocalService
NetworkService
local account
domain service account
gMSA in AD environment
```

Inspect:

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, StartName, State |
    Sort-Object StartName
```

Security rule:

```text
service requires X
      ↓
grant X
      ↓
do not grant full Administrator rights without need
```

---

# Part 6 — NTFS Permissions

### 21. ACL Model

```text
D:\Data
  |
  +-- ACE: Administrators = FullControl
  +-- ACE: Operations    = Modify
  +-- ACE: Users         = Read
```

Inspect:

```powershell
Get-Acl D:\Data | Format-List
```

Command-line:

```cmd
icacls D:\Data
```

### 22. Permission Levels

Conceptual hierarchy:

```text
Full Control
    |
Modify
    |
Read & Execute
    |
Read
```

Do not think only in names. Ask what the user must do:

```text
read?
create?
modify?
delete?
execute?
change permissions?
take ownership?
```

### 23. Inheritance

```text
D:\Data [ACL]
   |
   +-- Finance [inherits]
       |
       +-- Report.xlsx [inherits]
```

Inspect:

```powershell
(Get-Acl D:\Data).Access |
    Select-Object IdentityReference,
                  FileSystemRights,
                  IsInherited
```

Inheritance makes ACL administration scalable.

### 24. Explicit Deny

Design preference:

```text
clear Allow group model
      ↓
few special Deny entries
```

Excessive Deny rules create difficult effective-permission troubleshooting.

### 25. Ownership

The owner of an object has special control over permission management.

Inspect:

```powershell
(Get-Acl D:\Data).Owner
```

Changing ownership is a high-privilege administrative operation.

---

# Part 7 — Windows Storage

### 26. Storage Layers

```text
Physical / Virtual Disk
        ↓
Partition Table
 GPT / MBR
        ↓
Partition
        ↓
Volume
        ↓
Filesystem
 NTFS / ReFS
        ↓
Drive Letter / Mount Point
```

Inspect:

```powershell
Get-Disk
Get-Partition
Get-Volume
```

### 27. Initialize a Disposable Lab Disk

**Verify the disk first.**

```powershell
Get-Disk
```

If Disk 1 is definitely the empty lab disk:

```powershell
Initialize-Disk `
    -Number 1 `
    -PartitionStyle GPT

New-Partition `
    -DiskNumber 1 `
    -UseMaximumSize `
    -DriveLetter D

Format-Volume `
    -DriveLetter D `
    -FileSystem NTFS `
    -NewFileSystemLabel "Data"
```

Verify:

```powershell
Get-Disk
Get-Partition -DiskNumber 1
Get-Volume -DriveLetter D
```

Never copy disk numbers from a tutorial without checking your environment.

### 28. GPT vs MBR

```text
MBR
legacy partition scheme

GPT
modern partition scheme
UEFI-oriented systems
large/flexible partitioning
```

Modern Windows Server normally uses GPT unless a specific compatibility need requires otherwise.

### 29. NTFS

NTFS supports broad Windows workload features such as:

```text
ACLs
compression
quotas
encryption capabilities
large volumes/files
alternate data streams
mount points
```

Inspect:

```powershell
Get-Volume |
    Where-Object FileSystem -eq 'NTFS'
```

### 30. ReFS

ReFS is designed around resilience and scale for supported Windows Server workloads.

Mental selection model:

```text
General Windows workload
        ↓
       NTFS

Specific supported resilient workload
        ↓
       ReFS
```

Do not treat ReFS as a universal NTFS replacement.

### 31. Free-space Report

```powershell
Get-Volume |
    Where-Object DriveLetter |
    ForEach-Object {
        [pscustomobject]@{
            Drive      = $_.DriveLetter
            FileSystem = $_.FileSystem
            SizeGB     = [math]::Round($_.Size/1GB,2)
            FreeGB     = [math]::Round($_.SizeRemaining/1GB,2)
        }
    }
```

---

# Part 8 — Storage Spaces

### 32. Storage Spaces Architecture

```text
Physical Disks
 D1  D2  D3  D4
  \   |   |  /
   Storage Pool
        ↓
   Virtual Disk
        ↓
      Volume
```

Inspect:

```powershell
Get-PhysicalDisk
Get-StoragePool
Get-VirtualDisk
```

Do not create pools using disks that contain required data.

### 33. Resiliency Concept

Conceptual layouts can include:

```text
Simple
Mirror
Parity
```

The correct choice depends on:

```text
performance
capacity efficiency
failure tolerance
workload
hardware
```

---

# Part 9 — SMB File Services

### 34. SMB Architecture

```text
Client
   |
 TCP/445
   |
SMB Server
   |
NTFS/ReFS
```

UNC path:

```text
\\WIN-SRV01\Finance
```

### 35. Create a Share

```powershell
New-Item `
    -Path D:\Shares\Finance `
    -ItemType Directory

New-SmbShare `
    -Name "Finance" `
    -Path "D:\Shares\Finance" `
    -FullAccess "Administrators"
```

Inspect:

```powershell
Get-SmbShare
Get-SmbShareAccess -Name Finance
```

### 36. Share Permission + NTFS Permission

Remote file access:

```text
User
 ↓
Share ACL
 ↓
NTFS ACL
 ↓
Effective access
```

A practical design often uses:

```text
Share permissions
    relatively simple

NTFS permissions
    detailed business access model
```

### 37. SMB Session Inspection

```powershell
Get-SmbSession
Get-SmbOpenFile
```

This can help answer:

```text
Who is connected?
From where?
Which files are open?
```

### 38. SMB Security

Security layers can include:

```text
Kerberos/NTLM authentication
SMB signing
SMB encryption
share ACL
NTFS ACL
firewall
network segmentation
```

Inspect server settings:

```powershell
Get-SmbServerConfiguration
```

### 39. FSRM

File Server Resource Manager can support:

```text
quotas
file screening
storage reports
classification
```

Install:

```powershell
Install-WindowsFeature `
    FS-Resource-Manager `
    -IncludeManagementTools
```

---

# Part 10 — Services and Processes

### 40. Service Lifecycle

```text
Installed
   ↓
Startup Type
   ↓
Running / Stopped
   ↓
Function / Socket
```

Commands:

```powershell
Get-Service
Get-Service W32Time

Start-Service W32Time
Restart-Service W32Time
```

Configure startup:

```powershell
Set-Service W32Time -StartupType Automatic
```

### 41. Troubleshoot Service Failure

```powershell
Get-Service <ServiceName>

Get-WinEvent `
    -FilterHashtable @{
        LogName='System'
        ProviderName='Service Control Manager'
    } `
    -MaxEvents 30
```

Don't restart repeatedly before reading evidence.

### 42. Processes

```powershell
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 10 Name, Id, CPU, WorkingSet
```

Stop a lab process:

```powershell
Stop-Process -Id <PID>
```

A service-managed process may be recreated automatically if the service remains configured to run.

---

# Part 11 — Task Scheduler

### 43. Task Architecture

```text
Trigger
  ↓
Task Scheduler
  ↓
Action
  ↓
Executable / PowerShell
  ↓
Run-as identity
```

Task components:

- trigger
- action
- principal
- conditions
- settings

### 44. Scheduled PowerShell Script

```powershell
$Action = New-ScheduledTaskAction `
    -Execute "PowerShell.exe" `
    -Argument '-NoProfile -File C:\Admin\Health.ps1'

$Trigger = New-ScheduledTaskTrigger `
    -Daily `
    -At 6am

Register-ScheduledTask `
    -TaskName "DailyHealth" `
    -Action $Action `
    -Trigger $Trigger `
    -Description "Daily server health report"
```

Verify:

```powershell
Get-ScheduledTask -TaskName DailyHealth
```

---

# Part 12 — Event Viewer and Event Logs

### 45. Major Logs

```text
Application
Security
System
Setup
Forwarded Events
role-specific operational logs
```

Architecture:

```text
OS / Service / Application
          ↓
       Event Log
          ↓
Event Viewer / PowerShell / SIEM
```

### 46. Get-WinEvent

```powershell
Get-WinEvent `
    -LogName System `
    -MaxEvents 20
```

Errors:

```powershell
Get-WinEvent `
    -FilterHashtable @{
        LogName='System'
        Level=2
    } `
    -MaxEvents 20
```

### 47. Save Evidence

```powershell
Get-WinEvent `
    -LogName System `
    -MaxEvents 200 |
    Export-Csv `
        C:\Admin\SystemEvents.csv `
        -NoTypeInformation
```

Evidence can disappear after rotation/reboots, so capture important data early.

---

# Part 13 — Registry Foundations

### 48. Registry Model

```text
Registry
  |
  +-- HKEY_LOCAL_MACHINE
  |       machine-wide configuration
  |
  +-- HKEY_CURRENT_USER
          current-user configuration
```

PowerShell provider:

```powershell
Get-PSDrive -PSProvider Registry
```

### 49. Read Registry Values

```powershell
Get-ItemProperty `
    'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' |
    Select-Object ProductName, CurrentBuild
```

Before registry changes:

```text
understand value
   ↓
document current state
   ↓
backup/export if appropriate
   ↓
make minimum change
   ↓
verify
```

Avoid random registry "tweaks."

---

# Part 14 — Windows Networking

### 50. Networking Stack

```text
Application
   ↓
TCP / UDP
   ↓
IPv4 / IPv6
   ↓
NIC
   ↓
Switch
   ↓
Router
```

Use the same layer-by-layer reasoning learned in Phase 4.

### 51. Adapter and IP Inspection

```powershell
Get-NetAdapter
Get-NetIPAddress
Get-NetIPConfiguration
```

Useful report:

```powershell
Get-NetIPConfiguration |
    Select-Object `
        InterfaceAlias,
        IPv4Address,
        IPv4DefaultGateway,
        DNSServer
```

### 52. Static IPv4

**Use a lab NIC/console access.**

```powershell
New-NetIPAddress `
    -InterfaceAlias "Ethernet" `
    -IPAddress 10.60.0.10 `
    -PrefixLength 24 `
    -DefaultGateway 10.60.0.1
```

DNS:

```powershell
Set-DnsClientServerAddress `
    -InterfaceAlias "Ethernet" `
    -ServerAddresses 10.60.0.11
```

Verify:

```powershell
Get-NetIPConfiguration
```

### 53. Routes

```powershell
Get-NetRoute -AddressFamily IPv4 |
    Sort-Object DestinationPrefix
```

Lab route:

```powershell
New-NetRoute `
    -DestinationPrefix "10.70.0.0/24" `
    -InterfaceAlias "Ethernet" `
    -NextHop "10.60.0.1"
```

Visual:

```text
WIN-SRV01
10.60.0.10
    |
10.60.0.1
    |
10.70.0.0/24
```

### 54. Network Diagnostics

```powershell
Test-Connection 10.60.0.1

Resolve-DnsName example.com

Test-NetConnection 10.60.0.11 -Port 53

Get-NetTCPConnection -State Listen
```

Important:

```text
Ping works
≠
TCP application works
```

Use `Test-NetConnection -Port`.

---

# Part 15 — DNS Server

### 55. DNS Role

```text
Client
  |
  | query srv01.lab.example
  v
DNS Server
  |
  | A = 10.60.0.10
  v
Client uses IP
```

Install:

```powershell
Install-WindowsFeature DNS -IncludeManagementTools
```

### 56. Forward and Reverse Lookup

```text
Forward:
name -> IP

Reverse:
IP -> name
```

Primary lab zone:

```powershell
Add-DnsServerPrimaryZone `
    -Name "lab.example" `
    -ZoneFile "lab.example.dns"
```

### 57. A Record

```powershell
Add-DnsServerResourceRecordA `
    -ZoneName "lab.example" `
    -Name "srv01" `
    -IPv4Address "10.60.0.10"
```

Test:

```powershell
Resolve-DnsName `
    srv01.lab.example `
    -Server 10.60.0.10
```

### 58. CNAME

Concept:

```text
srv01.lab.example -> A -> 10.60.0.10
files.lab.example -> CNAME -> srv01.lab.example
```

Aliases should represent actual naming requirements.

### 59. DNS Troubleshooting

```powershell
Get-DnsClientServerAddress
Get-DnsServerZone

Get-DnsServerResourceRecord `
    -ZoneName "lab.example"

Resolve-DnsName srv01.lab.example
```

Flow:

```text
Correct resolver?
   ↓
Resolver reachable?
   ↓
Zone exists?
   ↓
Record exists?
   ↓
Record value correct?
```

---

# Part 16 — DHCP Server

### 60. DHCP DORA

```text
Client                   Server

Discover  -------------->
          <-------------- Offer
Request   -------------->
          <-------------- Ack
```

Mnemonic:

```text
D O R A
```

### 61. Install DHCP

```powershell
Install-WindowsFeature DHCP -IncludeManagementTools
```

In a domain, DHCP authorization becomes an AD-integrated concern.

### 62. Create IPv4 Scope

```powershell
Add-DhcpServerv4Scope `
    -Name "Lab Clients" `
    -StartRange 10.60.0.100 `
    -EndRange 10.60.0.199 `
    -SubnetMask 255.255.255.0
```

### 63. Scope Options

```powershell
Set-DhcpServerv4OptionValue `
    -ScopeId 10.60.0.0 `
    -Router 10.60.0.1 `
    -DnsServer 10.60.0.11 `
    -DnsDomain "lab.example"
```

### 64. Leases

```powershell
Get-DhcpServerv4Scope

Get-DhcpServerv4Lease `
    -ScopeId 10.60.0.0
```

Client:

```cmd
ipconfig /release
ipconfig /renew
ipconfig /all
```

---

# Part 17 — Windows Defender Firewall

### 65. Profiles

```text
Domain
Private
Public
```

Inspect:

```powershell
Get-NetFirewallProfile
```

### 66. Rules

```powershell
Get-NetFirewallRule |
    Where-Object Enabled -eq 'True' |
    Select-Object -First 20 `
        DisplayName, Direction, Action
```

Lab rule:

```powershell
New-NetFirewallRule `
    -DisplayName "Lab TCP 8080" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 8080 `
    -Action Allow
```

Remove:

```powershell
Remove-NetFirewallRule `
    -DisplayName "Lab TCP 8080"
```

### 67. Firewall Troubleshooting

```text
Process?
  ↓
Socket?
  ↓
Firewall?
  ↓
Route?
  ↓
Remote client?
```

Commands:

```powershell
Get-NetTCPConnection -State Listen
Get-NetFirewallProfile
Test-NetConnection <server> -Port <port>
```

---

# Part 18 — Windows Update and Servicing

### 68. Patch Management Workflow

```text
Inventory
  ↓
Review updates
  ↓
Test
  ↓
Backup / rollback plan
  ↓
Maintenance
  ↓
Install
  ↓
Reboot if required
  ↓
Health verification
```

Enterprise environments can use centralized update-management platforms.

### 69. Installed Update History

```powershell
Get-HotFix |
    Sort-Object InstalledOn -Descending |
    Select-Object -First 20
```

OS build:

```powershell
Get-ComputerInfo |
    Select-Object `
        WindowsProductName,
        WindowsVersion,
        OsBuildNumber
```

---

# Part 19 — Remote Administration

### 70. WinRM / PowerShell Remoting

Architecture:

```text
Admin Workstation
      |
PowerShell
      |
WS-Management / WinRM
      |
Remote Server
```

Enable in a controlled lab when required:

```powershell
Enable-PSRemoting -Force
```

Test:

```powershell
Test-WSMan WIN-SRV01
```

### 71. Invoke-Command

```powershell
Invoke-Command `
    -ComputerName WIN-SRV01 `
    -ScriptBlock {
        Get-Service W32Time
    }
```

Multiple servers:

```powershell
Invoke-Command `
    -ComputerName WIN-SRV01,WIN-SRV02 `
    -ScriptBlock {
        hostname
        Get-Uptime
    }
```

### 72. Interactive Remoting

```powershell
Enter-PSSession `
    -ComputerName WIN-SRV01

hostname
Get-Service

Exit-PSSession
```

In a correctly designed AD environment, DNS and Kerberos simplify secure remote administration.

### 73. RDP

```text
Admin PC
   |
 RDP
   |
Server
```

Security practices:

- Network Level Authentication
- restrict firewall sources
- VPN/RD Gateway or privileged-access architecture
- strong identity controls
- avoid direct Internet exposure

Do **not** expose TCP/3389 directly to the public Internet.

---

# Part 20 — Hyper-V

### 74. Hyper-V Architecture

```text
Hardware
   ↓
Hyper-V Hypervisor
   ↓
+------------------------+
| Root/Management        |
| Partition              |
+------------------------+
| VM1 | VM2 | VM3        |
+------------------------+
```

Hyper-V can run supported Windows and Linux guests.

### 75. Requirements Check

```cmd
systeminfo.exe
```

On a supported server:

```powershell
Install-WindowsFeature `
    -Name Hyper-V `
    -IncludeManagementTools `
    -Restart
```

Verify:

```powershell
Get-WindowsFeature Hyper-V
```

### 76. Virtual Switches

```text
External
VM ↔ physical network

Internal
VM ↔ host + other VMs

Private
VM ↔ VM
```

Inspect:

```powershell
Get-VMSwitch
```

Create:

```powershell
New-VMSwitch `
    -Name "LabInternal" `
    -SwitchType Internal
```

### 77. Generation 1 vs 2

```text
Generation 1
legacy compatibility

Generation 2
UEFI
Secure Boot capability
modern virtual hardware
```

For modern supported guest OSes, Generation 2 is normally preferred.

### 78. Create VM

```powershell
New-VM `
    -Name "LabVM01" `
    -Generation 2 `
    -MemoryStartupBytes 2GB `
    -NewVHDPath "D:\VMs\LabVM01\LabVM01.vhdx" `
    -NewVHDSizeBytes 40GB `
    -SwitchName "LabInternal"
```

Inspect:

```powershell
Get-VM
Get-VMNetworkAdapter -VMName LabVM01
Get-VHD "D:\VMs\LabVM01\LabVM01.vhdx"
```

### 79. Checkpoints

```powershell
Checkpoint-VM `
    -Name LabVM01 `
    -SnapshotName "BeforeLab"

Get-VMSnapshot -VMName LabVM01
```

Checkpoint:

```text
fast state rollback
```

Backup:

```text
recoverable protected copy
retention
restore workflow
```

They are not the same.

---

# Part 21 — Backup and Recovery

### 80. Backup Design

Ask:

```text
What data?
How frequently?
Where stored?
How long retained?
Encrypted?
Offline/immutable copy?
Restore tested?
RPO?
RTO?
```

### 81. Windows Server Backup

Install:

```powershell
Install-WindowsFeature Windows-Server-Backup
```

Verify:

```powershell
Get-WindowsFeature Windows-Server-Backup
```

Production environments may use another enterprise backup platform.

The important skill is recovery design and restore testing.

---

# Part 22 — Performance Monitoring

### 82. Four Main Resource Layers

```text
CPU
Memory
Disk
Network
```

Then:

```text
application-specific metrics
```

### 83. Performance Counters

```powershell
Get-Counter `
    '\Processor(_Total)\% Processor Time'
```

Memory:

```powershell
Get-Counter `
    '\Memory\Available MBytes'
```

Disk latency:

```powershell
Get-Counter `
    '\PhysicalDisk(_Total)\Avg. Disk sec/Transfer'
```

Sample:

```powershell
Get-Counter `
    '\Processor(_Total)\% Processor Time' `
    -SampleInterval 2 `
    -MaxSamples 5
```

### 84. Performance Monitor

Launch:

```powershell
perfmon.msc
```

It provides:

```text
live counters
Data Collector Sets
historical collection
reports
```

Historical evidence is critical for intermittent performance incidents.

---

# Part 23 — Security Foundations

### 85. Reduce Attack Surface

```text
fewer roles
   ↓
fewer services
   ↓
fewer ports
   ↓
less attack/maintenance surface
```

Inspect:

```powershell
Get-WindowsFeature |
    Where-Object InstallState -eq 'Installed'

Get-Service |
    Where-Object Status -eq 'Running'

Get-NetTCPConnection -State Listen
```

### 86. Security Baselines

Microsoft security baselines are starting points, not universal one-click answers.

```text
Microsoft baseline
      ↓
risk assessment
      ↓
application compatibility
      ↓
approved organizational baseline
```

### 87. Defender State

Where Microsoft Defender Antivirus is present:

```powershell
Get-MpComputerStatus |
    Select-Object `
        AntivirusEnabled,
        RealTimeProtectionEnabled
```

Enterprise environments may use other endpoint-security platforms.

### 88. Least Privilege

Bad:

```text
many local admins
services as LocalSystem
broad SMB rights
open firewall
```

Better:

```text
role-based groups
specific service identity
minimal NTFS/share permissions
required firewall rules
auditing
```

---

# Part 24 — Troubleshooting Methodology

### 89. Evidence-first Workflow

```text
1. Define symptom
2. Determine scope
3. Identify recent change
4. Map architecture
5. Collect evidence
6. Form one hypothesis
7. Test minimally
8. Verify result
9. Document
```

### 90. Network Failure

```powershell
Get-NetAdapter
Get-NetIPConfiguration
Get-NetRoute -AddressFamily IPv4

Test-Connection 10.60.0.1
Resolve-DnsName example.com
Test-NetConnection example.com -Port 443
```

Flow:

```text
NIC
 ↓
IP
 ↓
route
 ↓
DNS
 ↓
TCP
 ↓
application
```

### 91. Service Not Reachable

```powershell
Get-Service <ServiceName>
Get-NetTCPConnection -State Listen
Get-NetFirewallProfile
Test-NetConnection localhost -Port <port>
```

This separates:

```text
service failure
from
firewall/network failure
```

### 92. Disk Full

```powershell
Get-Volume |
    Select-Object DriveLetter, Size, SizeRemaining
```

Potential sources:

```text
logs
backups
temp data
application data
VM disks
updates
```

### 93. Health-report Script

```powershell
$OS = Get-CimInstance Win32_OperatingSystem

$Report = [ordered]@{
    ComputerName = $env:COMPUTERNAME
    Time = Get-Date
    OS = $OS.Caption
    Uptime = (Get-Date) - $OS.LastBootUpTime
    IPv4 = (
        Get-NetIPAddress -AddressFamily IPv4 |
        Where-Object IPAddress -notlike '169.254*'
    ).IPAddress
    FailedAutoServices = (
        Get-Service |
        Where-Object {
            $_.StartType -eq 'Automatic' -and
            $_.Status -ne 'Running'
        }
    ).Name
}

[pscustomobject]$Report |
    Format-List
```

This converts many administration concepts into one repeatable diagnostic.

---


# Enhanced Deep-Study Layer — Windows Server Infrastructure Engineering

The original course is preserved below. This enhanced layer adds a deeper operating-system model, PowerShell automation patterns, Windows boot/service internals, identity and privilege concepts, NTFS/SMB security, storage engineering, DNS/DHCP, firewalling, WinRM/remote administration, Hyper-V, backup/recovery, observability, hardening, troubleshooting, and production-style labs.

The core mental model is:

```text
Requirement
    ↓
Windows configuration surface
    ↓
Registry / policy / role configuration / API
    ↓
Windows service or kernel subsystem
    ↓
Runtime process / socket / storage / identity state
    ↓
Client-visible behavior
    ↓
Event logs + metrics + verification
```

A good Windows administrator should always be able to answer:

```text
What state do I want?
Where is that state stored?
Which Windows component consumes it?
What proves the configuration is active?
Will it survive reboot?
What logs prove success or failure?
How do I roll it back?
```

---

## Enhanced Deep Dive 1 — Windows User Mode vs Kernel Mode

A simplified architecture:

```text
Applications
PowerShell
Server roles
Windows services
        ↓
User Mode
--------------------------------
Kernel Mode
        ↓
Windows Executive
Kernel
Device drivers
Hardware abstraction
        ↓
CPU / Memory / Devices
```

Why the distinction matters:

```text
user-mode process crash
→ usually one process/service fails

kernel-mode driver failure
→ can destabilize or crash the whole OS
```

This is why driver quality and signed/approved drivers matter on infrastructure servers.

---

## Enhanced Deep Dive 2 — Windows Executive Components

Important kernel-side concepts include:

```text
Object Manager
I/O Manager
Memory Manager
Process/Thread Manager
Security Reference Monitor
Configuration Manager
Plug and Play Manager
```

You do not administer these directly every day, but they explain why Windows exposes:

```text
handles
security descriptors
registry
processes
threads
drivers
I/O requests
```

These are operating-system abstractions, not random management terms.

---

## Enhanced Deep Dive 3 — Registry as Configuration Database

The Registry is not one file.

Conceptually:

```text
HKLM
├── SYSTEM
├── SOFTWARE
├── SAM
├── SECURITY
└── other machine hives

HKCU
→ per-user settings
```

The registry provider lets PowerShell treat keys like paths:

```powershell
Get-ChildItem HKLM:\SOFTWARE

Get-ItemProperty `
  'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
```

A registry change may require:

```text
service restart
logoff/logon
policy refresh
or reboot
```

depending on the consumer.

---

## Enhanced Deep Dive 4 — Boot Process Mental Model

Modern boot path:

```text
UEFI firmware
    ↓
Windows Boot Manager
    ↓
BCD configuration
    ↓
Windows loader
    ↓
Kernel + boot drivers
    ↓
Session Manager
    ↓
Service Control Manager
    ↓
services / logon
```

Useful commands:

```cmd
bcdedit /enum
```

PowerShell:

```powershell
Get-ComputerInfo |
  Select-Object BiosFirmwareType, CsBootupState
```

Do not edit BCD casually on production servers.

---

## Enhanced Deep Dive 5 — Safe Mode and Recovery Environment

Recovery options can include:

```text
Windows Recovery Environment
Startup Repair
Command Prompt
Safe Mode
System Image Recovery
```

The purpose is to recover when:

```text
driver
service
boot configuration
update
filesystem
```

prevents normal startup.

Infrastructure design should include console or out-of-band access before a boot incident happens.

---

## Enhanced Deep Dive 6 — Server Core as an Operational Model

Server Core reduces local GUI components.

Think:

```text
Server Core
    ↓
smaller local interaction surface
    ↓
remote-first administration
    ↓
PowerShell / WAC / MMC / RSAT
```

Benefits can include:

```text
fewer installed GUI components
less local interactive administration
potentially smaller servicing/attack surface
```

But it demands stronger automation and remote-management skills.

---

## Enhanced Deep Dive 7 — Roles, Features, Services, Processes

These are different layers.

```text
Windows Feature / Role
      ↓ installs capability
Windows Service
      ↓ lifecycle entry
Process
      ↓ actual executable instance
Socket / file / API
      ↓ client-visible function
```

Example:

```text
DNS role installed
≠
DNS service running
≠
UDP/TCP 53 listening correctly
≠
zone answering correctly
```

Verify each layer independently.

---

## Enhanced Deep Dive 8 — Service Control Manager

SCM manages Windows services.

Useful tools:

```powershell
Get-Service
Get-CimInstance Win32_Service
```

Traditional:

```cmd
sc.exe query
sc.exe qc DNS
```

A service definition includes:

```text
binary path
startup type
service account
dependencies
recovery behavior
```

A process is runtime. A service is a managed lifecycle definition.

---

## Enhanced Deep Dive 9 — Service Startup Types

Common:

```text
Automatic
Automatic (Delayed Start)
Manual
Disabled
```

Do not assume:

```text
Manual = never starts
```

A dependency, trigger, or explicit start can launch a manual service.

Use:

```powershell
Get-CimInstance Win32_Service |
  Select-Object Name, StartMode, State
```

---

## Enhanced Deep Dive 10 — Service Dependencies

Inspect:

```powershell
Get-Service -Name DNS |
  Select-Object -ExpandProperty ServicesDependedOn
```

and:

```powershell
Get-Service -Name DNS |
  Select-Object -ExpandProperty DependentServices
```

Troubleshooting:

```text
service fails
  ↓
dependency unavailable?
  ↓
service account?
  ↓
config?
  ↓
binary?
  ↓
port collision?
  ↓
event log?
```

---

## Enhanced Deep Dive 11 — Service Recovery Actions

Some services can restart automatically after failure.

Inspect with service configuration tools or GUI.

The distinction:

```text
restart service
≠
fix root cause
```

Automatic recovery is useful for transient failures but can hide repeated crashes unless monitoring detects them.

---

## Enhanced Deep Dive 12 — PowerShell Object Pipeline

PowerShell moves .NET objects, not merely screen text.

```powershell
Get-Service |
  Where-Object Status -eq 'Running' |
  Sort-Object DisplayName |
  Select-Object Name, DisplayName, Status
```

Pipeline:

```text
ServiceController objects
      ↓ filter
ServiceController objects
      ↓ sort
ServiceController objects
      ↓ projection
custom output objects
```

This allows robust automation without parsing human-formatted output.

---

## Enhanced Deep Dive 13 — Get-Member and Discoverability

Use:

```powershell
Get-Service | Get-Member

Get-NetIPConfiguration | Get-Member
```

Ask:

```text
What type of object?
Which properties?
Which methods?
```

Do not guess property names.

---

## Enhanced Deep Dive 14 — PowerShell Help Discipline

Workflow:

```powershell
Get-Command *SmbShare*

Get-Help New-SmbShare -Full

Get-Help New-SmbShare -Examples
```

This is safer than copying a command from another Windows version without checking available parameters.

---

## Enhanced Deep Dive 15 — Select-Object Calculated Properties

Example:

```powershell
Get-Volume |
  Where-Object DriveLetter |
  Select-Object DriveLetter,
    FileSystemLabel,
    @{N='SizeGB';E={[math]::Round($_.Size/1GB,2)}},
    @{N='FreeGB';E={[math]::Round($_.SizeRemaining/1GB,2)}}
```

Calculated properties make reporting readable while preserving structured data.

---

## Enhanced Deep Dive 16 — PSCustomObject for Health Data

```powershell
[pscustomobject]@{
    Computer = $env:COMPUTERNAME
    Time     = Get-Date
    Uptime   = (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
}
```

This is preferable to concatenated strings if data will later be:

```text
exported
filtered
converted to JSON
sent to API
compared
```

---

## Enhanced Deep Dive 17 — Error Handling

PowerShell distinguishes non-terminating and terminating errors.

Example:

```powershell
try {
    Get-Item 'C:\DefinitelyMissing' -ErrorAction Stop
}
catch {
    Write-Error "Required path is unavailable: $($_.Exception.Message)"
}
```

Administration scripts should fail clearly rather than silently continue after critical failures.

---

## Enhanced Deep Dive 18 — `$ErrorActionPreference`

Global behavior can be changed:

```powershell
$ErrorActionPreference = 'Stop'
```

But use deliberately.

A production script should understand which failures:

```text
must stop
can be logged and continued
are expected conditions
```

---

## Enhanced Deep Dive 19 — PowerShell Logging

A simple structured log:

```powershell
function Write-Log {
    param(
        [string]$Message,
        [ValidateSet('INFO','WARN','ERROR')]
        [string]$Level = 'INFO'
    )

    "{0:u} [{1}] {2}" -f (Get-Date), $Level, $Message |
      Add-Content C:\Admin\server-admin.log
}
```

For mature environments, prefer centralized logging rather than local files only.

---

## Enhanced Deep Dive 20 — Idempotent PowerShell Thinking

Bad:

```powershell
New-Item C:\Admin -ItemType Directory
```

can fail if it already exists.

Better:

```powershell
if (-not (Test-Path C:\Admin)) {
    New-Item C:\Admin -ItemType Directory | Out-Null
}
```

Infrastructure automation should aim for:

```text
run once → desired state
run again → same desired state
```

This connects directly to later configuration-management tools.

---

## Enhanced Deep Dive 21 — Desired State Configuration Awareness

PowerShell DSC expresses desired configuration rather than imperative click-by-click actions.

Mental model:

```text
desired configuration
      ↓
DSC resource
      ↓
compare current state
      ↓
change only drift
```

Even if you do not deploy DSC yet, learn desired-state thinking because it transfers to:

```text
Ansible
Terraform
Intune
Azure Automation
configuration baselines
```

---

## Enhanced Deep Dive 22 — Local Security Principal Model

Windows authorization uses SIDs.

```text
Account name
   ↓ resolves to
SID
   ↓
access token
   ↓
ACL comparison
```

Rename:

```text
OpsUser
→ OperationsUser
```

does not normally change the SID.

ACLs authorize the SID, not the display text.

---

## Enhanced Deep Dive 23 — Access Token

At logon, Windows creates an access token containing:

```text
user SID
group SIDs
privileges
integrity level
restrictions
```

When accessing a resource:

```text
token
  ↓
security descriptor
  ↓
DACL evaluation
  ↓
allow/deny
```

Group membership changes may not affect an existing logon token until a new logon/session occurs.

---

## Enhanced Deep Dive 24 — UAC Split Token

Administrator logon can produce:

```text
standard filtered token
+
elevated administrative token
```

Normal applications use the standard token.

Elevation requests use UAC to launch an elevated process.

This reduces accidental privileged execution, but UAC is not a substitute for least-privilege account design.

---

## Enhanced Deep Dive 25 — Privileges vs Permissions

Permissions apply to objects:

```text
file
registry key
service
share
```

Privileges are system-level rights:

```text
back up files
restore files
debug programs
shut down system
```

Inspect user rights primarily through security policy tools, not NTFS ACLs.

Do not confuse:

```text
Modify on a file
```

with:

```text
SeBackupPrivilege
```

---

## Enhanced Deep Dive 26 — NTFS Security Descriptor

A file security descriptor can contain:

```text
Owner
DACL
SACL
control information
```

DACL:

```text
who is allowed/denied
```

SACL:

```text
what access should be audited
```

Inspect:

```powershell
Get-Acl D:\Data | Format-List
```

---

## Enhanced Deep Dive 27 — ACE Ordering and Effective Access

An ACL contains Access Control Entries.

Conceptually:

```text
explicit deny
explicit allow
inherited deny
inherited allow
```

Windows canonical ordering has rules, but effective permission can still be complex due to:

```text
multiple group memberships
inheritance
deny entries
share permissions
privileges
ownership
```

Prefer group-based allow models over many direct user exceptions.

---

## Enhanced Deep Dive 28 — NTFS Inheritance

Parent:

```text
D:\Departments
   ↓ inherited ACL
Finance
   ↓ inherited ACL
Reports
```

Inheritance reduces duplicated permission administration.

Breaking inheritance is sometimes necessary but creates another unique ACL to maintain.

Document every inheritance break.

---

## Enhanced Deep Dive 29 — `icacls` as a Diagnostic Tool

Inspect:

```cmd
icacls D:\Departments\Finance
```

Save ACLs:

```cmd
icacls D:\Departments /save C:\Admin\finance-acl.txt /t
```

Restore procedures should be tested in lab before relying on them.

Do not use broad reset operations against production directories without understanding inherited/explicit permissions.

---

## Enhanced Deep Dive 30 — Share Permissions vs NTFS

Remote SMB access requires both.

```text
Share ACL
    AND
NTFS ACL
    ↓
effective remote access
```

Example:

```text
Share = Read
NTFS = Modify
→ remote user effectively cannot modify through that share
```

Local access:

```text
NTFS only
```

This difference explains many "works locally, fails remotely" incidents.

---

## Enhanced Deep Dive 31 — SMB Authentication Path

Domain environment:

```text
Client
   ↓ DNS
Server name
   ↓
Kerberos if conditions satisfied
or NTLM fallback
   ↓
SMB session
   ↓
share ACL
   ↓
NTFS ACL
```

Using server IP instead of hostname can affect Kerberos behavior because SPN/name expectations change.

---

## Enhanced Deep Dive 32 — SMB Signing

SMB signing helps protect integrity/authenticity of SMB messages.

Concept:

```text
message
+
cryptographic signature
→ tamper detection
```

Security policy must consider:

```text
server requirements
client compatibility
performance
domain policy
```

Do not disable signing merely to fix a legacy client without assessing risk.

---

## Enhanced Deep Dive 33 — SMB Encryption

SMB encryption protects file traffic confidentiality/integrity across the network.

It can be configured at appropriate server/share levels depending on environment.

Use when:

```text
sensitive data crosses less-trusted networks
compliance requires transport encryption
```

Do not confuse SMB encryption with BitLocker disk encryption.

---

## Enhanced Deep Dive 34 — SMB Continuous Availability Awareness

In clustered/advanced designs, SMB can support capabilities for highly available file workloads.

At this stage, remember:

```text
ordinary file share
≠
clustered continuously available file service
```

HA behavior requires an architecture supporting it.

---

## Enhanced Deep Dive 35 — NTFS vs ReFS

Simplified:

```text
NTFS
→ broad compatibility/features
→ general Windows workload

ReFS
→ resilience/scale features for supported workloads
```

Do not choose ReFS because it sounds newer.

Ask:

```text
feature compatibility?
application support?
backup support?
boot volume?
deduplication requirements?
Hyper-V workload?
```

---

## Enhanced Deep Dive 36 — Alternate Data Streams Awareness

NTFS can store named streams.

PowerShell can inspect streams:

```powershell
Get-Item -Path C:\Temp\file.txt -Stream *
```

Security relevance:

```text
additional data can exist beyond normal unnamed stream
```

Do not assume visible file size/content tells the whole NTFS object story.

---

## Enhanced Deep Dive 37 — EFS vs BitLocker

EFS:

```text
file-level encryption tied to user certificates/keys
```

BitLocker:

```text
volume-level encryption
```

These solve different problems.

BitLocker protects data at rest when the disk is offline/stolen.

Once Windows is running and the volume unlocked, normal ACLs still control access.

---

## Enhanced Deep Dive 38 — BitLocker Server Awareness

Before enabling on infrastructure:

```text
TPM/platform support
recovery-key escrow
boot/recovery procedures
cluster/storage support
backup integration
```

Do not enable disk encryption without verified recovery keys.

A locked server with no recovery material is an availability incident.

---

## Enhanced Deep Dive 39 — Storage Device Identity

Before destructive storage operations:

```powershell
Get-Disk |
  Select-Object Number, FriendlyName, SerialNumber, Size, PartitionStyle, OperationalStatus
```

Verify:

```text
disk number
model
serial
capacity
partition state
```

Disk numbers are not stable business identity.

Do not copy `Disk 1` from a tutorial.

---

## Enhanced Deep Dive 40 — GPT Layers

```text
physical/virtual disk
   ↓
GPT
   ↓
partition
   ↓
volume
   ↓
filesystem
   ↓
drive letter / mount path
```

Each step is separate.

A new partition is not yet a formatted filesystem.

A formatted volume is not necessarily shared over SMB.

---

## Enhanced Deep Dive 41 — Mount Points Instead of Drive Letters

Windows can mount a volume into an NTFS folder path.

Concept:

```text
C:\Data\Archive
      ↓ mount point
separate volume
```

This can help environments that would otherwise exhaust drive letters or want application-specific storage paths.

Always document the underlying volume mapping.

---

## Enhanced Deep Dive 42 — Storage Spaces Resiliency

Simplified layouts:

```text
Simple
→ performance/capacity, no redundancy

Mirror
→ duplicate data

Parity
→ parity-protected capacity
```

Real performance/rebuild behavior depends on:

```text
disk count
media type
column layout
workload
cache
failure count
```

Do not use a resiliency name as a performance guarantee.

---

## Enhanced Deep Dive 43 — Storage Spaces Direct Awareness

Storage Spaces Direct combines local storage from multiple servers in supported clustered architectures.

Concept:

```text
Server1 local disks
Server2 local disks
Server3 local disks
       ↓
clustered storage pool
       ↓
resilient virtual disks/volumes
```

This is an advanced HA/storage topic, not the same as single-server Storage Spaces.

---

## Enhanced Deep Dive 44 — VSS

Volume Shadow Copy Service coordinates snapshots with applications/providers.

Uses:

```text
backup consistency
shadow copies
application-aware backup workflows
```

VSS is not itself a full backup policy.

A snapshot on the same storage can disappear with storage loss.

---

## Enhanced Deep Dive 45 — File Server Resource Manager

FSRM can provide:

```text
quotas
file screening
classification
storage reports
```

Example quota policy idea:

```text
Department share
  ↓
hard or soft quota
  ↓
threshold notifications
```

Quotas should be paired with monitoring and business ownership.

---

## Enhanced Deep Dive 46 — DNS Resolver vs DNS Server

Client resolver configuration:

```powershell
Get-DnsClientServerAddress
```

Server role:

```powershell
Get-DnsServerZone
```

These are different.

A server can host DNS zones while its own NIC resolver is misconfigured.

In AD environments, DNS client design becomes especially important.

---

## Enhanced Deep Dive 47 — Recursive Resolution

Concept:

```text
Client
  ↓ query
local DNS server
  ↓ if not authoritative/cached
forwarder/root process
  ↓
external DNS hierarchy
```

Enterprise DNS often separates:

```text
internal authoritative zones
external recursion/forwarding
```

A domain client should not bypass AD-aware internal DNS for convenience.

---

## Enhanced Deep Dive 48 — DNS Cache

Client:

```powershell
Get-DnsClientCache
Clear-DnsClientCache
```

Server cache behavior also exists.

A corrected DNS record may appear "still wrong" because:

```text
client cache
server cache
TTL
secondary replication
```

must expire/update.

---

## Enhanced Deep Dive 49 — DNS Record Types

Important:

```text
A      IPv4
AAAA   IPv6
CNAME  alias
PTR    reverse
MX     mail
NS     authoritative name server
SRV    service locator
TXT    text/policy use
```

Do not use CNAME where an application/protocol explicitly requires an A/AAAA or where alias behavior has service-specific implications.

---

## Enhanced Deep Dive 50 — DNS TTL

TTL controls caching duration.

Trade-off:

```text
long TTL
→ less query load
→ slower record-change convergence

short TTL
→ faster change propagation
→ more resolver queries
```

Do not lower TTL to near-zero permanently without reason.

---

## Enhanced Deep Dive 51 — DHCP Lease Model

Lease contains:

```text
IP address
client identity
lease duration
scope
options
```

Client lifecycle:

```text
discover
offer
request
ack
↓
lease renewal
```

DHCP configuration should align with:

```text
subnet
router
DNS
domain suffix
reservations
exclusions
```

---

## Enhanced Deep Dive 52 — DHCP Reservations vs Exclusions

Reservation:

```text
specific client identity
→ always receives chosen DHCP address
```

Exclusion:

```text
addresses inside scope
→ never dynamically leased
```

Static infrastructure addresses can be kept outside dynamic ranges or reserved according to design.

---

## Enhanced Deep Dive 53 — DHCP Relay Awareness

DHCP broadcasts normally do not cross routers.

Relay/forwarding allows clients on remote subnets to reach centralized DHCP.

Architecture:

```text
Client subnet
  ↓ broadcast
Router/DHCP relay
  ↓ unicast/forward
DHCP server
```

This is critical in enterprise multi-VLAN design.

---

## Enhanced Deep Dive 54 — Windows Networking Profiles

Firewall profiles:

```text
Domain
Private
Public
```

Profile selection affects enabled rules.

Inspect:

```powershell
Get-NetConnectionProfile
Get-NetFirewallProfile
```

A server unexpectedly in Public profile can behave very differently.

Do not simply disable the firewall; find why the profile is wrong.

---

## Enhanced Deep Dive 55 — Interface Metrics and Route Selection

Windows chooses routes based on prefix match and metrics.

Inspect:

```powershell
Get-NetRoute -AddressFamily IPv4 |
  Sort-Object DestinationPrefix, RouteMetric
```

Also interface metric:

```powershell
Get-NetIPInterface |
  Sort-Object InterfaceMetric
```

Multiple NICs can create unexpected routing if metrics/gateways are poorly designed.

---

## Enhanced Deep Dive 56 — Multi-Homed Server Caution

A server with multiple NICs may have:

```text
client network
backup network
storage network
management network
```

Do not configure multiple default gateways casually.

Multiple default routes can cause asymmetric or unpredictable traffic.

Design routing intentionally.

---

## Enhanced Deep Dive 57 — IPv6 Is Not "Disabled Networking"

Modern Windows uses IPv6 internally in many components.

Do not disable IPv6 across servers as a generic troubleshooting step.

If IPv6 is not used externally, understand Windows support guidance and application dependencies before changing stack behavior.

---

## Enhanced Deep Dive 58 — `Test-NetConnection`

This tests more than ping.

```powershell
Test-NetConnection server01 -Port 445
```

Useful fields:

```text
RemoteAddress
RemotePort
TcpTestSucceeded
InterfaceAlias
SourceAddress
```

This directly tests:

```text
name resolution
route
TCP reachability
```

for the selected target.

---

## Enhanced Deep Dive 59 — Windows Defender Firewall Rule Dimensions

A rule can include:

```text
direction
action
protocol
local port
remote port
local address
remote address
profile
program
service
interface
```

Good rule:

```text
allow required service
from required source
on required profile
```

Bad:

```text
allow all inbound everywhere
```

---

## Enhanced Deep Dive 60 — Firewall Logging

Firewall logs can help diagnose dropped/allowed traffic depending on policy.

Configure in a controlled way and monitor disk usage.

The goal:

```text
prove whether Windows Firewall rejected the packet
```

rather than disabling it and losing the evidence.

---

## Enhanced Deep Dive 61 — WinRM Architecture

```text
PowerShell client
  ↓ WS-Man
WinRM listener
  ↓ authentication
PowerShell endpoint
  ↓ command execution
```

Inspect:

```powershell
winrm enumerate winrm/config/listener
Test-WSMan localhost
```

Domain environments normally benefit from Kerberos-based remoting when DNS/SPNs are correct.

---

## Enhanced Deep Dive 62 — PowerShell Remoting Serialization

Remote objects are often deserialized representations.

Example:

```powershell
Invoke-Command -ComputerName SRV01 {
    Get-Service W32Time
}
```

Returned object may not have every live method of the original remote .NET object.

Think:

```text
remote object
→ serialized data
→ local deserialized representation
```

Use remoting-aware logic rather than assuming local methods always work.

---

## Enhanced Deep Dive 63 — The Double-Hop Problem

Kerberos delegation issue:

```text
Admin
  ↓
ServerA
  ↓
ServerB
```

Credentials delegated to ServerA may not automatically be usable for ServerB.

Solutions depend on architecture:

```text
Kerberos constrained delegation
resource-based constrained delegation
CredSSP in limited scenarios
run command directly against final target
```

Do not "fix" this by embedding passwords in scripts.

---

## Enhanced Deep Dive 64 — JEA Awareness

Just Enough Administration can expose limited PowerShell capabilities.

Model:

```text
operator
  ↓ JEA endpoint
allowed cmdlets/functions only
  ↓
admin task
```

This can reduce the need for broad local Administrator membership.

JEA is an advanced least-privilege administration tool.

---

## Enhanced Deep Dive 65 — RDP Security Model

RDP provides interactive desktop access.

Security principles:

```text
NLA
restricted sources
MFA through surrounding access architecture
RD Gateway/VPN/PAW
session auditing
no direct Internet exposure
```

RDP should not be the only administration method.

---

## Enhanced Deep Dive 66 — Windows Admin Center Trust Boundary

WAC Gateway can manage many servers.

Therefore it becomes a privileged management component.

Protect:

```text
gateway host
TLS certificate
administrator authentication
RBAC where applicable
network access
update state
```

A compromised centralized management gateway can increase blast radius.

---

## Enhanced Deep Dive 67 — Scheduled Task Identity

Task execution depends on:

```text
principal
logon type
privilege level
working directory
environment
credentials
```

"Runs manually, fails scheduled" commonly results from:

```text
different user
different current directory
missing network credentials
missing mapped drive
noninteractive environment
```

Use UNC paths instead of relying on interactive mapped drives.

---

## Enhanced Deep Dive 68 — Scheduled Task Last Result

Inspect:

```powershell
Get-ScheduledTaskInfo -TaskName DailyHealth
```

Useful:

```text
LastRunTime
LastTaskResult
NextRunTime
```

Also review Task Scheduler operational logs when diagnosis requires deeper evidence.

---

## Enhanced Deep Dive 69 — Event Log Channels

Event Viewer includes more than:

```text
System
Application
Security
```

Applications and Windows components expose operational/admin channels.

List:

```powershell
Get-WinEvent -ListLog * |
  Where-Object RecordCount -gt 0 |
  Select-Object -First 30 LogName, RecordCount
```

Use the provider-specific channel when available.

---

## Enhanced Deep Dive 70 — FilterHashtable Performance

Better than pulling all events then filtering.

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'System'
    Level     = 2
    StartTime = (Get-Date).AddHours(-2)
}
```

This asks the event subsystem for only matching events.

---

## Enhanced Deep Dive 71 — Windows Event Forwarding Awareness

Architecture:

```text
Servers
   ↓ subscriptions
Windows Event Collector
   ↓
central event store / SIEM
```

Central collection helps when:

```text
server fails
attacker clears local logs
cross-host timeline needed
```

Security monitoring should not depend only on local Event Viewer.

---

## Enhanced Deep Dive 72 — Sysinternals Toolkit Awareness

Useful diagnostic tools include:

```text
Process Explorer
Process Monitor
Autoruns
TCPView
Sigcheck
Handle
PsExec (authorized administration)
```

Use tools from trusted official sources.

Examples of questions:

```text
Which process opened this file?
Which registry key is failing?
Which binary starts automatically?
Which connection belongs to which process?
```

Do not use powerful remote execution tools outside authorized environments.

---

## Enhanced Deep Dive 73 — Process Explorer vs Task Manager

Task Manager:

```text
quick operational view
```

Process Explorer:

```text
deeper process tree
handles
signatures
parent/child relationships
DLL information
```

Both should be correlated with:

```text
service ownership
event logs
network sockets
```

---

## Enhanced Deep Dive 74 — Procmon as Evidence

Process Monitor captures:

```text
filesystem
registry
process/thread
selected network-related activity
```

It can answer:

```text
Access Denied to which path?
Which registry value is queried?
Which config file is missing?
```

Filter aggressively; raw Procmon traces can be enormous.

---

## Enhanced Deep Dive 75 — Hyper-V Type-1 Architecture

Simplified:

```text
Hardware
   ↓
Hyper-V hypervisor
   ↓
Parent/management partition
   ↓
child partitions/VMs
```

VMs do not simply run as ordinary user processes like a basic desktop emulator.

Understanding this explains why Hyper-V networking/storage integrates deeply with Windows.

---

## Enhanced Deep Dive 76 — VHDX

Virtual disk formats represent block storage for VMs.

VHDX supports modern Hyper-V features.

Inspect:

```powershell
Get-VHD D:\VMs\LabVM01\LabVM01.vhdx
```

Concepts:

```text
fixed
dynamically expanding
differencing
```

Each has performance/capacity/management trade-offs.

---

## Enhanced Deep Dive 77 — Dynamic vs Fixed VHDX

Dynamic:

```text
logical max size
physical file grows as data is written
```

Fixed:

```text
space allocated up front
```

Do not assume dynamic means unlimited free space.

Host volume can fill even when guest believes its virtual disk has space remaining.

---

## Enhanced Deep Dive 78 — Hyper-V Checkpoints

Checkpoint creates a rollback chain/state.

Use cases:

```text
short-lived lab change
pre-upgrade testing
```

Risks:

```text
disk chain growth
performance impact
application consistency concerns
not independent from same storage
```

Checkpoints should not accumulate indefinitely.

---

## Enhanced Deep Dive 79 — Hyper-V Networking

External:

```text
VM ↔ physical network
```

Internal:

```text
VM ↔ host + VMs
```

Private:

```text
VM ↔ VMs only
```

A vSwitch is a virtual Layer-2 construct.

VM routing/NAT behavior depends on additional Windows network configuration.

---

## Enhanced Deep Dive 80 — Hyper-V Integration Services Awareness

Modern guests use integration components for:

```text
time
shutdown
heartbeat
data exchange
backup coordination
```

Guest health should not be judged only by:

```text
VM state = Running
```

Application inside guest can still be failed.

---

## Enhanced Deep Dive 81 — Windows Server Backup vs Enterprise Backup

Windows Server Backup provides platform backup capability.

Enterprise environments may require:

```text
central scheduling
immutable/offline copies
application consistency
deduplication
encryption
offsite replication
reporting
SLA
```

Backup product choice is secondary to recoverability.

---

## Enhanced Deep Dive 82 — RPO and RTO

RPO:

```text
How much data loss is acceptable?
```

RTO:

```text
How long can service be unavailable?
```

Example:

```text
RPO = 4 hours
→ backups/replication must support ≤4 h data-loss target

RTO = 1 hour
→ restore/rebuild process must recover service ≤1 h
```

A backup that takes 8 hours to restore cannot meet a 1-hour RTO.

---

## Enhanced Deep Dive 83 — Recovery Testing

Backup success message is not enough.

Test:

```text
file restore
system-state restore where relevant
VM restore
bare-metal scenario where required
application consistency
credentials/keys availability
```

Document measured restore time.

---

## Enhanced Deep Dive 84 — CPU Troubleshooting

Inspect:

```powershell
Get-Process |
  Sort-Object CPU -Descending |
  Select-Object -First 10 Name, Id, CPU
```

Counters:

```powershell
Get-Counter '\Processor(_Total)\% Processor Time'
```

Ask:

```text
sustained or burst?
one process or many?
user workload or system?
VM host contention?
```

CPU percentage alone does not identify root cause.

---

## Enhanced Deep Dive 85 — Memory Troubleshooting

Useful signals:

```text
available memory
commit
paging
working sets
memory leaks
```

Example:

```powershell
Get-Counter '\Memory\Available MBytes'
```

Processes:

```powershell
Get-Process |
  Sort-Object WorkingSet64 -Descending |
  Select-Object -First 10 Name,
    @{N='WorkingSetMB';E={[math]::Round($_.WorkingSet64/1MB,1)}}
```

Do not treat "high RAM usage" as automatically unhealthy; caching can be useful.

---

## Enhanced Deep Dive 86 — Disk Latency

Disk problems are not only "disk full."

Monitor:

```text
latency
queue
throughput
IOPS
free capacity
errors
```

Counter:

```powershell
Get-Counter '\PhysicalDisk(_Total)\Avg. Disk sec/Transfer'
```

Interpret in context of storage type and workload.

---

## Enhanced Deep Dive 87 — Network Performance

Inspect:

```powershell
Get-NetAdapterStatistics
```

Look for:

```text
errors
discards
bytes
link state
```

Also:

```powershell
Get-Counter '\Network Interface(*)\Bytes Total/sec'
```

A slow application can be caused by:

```text
packet loss
duplex/link issue
route
DNS delay
upstream service
```

not simply "low bandwidth."

---

## Enhanced Deep Dive 88 — Data Collector Sets

Performance Monitor can collect counters over time.

This is essential for intermittent incidents:

```text
2:00 AM slowdown
```

that is gone by 9:00 AM.

Historical data supports:

```text
baseline
trend
capacity planning
incident correlation
```

---

## Enhanced Deep Dive 89 — Windows Update Servicing Stack Thinking

Update lifecycle:

```text
available update
  ↓
download/stage
  ↓
install
  ↓
pending reboot?
  ↓
reboot
  ↓
component/service health
```

An installed update record does not automatically prove the application remains healthy.

Patch validation includes service checks and business tests.

---

## Enhanced Deep Dive 90 — Reboot Coordination

Before reboot:

```text
maintenance approval
dependency impact
cluster/HA state
backup/recovery
active users/sessions
pending tasks
```

After reboot verify:

```text
OS boot
network
DNS
time
services
listeners
storage
applications
scheduled jobs
monitoring
```

"Ping works" is not post-patch validation.

---

## Enhanced Deep Dive 91 — Security Baseline as Configuration Set

A baseline may define:

```text
password/account policy
audit policy
firewall
SMB security
RDP security
Defender
TLS/crypto
user rights
services
logging
```

Workflow:

```text
Microsoft baseline
  ↓
organizational risk assessment
  ↓
application test
  ↓
approved baseline
  ↓
GPO/automation
  ↓
compliance monitoring
```

Do not deploy a baseline to all servers without role-specific compatibility testing.

---

## Enhanced Deep Dive 92 — Microsoft Defender Antivirus

Inspect:

```powershell
Get-MpComputerStatus
Get-MpPreference
```

Security operations should understand:

```text
real-time protection
signature freshness
exclusions
detections
cloud protection
```

Exclusions are security exceptions and should be narrowly justified.

---

## Enhanced Deep Dive 93 — Attack Surface Reduction Awareness

Modern endpoint/server security can include controls beyond antivirus.

Concepts:

```text
application control
attack surface reduction
credential protections
exploit mitigations
Defender for Endpoint/EDR
```

Windows Server hardening should integrate with enterprise security tooling rather than rely on one setting.

---

## Enhanced Deep Dive 94 — Credential Guard Awareness

Credential Guard uses virtualization-based security to protect selected credential material.

Infrastructure/security teams should understand:

```text
platform requirements
compatibility
deployment policy
credential-protection benefits
```

It is not a substitute for protecting privileged accounts and limiting where they log on.

---

## Enhanced Deep Dive 95 — Secure Boot and TPM

Secure Boot helps verify trusted boot components.

TPM can protect cryptographic secrets/measure boot state.

Used by technologies such as:

```text
BitLocker
VBS
credential protections
attestation scenarios
```

Availability planning must include recovery procedures for TPM/BitLocker changes.

---

## Enhanced Deep Dive 96 — Local Administrator Password Management

Shared local admin passwords create lateral-movement risk.

In AD environments, Windows LAPS can provide:

```text
unique password per machine
automatic rotation
controlled retrieval
```

This becomes a major bridge to Course 27.

---

## Enhanced Deep Dive 97 — Windows Server Network Hardening

Review:

```text
listening ports
enabled firewall rules
SMB exposure
RDP exposure
WinRM exposure
DNS/DHCP role networks
management subnets
```

Command set:

```powershell
Get-NetTCPConnection -State Listen
Get-NetUDPEndpoint
Get-NetFirewallProfile
Get-NetFirewallRule |
  Where-Object Enabled -eq 'True'
```

Every listener should have a business/role owner.

---

## Enhanced Deep Dive 98 — Local Admin Group Review

```powershell
Get-LocalGroupMember Administrators
```

Ask:

```text
Why is each identity here?
Is it named?
Is it still employed/required?
Could JEA/delegated group work instead?
```

Local Administrators membership is a high-impact security boundary.

---

## Enhanced Deep Dive 99 — Evidence-First Troubleshooting

Do not start by changing configuration.

Use:

```text
symptom
  ↓
scope
  ↓
recent change
  ↓
architecture path
  ↓
logs/state
  ↓
hypothesis
  ↓
minimal test
  ↓
fix
  ↓
verification
```

Evidence sources:

```text
Event Logs
service state
processes
network sockets
firewall
DNS
storage
performance counters
registry/policy
```

---

## Enhanced Deep Dive 100 — Windows Infrastructure Decision Tree

For "service is unreachable":

```text
Role installed?
   ↓
Service running?
   ↓
Process exists?
   ↓
Socket listening?
   ↓
Correct bind address?
   ↓
Windows Firewall?
   ↓
Route?
   ↓
DNS?
   ↓
Remote firewall/network?
   ↓
Application protocol?
```

This same logic works for:

```text
SMB
DNS
DHCP
WinRM
RDP
web apps
custom services
```

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Windows Kernel/User-Mode Map

Create a diagram mapping PowerShell, service process, driver, kernel, and hardware for DNS or SMB.

## Enhanced Lab 2 — Boot Inventory

Record firmware mode, BCD entries, boot volume, recovery options, and console access plan.

## Enhanced Lab 3 — Server Core Management Plan

Design how you would manage a Core server using PowerShell, WAC, MMC/RSAT, WinRM, and console.

## Enhanced Lab 4 — Role→Service→Socket

Choose DNS or another role and prove all four layers independently.

## Enhanced Lab 5 — Service Dependencies

Map dependencies of five services and explain what failure of each dependency could cause.

## Enhanced Lab 6 — PowerShell Object Exploration

Use `Get-Member` on services, processes, volumes, adapters, and SMB sessions.

## Enhanced Lab 7 — PowerShell Reporting

Build a `PSCustomObject` server baseline and export CSV/JSON.

## Enhanced Lab 8 — Error Handling

Create a script with `try/catch`, explicit `-ErrorAction Stop`, and meaningful exit/report behavior.

## Enhanced Lab 9 — Idempotent Directory Script

Create required admin folders only if missing and prove second run makes no changes.

## Enhanced Lab 10 — Local SID Observation

Create/rename a local user and verify SID remains the same.

## Enhanced Lab 11 — Group Token Refresh

Add a user to a group and compare access before/after new sign-in session.

## Enhanced Lab 12 — UAC

Compare standard and elevated PowerShell tokens using a harmless admin-only command.

## Enhanced Lab 13 — NTFS Inheritance

Build parent/child folders, inherit ACLs, break inheritance once, and document effect.

## Enhanced Lab 14 — Explicit Deny

Create a controlled deny and explain how it interacts with group allow.

## Enhanced Lab 15 — ACL Backup

Use `icacls /save` on a lab tree and restore into a test workflow.

## Enhanced Lab 16 — Share vs NTFS Matrix

Create four combinations of share/NTFS rights and test effective remote access.

## Enhanced Lab 17 — SMB Session Security

Observe SMB session, server configuration, signing/encryption settings, and authentication context.

## Enhanced Lab 18 — Disk Identity

Attach two disposable disks and identify them by model/serial/size before choosing one.

## Enhanced Lab 19 — GPT Volume

Initialize, partition, format, label, and verify a disposable disk.

## Enhanced Lab 20 — Folder Mount Point

Mount a small volume into an NTFS folder and document mapping.

## Enhanced Lab 21 — ReFS Comparison

Create NTFS and ReFS lab volumes if supported and compare available features/workload suitability.

## Enhanced Lab 22 — Storage Spaces

Use disposable virtual disks to build a lab pool and mirror if platform supports it.

## Enhanced Lab 23 — FSRM

Install FSRM, create a soft quota and report in the lab.

## Enhanced Lab 24 — DNS Resolver Cache

Create/change a lab DNS record and inspect resolver cache/TTL behavior.

## Enhanced Lab 25 — DNS Record Types

Create A, CNAME, PTR, and SRV records in isolated lab and query each.

## Enhanced Lab 26 — DNS Failure Matrix

Break resolver address, server service, record, and route separately; classify each layer.

## Enhanced Lab 27 — DHCP Reservation

Create a reservation for a lab client and compare it with exclusion behavior.

## Enhanced Lab 28 — DHCP Relay Design

Draw two client VLANs reaching centralized DHCP through router relay.

## Enhanced Lab 29 — Firewall Profiles

Move an isolated lab NIC between profiles where appropriate and observe rule impact.

## Enhanced Lab 30 — Narrow Firewall Rule

Permit TCP/8080 only from one lab subnet and verify allowed/denied clients.

## Enhanced Lab 31 — Firewall Logging

Enable controlled logging and generate one allowed/blocked lab test.

## Enhanced Lab 32 — Multi-Homed Routing

Use a VM with two lab NICs, inspect metrics/routes, and explain default-gateway design.

## Enhanced Lab 33 — IPv6 Observation

Inspect IPv6 addresses/routes/DNS and explain why disabling IPv6 blindly is poor troubleshooting.

## Enhanced Lab 34 — WinRM Baseline

Inspect listeners, test WS-Man, use Invoke-Command, and record authentication method.

## Enhanced Lab 35 — PowerShell Deserialization

Return a remote service object and compare its type/members with local object.

## Enhanced Lab 36 — Double-Hop Design

Draw Admin→ServerA→ServerB and explain secure architectural solutions without embedding passwords.

## Enhanced Lab 37 — JEA Design

Create a conceptual JEA role capability allowing only service status/restart for one service.

## Enhanced Lab 38 — RDP Hardening Review

Document source restrictions, NLA, gateway/VPN/PAW design, and why public 3389 is unacceptable.

## Enhanced Lab 39 — Scheduled Task Context

Run the same script interactively and scheduled; compare user, working directory, environment, and network access.

## Enhanced Lab 40 — Task Scheduler Evidence

Inspect last run result and operational events for a failed synthetic task.

## Enhanced Lab 41 — Event FilterHashtable

Produce a report of System errors from the last two hours.

## Enhanced Lab 42 — Event Forwarding Design

Draw source-initiated Windows Event Forwarding into a collector/SIEM.

## Enhanced Lab 43 — Sysinternals Process Tree

Use trusted Sysinternals tools to map a service→process→child processes.

## Enhanced Lab 44 — Procmon Access Denied

Create a safe folder-permission problem and use Procmon to locate the failing path.

## Enhanced Lab 45 — Hyper-V Switches

Create internal/private switches and explain connectivity boundaries.

## Enhanced Lab 46 — VHDX Growth

Create dynamic VHDX, write guest data, compare logical vs physical size.

## Enhanced Lab 47 — Checkpoint Lifecycle

Create checkpoint, modify VM, revert, then remove checkpoint and explain disk chain implications.

## Enhanced Lab 48 — VM Health

Compare `VM State=Running` with guest service/application health.

## Enhanced Lab 49 — Backup RPO/RTO

Define RPO/RTO for a file server and build an appropriate backup schedule.

## Enhanced Lab 50 — Restore Test

Back up lab files and perform a documented restore to alternate path.

## Enhanced Lab 51 — CPU Baseline

Collect CPU counter at idle and under safe load; identify top CPU processes.

## Enhanced Lab 52 — Memory Baseline

Collect available memory and top working sets before/after safe memory load.

## Enhanced Lab 53 — Disk Latency

Generate a safe copy workload and collect disk latency counters.

## Enhanced Lab 54 — NIC Statistics

Collect adapter errors/discards/throughput before/after safe traffic test.

## Enhanced Lab 55 — Data Collector Set

Create a short performance collection for CPU/memory/disk/network.

## Enhanced Lab 56 — Update Readiness

Create a pre-patch checklist and post-patch validation script.

## Enhanced Lab 57 — Security Baseline Review

Review installed roles, listeners, firewall rules, local admins, Defender state, RDP, and SMB.

## Enhanced Lab 58 — Defender Exclusion Review

List exclusions and document why every exclusion would require justification.

## Enhanced Lab 59 — BitLocker Recovery Design

Without encrypting production data, document TPM/recovery-key/boot-repair process for a server.

## Enhanced Lab 60 — Windows LAPS Design

Design how unique local administrator passwords would be managed after Course 27 domain deployment.

## Enhanced Lab 61 — Health Script v2

Create a structured script reporting:
`OS, uptime, disks, adapters, routes, DNS, failed services, listeners, firewall profiles, top CPU, recent errors`.

## Enhanced Lab 62 — Remoting Fleet Report

Use Invoke-Command against two lab servers and combine health results.

## Enhanced Lab 63 — Service Unreachable Challenge

Break service, listener, firewall, DNS, and route separately and solve using the decision tree.

## Enhanced Lab 64 — SMB Access Challenge

Inject wrong share ACL, NTFS ACL, group membership, hostname/authentication, and firewall issues.

## Enhanced Lab 65 — DNS/DHCP Integration

Build an isolated DNS/DHCP lab and document client configuration from lease to resolver behavior.

## Enhanced Lab 66 — Remote Admin Failure Matrix

Break WinRM listener, DNS, firewall, credentials, and service state individually.

## Enhanced Lab 67 — Server Core Simulation

Administer a lab server for one session using only PowerShell/remote tools, not GUI.

## Enhanced Lab 68 — Change Rollback

Perform a firewall/config change with before-state export, test, rollback, and after verification.

## Enhanced Lab 69 — Security Review Report

Write `WINDOWS_SERVER_SECURITY_REVIEW.md` with at least 30 checks.

## Enhanced Lab 70 — Integrated Infrastructure Failure Challenge

Inject at least 20 controlled faults across:

```text
services
permissions
storage
SMB
DNS
DHCP
firewall
routing
WinRM
tasks
Hyper-V
performance
security
```

Document for each:

```text
symptom
expected architecture path
evidence
failed layer
root cause
minimal fix
verification
prevention
```



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Server Baseline

1. Deploy WIN-SRV01.
2. Record edition, installation type, build, hostname, CPU, RAM, disks, IP, DNS, installed roles, and listening ports.
3. Save `SERVER_BASELINE.md`.
4. Explain which information comes from OS, networking, and service layers.

### Lab 2 — PowerShell Administration

1. Use `Get-Command` to discover networking commands.
2. Use `Get-Help` for at least five cmdlets.
3. Create a process report.
4. Create a service report.
5. Export one report to CSV.
6. Create one custom `PSCustomObject`.

### Lab 3 — Local Identity

1. Create two local users.
2. Create one local group.
3. Add one user to Remote Desktop Users.
4. Inspect Administrators membership.
5. Test least-privilege behavior.

### Lab 4 — NTFS Permissions

1. Create `D:\Departments\Finance`.
2. Create `Finance-Read` and `Finance-Modify` groups.
3. Assign correct NTFS permissions.
4. Test with lab users.
5. Explain inheritance.

### Lab 5 — Storage

1. Attach an empty virtual disk.
2. Verify disk identity.
3. Initialize GPT.
4. Create NTFS volume.
5. Label it Data.
6. Verify using `Get-Disk`, `Get-Partition`, and `Get-Volume`.

### Lab 6 — SMB

1. Create Finance share.
2. Configure share permission.
3. Configure NTFS separately.
4. Connect by UNC from a client.
5. Observe effective access.
6. Inspect SMB session.

### Lab 7 — Services and Events

1. Choose a safe lab service.
2. Start, stop, and restart it.
3. Find Service Control Manager events.
4. Write a PowerShell event report.
5. Explain service state vs process/socket state.

### Lab 8 — Scheduled Task

1. Create `C:\Admin\Health.ps1`.
2. Register a daily task.
3. Trigger it manually.
4. Verify output.
5. Inspect Task Scheduler state.

### Lab 9 — DNS

1. Install DNS.
2. Create `lab.example`.
3. Add `srv01` A record.
4. Add an alias.
5. Query with `Resolve-DnsName`.
6. Break one record and troubleshoot.

### Lab 10 — DHCP

1. Install DHCP in an isolated lab.
2. Create a scope.
3. Configure router and DNS options.
4. Renew a client.
5. Inspect leases.
6. Explain DORA.

### Lab 11 — Firewall

1. Run an authorized test service on TCP/8080.
2. Verify local listener.
3. Add inbound firewall rule.
4. Test remotely.
5. remove/disable the rule.
6. Observe the difference.

### Lab 12 — PowerShell Remoting

1. Verify WinRM.
2. Run `Test-WSMan`.
3. Use `Invoke-Command`.
4. Use `Enter-PSSession`.
5. Document authentication and DNS dependency.

### Lab 13 — Hyper-V

1. Verify virtualization support.
2. Install Hyper-V if supported.
3. Create internal switch.
4. Create Generation 2 VM.
5. Create a checkpoint.
6. Restore in the lab.
7. Explain why checkpoint is not backup.

### Lab 14 — Performance

1. Collect CPU counter.
2. Collect memory counter.
3. Collect disk counter.
4. Generate safe lab load.
5. Compare before/after.
6. Document the suspected bottleneck.

### Lab 15 — Broken Windows Server Challenge

Inject one fault at a time:

1. wrong DNS client
2. disabled service
3. firewall block
4. wrong NTFS permission
5. wrong share permission
6. disabled scheduled task
7. wrong static route
8. wrong DNS record

For every fault:

```text
Symptom
Expected path
Evidence
Failed layer
Root cause
Fix
Verification
```

---

## 6. Mini Project

# Mini Project — Windows Infrastructure Member Server

Build:

```text
WIN-SRV01
10.60.0.10/24
```

Architecture:

```text
Client
  |
  +-- DNS ----------> WIN-SRV01 DNS lab zone
  |
  +-- SMB ----------> D:\Shares
  |
  +-- WinRM --------> PowerShell Remoting
  |
  +-- RDP ----------> restricted administration
```

## Requirements

### Storage

```text
Disk 0 -> OS
Disk 1 -> D: Data
```

Create:

```text
D:\Shares\Public
D:\Shares\Operations
D:\Admin
```

### Local Identity

Create:

```text
Operations group
Admin operator
Normal test user
```

Use least privilege.

### SMB

Create:

```text
\\WIN-SRV01\Public
\\WIN-SRV01\Operations
```

Document both:

```text
share ACL
NTFS ACL
```

### DNS

Create:

```text
infra.lab
srv01.infra.lab
files.infra.lab
```

### DHCP

Create an isolated test scope if lab networking permits it.

### Security

- Defender Firewall enabled
- only required inbound rules
- no unnecessary local administrators
- document listening ports
- update state documented

### Remote Management

- PowerShell Remoting
- controlled RDP
- optional Windows Admin Center

### Automation

Create:

```text
C:\Admin\DailyHealth.ps1
```

Report:

- hostname
- OS/build
- uptime
- disks/free space
- IPv4
- DNS servers
- failed automatic services
- top CPU processes
- installed roles
- recent System errors

Schedule it.

### Documentation

```text
README.md
SERVER_BASELINE.md
STORAGE.md
NETWORK.md
DNS.md
DHCP.md
SMB.md
FIREWALL.md
REMOTE_ADMIN.md
HEALTH_REPORT.md
TROUBLESHOOTING.md
```

### Failure Tests

1. wrong DNS resolver
2. share permission mismatch
3. NTFS permission mismatch
4. service stopped
5. firewall rule disabled
6. static route wrong
7. DNS record wrong
8. scheduled task disabled

---


# Expanded Capstone — Windows Enterprise Member-Server Platform

Build:

```text
                        ADMIN01
                           |
                 WinRM / WAC / RDP
                           |
                           v
                       WIN-SRV01
              +------------+-------------+
              |            |             |
             DNS          SMB         Automation
              |            |             |
         lab.example     D:\Shares      Health.ps1
                           |
                    NTFS / ACL / FSRM

Optional:
WIN-HV01 → Hyper-V lab host
```

## Required Server Baseline

Document:

```text
edition
installation type
build
firmware
CPU/RAM
disks
volumes
NICs
IP/routes
DNS resolver
roles/features
services
listeners
firewall profiles
local admins
Defender state
recent errors
```

## Storage

Use an extra disposable disk.

Create:

```text
D:\Shares\Public
D:\Shares\Operations
D:\Shares\Finance
D:\Admin
D:\Logs
```

Implement:

```text
group-based NTFS permissions
simple share permissions
quota/reporting where appropriate
```

## Network Services

Create isolated lab:

```text
DNS zone: infra.lab
A/PTR/CNAME records
DHCP scope
router/DNS/domain options
reservation
```

## Remote Administration

Support:

```text
PowerShell Remoting
restricted RDP
optional Windows Admin Center
```

Do not expose management ports to the Internet.

## Automation

Create:

```text
C:\Admin\DailyHealth.ps1
```

The script must:

```text
return structured objects
use try/catch
create output directory idempotently
log failures
report:
OS/build
uptime
volumes/free space
NIC/IP/routes/DNS
failed automatic services
listening TCP ports
firewall profile
top CPU/memory processes
recent System errors
installed roles
```

Schedule the script.

## Security

Review:

```text
unnecessary roles
listeners
local admins
firewall source scope
SMB signing/encryption policy
RDP
WinRM
Defender
BitLocker/recovery plan
update status
event forwarding design
Windows LAPS future design
```

## Optional Hyper-V Node

Create:

```text
one Generation 2 VM
internal switch
VHDX
one short-lived checkpoint
```

Document why checkpoint is not backup.

## Failure Matrix

At least 25:

```text
DNS resolver wrong
DNS service stopped
record wrong
DHCP option wrong
DHCP scope exhausted simulation/design
SMB service stopped
share ACL wrong
NTFS ACL wrong
group token stale
firewall blocks 445
WinRM service disabled
WinRM firewall blocked
RDP source rule wrong
task runs as wrong identity
task working directory wrong
disk almost full
log growth
dynamic VHDX host volume low
service dependency stopped
port collision
NIC disabled
wrong route
wrong default gateway
Defender exclusion risk
post-update service failure
```

For every incident record:

```text
User-visible symptom
Expected path
Evidence
Root cause
Fix
Verification
Rollback/prevention
```

## Documentation

```text
README.md
SERVER_ARCHITECTURE.md
BASELINE.md
STORAGE.md
NTFS_PERMISSIONS.md
SMB.md
DNS.md
DHCP.md
NETWORK.md
FIREWALL.md
REMOTE_ADMIN.md
POWERSHELL_AUTOMATION.md
HYPERV.md
BACKUP_RPO_RTO.md
MONITORING.md
SECURITY_BASELINE.md
FAILURE_TESTS.md
CHANGE_ROLLBACK.md
```


## 7. Recommended Resources

Prioritize official Microsoft Learn documentation:

- Windows Server documentation
- Windows Server 2025 documentation
- Server Core
- Server Manager
- Windows Admin Center
- Windows Server Storage
- NTFS
- ReFS
- SMB
- Hyper-V
- DNS Server
- DHCP Server
- Windows Defender Firewall
- PowerShell

Use local command discovery continuously:

```powershell
Get-Command
Get-Help <Cmdlet> -Full
Get-Help <Cmdlet> -Examples
```

---

## 8. Certification Relevance

This material supports:

- Windows Server Administration
- Windows hybrid administration
- enterprise infrastructure support
- Active Directory administration
- Hyper-V
- Windows security engineering
- SOC / incident-response Windows analysis
- cloud Windows Server operations

It prepares directly for Course 27 because AD DS depends on:

```text
DNS
networking
PowerShell
services
firewall
security
storage
remote administration
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Managing everything only with GUI.  
  **Best practice:** Learn the equivalent PowerShell state and verification commands.

- **Mistake:** Changing the only remote NIC without console access.  
  **Best practice:** Use console/out-of-band access or a rollback plan.

- **Mistake:** Giving Administrator rights to solve file-access issues.  
  **Best practice:** Fix the actual ACL requirement.

- **Mistake:** Ignoring the interaction between SMB share and NTFS permissions.  
  **Best practice:** Evaluate both.

- **Mistake:** Initializing a disk by copied disk number.  
  **Best practice:** Verify disk size/model/status first.

- **Mistake:** Opening broad firewall rules.  
  **Best practice:** Limit direction, protocol, port, profile, and source where appropriate.

- **Mistake:** Using public DNS on future domain members.  
  **Best practice:** Use AD-aware DNS after the domain exists.

- **Mistake:** Treating Hyper-V checkpoints as backup.  
  **Best practice:** Use actual tested backup.

- **Mistake:** Restarting a service repeatedly before checking logs.  
  **Best practice:** Capture evidence first.

- **Mistake:** Publishing RDP directly to the Internet.  
  **Best practice:** Use secure remote-access architecture such as VPN/RD Gateway/privileged access.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is Server Core?

**Short answer:** A minimal Windows Server installation option intended for command-line and remote administration while supporting many server roles.

### Q2. Role vs feature?

**Short answer:** A role provides a major server function; a feature provides supporting functionality.

### Q3. Why is PowerShell's object pipeline important?

**Short answer:** It preserves structured properties between commands instead of passing only plain text.

### Q4. What does `Get-WindowsFeature` do?

**Short answer:** Lists Windows Server roles/features and installation state.

### Q5. What does `Get-Acl` inspect?

**Short answer:** An object's security descriptor and ACL.

### Q6. What two permission layers affect remote SMB access?

**Short answer:** Share permissions and NTFS permissions.

### Q7. What is GPT?

**Short answer:** A modern disk partition-table format.

### Q8. What is ReFS?

**Short answer:** A resilient Windows filesystem designed for supported workload scenarios.

### Q9. What port does SMB commonly use?

**Short answer:** TCP 445.

### Q10. What PowerShell command resolves DNS?

**Short answer:** `Resolve-DnsName`.

### Q11. What is DHCP DORA?

**Short answer:** Discover, Offer, Request, Acknowledge.

### Q12. What provides PowerShell remoting transport on Windows?

**Short answer:** WinRM/WS-Management.

### Q13. What is Hyper-V?

**Short answer:** Microsoft's hypervisor-based virtualization technology.

### Q14. Why is a checkpoint not a backup?

**Short answer:** It is mainly a state rollback mechanism and often depends on the same virtualization/storage environment.

### Q15. What four resource categories start performance troubleshooting?

**Short answer:** CPU, memory, disk, network.

### Q16. What is the course's main troubleshooting principle?

**Short answer:** Collect evidence and isolate the failing layer before changing configuration.

---


# Enhanced Self-Assessment Bank

### Q1. User mode vs kernel mode?
**Answer:** User mode isolates applications/services; kernel mode contains core OS/driver execution with system-wide impact.

### Q2. What manages Windows services?
**Answer:** Service Control Manager.

### Q3. Role installed means service healthy?
**Answer:** No.

### Q4. Service vs process?
**Answer:** Service is a lifecycle/configuration object; process is a running executable instance.

### Q5. Why is Server Core important?
**Answer:** Supports remote/command-first administration with fewer local GUI components.

### Q6. What does PowerShell pipeline pass?
**Answer:** Structured .NET objects.

### Q7. Why `Get-Member`?
**Answer:** Discover object type, properties, and methods.

### Q8. Why use `Get-Help`?
**Answer:** Verify cmdlet syntax/parameters/examples for installed environment.

### Q9. What is PSCustomObject useful for?
**Answer:** Structured reports and automation data.

### Q10. Why `-ErrorAction Stop` inside try/catch?
**Answer:** Convert selected non-terminating errors into catchable terminating errors.

### Q11. What is idempotent automation?
**Answer:** Repeated execution converges to same desired state without unnecessary change.

### Q12. What is DSC conceptually?
**Answer:** Desired-state configuration framework.

### Q13. What is a SID?
**Answer:** Stable Windows security identifier for a principal.

### Q14. What is an access token?
**Answer:** User/group SIDs, privileges, integrity/restriction data used for authorization.

### Q15. Why group changes may need new logon?
**Answer:** Existing access token may not include new membership.

### Q16. Permission vs privilege?
**Answer:** Permission applies to an object; privilege is a system-level user right.

### Q17. DACL?
**Answer:** ACL defining allowed/denied access.

### Q18. SACL?
**Answer:** ACL defining auditing rules.

### Q19. Why inheritance?
**Answer:** Scales ACL management from parent to children.

### Q20. Share vs NTFS?
**Answer:** Remote SMB access must pass both share and filesystem permissions.

### Q21. SMB uses which common port?
**Answer:** TCP 445.

### Q22. SMB signing?
**Answer:** Protects message integrity/authenticity.

### Q23. SMB encryption?
**Answer:** Encrypts SMB traffic over network.

### Q24. NTFS vs ReFS?
**Answer:** NTFS is broad general-purpose filesystem; ReFS targets supported resilience/scale workloads.

### Q25. EFS vs BitLocker?
**Answer:** File-level user-key encryption vs volume-level encryption.

### Q26. Why verify BitLocker recovery material?
**Answer:** Prevent permanent lockout during TPM/boot recovery events.

### Q27. First storage safety rule?
**Answer:** Prove exact disk identity before destructive action.

### Q28. GPT?
**Answer:** Modern partition table format.

### Q29. Volume mount point?
**Answer:** Volume attached to an NTFS directory instead of drive letter.

### Q30. Storage Spaces mirror?
**Answer:** Redundant data copies across underlying disks.

### Q31. What is VSS?
**Answer:** Snapshot coordination framework used by backup/application-consistency workflows.

### Q32. FSRM?
**Answer:** File Server Resource Manager for quotas, file screens, reports/classification.

### Q33. Resolver vs DNS server?
**Answer:** Resolver configuration tells client where to ask; DNS server hosts/resolves zones.

### Q34. A record?
**Answer:** Name to IPv4 address.

### Q35. PTR?
**Answer:** Reverse IP-to-name record.

### Q36. SRV?
**Answer:** Service locator record.

### Q37. TTL?
**Answer:** Cache lifetime for a DNS record.

### Q38. DHCP DORA?
**Answer:** Discover, Offer, Request, Acknowledge.

### Q39. Reservation vs exclusion?
**Answer:** Reservation maps a client to chosen address; exclusion prevents dynamic leasing of an address range.

### Q40. Why DHCP relay?
**Answer:** Forward client DHCP requests across routed networks.

### Q41. Firewall profiles?
**Answer:** Domain, Private, Public.

### Q42. Why not disable firewall to troubleshoot?
**Answer:** It weakens security and removes evidence; inspect exact rule/profile instead.

### Q43. Route selection uses what major concepts?
**Answer:** Longest prefix match and route/interface metrics.

### Q44. Why multiple default gateways risky?
**Answer:** Can create asymmetric/unpredictable routing.

### Q45. Should IPv6 be disabled generically?
**Answer:** No.

### Q46. `Test-NetConnection -Port` proves what?
**Answer:** DNS/route/TCP reachability to selected service endpoint.

### Q47. What is WinRM?
**Answer:** Windows Remote Management / WS-Management service used by PowerShell remoting.

### Q48. Why can remote objects be different locally?
**Answer:** They are often serialized/deserialized copies.

### Q49. Double-hop?
**Answer:** Credentials used to reach server A are not automatically delegated from A to B.

### Q50. JEA?
**Answer:** Just Enough Administration, constrained PowerShell admin endpoints.

### Q51. Why public RDP is risky?
**Answer:** Directly exposes privileged interactive management service to Internet attack.

### Q52. Why scheduled script works manually but fails scheduled?
**Answer:** Different identity, environment, working directory, or credential/network context.

### Q53. How inspect scheduled task last result?
**Answer:** `Get-ScheduledTaskInfo`.

### Q54. Why `FilterHashtable`?
**Answer:** Efficient server-side Event Log filtering.

### Q55. Windows Event Forwarding?
**Answer:** Centralized collection of Windows events from multiple systems.

### Q56. Procmon?
**Answer:** Diagnostic tool tracing filesystem/registry/process activity.

### Q57. Hyper-V external switch?
**Answer:** Connects VM networking to physical network.

### Q58. Dynamic VHDX?
**Answer:** File grows as guest writes up to configured virtual maximum.

### Q59. Checkpoint equals backup?
**Answer:** No.

### Q60. Why VM Running is insufficient?
**Answer:** Guest OS/application may still be unhealthy.

### Q61. RPO?
**Answer:** Maximum acceptable data-loss window.

### Q62. RTO?
**Answer:** Maximum acceptable recovery duration.

### Q63. Why test restore?
**Answer:** Backup success does not prove recoverability.

### Q64. Four initial performance layers?
**Answer:** CPU, memory, disk, network.

### Q65. High RAM usage always bad?
**Answer:** No.

### Q66. Disk full only storage problem?
**Answer:** No; latency/queue/errors can fail performance first.

### Q67. Why historical counters?
**Answer:** Intermittent incidents may be gone when administrator investigates.

### Q68. Patch installed means server healthy?
**Answer:** No; post-update service/application validation is required.

### Q69. What is a security baseline?
**Answer:** Approved set of security configuration controls.

### Q70. Why narrow Defender exclusions?
**Answer:** Exclusions reduce inspection and expand attack surface.

### Q71. Credential Guard?
**Answer:** VBS-based protection for selected Windows credential material.

### Q72. Secure Boot?
**Answer:** Helps verify trusted boot components.

### Q73. TPM role?
**Answer:** Hardware-backed protection/measurement used by security features such as BitLocker/VBS.

### Q74. Windows LAPS?
**Answer:** Manages unique rotating local administrator passwords in directory-managed environments.

### Q75. First principle for listener review?
**Answer:** Every open port should map to a required service/business owner.

### Q76. Why review local Administrators?
**Answer:** Membership grants high-impact local control.

### Q77. Best troubleshooting sequence?
**Answer:** Symptom → scope → architecture → evidence → hypothesis → minimal fix → verification.

### Q78. Service unreachable decision path?
**Answer:** Role → service → process → socket → firewall → route → DNS → remote path → application.

### Q79. What makes a Windows change complete?
**Answer:** Runtime verification, persistence/reboot behavior, logs, rollback, and documentation.

### Q80. Main goal of Course 26?
**Answer:** Understand Windows Server as an infrastructure system, not only a GUI.


## Completion Checklist

- [ ] I can administer Windows Server with PowerShell and GUI tools.
- [ ] I can install and inspect roles/features.
- [ ] I can manage local identity and NTFS permissions.
- [ ] I can configure disks, NTFS volumes, and SMB shares safely.
- [ ] I can manage services, tasks, Event Logs, and basic registry data.
- [ ] I can configure Windows networking and troubleshoot by layer.
- [ ] I can configure lab DNS and DHCP.
- [ ] I can manage Windows Defender Firewall.
- [ ] I can use PowerShell Remoting.
- [ ] I can explain Hyper-V architecture and create a lab VM.
- [ ] I can build a health/performance report.
- [ ] I completed all labs and the Windows member-server mini project.
