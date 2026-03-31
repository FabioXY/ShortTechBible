## BAAS — Backend as a Service

A cloud model that provides developers with pre-built backend infrastructure (authentication, databases, file storage, push notifications, APIs) accessible via SDKs, eliminating the need to manage servers. Examples include Firebase, AWS Amplify, and Supabase. BaaS accelerates mobile and web app development at the cost of vendor lock-in.

**Difficulty:** Intermediate
**Category:** Cloud

---

## BCD — Binary-Coded Decimal

An encoding where each decimal digit (0–9) is represented by its four-bit binary equivalent. BCD avoids floating-point rounding errors for base-10 calculations, making it standard in financial systems, point-of-sale terminals, and digital displays. Packed BCD stores two digits per byte; unpacked BCD stores one digit per byte.

**Difficulty:** Intermediate
**Category:** Hardware

---

## BCP — Business Continuity Planning

The process of creating systems and procedures to ensure critical business functions continue during and after a disaster. BCP encompasses risk assessment, recovery time objectives (RTO), recovery point objectives (RPO), failover procedures, and regular testing (DR drills). Distinct from Disaster Recovery (DR), which is a subset focused on IT systems.

**Difficulty:** Intermediate
**Category:** Dev

---

## BDD — Behavior-Driven Development

A software development methodology that extends TDD by writing tests in a natural language format (Gherkin: Given/When/Then) readable by non-technical stakeholders. BDD bridges the communication gap between developers and business. Tools like Cucumber, SpecFlow, and Behave parse Gherkin scenarios into executable test code.

**Difficulty:** Intermediate
**Category:** Dev

---

## BDR — Backup Designated Router

In OSPF multi-access networks, the BDR is elected as a standby for the Designated Router (DR). The DR and BDR are responsible for forming adjacencies with all other routers on the segment, reducing the number of OSPF adjacencies from O(n²) to O(n). If the DR fails, the BDR takes over without re-election.

**Difficulty:** Advanced
**Category:** Networking

---

## BER — Bit Error Rate

The ratio of incorrectly received bits to the total number of transmitted bits over a communication channel, expressed as a dimensionless ratio (e.g., 10⁻⁹). BER is the primary quality metric for digital transmission systems. It is affected by signal-to-noise ratio, modulation scheme, interference, and cable quality.

**Difficulty:** Intermediate
**Category:** Networking

---

## BFD — Bidirectional Forwarding Detection

A lightweight, protocol-agnostic hello mechanism designed to detect link failures in milliseconds rather than the seconds required by BGP/OSPF hold timers. BFD runs between two network nodes and notifies the upper-layer routing protocol when the path goes down, enabling sub-second convergence.

**Difficulty:** Advanced
**Category:** Networking

---

## BFS — Breadth-First Search

A graph traversal algorithm that explores all vertices at the current depth before moving to vertices at the next depth level, using a queue data structure. BFS finds the shortest path in unweighted graphs. It is used in network routing, web crawlers, social network analysis, and garbage collection (finding reachable objects).

**Difficulty:** Intermediate
**Category:** Dev

---

## BFT — Byzantine Fault Tolerance

The ability of a distributed system to continue operating correctly even when some nodes fail in arbitrary ways, including sending conflicting or malicious messages. BFT consensus algorithms (PBFT, Tendermint) can tolerate up to f faulty nodes in a system of at least 3f+1 nodes. Fundamental to blockchain and distributed ledger systems.

**Difficulty:** Advanced
**Category:** Dev

---

## BGA — Ball Grid Array

A surface-mount IC packaging type where the chip connects to the PCB via a grid of solder balls on the bottom surface rather than leads on the edges. BGA offers more connections per unit area, better electrical performance (shorter signal paths), and lower thermal resistance than QFP or DIP packages. Used for CPUs, GPUs, and RAM chips.

**Difficulty:** Intermediate
**Category:** Hardware

---

## BGP — Border Gateway Protocol

The routing protocol that drives the global internet. BGP exchanges reachability information between autonomous systems using TCP port 179. It is a path-vector protocol: each route advertisement carries the full AS path, enabling loop detection and policy-based routing. Misconfigurations can cause large-scale internet outages (route leaks, hijacks).

**Difficulty:** Advanced
**Category:** Networking

---

## BHT — Branch History Table

A hardware structure in a CPU's branch predictor that records the recent history of conditional branch outcomes (taken/not-taken) indexed by branch instruction address. The BHT allows the processor to predict future branch behavior and speculatively execute instructions before the branch condition is evaluated, reducing pipeline stalls.

**Difficulty:** Advanced
**Category:** Hardware

---

## BIND — Berkeley Internet Name Domain

The most widely deployed DNS server software, maintained by ISC (Internet Systems Consortium). BIND implements a full-featured authoritative name server and caching resolver. It introduced many DNS features that became RFCs, including DNSSEC validation. Configuration is done via named.conf and zone files.

**Difficulty:** Intermediate
**Category:** Protocol

---

