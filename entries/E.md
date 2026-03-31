## EAL — Evaluation Assurance Level

A numerical grade (EAL1–EAL7) in the Common Criteria for Information Technology Security Evaluation (ISO/IEC 15408) indicating the rigor and depth of a security product's evaluation. Higher EAL levels require more extensive testing, formal verification, and documentation. EAL4 is the highest level practically achieved by commercial products; EAL6–7 require near-formal mathematical proofs and are typical of government/military systems.

**Difficulty:** Advanced
**Category:** Security

---

## EAP — Extensible Authentication Protocol

A framework (not a single protocol) supporting multiple authentication methods over PPP and 802.1X. EAP carries authentication exchanges between a supplicant and authentication server (RADIUS). Common EAP methods: EAP-TLS (certificate-based, strongest), EAP-TTLS, PEAP (password over a TLS tunnel). The access point acts as an EAP pass-through authenticator.

**Difficulty:** Advanced
**Category:** Security

---

## EBGP — External BGP

The BGP session type established between routers in different autonomous systems (ASes). eBGP peers are typically directly connected (TTL=1 by default; multi-hop eBGP requires explicit configuration) and exchange full internet routing tables. eBGP routes receive a lower administrative distance than iBGP routes (iBGP = internal BGP, within the same AS). Route policies are applied on eBGP sessions to control what is advertised and accepted.

**Difficulty:** Advanced
**Category:** Networking

---

## EBPF — Extended Berkeley Packet Filter

A Linux kernel subsystem providing a sandboxed virtual machine allowing user-defined programs to run safely in kernel context, triggered by kernel events (system calls, network packets, tracepoints, kprobes). eBPF programs are verified by the kernel's verifier before loading. Used for high-performance observability (Cilium, bpftrace, Pixie), networking (XDP, tc filters), and security enforcement (Falco, Tetragon) without kernel modules.

**Difficulty:** Advanced
**Category:** OS

---

## EBS — Elastic Block Store

AWS's network-attached block storage service providing persistent volumes for EC2 instances. EBS volumes are available in multiple types (gp3, io2, st1, sc1) optimized for IOPS, throughput, or cost. Volumes persist independently of the instance lifecycle and can be snapshotted to S3. EBS multi-attach allows a single io1/io2 volume to be attached to multiple instances in the same AZ for clustered workloads.

**Difficulty:** Intermediate
**Category:** Cloud

---

## ECB — Electronic Codebook

The simplest block cipher mode of operation: each block of plaintext is encrypted independently with the same key. ECB is insecure because identical plaintext blocks produce identical ciphertext blocks, revealing data patterns. The classic demonstration is encrypting a bitmap image — structures remain visible in the ciphertext. ECB must never be used for encrypting more than one block of data.

**Difficulty:** Intermediate
**Category:** Security

---

## ECC — Error-Correcting Code (memory)

RAM with additional bits per word that detect and correct single-bit errors and detect double-bit errors using Hamming or Reed-Solomon codes. ECC memory adds 8 bits per 64-bit data word. Required in servers, workstations, and any environment where silent data corruption is unacceptable — cosmic rays and electrical noise cause bit flips at a frequency that matters at scale and for long-running processes.

**Difficulty:** Intermediate
**Category:** Hardware

---

## ECDH — Elliptic-Curve Diffie-Hellman

A key agreement protocol allowing two parties to establish a shared secret over an insecure channel using elliptic-curve cryptography. ECDH provides the same security as classical DH with much smaller keys (256-bit ECDH ≈ 3072-bit RSA). The ephemeral variant (ECDHE) generates a new key pair per session, providing forward secrecy: past sessions remain secure if the long-term key is later compromised.

**Difficulty:** Advanced
**Category:** Security

---

## ECN — Explicit Congestion Notification

An IP/TCP extension (RFC 3168) allowing routers to signal congestion to endpoints without dropping packets. ECN-capable routers set the CE (Congestion Experienced) bits in the IP header; the receiver reflects the notification to the sender via TCP ECE/CWR flags; the sender reduces its transmission rate. ECN reduces latency and retransmissions in congested networks compared to packet-drop-based congestion signals.

**Difficulty:** Advanced
**Category:** Networking

