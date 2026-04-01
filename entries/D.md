## DAC — Digital-to-Analog Converter

A hardware component converting discrete digital values (binary numbers) into continuous analog signals (voltages, currents). DACs are found in audio output stages, motor controllers, RF transmitters, and display drivers. Resolution (bit depth) determines the number of discrete output levels; sample rate determines maximum output frequency. The inverse of an ADC.

**Difficulty:** Intermediate
**Category:** Hardware

---

## DAG — Directed Acyclic Graph

A graph data structure with directed edges and no cycles. DAGs model dependencies: tasks, build systems, data pipelines, version control history (git commits form a DAG). Topological sort is the key algorithm on DAGs, yielding a linear order respecting all dependencies. Used in Apache Airflow, Spark execution plans, and blockchain DAG architectures (IOTA, Nano).

**Difficulty:** Intermediate
**Category:** Dev

---

## DASH — Dynamic Adaptive Streaming over HTTP

An adaptive bitrate streaming standard (ISO/IEC 23009) that segments video/audio into small chunks and delivers them over HTTP. The client downloads a manifest (MPD file), selects the appropriate quality tier based on available bandwidth, and fetches segments. DASH allows seamless mid-stream quality switching without interruption. The open-standard equivalent of Apple's HLS.

**Difficulty:** Intermediate
**Category:** Protocol

---

## DAST — Dynamic Application Security Testing

Security testing methodology that analyzes a running application from the outside, sending crafted inputs and observing responses to find vulnerabilities (XSS, SQL injection, SSRF) without access to source code. DAST tools (OWASP ZAP, Burp Suite, Nessus) act like an external attacker. Contrast with SAST (static analysis of source code) — both are needed for comprehensive coverage.

**Difficulty:** Intermediate
**Category:** Security

---

## DBMS — Database Management System

Software providing systematic management of databases: storage engine, query processor, transaction manager, concurrency control, recovery, and access control. A DBMS abstracts physical data storage behind a logical data model (relational, document, graph, key-value). Examples: PostgreSQL, MySQL, MongoDB, Redis, Cassandra. The DBMS is distinct from the database (the actual data).

**Difficulty:** Base
**Category:** Database

---

## DCE — Distributed Computing Environment

An open software framework developed by the Open Software Foundation in the 1990s providing a comprehensive set of distributed computing services: RPC, directory service (CDS), time synchronization (DTS), and threads (DCE Threads). DCE/RPC is the basis for Microsoft's MSRPC, which underlies DCOM and many Windows services including Active Directory replication.

**Difficulty:** Advanced
**Category:** Protocol

---

## DCIM — Data Center Infrastructure Management

Software and methodology for managing data center physical infrastructure: power, cooling, floor space, and IT assets. DCIM platforms collect real-time data from PDUs, CRACs, UPS systems, and server sensors, enabling capacity planning, PUE optimization, and change management. Bridging the gap between facilities management and IT operations.

**Difficulty:** Intermediate
**Category:** Cloud

---

## DDNS — Dynamic DNS

A service that automatically updates DNS records when a device's IP address changes, typically used for hosts with dynamically assigned IPs (home connections, laptops). The client runs a DDNS agent that detects IP changes and sends authenticated update requests to the DNS provider (RFC 2136). Used to maintain reachable hostnames for home servers, cameras, and VPN endpoints without a static IP.

**Difficulty:** Intermediate
**Category:** Networking

---

## DDL — Data Definition Language

The SQL subset for defining and modifying database schema: CREATE, ALTER, DROP, TRUNCATE, RENAME. DDL statements modify the data catalog and are auto-committed in most RDBMS (cannot be rolled back). Contrast with DML (INSERT, UPDATE, DELETE — data manipulation) and DCL (GRANT, REVOKE — data control). Schema migrations (Flyway, Liquibase, Alembic) manage DDL changes across environments.

**Difficulty:** Base
**Category:** Database

---

## DFS — Distributed File System

A file system allowing files to be accessed from multiple computers over a network as if they were local. DFS abstracts physical location: clients use namespace paths that transparently map to servers. Microsoft DFS-N (Namespace) + DFS-R (Replication) provide HA file shares in Windows environments. HDFS, GlusterFS, and CephFS are Linux-native alternatives.

**Difficulty:** Intermediate
**Category:** OS

---

## DHCP — Dynamic Host Configuration Protocol

