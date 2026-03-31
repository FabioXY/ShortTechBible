
## OCSP — Online Certificate Status Protocol

Protocol (RFC 6960) for checking whether a specific X.509 certificate has been
revoked, as an alternative to downloading full CRLs. A client sends the certificate
serial number to the CA's OCSP responder and receives a signed response: good,
revoked, or unknown. OCSP Stapling embeds the responder's signed reply in the
TLS handshake to eliminate the client round-trip.

**Difficulty:** Intermediate
**Category:** Security

---

## ODBC — Open Database Connectivity

Microsoft API standard providing a common interface for applications to access
relational database management systems. An ODBC driver translates generic SQL
calls to the target database's native protocol. Supported by virtually every
RDBMS; widely used in data integration, ETL, and business intelligence tools.

**Difficulty:** Intermediate
**Category:** Dev

---

## OIDC — OpenID Connect

Identity layer built on top of OAuth 2.0 (RFC 8414) that adds user authentication
to OAuth's authorization framework. Returns an ID Token (a signed JWT) alongside
the access token, containing user identity claims. Standard for single sign-on
(SSO) across web and mobile applications.

**Difficulty:** Intermediate
**Category:** Security

---

## OLAP — Online Analytical Processing

Database workload category characterized by complex queries aggregating large
volumes of historical data across multiple dimensions. Contrasted with OLTP
(many small transactional reads/writes). OLAP systems (Snowflake, BigQuery,
ClickHouse) use columnar storage and vectorized execution optimized for analytics.

**Difficulty:** Intermediate
**Category:** Database

---

## OLTP — Online Transaction Processing

Database workload category handling large numbers of short, concurrent read and
write transactions — orders, payments, user registrations. Requires ACID guarantees,
row-level locking, and fast index-based access. Contrasted with OLAP; most
production relational databases (PostgreSQL, MySQL, Oracle) serve OLTP workloads.

**Difficulty:** Intermediate
**Category:** Database

---

## OOM — Out of Memory

Condition where the OS cannot satisfy a memory allocation request because all
physical RAM and swap space are exhausted. On Linux, the OOM killer selects and
terminates a process to free memory, guided by `oom_score_adj` values. Preventing
OOM requires memory limits on containers, proper swap configuration, and capacity
planning.

**Difficulty:** Intermediate
**Category:** OS

---

## OPEX — Operational Expenditure

Ongoing costs for running IT systems: hosting, cloud compute, software subscriptions,
personnel, and support contracts. Contrasted with CAPEX (Capital Expenditure)
for one-time purchases of hardware and software licenses. Cloud adoption typically
shifts IT spending from CAPEX to OPEX.

**Difficulty:** Base
**Category:** Dev

---

## ORB — Object Request Broker

Middleware component in the CORBA architecture that enables objects on different
machines and in different languages to communicate transparently. The ORB marshals
method calls into network messages and dispatches them to remote objects.
Largely replaced by REST, gRPC, and message queues in modern distributed systems.

**Difficulty:** Advanced
**Category:** Dev

---

## ORM — Object-Relational Mapping

