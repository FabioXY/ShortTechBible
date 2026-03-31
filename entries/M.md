
## MAAS — Metal as a Service

Canonical's open-source platform for provisioning bare-metal servers as cloud
instances. Automates server discovery via BMC/IPMI, PXE booting, OS deployment,
and lifecycle management. Enables cloud-like provisioning automation on physical
hardware without requiring a hypervisor layer.

**Difficulty:** Intermediate
**Category:** Cloud

---

## MAPI — Messaging Application Programming Interface

Microsoft's proprietary protocol and API for Outlook and Exchange Server email,
calendar, and contact synchronization. Extended MAPI provides rich client access
to Exchange mailboxes. Modern deployments add EWS and the Microsoft Graph API
as alternative access layers for web and mobile clients.

**Difficulty:** Intermediate
**Category:** Protocol

---

## MBPS — Megabits Per Second

Unit of data transfer rate equal to one million bits per second. Standard measure
for network link speeds (100 Mbps Fast Ethernet, 1000 Mbps Gigabit Ethernet).
Distinct from MBps (Megabytes per second) which is 8× larger. The lowercase b
vs uppercase B distinction is a frequent source of bandwidth confusion.

**Difficulty:** Base
**Category:** Networking

---

## MDNS — Multicast DNS

Protocol (RFC 6762) for DNS-like hostname resolution on local segments without
a dedicated DNS server. Devices broadcast queries and responses to 224.0.0.251
on port 5353. Used by Apple Bonjour, Avahi on Linux, and mDNS-SD for
zero-configuration service discovery on LANs and home networks.

**Difficulty:** Intermediate
**Category:** Protocol

---

## MEMS — Microelectromechanical Systems

Technology integrating mechanical and electrical components at the microscale
on silicon. Used to manufacture accelerometers, gyroscopes, pressure sensors,
and digital micromirror devices. Accelerometers in laptops (including MacBooks)
that protect the hard drive during free-fall detection are MEMS devices.

**Difficulty:** Advanced
**Category:** Hardware

---

## MFA — Multi-Factor Authentication

Authentication requiring verification from two or more independent categories:
something you know (password), something you have (TOTP token, hardware key),
or something you are (biometric). Significantly raises the cost of credential
attacks even when passwords are fully compromised via breach or phishing.

**Difficulty:** Base
**Category:** Security

---

## MGMT — Management Interface

Dedicated out-of-band network interface on servers, switches, and appliances
separate from data plane interfaces. Allows administrative access (SSH, HTTPS,
SNMP) even when the primary data network is down, the device is being provisioned,
or the OS is unresponsive.

**Difficulty:** Base
**Category:** Networking

---

## MIME — Multipurpose Internet Mail Extensions

Standard (RFC 2045–2049) extending email format to support non-ASCII character
sets, attachments, and multiple content types in a single message. Defines
Content-Type headers (text/html, image/jpeg, application/pdf) adopted by HTTP
as its own content-type negotiation mechanism.

**Difficulty:** Base
**Category:** Protocol

---

## MIPS — Million Instructions Per Second

Legacy CPU performance metric counting machine instructions executed per second.
Misleading as a cross-architecture benchmark because instruction complexity varies
enormously between ISAs. Also the name of a RISC processor architecture (MIPS
Architecture) used widely in embedded systems, routers, and network equipment.

**Difficulty:** Intermediate
**Category:** Hardware

---

## MITM — Man in the Middle

Attack where an adversary secretly intercepts and potentially alters communications
between two parties believing they communicate directly. Examples: ARP spoofing,
rogue Wi-Fi APs, SSL stripping. Mitigated by TLS with verified certificates,
HSTS preloading, and mutual TLS authentication.

**Difficulty:** Intermediate
**Category:** Security

---

## MLAG — Multi-Chassis Link Aggregation

Network technology allowing link aggregation across two physically separate
switches, presenting them as a single logical switch to connected devices.
Eliminates Spanning Tree Protocol-blocked ports while maintaining full redundancy.
Vendor implementations: Cisco vPC, Arista MLAG, Cumulus CLAG.

**Difficulty:** Advanced
**Category:** Networking

---

## MMIO — Memory-Mapped I/O

Technique mapping device registers into the same address space as RAM, allowing
the CPU to access them with standard load/store instructions rather than special
I/O ports. PCI/PCIe devices expose their registers via BAR (Base Address Register)
regions that the OS maps into kernel virtual address space.

**Difficulty:** Advanced
**Category:** Hardware

---

## MOCA — Multimedia over Coax Alliance

Standard for networking over existing coaxial cable infrastructure. Provides
Ethernet-like connectivity with speeds up to 2.5 Gbps (MoCA 2.5), enabling
wired-quality networking between rooms already wired for cable TV without
installing new Ethernet cable throughout the building.

**Difficulty:** Intermediate
**Category:** Networking

---

## MPEG — Moving Picture Experts Group

ISO/IEC working group developing audio and video compression standards. Key
outputs: MPEG-1 (VCD, MP3), MPEG-2 (DVD, broadcast TV), MPEG-4 (H.264 video),
and MPEG-H (HEVC/H.265). The group's standards define codecs used in virtually
all digital media production, distribution, and playback today.