A network management protocol (UDP ports 67/68) automatically assigning IP addresses, subnet masks, default gateways, DNS servers, and other parameters via DORA (Discover, Offer, Request, Acknowledge). Leases are time-limited; clients renew before expiry. DHCP snooping on switches prevents rogue DHCP servers. DHCPv6 and SLAAC serve a similar role in IPv6 networks.

**Difficulty:** Base
**Category:** Networking

---

## DHT — Distributed Hash Table

A decentralized data structure providing a key-value lookup distributed across many nodes with no central coordinator. Each node is responsible for a portion of the key space; lookups require O(log n) hops. Used in peer-to-peer systems: BitTorrent (Mainline DHT), IPFS (Kademlia), and distributed databases. DHTs provide resilience to node churn but face consistency and Sybil attack challenges.

**Difficulty:** Advanced
**Category:** Networking

---

## DKIM — DomainKeys Identified Mail

An email authentication method where a domain owner signs outgoing messages with a private key; the signature appears in a DKIM-Signature header. Recipients retrieve the public key from a DNS TXT record and verify the signature, confirming the message has not been altered and was authorized by the signing domain. Required for effective DMARC enforcement and email deliverability.

**Difficulty:** Intermediate
**Category:** Security

---

## DKMS — Dynamic Kernel Module Support

A framework enabling Linux kernel modules (device drivers, filesystems) to be automatically recompiled when the kernel is updated, maintaining driver availability across kernel upgrades. DKMS modules are stored in /usr/src and rebuilt by the package manager post-install. Used by NVIDIA drivers, VirtualBox kernel modules, and ZFS on Linux to survive kernel version changes.

**Difficulty:** Intermediate
**Category:** OS

---

## DLL — Dynamic Link Library

A Windows executable containing shared code and data that multiple programs can use simultaneously, loaded at runtime rather than compiled into each executable. DLLs reduce disk footprint and enable hot-patching (replace the DLL without recompiling dependents). DLL hijacking (placing a malicious DLL earlier in the search path) is a persistent privilege escalation and persistence technique.

**Difficulty:** Intermediate
**Category:** OS

---

## DMA — Direct Memory Access

A hardware mechanism allowing peripherals (NIC, GPU, storage controller) to read/write main memory directly without CPU involvement per transfer. The CPU programs the DMA controller with source, destination, and length, then the DMA handles the transfer, issuing an interrupt on completion. IOMMU/VT-d restricts DMA to authorized memory regions, preventing DMA attacks from malicious PCIe devices.

**Difficulty:** Intermediate
**Category:** Hardware

---

## DMZ — Demilitarized Zone

A network segment placed between an external (untrusted) network and an internal (trusted) network, hosting publicly accessible services (web servers, mail relays, DNS) that must be reachable from the internet. Traffic to the DMZ is filtered by an outer firewall; traffic from the DMZ to the internal network is restricted by an inner firewall. Compromising a DMZ host does not directly expose the internal network.

**Difficulty:** Intermediate
**Category:** Security

---

## DNS — Domain Name System

A hierarchical, distributed database mapping hostnames to IP addresses (A, AAAA records) and storing mail routing (MX), text (TXT), aliases (CNAME), name servers (NS), and service discovery (SRV) records. Queries traverse resolver → root server → TLD server → authoritative server. DNS operates over UDP/TCP port 53. DNSSEC adds cryptographic authentication to prevent spoofing.

**Difficulty:** Base
**Category:** Networking

---

## DOH — DNS over HTTPS

A protocol (RFC 8484) sending DNS queries and responses encapsulated in HTTPS, preventing ISP eavesdropping and manipulation of DNS traffic. DoH clients send queries to a resolver's HTTPS endpoint; responses are indistinguishable from regular web traffic. DoH improves privacy for users but complicates corporate network monitoring and parental controls, generating ongoing policy debates.

**Difficulty:** Intermediate
**Category:** Security

---

## DOM — Document Object Model

A programming interface representing an HTML or XML document as a tree of objects (nodes) that scripts can query and manipulate. The browser constructs the DOM from parsed HTML; JavaScript modifies the DOM to update the page dynamically without a full reload. DOM manipulation is the foundation of interactive web applications; performance is critical since excessive reflows and repaints degrade rendering speed.

**Difficulty:** Intermediate
**Category:** Dev