## BIOS — Basic Input/Output System

Firmware stored in a chip on the motherboard that initializes hardware (POST), locates a bootable device, and hands control to the bootloader. BIOS uses a 16-bit real-mode interface and is limited to MBR-based booting from disks under 2 TB. Largely replaced by UEFI on modern systems, though the term is still widely used colloquially.

**Difficulty:** Base
**Category:** Hardware

---

## BIT — Binary Digit

The most fundamental unit of information in computing, representing one of two states: 0 or 1, off or on, false or true. All digital data is ultimately represented as sequences of bits. Eight bits form one byte. The term was coined by John Tukey in 1947 and popularized by Claude Shannon in information theory.

**Difficulty:** Base
**Category:** Hardware

---

## BIU — Bus Interface Unit

A component of a CPU that manages communication between the processor and the external system bus. The BIU handles fetch requests (reading instructions and data from memory), write operations, and cache line fills. In modern pipelined processors, the BIU is integrated into the memory subsystem and L1/L2 cache controllers.

**Difficulty:** Advanced
**Category:** Hardware

---

## BLE — Bluetooth Low Energy

A wireless personal area network technology introduced in Bluetooth 4.0, optimized for low power consumption at the cost of throughput. BLE operates in the 2.4 GHz ISM band and uses a different channel/packet structure than Classic Bluetooth. It is the foundation for IoT sensors, wearables, and proximity-based services (beacons).

**Difficulty:** Intermediate
**Category:** Networking

---

## BLOB — Binary Large Object

A data type in databases and storage systems used to store arbitrary binary data (images, video, compiled code, encrypted files) as a single opaque unit. BLOBs are typically stored outside the main table rows (in an overflow segment or separate object store) because their size is unpredictable and often large.

**Difficulty:** Base
**Category:** Database

---

## BLP — Bell-LaPadula Model

A formal state-machine security model for mandatory access control (MAC) in multi-level secure (MLS) systems. BLP defines two core properties: Simple Security (no read up — a subject cannot read data at a higher classification) and the Star Property (no write down — a subject cannot write data to a lower classification). Foundational in military and government security systems.

**Difficulty:** Advanced
**Category:** Security

---

## BMC — Baseboard Management Controller

A dedicated microcontroller embedded on a server motherboard that provides out-of-band management capabilities independent of the main CPU and OS. The BMC runs its own firmware, has its own network interface, and implements IPMI, Redfish, and KVM-over-IP, allowing remote power control, sensor monitoring, and console access even when the server is powered off.

**Difficulty:** Advanced
**Category:** Hardware

---

## BMR — Bare Metal Restore

A disaster recovery process that restores an entire system from scratch to blank hardware with no pre-installed OS, including the OS, applications, settings, and data, from a backup image. BMR solutions capture a complete system snapshot (including the boot sector and partition structure) and can restore to dissimilar hardware using driver injection.

**Difficulty:** Intermediate
**Category:** OS

---

## BOF — Buffer Overflow

A vulnerability that occurs when a program writes more data to a buffer than it can hold, overwriting adjacent memory. Stack-based BOFs can overwrite the return address to redirect execution to attacker-controlled code. Mitigated by ASLR, stack canaries, DEP/NX, and safe string-handling functions. One of the most historically exploited vulnerability classes.

**Difficulty:** Advanced
**Category:** Security

---

## BOM — Byte Order Mark

A Unicode character (U+FEFF) optionally placed at the beginning of a text stream to indicate byte order (endianness) and encoding. In UTF-8, the BOM (EF BB BF) is discouraged by the Unicode standard but used by Windows tools to signal UTF-8 encoding. In UTF-16, it is required to distinguish big-endian from little-endian encoding.

**Difficulty:** Intermediate
**Category:** Dev

---

## BOT — Automated Internet Bot

A software application that runs automated, repetitive tasks over the internet at much higher speed than a human. Bots account for a significant portion of internet traffic. Legitimate bots include web crawlers, monitoring agents, and chat bots. Malicious bots perform credential stuffing, DDoS, scraping, and spam distribution.

**Difficulty:** Base
**Category:** Security

---

## BPF — Berkeley Packet Filter

A virtual machine built into the Linux and BSD kernels that allows user-space programs to attach custom programs to network sockets and other kernel hooks. Classic BPF (cBPF) was used for tcpdump filters. Extended BPF (eBPF) is a general-purpose in-kernel virtual machine used for networking, observability, tracing, and security enforcement without kernel modules.

**Difficulty:** Advanced
**Category:** OS

---

## BPDU — Bridge Protocol Data Unit

A data frame used by Spanning Tree Protocol (STP) and its variants (RSTP, MSTP) to exchange information between switches. BPDUs carry the bridge ID, root bridge ID, path cost, and port role information. Switches use BPDUs to elect the root bridge and calculate the loop-free spanning tree topology.

**Difficulty:** Intermediate
**Category:** Networking

---

## BPS — Bits Per Second

