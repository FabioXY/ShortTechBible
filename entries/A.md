## AAA — Authentication, Authorization, Accounting

A security framework that controls access to network resources. Authentication verifies identity, Authorization determines what the user can do, and Accounting tracks what they did. AAA is typically implemented via RADIUS or TACACS+ servers in enterprise networks and ISP environments.

**Difficulty:** Intermediate
**Category:** Security

---

## AAAA — IPv6 DNS Resource Record

The DNS record type that maps a domain name to an IPv6 address, analogous to the A record for IPv4. Named "quad-A" because IPv6 addresses are 128 bits — four times the 32 bits of IPv4. Resolvers query for AAAA records when the client has IPv6 connectivity.

**Difficulty:** Intermediate
**Category:** Networking

---

## ABAC — Attribute-Based Access Control

An access control model that evaluates policies based on attributes of the user, resource, environment, and action rather than fixed role assignments. ABAC enables fine-grained, dynamic authorization decisions (e.g., "allow access if user.department=HR and resource.classification=internal and time=business_hours"). More expressive than RBAC but harder to manage.

**Difficulty:** Advanced
**Category:** Security

---

## ACID — Atomicity, Consistency, Isolation, Durability

The four properties that guarantee database transactions are processed reliably. Atomicity means all operations in a transaction succeed or all roll back. Consistency ensures the database moves from one valid state to another. Isolation prevents concurrent transactions from interfering. Durability guarantees committed data survives crashes.

**Difficulty:** Intermediate
**Category:** Database

---

## ACL — Access Control List

A set of rules attached to a network interface, file system object, or other resource that specifies which users or systems are granted or denied access. ACLs operate at the packet level in networking (filtering by IP/port) and at the object level in file systems (defining read/write/execute permissions per user or group).

**Difficulty:** Intermediate
**Category:** Security

---

## ACME — Automatic Certificate Management Environment

An IETF protocol (RFC 8555) that automates the issuance, renewal, and revocation of TLS certificates between a certificate authority and a web server. ACME is the protocol behind Let's Encrypt. Clients like Certbot implement the ACME challenge-response flow to prove domain ownership without human interaction.

**Difficulty:** Intermediate
**Category:** Security

---

## ACPI — Advanced Configuration and Power Interface

A hardware abstraction layer and specification that allows the OS to manage device power states, thermal sensors, battery status, and hardware enumeration. ACPI replaced APM and is implemented in firmware as tables (DSDT, SSDT) that the OS kernel parses at boot to discover hardware topology.

**Difficulty:** Advanced
**Category:** OS

---

## ADC — Analog-to-Digital Converter

A circuit or chip that converts a continuous analog signal (voltage, current) into a discrete digital representation. The key parameters are resolution (bits per sample) and sampling rate (samples per second). ADCs are fundamental to audio interfaces, sensors, oscilloscopes, and any system that bridges the physical and digital worlds.

**Difficulty:** Intermediate
**Category:** Hardware

---

## ADFS — Active Directory Federation Services

A Microsoft identity federation service that extends Active Directory authentication across organizational boundaries using SAML 2.0 and WS-Federation. ADFS enables SSO between on-premises AD and external services (cloud apps, partner organizations) without synchronizing passwords externally.

**Difficulty:** Advanced
**Category:** Security

---

## ADSL — Asymmetric Digital Subscriber Line

A DSL technology that provides higher download bandwidth than upload bandwidth over existing copper telephone lines. ADSL uses frequencies above the voice band (25 kHz–1.1 MHz), allowing simultaneous voice and data. ADSL2+ reaches up to 24 Mbps downstream. Performance degrades with distance from the DSLAM.

**Difficulty:** Intermediate
**Category:** Networking

---

## AES — Advanced Encryption Standard

A symmetric-key block cipher standardized by NIST in 2001, operating on 128-bit blocks with key sizes of 128, 192, or 256 bits. It replaced DES and is the de facto standard for symmetric encryption across TLS, disk encryption, VPNs, and virtually every modern secure protocol.

**Difficulty:** Intermediate
**Category:** Security

---

## AGP — Accelerated Graphics Port