---

## EDR — Endpoint Detection and Response

A security product category providing continuous monitoring of endpoint activity, behavioral detection of threats, and automated or manual response capabilities on workstations and servers. EDR tools record process creation, network connections, file writes, and registry changes; correlate behaviors into alerts; and allow analysts to isolate hosts, kill processes, or collect forensic evidence. Examples: CrowdStrike Falcon, SentinelOne, Microsoft Defender for Endpoint.

**Difficulty:** Intermediate
**Category:** Security

---

## EDNS — Extension Mechanisms for DNS

A DNS specification (RFC 6891, originally RFC 2671) extending the original DNS message format by introducing OPT pseudo-records. EDNS0 (version 0) allows larger UDP DNS messages (up to 4096 bytes, enabling DNSSEC responses), signals DNSSEC support (DO bit), and provides a framework for future DNS extensions (EDNS Client Subnet, DNS Cookies, Padding). Required for DNSSEC operation.

**Difficulty:** Advanced
**Category:** Networking

---

## EFI — Extensible Firmware Interface

The firmware interface specification developed by Intel in the 1990s (originally for Itanium), standardized as the basis for UEFI. EFI introduced a 32/64-bit pre-OS execution environment, GPT disk support, and driver model. The EFI System Partition (ESP) is a FAT32 partition storing bootloaders and firmware applications. "EFI" and "UEFI" are often used interchangeably in practice.

**Difficulty:** Intermediate
**Category:** Hardware

---

## EGP — Exterior Gateway Protocol

An early inter-autonomous-system routing protocol (RFC 904, 1984) that allowed ASes to exchange reachability information. EGP was simple and limited: it only conveyed reachability (not topology) and did not support policy routing. BGP (1989) replaced EGP, which was officially declared historic in RFC 1772. The term "EGP" is sometimes used generically to mean any inter-AS routing protocol.

**Difficulty:** Advanced
**Category:** Networking

---

## EIDE — Enhanced IDE

An extension of the original ATA/IDE interface increasing maximum transfer rates, adding support for drives larger than 504 MB (LBA addressing), and allowing connection of up to four devices (two channels, two devices per channel). EIDE also added ATAPI, enabling optical drives and tape devices to use the same interface. Superseded by ATA-66/100/133 and eventually by SATA.

**Difficulty:** Base
**Category:** Hardware

---

## EIRP — Effective Isotropic Radiated Power

The total power radiated by a transmitting antenna in the direction of maximum gain, expressed in dBm or watts. EIRP = transmitter output power + antenna gain - cable losses. Regulatory bodies (FCC, ETSI) limit EIRP for Wi-Fi, cellular, and other radio systems to prevent interference. Wi-Fi APs and routers must comply with regional EIRP limits; exceeding them is illegal.

**Difficulty:** Advanced
**Category:** Networking

---

## ELF — Executable and Linkable Format

The standard binary format for executables, shared libraries, and object files on Linux and most Unix-like systems. An ELF file contains a header (architecture, entry point), program headers (segments for the loader), and section headers (for the linker). ELF supports dynamic linking (shared library loading at runtime), debug information (DWARF), and position-independent code (PIC/PIE) for ASLR.

**Difficulty:** Advanced
**Category:** OS

---

## ELK — Elasticsearch, Logstash, Kibana

A popular open-source log management and analytics stack. Logstash ingests and parses logs from diverse sources; Elasticsearch stores and indexes them; Kibana visualizes and queries the data. Often extended to the "Elastic Stack" with Beats (lightweight shippers) and APM agents. Widely used for centralized logging, security analytics (SIEM), and observability in cloud-native environments.

**Difficulty:** Intermediate
**Category:** Dev

---

## EMM — Enterprise Mobility Management

A set of technologies for managing employee mobile devices, applications, and data within an organization. EMM encompasses MDM (device-level control), MAM (application management), and MCM (content management). Modern EMM platforms (Intune, Jamf, MobileIron) enforce encryption, remote wipe, app distribution, and compliance policies on both corporate-owned and BYOD devices.

**Difficulty:** Intermediate
**Category:** Security

---

## ENI — Elastic Network Interface

