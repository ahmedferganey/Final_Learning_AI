# Phase 6 — Windows Enterprise Administration

This phase follows operating-system, networking, programming, Linux, and infrastructure fundamentals.

## Course Order

1. **26. Microsoft Windows Server Infrastructure**
2. **27. Microsoft Active Directory Administration**

## Dependency Flow

```text
Operating Systems + Networking
            ↓
26. Microsoft Windows Server Infrastructure
            ↓
27. Microsoft Active Directory Administration
```

## Technical Baseline

The material uses **Windows Server 2025** as the main current reference point while explaining concepts that also apply to Windows Server 2022/2019 environments.

The learning style is deliberately practical:

```text
Concept
   ↓
Visualization / architecture diagram
   ↓
PowerShell or command example
   ↓
Expected behavior
   ↓
Troubleshooting
   ↓
Hands-on lab
```

The objective is not to memorize definitions. You should be able to visualize the architecture, run commands, interpret output, and diagnose failures.

## Recommended Lab

```text
Host Computer
    |
    +-- Hypervisor
          |
          +-- WIN-SRV01
          |     Windows Server 2025
          |
          +-- WIN-DC01
          |     Windows Server 2025
          |
          +-- WIN-DC02
          |     Windows Server 2025
          |
          +-- WIN-CLIENT01
                Windows 11
```

Suggested isolated lab network:

```text
10.60.0.0/24

WIN-SRV01      10.60.0.10
WIN-DC01       10.60.0.11
WIN-DC02       10.60.0.12
WIN-CLIENT01   10.60.0.50
Gateway        10.60.0.1
```

## Safety

Use disposable VMs/checkpoints for:

- storage initialization
- firewall changes
- registry changes
- DNS/DHCP experiments
- Hyper-V nested virtualization
- domain-controller promotion
- Group Policy experiments
- FSMO recovery exercises
- Active Directory recovery

Never perform destructive identity, storage, or domain-controller exercises in environments you do not own and administer.

## Current Progress

- [x] 26. Microsoft Windows Server Infrastructure
- [x] 27. Microsoft Active Directory Administration

**Phase 6 is complete after both mini projects are completed.**