A dedicated point-to-point channel introduced by Intel in 1997 to connect a graphics card directly to the CPU and system memory, bypassing the PCI bus. AGP provided higher bandwidth for texture data transfers. Superseded by PCIe around 2004, AGP slots are now found only on legacy hardware.

**Difficulty:** Base
**Category:** Hardware

---

## AHCI — Advanced Host Controller Interface

A technical standard that defines the operation of Serial ATA (SATA) host controllers. AHCI enables advanced SATA features including Native Command Queuing (NCQ), hot-plugging, and port multiplier support. Operating systems need an AHCI driver to access these features; without it, the controller falls back to IDE compatibility mode.

**Difficulty:** Intermediate
**Category:** Hardware

---

## AIX — Advanced Interactive eXecutive

IBM's proprietary Unix operating system, running primarily on IBM Power Systems hardware. AIX is known for its advanced logical volume manager (LVM), Workload Partitions (WPARs), and enterprise-grade RAS features. It holds UNIX 03 certification and is widely used in large banking and financial institutions.

**Difficulty:** Advanced
**Category:** OS

---

## AJAX — Asynchronous JavaScript and XML

A web development technique that allows a browser to send HTTP requests and update parts of a page without a full page reload. Despite the name, modern AJAX typically uses JSON rather than XML. It was popularized by Gmail and Google Maps and is the foundation of all modern single-page application interactions.

**Difficulty:** Intermediate
**Category:** Dev

---

## ALUA — Asymmetric Logical Unit Access

A SCSI standard that allows a storage array to expose multiple paths to a LUN with different access states: Active/Optimized (preferred path through the owning controller) and Active/Non-Optimized (accessible but with higher latency via the non-owning controller). Multipath software uses ALUA state information to select the best path automatically.

**Difficulty:** Advanced
**Category:** Hardware

---

## ALU — Arithmetic Logic Unit

The fundamental digital circuit inside every CPU and GPU that performs integer arithmetic (add, subtract, multiply) and bitwise logic operations (AND, OR, XOR, NOT, shift). The ALU is fed operands from registers, performs the operation in a single clock cycle, and writes the result back to a register along with status flags (zero, carry, overflow).

**Difficulty:** Intermediate
**Category:** Hardware

---

## AMI — Amazon Machine Image

A pre-configured virtual machine template in AWS that contains the OS, application server, and application required to launch an EC2 instance. AMIs are region-specific but can be copied. They capture the root volume snapshot, launch permissions, and block device mapping. Public AMIs are shared by AWS and the community; private AMIs are account-specific.

**Difficulty:** Intermediate
**Category:** Cloud

---

## AMQP — Advanced Message Queuing Protocol

An open standard application-layer protocol (ISO/IEC 19464) for message-oriented middleware. AMQP defines a binary wire format, broker model (exchanges, queues, bindings), and delivery guarantees (at-most-once, at-least-once, exactly-once). RabbitMQ implements AMQP 0-9-1; Azure Service Bus implements AMQP 1.0.

**Difficulty:** Advanced
**Category:** Protocol

---

## ANSI — American National Standards Institute

A private non-profit organization that oversees the development of voluntary consensus standards for products, services, processes, and systems in the US. In IT, ANSI is known for standardizing character encoding (ANSI C, ANSI SQL), terminal escape codes (ANSI escape sequences), and coordinating with ISO on international standards.

**Difficulty:** Base
**Category:** Protocol

---

## APFS — Apple File System

Apple's proprietary file system introduced in 2017, replacing HFS+. APFS is designed for flash and SSD storage, featuring copy-on-write metadata, native encryption (per-volume or per-file), space sharing across volumes in a container, snapshots, cloning, and nanosecond timestamp precision. It is the default file system on all Apple platforms.

**Difficulty:** Intermediate
**Category:** OS

---

## APIC — Advanced Programmable Interrupt Controller

A hardware component in x86 systems that manages hardware interrupts more flexibly than the legacy 8259 PIC. Each CPU core has a Local APIC (LAPIC) for receiving interrupts; an I/O APIC routes device interrupts to the appropriate LAPIC. APICs support 256 interrupt vectors, interrupt priorities, and inter-processor interrupts (IPIs) for SMP coordination.