A virtual network interface in AWS that can be attached to, detached from, and moved between EC2 instances within the same Availability Zone, retaining its MAC address, IP addresses, and security groups. ENIs enable use cases like management networks (separate interface for SSH), dual-homed instances, and network appliance HA (floating secondary ENI for failover).

**Difficulty:** Intermediate
**Category:** Cloud

---

## EOF — End of File

A condition returned by read() and related functions indicating no more data is available from a file or stream. In Unix, EOF is not a character stored in the file — it is a kernel signal when the read position reaches the end. On interactive terminals, Ctrl+D generates EOF. In binary protocols, explicit length fields or framing delimiters are preferable to EOF-based framing to handle concatenated messages correctly.

**Difficulty:** Base
**Category:** OS

---

## EOL — End of Life

The point at which a vendor ceases to provide security patches, bug fixes, and support for a product (OS, library, hardware). Running EOL software exposes systems to unpatched vulnerabilities indefinitely. EOL dates are published in advance; migration planning should begin well before them. In networking, EOL also marks when hardware will no longer receive security advisories, typically followed by End of Sale (EoS).

**Difficulty:** Base
**Category:** Dev

---

## EPP — Endpoint Protection Platform

A security product category providing preventive security on endpoints: antivirus, anti-malware, application control, host firewall, and sometimes DLP. EPP focuses on blocking known threats before execution, using signature-based and ML-based detection. Modern security frameworks use EPP and EDR together: EPP prevents commodity threats; EDR handles sophisticated, novel attacks requiring behavioral analysis.

**Difficulty:** Intermediate
**Category:** Security

---

## EPT — Extended Page Tables

Intel VT-x hardware feature (also called Nested Paging on AMD with NPT) adding a second level of address translation for virtualization. The guest OS manages guest virtual → guest physical translation; the hypervisor maintains guest physical → host physical translation via EPT. EPT eliminates the need for the hypervisor to emulate TLB flushing, dramatically improving VM memory performance.

**Difficulty:** Advanced
**Category:** OS

---

## ERD — Entity-Relationship Diagram