Programming technique that converts data between incompatible type systems in
object-oriented languages and relational databases. The ORM framework generates
SQL from object operations, handles result set mapping, and manages connections.
Examples: Hibernate (Java), SQLAlchemy (Python), ActiveRecord (Ruby), Entity
Framework (C#).

**Difficulty:** Intermediate
**Category:** Dev

---

## OSI — Open Systems Interconnection

Seven-layer network model (ISO/IEC 7498-1) providing a conceptual framework for
network protocol design. Layers: Physical, Data Link, Network, Transport, Session,
Presentation, Application. Used as a reference model for troubleshooting and
protocol classification, though real protocols (TCP/IP) do not map cleanly to it.

**Difficulty:** Base
**Category:** Networking

---

## OSPF — Open Shortest Path First

Link-state interior gateway routing protocol (RFC 2328 for OSPFv2). Routers flood
Link State Advertisements (LSAs) to build a complete topology map, then compute
shortest paths using Dijkstra's algorithm. Supports areas to limit LSA flooding
scope. OSPFv3 extends OSPF for IPv6 (RFC 5340).

**Difficulty:** Advanced
**Category:** Networking

---

## OSS — Open Source Software

Software whose source code is made publicly available under a license permitting
inspection, modification, and redistribution. Common licenses: MIT, Apache 2.0,
GPL, LGPL. The OSS ecosystem underpins virtually all modern infrastructure:
Linux, Kubernetes, PostgreSQL, OpenSSL. Distinct from freeware (no source access).

**Difficulty:** Base
**Category:** Dev

---

## OTA — Over the Air

Mechanism for distributing firmware or software updates to devices wirelessly
without physical connection or manual user intervention. Used in smartphones,
IoT devices, vehicles, and embedded systems. Requires secure update channels
(signed images, TLS transport) to prevent malicious firmware injection.

**Difficulty:** Intermediate
**Category:** Networking

---

## OVA — Open Virtual Appliance

Single-file distribution format for virtual machine images, packaging the OVF
descriptor, virtual disk files (VMDK), and optional manifest into a single
compressed `.ova` archive. Simplifies VM distribution and import across
hypervisors (VMware, VirtualBox) that support the OVF standard.

**Difficulty:** Intermediate
**Category:** Cloud

---

## OVF — Open Virtualization Format

Open standard (DMTF DSP0243) for packaging and distributing virtual machines.
An OVF package consists of a descriptor XML file, disk image files (VMDK, VHD),
and optional certificate and manifest files. OVA is a single-file archive of
an OVF package. Supported by VMware, VirtualBox, and Proxmox importers.

**Difficulty:** Intermediate
**Category:** Cloud

---

## OVS — Open vSwitch

Production-quality, multilayer virtual switch designed for hypervisor environments.
Supports standard network features (VLANs, bonding, spanning tree, LACP, VXLAN,
GRE tunnels) and exposes a programmable dataplane via OpenFlow. Default virtual
switch in OpenStack deployments; supports hardware offloading via DPDK and
SmartNICs.

**Difficulty:** Advanced
**Category:** Networking

---

## OCRA — OATH Challenge Response Algorithm

RFC 6287 specification extending HOTP to support mutual challenge-response
authentication. Both client and server exchange challenges that are incorporated
into the OTP computation, providing two-way authentication and preventing replay
attacks. Used in hardware tokens and advanced OATH-compliant authentication systems.

**Difficulty:** Advanced
**Category:** Security

---

## OPAL — Open Platform for Privacy-preserving Data Analysis

Opal is also: Self-Encrypting Drive (SED) standard by the Trusted Computing Group
defining a security subsystem class for storage devices. An Opal-compliant drive
encrypts all data transparently using an AES key stored in hardware. Pre-boot
authentication unlocks the key; BitLocker and VeraCrypt can use Opal hardware.

**Difficulty:** Advanced
**Category:** Security

---

## OCFS — Oracle Cluster File System

Cluster-aware filesystem developed by Oracle for shared storage in Oracle RAC
(Real Application Clusters) deployments. Allows multiple nodes to mount and
access the same filesystem concurrently over shared block storage. OCFS2 is the
open-source version included in the Linux kernel since 2.6.16.

**Difficulty:** Advanced
**Category:** OS

---

## OVAL — Open Vulnerability and Assessment Language

XML-based language for describing machine state and vulnerability conditions in
a standardized way. Enables automated security compliance checking: OVAL definitions
describe what to check on a system, and scanners (OpenSCAP) evaluate the system
against those definitions to produce a compliance report.

**Difficulty:** Advanced
**Category:** Security

---

## OWRT — OpenWrt

Open-source Linux distribution targeting embedded network devices such as routers
and access points. Replaces vendor firmware with a fully customizable OS supporting
hundreds of packages. Used widely in home labs, mesh networking projects, and
enterprise branch office deployments needing custom routing behavior.

**Difficulty:** Intermediate
**Category:** OS

---

## OXML — Office Open XML

ISO/IEC 29500 standard for representing word processing, spreadsheet, and
presentation documents as ZIP-archived XML files. The native file format for
Microsoft Office 2007+ (`.docx`, `.xlsx`, `.pptx`). Defined by Microsoft and
standardized by ECMA International before ISO adoption, despite controversy
over the standardization process.

**Difficulty:** Intermediate
**Category:** Dev

---

## OBDA — Ontology-Based Data Access

Data integration approach using a formal ontology to provide a unified conceptual
view of heterogeneous data sources. Users query the ontology layer; a mapping
layer translates queries to the underlying databases. Applied in knowledge
graphs, semantic web applications, and enterprise data federation.

**Difficulty:** Advanced
**Category:** Database

---

## OLSR — Optimized Link State Routing

Proactive link-state routing protocol (RFC 3626) designed for mobile ad-hoc
networks (MANETs). Uses MultiPoint Relays (MPRs) to reduce flooding overhead
compared to full LSA flooding. Maintains routing tables continuously, unlike
reactive protocols that discover routes on demand. Used in mesh networking projects.

**Difficulty:** Advanced
**Category:** Networking

---

## OFDM — Orthogonal Frequency Division Multiplexing

Modulation technique dividing a wide radio channel into many narrow orthogonal
subcarriers, each carrying a fraction of the data stream. Highly resistant to
multipath interference. Foundation of Wi-Fi (802.11a/g/n/ac/ax), LTE, 5G NR,
and ADSL/VDSL broadband standards.

**Difficulty:** Advanced
**Category:** Networking

---

## OOBD — Object-Oriented Database

Database system storing data as objects consistent with object-oriented programming
concepts rather than rows in tables. Objects have attributes, methods, and class
hierarchies. Examples: db4o, Versant, ObjectDB. Lost ground to relational databases
in the 1990s; concepts partially re-emerged in document stores and ORMs.

**Difficulty:** Advanced
**Category:** Database

---

## OSCP — Offensive Security Certified Professional

Vendor certification from Offensive Security requiring candidates to compromise
multiple machines in a controlled lab environment within 24 hours, then write
a professional penetration testing report. Considered one of the most respected
hands-on penetration testing certifications in the industry.

**Difficulty:** Advanced
**Category:** Security

---

## OTDR — Optical Time Domain Reflectometer

Fiber optic test instrument that injects laser pulses into a fiber and measures
the reflected light over time to locate faults, splices, connectors, and measure
attenuation along the fiber length. Essential tool for fiber optic installation
and troubleshooting. Resolution typically down to 1 meter.

**Difficulty:** Intermediate
**Category:** Hardware

---

## ORDB — Open Relay Database

Historical database of mail servers configured to relay email for any sender,
enabling spam distribution. Operators blocked mail from listed servers. Now
largely replaced by modern RBLs (Real-time Blackhole Lists) like Spamhaus.
Open relay mail servers are still occasionally found in misconfigured environments.

**Difficulty:** Intermediate
**Category:** Security

---

## OUTP — Output (Port or Register Context)

In x86 assembly and system programming, `OUT` is the instruction writing a value
to a hardware I/O port. I/O ports are a separate address space from memory used
by legacy devices (PIC, PIT, ISA bus). Modern hardware prefers MMIO over port
I/O, but the x86 IN/OUT instruction pair remains in hardware abstraction layers.

**Difficulty:** Advanced
**Category:** Hardware

---

## ORCH — Orchestration

Automated arrangement and coordination of complex computer systems, middleware,
and services. In cloud: Kubernetes orchestrates containers; Ansible and Terraform
orchestrate infrastructure. Distinct from automation (scripting individual tasks)
in that orchestration manages dependencies, ordering, and state across many
components simultaneously.

**Difficulty:** Intermediate
**Category:** Cloud

---

## ONOS — Open Network Operating System

Open-source SDN controller platform developed by the Open Networking Foundation.
Provides a distributed, fault-tolerant control plane for carrier-grade software-defined
networking. Supports OpenFlow, P4, and NETCONF southbound APIs and offers high-level
network intent abstractions for application developers.

**Difficulty:** Advanced
**Category:** Networking

---

## OPSF — Operations Support Function

Generic term in telecommunications and IT management for systems and processes
supporting network operations: fault management, configuration management,
accounting, performance monitoring, and security (FCAPS). The operational backbone
enabling NOC teams to manage large-scale infrastructure effectively.

**Difficulty:** Intermediate
**Category:** Dev

---

## ORCS — Object Repository Control System

Source control and versioning system for large binary object repositories in
software development pipelines. Manages artifact versions, access control, and
retention policies for compiled binaries, container images, and firmware blobs.
Generically describes solutions like JFrog Artifactory and Sonatype Nexus.

**Difficulty:** Intermediate
**Category:** Dev


---

## OPSC — OpSec (Operational Security)
Process of identifying and protecting sensitive information that, if obtained by adversaries, could be used to compromise operations or systems. In IT security, OPSC covers practices like minimizing data exposure, avoiding information leakage in error messages, log hygiene, and limiting insider knowledge distribution. Originates from military intelligence doctrine.
**Difficulty:** Intermediate
**Category:** Security

---

## OCLP — OpenCore Legacy Patcher
Open-source project that patches macOS to run on Apple hardware older than the officially supported models. Injects drivers and kexts at boot time via OpenCore bootloader, enabling features like Metal GPU acceleration and Wi-Fi on unsupported Macs. Widely used to extend the lifespan of 2013-2017 Mac hardware.
**Difficulty:** Intermediate
**Category:** OS

---

## OVMF — Open Virtual Machine Firmware
UEFI firmware implementation for virtual machines, based on Intel's EDK II (EFI Development Kit). Used as the UEFI BIOS for QEMU/KVM guests, enabling Secure Boot, UEFI boot entries, and 64-bit boot without legacy BIOS emulation. Required for Windows 11 VMs and Linux guests needing UEFI runtime services.
**Difficulty:** Intermediate
**Category:** OS

---

## ORAN — Open RAN
Industry initiative (O-RAN Alliance) to disaggregate and standardize radio access network components through open interfaces. Separates the radio unit (RU), distributed unit (DU), and centralized unit (CU), allowing multi-vendor interoperability. Aimed at reducing telco vendor lock-in and enabling software-defined mobile network deployments.
**Difficulty:** Advanced
**Category:** Networking



---

## ONVIF — Open Network Video Interface Forum
Industry standard (backed by Axis, Bosch, Sony) defining interoperability protocols for IP-based physical security products: IP cameras, NVRs, access control, and video analytics. Profiles (S for streaming, T for advanced video, G for recording, A for access control) define feature sets. Uses SOAP/WSDL over HTTP for device discovery and configuration.
**Difficulty:** Intermediate
**Category:** Protocol


---

## OMAS — Open Metadata and Governance Service
EGERIA project component (Linux Foundation) that provides a set of REST and event-driven APIs for integrating metadata repositories, data catalogs, and governance tools. Enables consistent metadata management across heterogeneous data platforms (Hadoop, cloud, relational) through a distributed metadata bus.
**Difficulty:** Advanced
**Category:** Database
