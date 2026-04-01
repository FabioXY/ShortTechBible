## ICMP — Internet Control Message Protocol

Network-layer protocol used by IP devices to send error and diagnostic messages.
Operates alongside IP without a port number. Commands like `ping` and `traceroute`
rely on ICMP Echo Request/Reply and Time Exceeded messages. Not used for data
transfer but essential for network troubleshooting.

**Difficulty:** Base
**Category:** Networking

---

## ICAP — Internet Content Adaptation Protocol

Protocol (RFC 3507) that allows HTTP proxies to offload content processing to
external servers. An ICAP server can scan for malware, filter URLs, or rewrite
responses without modifying the proxy itself. Uses REQMOD and RESPMOD modes
to intercept HTTP requests and responses respectively.

**Difficulty:** Intermediate
**Category:** Protocol

---

## IDE — Integrated Development Environment

Software application bundling a code editor, debugger, compiler or interpreter,
and build tools into a single interface. Examples: VS Code, IntelliJ IDEA, Eclipse.
Modern IDEs add language servers via LSP, version control integration, and plugin
ecosystems that dramatically accelerate development workflows.

**Difficulty:** Base
**Category:** Dev

---

## IDS — Intrusion Detection System

Security system that monitors network traffic or host activity for malicious
patterns and policy violations. Passive by design: it detects and alerts but
does not block. Two main modes: signature-based (known attack patterns) and
anomaly-based (detecting deviation from a learned baseline).

**Difficulty:** Intermediate
**Category:** Security

---

## IDPS — Intrusion Detection and Prevention System

Extension of IDS that adds active inline blocking capability. Sits directly in
the traffic path and can drop packets, reset connections, or quarantine hosts
in real time. The prevention component introduces latency risk, so threshold
tuning is critical to avoid false positives blocking legitimate traffic.

**Difficulty:** Intermediate
**Category:** Security

---

## IEEE — Institute of Electrical and Electronics Engineers

International professional association that publishes widely adopted technical
standards. IEEE 802 defines Ethernet (802.3), Wi-Fi (802.11), and Bluetooth
(802.15). IEEE standards govern everything from power systems to embedded
software engineering practices and are referenced globally.

**Difficulty:** Base
**Category:** Networking

---

## IETF — Internet Engineering Task Force

Open standards organization that develops and promotes Internet protocols
primarily through the RFC process. Anyone can participate. Notable RFCs include
TCP (793), HTTP/2 (7540), and TLS 1.3 (8446). Working groups operate by
rough consensus and running code rather than formal voting.

**Difficulty:** Intermediate
**Category:** Protocol

---

## IGMP — Internet Group Management Protocol

Protocol used by IPv4 hosts and routers to manage multicast group membership.
A host sends an IGMP Join to subscribe to a multicast group; routers track
membership to avoid flooding multicast traffic on uninterested segments.
IGMPv3 adds source filtering for precise multicast source control.

**Difficulty:** Intermediate
**Category:** Networking

---

## IGRP — Interior Gateway Routing Protocol

Cisco-proprietary distance-vector routing protocol developed in the 1980s as an
improvement over RIP. Used composite metrics (bandwidth, delay, reliability,
load, MTU) rather than just hop count. Superseded by EIGRP and now obsolete,
but historically significant in large enterprise campus networks.

**Difficulty:** Advanced
**Category:** Networking

---

## IKE — Internet Key Exchange

Protocol used to establish a Security Association (SA) in the IPsec suite.
Runs over UDP port 500. IKEv1 used two phases; IKEv2 (RFC 7296) simplified
the exchange, added EAP authentication, and improved reliability. Handles
mutual authentication and negotiation of cipher parameters between peers.

**Difficulty:** Advanced
**Category:** Security

---

## ILP — Instruction-Level Parallelism

CPU optimization technique that executes multiple instructions simultaneously
within a single processor core. Achieved through pipelining, superscalar
execution, out-of-order execution, and speculative execution. Fundamentally
limited by data dependencies and control hazards between adjacent instructions.

**Difficulty:** Advanced
**Category:** Hardware

---

## IMAP — Internet Message Access Protocol