---

## DOS — Denial of Service

An attack making a system, service, or network resource unavailable by overwhelming it with requests or exploiting a vulnerability that causes it to crash or consume excessive resources. Unlike DDoS (distributed), a DoS originates from a single source. Application-layer DoS (HTTP floods, slow HTTP, regex DoS) targets specific resource constraints rather than raw bandwidth.

**Difficulty:** Base
**Category:** Security

---

## DOT — DNS over TLS

A protocol (RFC 7858) encrypting DNS queries with TLS over TCP port 853, preventing eavesdropping and tampering. Unlike DoH, DoT uses a dedicated port, making it easily identifiable and blockable by network administrators — an advantage for enterprise policy enforcement and a disadvantage for censorship circumvention. Clients can verify the resolver's certificate for authenticity.

**Difficulty:** Intermediate
**Category:** Security

---

## DPI — Deep Packet Inspection

A network processing technique that examines packet content beyond headers, analyzing application-layer data to classify traffic, enforce policy, detect malware, and prioritize QoS. DPI devices inspect the payload of packets, including encrypted streams (using SSL inspection / MITM). Used in firewalls (NGFW), IDS/IPS, traffic shaping, and in authoritarian content filtering systems.

**Difficulty:** Intermediate
**Category:** Networking

---

## DPDK — Data Plane Development Kit

An open-source framework enabling user-space packet processing at line rate by bypassing the Linux kernel network stack. DPDK uses poll-mode drivers (PMDs), huge pages, CPU pinning, and zero-copy I/O to achieve multi-million packets-per-second throughput on commodity hardware. Used in virtual routers, NFV appliances, and high-frequency trading networks.

**Difficulty:** Advanced
**Category:** Networking

---

## DRAM — Dynamic Random-Access Memory

The most common type of main memory. DRAM stores each bit in a capacitor that leaks charge, requiring refresh thousands of times per second (hence "dynamic"). Denser and cheaper than SRAM but slower due to refresh cycles and higher latency. Modern variants: DDR4 (2014), DDR5 (2020), LPDDR5 (mobile). ECC DRAM adds error correction bits for server reliability.

**Difficulty:** Intermediate
**Category:** Hardware

---

## DRI — Directly Responsible Individual

An accountability framework, popularized by Apple, designating a single named person responsible for the success or failure of a project, decision, or deliverable. Unlike committee ownership, DRI prevents diffusion of responsibility. In software projects, the DRI is the person who must make the final call, not just one of many stakeholders. Analogous to the "single throat to choke" ownership model.

**Difficulty:** Base
**Category:** Dev

---

## DRM — Digital Rights Management

Technical access controls protecting copyrighted digital content (video, audio, software, ebooks) from unauthorized copying, redistribution, or modification. DRM systems encrypt content and require a license key linked to the device or account for playback. Examples: Apple FairPlay, Widevine (Google), PlayReady (Microsoft). DRM restricts fair-use rights and is routinely circumvented, making its effectiveness debated.

**Difficulty:** Intermediate
**Category:** Security

---

## DRP — Disaster Recovery Plan

A documented procedure for restoring IT systems and data after a catastrophic event (hardware failure, natural disaster, cyberattack, human error). A DRP defines RTOs (Recovery Time Objectives) and RPOs (Recovery Point Objectives), identifies critical systems, documents restoration procedures, and specifies responsible parties. DRPs must be tested regularly through tabletop exercises and actual failover drills.

**Difficulty:** Intermediate
**Category:** Cloud

---

## DSA — Digital Signature Algorithm

A FIPS 186 standard for digital signatures using discrete logarithm mathematics, standardized by NIST in 1994. DSA generates a signature pair (r, s) from a hash of the message and a random per-signature nonce (k). Reuse of k leaks the private key (the PlayStation 3 root key was recovered this way). ECDSA (elliptic curve variant) provides the same security with much smaller keys.

**Difficulty:** Advanced
**Category:** Security

---

## DSCP — Differentiated Services Code Point

A 6-bit field in the IP header's DS byte used to classify and prioritize network traffic for QoS. Packets are marked with DSCP values (EF for voice, AF for video, BE for best-effort) at the network edge; core routers queue and schedule packets based on these markings without per-flow state. DSCP replaced the older IP Precedence field (3 bits) with a more expressive 64-value space.