The standard unit for measuring data transmission speed in digital communications. BPS expresses how many binary digits a channel can transfer per second. Common multiples: Kbps (10³), Mbps (10⁶), Gbps (10⁹). Not to be confused with bytes per second (Bps) — a distinction that matters when calculating file transfer times.

**Difficulty:** Base
**Category:** Networking

---

## BRAM — Block RAM

Dedicated static RAM blocks integrated directly into FPGA fabric, as opposed to distributed RAM built from LUTs. BRAMs are synchronous, dual-ported memory arrays (typically 18Kb or 36Kb per block) used for FIFOs, buffers, lookup tables, and on-chip data storage in FPGA designs. Xilinx and Intel FPGAs each have their own BRAM implementations.

**Difficulty:** Advanced
**Category:** Hardware

---

## BRK — Break Signal

In serial communications, a break signal is a prolonged spacing condition (logic 0) transmitted for longer than one character frame. BRK is used to signal the remote system to reset or interrupt the current session. In Unix terminals, sending a break generates SIGINT. In RS-232, a break of >200ms indicates a line fault or intentional interrupt.

**Difficulty:** Intermediate
**Category:** Protocol

---

## BSD — Berkeley Software Distribution

A Unix derivative developed at UC Berkeley from the late 1970s onward. BSD introduced many foundational networking concepts including the BSD socket API and the TCP/IP stack later adopted by virtually all operating systems. Modern descendants include FreeBSD, OpenBSD, NetBSD, and macOS (which uses a BSD-derived kernel called XNU).

**Difficulty:** Intermediate
**Category:** OS

---

## BSON — Binary JSON

A binary-encoded serialization format for JSON-like documents, used natively by MongoDB. BSON extends JSON with additional data types (int32, int64, double, datetime, binary, ObjectId, regex) and encodes length fields to enable fast traversal without parsing the full document. BSON documents can be larger than their JSON equivalents due to type metadata overhead.

**Difficulty:** Intermediate
**Category:** Database

---

## BSS — Block Started by Symbol

A segment in a compiled program's memory layout that holds uninitialized global and static variables. BSS is not stored in the executable file (it contains no data), only its size. The OS initializes BSS memory to zero at program load time. The name is historical, from an IBM 704 assembly directive meaning "Block Started by Symbol."

**Difficulty:** Intermediate
**Category:** OS

---

## BSOD — Blue Screen of Death

The colloquial name for the Windows stop error screen displayed when the kernel encounters a critical, unrecoverable error (hardware failure, driver bug, memory corruption). The BSOD shows a stop code (e.g., IRQL_NOT_LESS_OR_EQUAL, MEMORY_MANAGEMENT) and optionally generates a minidump file for post-mortem debugging with WinDbg.

**Difficulty:** Base
**Category:** OS

---

## BST — Binary Search Tree

A data structure where each node has at most two children, and all nodes in the left subtree have smaller keys while all nodes in the right subtree have larger keys. BSTs support O(log n) search, insert, and delete on average. Degenerate cases (sorted input) degrade to O(n); self-balancing variants (AVL, Red-Black) guarantee O(log n) worst case.

**Difficulty:** Intermediate
**Category:** Dev

---

## BWT — Burrows-Wheeler Transform

A data transformation algorithm (not itself a compressor) that rearranges characters in a string to improve the compression ratio of subsequent algorithms like move-to-front and Huffman coding. BWT is the core of the bzip2 compression format. The transform is reversible — the original string can be recovered from the transformed output.

**Difficulty:** Advanced
**Category:** Dev

---

## BYOD — Bring Your Own Device

An organizational policy that allows employees to use personally owned devices (smartphones, laptops, tablets) for work purposes and to access corporate resources. BYOD reduces hardware costs but introduces security challenges: mixed personal/corporate data, unmanaged patch levels, and difficulty enforcing security policies on devices the organization does not own.

**Difficulty:** Base
**Category:** Security

---

## BORG — BorgBackup
Deduplicating, compression, and encryption backup program for Linux/macOS. Uses content-defined chunking so only changed data is transmitted and stored. Supports LZMA, LZ4, zstd compression and AES-CTR encryption. Backups are stored as archives inside a repository; accessed via borg mount using FUSE.
**Difficulty:** Intermediate
**Category:** OS

---

## BRPF — Berkeley Packet Filter (Raw)
Raw access layer of the BPF kernel subsystem, providing a VM-based packet filtering engine at the network driver level. eBPF extends the classic BPF with a more capable instruction set, maps, and helper functions, enabling use beyond packet filtering: tracing, security policy, and XDP forwarding.
**Difficulty:** Advanced
**Category:** OS

---

## BYOK — Bring Your Own Key
Cloud encryption model where the customer generates and controls the master encryption key rather than relying on the provider's managed keys. Keys are stored in a customer-managed HSM or KMS (e.g. AWS CloudHSM, Azure Key Vault) and imported into the cloud service. Revocation immediately renders encrypted data inaccessible.
**Difficulty:** Intermediate
**Category:** Security
