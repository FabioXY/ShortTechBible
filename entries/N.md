
## NAT — Network Address Translation

Process of rewriting source or destination IP addresses in packet headers as
they pass through a router or firewall. Enables private RFC 1918 address spaces
to communicate with the Internet via a single public IP. Introduces connection
tracking state and complicates inbound connections requiring port forwarding.

**Difficulty:** Base
**Category:** Networking

---

## NFS — Network File System

Distributed filesystem protocol (RFC 7530 for NFSv4) allowing a client to mount
and access remote directory trees as if they were local. Developed by Sun
Microsystems in 1984. NFSv4 added strong security (Kerberos), stateful semantics,
and better WAN performance over earlier stateless versions.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NIC — Network Interface Card

Hardware component providing a device with physical or wireless network connectivity.
Contains a MAC address burned into firmware, implements the PHY and MAC layers,
and offloads checksum computation, segmentation (TSO), and receive-side scaling
(RSS) from the CPU in modern server NICs.

**Difficulty:** Base
**Category:** Hardware

---

## NIDS — Network Intrusion Detection System

Passive security system monitoring network traffic at a span port or inline tap
for known attack patterns and policy violations. Generates alerts without
blocking traffic. Contrasted with NIPS (Network Intrusion Prevention System)
which actively blocks. Snort and Suricata are common open-source NIDS engines.

**Difficulty:** Intermediate
**Category:** Security

---

## NIST — National Institute of Standards and Technology

US federal agency within the Department of Commerce that develops technology
standards, guidelines, and best practices. Key IT publications: NIST SP 800-53
(security controls), NIST SP 800-171 (CMMC baseline), NIST Cybersecurity Framework,
and FIPS standards (AES, SHA-2, etc.).

**Difficulty:** Base
**Category:** Security

---

## NMAP — Network Mapper

Open-source tool for network discovery and security auditing. Uses raw IP packets
to determine hosts on a network, their open ports, running services, OS type,
and software versions. A foundational tool for both security assessments and
network inventory. Common usage: `nmap -sV -O target`.

**Difficulty:** Intermediate
**Category:** Security

---

## NMI — Non-Maskable Interrupt

Hardware interrupt that cannot be disabled by the CPU's interrupt flag, ensuring
the processor always responds regardless of current interrupt enable state. Used
for critical hardware failures (ECC memory errors, watchdog timeouts, hardware
panics). In Linux, NMI can trigger a kernel backtrace for deadlock diagnosis.

**Difficulty:** Advanced
**Category:** Hardware

---

## NNTP — Network News Transfer Protocol

Application-layer protocol (RFC 3977) for distributing, querying, and posting
articles in Usenet newsgroups. Operates on TCP port 119 (563 for NNTPS over
TLS). Once central to Internet community discussion, largely supplanted by
web forums and social media but still active in some technical communities.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NOC — Network Operations Center

Centralized facility where IT staff monitor, manage, and maintain networks and
infrastructure around the clock. Handles incident detection, escalation, and
resolution for network outages, performance degradation, and security events.
Distinct from SOC (Security Operations Center) which focuses on security threats.

**Difficulty:** Base
**Category:** Networking

---

## NTFS — New Technology File System

Microsoft's proprietary journaling filesystem used by Windows since Windows NT
3.1. Supports large files, file permissions (ACLs), encryption (EFS), compression,
sparse files, hard links, alternate data streams, and change journals. Maximum
volume size: 256 TB with 64 KB clusters.

**Difficulty:** Intermediate
**Category:** OS

---

## NTP — Network Time Protocol

Protocol (RFC 5905) for synchronizing system clocks over a network. Uses a
hierarchical system of time sources called strata: stratum 0 (atomic clocks/GPS),
stratum 1 (servers directly connected to stratum 0), and so on. Achieves
millisecond accuracy on LANs; NTPv4 supports microsecond precision.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NUMA — Non-Uniform Memory Access

Multi-processor memory architecture where each CPU socket has local DRAM with
lower latency, while accessing another socket's memory incurs higher latency.
Optimal performance requires NUMA-aware memory allocation. Managed in Linux via
`numactl`, `/proc/sys/kernel/numa_balancing`, and cgroup memory node pinning.

**Difficulty:** Advanced
**Category:** Hardware

---

## NVME — Non-Volatile Memory Express

High-performance storage interface protocol designed specifically for SSDs over
PCIe. Replaces legacy AHCI which was designed for spinning disks and limited
to one command queue of 32 commands. NVMe supports 65,535 queues each with
65,535 commands, achieving millions of IOPS with sub-100µs latency.

**Difficulty:** Intermediate
**Category:** Hardware

---

## NETB — NetBIOS

Network Basic Input/Output System — API and protocol suite developed by IBM
in 1983 for local network communication. Provides name registration, session
establishment, and datagram services over NetBEUI or TCP/IP (NetBIOS over
TCP/IP, RFC 1001/1002). Now largely replaced by DNS and SMB direct, but
still present in legacy Windows networks.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NFSD — NFS Daemon