**Difficulty:** Advanced
**Category:** Networking

---

## DSL — Domain-Specific Language

A programming or specification language designed for a specific problem domain rather than general-purpose programming. DSLs trade generality for expressiveness within their domain: SQL (data querying), CSS (styling), Makefile syntax (build automation), HCL (infrastructure as Terraform code), regular expressions (pattern matching). DSLs can be internal (embedded in a host language) or external (with their own parser).

**Difficulty:** Intermediate
**Category:** Dev

---

## DTD — Document Type Definition

A set of markup declarations defining the structure and legal elements and attributes of an XML or HTML document. A DTD specifies which elements are allowed, in what order, and what attributes they may carry. DTDs use a non-XML syntax; XML Schema (XSD) and RELAX NG are more expressive successors. HTML 4.01 and XHTML were defined by SGML DTDs; HTML5 dropped DTD entirely.

**Difficulty:** Intermediate
**Category:** Dev

---

## DTO — Data Transfer Object

A design pattern (not a protocol) using a simple, flat object to carry data between subsystems or across network boundaries. DTOs have no business logic — only fields and accessors. They decouple the internal domain model from the external API contract, enabling independent versioning. Common in Java enterprise apps (Spring, Jakarta EE) and in REST API response/request bodies.

**Difficulty:** Intermediate
**Category:** Dev

---

## DUID — DHCP Unique Identifier

A persistent, vendor-assigned identifier used by DHCPv6 clients to identify themselves to a server, replacing the MAC-address-based approach used in DHCPv4. DUIDs have four types (DUID-LLT, DUID-EN, DUID-LL, DUID-UUID) and are stored persistently by clients so they survive reboots and network interface changes. The DUID, combined with an IAID, forms the basis for DHCPv6 prefix delegation.

**Difficulty:** Advanced
**Category:** Networking

---

## DVCS — Distributed Version Control System

A version control architecture where every clone of the repository contains the complete history, enabling offline work and peer-to-peer collaboration without a central server. DVCS operations (commit, branch, merge, log) are local and fast. Git and Mercurial are the dominant DVCS tools. Contrast with centralized VCS (SVN, CVS) where operations require server connectivity.

**Difficulty:** Intermediate
**Category:** Dev

---

## DUT — Device Under Test

A term used in hardware testing and quality assurance to refer to the specific device or component being tested in a test setup. The DUT is connected to test instruments (oscilloscopes, logic analyzers, power supplies) and a test harness. In software testing, the analogous term is SUT (System Under Test). Common in embedded development, RF testing, PCB validation, and protocol compliance testing.

**Difficulty:** Base
**Category:** Hardware

---

## DLNA — Digital Living Network Alliance
Industry standard for sharing media (audio, video, images) between consumer electronics devices over a home network using UPnP and HTTP. DLNA-certified devices (TVs, NAS, game consoles) discover each other via SSDP and stream content via HTTP with DLNA-specific MIME type profiles.
**Difficulty:** Base
**Category:** Networking

---

## DNAT — Destination NAT
NAT variant that rewrites the destination IP address (and optionally port) of incoming packets. Used to forward external traffic to an internal server (port forwarding). Implemented in iptables via the DNAT target in the PREROUTING chain, or in nftables with dnat to. The inverse of SNAT.
**Difficulty:** Intermediate
**Category:** Networking


---

## DACL — Discretionary Access Control List

Component of a Windows security descriptor specifying which users and groups are allowed or denied access to a securable object (file, registry key, service, process). Controlled by the object owner. Distinguished from SACL (System ACL, used for auditing). Managed via icacls, Get-Acl/Set-Acl, or the Security tab in Windows Explorer.

**Difficulty:** Intermediate
**Category:** Security

---

## DMARC — Domain-based Message Auth Reporting

Email authentication policy framework (RFC 7489) built on SPF and DKIM. Instructs receiving servers what to do with messages failing authentication: none (monitor only), quarantine (spam folder), or reject. Generates aggregate (rua) and forensic (ruf) XML reports. Essential for preventing domain spoofing and business email compromise (BEC) attacks.

**Difficulty:** Intermediate
**Category:** Security

---

## DNSBL — DNS Block List

Blacklist published via DNS used by mail servers and security appliances to check if a sending IP or domain is a known source of spam, malware, or phishing. Queried via reversed IP lookup (e.g. 4.3.2.1.zen.spamhaus.org). A positive response indicates the IP is listed. Major DNSBLs: Spamhaus ZEN, Barracuda, SORBS, URIBL.

