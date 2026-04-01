## LACP — Link Aggregation Control Protocol

IEEE 802.3ad protocol for dynamically negotiating link aggregation (bonding)
between two devices. Both ends exchange LACPDUs to agree on which ports to
combine into a logical trunk for increased bandwidth and redundancy. Requires
a switch that supports LACP; simpler static bonding needs no protocol negotiation.

**Difficulty:** Intermediate
**Category:** Networking

---

## LAMP — Linux Apache MySQL PHP

Traditional open-source web application stack consisting of Linux (OS), Apache
(web server), MySQL (database), and PHP (scripting language). Dominated web
development through the 2000s. Variants include LEMP (Nginx replacing Apache)
and LAPP (PostgreSQL replacing MySQL).

**Difficulty:** Base
**Category:** Dev

---

## LBA — Logical Block Address

Addressing scheme for storage devices that exposes disk sectors as a flat,
zero-indexed array of fixed-size blocks (typically 512 bytes or 4096 bytes).
Abstracts away the physical CHS (Cylinder, Head, Sector) geometry, allowing
the OS and filesystem to address sectors sequentially regardless of drive geometry.

**Difficulty:** Intermediate
**Category:** Hardware

---

## LDAP — Lightweight Directory Access Protocol

Open protocol (RFC 4511) for reading and modifying directory services over TCP/IP.
Organizes entries in a hierarchical DIT (Directory Information Tree) using
Distinguished Names (DNs). Used for centralized authentication and user/group
lookups in enterprise environments. Port 389 (636 for LDAPS over TLS).

**Difficulty:** Intermediate
**Category:** Protocol

---

## LFU — Least Frequently Used

Cache eviction algorithm that removes the entry with the lowest access frequency
when the cache is full. Performs better than LRU for workloads with significant
temporal locality differences between items. Requires maintaining access counters
per entry, adding memory and update overhead compared to LRU.

**Difficulty:** Intermediate
**Category:** Dev

---

## LGA — Land Grid Array

CPU socket design where the electrical contacts (pins) are located on the motherboard
socket rather than on the processor package. The processor die sits on a flat
land grid. Dominant in Intel server (LGA3647, LGA4677) and desktop (LGA1700)
platforms. Easier to replace a bent socket than a bent pin on the CPU.

**Difficulty:** Intermediate
**Category:** Hardware

---

## LRU — Least Recently Used

Cache eviction algorithm that discards the entry not accessed for the longest
time when the cache reaches capacity. Assumes recently accessed data is more
likely to be accessed again (temporal locality). Simple to implement with a
doubly linked list plus hash map. Used by Linux page cache and CPU TLBs.

**Difficulty:** Intermediate
**Category:** Dev

---

## LSM — Linux Security Module

Kernel framework providing hooks for mandatory access control systems to plug
into the kernel without modifying core code. SELinux, AppArmor, and Tomoyo are
LSM implementations. Hooks intercept security-sensitive operations (file open,
socket bind, process fork) and allow or deny based on policy.

**Difficulty:** Advanced
**Category:** Security

---

## LSP — Language Server Protocol

Open protocol (developed by Microsoft) standardizing communication between code
editors and language intelligence backends. An LSP server provides completions,
hover documentation, go-to-definition, and diagnostics; any LSP-compatible editor
can use it. Eliminates per-editor plugin duplication for each language.

**Difficulty:** Intermediate
**Category:** Dev

---

## LTE — Long-Term Evolution

Fourth-generation (4G) mobile broadband standard providing peak downlink speeds
of 100–150 Mbps in typical deployments. Uses OFDMA for downlink and SC-FDMA
for uplink. LTE Advanced (LTE-A) adds carrier aggregation to increase throughput
further. Succeeded by 5G NR in new spectrum deployments.

**Difficulty:** Intermediate
**Category:** Networking

---

## LVM — Logical Volume Manager

Linux storage abstraction layer that pools physical disks (PVs) into volume
groups (VGs) from which logical volumes (LVs) of arbitrary size are carved.
Supports online resizing, snapshots, and striping across multiple disks.
Commonly layered under filesystems like ext4 and XFS in enterprise Linux deployments.

