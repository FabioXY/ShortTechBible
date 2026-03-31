# P

## PAM — Pluggable Authentication Modules

Linux/Unix framework allowing system administrators to configure authentication
policies without modifying individual applications. Each service references a
PAM stack in `/etc/pam.d/`; modules in the stack handle authentication, account
validation, password management, and session setup independently and composably.

**Difficulty:** Advanced
**Category:** Security

---

## PAT — Port Address Translation

Specific form of NAT where both IP address and port number are translated, allowing
thousands of private hosts to share a single public IP. The gateway maintains
a table of (private IP, private port) → (public IP, public port) mappings.
Also called NAPT or IP masquerading in Linux terminology.

**Difficulty:** Intermediate
**Category:** Networking

---

## PBX — Private Branch Exchange

Private telephone switching system within an organization routing calls between
internal extensions and connecting to the public telephone network. Modern IP
PBXes (Asterisk, FreePBX) use VoIP protocols (SIP, H.323) over IP networks
rather than traditional TDM circuits.

**Difficulty:** Intermediate
**Category:** Networking

---

## PCI — Peripheral Component Interconnect

Parallel computer bus standard (32/64-bit) introduced by Intel in 1992 for
connecting peripheral devices to a motherboard. Superseded by PCI Express (PCIe)
in the mid-2000s. PCI devices share a bus; all devices see all transactions.
Still found on legacy industrial and embedded hardware.

**Difficulty:** Intermediate
**Category:** Hardware

---

## PCIE — PCI Express

High-speed serial interconnect standard replacing parallel PCI. Uses point-to-point
lanes (x1, x4, x8, x16) each providing bidirectional bandwidth. PCIe 5.0 provides
32 GT/s per lane. Used for GPUs, NVMe SSDs, NICs, and FPGA cards. Backward
compatible across generations in both physical slots and protocol.

**Difficulty:** Intermediate
**Category:** Hardware

---

## PDU — Protocol Data Unit

Generic term for the unit of data at a specific OSI layer. At Layer 2: frame.
Layer 3: packet. Layer 4: segment (TCP) or datagram (UDP). Layer 7: message.
Also refers to Power Distribution Units in data centers — rack-mounted devices
distributing power to servers with optional remote monitoring and switching.

**Difficulty:** Base
**Category:** Networking

---

## PHP — PHP Hypertext Preprocessor

Server-side scripting language originally designed for web development. Code
executes on the server and generates HTML sent to the client. Powers approximately
75% of server-side web applications including WordPress, Drupal, and Joomla.
Modern PHP (8.x) includes JIT compilation, typed properties, and fibers.

**Difficulty:** Base
**Category:** Dev

---

## PKI — Public Key Infrastructure

System of policies, processes, and technologies managing digital certificates
and public/private key pairs. A Certificate Authority (CA) issues signed X.509
certificates binding a public key to an identity. Enables TLS, email signing,
code signing, and mutual authentication in enterprise environments.

**Difficulty:** Intermediate
**Category:** Security

---

## PLC — Programmable Logic Controller

Industrial computer designed for real-time control of manufacturing processes.
Executes ladder logic or structured text programs reading digital/analog inputs
and controlling outputs (motors, valves, actuators). Used in SCADA systems;
requires strict network isolation from IT networks due to legacy security design.

**Difficulty:** Intermediate
**Category:** Hardware

---

## POP3 — Post Office Protocol Version 3

Simple email retrieval protocol (RFC 1939) that downloads messages from a server
to the client and optionally deletes them from the server. Stateless and limited
compared to IMAP: no server-side folder management or state synchronization.
Port 110 (995 for POP3S over TLS). Still used for simple single-device email clients.

**Difficulty:** Base
**Category:** Protocol

---

## POSIX — Portable Operating System Interface

Family of IEEE standards (1003.x) defining the API for Unix-compatible operating
systems. Covers system calls, shell, utilities, and threading. POSIX compliance
enables portable application development across Linux, macOS, BSD, and commercial
Unix. Programs using POSIX APIs compile and run without modification across
compliant systems.

**Difficulty:** Intermediate
**Category:** OS

---

## PPP — Point-to-Point Protocol

Data link protocol (RFC 1661) for direct connections between two nodes over
serial lines, phone lines, or tunnels. Provides framing, authentication (PAP,
CHAP), compression, and multiprotocol support via NCPs (LCP, IPCP). Used in
dial-up modems, DSL (PPPoE), and VPN tunnels (PPTP, L2TP).

**Difficulty:** Intermediate
**Category:** Protocol

---

## PPTP — Point-to-Point Tunneling Protocol

VPN protocol developed by Microsoft encapsulating PPP frames inside GRE tunnels
over TCP/IP. Uses TCP port 1723 for control and GRE (protocol 47) for data.
Provides MPPE encryption but with serious known vulnerabilities (MS-CHAPv2
is cryptographically broken). Considered insecure; replaced by L2TP/IPsec,
OpenVPN, and WireGuard.

**Difficulty:** Intermediate
**Category:** Security

---

