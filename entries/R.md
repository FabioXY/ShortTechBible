## RAM — Random Access Memory

Volatile primary memory providing fast, direct (random) access to any memory
location in constant time. Holds running programs and data; contents are lost
on power failure. Types: DRAM (main system RAM), SRAM (CPU caches). Measured
in capacity (GB) and speed (MHz/MT/s bandwidth).

**Difficulty:** Base
**Category:** Hardware

---

## RBAC — Role-Based Access Control

Access control model where permissions are assigned to roles and users are assigned
to roles, rather than assigning permissions directly to users. Simplifies permission
management in large organizations. Implemented in Kubernetes, AWS IAM, database
systems, and enterprise applications.

**Difficulty:** Intermediate
**Category:** Security

---

## RDBMS — Relational Database Management System

Database management system organizing data into structured tables with predefined
schemas, relationships enforced by foreign keys, and ACID transaction guarantees.
Examples: PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server, SQLite.
Uses SQL for data definition, manipulation, and querying.

**Difficulty:** Base
**Category:** Database

---

## REST — Representational State Transfer

Architectural style for distributed hypermedia systems defined by Roy Fielding.
Key constraints: stateless client-server communication, uniform interface (HTTP
verbs: GET, POST, PUT, DELETE, PATCH), resource identification via URIs, and
representation (typically JSON or XML). The dominant API style for web services.

**Difficulty:** Intermediate
**Category:** Dev

---

## RFC — Request for Comments

Publication format of the IETF and IRTF defining Internet standards, experimental
protocols, best practices, and informational documents. Despite the name, published
RFCs are stable documents. Proposed Standards become full Internet Standards
after two independent implementations. RFC 1 was published in 1969.

**Difficulty:** Base
**Category:** Protocol

---

## RIP — Routing Information Protocol

Distance-vector interior gateway routing protocol using hop count (max 15) as
its metric. Simple to configure but converges slowly on large networks. RIPv2
(RFC 2453) adds CIDR support and authentication. Superseded by OSPF and EIGRP
in all but the smallest network deployments.

**Difficulty:** Intermediate
**Category:** Networking

---

## RPO — Recovery Point Objective

Maximum acceptable amount of data loss expressed as time, measured from the
last backup or recovery point to the moment of failure. An RPO of 1 hour means
the organization tolerates losing at most 1 hour of data. Drives backup frequency
and replication strategy decisions in disaster recovery planning.

**Difficulty:** Intermediate
**Category:** Dev

---

## RTO — Recovery Time Objective

Maximum acceptable duration from a failure event to full service restoration.
An RTO of 4 hours means the system must be operational within 4 hours of outage.
Shorter RTOs require more investment in redundancy, automated failover, and
pre-provisioned standby infrastructure.

**Difficulty:** Intermediate
**Category:** Dev

---

## RTMP — Real-Time Messaging Protocol

TCP-based protocol developed by Adobe for streaming audio, video, and data between
a Flash Media Server and client. Port 1935. Still widely used for ingestion of
live video streams to platforms like YouTube Live and Twitch, even though Flash
is dead. Superseded by HLS and DASH for delivery to end viewers.

**Difficulty:** Intermediate
**Category:** Protocol

---

## RTSP — Real-Time Streaming Protocol

Application-layer protocol (RFC 7826) for controlling streaming media servers.
Acts as a "network remote control" — establishes, controls, and tears down media
sessions, while actual data is typically carried by RTP/RTCP. Used in IP cameras
(ONVIF), VoIP, and multimedia streaming servers.

**Difficulty:** Intermediate
**Category:** Protocol

---

## RDP — Remote Desktop Protocol

Microsoft proprietary protocol providing remote graphical access to a Windows
desktop. Runs on TCP/UDP port 3389. Supports multi-monitor, clipboard sharing,
audio redirection, RemoteFX GPU acceleration, and NLA (Network Level Authentication).
A primary target for brute-force and ransomware attacks when internet-exposed.

**Difficulty:** Intermediate
**Category:** Protocol

---

## RFID — Radio Frequency Identification

Technology using radio waves to wirelessly identify and track tags attached to
objects. Passive tags (no battery) draw power from the reader field; active tags
have their own power source. Frequencies: 125 kHz (access cards), 13.56 MHz
(NFC, Mifare), 900 MHz (supply chain). Common in access control and asset tracking.

**Difficulty:** Intermediate
**Category:** Hardware

---

## ROCE — RDMA over Converged Ethernet

Network protocol enabling Remote Direct Memory Access over standard Ethernet
networks without CPU involvement. The NIC writes data directly into remote host
memory, bypassing the OS and TCP/IP stack. Used in high-performance computing,
AI training clusters, and ultra-low-latency storage (NVMe-oF/RDMA) fabrics.

**Difficulty:** Advanced
**Category:** Networking

---

## RPCF — Remote Procedure Call Framework

