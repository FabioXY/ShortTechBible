## HBA — Host Bus Adapter

A hardware component connecting a server to a storage network (SAN) via Fibre Channel, iSCSI, or SAS. HBAs offload storage protocol processing from the CPU, providing dedicated queues, DMA engines, and protocol acceleration. FC HBAs require unique WWPNs (World Wide Port Names) for fabric zoning. SmartHBAs combine NIC and HBA functions; software-defined HBAs use the main NIC with driver-level protocol handling.

**Difficulty:** Intermediate
**Category:** Hardware

---

## HDD — Hard Disk Drive

A magnetic storage device using rotating platters coated with ferromagnetic material, with read/write heads on actuator arms. HDDs store data by magnetizing regions of the platter surface. Access time includes rotational latency (up to half a revolution) and seek time (head movement). HDDs offer high capacity at low cost per GB but are slow (5–20 ms latency) and susceptible to physical shock, making them unsuitable for mobile workloads.

**Difficulty:** Base
**Category:** Hardware

---

## HDMI — High-Definition Multimedia Interface

A proprietary audio/video interface transmitting uncompressed digital video and audio over a single cable. HDMI 2.0 supports 4K at 60 Hz; HDMI 2.1 supports 8K at 60 Hz or 4K at 120 Hz with DSC. HDMI includes HDCP (copy protection), CEC (consumer electronics control for single-remote operation), ARC/eARC (audio return channel), and optional Ethernet channel. The connector is physically fragile; DisplayPort is preferred for workstations.

**Difficulty:** Base
**Category:** Hardware

---

## HMAC — Hash-based Message Authentication Code

A MAC construction using a cryptographic hash function combined with a secret key: HMAC(K, m) = H((K ⊕ opad) || H((K ⊕ ipad) || m)). HMAC provides both data integrity and sender authenticity. Used in JWT (HS256/HS512), TLS record authentication, API request signing (AWS Signature Version 4), and TOTP. Resistant to length-extension attacks that affect plain Merkle-Damgård hash functions.

**Difficulty:** Intermediate
**Category:** Security

---

## HSM — Hardware Security Module

A dedicated cryptographic processor providing tamper-resistant key generation, storage, and cryptographic operations. HSMs protect private keys from extraction: keys are generated and used entirely inside the HSM; they never appear in plaintext in host memory. Used for root CA key protection, payment processing (PCI HSMs), disk encryption key custody, and code signing. Cloud HSMs: AWS CloudHSM, Azure Dedicated HSM.

**Difficulty:** Advanced
**Category:** Security

---

## HFT — High-Frequency Trading

An algorithmic trading strategy executing thousands to millions of orders per second, profiting from microsecond-level price inefficiencies. HFT infrastructure minimizes latency at every level: co-location at exchange data centers, kernel-bypass networking (DPDK, RDMA), FPGA-based order processing, and custom PCBs with controlled trace lengths. HFT firms drive demand for ultra-low-latency networking technology.

**Difficulty:** Advanced
**Category:** Networking

---

## HLS — HTTP Live Streaming

An Apple-developed adaptive bitrate streaming protocol (RFC 8216) that segments video/audio into .ts or fMP4 chunks and serves them over HTTP. Clients download an M3U8 playlist describing available quality variants and fetch segments matching available bandwidth. HLS is supported natively in Safari and iOS; other platforms use JavaScript players (hls.js). The main competitor to MPEG-DASH for OTT video delivery.

**Difficulty:** Intermediate
**Category:** Protocol

---

## HTML — HyperText Markup Language

The standard markup language for web pages, defining structure and meaning via a hierarchy of elements. HTML5 added semantic elements (<article>, <nav>, <section>), native <audio>/<video>, Canvas API, Web Storage, WebSockets, and Web Workers. The HTML parser in browsers is remarkably error-tolerant; invalid HTML is silently corrected. HTML is not a programming language — it describes document structure, with behavior delegated to JavaScript.

**Difficulty:** Base
**Category:** Dev

---

## HTTP — HyperText Transfer Protocol

