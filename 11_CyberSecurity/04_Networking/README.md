# Phase 4 — Networking

This folder starts Phase 4 of the Unified Cloud Infrastructure & Cybersecurity Engineering study plan.

## Phase 4 Course Order

1. **16. Cisco Network Associate**
2. **17. Cisco Internetworking**
3. **18. Advanced Routing Design and Implementation**
4. **19. Advanced Switching Design and Implementation**

Only Course 16 is generated in this package. Courses 17–19 should be studied after Course 16 because they assume that IPv4/IPv6, Ethernet, switching, VLANs, routing, NAT, ACLs, DHCP, DNS, TCP/UDP, packet flow, and Cisco IOS fundamentals are already comfortable.

## Dependency Flow

```text
Phase 1 — Computer Networks Fundamentals
                   |
                   v
16. Cisco Network Associate
                   |
                   v
17. Cisco Internetworking
                   |
                   v
18. Advanced Routing Design & Implementation
                   |
                   v
19. Advanced Switching Design & Implementation
```

## How to Study Course 16

Do not read this file like a glossary.

For every major concept:

1. Read the explanation.
2. Draw the topology or packet flow yourself.
3. Reproduce the configuration in Cisco Packet Tracer or an equivalent legal lab environment.
4. Predict what the device will do before running a verification command.
5. Use `show` commands to prove your prediction.
6. Break one configuration intentionally.
7. Troubleshoot from Layer 1 upward.
8. Capture traffic with Wireshark where possible.
9. Explain the result in your own words.
10. Save the lab and a short troubleshooting note.

## Recommended Lab Tools

- Cisco Packet Tracer for CCNA-level simulation.
- Wireshark for packet analysis.
- Windows networking commands: `ipconfig`, `ping`, `tracert`, `arp`, `route`, `netstat`, `nslookup`.
- Linux networking commands: `ip`, `ping`, `traceroute`, `ss`, `dig`, `ip neigh`.
- A spreadsheet or notebook for subnetting practice.

## Suggested Base Topology

Use this topology repeatedly and extend it as the course progresses.

```text
                         Internet / ISP
                              |
                           [R-EDGE]
                              |
                     10.255.0.0/30
                              |
                            [R1]
                         /         \
                        /           \
                10.0.12.0/30    10.0.13.0/30
                    /                 \
                  [R2]               [R3]
                   |                   |
              +----+----+         +----+----+
              |         |         |         |
            [SW1]     [SW2]     [SW3]     [SW4]
              |         |         |         |
          VLAN 10   VLAN 20   VLAN 30   VLAN 40
          USERS     SERVERS    HR       FINANCE
```

As the material progresses, add:

- Trunks
- Router-on-a-stick
- DHCP
- Static routes
- NAT/PAT
- ACLs
- IPv6
- WLAN
- A management VLAN
- A Packet Tracer server providing DNS/HTTP services

## Lab Safety

Use Packet Tracer, your own virtual machines, your own home lab, or systems you are explicitly authorized to administer. Network-security topics in Course 16 are introductory and defensive. Offensive implementation belongs in later cybersecurity phases and must remain inside authorized labs.

## Exit Criteria for Course 16

Before moving to Cisco Internetworking, you should be able to:

- Explain the OSI and TCP/IP models using a real web request.
- Trace encapsulation from application data to Ethernet bits and back.
- Explain how a switch learns MAC addresses and forwards frames.
- Calculate IPv4 networks, broadcasts, host ranges, CIDR prefixes, and VLSM plans manually.
- Recognize and configure basic IPv6 addressing.
- Explain ARP and IPv6 Neighbor Discovery.
- Explain TCP handshakes, reliability, UDP behavior, ports, and sockets.
- Configure Cisco IOS basics, VLANs, trunks, router-on-a-stick, static/default routing, DHCP, NAT/PAT, and basic ACLs.
- Use Windows, Linux, Cisco IOS, and Wireshark troubleshooting tools.
- Build and troubleshoot a complete small enterprise topology without following a step-by-step answer sheet.