Email retrieval protocol (RFC 9051) that keeps messages on the server and
synchronizes state across multiple clients. Unlike POP3 which downloads and
optionally deletes, IMAP preserves folder structure and read/unread flags
server-side. Default port 143; port 993 for IMAPS over TLS.

**Difficulty:** Base
**Category:** Protocol

---

## IMEI — International Mobile Equipment Identity

15-digit unique identifier assigned to every GSM, UMTS, and LTE mobile device.
Used by carriers to block stolen devices from accessing the network. Structured
as TAC (Type Allocation Code) plus serial number plus a Luhn check digit.
Can be retrieved by dialing `*#06#` on most handsets.

**Difficulty:** Base
**Category:** Networking

---

## INET — Internet Address Family (Socket API)

Prefix used in POSIX socket programming to denote Internet address families.
`AF_INET` refers to IPv4 and `AF_INET6` to IPv6. Functions like `inet_aton()`
and `inet_ntop()` handle conversion between binary network representations and
human-readable dotted-decimal or colon-separated string formats.

**Difficulty:** Intermediate
**Category:** Dev

---

## INTR — Interrupt Signal

Hardware or software signal that pauses CPU execution to handle an urgent event.
Hardware interrupts originate from devices (keyboard, NIC, storage); software
interrupts are triggered by privileged instructions. The CPU saves context,
jumps to the ISR, handles the event, then resumes the interrupted task.

**Difficulty:** Intermediate
**Category:** Hardware

---

## IOCP — I/O Completion Port

Windows kernel mechanism for high-performance asynchronous I/O. Applications
submit I/O requests associated with a completion port; a thread pool dequeues
completion notifications as operations finish. Avoids one-thread-per-connection
overhead, enabling servers to handle thousands of concurrent connections efficiently.

**Difficulty:** Advanced
**Category:** OS

---

## IOPS — Input/Output Operations Per Second

Metric measuring the throughput of a storage device for discrete read and write
operations. Distinct from bandwidth (MB/s), which measures sequential data volume.
IOPS matters most for databases and VMs with many small random accesses.
NVMe SSDs reach millions of IOPS; spinning HDDs are limited to a few hundred.

**Difficulty:** Base
**Category:** Hardware

---

## IOT — Internet of Things

Ecosystem of physical devices embedded with sensors, software, and connectivity
that collect and exchange data over the Internet. Examples: smart thermostats,
industrial sensors, medical monitors. Security is a major concern since IoT
devices often lack update mechanisms and run with minimal compute resources.

**Difficulty:** Base
**Category:** Networking

---

## IPC — Inter-Process Communication

Set of OS mechanisms allowing processes on the same host to exchange data and
synchronize execution. Methods include pipes, named pipes (FIFOs), message
queues, shared memory, Unix domain sockets, and signals. Each has different
latency, throughput, and complexity trade-offs for different use cases.

**Difficulty:** Intermediate
**Category:** OS

---

## IPAM — IP Address Management

Practice and software category for planning, tracking, and managing IP address
space across an organization. A centralized IPAM system records all allocated
IPs, subnets, VLANs, and DNS/DHCP bindings. Prevents address conflicts and
aids capacity planning in large enterprise and cloud networks.

**Difficulty:** Intermediate
**Category:** Networking

---

## IPCP — IP Control Protocol

Network Control Protocol (NCP) within PPP responsible for negotiating IP layer
parameters over a point-to-point link. Negotiates IP addresses for both ends,
compression options, and DNS server addresses. Runs after LCP establishes the
link layer; IP traffic cannot flow until IPCP completes negotiation.

**Difficulty:** Advanced
**Category:** Protocol

---

## IPMI — Intelligent Platform Management Interface

Hardware-level interface for out-of-band server management. Operates independently
of the CPU and OS via a Baseboard Management Controller (BMC). Enables remote
power cycling, serial console access, sensor monitoring (temperatures, voltages,
fan speeds), and hardware event log access even when the server is powered off.

**Difficulty:** Intermediate
**Category:** Hardware

---

## IPV4 — Internet Protocol Version 4