The application-layer protocol for web communication. HTTP/1.1 uses persistent TCP connections and pipelining; HTTP/2 multiplexes requests over a single TLS connection using binary framing; HTTP/3 uses QUIC (UDP) to eliminate head-of-line blocking at the transport layer. HTTP is stateless: each request is independent. Cookies and session tokens layer state on top.

**Difficulty:** Base
**Category:** Protocol

---

## HSTS — HTTP Strict Transport Security

A web security policy header (RFC 6797) instructing browsers to communicate with a site only via HTTPS for a specified duration (max-age). Once received, the browser enforces HTTPS even if the user types http://, preventing SSL-stripping attacks. The includeSubDomains and preload directives extend protection to all subdomains and submit the domain to browser preload lists (hard-coded HTTPS enforcement from first visit).

**Difficulty:** Intermediate
**Category:** Security

---

## HTOP — Interactive Process Viewer

A cross-platform interactive process monitoring utility (successor to top) with a color-coded, real-time display of CPU per-core usage, memory, swap, load averages, and a sortable/filterable process list. HTOP supports mouse interaction, tree view of process hierarchies, and direct process management (kill, renice, trace). Written in ncurses; the modern successor btop++ adds GPU monitoring.

**Difficulty:** Base
**Category:** OS

---

## HVAC — Heating, Ventilation, and Air Conditioning

Mechanical systems controlling temperature, humidity, and air quality in buildings. In data center contexts, HVAC (specifically precision cooling) is a critical infrastructure component: servers generate significant heat that must be removed to prevent throttling and hardware failure. Hot-aisle/cold-aisle containment, in-row cooling, liquid cooling, and free-air cooling (economization) are strategies for data center HVAC efficiency.

**Difficulty:** Base
**Category:** Hardware

---

## HWND — Window Handle

A Windows OS handle (opaque integer) uniquely identifying a top-level or child window within the Win32 API. HWNDs are returned by CreateWindow/CreateWindowEx and used in all window management API calls (ShowWindow, MoveWindow, SendMessage, DestroyWindow). The relationship between process, thread, and HWND is defined by the Windows message loop threading model; cross-thread window manipulation requires PostMessage, not direct API calls.

**Difficulty:** Intermediate
**Category:** OS

---

## HADR — High Availability Disaster Recovery

A combined strategy ensuring both continuous availability (HA) and business continuity after catastrophic events (DR). HADR solutions typically provide: local HA (clustering, mirroring) to handle component failures without downtime, and geographical DR (replication to a remote site) to handle site-level disasters. IBM Db2 HADR is a specific implementation providing log-shipping-based replication for Db2 databases.

**Difficulty:** Intermediate
**Category:** Database

---

## HPET — High Precision Event Timer

A hardware timer specification defined by Intel and Microsoft to replace legacy timer chips (PIT 8254, RTC) in PC systems. HPET provides at least three comparators with a minimum frequency of 10 MHz and sub-microsecond precision. Used by the OS for high-resolution timer events, sleep(), and clock_gettime(). In virtualized environments, HPET emulation can be a performance bottleneck; many hypervisors disable it.

**Difficulty:** Advanced
**Category:** Hardware

---

## HSRP — Hot Standby Router Protocol

A Cisco-proprietary FHRP protocol providing default gateway redundancy. One router holds the Active role, forwarding traffic for the virtual IP; others are in Standby, monitoring the active router via hello messages. On active router failure, the highest-priority standby router transitions to active and sends a gratuitous ARP to update downstream switch MAC tables. HSRP v2 supports IPv6 and 4096 group numbers.

**Difficulty:** Intermediate
**Category:** Networking

---

## HDCP — High-bandwidth Digital Content Protection

A digital copy protection scheme developed by Intel for HDMI, DisplayPort, DVI, and MHL connections. HDCP authenticates the receiving device against a revocation list and encrypts the display signal in real time. HDCP 2.2 is required for 4K UHD content playback; the entire chain (source, cable, display) must support it. HDCP has been cryptographically broken; master keys were leaked in 2010, enabling bypass.

**Difficulty:** Intermediate
**Category:** Security

---

## HPKP — HTTP Public Key Pinning