**Difficulty:** Intermediate
**Category:** OS

---

## LXC — Linux Containers

OS-level virtualization technology using Linux namespaces and cgroups to run
isolated user-space environments sharing the host kernel. Lighter than full VMs
but less isolated than hypervisor-based virtualization. Docker's early versions
used LXC; Proxmox LXC containers provide lightweight VM-like environments for
services with minimal overhead.

**Difficulty:** Intermediate
**Category:** OS

---

## LDIF — LDAP Data Interchange Format

Plain-text file format (RFC 2849) for representing LDAP directory entries and
update operations. Used for bulk importing, exporting, and migrating directory
data. Each entry block lists the DN followed by attribute-value pairs. Supported
by all major LDAP servers (OpenLDAP, Active Directory via `ldifde`).

**Difficulty:** Intermediate
**Category:** Protocol

---

## LLC — Logical Link Control

Upper sublayer of the OSI Data Link Layer (Layer 2), defined by IEEE 802.2.
Provides flow control, error checking, and multiplexing of network-layer protocols
over the same MAC layer. In Ethernet, LLC is often bypassed in favor of direct
EtherType fields, but it remains relevant in Wi-Fi and token ring networks.

**Difficulty:** Advanced
**Category:** Networking

---

## LLDP — Link Layer Discovery Protocol

IEEE 802.1AB protocol allowing network devices to advertise their identity,
capabilities, and neighbors over a local network segment. Devices periodically
send LLDPDUs containing chassis ID, port ID, TTL, and optional TLVs (VLAN,
management IP). Used by NMS tools to build accurate network topology maps.

**Difficulty:** Intermediate
**Category:** Networking

---

## LOPS — Lines of Product Source

Software metrics unit counting total source lines across a product's entire
codebase, including all modules, libraries, and configuration files. Distinct
from SLOC (which may exclude comments/blanks) or KLOC (per-thousand). Used
in cost modeling and portfolio sizing at the product level.

**Difficulty:** Base
**Category:** Dev

---

## LTSP — Linux Terminal Server Project

Open-source framework for deploying diskless thin client workstations that boot
over the network from a central Linux server. Clients receive a kernel via PXE,
mount the root filesystem via NFS, and run a desktop session on the server.
Reduces hardware cost and centralizes management for large deployments.

**Difficulty:** Intermediate
**Category:** OS

---

## LUKS — Linux Unified Key Setup

Standard disk encryption specification for Linux block devices. Uses dm-crypt
as the backend and stores key material in a header at the beginning of the
encrypted volume. Supports multiple key slots (up to 32 in LUKS2) allowing
different passphrases for the same volume. Managed with the `cryptsetup` tool.

**Difficulty:** Intermediate
**Category:** Security

---

## LVDS — Low-Voltage Differential Signaling

High-speed, low-power electrical signaling standard using a differential pair
to transmit data. The receiver reads the voltage difference between two wires,
making it immune to common-mode noise. Used for internal display connections
(laptop panels, embedded displays) and high-speed serial links in industrial
and networking equipment.

**Difficulty:** Advanced
**Category:** Hardware

---

## LACR — Link Aggregation Control Record

Internal data structure maintained by LACP-capable switches and network interfaces
tracking the state of each aggregated port, its partner system's MAC address,
operational key, and port priority. Used by the LACP state machine to determine
which ports are active in the aggregated bundle.

**Difficulty:** Advanced
**Category:** Networking

---

## LEMP — Linux Nginx MySQL PHP

Web stack variant of LAMP replacing Apache with Nginx. Nginx's event-driven
architecture handles concurrent connections more efficiently at high traffic loads.
MySQL can be substituted with MariaDB or PostgreSQL. Widely used in modern VPS
and cloud deployments where memory efficiency and performance matter.

**Difficulty:** Base
**Category:** Dev

---

## LKML — Linux Kernel Mailing List

Primary communication channel for Linux kernel development. Patch submissions,
design discussions, bug reports, and release announcements are all conducted
via email threads on LKML. Searchable archives at lkml.org document the entire
history of kernel development decisions since the early 1990s.

**Difficulty:** Intermediate
**Category:** OS

---

## LLVM — Low Level Virtual Machine