Fourth version of the Internet Protocol, defining 32-bit addresses that yield
approximately 4.3 billion unique values. The dominant routing protocol since the
1980s. Address exhaustion (completed in most regions by 2011–2019) drove the
adoption of NAT and the eventual transition to IPv6.

**Difficulty:** Base
**Category:** Networking

---

## IPV6 — Internet Protocol Version 6

Successor to IPv4 using 128-bit addresses, providing 3.4×10³⁸ unique values.
Eliminates NAT by design, mandates IPsec support, and introduces stateless
address autoconfiguration (SLAAC). Dual-stack deployments run IPv4 and IPv6
simultaneously during the long transition period.

**Difficulty:** Intermediate
**Category:** Networking

---

## IPTV — Internet Protocol Television

Delivery of television content over IP networks instead of broadcast or cable.
Uses multicast for live TV and unicast for on-demand streaming. Requires Quality
of Service (QoS) guarantees to prevent buffering. Common protocols: IGMP for
channel join/leave, RTSP for stream control and session management.

**Difficulty:** Intermediate
**Category:** Networking

---

## IPS — Intrusion Prevention System

Inline network security device that inspects traffic in real time and actively
blocks detected threats. Unlike passive IDS, IPS sits directly in the data path
and can drop packets before delivery. Requires careful threshold tuning to
minimize false positives that would block legitimate business traffic.

**Difficulty:** Intermediate
**Category:** Security

---

## IRAM — Internal RAM

RAM embedded directly within a processor or microcontroller die rather than
connected as external DRAM chips. Offers significantly lower latency and higher
bandwidth due to physical proximity to CPU cores. Common in embedded systems,
DSPs, GPU shared memory, and network processor packet buffers.

**Difficulty:** Advanced
**Category:** Hardware

---

## IRQ — Interrupt Request

Signal line used by hardware devices to notify the CPU that they require
immediate attention. Legacy x86 systems used the 8259 PIC with 16 IRQ lines.
Modern systems use the APIC, which supports hundreds of IRQs with programmable
priority levels and can distribute interrupts across multiple CPU cores.

**Difficulty:** Intermediate
**Category:** Hardware

---

## ISDN — Integrated Services Digital Network

Circuit-switched telephone network standard providing digital transmission over
ordinary copper telephone wire. B channels (64 kbps each) carry voice or data;
the D channel carries signaling. BRI provides 2B+D; PRI provides 23B+D (North
America) or 30B+D (Europe). Largely replaced by DSL and fiber broadband.

**Difficulty:** Intermediate
**Category:** Networking

---

## ISO — International Organization for Standardization

Non-governmental organization that develops and publishes international standards
across virtually every industry. In computing: ISO 9660 (CD-ROM filesystem),
ISO 27001 (information security management), ISO/IEC 12207 (software lifecycle).
Also used colloquially for optical disc image files in the ISO 9660 format.

**Difficulty:** Base
**Category:** Protocol

---

## ISOC — Internet Society

International non-profit that supports the open development and use of the Internet.
Provides organizational and financial backing for the IETF, IRTF, and IAB.
Advocates for Internet access, security, and governance policies globally.
Founded in 1992 by Vint Cerf and Bob Kahn as steward of the open Internet.

**Difficulty:** Base
**Category:** Networking

---

## ISP — Internet Service Provider

Company that provides Internet access and related services to consumers and
businesses. Operates physical infrastructure (fiber, cable, DSL, wireless) and
connects to upstream transit providers. Also typically provides DNS resolution,
email hosting, and allocates public IP addresses to customers.

**Difficulty:** Base
**Category:** Networking

---

## ISR — Interrupt Service Routine

Function in OS kernel or firmware that executes in response to a hardware interrupt.
Must execute quickly to avoid blocking other interrupts. Typically saves registers,
reads/clears the device status, performs minimal handling, then schedules a
deferred work queue or bottom half for heavier processing outside interrupt context.

**Difficulty:** Advanced
**Category:** OS

---

## ITAR — International Traffic in Arms Regulations

United States export control regulations governing manufacture, sale, and
distribution of defense-related articles, services, and data. IT systems handling
ITAR-controlled technical data require strict access controls, US-person-only
access restrictions, encryption, and comprehensive audit trails.

**Difficulty:** Intermediate
**Category:** Security

