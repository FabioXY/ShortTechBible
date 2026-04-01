## ZRAM — Zram (formerly compcache)

Linux kernel module that creates a compressed block device entirely in RAM. Used as a swap device to hold compressed memory pages, effectively expanding usable RAM with CPU overhead. Enabled by default in Android, ChromeOS, and many Linux distributions (Fedora, Ubuntu). Configured via /sys/block/zram0/ and systemd-zram-setup.

**Difficulty:** Intermediate
**Category:** OS


---

## ZERO — Zero-Day Exploit

Vulnerability in software or hardware that is unknown to the vendor and has no available patch at the time of exploitation. The term refers to the zero days of advance warning defenders have. Traded on exploit markets, used by nation-state APTs, and addressed post-disclosure through emergency patches or mitigations.

**Difficulty:** Intermediate
**Category:** Security


---

## ZFCP — Z Fiber Channel Protocol

IBM z/Architecture implementation of Fibre Channel Protocol for connecting mainframes (IBM Z series) to SAN storage. ZFCP adapters attach LUNs to z/OS and Linux on IBM Z, managed via the sysfs interface on Linux (echo to /sys/bus/ccw/drivers/zfcp/) and hardware management console on z/OS.

**Difficulty:** Advanced
**Category:** Hardware


---

## ZFSN — ZFS (Z File System) Snapshot

Atomic, space-efficient point-in-time copy of a ZFS dataset or volume. Snapshots are instantaneous and consume no additional space at creation; they grow only as data diverges (copy-on-write). Listed with zfs list -t snapshot, rolled back with zfs rollback, and cloned with zfs clone. Foundation of ZFS-based backup pipelines.

**Difficulty:** Intermediate
**Category:** OS


---

## ZINC — Zinc (Elasticsearch-compatible search)

Lightweight, Elasticsearch-compatible full-text search engine written in Go. Designed as a low-resource alternative to Elasticsearch for self-hosted environments. Supports Elasticsearch query DSL, mappings, and index APIs, allowing drop-in compatibility with Elasticsearch clients without the JVM overhead.

**Difficulty:** Intermediate
**Category:** Database


---

## ZLIB — Zlib Compression Library

Open-source data compression library implementing the DEFLATE algorithm (LZ77 + Huffman coding). Used as a foundational component in PNG, HTTP Content-Encoding: deflate, ZIP, gzip, and PDF. Available in virtually every programming language. The zlib format wraps DEFLATE with a 2-byte header and Adler-32 checksum.

**Difficulty:** Intermediate
**Category:** Dev


---

## ZMTP — ZeroMQ Message Transport Protocol

Wire-level protocol used by ZeroMQ for framing, versioning, and authenticating messages between sockets. ZMTP 3.x supports NULL, PLAIN, and CURVE security mechanisms. Transport-agnostic: runs over TCP, IPC (Unix sockets), UDP multicast (PGM), WebSocket, and shared memory.

**Difficulty:** Advanced
**Category:** Protocol


---

## ZNAP — Zsh Plugin Manager / ZFS Snapshot Automation

Dual usage: (1) A lightweight Zsh plugin manager that sources plugins and completions from GitHub repos without a dedicated plugin framework. (2) A ZFS snapshot automation tool that schedules, retains, and replicates snapshots based on cron-like policies. Context determines meaning.

**Difficulty:** Intermediate
**Category:** OS


---

## ZPAQ — ZPAQ Archiver

Journaling archiver and lossless compression format with very high compression ratios using context mixing algorithms (PAQ-based). Supports incremental backups: adds only changed files to the archive. Slower than gzip/bzip2 but achieves ratios comparable to or exceeding 7z on text and source code.

**Difficulty:** Advanced
**Category:** OS


---

## ZTNA — Zero Trust Network Access

Security model that replaces traditional VPN-based perimeter access with identity-aware, least-privilege, per-session authentication. Users and devices are continuously verified regardless of network location. Implemented via SSE brokers (Zscaler, Cloudflare Access, Palo Alto Prisma) using reverse proxies and device posture checks.

**Difficulty:** Advanced
**Category:** Security


---

## ZVOL — ZFS Volume

Block device created within a ZFS pool, exposed as a raw disk (e.g. /dev/zvol/poolname/volname). Used to provide block storage for virtual machines (QEMU, bhyve), iSCSI LUNs, and swap. Inherits ZFS features: snapshots, compression, encryption, and replication via zfs send/receive.