Compiler infrastructure project providing a collection of modular, reusable
compiler and toolchain technologies. LLVM IR (Intermediate Representation) is
a target-independent assembly language. Clang is the C/C++ frontend; LLVM
backends exist for x86, ARM, RISC-V, WebAssembly, and NVIDIA GPUs (PTX).

**Difficulty:** Advanced
**Category:** Dev

---

## LNAV — Log File Navigator

Terminal-based log file viewer designed for real-time log analysis. Automatically
detects and parses common log formats, highlights log levels by color, supports
SQL queries against log fields, and follows multiple files simultaneously.
Useful for interactive troubleshooting sessions directly in the terminal.

**Difficulty:** Base
**Category:** Dev

---

## LPAR — Logical Partition

IBM mainframe and Power Systems virtualization concept where a physical server's
resources (CPU, memory, I/O) are partitioned into multiple independent logical
environments. Each LPAR runs its own OS instance. Equivalent to a hypervisor VM
in x86 architecture but managed by the hardware's firmware layer (POWER Hypervisor).

**Difficulty:** Advanced
**Category:** Hardware

---

## LRFU — Least Recently/Frequently Used

Cache eviction policy combining LRU and LFU characteristics. Each cache entry
has a combined weight based on both recency and frequency of access. The entry
with the lowest combined weight is evicted when the cache is full. More adaptive
than either pure LRU or LFU alone for mixed access patterns.

**Difficulty:** Advanced
**Category:** Dev

---

## LSOF — List Open Files

Unix utility displaying all files currently open by processes, including regular
files, directories, sockets, pipes, and device files. Since everything in Unix
is a file, `lsof` is invaluable for network diagnostics (listing open TCP/UDP
sockets), finding which process holds a lock, and debugging file descriptor leaks.

**Difficulty:** Intermediate
**Category:** OS

---

## LTFS — Linear Tape File System

Open standard filesystem for LTO tape drives that presents a tape cartridge like
a removable disk to the OS. Files are written with LTFS metadata allowing random
access by filename without requiring a separate catalog database. Used in media
archives and long-term cold storage workflows.

**Difficulty:** Advanced
**Category:** Hardware

---

## LZMA — Lempel-Ziv-Markov Chain Algorithm

High-ratio lossless compression algorithm used in 7-Zip, XZ, and the Linux kernel
(for compressed kernel images and initramfs). Achieves better compression ratios
than DEFLATE (used in gzip/zip) at the cost of significantly higher compression
CPU time and memory usage. Decompression is fast and uses less memory.

**Difficulty:** Intermediate
**Category:** Dev

---

## LAAS — Logging as a Service

Cloud or managed service providing centralized log ingestion, indexing, storage,
and querying without self-hosting the infrastructure. Examples: Datadog Logs,
Splunk Cloud, AWS CloudWatch Logs. Allows teams to search and alert on logs at
scale without managing Elasticsearch clusters or disk capacity.

**Difficulty:** Intermediate
**Category:** Cloud

---

## LCFS — Last Come First Served

Scheduling discipline (also called LIFO scheduling) where the most recently
arrived job or request is processed first. Rarely used in practice because it
can cause starvation of older requests. Appears in some stack-based execution
models and cache replacement analysis as a theoretical baseline.

**Difficulty:** Intermediate
**Category:** OS

---

## LOIC — Low Orbit Ion Cannon

Open-source network stress testing tool that gained notoriety as a DDoS weapon
used by hacktivist groups. Floods a target with TCP, UDP, or HTTP requests from
a single machine or coordinated botnet. Named for a fictional weapon in the
Command & Conquer game series.

**Difficulty:** Intermediate
**Category:** Security

---

## LPIC — Linux Professional Institute Certification

Vendor-neutral Linux certification program by the Linux Professional Institute.
Three levels: LPIC-1 (system administrator basics), LPIC-2 (advanced administration),
LPIC-3 (enterprise-level specializations in mixed environments, security,
and virtualization). Recognized globally in Linux system administration careers.

**Difficulty:** Base
**Category:** OS

---

## LSIO — LinuxServer.io