**Difficulty:** Advanced
**Category:** Hardware

---

## API — Application Programming Interface

A defined contract (set of endpoints, methods, request/response formats) that allows two software components to communicate without exposing internal implementation. APIs can be REST, GraphQL, RPC-based, or library-level. The key concept is abstraction: the caller does not need to know how the service works internally.

**Difficulty:** Base
**Category:** Dev

---

## APM — Application Performance Monitoring

A category of tools and practices that measure and manage the performance and availability of software applications. APM solutions collect metrics (response time, error rate, throughput), distributed traces, and logs to detect anomalies and identify bottlenecks. Examples: Datadog, New Relic, Dynatrace, OpenTelemetry.

**Difficulty:** Intermediate
**Category:** Dev

---

## APT — Advanced Persistent Threat

A prolonged, targeted cyberattack in which an intruder gains unauthorized access to a network and remains undetected for an extended period. APTs are typically state-sponsored or well-funded criminal groups targeting specific organizations for espionage, sabotage, or data theft. They use multiple stages: reconnaissance, initial compromise, lateral movement, exfiltration.

**Difficulty:** Advanced
**Category:** Security

---

## ARIN — American Registry for Internet Numbers

The Regional Internet Registry (RIR) responsible for distributing and managing IP addresses (IPv4 and IPv6) and ASNs in the United States, Canada, and many Caribbean and North Atlantic territories. ARIN receives address blocks from IANA and allocates them to ISPs, enterprises, and cloud providers in its service region.

**Difficulty:** Intermediate
**Category:** Networking

---

## ARM — Advanced RISC Machine

A family of RISC (Reduced Instruction Set Computer) processor architectures licensed by Arm Holdings. ARM cores use a fixed-width, load-store instruction set designed for power efficiency. ARM dominates mobile (virtually all smartphones), embedded systems, and increasingly servers and desktops (Apple Silicon, AWS Graviton, Ampere).

**Difficulty:** Intermediate
**Category:** Hardware

---

## ARP — Address Resolution Protocol

A Layer 2 protocol used to map a known IPv4 address to an unknown MAC address on a local network segment. A device broadcasts "Who has IP X?" and the owner replies with its MAC. ARP has no authentication, making it vulnerable to ARP spoofing and poisoning attacks.

**Difficulty:** Intermediate
**Category:** Networking

---

## ASM — Assembly Language

A low-level programming language with a strong correspondence to machine code instructions of a specific CPU architecture. Each assembly mnemonic (MOV, ADD, JMP, CALL) maps to one or a few machine instructions. Assembly is used for bootloaders, device drivers, performance-critical inner loops, and reverse engineering.

**Difficulty:** Advanced
**Category:** Dev

---

## ASN — Autonomous System Number

A unique identifier assigned to an autonomous system (a group of IP networks under a single routing policy) for use in BGP routing. ASNs are 16-bit (1–65535) or 32-bit (RFC 4893). Internet service providers and large organizations each hold one or more ASNs to exchange routing information on the global internet.

**Difficulty:** Advanced
**Category:** Networking

---

## ASLR — Address Space Layout Randomization

An OS security technique that randomizes the memory addresses used by a process (stack, heap, libraries, executable base) each time it runs. ASLR makes it harder for attackers to predict the location of code they want to execute after exploiting a memory corruption bug. Effective only when combined with DEP/NX and PIE compilation.

**Difficulty:** Advanced
**Category:** Security

---

## ASIC — Application-Specific Integrated Circuit

A chip designed for a specific application rather than general-purpose computation. ASICs deliver maximum performance and power efficiency for their target workload (Bitcoin mining, network packet processing, ML inference) because every transistor is dedicated to that function. They are expensive to design but cheap per unit at scale.

**Difficulty:** Advanced
**Category:** Hardware

---

## ASP — Active Server Pages

Microsoft's first server-side scripting platform (1996), allowing HTML pages to embed VBScript or JScript code executed on the web server before sending the response to the client. ASP (classic) was superseded by ASP.NET, which introduced compiled code, the .NET runtime, and a proper MVC framework.

