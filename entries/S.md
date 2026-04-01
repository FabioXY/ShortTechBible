## SAN — Storage Area Network

Dedicated high-speed network connecting servers to shared block storage devices.
Uses Fibre Channel (FC) or iSCSI over Ethernet. Storage appears to servers as
locally attached block devices (LUNs). Contrasted with NAS, which provides
file-level access (NFS, SMB) over a standard IP network.

**Difficulty:** Intermediate
**Category:** Hardware

---

## SCSI — Small Computer Systems Interface

Parallel and serial interface standard for connecting and transferring data between
computers and peripheral devices. SAS (Serial Attached SCSI) is the modern serial
variant. The SCSI command set is used by SATA, SAS, USB mass storage, iSCSI,
and Fibre Channel even when the original parallel physical bus is not.

**Difficulty:** Intermediate
**Category:** Hardware

---

## SDLC — Software Development Lifecycle

Structured process covering all phases of software production: planning, requirements,
design, implementation, testing, deployment, and maintenance. Frameworks applying
SDLC principles include Waterfall, Agile (Scrum, Kanban), and DevOps, each
with different phase durations, iteration lengths, and feedback loop speeds.

**Difficulty:** Base
**Category:** Dev

---

## SFTP — SSH File Transfer Protocol

Secure file transfer protocol running as a subsystem over an SSH connection.
Despite the name similarity, it is entirely different from FTP — it uses SSH
encryption and a single connection on port 22. Provides file operations: upload,
download, rename, delete, and directory listing with full path traversal.

**Difficulty:** Base
**Category:** Protocol

---

## SGID — Set Group ID

Unix/Linux file permission bit causing an executable to run with the group
privileges of the file owner rather than the calling user's group. On directories,
SGID causes new files created inside to inherit the directory's group rather
than the creator's primary group. Used to share files within a project group.

**Difficulty:** Advanced
**Category:** OS

---

## SIEM — Security Information and Event Management

Platform aggregating and correlating security event logs from multiple sources
(firewalls, endpoints, IDS) to detect threats, support compliance, and provide
centralized forensic evidence. Examples: Splunk, IBM QRadar, Microsoft Sentinel.
Generates alerts based on correlation rules and behavioral baselines.

**Difficulty:** Intermediate
**Category:** Security

---

## SIMD — Single Instruction Multiple Data

CPU execution model where a single instruction operates on multiple data elements
simultaneously using wide registers (SSE: 128-bit, AVX: 256-bit, AVX-512: 512-bit
on x86; NEON on ARM). Dramatically accelerates multimedia processing, machine
learning inference, and scientific computation through data-level parallelism.

**Difficulty:** Advanced
**Category:** Hardware

---

## SLIP — Serial Line Internet Protocol

Simple encapsulation method (RFC 1055) for sending IP datagrams over serial lines.
Has no framing, error detection, or authentication. A frame is just raw IP data
with a specific delimiter byte. Superseded by PPP which adds these missing features.
Primarily of historical interest now but used in some embedded systems.

**Difficulty:** Advanced
**Category:** Protocol

---

## SMTP — Simple Mail Transfer Protocol

Core email transmission protocol (RFC 5321) for sending messages between mail
servers and from clients to servers. Operates over TCP port 25 (server-to-server)
or port 587 (client submission with STARTTLS). Does not handle retrieval (use
IMAP or POP3). Modern deployments require SPF, DKIM, and DMARC for authentication.

**Difficulty:** Base
**Category:** Protocol

---

## SNMP — Simple Network Management Protocol

Protocol for monitoring and managing network devices. Agents running on devices
expose a Management Information Base (MIB); a manager polls or receives traps
from agents. SNMPv1/v2c use community strings (effectively passwords in plaintext);
SNMPv3 adds authentication (MD5/SHA) and encryption (DES/AES).

**Difficulty:** Intermediate
**Category:** Protocol

---

## SOC — Security Operations Center

Centralized facility monitoring, detecting, analyzing, and responding to cybersecurity
incidents around the clock. SOC analysts use SIEM, EDR, and threat intelligence
tools to investigate alerts and coordinate incident response. Distinct from NOC
(Network Operations Center) which focuses on infrastructure availability.

**Difficulty:** Intermediate
**Category:** Security

---

## SQL — Structured Query Language