Community maintaining a large collection of Docker images for self-hosted
applications with a consistent design: unified base images, regular automated
updates, non-root container execution, and environment-variable-based configuration.
Popular in home lab communities for services like Plex, Sonarr, and Nextcloud.

**Difficulty:** Base
**Category:** Cloud

---

## LSST — Large-Scale System Testing

Testing discipline focused on validating the behavior of IT systems under
realistic or extreme load conditions at full production scale. Covers performance,
failover, data consistency under concurrent load, and degradation profiles.
Distinct from unit or integration testing; requires dedicated infrastructure.

**Difficulty:** Intermediate
**Category:** Dev

---

## LZSS — Lempel-Ziv-Storer-Szymanski

Lossless compression algorithm variant of LZ77 that only outputs a reference
when it results in a smaller output than the raw literal. Used in early game
cartridge compression and embedded firmware due to extremely simple decoder
implementation. Successor to LZ77; basis for many embedded compression formats.

**Difficulty:** Advanced
**Category:** Dev

---

## LURK — Lightweight Upstream Retry and Keep-alive

Protocol extension concept for delegating short-lived TLS session key operations
to a trusted backend server rather than performing them on edge nodes. Allows
CDN edge servers to establish TLS sessions using keys stored securely in a
customer's private infrastructure without exposing the private key.

**Difficulty:** Advanced
**Category:** Security

---

## LPWA — Low Power Wide Area

Class of wireless network technology designed for IoT devices requiring long
range with minimal power consumption and low data rates. Examples: LoRaWAN,
Sigfox, NB-IoT, LTE-M. Trade off bandwidth for battery life measured in years,
covering distances of kilometers from a single gateway.

**Difficulty:** Intermediate
**Category:** Networking

---

## LRAT — Log Retention and Archiving Tool

Generic term for software responsible for managing the lifecycle of log data:
ingestion, compression, tiered storage migration, retention policy enforcement,
and secure deletion. Examples: Logstash with lifecycle policies, Graylog, and
cloud-native solutions like AWS S3 Intelligent-Tiering for log archives.

**Difficulty:** Intermediate
**Category:** Dev

---

## LUNS — Logical Unit Numbers

Plural reference to LUN (Logical Unit Number) identifiers used in SCSI and
SAN storage environments. Each LUN represents a discrete addressable storage
unit (volume) presented by a storage array to a host. Zoning and masking
configurations control which hosts can see and access specific LUNs over Fibre
Channel or iSCSI fabrics.

**Difficulty:** Intermediate
**Category:** Hardware


---

## LINUX — Linux Kernel

Open-source Unix-like monolithic kernel created by Linus Torvalds in 1991. Written in C with architecture-specific assembly. Key subsystems: CFS process scheduler, virtual memory manager, VFS (virtual file system), TCP/IP networking stack, Netfilter, device driver model, and eBPF runtime. Licensed under GPLv2. Basis of Android, embedded systems, and the majority of global server infrastructure.

**Difficulty:** Base
**Category:** OS

---

## LBAAS — Load Balancer as a Service

Cloud networking service providing on-demand load balancing without managing appliances. Examples: AWS ALB/NLB, Azure Load Balancer, GCP Cloud Load Balancing, OpenStack Octavia. Features: health checks, SSL termination, session persistence, autoscaling integration, and WAF attachment. Billed per hour and per gigabyte of processed traffic.

**Difficulty:** Intermediate
**Category:** Cloud

---

## LUSTRE — Lustre File System

High-performance parallel distributed file system used in HPC. Architecture: Metadata Servers (MDS/MDT) handle namespace operations; Object Storage Servers (OSS/OST) handle data. Clients mount Lustre via kernel module, striping files across multiple OSTs for parallel I/O throughput reaching hundreds of GB/s. Used in the majority of top 500 supercomputers.

**Difficulty:** Advanced
**Category:** Hardware

---

## LOGFM — Log Format Standard

Specification defining the structure and fields of log output for a service or application. Common formats: Apache Combined Log Format, JSON structured logging, syslog RFC 5424, W3C Extended Log Format. Structured JSON logs are preferred in observability stacks (Loki, Splunk, Elasticsearch) for machine-readable field parsing and search.