**Difficulty:** Intermediate
**Category:** Security

---

## DNSSEC — DNS Security Extensions

IETF standards (RFC 4033-4035) adding cryptographic signatures to DNS records. Signs RRsets with RRSIG records; DNSKEY records publish zone signing keys; DS records chain trust from parent to child zones. Prevents cache poisoning (Kaminsky attack) by allowing resolvers to verify record authenticity. Does not encrypt DNS queries.

**Difficulty:** Advanced
**Category:** Security

---

## DRBD — Distributed Replicated Block Device

Open-source Linux kernel module synchronously mirroring block devices between two servers over TCP/IP or RDMA. Creates a software RAID-1 equivalent across nodes without shared SAN hardware. Used in Pacemaker-based HA clusters for automatic failover of databases and file systems. Supports Primary/Primary mode for active-active configurations with cluster-aware applications.

**Difficulty:** Advanced
**Category:** Hardware

---

## DPAPI — Data Protection API

Windows cryptographic API encrypting data tied to a user or machine identity without explicit key management. Applications call CryptProtectData/CryptUnprotectData; Windows derives the encryption key from the user's password hash or machine secret. Used by Chrome (saved passwords), Credential Manager, and BitLocker recovery key protection.

**Difficulty:** Advanced
**Category:** Security

---

## DSYNC — Directory Sync Process

Synchronization of identity data (users, groups, attributes) between a source directory (AD, LDAP) and a target (cloud IdP, SaaS application). Implemented by Azure AD Connect, Okta AD Agent, and Google Cloud Directory Sync. Supports full sync and delta sync modes. Attribute mapping rules control which fields are replicated and transformed.

**Difficulty:** Intermediate
**Category:** Security

---

## DEVOP — DevOps Practice

Cultural and technical movement combining software development (Dev) and IT operations (Ops) to shorten delivery cycles and improve reliability. Key practices: CI/CD pipelines, infrastructure as code, monitoring as code, and blameless postmortems. Measured via DORA metrics: deployment frequency, lead time for changes, MTTR, and change failure rate.

**Difficulty:** Intermediate
**Category:** Dev

---

## DRATS — Disaster Recovery as a Service

Cloud-delivered disaster recovery model where a provider replicates workloads to their infrastructure and manages failover automation. Provides contractual RTO/RPO guarantees without a dedicated DR data center. Implemented via Zerto, VMware Cloud DR, and AWS Elastic Disaster Recovery. Billed on a subscription model based on protected VM count.

**Difficulty:** Intermediate
**Category:** Cloud


---

## DTLS — Datagram Transport Layer Security

Adaptation of TLS for datagram protocols (UDP, DCCP) defined in RFC 6347. Adds sequence numbers and retransmission logic to handle packet loss and reordering without a reliable transport layer. Used in WebRTC (DTLS-SRTP for media), QUIC predecessors, VPN protocols, and IoT deployments requiring encrypted UDP.

**Difficulty:** Advanced
**Category:** Protocol

---

## DEVFS — Device Filesystem

Virtual filesystem exposing kernel device objects as files under /dev, populated dynamically as hardware is detected. In Linux, replaced by udev (userspace device manager) which creates device nodes based on kernel uevents and rules in /etc/udev/rules.d/. Provides a consistent interface between hardware drivers and userspace applications.

**Difficulty:** Intermediate
**Category:** OS

---

## DLRM — Deep Learning Recommendation Model

Neural network architecture published by Meta for large-scale recommendation systems. Combines embedding tables for categorical features (user IDs, item IDs) with MLPs for dense features, then applies dot-product interactions. Characterized by massive embedding memory requirements (hundreds of GB) and mixed CPU/GPU execution patterns.

**Difficulty:** Advanced
**Category:** AI

---

## DSHOT — Digital Shot

Digital protocol for communication between flight controllers and ESCs (Electronic Speed Controllers) in drones and RC aircraft. Encodes throttle values as digital packets rather than analog PWM signals, eliminating calibration requirements. DSHOT150/300/600/1200 variants indicate bitrate in kbps. Supports bidirectional telemetry (RPM feedback) in extended variants.

**Difficulty:** Advanced
**Category:** Protocol