**Difficulty:** Base
**Category:** Dev

---

## ATA — Advanced Technology Attachment

A parallel interface standard for connecting storage devices (HDDs, optical drives) to a motherboard, originally called IDE. ATA evolved through versions (ATA-1 through ATA-7) and was superseded by SATA. Still referenced in contexts like S.M.A.R.T. diagnostics, which originated from the ATA command set.

**Difficulty:** Base
**Category:** Hardware

---

## ATM — Asynchronous Transfer Mode

A cell-switching network technology that transmits data in fixed 53-byte cells (5-byte header + 48-byte payload). ATM supports simultaneous voice, video, and data with guaranteed QoS by using virtual circuits (VCs). Widely deployed in carrier backbone networks in the 1990s, ATM was largely replaced by MPLS and Ethernet.

**Difficulty:** Advanced
**Category:** Networking

---

## ATDD — Acceptance Test-Driven Development

A collaborative development practice where acceptance tests are written before implementation, driven by agreement between developers, testers, and business stakeholders. ATDD tests define the "done" criteria in human-readable form (often using Gherkin/Cucumber syntax) and serve as living documentation as well as regression tests.

**Difficulty:** Intermediate
**Category:** Dev

---

## AUP — Acceptable Use Policy

A set of rules governing how users may use an organization's network, systems, and internet access. AUPs define permitted and prohibited activities, security responsibilities, privacy expectations, and consequences for violations. Legally, a signed AUP establishes user consent and organizational liability boundaries.

**Difficulty:** Base
**Category:** Security

---

## AVI — Audio Video Interleave

A multimedia container format developed by Microsoft in 1992 as part of the Video for Windows framework. AVI interleaves audio and video data in a single file using the RIFF structure. While AVI supports multiple codecs (DivX, Xvid, H.264), it lacks native support for features like chapters, streaming, or variable frame rates found in modern containers like MKV or MP4.

**Difficulty:** Base
**Category:** Dev

---

## AVR — Alf and Vegard's RISC processor

An 8-bit RISC microcontroller architecture developed by Atmel (now Microchip), named after its designers Alf-Egil Bogen and Vegard Wollan. AVR microcontrollers execute most instructions in a single clock cycle due to a Harvard architecture with separate instruction and data buses. Arduino boards use AVR MCUs (ATmega328P and variants).

**Difficulty:** Intermediate
**Category:** Hardware

---

## AWS — Amazon Web Services

The cloud computing platform operated by Amazon, offering over 200 services including compute (EC2), storage (S3), databases (RDS, DynamoDB), networking (VPC), and AI/ML. AWS operates dozens of geographic regions, each with multiple isolated Availability Zones. It is the world's largest cloud provider by market share.

**Difficulty:** Base
**Category:** Cloud


---

## ADLDS — Active Directory Lightweight Directory Services

Standalone LDAP-compatible directory service in Windows Server running without a full AD domain. Provides application-specific directory data without Domain Controller infrastructure. Used by applications like Exchange and SharePoint for schema-isolated directory partitions. Managed via dsdbutil and Active Directory Sites and Services.

**Difficulty:** Advanced
**Category:** Security

---

## APIPA — Automatic Private IP Addressing

Windows and Linux fallback mechanism (RFC 3927) assigning a self-configured 169.254.x.x/16 address when DHCP is unavailable. Allows link-local communication between hosts on the same segment without a DHCP server. APIPA addresses are non-routable and their presence indicates DHCP failure during diagnostics.

**Difficulty:** Base
**Category:** Networking

---

## ASPNET — ASP.NET Framework

Microsoft web application framework built on the .NET runtime. Supports MVC, Web API, Razor Pages, and SignalR. ASP.NET Core (cross-platform successor) runs on Linux, macOS, and Windows with built-in dependency injection and a middleware pipeline. NuGet package manager handles dependencies; Kestrel is the built-in HTTP server.

**Difficulty:** Intermediate
**Category:** Dev

---

## ATAPI — AT Attachment Packet Interface