Domain-specific language for managing and querying relational databases. Standard
operations: SELECT (retrieve), INSERT (add), UPDATE (modify), DELETE (remove),
CREATE/DROP (schema management). ANSI SQL defines the standard; each RDBMS
extends it with proprietary functions and syntax.

**Difficulty:** Base
**Category:** Database

---

## SRE — Site Reliability Engineering

Engineering discipline applying software engineering principles to infrastructure
and operations problems. Originated at Google. Key practices: defining SLOs
(Service Level Objectives), managing error budgets, measuring toil and automating
it away, and using blameless post-mortems for incident learning.

**Difficulty:** Intermediate
**Category:** Dev

---

## SSH — Secure Shell

Cryptographic network protocol (RFC 4253) providing secure remote login, command
execution, and file transfer over an unsecured network. Replaced Telnet and rsh.
Uses public-key cryptography for server and optional client authentication.
Default port 22. Also tunnels arbitrary TCP connections (port forwarding).

**Difficulty:** Base
**Category:** Security

---

## SSL — Secure Sockets Layer

Predecessor to TLS providing encrypted communications over a computer network.
SSL 2.0 and 3.0 are cryptographically broken (POODLE, DROWN attacks). All SSL
versions are deprecated; TLS 1.2 and 1.3 are the current standards. The term
"SSL" persists colloquially to refer to TLS-based HTTPS connections.

**Difficulty:** Base
**Category:** Security

---

## SSO — Single Sign-On

Authentication property allowing a user to log in once and gain access to multiple
applications without re-authenticating to each. Implemented via SAML 2.0, OIDC,
or Kerberos tickets. An SSO failure creates a single point of authentication
outage for all dependent services.

**Difficulty:** Intermediate
**Category:** Security

---

## SSSD — System Security Services Daemon

Linux daemon providing centralized authentication and identity information for
clients accessing network-based identity providers (LDAP, Active Directory,
Kerberos, FreeIPA). Caches credentials for offline authentication, implements
SUDO rules distribution, and handles NSS and PAM integration on enterprise Linux
systems.

**Difficulty:** Advanced
**Category:** OS

---

## SUDO — Superuser Do