**Difficulty:** Intermediate
**Category:** Dev

---

## MPIO — Multipath I/O

Storage access technique using multiple physical paths between a host and storage
to provide redundancy and load balancing. Linux implements it via `dm-multipath`;
Windows via the MPIO framework. Requires HBAs, switches, and arrays that present
the same LUN across multiple target ports simultaneously.

**Difficulty:** Intermediate
**Category:** Hardware

---

## MPLS — Multiprotocol Label Switching

High-performance forwarding using short fixed-length labels rather than IP addresses
for routing decisions. Labels are swapped at each Label Switch Router (LSR),
enabling traffic engineering, VPN services (MPLS L3VPN, L2VPN), and QoS-based
path selection in service provider and enterprise core networks.

**Difficulty:** Advanced
**Category:** Networking

---

## MPTC — Multipath TCP

TCP extension (RFC 8684) allowing a single connection to use multiple network
paths simultaneously. A smartphone can aggregate Wi-Fi and LTE for one TCP
connection, improving throughput and enabling seamless path failover. Deployed
by Apple for Siri and by Linux via the `mptcpd` daemon.

**Difficulty:** Advanced
**Category:** Networking

---

## MQTT — Message Queuing Telemetry Transport

Lightweight publish/subscribe protocol for constrained devices and low-bandwidth
networks. A broker routes messages between publishers and subscribers via topic
strings. Default port 1883 (8883 for TLS). Dominant protocol in IoT, home
automation (Home Assistant), and industrial telemetry pipelines.

**Difficulty:** Intermediate
**Category:** Protocol

---

## MSIX — Microsoft App Installer Package

Modern Windows application packaging format superseding MSI and AppX. Supports
clean installation, automatic updates, and containerized execution. Distributable
via the Microsoft Store, enterprise deployment tools (Intune), or direct download,
with more reliable installation tracking and rollback than legacy MSI.

**Difficulty:** Intermediate
**Category:** OS

---

## MSRC — Microsoft Security Response Center

Microsoft's team receiving, validating, and coordinating remediation of security
vulnerability reports. Manages CVE assignments for Microsoft products, coordinates
Patch Tuesday releases, and operates the Microsoft Bug Bounty program offering
compensation for qualifying responsible vulnerability disclosures.

**Difficulty:** Intermediate
**Category:** Security

---

## MSS — Maximum Segment Size

TCP option specifying the largest payload a host accepts in a single segment,
excluding IP and TCP headers. Negotiated in the SYN/SYN-ACK during the three-way
handshake. Typically derived from interface MTU minus 40 bytes (20 IP + 20 TCP).
Misconfigured MSS causes fragmentation or black holes when PMTUD is broken.

**Difficulty:** Intermediate
**Category:** Networking

---

## MSTP — Multiple Spanning Tree Protocol

IEEE 802.1s extension mapping multiple VLANs to fewer spanning tree instances
(MSTIs). Different VLANs can use different root bridges and active paths,
achieving load balancing across redundant links while preventing Layer 2 loops.
Supersedes PVST+ in large enterprise multi-VLAN network designs.

**Difficulty:** Advanced
**Category:** Networking

---

## MTBF — Mean Time Between Failures

Statistical measure of the average operating time between two consecutive failures
of a repairable system. Used to assess hardware reliability and plan preventive
maintenance. Derived from field reliability data or manufacturer accelerated
life testing. Higher MTBF indicates higher reliability.

**Difficulty:** Intermediate
**Category:** Hardware

---

## MTTR — Mean Time to Recovery

Average time from failure detection to full service restoration. Includes
detection, diagnosis, repair or failover, and validation phases. Key SRE metric
alongside error budgets. Improved by better monitoring, automated remediation,
documented runbooks, and regular incident response drills.

**Difficulty:** Intermediate
**Category:** Dev

---

## MTU — Maximum Transmission Unit

Maximum packet size in bytes transmittable on a network segment without IP-layer
fragmentation. Standard Ethernet MTU is 1500 bytes. Jumbo frames extend this
to 9000 bytes on supported hardware. Path MTU Discovery (PMTUD) probes the
minimum MTU along an end-to-end path to optimize segment sizing.

**Difficulty:** Base
**Category:** Networking

---

## MUSL — Musl C Standard Library

Lightweight, standards-compliant C library designed for static linking and
embedded Linux. Default libc in Alpine Linux, explaining Alpine's tiny Docker
image sizes. Fully implements POSIX 2008 and C11 with simpler, more auditable
code than glibc; some glibc extensions are not available.

**Difficulty:** Advanced
**Category:** OS

---

## MVCC — Multiversion Concurrency Control

Database concurrency technique where each transaction sees a consistent snapshot
from the moment it started. Writers create new row versions rather than overwriting
in place; readers access the appropriate version without blocking writers. Used
by PostgreSQL, InnoDB, Oracle, CockroachDB, and most MVCC-based storage engines.

**Difficulty:** Advanced
**Category:** Database