A visual data modeling tool showing entities (tables), attributes, and relationships (one-to-one, one-to-many, many-to-many) in a database. ERDs use standard notation (Crow's Foot or Chen notation) and are used in the database design phase to communicate structure before implementation. ORMs can auto-generate ERDs from live databases using tools like DBeaver, dbdiagram.io, or pgAdmin.

**Difficulty:** Base
**Category:** Database

---

## ESXI — VMware ESXi Hypervisor

VMware's Type-1 (bare-metal) hypervisor, the core component of vSphere. ESXi runs directly on hardware with a minimal footprint (no general-purpose OS), providing CPU, memory, storage, and network virtualization for guest VMs. ESXi is managed via vCenter for multi-host deployments or directly via the Host Client. Licensing concerns have driven significant migration to KVM/Proxmox since the Broadcom acquisition of VMware.

**Difficulty:** Intermediate
**Category:** Cloud

---

## ESB — Enterprise Service Bus

A middleware integration pattern providing a centralized communication layer between heterogeneous enterprise applications. The ESB handles message routing, transformation, protocol mediation, and orchestration. Popular in SOA architectures of the 2000s with products like MuleSoft, IBM Integration Bus, and WSO2. Largely superseded by event-streaming platforms (Kafka) and lightweight API gateways in microservice architectures.

**Difficulty:** Advanced
**Category:** Dev

---

## ESN — Electronic Serial Number

A unique identifier burned into mobile device hardware (originally 32-bit in CDMA phones, later expanded to MEID — 56-bit). The ESN/MEID identifies the device to the carrier network, enabling blocking of stolen devices. In broader usage, ESN refers to any hardware serial number used for device identification in inventory management, warranty tracking, and telecom provisioning.

**Difficulty:** Base
**Category:** Hardware

---

## ESS — Extended Service Set

A wireless network topology consisting of multiple BSS (Basic Service Sets / access points) connected by a wired distribution system, all sharing the same SSID. Clients can roam between APs within an ESS seamlessly (with re-association, not full re-authentication in 802.11r fast BSS transition). The ESS appears as a single logical network to clients regardless of which AP they are associated with.

**Difficulty:** Intermediate
**Category:** Networking

---

## ETCD — Distributed Key-Value Store

A strongly consistent, distributed key-value store (using the Raft consensus algorithm) designed for storing small amounts of critical configuration data that must be highly available and consistent. etcd is the backbone of Kubernetes: all cluster state (pod definitions, service configurations, secrets, RBAC rules) is stored in etcd. Data is stored in a hierarchical key namespace; clients watch keys for changes.

**Difficulty:** Intermediate
**Category:** Cloud

---

## ETL — Extract, Transform, Load

A data integration process pulling data from source systems (Extract), cleaning and restructuring it (Transform), and writing it to a target (Load — typically a data warehouse or data lake). ETL pipelines are the backbone of BI and analytics. Modern ELT (load first, transform after) uses cloud data warehouse compute (Snowflake, BigQuery, Redshift) to avoid pre-load transformation bottlenecks.

**Difficulty:** Intermediate
**Category:** Database

---

## ETW — Event Tracing for Windows

A high-performance, kernel-level tracing framework built into Windows providing structured event logging for diagnostic and security purposes. ETW uses providers (registered in the registry), controllers (start/stop sessions), and consumers (read events). The entire Windows kernel, drivers, and user-mode components instrument themselves with ETW events. EDR products and Sysmon use ETW to monitor process creation, network connections, and file operations.

**Difficulty:** Advanced
**Category:** OS

---

## EULA — End User License Agreement

A legal contract between a software vendor and the end user specifying the terms of software use: what is permitted (number of installs, use cases), what is prohibited (reverse engineering, redistribution), warranty disclaimers, and liability limitations. EULAs are typically click-through agreements. Their enforceability varies by jurisdiction; courts have challenged some terms as unconscionable.

**Difficulty:** Base
**Category:** Dev

---

## EULA — End User License Agreement

A legal contract between software vendor and user specifying use terms. EULAs restrict activities like reverse engineering, redistribution, and simultaneous installations. They disclaim warranties and limit liability. Enforceability varies by jurisdiction; shrink-wrap and click-through EULAs have been challenged in courts as contracts of adhesion where users have no meaningful negotiating power.

**Difficulty:** Base
**Category:** Dev

---

## EVPN — Ethernet VPN

An IETF standard (RFC 7432) for providing Layer 2 and Layer 3 VPN services over an MPLS or VXLAN fabric using BGP as the control plane. EVPN replaces older L2VPN technologies (VPLS, LDP-signaled pseudowires) with a scalable, BGP-based approach supporting multi-homing, ARP/ND suppression, and integrated IP routing. EVPN/VXLAN is the dominant architecture for modern data center fabrics.

**Difficulty:** Advanced
**Category:** Networking

---

## EVM — Ethereum Virtual Machine

The runtime environment for smart contracts on the Ethereum blockchain. The EVM is a quasi-Turing-complete, stack-based virtual machine executing EVM bytecode compiled from Solidity or Vyper. Each operation consumes "gas" (preventing infinite loops); the gas limit per block constrains computation. The EVM is sandboxed and deterministic across all nodes, enabling trustless distributed computation.

**Difficulty:** Advanced
**Category:** Dev

---

## EXIF — Exchangeable Image File Format

A standard for embedding metadata in image (JPEG, TIFF, HEIC) and audio files. EXIF metadata includes camera model, lens, exposure settings, timestamp, and critically, GPS coordinates if the device has location services enabled. EXIF data in photos shared online is a significant privacy risk: the GPS coordinates embedded in a photo can reveal home/work locations. Tools like ExifTool read, write, and strip EXIF data.

**Difficulty:** Intermediate
**Category:** Dev

---

## EXT4 — Fourth Extended Filesystem

The default filesystem for most Linux distributions, introduced in 2008 as the successor to ext3. EXT4 supports volumes up to 1 exabyte, files up to 16 TB, extents (contiguous block ranges reducing fragmentation), delayed allocation, journal checksums, and online defragmentation. EXT4 maintains backward compatibility with ext2/ext3. For new deployments, ZFS, Btrfs, and XFS offer more advanced features.

**Difficulty:** Intermediate
**Category:** OS