**Difficulty:** Base
**Category:** Dev

---

## LOGRT — Log Rotation Config

Process and configuration archiving current log files and creating new empty ones to prevent unlimited disk growth. Managed by logrotate on Linux (/etc/logrotate.d/). Rotation strategies: size-based, time-based (daily, weekly), or count-based. Signals (SIGHUP) reload daemons after rotation so they open new file descriptors on the new log file.

**Difficulty:** Intermediate
**Category:** OS

---

## LSYND — Lsyncd Live Sync

Live Syncing Daemon watching directories using inotify (Linux) or kqueue (BSD) and triggering rsync on changes. Provides near-real-time file replication between servers with configurable delay batching to avoid excessive sync invocations during rapid file changes. Used for web content replication, active-active NFS alternatives, and incremental backup triggers.

**Difficulty:** Intermediate
**Category:** OS

---

## LSSOF — lsof File Inspector

List Open Files: Unix/Linux diagnostic tool displaying all files (regular files, sockets, pipes, device nodes) opened by running processes. Used to find which process holds a lock, which ports are listening (lsof -i :443), and which deleted files are keeping disk space allocated. Key options: -p (by PID), -u (by user), -i (by network connection).

**Difficulty:** Intermediate
**Category:** OS

---

## LTERM — Linux Terminal Emulator

Graphical terminal emulator providing a command-line interface to the shell. Common emulators: GNOME Terminal, Konsole, Alacritty, WezTerm, xterm. Implement VT100/VT220/xterm escape sequences for cursor control, color (256-color, true color), and formatting. Session multiplexers (tmux, screen) add persistence, window management, and split panes.

**Difficulty:** Base
**Category:** OS

---

## LWIP — Lightweight IP Stack

Open-source TCP/IP stack for embedded systems with severe memory constraints (tens of KB RAM). Implements IPv4/IPv6, TCP, UDP, DHCP, DNS, ICMP, SNMP, and PPP. Used in microcontrollers (STM32, ESP32, ESP8266) and RTOS environments (FreeRTOS+TCP, Zephyr). Configurable to trade feature completeness for memory footprint.

**Difficulty:** Advanced
**Category:** Hardware

---

## LOGLV — Log Level Hierarchy

Severity classification for log messages controlling which messages are emitted and stored. Standard levels (syslog RFC 5424, lowest to highest severity): DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL, ALERT, EMERG. Application frameworks (Log4j, Python logging, Winston) implement similar hierarchies. Production systems typically emit WARNING and above.

**Difficulty:** Base
**Category:** Dev

---

## LZONE — DNS Local Zone Override

DNS zone configured on a resolver to override public DNS responses for specific domains with local records. Used for split-horizon DNS (returning internal IPs for internal queries), development overrides, and ad/malware blocking (RPZ — Response Policy Zones). Configured in BIND via zone blocks, Unbound via local-zone/local-data, or Pi-hole custom DNS entries.

**Difficulty:** Intermediate
**Category:** Networking


---

## LLDB — Low Level Debugger

Debugger developed by the LLVM project as a modern alternative to GDB. Supports C, C++, Objective-C, and Swift debugging with a consistent Python scripting API, structured data inspection, and expression evaluation using the Clang/LLVM infrastructure. Default debugger in Xcode. Provides memory and register inspection, breakpoints, watchpoints, and remote debugging via GDB server protocol.

**Difficulty:** Intermediate
**Category:** Dev

---

## LKRG — Linux Kernel Runtime Guard

Loadable kernel module implementing runtime integrity checking for the Linux kernel. Monitors kernel text, read-only data, and process credentials for unauthorized modifications. Detects rootkit techniques such as syscall table hijacking, function pointer overwriting, and privilege escalation attempts. Developed by the Openwall Project.

**Difficulty:** Advanced
**Category:** Security

---

## LGTM — Looks Good To Me

Code review approval signal used in pull request workflows to indicate a reviewer has inspected changes and approves merging. Popularized as text comment, later formalized in GitHub review approvals. Also the name of GitHub's now-retired static analysis platform (LGTM.com) based on CodeQL, replaced by GitHub Advanced Security.

**Difficulty:** Base
**Category:** Dev