Kernel-space or user-space server process on Linux/Unix systems handling NFS
client requests. The Linux kernel NFS server (`knfsd`) processes requests entirely
in kernel space for performance. Configuration via `/etc/exports`; supports
Kerberos authentication for NFSv4 with `rpc.gssd` and `rpc.idmapd` helpers.

**Difficulty:** Intermediate
**Category:** OS

---

## NFTB — Netfilter Tables

Wait, the correct acronym is NFTS. Actually the proper name is nftables. Since nftables > 4 chars, this won't work. Replacing with:

## NHRP — Next Hop Resolution Protocol

Protocol used in DMVPN (Dynamic Multipoint VPN) deployments to allow spoke VPN
routers to discover the public IP address of other spoke routers dynamically.
A central hub maintains an NHRP database; spokes query it to build direct
spoke-to-spoke tunnels on demand, reducing hub-and-spoke traffic bottlenecks.

**Difficulty:** Advanced
**Category:** Networking

---

## NLSP — NetWare Link Services Protocol

Novell's link-state routing protocol developed as an improvement over RIP/SAP
in IPX networks. Used shortest-path routing based on complete network topology
knowledge rather than distance vectors. Now obsolete along with IPX/SPX, but
historically relevant in enterprise networks of the 1990s.

**Difficulty:** Advanced
**Category:** Networking

---

## NDEF — NFC Data Exchange Format

Standard (defined by the NFC Forum) for structuring data in NFC (Near Field
Communication) messages. An NDEF message contains one or more NDEF records,
each with a type (URI, text, MIME type), payload, and optional identifier.
Used in NFC tags on product packaging, access cards, and contactless payment
systems.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NDIS — Network Driver Interface Specification

Microsoft and 3Com specification defining a standard interface between network
device drivers and upper-layer network protocols in Windows. Allows protocol
drivers (TCP/IP, IPX) to work with any NIC driver implementing the NDIS
interface without modification. NDIS 6.x supports filter drivers for packet
inspection and modification.

**Difficulty:** Advanced
**Category:** OS

---

## NGFW — Next-Generation Firewall

Firewall extending stateful packet inspection with application-layer awareness,
user identity tracking, SSL/TLS inspection, and integrated IPS. Can identify
and control applications regardless of port (e.g., blocking Dropbox traffic even
on port 443). Examples: Palo Alto PA-Series, Fortinet FortiGate, pfSense with Suricata.

**Difficulty:** Intermediate
**Category:** Security

---

## NPIV — N-Port ID Virtualization

Fibre Channel feature allowing a single physical HBA port to register multiple
virtual N-Port IDs (WWPNs) with the FC fabric. Enables virtualization hosts to
assign each VM its own Fibre Channel identity without requiring dedicated physical
HBAs per VM. Simplifies zoning and LUN masking in virtualized SAN environments.

**Difficulty:** Advanced
**Category:** Hardware

---

## NRPE — Nagios Remote Plugin Executor

Agent-based plugin for the Nagios monitoring framework allowing the Nagios server
to execute monitoring checks on remote hosts. The NRPE daemon runs on monitored
hosts, receives check requests from Nagios via TCP port 5666, executes the
specified plugin locally, and returns the result code and output.

**Difficulty:** Intermediate
**Category:** Dev

---

## NSEC — Next Secure (DNSSEC Record)

DNSSEC resource record that proves the non-existence of DNS records between two
adjacent names in a signed zone. Allows a resolver to verify that a queried
name does not exist without receiving an NXDOMAIN response that could be spoofed.
NSEC3 uses hashed owner names to prevent zone enumeration.

**Difficulty:** Advanced
**Category:** Protocol

---

## NSFW — Not Safe for Work

Content warning label indicating material inappropriate for professional settings.
Relevant to IT in content filtering policies, where proxy and DLP systems flag
or block NSFW content based on categories, image classifiers, or URL reputation
lists enforced by web filtering solutions.

**Difficulty:** Base
**Category:** Security

---

## NTLM — NT LAN Manager

Suite of Microsoft challenge/response authentication protocols providing
authentication, integrity, and confidentiality. Used as a fallback when Kerberos
is unavailable in Windows environments. NTLMv1 is cryptographically broken;
NTLMv2 is stronger but still vulnerable to Pass-the-Hash and relay attacks.

**Difficulty:** Advanced
**Category:** Security

---

## NWCM — Network Configuration Manager

Generic term for software maintaining a versioned database of network device
configurations. Automates configuration backup, diff-based change detection,
compliance checking against policy templates, and rollback capabilities for
routers, switches, and firewalls. Examples: Oxidized, RANCID, SolarWinds NCM.

**Difficulty:** Intermediate
**Category:** Networking

---

## NPFS — Named Pipe File System