---

## ITAM — IT Asset Management

Discipline of tracking and optimizing the full lifecycle of hardware and software
assets within an organization. Covers procurement, deployment, license compliance
monitoring, maintenance scheduling, and secure disposal. Reduces audit risk and
helps identify unused software licenses available for reclamation and cost savings.

**Difficulty:** Base
**Category:** Dev

---

## ITIL — IT Infrastructure Library

Framework of best practices for IT service management organized into a service
lifecycle: Strategy, Design, Transition, Operation, and Continual Improvement.
ITIL 4 (2019) updated the framework to align with Agile, DevOps, and cloud-native
practices, adding a Service Value System model for holistic service delivery.

**Difficulty:** Intermediate
**Category:** Dev

---

## ITU — International Telecommunication Union

United Nations specialized agency for information and communication technology
standards and global spectrum coordination. Publishes recommendations across
three sectors: ITU-T (telecommunications standards), ITU-R (radio), and ITU-D
(development). Manages allocation of radio frequencies and satellite orbital slots.

**Difficulty:** Intermediate
**Category:** Protocol

---

## IVR — Interactive Voice Response

Automated telephony system that interacts with callers using pre-recorded prompts
and recognizes DTMF tones or natural speech. Routes calls to correct queues,
collects account information, and handles routine requests without human agents.
Used extensively in banking, healthcare, and enterprise call center deployments.

**Difficulty:** Base
**Category:** Networking

---

## IXFR — Incremental Zone Transfer

DNS mechanism (RFC 1995) allowing a secondary nameserver to request only the
changes to a zone since its last synchronization, rather than a full AXFR transfer.
Reduces bandwidth consumption significantly for large zones. The primary server
must maintain a change history indexed by the DNS zone serial number.

**Difficulty:** Advanced
**Category:** Protocol


---

## IPSEC — IPsec Protocol Suite

IETF framework securing IP communications via cryptographic authentication and encryption at the network layer. Two modes: Transport (encrypts payload only, host-to-host) and Tunnel (encrypts the entire original IP packet, used in VPNs). Protocols: AH (authentication header) and ESP (encapsulating security payload). Key management: IKEv2 (RFC 7296, recommended) or legacy IKEv1.

**Difficulty:** Advanced
**Category:** Security

---

## INODE — Index Node Structure

Data structure in Unix/Linux file systems (ext4, XFS, Btrfs) storing file metadata: permissions, owner, timestamps, file size, and pointers to data blocks. Does not contain the filename, which is stored in the directory entry. Each file has one inode identified by a unique inode number. Running out of inodes prevents creating new files even with free disk space available.

**Difficulty:** Intermediate
**Category:** OS

---

## ISTIO — Istio Service Mesh

Open-source service mesh (CNCF graduated) adding traffic management, mTLS, observability, and policy enforcement to Kubernetes workloads without application code changes. Uses Envoy sidecar proxies injected into pods. Control plane: istiod. Configured via CRDs: VirtualService, DestinationRule, Gateway, AuthorizationPolicy. Provides circuit breaking, retries, and canary deployments.

**Difficulty:** Advanced
**Category:** Cloud

---

## IPMGR — IP Address Manager

Software component allocating, tracking, and managing IP address assignments across a network. Core functions: IPAM (IP Address Management), DNS and DHCP integration, subnet planning, conflict detection, and utilization reporting. Platforms: Infoblox, phpIPAM, NetBox, SolarWinds IPAM. NetBox is widely used as open-source IPAM with REST API and IaC integration.

**Difficulty:** Intermediate
**Category:** Networking

---

## ISATAP — Intra-Site Auto Tunnel Addressing

IPv6 transition mechanism (RFC 5214) allowing IPv6 communication over IPv4 infrastructure within an organization. Encapsulates IPv6 in IPv4 with an interface identifier derived from the IPv4 address. Deprecated in modern deployments; superseded by native dual-stack or 464XLAT/DS-Lite for IPv6 transition in enterprise and carrier environments.

**Difficulty:** Advanced
**Category:** Protocol

---

## ISAKMP — IKE Security Association Protocol