Extension of the ATA (IDE) interface allowing non-disk devices (CD-ROM, DVD, tape drives) to connect via the same ribbon cable and protocol. Uses SCSI command packets encapsulated over the ATA bus. Superseded by SATA with ATAPI tunneling support (SATA Packet Interface). Still referenced in optical drive and legacy hardware documentation.

**Difficulty:** Intermediate
**Category:** Hardware

---

## AXFR — DNS Zone Transfer Full

DNS operation (query type AXFR) transferring an entire zone from a primary to a secondary name server over TCP port 53. Initiated by the secondary server. Should be restricted to authorized secondary IPs via ACL or TSIG authentication to prevent zone enumeration by attackers.

**Difficulty:** Intermediate
**Category:** Protocol

---

## AIOPS — AIOps Platform

Application of artificial intelligence and machine learning to IT operations. Aggregates data from monitoring, logs, events, and metrics to automate anomaly detection, root cause analysis, and incident correlation. Platforms include Moogsoft, BigPanda, Dynatrace Davis AI, and IBM Watson AIOps. Reduces MTTA and MTTR by correlating related alerts automatically.

**Difficulty:** Advanced
**Category:** AI

---

## AUTHZ — Authorization Token

Short form of authorization: the process of determining what actions an authenticated identity is permitted to perform. Distinguished from AuthN (authentication). Implemented via RBAC, ABAC, policy engines (OPA, Cedar), and OAuth 2.0 scopes in modern identity-aware systems. Typically represented as claims in JWT tokens.

**Difficulty:** Base
**Category:** Security

---

## AUTHN — Authentication Method

Short form of authentication: verifying the identity of a user, device, or service. Methods include passwords, X.509 certificates (mTLS), biometrics, hardware tokens (FIDO2), and federated SSO assertions. Precedes Authorization (AuthZ) in the AAA security model. Multi-factor authentication (MFA) combines two or more independent AuthN factors.

**Difficulty:** Base
**Category:** Security

---

## ASNDB — Autonomous System Number Database

Repository mapping Autonomous System Numbers (ASNs) to registered organizations, country, and IP prefix ranges. Maintained by ARIN, RIPE, APNIC, and aggregators like CAIDA, MaxMind, and IPinfo. Used for geolocation, traffic attribution, BGP policy enforcement, and abuse contact lookup during incident response.

**Difficulty:** Intermediate
**Category:** Networking

---

## ARPTS — ARP Table Size

Maximum number of entries the kernel ARP cache can hold before eviction. Configurable on Linux via /proc/sys/net/ipv4/neigh/default/gc_thresh1-3. Undersized ARP tables cause packet loss in large Layer 2 segments with many hosts; oversized tables waste kernel memory. Monitor with ip neigh show and arp -n.

**Difficulty:** Intermediate
**Category:** Networking


---

## ALSA — Advanced Linux Sound Architecture

Kernel-level sound subsystem replacing OSS in Linux 2.6+. Provides device drivers for audio hardware, a user-space library (alsa-lib) for applications, and a plugin system for format conversion and resampling. ALSA uses device nodes under /dev/snd/ and exposes cards, PCM devices, and mixer controls.

**Difficulty:** Intermediate
**Category:** OS

---

## AIDE — Advanced Intrusion Detection Environment

Host-based IDS that builds a database of file attributes (hashes, permissions, timestamps, inodes) at baseline and detects deviations on subsequent scans. Configured via aide.conf with include/exclude rules and attribute selectors. Commonly run via cron and used to detect unauthorized file modifications.

**Difficulty:** Intermediate
**Category:** Security

---

## ABEND — Abnormal End

Term originating in IBM mainframe environments (OS/360) for a process termination caused by an unrecoverable error rather than a normal exit. Each ABEND carries a system or user completion code (e.g., S0C7 = data exception). The term persists in modern usage to describe any unexpected program crash.

**Difficulty:** Base
**Category:** OS

---

## AVFS — A Virtual File System

FUSE-based virtual filesystem allowing access to compressed and archive files (ZIP, TAR, GZ, BZ2) as if they were directories. Mounts archives transparently at ~/.avfs, enabling standard tools to read archive contents without explicit extraction. Used in file managers and shell scripts.

**Difficulty:** Intermediate
**Category:** OS