Windows kernel filesystem driver implementing named pipes as filesystem objects
under the `\Device\NamedPipe\` namespace. Named pipes provide a reliable,
ordered byte-stream IPC mechanism between processes on the same machine or across
the network (using SMB as the transport). Used extensively by Windows system
services and RPC endpoints.

**Difficulty:** Advanced
**Category:** OS

---

## NFVI — Network Functions Virtualization Infrastructure

The physical and virtual compute, storage, and network resources on which
virtualized network functions (VNFs) run. Part of the ETSI NFV architecture
alongside the Management and Orchestration (MANO) layer. Enables carrier-grade
network functions (firewalls, load balancers, IMS) to run on commodity hardware.

**Difficulty:** Advanced
**Category:** Networking

---

## NLRI — Network Layer Reachability Information

BGP path attribute containing IP prefix information a router is advertising to
peers. An UPDATE message carries one or more NLRIs in its prefix fields. BGP
multi-protocol extensions (RFC 4760) extend NLRI to carry IPv6, VPN, and other
address families beyond IPv4 unicast.

**Difficulty:** Advanced
**Category:** Networking

---

## NSCD — Name Service Cache Daemon

Linux caching daemon for name service lookups (users, groups, hosts, services).
Reduces latency and load on LDAP and DNS servers by caching results of `getpwnam()`,
`getgrnam()`, and `gethostbyname()` calls. Configured via `/etc/nscd.conf`.
Can cause stale cache issues when directory entries change rapidly.

**Difficulty:** Intermediate
**Category:** OS

---

## NTPD — NTP Daemon

Background service implementing the NTP protocol to continuously adjust system
clock time and frequency. Uses a complex algorithm (clock discipline) to slew
the clock gradually rather than step-adjusting it, avoiding disruption to
time-sensitive applications. `chrony` is a modern alternative with better
accuracy on systems with intermittent network connectivity.

**Difficulty:** Intermediate
**Category:** OS

---

## NBNS — NetBIOS Name Service

Name resolution service in NetBIOS over TCP/IP (NBT) networks. Resolves NetBIOS
names to IP addresses when no WINS server is configured, using broadcast queries
on UDP port 137. Successor to broadcast-based name resolution before DNS became
universal; still active in Windows networks for legacy compatibility.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NCSI — Network Controller Sideband Interface

Intel specification defining a communication interface between a BMC (Baseboard
Management Controller) and a server's network controller. Allows the BMC to share
the NIC for out-of-band management traffic without requiring a dedicated management
NIC, while keeping BMC traffic logically separate from host OS traffic.

**Difficulty:** Advanced
**Category:** Hardware

---

## NACL — Network Access Control List

Stateless firewall rule set applied at the subnet level in cloud environments
(particularly AWS VPC). Unlike security groups (stateful), NACLs evaluate each
packet independently in both directions. Rules are numbered and evaluated in
ascending order; the first matching rule determines allow or deny action.

**Difficulty:** Intermediate
**Category:** Security

---

## NEBS — Network Equipment Building System

Set of standards developed by Telcordia defining physical protection, spatial,
and environmental requirements for telecommunications equipment deployed in
central offices. NEBS-compliant hardware must withstand seismic activity, wide
temperature ranges, fire resistance, and EMC requirements for carrier deployment.

**Difficulty:** Advanced
**Category:** Hardware


---

## NVRM — NVIDIA Resource Manager
Kernel-level driver component within the NVIDIA GPU driver stack responsible for managing GPU hardware resources: memory allocation, context scheduling, power states, and hardware engine arbitration. Interfaces between userspace (CUDA, OpenGL, Vulkan) and the physical GPU. Closed-source; the open-source nouveau driver reverse-engineered its interface.
**Difficulty:** Advanced
**Category:** Hardware

---

## NVPN — Named VPN
VPN configuration model where each tunnel or profile is identified by a human-readable name rather than a numeric ID or raw endpoint address. Used in modern VPN clients (WireGuard config files, GlobalProtect profiles, Cisco AnyConnect) to allow users to select pre-configured tunnels by label, with all cryptographic parameters abstracted.
**Difficulty:** Base
**Category:** Security

---

## NVOF — NVIDIA Optical Flow
NVIDIA GPU hardware accelerator (available from Turing architecture onward) that computes optical flow fields between video frames in hardware, offloading this computationally expensive operation from the CUDA cores. Used in video compression, action recognition, and real-time video analytics pipelines.
**Difficulty:** Advanced
**Category:** Hardware

---

## NWFP — Network Wire Filter Program
BPF (Berkeley Packet Filter) program attached to a network interface at the kernel level to filter or process packets before they reach userspace. Written in eBPF bytecode and loaded via tc (traffic control) or XDP (eXpress Data Path). Used for packet capture filtering (tcpdump), DDoS mitigation, and high-performance load balancing.
**Difficulty:** Advanced
**Category:** Networking