---

## MVVM — Model-View-ViewModel

Architectural pattern separating UI (View), business logic (Model), and a
ViewModel that exposes data bindings and commands. The View binds declaratively
to ViewModel properties; user interactions fire ViewModel commands. Dominant
in WPF, Angular data binding, Jetpack Compose, and SwiftUI.

**Difficulty:** Intermediate
**Category:** Dev

---

## MDRA — Managed Disaster Recovery as a Service

Managed cloud service providing automated failover, data replication, and recovery
for IT infrastructure. The provider handles replication health monitoring, failover
orchestration, and periodic RTO/RPO validation testing. Reduces operational burden
of maintaining an independently staffed DR site.

**Difficulty:** Intermediate
**Category:** Cloud

---

## MSAN — Multi-Service Access Node

Telecommunications edge device aggregating multiple subscriber access technologies
(VDSL2, POTS, fiber, Ethernet) onto a single platform. Provides DSLAM functionality
alongside voice switching for efficient consolidation of last-mile access
infrastructure at the street cabinet or central office.

**Difficulty:** Advanced
**Category:** Networking

---

## MPDU — MAC Protocol Data Unit

Data unit at the IEEE 802.11 MAC sublayer containing a MAC header, payload
(MSDU or fragment), and FCS. Multiple MPDUs can be aggregated into an A-MPDU
for a single transmission, a key efficiency optimization in 802.11n/ac/ax
(Wi-Fi 4/5/6) reducing per-frame overhead significantly.

**Difficulty:** Advanced
**Category:** Networking

---

## MSDU — MAC Service Data Unit

Payload passed from the LLC layer down to the MAC layer in IEEE 802.11. Maximum
size is 2304 bytes. If larger than the fragmentation threshold, split into
multiple MPDUs. Understanding MSDU vs MPDU boundaries is essential when
analyzing Wi-Fi frame captures in protocol analyzers.

**Difficulty:** Advanced
**Category:** Networking

---

## NUMA — Non-Uniform Memory Access

Multi-processor memory architecture where each CPU has local memory with lower
latency and higher bandwidth, while accessing remote memory on another CPU's
node incurs higher latency. Optimal performance requires NUMA-aware memory
allocation. Linux manages NUMA via the `numactl` tool and NUMA balancing kernel
subsystem.

**Difficulty:** Advanced
**Category:** Hardware

---

## MSET — Multivariate State Estimation Technique

Machine learning anomaly detection method for industrial and IT systems. Learns
normal multi-dimensional behavior from historical metric data, then flags deviations
exceeding a threshold as anomalies. Used in predictive maintenance for data center
cooling, UPS health monitoring, and network baseline anomaly detection.

**Difficulty:** Advanced
**Category:** AI

---

## MACK — MAC Acknowledgment Frame

IEEE 802.11 control frame sent by a receiving station to acknowledge successful
receipt of a unicast data or management frame. Sent after a Short Interframe
Space (SIFS). Absence of an ACK triggers retransmission. ACK frames are not
sent for multicast or broadcast frames, creating reliability gaps for such traffic.

**Difficulty:** Advanced
**Category:** Networking

---

## MCAS — Managed Certificate Authority Service

Cloud service providing hosted Certificate Authority capabilities for issuing
and managing TLS certificates within an organization. Automates certificate
lifecycle, revocation via OCSP/CRL, and integration with PKI infrastructure.
Examples: AWS Private CA, Google Cloud Certificate Authority Service.

**Difficulty:** Intermediate
**Category:** Security


---

## MTLS — Mutual TLS
TLS authentication mode where both client and server present X.509 certificates to verify each other's identity, not just the server to the client. Used in service mesh (Istio, Linkerd), zero trust architectures, and API gateways to enforce machine-to-machine authentication without passwords or tokens. Also called two-way TLS or client certificate authentication.
**Difficulty:** Intermediate
**Category:** Security

---

## MPPE — Microsoft Point-to-Point Encryption
Microsoft-proprietary encryption protocol used to encrypt PPP and PPTP VPN connections. Uses RC4 stream cipher with 40-bit, 56-bit, or 128-bit keys derived from MS-CHAPv2 credentials. Deprecated due to RC4 weaknesses and MS-CHAPv2 vulnerabilities; replaced by SSTP and IKEv2 in modern Windows VPN implementations.
**Difficulty:** Intermediate
**Category:** Security

---

## MSSP — Managed Security Service Provider
Third-party company that remotely manages and monitors a customer's security infrastructure and operations. Services include 24/7 SOC, SIEM management, threat intelligence, vulnerability scanning, and incident response. Differs from MDR (Managed Detection and Response) in scope and integration depth.
**Difficulty:** Intermediate
**Category:** Security


---

## MRCP — Media Resource Control Protocol
IETF protocol (RFC 6787) for controlling speech processing resources (ASR, TTS, speaker verification) on a media server from a client application. Used in IVR platforms and unified communications systems to separate the speech processing engine from the call control logic. Operates over SIP for session setup and RTSP-like messaging for media control.
**Difficulty:** Advanced
**Category:** Protocol