A deprecated HTTP security header (RFC 7469) allowing web servers to declare which certificate public keys (pins) browsers should accept. HPKP was designed to prevent MITM attacks using rogue CA-issued certificates. It was disabled by Chrome in 2018 and Firefox in 2020 due to catastrophic misconfiguration risks: a wrong pin could lock users out of a site permanently. Replaced by Certificate Transparency (CT) log monitoring.

**Difficulty:** Advanced
**Category:** Security

---

## HPACK — Header Compression for HTTP/2

The compression format (RFC 7541) used by HTTP/2 to reduce header overhead. HPACK uses a static table (61 predefined header/value pairs), a dynamic table (recently sent headers), and Huffman encoding. HPACK eliminates the verbose repetition of headers (User-Agent, Accept-Encoding, Cookie) across requests in the same HTTP/2 session, reducing per-request overhead by 80–90% compared to HTTP/1.1.

**Difficulty:** Advanced
**Category:** Protocol

---

## HEAP — Memory Heap

The region of a process's address space used for dynamic memory allocation (malloc/free in C, new/delete in C++). Unlike the stack (last-in, first-out, automatically managed), heap allocations have arbitrary lifetimes and must be explicitly freed. Heap fragmentation, use-after-free bugs, and double-free vulnerabilities are among the most common security vulnerabilities. Garbage-collected languages manage heap allocation automatically.

**Difficulty:** Intermediate
**Category:** OS

---

## HMM — Hidden Markov Model

A statistical model representing a system transitioning between hidden states, where only observable outputs (emissions) are visible. HMMs are parameterized by transition probabilities, emission probabilities, and initial state distribution, trained via the Baum-Welch algorithm (EM variant). Historically the dominant model for speech recognition and bioinformatics sequence alignment; largely replaced by deep learning but still used in structured prediction tasks.

**Difficulty:** Advanced
**Category:** AI

---

## HNAT — Hardware Network Address Translation

NAT processing performed entirely in hardware (by an ASIC or NPU) without CPU involvement, enabling line-rate packet forwarding on routers and home gateways. HNAT offload tables store active connection mappings; the hardware rewrites source/destination IP addresses and recalculates checksums for each packet. Critical for ISP edge routers handling millions of concurrent sessions at multi-gigabit speeds.

**Difficulty:** Advanced
**Category:** Networking

---

## HOST — Hostname / Host Record

In DNS, an A or AAAA record mapping a hostname to an IP address. In general usage, a "host" refers to any networked device (server, workstation, VM, container) identified by an IP address. The /etc/hosts file provides a local, static hostname-to-IP mapping that takes precedence over DNS on most systems, used for testing, split-horizon overrides, and ad blocking.

**Difficulty:** Base
**Category:** Networking

---

## HART — Highway Addressable Remote Transducer

An industrial communication protocol (IEC 61158) for communicating with smart field instruments (pressure sensors, flow meters, level transmitters) over 4–20 mA analog loops. HART superimposes a digital FSK signal (1200/2200 Hz) on the analog loop, enabling digital configuration and diagnostics alongside the existing analog reading without replacing wiring. Widely used in process automation and oil/gas industry.

**Difficulty:** Advanced
**Category:** Protocol

---

## HITS — Hyperlink-Induced Topic Search

A link analysis algorithm (Kleinberg 1999) computing two scores for each web page: Hub score (how well the page links to authoritative sources) and Authority score (how well the page is linked by high-quality hubs). HITS provided an alternative to PageRank for search ranking. The hub/authority duality concept influenced understanding of web graph structure and information network analysis.

**Difficulty:** Advanced
**Category:** Dev

---

## HELO — SMTP HELO Command

The original SMTP handshake command sent by a mail client to identify itself to a mail server, followed by its domain name (HELO mail.example.com). The server uses this to record the sender's claimed identity in Received headers. EHLO (Extended HELO) replaced HELO in ESMTP (RFC 5321), enabling capability negotiation (STARTTLS, AUTH, SIZE). Servers should not reject mail solely based on HELO mismatch but may use it in spam scoring.

**Difficulty:** Intermediate
**Category:** Protocol