Unix/Linux command allowing permitted users to run commands with elevated (root
or another user's) privileges based on policy defined in `/etc/sudoers`. Logs
each invoked command for audit purposes. More granular than `su` because access
can be restricted to specific commands per user or group.

**Difficulty:** Base
**Category:** OS

---

## SUID — Set User ID

Unix/Linux file permission bit causing an executable to run with the owner's
UID rather than the executing user's UID. Classic examples: `passwd` runs as
root to modify `/etc/shadow`. SUID binaries are high-value targets for privilege
escalation; minimizing their count and auditing them reduces attack surface.

**Difficulty:** Advanced
**Category:** Security

---

## SWAP — Swap Space

Disk area used by the OS as overflow when physical RAM is exhausted. Pages are
moved from RAM to swap (swapped out) to free memory; accessed again pages are
swapped back in (swap in), causing high latency. On Linux, either a swap partition
or a swap file. Modern systems prefer zswap (compressed RAM cache for swap).

**Difficulty:** Intermediate
**Category:** OS

---

## SATA — Serial Advanced Technology Attachment

Storage interface standard for connecting hard drives and SSDs to a motherboard.
SATA III provides 6 Gbps bandwidth. Uses a 7-pin data connector and 15-pin power
connector. Hot-plug capable. Superseded by NVMe/PCIe for performance workloads,
but SATA remains prevalent for high-capacity bulk storage.

**Difficulty:** Base
**Category:** Hardware

---

## SKEL — Skeleton Directory

Template directory (`/etc/skel` on Linux) whose contents are automatically copied
to a new user's home directory when the account is created. Contains default
shell configuration files (`.bashrc`, `.profile`, `.bash_logout`). Administrators
customize `/etc/skel` to provide a standard starting environment for new users.

**Difficulty:** Intermediate
**Category:** OS

---

## SNAT — Source Network Address Translation

NAT mode rewriting the source IP address of outgoing packets. Used when private
hosts behind a NAT router initiate connections to the Internet; the router
replaces the private source IP with its public IP. Opposite of DNAT (Destination
NAT), which rewrites the destination IP for inbound connections.

**Difficulty:** Intermediate
**Category:** Networking

---

## SOAR — Security Orchestration Automation and Response

Platform integrating security tools, automating repetitive analyst tasks, and
orchestrating incident response playbooks. Ingests alerts from SIEM and other
sources, runs automated triage and enrichment, and triggers response actions
(block IP, quarantine host) with minimal human intervention.

**Difficulty:** Intermediate
**Category:** Security

---

## SPOF — Single Point of Failure

Component whose failure causes the entire system to fail. Eliminating SPOFs
requires redundancy at every critical layer: power (UPS, dual PSU), network
(bonding, dual switches), storage (RAID, replication), and application (clustering,
load balancing). Architecture reviews specifically identify and quantify SPOFs.

**Difficulty:** Base
**Category:** Dev

---

## SRTT — Smoothed Round-Trip Time

TCP's running estimate of the round-trip time for a connection, calculated using
an exponentially weighted moving average: SRTT = (1-α) × SRTT + α × RTT_sample.
Used to set the retransmission timeout (RTO). Rapid RTT fluctuations require
the RTTVAR variance component to prevent premature timeouts.

**Difficulty:** Advanced
**Category:** Networking

---

## STRM — Stream

Continuous sequence of data elements made available over time rather than as
a complete dataset. In programming: Java Streams API, Node.js streams, Python
generators. In networking: TCP byte stream, QUIC streams. In data engineering:
Kafka topic streams for real-time event processing pipelines.

**Difficulty:** Base
**Category:** Dev

---

## STUN — Session Traversal Utilities for NAT

Protocol (RFC 5389) allowing hosts behind NAT to discover their public IP address
and port mapping. A client sends a request to a STUN server on the public Internet;
the server returns the observed public source address and port. Used by WebRTC,
SIP, and VoIP clients to establish peer-to-peer connections through NAT devices.

**Difficulty:** Intermediate
**Category:** Protocol

---

## SUBG — Subnet Gateway

Default gateway address within a specific IP subnet acting as the exit point
for traffic destined outside the local subnet. The gateway is the first router
hop; all traffic to non-local destinations is forwarded to the SUBG. Configured
via DHCP option 3 or static network configuration.

**Difficulty:** Base
**Category:** Networking

---

## SWTK — Kernel Software Tracking

Generic term for kernel instrumentation mechanisms that record execution flow,
function call sequences, and timing data for diagnosis and optimization. Includes
Linux tracing infrastructure (ftrace, eBPF, SystemTap) used to identify bottlenecks,
latency spikes, and unexpected code paths in production without recompilation.

**Difficulty:** Advanced
**Category:** OS

---

## SVGA — Super VGA

Display standard extending VGA to higher resolutions (800×600 minimum, commonly
1024×768 and above) and 256+ colors. Defined by the VESA group. SVGA drivers
were required to access extended resolutions before hardware standardization.
Now obsolete as a standard; modern displays use HDMI, DisplayPort, and native
GPU framebuffers.

**Difficulty:** Base
**Category:** Hardware

---

## SYSF — Sysfs Virtual Filesystem

Linux virtual filesystem mounted at `/sys` exposing kernel objects (devices, drivers,
buses, power states) as files and directories. Provides a structured interface
for user space to read device attributes and write configuration without ioctl calls.
Used by udev, NetworkManager, and device management tools.

**Difficulty:** Advanced
**Category:** OS

---

## SMBD — Samba Daemon

Core Samba process providing SMB/CIFS file and print sharing on Unix/Linux systems.
Handles authentication, file locking, and Windows-compatible share access.
Configured via `smb.conf`. Paired with `nmbd` (NetBIOS name service) and `winbindd`
(Windows domain integration) for full Active Directory member functionality.

**Difficulty:** Intermediate
**Category:** OS

---

## SRTE — Segment Routing Traffic Engineering

Network traffic engineering approach using Segment Routing (SR) to define explicit
paths through a network by prepending an ordered list of segment identifiers
(SIDs) to packets. Eliminates per-flow state on intermediate nodes; path
information is carried in the packet header itself.

**Difficulty:** Advanced
**Category:** Networking

---

## SCAP — Security Content Automation Protocol

NIST framework of standards (CVE, CCE, XCCDF, OVAL, CVSS) for automating security
configuration checking, vulnerability measurement, and compliance assessment.
Tools implementing SCAP (OpenSCAP, Nessus) can evaluate systems against CIS
Benchmarks and STIG profiles and produce standardized compliance reports.

**Difficulty:** Advanced
**Category:** Security

---

## SDDC — Software-Defined Data Center

Data center where all infrastructure components (compute, storage, networking)
are virtualized and delivered as a service, managed through software abstraction
layers rather than hardware-specific interfaces. VMware vSphere, NSX, and vSAN
form a common SDDC stack; Nutanix is a hyperconverged alternative.

**Difficulty:** Intermediate
**Category:** Cloud

---

## SCIM — System for Cross-domain Identity Management

Open standard protocol (RFC 7642-7644) for automating user provisioning and
deprovisioning between identity providers and service providers. Defines a REST
API and JSON schema for CRUD operations on users, groups, and entitlements.
Eliminates manual account management when onboarding/offboarding employees across
SaaS applications.

**Difficulty:** Intermediate
**Category:** Security

---

## SLOC — Source Lines of Code

Count of non-blank, non-comment lines of source code in a codebase. Used in
software size estimation and productivity analysis. Tools: `cloc`, `scc`, `tokei`.
Compared across languages using language weighting factors. Subject to the same
criticisms as KLOC as a proxy for complexity or quality.

**Difficulty:** Base
**Category:** Dev

---

## SNTP — Simple Network Time Protocol
Simplified version of NTP (RFC 4330) designed for devices that do not need full NTP accuracy or complexity. Uses the same packet format as NTP but implements only unicast client-server mode without the full clock discipline algorithm. Common in embedded systems, IoT devices, and appliances.
**Difficulty:** Base
**Category:** Protocol


---

## SHELL — Unix Shell Interpreter

Command interpreter providing a user interface to the OS. Parses and executes commands, manages job control, handles I/O redirection (>, >>, <, 2>&1) and pipelines (|). Supports scripting: variables, loops, conditionals, functions. Common shells: bash (default on most Linux), zsh (default on macOS), fish, dash (POSIX minimal, used for /bin/sh on Debian/Ubuntu).

**Difficulty:** Base
**Category:** OS

---

## SMTPS — SMTP Secure Port 465

SMTP over implicit TLS on port 465, where the connection starts encrypted immediately. Re-standardized in RFC 8314 (2018) as the preferred submission port for mail clients. Distinct from STARTTLS on port 587 (upgrades unencrypted connection). Mail relaying between servers still uses port 25 with STARTTLS opportunistic encryption.

**Difficulty:** Intermediate
**Category:** Protocol

---

## SYSMD — Systemd Init System

System and service manager for Linux replacing SysV init. Unit files (.service, .socket, .timer, .mount, .target) declare dependencies and startup order. journald collects structured binary logs queryable via journalctl -u service. Parallel service startup reduces boot time. Provides socket activation, cgroup-based process tracking, and transient service units.

**Difficulty:** Intermediate
**Category:** OS

---

## SFLOW — sFlow Sampling Protocol

Sampling-based network monitoring protocol (RFC 3176) providing continuous traffic analysis at line rate. Samples 1-in-N packets and exports flow records to a collector. More scalable than NetFlow/IPFIX for 100G+ links where full flow export is impractical. Supported by data center switches (Arista, Juniper, Cumulus) for traffic visibility and capacity planning.

**Difficulty:** Advanced
**Category:** Networking

---

## SWARM — Docker Swarm Mode

Native Docker container orchestration mode grouping Docker hosts into a swarm with manager and worker nodes. Services define desired state (replicas, image, ports); the swarm scheduler places containers across workers. Supports rolling updates, service discovery via internal DNS, overlay networks, and secrets management. Simpler than Kubernetes but less feature-rich.

**Difficulty:** Intermediate
**Category:** Cloud

---

## SOCAT — Socket Cat Relay

Multipurpose relay utility for bidirectional byte stream transfer between two addresses. Supports TCP, UDP, Unix sockets, files, processes, SSL/TLS, and VSOCK. More powerful than netcat: supports full-duplex relay, SSL termination, SOCKS proxy. Used for port forwarding, socket debugging, VPN-less tunneling, and creating test listeners.

**Difficulty:** Intermediate
**Category:** Networking

---

## SPARK — Apache Spark Engine

Unified analytics engine for large-scale data processing. In-memory computation provides 10-100x speed improvement over Hadoop MapReduce for iterative algorithms. Supports batch (DataFrame API), streaming (Structured Streaming), ML (MLlib), and graph (GraphX) workloads. APIs in Python (PySpark), Scala, Java, and R. Runs on YARN, Kubernetes, Mesos, or standalone cluster.

**Difficulty:** Advanced
**Category:** Database

---

## SLAAC — Stateless Address Autoconfiguration

IPv6 mechanism (RFC 4862) allowing hosts to self-configure global unicast addresses without DHCP. Combines the /64 prefix from Router Advertisement messages with an Interface Identifier (EUI-64 from MAC or random per RFC 8981 privacy extensions). DNS configuration requires RDNSS option (RFC 8106) in the RA or a separate DHCPv6 stateless server.

**Difficulty:** Intermediate
**Category:** Protocol

---

## SWAGR — Swagger API Spec Tool

Original name for the OpenAPI Specification (OAS): language-agnostic, machine-readable format for REST API definitions. Swagger 2.0 was donated to the OpenAPI Initiative and renamed OpenAPI 3.0. Swagger UI renders interactive API documentation from OpenAPI files; Swagger Codegen generates client SDKs and server stubs in 40+ languages.

**Difficulty:** Intermediate
**Category:** Dev

---

## STELT — Stealth Port Scan

Nmap TCP SYN scan (-sS, half-open scan) sending SYN packets without completing the TCP handshake. Open port: returns SYN-ACK (scanner immediately resets). Closed port: returns RST. Faster and less detectable than full connect scans since no connection is established and many systems do not log incomplete handshakes. Requires raw socket privileges.

**Difficulty:** Intermediate
**Category:** Security

---

## SHMEM — Shared Memory IPC

Inter-process communication mechanism allowing multiple processes to access a common memory region without kernel mediation per data transfer. POSIX API: shm_open, mmap, shm_unlink. System V API: shmget, shmat, shmdt. Fastest IPC method but requires explicit synchronization (mutex, semaphore) to prevent race conditions. Used in databases, video processing, and high-frequency trading.

**Difficulty:** Advanced
**Category:** OS

---

## SALTK — SaltStack Automation

Python-based infrastructure automation tool using a master-minion architecture with ZeroMQ messaging. States (.sls files in YAML+Jinja2) describe desired system configuration. Execution modules run ad-hoc commands across thousands of minions simultaneously. Salt-ssh provides agentless mode over SSH. Acquired by VMware; now part of Broadcom's portfolio.

**Difficulty:** Intermediate
**Category:** Dev


---

## STAP — SystemTap

Linux dynamic tracing framework that compiles probe scripts into kernel modules at runtime. A stap script attaches probes to kernel functions, syscalls, uprobes, and tracepoints; probe handlers execute arbitrary C-like code to collect and aggregate data. Used for performance analysis and debugging without kernel recompilation. Requires debug symbols or DWARF info.

**Difficulty:** Advanced
**Category:** OS

---

## SMAP — Supervisor Mode Access Prevention

x86 CPU security feature (Intel Broadwell+, AMD Zen) that prevents the kernel from accidentally reading or writing userspace memory while running in kernel mode (ring 0). Access must be explicitly allowed via STAC/CLAC instructions around intentional user memory copies (copy_from_user, copy_to_user). Mitigates certain kernel exploitation techniques.

**Difficulty:** Advanced
**Category:** Hardware

---

## SONAR — SonarQube Platform

Continuous code quality and security platform that performs static analysis on source code. Detects bugs, code smells, security vulnerabilities, and measures technical debt. Integrates with CI/CD pipelines via SonarScanner; results displayed on a dashboard with issue tracking. Supports 30+ languages. SonarCloud is the hosted SaaS version.

**Difficulty:** Intermediate
**Category:** Dev

---

## SECAP — Security Capability

Linux capability bit within the kernel's POSIX capabilities model, subdivided into permitted, effective, and inheritable sets per process. Individual capabilities (CAP_NET_ADMIN, CAP_SYS_PTRACE, CAP_SETUID, etc.) grant specific privileged operations without requiring full root. Container runtimes drop all non-required capabilities by default to reduce attack surface.

**Difficulty:** Advanced
**Category:** Security