## PTZ — Pan-Tilt-Zoom

Camera system with remote-controllable horizontal (pan), vertical (tilt), and
optical zoom capabilities. Common in security surveillance and video conferencing.
PTZ cameras are controlled via RS-485 serial (Pelco-D/P protocols) in CCTV
systems or via IP-based protocols (ONVIF, VISCA over IP) in modern installations.

**Difficulty:** Intermediate
**Category:** Hardware

---

## PXE — Preboot Execution Environment

Intel specification enabling a computer to boot from a network server before
loading the local OS. The client uses DHCP to get an IP and TFTP server address,
downloads a network boot program (NBP), and continues to load a full OS or
installer. Used in mass OS deployment, diskless workstations, and recovery systems.

**Difficulty:** Intermediate
**Category:** Networking

---

## PMTU — Path MTU

The maximum packet size that can traverse an entire network path without IP-level
fragmentation. Determined by PMTU Discovery (RFC 1191): the source sends large
packets with the DF (Don't Fragment) bit set and observes ICMP "fragmentation
needed" responses to find the minimum MTU along the path.

**Difficulty:** Intermediate
**Category:** Networking

---

## PSTN — Public Switched Telephone Network

The traditional global circuit-switched telephone network built from copper wire,
fiber, and microwave links. Uses 64 kbps PCM-encoded voice channels and TDM
multiplexing. Rapidly being replaced by VoIP and all-IP infrastructure, but
still serves as an emergency fallback and reaches locations without broadband.

**Difficulty:** Intermediate
**Category:** Networking

---

## PSK — Pre-Shared Key

Symmetric cryptographic key distributed to all parties before communication begins,
without a PKI or key exchange protocol. Used in WPA2-Personal Wi-Fi, IPsec tunnel
configurations, and simple VPN setups. Simpler than PKI but requires a secure
out-of-band key distribution mechanism and scales poorly with many participants.

**Difficulty:** Intermediate
**Category:** Security

---

## POC — Proof of Concept

Working demonstration of a proposed solution at minimal scale and fidelity,
designed to validate feasibility before committing to full development. In
security: a PoC exploit demonstrates that a vulnerability is genuinely exploitable,
proving the risk is real rather than theoretical.

**Difficulty:** Base
**Category:** Dev

---

## PRTG — Paessler Router Traffic Grapher

Commercial network monitoring software providing SNMP-based monitoring, flow
analysis (NetFlow, sFlow), bandwidth graphs, and alerting for IT infrastructure.
Uses a sensor-based licensing model. Popular in small-to-medium enterprise
environments for its ease of deployment and wide device support.

**Difficulty:** Intermediate
**Category:** Networking

---

## PKCS — Public Key Cryptography Standards

Set of standard specifications published by RSA Security (now managed by OASIS).
Key standards: PKCS#1 (RSA), PKCS#7 (CMS/signed data), PKCS#8 (private key info),
PKCS#11 (cryptographic token interface for HSMs and smart cards), PKCS#12 (PFX
archive combining cert and private key).

**Difficulty:** Advanced
**Category:** Security

---

## PNAT — Port Network Address Translation

Synonym for PAT/NAPT. Emphasizes the port-translation aspect of the NAT operation
where source port numbers are remapped alongside IP addresses. Common in firewall
and NAT documentation from vendors like Check Point and Juniper.

**Difficulty:** Intermediate
**Category:** Networking

---

## PRNG — Pseudorandom Number Generator

Algorithm that produces a sequence of numbers approximating true randomness from
an initial seed value. Deterministic: same seed always produces the same sequence.
Non-cryptographic PRNGs (Mersenne Twister) are fast but predictable if the seed
is known. CSPRNGs (ChaCha20, AES-CTR) provide unpredictability for security uses.

**Difficulty:** Intermediate
**Category:** Security

---

## PRTK — Password Recovery Toolkit

Commercial forensic tool (AccessData) for password cracking using dictionary
attacks, hybrid attacks, brute force, and rainbow tables against various file
and archive formats. Used in digital forensics and law enforcement investigations
to recover passwords from encrypted evidence.

**Difficulty:** Advanced
**Category:** Security

---

## PROM — Programmable Read-Only Memory

Type of ROM that can be programmed once after manufacture by electrically blowing
fuses on the chip. Once programmed, contents are permanent. Superseded by
EPROM (erasable with UV light), EEPROM (electrically erasable), and Flash memory.
Still used for field-programmable logic where single-time programming is acceptable.

**Difficulty:** Advanced
**Category:** Hardware

---

## PULL — Pull Request

Mechanism in distributed version control (Git) for proposing code changes to
a repository. A contributor pushes changes to a branch, then opens a pull request
(PR) to merge it into the main branch. Code review, CI pipeline results, and
approval gates happen within the PR before merging.

**Difficulty:** Base
**Category:** Dev

---

## PUSH — Push Notification

Mechanism for servers to send real-time data to clients without the client polling.
In mobile: APNs (Apple) and FCM (Google) deliver push notifications via persistent
connections. In web: WebPush (RFC 8030) and WebSockets. In Git: uploading local
commits to a remote repository.