---

## HIDS — Host-based Intrusion Detection System

A security system monitoring and analyzing activity on a single host (system calls, file integrity, log entries, network connections, registry changes) to detect malicious activity or policy violations. Unlike NIDS (network-based), HIDS has visibility into encrypted traffic because it monitors at the OS layer. Tools: OSSEC, Wazuh, Tripwire, AIDE, auditd. HIDS generates alerts but typically does not block activity (see HIPS).

**Difficulty:** Intermediate
**Category:** Security

---

## HIPS — Host-based Intrusion Prevention System

An evolution of HIDS that actively blocks detected malicious activity rather than only alerting. HIPS intercepts system calls, network connections, and process launches in real time, blocking those matching known attack patterns or behavioral anomalies. Modern EDR products incorporate HIPS functionality. The tradeoff: blocking can cause false positives that disrupt legitimate workloads, requiring tuning before strict enforcement.

**Difficulty:** Intermediate
**Category:** Security

---

## HECI — Host Embedded Controller Interface

The communication channel between the main CPU/OS and the Intel Management Engine (ME) embedded in the PCH (Platform Controller Hub). HECI enables the OS to send commands to and receive responses from the ME firmware for features like AMT (Active Management Technology), PAVP (Protected Audio Video Path), and firmware updates. The ME communicates independently of the OS over a separate out-of-band network path.

**Difficulty:** Advanced
**Category:** Hardware

---

## HFSC — Hierarchical Fair Service Curve

A Linux traffic control queuing discipline providing hierarchical bandwidth allocation with per-class delay guarantees. Unlike HTB (Hierarchical Token Bucket), HFSC models service curves (piecewise linear functions of service vs. time) enabling both bandwidth sharing and bounded latency for real-time traffic. Used in advanced QoS configurations for networks requiring strict latency bounds (VoIP, industrial control) alongside bulk traffic.

**Difficulty:** Advanced
**Category:** Networking

---

## HLSL — High-Level Shader Language

Microsoft's C-like programming language for writing GPU shader programs (vertex, pixel, geometry, compute, hull, domain shaders) in Direct3D. HLSL is compiled to DXBC (DirectX Bytecode) or DXIL (DirectX Intermediate Language for DXR/DirectX 12). Analogous to GLSL (OpenGL) and Metal Shading Language (Apple). HLSL shaders are the building blocks of all Direct3D rendering pipelines.

**Difficulty:** Advanced
**Category:** Dev

---

## HOOK — Software Hook

A programming mechanism intercepting function calls, messages, or events before they reach their intended target. Hooks allow extending or modifying behavior without modifying the original code. In Windows, SetWindowsHookEx installs system-wide or thread-level hooks for keyboard/mouse monitoring. In Linux, LD_PRELOAD hooks intercept libc calls. Security tools, debuggers, and API monitoring frameworks use hooks extensively; malware also uses hooks for keylogging and API interception.

**Difficulty:** Intermediate
**Category:** Dev

---

## HRSP — HTTP Response
Generic term for the server-side reply in an HTTP transaction. Consists of a status line (version, code, reason phrase), headers (Content-Type, Set-Cookie, Cache-Control, etc.), and optional body. Status codes are grouped: 1xx informational, 2xx success, 3xx redirect, 4xx client error, 5xx server error.
**Difficulty:** Base
**Category:** Protocol

---

## HDLC — High-level Data Link Control
ISO bit-oriented data link layer protocol (ISO 13239). Frames data with a flag sequence (01111110), address, control, and FCS fields. Foundation for many WAN protocols (PPP, LAPB, LAPD). Supports three frame types: I-frames (data), S-frames (supervisory), and U-frames (unnumbered/control).
**Difficulty:** Advanced
**Category:** Protocol

---

## HMIP — Hierarchical Mobile IP
Extension to Mobile IP that introduces a regional anchor point (MAP - Mobility Anchor Point) to localize handover signaling within a visited domain. Reduces handover latency and binding updates to the home agent by handling local mobility regionally. Defined in RFC 4140.
**Difficulty:** Advanced
**Category:** Protocol