Software infrastructure allowing a program to execute procedures on a remote
system as if they were local function calls, abstracting network communication.
Handles serialization (marshaling), transport, and error handling. Modern RPC
frameworks: gRPC (Protocol Buffers over HTTP/2), Apache Thrift, Avro RPC.

**Difficulty:** Intermediate
**Category:** Dev

---

## RSTP — Rapid Spanning Tree Protocol

IEEE 802.1w enhancement to classic STP reducing convergence time from 30–50
seconds to under 1 second. Introduces port roles (root, designated, alternate,
backup) and rapid transition mechanisms. Fully backward compatible with 802.1D STP.
Default STP variant in most modern managed switches.

**Difficulty:** Intermediate
**Category:** Networking

---

## RTOS — Real-Time Operating System

Operating system providing deterministic response times with guaranteed deadlines
for time-critical tasks. Used in embedded systems, industrial control, avionics,
and medical devices. Examples: FreeRTOS, VxWorks, QNX, Zephyr. Hard RTOS
guarantees meeting all deadlines; soft RTOS allows occasional deadline misses.

**Difficulty:** Advanced
**Category:** OS

---

## RRDP — Round Robin Database Protocol

Protocol (RFC 8182) for distributing RPKI (Resource Public Key Infrastructure)
data to relying party software. Allows RPKI validators to efficiently retrieve
delta updates from a notification file and a series of snapshot and delta XML
files from a repository server over HTTPS.

**Difficulty:** Advanced
**Category:** Security

---

## RPKI — Resource Public Key Infrastructure

Cryptographic framework for securing BGP routing by allowing IP address holders
to publish Route Origin Authorizations (ROAs) signed with certificates chaining
to RIR trust anchors. Routers use RPKI-validated ROAs to filter invalid BGP
routes, mitigating route hijacking and BGP prefix hijacking attacks.

**Difficulty:** Advanced
**Category:** Security

---

## RARP — Reverse ARP

Deprecated protocol allowing a diskless workstation to discover its own IP address
from its MAC address by broadcasting to a RARP server. Superseded by BOOTP and
DHCP which provide far more configuration information. Defined in RFC 903 (1984);
no longer used in modern networks.

**Difficulty:** Intermediate
**Category:** Protocol

---

## RDMA — Remote Direct Memory Access

Technology allowing computers to transfer data directly to/from the memory of
a remote host over a network without involving either host's CPU or OS. Eliminates
kernel context switches and data copies in the critical path. Used in InfiniBand,
RoCE, and iWARP for high-performance computing and storage networking.

**Difficulty:** Advanced
**Category:** Networking

---

## REGO — Rego Policy Language

Declarative, purpose-built policy language used by Open Policy Agent (OPA).
Expresses authorization policies, admission control rules, and compliance checks
as logic rules evaluated against JSON input. Used in Kubernetes (OPA Gatekeeper)
to enforce custom admission policies declaratively.

**Difficulty:** Advanced
**Category:** Security

---

## RIPE — Réseaux IP Européens Network Coordination Centre

One of five Regional Internet Registries (RIRs) responsible for allocating and
registering IP addresses and AS numbers in Europe, the Middle East, and Central
Asia. Operates public databases for WHOIS queries, route object registration,
and RPKI certificate management.

**Difficulty:** Intermediate
**Category:** Networking

---

## RRDB — Round Robin Database

Circular storage system where new data overwrites the oldest data once the
database reaches its maximum size. Used in time-series monitoring (RRDtool, Graphite)
to store metric data at decreasing granularity over time without unbounded disk
growth. Ideal for long-term performance trending with configurable consolidation.

**Difficulty:** Intermediate
**Category:** Database

---

## RRSIG — Resource Record Signature

DNSSEC record type containing a digital signature over a set of DNS records.
Each RRSIG covers a specific RRset and includes the signing algorithm, key tag,
validity period, and the signature value. Resolvers with DNSSEC validation
verify RRSIG values against DNSKEY records to authenticate DNS responses.

**Difficulty:** Advanced
**Category:** Protocol

---

## RPS — Receive Packet Steering

Linux kernel feature distributing incoming network packet processing across
multiple CPU cores in software, extending RSS (Receive Side Scaling) to NICs
that lack hardware multi-queue support. Configured via `/sys/class/net/ethX/
queues/rx-N/rps_cpus` bitmask. Reduces per-core interrupt handling bottlenecks.

**Difficulty:** Advanced
**Category:** OS

---

## RPCS — Remote Procedure Call Service

Daemon or service component on a system that listens for and handles incoming
RPC calls. On Unix: `rpcbind` (formerly portmapper) maps RPC program numbers
to network ports. NFS, NIS, and NLM depend on rpcbind for service registration.
Blocking rpcbind effectively disables all RPC-based services.

**Difficulty:** Advanced
**Category:** OS

---

## REPO — Repository

Version-controlled storage location for source code, packages, or configuration.
In Git: a directory containing the codebase history and metadata. In package
management: a server hosting installable packages (APT repo, YUM repo, PyPI).
In DevOps: the source of truth for infrastructure-as-code and CI/CD pipelines.