**Difficulty:** Base
**Category:** Dev

---

## PVST — Per-VLAN Spanning Tree

Cisco proprietary extension to IEEE 802.1D STP that runs a separate Spanning
Tree instance for each VLAN. Allows different VLANs to have different root bridges
for load balancing across redundant links. PVST+ adds interoperability with
IEEE 802.1Q trunks. Replaced by MSTP in modern large-scale VLAN deployments.

**Difficulty:** Intermediate
**Category:** Networking

---

## PWSH — PowerShell

Cross-platform task automation and configuration management shell and scripting
language built on .NET. Uses cmdlets (verb-noun named commands) that operate
on .NET objects rather than text streams. PowerShell Core (7.x) runs on Linux
and macOS in addition to Windows, enabling cross-platform automation workflows.

**Difficulty:** Intermediate
**Category:** OS

---

## PBKD — Password-Based Key Derivation

Cryptographic process converting a human-memorable password into a fixed-length
cryptographic key suitable for use in symmetric encryption. Applies a hash function
many thousands of times with a random salt to slow brute-force attacks. PBKDF2
(RFC 8018) is the most widely used standard; Argon2 is the modern recommended
alternative.

**Difficulty:** Advanced
**Category:** Security

---

## PCAP — Packet Capture

File format and library (libpcap) for capturing raw network packets from a
network interface. `.pcap` files are analyzed with Wireshark, tcpdump, or
tshark. PCAP-ng (next generation) extends the format to support multiple interfaces,
nanosecond timestamps, and per-packet metadata in a single capture file.

**Difficulty:** Intermediate
**Category:** Networking

---

## PMTS — Path MTU Selection

Process by which a TCP/IP stack dynamically selects the optimal packet size for
a given network path to avoid fragmentation while maximizing throughput. Combines
PMTU Discovery results with MSS negotiation. Failures in this process (e.g.,
firewalls blocking ICMP) cause connectivity issues in real-world networks.

**Difficulty:** Advanced
**Category:** Networking

---

## PROC — Process (in /proc context)

Virtual filesystem in Linux (`/proc`) exposing kernel and process information
as pseudo-files readable by user space. Contains per-process directories with
memory maps, file descriptors, status, and resource limits, plus system-wide
files for CPU info, memory stats, and kernel parameters (sysctl via `/proc/sys`).

**Difficulty:** Intermediate
**Category:** OS

---

## PING — Packet Internet Groper

Network diagnostic utility using ICMP Echo Request/Reply messages to test
reachability of a host and measure round-trip time. The name is also a backronym
derived from sonar terminology. `ping` is often the first diagnostic command
run when troubleshooting network connectivity issues.

**Difficulty:** Base
**Category:** Networking

---

## PXEL — PXE Loader

Second-stage bootloader component in a PXE boot chain, loaded after the initial
PXE ROM code. Commonly a small executable (pxelinux.0, grubx64.efi) fetched
via TFTP that presents a boot menu, fetches the kernel and initrd, and passes
the correct boot parameters to start the OS installer or live environment.

**Difficulty:** Advanced
**Category:** OS

---

## PITR — Point-in-Time Recovery

Database backup and recovery technique allowing restoration of data to any
specific moment within a retention window. PostgreSQL PITR uses a base backup
plus continuous WAL (Write-Ahead Log) archiving. Combined with streaming
replication, enables sub-second recovery point objectives in production databases.

**Difficulty:** Advanced
**Category:** Database

---

## PNAC — Port-based Network Access Control

IEEE 802.1X-based framework controlling access to network infrastructure ports.
A supplicant (device) authenticates to an authenticator (switch/AP) via an
EAP method; the authenticator communicates with a RADIUS authentication server
to grant or deny port access based on identity and policy.

**Difficulty:** Advanced
**Category:** Security

---

## PRTG — Paessler Router Traffic Grapher

Wait, PRTG already used. Replacing with:

## PVRS — Physical Volume Resource Set

LVM concept grouping multiple Physical Volumes (PVs) into a Volume Group (VG).
The VG represents the total available storage pool from which Logical Volumes
(LVs) are carved. The VG abstraction allows adding new PVs online to expand
the storage pool without unmounting existing logical volumes.

**Difficulty:** Advanced
**Category:** OS

---

## PAKE — Password Authenticated Key Exchange

Cryptographic protocol allowing two parties to establish a shared secret using
only a password, without transmitting the password itself. Provides mutual
authentication without a PKI. Examples: SRP (RFC 5054), SPEKE, and OPAQUE
(used in iCloud Keychain). Prevents phishing and server database compromise
from revealing passwords.

**Difficulty:** Advanced
**Category:** Security

---

## PROF — Profiler

Development tool measuring program performance by sampling or instrumenting code
execution. Records which functions consume the most CPU time, memory allocations,
and call frequencies. Types: sampling profilers (perf, py-spy) measure with
minimal overhead; instrumentation profilers (gprof) add code to every function.

**Difficulty:** Intermediate
**Category:** Dev