**Difficulty:** Intermediate
**Category:** OS


---

## ZXID — Zxid Identity Management

Open-source C library implementing SAML 2.0, Liberty ID-WSF 2.0, and WS-Federation for web SSO and identity federation. Used to add SAML SP or IdP functionality to web applications written in C, Perl, PHP, Java, and Python without a heavyweight application server dependency.

**Difficulty:** Advanced
**Category:** Security


---

## ZDNS — Zone DNS / ZeroMQ DNS

Dual usage: (1) Authoritative DNS zone management system that stores zone data in a relational database rather than flat zone files. (2) The DNS subsystem in containerized environments (Docker, Kubernetes) that provides service discovery within overlay networks using internal DNS resolvers.

**Difficulty:** Intermediate
**Category:** Networking


---

## ZITI — Zero Trust IT Infrastructure

Open-source framework developed by NetFoundry for embedding zero trust networking directly into applications. Provides SDKs for creating dark, software-defined overlay networks where services are not exposed to the public internet. Applications initiate outbound-only connections to a controller, eliminating inbound attack surface.

**Difficulty:** Advanced
**Category:** Security


---

## ZLIM — Zone Limit

Resource limit applied at the zone or container level in operating systems that support OS-level virtualization (Solaris Zones, FreeBSD jails). Constrains CPU shares, memory, swap, and network bandwidth for workloads within the zone, preventing noisy-neighbor effects in multi-tenant deployments.

**Difficulty:** Intermediate
**Category:** OS


---

## ZPKI — Zero-Touch PKI