Framework (RFC 2408) for establishing Security Associations and exchanging cryptographic keys for IPsec. Defines message format and negotiation procedures but not specific algorithms. Forms the basis of IKEv1 Phase 1 (Main Mode, Aggressive Mode). Superseded by IKEv2, which merges ISAKMP and IKE into a simpler, more reliable exchange.

**Difficulty:** Advanced
**Category:** Security

---

## IPFIX — IP Flow Information Export

IETF standard (RFC 7011) for exporting IP flow data from routers and network devices to collectors. Successor to NetFlow v9 with a template-based approach where the exporter defines field types before sending records. Used for traffic analysis, capacity planning, security monitoring, anomaly detection, and ISP billing across carrier and enterprise networks.

**Difficulty:** Advanced
**Category:** Networking

---

## IMAPS — IMAP Secure Protocol

IMAP4 over implicit TLS on port 993. Provides encrypted email retrieval with full IMAP4 semantics: server-side message storage, folder management, message flags, server-side search, and selective download. Preferred over STARTTLS on port 143 for mail client configuration as the encrypted session begins immediately without protocol upgrade.

**Difficulty:** Intermediate
**Category:** Protocol

---

## INFRA — IT Infrastructure

Physical and virtual resources providing the foundation for computing systems: servers, networking, storage, power, and platform software. In Infrastructure as Code (IaC) contexts, infrastructure is defined declaratively (Terraform, Pulumi, Crossplane) and version-controlled. Cloud-native infrastructure follows the immutable infrastructure pattern: replace rather than modify.

**Difficulty:** Base
**Category:** Cloud

---

## IRQBL — IRQ Balance Daemon

Linux daemon (irqbalance) automatically distributing hardware interrupt requests across CPU cores to prevent a single core becoming the bottleneck for all device interrupts. Improves throughput on multi-core systems under heavy I/O load. Network performance tuning often pins specific NIC queue IRQs to dedicated CPU cores using /proc/irq/N/smp_affinity instead.

**Difficulty:** Advanced
**Category:** OS


---

## IOMMU — Input-Output Memory Management Unit

Hardware unit that maps device-visible virtual addresses to physical memory addresses, enabling DMA remapping. Intel calls it VT-d; AMD uses AMD-Vi. Critical for PCI passthrough in virtualization (VFIO), preventing DMA attacks from malicious or compromised PCIe devices, and enabling SR-IOV virtual functions to operate in isolated address spaces.

**Difficulty:** Advanced
**Category:** Hardware

---

## IDRAC — Integrated Dell Remote Access Controller

Out-of-band management controller embedded in Dell PowerEdge servers. Provides remote KVM (virtual console), power management, hardware monitoring, firmware updates, and OS deployment via a dedicated NIC and management web interface, Redfish API, and RACADM CLI. Operates independently of the host OS, allowing management even when the OS is crashed or offline.

**Difficulty:** Intermediate
**Category:** Hardware

---

## IPVS — IP Virtual Server

Layer-4 load balancing component built into the Linux kernel (netfilter framework). Supports NAT, DR (Direct Routing), and IP tunneling forwarding modes with scheduling algorithms including round-robin, least connections, weighted, and source hashing. Used by Kubernetes kube-proxy in IPVS mode as a scalable alternative to iptables for service routing.

**Difficulty:** Advanced
**Category:** Networking

---

## IMUX — Inverse Multiplexer

Device or protocol that aggregates multiple low-bandwidth links into a single logical channel, splitting traffic across them and reassembling at the far end. Used historically with ISDN bonding (multiple B-channels) and in multilink PPP (MLPPP). Modern equivalents include LACP bonding, SD-WAN path aggregation, and MPTCP.

**Difficulty:** Advanced
**Category:** Networking

---

## IKEV2 — Internet Key Exchange Version 2

Protocol (RFC 7296) used in IPsec to establish and manage Security Associations. IKEv2 replaces IKEv1's aggressive/main modes with a simplified four-message exchange (IKE_SA_INIT + IKE_AUTH). Supports MOBIKE for VPN mobility across IP changes (e.g., Wi-Fi to cellular), EAP authentication, and traffic selector negotiation.

**Difficulty:** Advanced
**Category:** Security