**Difficulty:** Base
**Category:** Dev

---

## RECV — Receive Buffer

Network socket buffer holding incoming data that has arrived at the kernel but
not yet been read by the application. Tuned via `SO_RCVBUF` socket option or
system-wide sysctl (`net.core.rmem_max`). Oversized receive buffers increase
latency (bufferbloat); undersized buffers cause packet drops under high throughput.

**Difficulty:** Advanced
**Category:** Networking

---

## RMON — Remote Network Monitoring

SNMP extension (RFC 2819) defining a standard set of MIB statistics for detailed
network segment monitoring. RMON1 covers Ethernet statistics (packets, errors,
collisions); RMON2 adds protocol decoding at higher layers. Allows a central
NMS to collect detailed traffic statistics from remote monitoring probes.

**Difficulty:** Advanced
**Category:** Networking

---

## RMTS — Remote Management Terminal Service

Generic term for terminal-server services allowing remote command-line access
to servers and network devices. Encompasses SSH, Telnet (legacy, plaintext),
and serial console access via terminal servers. Essential for managing headless
servers and network equipment without physical presence.

**Difficulty:** Intermediate
**Category:** Networking

---

## RLIM — Resource Limit

OS mechanism bounding the resource consumption of processes to prevent any single
process from exhausting system resources. Configured via `ulimit` in shell or
`setrlimit()` syscall. Limits enforced: open file descriptors (nofile), maximum
memory (as), CPU time, processes (nproc), and core dump size.

**Difficulty:** Intermediate
**Category:** OS

---

## RSAC — RSA Cryptosystem

Public-key cryptographic algorithm named after Rivest, Shamir, and Adleman.
Security relies on the computational difficulty of factoring the product of two
large prime numbers. Used for key exchange, digital signatures, and encryption.
Minimum recommended key size is 2048 bits; 4096 bits for long-term security.

**Difficulty:** Advanced
**Category:** Security

---

## RTBL — Routing Table

Data structure maintained by routers and OS kernels mapping destination network
prefixes to next-hop addresses and outbound interfaces. The kernel consults the
routing table for every packet forwarding decision. Managed via `ip route` (Linux),
`route` (legacy), or router CLI commands. Default route (0.0.0.0/0) is the
gateway of last resort.

**Difficulty:** Intermediate
**Category:** Networking

---

## RNDC — Remote Name Daemon Control

Command-line tool for controlling and administering a BIND DNS server remotely.
Uses a shared secret (TSIG key) for authentication. Common operations: reloading
zone files (`rndc reload`), flushing the cache (`rndc flush`), checking server
statistics, and stopping/starting the daemon gracefully.

**Difficulty:** Intermediate
**Category:** Protocol

---

## RSNA — Robust Security Network Association

IEEE 802.11i framework defining the security mechanisms for WPA2 and WPA3
networks. Encompasses the four-way handshake for deriving session keys from
the PMK, CCMP (AES-based encryption), TKIP (legacy), and the management of
GTKs (Group Temporal Keys) for multicast and broadcast frames.

**Difficulty:** Advanced
**Category:** Security

---

## RTMT — Real-Time Monitoring Tool

Cisco tool for monitoring, configuring alerts, and collecting performance counters
from Cisco Unified Communications Manager (CUCM) clusters. Provides real-time
dashboards for voice quality metrics, call routing performance, and system health
without requiring CLI access to individual servers.

**Difficulty:** Advanced
**Category:** Networking

---

## RJMP — Relative Jump

Assembly language instruction performing a program counter-relative branch to
a target address computed by adding a signed offset to the current PC value.
Used in position-independent code (PIC) and compact instruction sets (AVR
microcontrollers) where shorter relative offsets reduce code size compared to
absolute jumps.

**Difficulty:** Advanced
**Category:** Dev

---

## RRIP — Rock Ridge Interchange Protocol

Extension to the ISO 9660 CD-ROM filesystem standard providing POSIX filesystem
semantics: long filenames, symlinks, device files, file permissions, and UID/GID
ownership. Allows Unix systems to store and retrieve files on CD-ROMs with full
Unix metadata intact, overcoming ISO 9660's 8.3 filename and flat-hierarchy limitations.

**Difficulty:** Advanced
**Category:** OS

---

## RSVP — Resource Reservation Protocol
IETF signaling protocol (RFC 2205) used by hosts and routers to request and reserve network resources (bandwidth, buffer space) along a data path. Forms the basis of IntServ QoS. Operates on a soft-state model where reservations must be periodically refreshed. Less common in modern IP networks where DiffServ is preferred.
**Difficulty:** Advanced
**Category:** Protocol

---

## RTCP — RTP Control Protocol
Companion protocol to RTP that provides out-of-band control and statistics for media streams. Sends RTCP packets (SR, RR, SDES, BYE, APP types) to report packet loss, jitter, and round-trip time. Used by VoIP and video conferencing systems (WebRTC, SIP) to monitor and adapt media quality.
**Difficulty:** Advanced
**Category:** Protocol