PKI deployment model that automates the full certificate lifecycle (enrollment, renewal, revocation) without manual intervention. Uses ACME protocol (Let's Encrypt, EJBCA), EST (Enrollment over Secure Transport, RFC 7030), or vendor APIs to issue and renew certificates based on device identity and automated validation.

**Difficulty:** Advanced
**Category:** Security


---

## ZLOG — Zeroconf Logging

Logging framework or protocol that uses zero-configuration discovery (mDNS/DNS-SD, Bonjour) to automatically find and register log aggregation endpoints on the local network. Allows syslog clients and applications to locate a central log collector without static IP or hostname configuration.

**Difficulty:** Intermediate
**Category:** Networking


---

## ZERG — Zone-based Edge Routing Gateway

Routing appliance or software component positioned at the boundary between security zones in segmented network architectures. Enforces inter-zone traffic policies, applies NAT between zones, and logs cross-zone flows. Used in firewall-segmented environments to implement the principle of least-privilege network access between DMZ, internal, and external zones.

**Difficulty:** Advanced
**Category:** Networking


---

## ZPLN — Zeppelin Notebook

Apache Zeppelin: web-based notebook for interactive data analytics, supporting Spark, SQL, Python, R, and Scala interpreters in a single interface. Provides live visualization, collaboration, and parameterized reports. Used in data engineering and ML pipelines for exploratory data analysis on Hadoop and Spark clusters.

**Difficulty:** Intermediate
**Category:** Database


---

## ZMAP — ZMap Network Scanner

Open-source network scanner designed for internet-wide scanning at multi-million packets-per-second rates. Performs stateless TCP SYN, ICMP, and UDP probes without maintaining per-connection state. Used by security researchers for censys.io, vulnerability exposure analysis, and mass scanning of specific port/protocol combinations.

**Difficulty:** Intermediate
**Category:** Security


---

## ZXNG — ZX Next Generation

FPGA-based reimplementation of the ZX Spectrum 8-bit computer. Relevant in retrocomputing and embedded education contexts. Demonstrates FPGA soft-core CPU implementation, bus arbitration, and legacy I/O emulation techniques applicable to modern FPGA-based system design and emulation engineering.

**Difficulty:** Advanced
**Category:** Hardware


---

## ZSTD — Zstandard Compression

Fast lossless compression algorithm and format developed by Facebook (Meta), standardized as RFC 8478. Achieves compression ratios comparable to zlib at significantly higher speeds (both compression and decompression). Used in Linux kernel (since 5.1 for initramfs), Btrfs, SquashFS, Arch Linux packages, and HTTP Content-Encoding: zstd.

**Difficulty:** Intermediate
**Category:** Dev


---

## ZSOC — Zero-Trust Security Operations Center

SOC architecture that applies zero trust principles to security monitoring infrastructure itself. All analyst workstations, SIEM access, and tool integrations are identity-verified and least-privilege provisioned. Prevents lateral movement within the SOC platform in case of analyst credential compromise.

**Difficulty:** Advanced
**Category:** Security


---

## ZNFS — Zoned NFS

NFS deployment pattern where exported shares are organized into security or geographic zones, with different access policies, authentication requirements (Kerberos vs AUTH_SYS), and network paths per zone. Used in multi-tenant and geographically distributed NFS environments to enforce data locality and compliance.

**Difficulty:** Advanced
**Category:** Networking


---

## ZQOS — Zone Quality of Service

QoS policy framework that applies traffic prioritization, bandwidth limits, and DSCP markings on a per-security-zone basis rather than per-interface or per-flow. Implemented in zone-based firewalls (Cisco ZBF, Juniper SRX, Palo Alto) to enforce consistent traffic treatment across all interfaces in a zone.

**Difficulty:** Advanced
**Category:** Networking


---

## ZMOD — Zmodem Protocol

File transfer protocol developed in 1986 for serial and modem connections. Improves on XMODEM and YMODEM with CRC-32 error checking, streaming transfers (no per-packet ACK), crash recovery (resume interrupted transfers), and auto-start. Still supported in terminal emulators (minicom, SecureCRT, Tera Term) for serial console file transfers.

**Difficulty:** Intermediate
**Category:** Protocol


---

## ZKVM — Zero-Knowledge Virtual Machine

Virtual machine architecture that generates cryptographic proofs (ZK-SNARK or ZK-STARK) of correct execution for every computation performed, without revealing the inputs. Enables verifiable, privacy-preserving smart contract execution and off-chain computation with on-chain verification. Examples include RISC Zero, SP1, and Cairo VM.

**Difficulty:** Advanced
**Category:** Security


---

## ZKEY — ZFS Encryption Key

Cryptographic key used to encrypt ZFS datasets with native ZFS encryption (available since OpenZFS 0.8). Managed via zfs key -l (load), zfs key -u (unload), and zfs change-key. Supports raw keys, passphrase-derived keys, and PKCS#11 hardware token integration. Per-dataset keys allow independent encryption boundaries within a pool.

**Difficulty:** Advanced
**Category:** Security


---

## ZPTP — Zero-Touch Provisioning over PTP

Provisioning model that combines ZTP (Zero-Touch Provisioning) for automated network device bootstrap with PTP (IEEE 1588 Precision Time Protocol) synchronization. Ensures newly provisioned switches and routers acquire both configuration and accurate time references before entering production, critical for financial trading and telecom timing networks.

**Difficulty:** Advanced
**Category:** Networking


---

## ZRTP — Z Real-time Transport Protocol

Cryptographic key agreement protocol for SRTP (Secure RTP) media streams, designed by Phil Zimmermann (PGP creator). Uses Diffie-Hellman key exchange within RTP packets with no PKI dependency. Provides end-to-end encryption for VoIP calls; implemented in Linphone, Twinkle, and Signal's early voice encryption. Defined in RFC 6189.

**Difficulty:** Advanced
**Category:** Security


---

## ZTDP — Zero Trust Data Plane

Data plane implementation of zero trust architecture where packet forwarding decisions at the network layer enforce per-flow identity and posture verification rather than relying solely on perimeter-based trust. Implemented via microsegmentation engines, identity-tagged packets (SXP, SGT), and software-defined networking policies.

**Difficulty:** Advanced
**Category:** Security


---

## ZSTR — ZFS Stream

Serialized data stream produced by the zfs send command, encoding dataset snapshots, incremental changes, and optionally raw encrypted data for replication. Received by zfs receive on the destination system. Supports resumable sends (zfs send -t token), compressed streams, and large block support for efficient replication across WAN links.

**Difficulty:** Intermediate
**Category:** OS


---

## ZBUS — Zero Bus

Lightweight, event-driven inter-process communication framework for Linux based on D-Bus semantics. Implements the D-Bus protocol in pure Rust, enabling type-safe service interfaces, signals, and property access between system daemons without the libdbus C library dependency. Used in systemd ecosystem tooling and Flatpak portal interfaces.

**Difficulty:** Advanced
**Category:** OS


---

## ZONE — DNS Zone

Administrative partition of the DNS namespace managed by a specific authority (zone file or DNS server). A zone contains resource records for a contiguous portion of the domain tree. Zone transfers (AXFR, IXFR) replicate zone data from primary to secondary servers. DNSSEC signs zones with RRSIG and DNSKEY records.

**Difficulty:** Intermediate
**Category:** Networking


---

## ZCAT — Zcat Decompressor

Command-line utility that decompresses and prints gzip-compressed files to stdout without creating an uncompressed output file. Functionally equivalent to gunzip -c or zlib decompression piped to stdout. Used in shell pipelines to process compressed logs, archives, and data files without intermediate disk writes.

**Difficulty:** Base
**Category:** OS


---

## ZPBX — Zulu PBX

Open-source Asterisk-based PBX distribution focused on enterprise telephony features. Provides a web-based configuration interface over Asterisk, supporting SIP trunks, IVR, ring groups, call recording, and voicemail. Positioned as a commercial-support alternative to FreePBX in the Asterisk ecosystem.

**Difficulty:** Intermediate
**Category:** Networking


---

## ZTPM — Zero Trust Policy Management

Centralized platform for authoring, distributing, and auditing zero trust access policies across users, devices, applications, and network segments. Integrates identity providers, device posture engines, and network enforcement points (SWG, CASB, microsegmentation) to maintain consistent least-privilege access across hybrid environments.

**Difficulty:** Advanced
**Category:** Security


---

## ZAPI — ZAPI (ONTAP API)

NetApp ONTAP management API providing XML-RPC-style calls over HTTPS for managing storage arrays, volumes, LUNs, aggregates, snapshots, and replication relationships. Being replaced by the ONTAP REST API (v9.6+), but ZAPI remains in use for legacy integrations and features not yet ported to REST.

**Difficulty:** Advanced
**Category:** Hardware


---

## ZPRL — ZFS Pool Resilience Layer

Conceptual layer within ZFS responsible for maintaining pool integrity through RAID-Z (RAID-Z1, RAID-Z2, RAID-Z3) parity schemes, ditto blocks (redundant copies within a pool), and background scrubbing. Ensures data and metadata remain consistent after disk failures without requiring external RAID hardware controllers.

**Difficulty:** Advanced
**Category:** OS


---

## ZCAP — Zone Capability

Authorization primitive in capability-based security systems (object-capability model) that grants a specific set of rights (read, write, execute, delegate) to a resource within a defined zone. Used in Zephyr RTOS, capability-based microkernel research (seL4, Fuchsia), and emerging Web Permissions APIs to replace ambient authority with explicit, unforgeable tokens.

**Difficulty:** Advanced
**Category:** Security



---

## ZINCD — Zinc Search Daemon

Lightweight Elasticsearch-compatible full-text search engine daemon written in Go. Designed as a low-resource alternative to Elasticsearch for self-hosted environments. Supports Elasticsearch query DSL, index mappings, and API compatibility, allowing drop-in use with Elasticsearch clients without JVM or the operational complexity of a full Elastic Stack deployment.

**Difficulty:** Intermediate
**Category:** Database

---

## ZSTRD — Zstd Streaming Mode

Zstandard compression in streaming mode processing data in chunks without requiring the full input in memory. Enables real-time compression of network streams, log pipelines (Fluentd zstd output plugin), and large file transfers. The zstd CLI --stream flag, libzstd streaming API, and kernel integration all support chunk-based streaming compression and decompression.

**Difficulty:** Intermediate
**Category:** Dev


---

## ZINIT — Zsh Plugin Manager

Fast Zsh plugin manager (formerly zplugin) supporting turbo mode for deferred plugin loading after shell startup, reducing interactive shell launch time. Supports loading from GitHub, local paths, and OMZ-compatible plugins. Features include snippet management, binary program management via pack, and ice-modifiers for fine-grained load control.

**Difficulty:** Intermediate
**Category:** OS

---

## ZSWAP — Compressed Swap Cache

Linux kernel feature (since 3.11) implementing a compressed in-memory cache for swap pages. When a page is swapped out, ZSWAP compresses it (using lz4, zstd, or lzo) and stores it in a dynamically allocated pool before writing to the swap device. Reduces swap I/O at the cost of CPU cycles for compression/decompression. Useful on systems with fast CPUs and slow disks.

**Difficulty:** Advanced
**Category:** OS

---

## ZBEAM — Zero-copy Beam

Internal Erlang/OTP VM (BEAM) optimization concept for reducing memory copies when sending large binaries between processes or over network sockets. The BEAM VM uses reference-counted binary heaps shared across processes; binaries above 64 bytes are stored off-process heap and passed by reference rather than copied. Critical for high-throughput Erlang/Elixir network servers.

**Difficulty:** Advanced
**Category:** Dev
