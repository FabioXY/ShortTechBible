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


---

## REDIS — Redis Cache Server

In-memory data structure server supporting strings, hashes, lists, sets, sorted sets, streams, and geospatial indexes. Persistence: RDB snapshots and AOF (append-only file). HA via Redis Sentinel; horizontal sharding via Redis Cluster. Commonly used for caching, session storage, pub/sub messaging, rate limiting, and distributed locks (Redlock algorithm).

**Difficulty:** Intermediate
**Category:** Database

---

## REGEX — Regular Expression

Formal language describing string patterns using metacharacters (., *, +, ?, [], {}, ^, $, |, ()). Implemented in virtually every programming language and tool (grep, sed, Perl, Python re, PCRE2). Two main engine types: NFA (backtracking, feature-rich) and DFA (linear time, no backtracking). ReDoS attacks exploit catastrophic backtracking in poorly written expressions.

**Difficulty:** Intermediate
**Category:** Dev

---

## RSYNC — Remote Sync Utility

Unix utility for fast, incremental file and directory synchronization over SSH or rsync daemon protocol. Uses a rolling checksum delta algorithm to transfer only changed file blocks. Preserves permissions, timestamps, symlinks, hardlinks, and ACLs. Key flags: -a (archive), -v (verbose), -z (compress), --delete (mirror), --dry-run (preview). Basis of many backup solutions.

**Difficulty:** Intermediate
**Category:** OS

---

## REALM — Kerberos Auth Realm

Administrative domain in Kerberos containing users, services, and a KDC (Key Distribution Center). Realm names are uppercase by convention, typically matching the DNS domain (EXAMPLE.COM). Cross-realm trust allows principals from one realm to authenticate to services in another. Active Directory domains map one-to-one to Kerberos realms.

**Difficulty:** Intermediate
**Category:** Security

---

## RCLNE — Rclone Cloud Sync

Command-line utility syncing and managing files between local storage and 40+ cloud providers (S3, GCS, Azure Blob, Backblaze B2, Dropbox, OneDrive, SFTP). Supports encrypted remotes, FUSE mounting, bandwidth throttling, server-side copy, and filtering. Used for multi-cloud backup, migration, and mounting S3 buckets as local filesystems.

**Difficulty:** Intermediate
**Category:** Cloud

---

## RTFCT — runc Container Runtime

Low-level OCI container runtime implementing the OCI Runtime Specification. Spawns and manages container processes using Linux namespaces, cgroups v1/v2, and seccomp profiles. Used by Docker (via containerd), Kubernetes (via CRI-O or containerd), and Podman as the default underlying runtime. Alternative runtimes (gVisor, Kata Containers) implement the same OCI interface.

**Difficulty:** Advanced
**Category:** Cloud

---

## RSTLS — Rustls TLS Library

Modern TLS implementation in pure Rust without unsafe code. Implements TLS 1.2 and 1.3 with a focus on memory safety and correctness. No support for legacy protocols (SSL 3.0, TLS 1.0/1.1) or weak cipher suites by design. Used in Cloudflare infrastructure, Actix-web, and Hyper HTTP library. Growing adoption as a safer alternative to OpenSSL.

**Difficulty:** Advanced
**Category:** Security

---

## RPCBM — RPC Bind Mapper

Portmapper service (rpcbind) mapping ONC RPC program numbers to TCP/UDP ports. Clients query rpcbind (port 111) to discover which port a specific RPC service is listening on. Required for NFSv3, NIS, and other ONC RPC services. NFSv4 uses only port 2049 and does not require rpcbind, simplifying firewall rules for NFS.

**Difficulty:** Intermediate
**Category:** Protocol

---

## RPKID — RPKI Validation Daemon

Software daemon implementing Resource Public Key Infrastructure for BGP route origin validation. Fetches Route Origin Authorizations (ROAs) from RPKI repositories, validates cryptographically, and exports Validated ROA Payloads to the BGP router via RTR protocol (RFC 8210). Implementations: Routinator (NLnet Labs), FORT, Cloudflare OctoRPKI.

**Difficulty:** Advanced
**Category:** Networking

---

## RTTMS — RTT Measurement

Round-Trip Time: elapsed time between sending a packet and receiving its acknowledgment. Measured by ping (ICMP), traceroute, and TCP (SRTT — Smoothed RTT per connection). TCP uses RTT to calculate RTO (Retransmission Timeout): RTO = SRTT + 4*RTTVAR. High RTT reduces TCP throughput by limiting congestion window growth.

**Difficulty:** Intermediate
**Category:** Networking

---

## ROOTF — Root Filesystem

Top-level filesystem mounted at / in Unix/Linux systems. Contains essential directories: /bin, /sbin, /etc, /lib, /proc, /sys, /dev, /tmp, /var, /usr, /home. The kernel mounts it at boot from the device specified in the bootloader. Immutable rootfs (read-only root) is used in container images and embedded systems for security and reproducibility.

**Difficulty:** Intermediate
**Category:** OS

---

## RUSTP — Rust Language Toolchain

Rust language ecosystem: Cargo (build system and package manager), crates.io (package registry), Cargo.toml (dependencies), Cargo.lock (reproducible builds). Rust's ownership and borrow checker prevents memory safety bugs at compile time: no use-after-free, no data races, no null pointer dereferences in safe code. Widely adopted for systems programming, WebAssembly, and CLI tools.

**Difficulty:** Intermediate
**Category:** Dev


---

## RBASH — Restricted Bash

Restricted variant of the Bash shell (invoked as rbash or bash -r) that limits the user's ability to change directories, set PATH/SHELL/HISTFILE, redirect output, and execute commands with slashes in their names. Used to create constrained shell environments for service accounts or shared systems. Escape vectors exist; not suitable as a security boundary without additional isolation.

**Difficulty:** Intermediate
**Category:** OS

---

## RPATH — Runtime Library Search Path

ELF binary metadata field specifying directories the dynamic linker searches for shared libraries at runtime, before consulting LD_LIBRARY_PATH and /etc/ld.so.conf. Embedded at link time via -Wl,-rpath,/path. Useful for deploying applications with bundled libraries but can create security issues if writable paths are included. $ORIGIN substitution enables relative rpaths.

**Difficulty:** Advanced
**Category:** OS

---

## RDTSC — Read Time Stamp Counter

x86 instruction that reads the processor's Time Stamp Counter — a 64-bit counter incremented every clock cycle since reset. Used for high-resolution timing in benchmarks, profiling, and latency measurements. Modern CPUs provide a constant-rate TSC (invariant TSC) unaffected by frequency scaling. RDTSCP adds a memory fence and processor ID for serialized reads.

**Difficulty:** Advanced
**Category:** Hardware
