## GAN — Generative Adversarial Network

A deep learning architecture (Goodfellow 2014) comprising two competing neural networks: a generator that produces synthetic data and a discriminator that distinguishes real from generated data. Training is a minimax game: the generator improves to fool the discriminator; the discriminator improves to detect fakes. GANs produce photorealistic images (StyleGAN, DALL-E predecessors) but are notoriously unstable to train.

**Difficulty:** Advanced
**Category:** AI

---

## GAP — Generic Access Profile

A Bluetooth specification defining how Bluetooth devices discover each other, establish connections, and manage security. GAP defines device roles (central, peripheral, broadcaster, observer), advertising packets, connection procedures, and bonding (pairing with key storage). GAP is the foundational layer all Bluetooth and BLE profiles build upon; without GAP compliance, interoperability between vendors would be impossible.

**Difficulty:** Intermediate
**Category:** Protocol

---

## GARP — Gratuitous ARP

An ARP request or reply where a host announces its own IP-to-MAC mapping without being asked, typically sent at interface initialization or when an IP address is claimed. Gratuitous ARPs update neighbor caches, detect IP conflicts (no reply = no conflict), and are exploited by FHRP protocols (HSRP, VRRP) to advertise a new active router's MAC after failover. Also a primary mechanism for ARP spoofing attacks.

**Difficulty:** Intermediate
**Category:** Networking

---

## GBE — Gigabit Ethernet

IEEE 802.3ab (1000BASE-T over copper) and 802.3z (1000BASE-X over fiber) standards delivering 1 Gbit/s Ethernet. 1000BASE-T uses all four pairs of Cat5e/Cat6 cabling with PAM-5 encoding. GbE replaced Fast Ethernet (100 Mbit/s) as the standard desktop and server interface in the mid-2000s. Now largely superseded by 10GbE in server infrastructure; 2.5GbE and 5GbE intermediate standards target NAS and Wi-Fi 6 uplink.

**Difficulty:** Base
**Category:** Networking

---

## GCC — GNU Compiler Collection

The primary open-source compiler suite for C, C++, Fortran, Ada, Go, and D, part of the GNU Project. GCC compiles source code through multiple stages: preprocessing, parsing, optimization (hundreds of GIMPLE/RTL passes), and code generation. GCC supports virtually every CPU architecture (x86, ARM, RISC-V, MIPS, PowerPC) and is the standard compiler for Linux kernel and GNU/Linux userland.

**Difficulty:** Intermediate
**Category:** Dev

---

## GCP — Google Cloud Platform

Google's public cloud computing platform providing infrastructure (GCE VMs, GKE Kubernetes, Cloud Storage, BigQuery, Cloud Spanner, Pub/Sub, Cloud Run). GCP competes with AWS and Azure; its differentiators include BigQuery (serverless data warehouse), TPU availability, and the global fiber backbone. Google Workspace integration and strong data analytics capabilities are key customer draw factors.

**Difficulty:** Base
**Category:** Cloud

---

## GDT — Global Descriptor Table

An x86 architecture data structure defining memory segments for the CPU, loaded via the LGDT instruction. GDT entries (segment descriptors) specify base address, limit, privilege level (ring 0–3), and type (code, data, system). In 64-bit long mode segmentation is mostly vestigial (flat 64-bit model), but the GDT still defines the TSS (Task State Segment) for syscall/interrupt privilege transitions and per-CPU data.

**Difficulty:** Advanced
**Category:** OS

---

## GDDR — Graphics Double Data Rate

A specialized DRAM technology designed for GPU memory with high bandwidth optimized for the wide parallel data buses of graphics cards. GDDR5/GDDR6/GDDR6X achieve bandwidth far exceeding DDR4/DDR5 system RAM by using wider buses, higher clock rates, and multi-channel interfaces. GDDR6X (used in NVIDIA RTX 4090) uses PAM4 signaling. HBM (High Bandwidth Memory) is an alternative for datacenter GPUs.

**Difficulty:** Intermediate
**Category:** Hardware

---

## GDPR — General Data Protection Regulation

The EU regulation (2016/679, effective May 2018) governing personal data collection, processing, storage, and transfer. GDPR grants EU residents rights over their data (access, erasure, portability, objection) and requires lawful basis for processing. Violations can be fined up to 4% of global annual revenue or €20 million. Applies to any organization processing data of EU residents, regardless of where the organization is located.

**Difficulty:** Intermediate
**Category:** Security

---

## GGUF — GGML Universal File Format

A binary file format for storing and distributing quantized large language models, introduced by the llama.cpp project as a replacement for the earlier GGML format. GGUF stores model tensors, metadata (vocabulary, hyperparameters, architecture description), and tokenizer data in a single self-describing file. It enables CPU/GPU inference of LLMs like LLaMA, Mistral, and Phi on consumer hardware via llama.cpp, Ollama, and LM Studio.

**Difficulty:** Advanced
**Category:** AI

---

## GFS — Google File System

A distributed file system developed by Google (2003 paper) for storing and processing large files across thousands of commodity servers. GFS uses a single master tracking metadata and chunk servers storing 64 MB data chunks replicated 3×. GFS influenced HDFS (Hadoop Distributed File System) and demonstrated that large-scale reliable storage could be built from unreliable commodity hardware with software fault tolerance.

**Difficulty:** Advanced
**Category:** Cloud

---

## GID — Group Identifier

A numeric identifier assigned to a user group in Unix/Linux systems, stored in /etc/group. Every file has an associated GID; group permissions apply to all users who are members of that group. The primary GID is the default group for new files; supplementary GIDs can be added. GIDs are used for access control in multiuser systems, container isolation (gid namespaces), and shared project directories.

**Difficulty:** Base
**Category:** OS

---

## GLBP — Gateway Load Balancing Protocol

A Cisco-proprietary FHRP protocol that extends HSRP/VRRP by providing active-active default gateway redundancy on a LAN. GLBP elects one Active Virtual Gateway (AVG) managing up to four Active Virtual Forwarders (AVFs), each advertising a different virtual MAC address for the shared virtual IP. Hosts receive different MAC addresses via ARP, distributing traffic across multiple physical routers.

**Difficulty:** Advanced
**Category:** Networking

---

## GLUE — General Language Understanding Evaluation

A multi-task benchmark (Wang et al. 2018) for evaluating English language understanding capabilities of NLP models across nine tasks (sentiment, natural language inference, coreference, question answering). SuperGLUE (2019) replaced it with harder tasks after models surpassed human-level performance. GLUE/SuperGLUE scores are the primary published metrics for comparing large language model progress.

**Difficulty:** Advanced
**Category:** AI

---

## GMAC — Galois Message Authentication Code

A message authentication code derived from GCM (Galois/Counter Mode) using only the GHASH authentication component without the CTR encryption step. GMAC produces an authentication tag over additional authenticated data (AAD) alone, without encrypting any plaintext. Used when authentication without confidentiality is needed, or as a building block in AEAD constructions where the encryption and authentication are composed.

**Difficulty:** Advanced
**Category:** Security

---

## GMM — Gaussian Mixture Model

A probabilistic model representing a distribution as a weighted sum of Gaussian (normal) distributions. Each component Gaussian captures a cluster of data; the EM (Expectation-Maximization) algorithm fits GMM parameters to observed data. Used in speaker recognition, anomaly detection, image segmentation, and density estimation. GMMs are the basis of classic HMM-based speech recognition systems.

**Difficulty:** Advanced
**Category:** AI

---

## GND — Ground (electrical)

The reference voltage level (0 V) in a circuit, serving as the return path for current and the baseline against which all other voltages are measured. In digital systems, GND must be shared between all components for correct operation. Ground planes in PCB design reduce impedance and noise coupling. Ground loops (two different ground potentials in a circuit) cause interference in audio and measurement systems.

**Difficulty:** Base
**Category:** Hardware

---

## GNN — Graph Neural Network

A class of neural networks operating directly on graph-structured data (nodes, edges, features). GNNs iteratively aggregate feature information from neighboring nodes (message passing), producing node or graph-level embeddings. Used in drug discovery (molecular property prediction), social network analysis, recommendation systems, fraud detection, and circuit design. Variants: GCN, GAT, GraphSAGE, MPNN.

**Difficulty:** Advanced
**Category:** AI

---

## GNSS — Global Navigation Satellite System

The generic term for satellite-based navigation systems, encompassing GPS (US), GLONASS (Russia), Galileo (EU), and BeiDou (China). GNSS receivers determine position by measuring signal travel time from at least four satellites, requiring nanosecond-precision timing. Multi-constellation GNSS receivers achieve sub-meter accuracy; differential GNSS (DGNSS) and RTK corrections enable centimeter-level precision.

**Difficulty:** Intermediate
**Category:** Hardware

---

## GPON — Gigabit Passive Optical Network

An ITU-T G.984 standard for fiber-to-the-home access networks. A single OLT (Optical Line Terminal) at the exchange connects to up to 128 ONUs (Optical Network Units) at premises via passive optical splitters. Downstream traffic is broadcast at 2.5 Gbit/s; upstream at 1.25 Gbit/s using TDMA. GPON is the dominant PON technology for residential FTTH deployments globally.

**Difficulty:** Advanced
**Category:** Networking

---

## GPIO — General Purpose Input/Output

Digital pins on a microcontroller or SBC that can be programmatically configured as inputs (reading switch states, sensor signals) or outputs (driving LEDs, relays, motors). GPIO pins typically support pull-up/pull-down resistors, interrupt-on-change, and sometimes PWM output or I2C/SPI/UART multiplexing. GPIO is the fundamental I/O interface in embedded development (Raspberry Pi, Arduino, ESP32).

**Difficulty:** Intermediate
**Category:** Hardware

---

## GPG — GNU Privacy Guard

An open-source implementation of the OpenPGP standard (RFC 4880) for encrypting and signing data and communications. GPG uses asymmetric cryptography (RSA, EdDSA, ECDH) for key exchange and digital signatures, and symmetric encryption for data. Used for email encryption (Enigmail, Delta Chat), package signing (Debian/RPM repos), git commit signing, and encrypted backups. GnuPG 2.x is the current maintained version.

**Difficulty:** Intermediate
**Category:** Security

---

## GPRS — General Packet Radio Service

A mobile data standard (2.5G) extending GSM networks to support packet-switched data transmission at up to 114 kbit/s theoretical (practical: 20–40 kbit/s). GPRS introduced an "always-on" data connection model, replacing circuit-switched modem connections. Superseded by EDGE (2.75G), UMTS/HSPA (3G), LTE (4G), and NR (5G). GPRS infrastructure is still used as fallback in IoT and M2M deployments.

**Difficulty:** Intermediate
**Category:** Networking

---

## GPS — Global Positioning System

The US-operated GNSS constellation of 31+ MEO satellites providing positioning, navigation, and timing (PNT) services globally. GPS receivers calculate position from the pseudorange to at least four satellites using time-of-flight of L-band radio signals. Civilian GPS accuracy is ~5 m; DGPS and RTK corrections achieve sub-centimeter. GPS timing underpins global financial systems, cellular networks, and power grid synchronization.

**Difficulty:** Base
**Category:** Hardware

---

## GPT — GUID Partition Table

A disk partitioning scheme defined in the UEFI specification, replacing MBR. GPT stores partition entries in a header and backup copy at the disk end, supports up to 128 partitions by default, handles disks larger than 2 TB, and assigns a unique 128-bit GUID to each partition. GPT includes a protective MBR to prevent legacy tools from treating a GPT disk as unpartitioned.

**Difficulty:** Intermediate
**Category:** Hardware

---

## GRE — Generic Routing Encapsulation

A Cisco-originated tunneling protocol (RFC 2784) encapsulating a wide variety of network-layer protocols inside IP packets. GRE adds a 4-byte header (protocol type, optional key, sequence number) enabling tunneling of multicast, IPv6 over IPv4, and non-IP protocols. GRE provides no encryption (combine with IPSec for security) and no congestion control. Used in DMVPN, LISP, and SDN overlays.

**Difficulty:** Intermediate
**Category:** Networking

---

## GRO — Generic Receive Offload

A Linux kernel network optimization that coalesces multiple received network packets with the same flow parameters into a single larger packet before passing them up the network stack. GRO reduces per-packet processing overhead (interrupt handling, protocol stack traversal) at the cost of slight latency. Complementary to GSO (Generic Segmentation Offload) on the transmit path. Enabled by default on modern Linux NICs.

**Difficulty:** Advanced
**Category:** OS

---

## GRPC — Google Remote Procedure Call

A high-performance, open-source RPC framework using HTTP/2 for transport and Protocol Buffers (protobuf) for interface definition and serialization. gRPC supports four communication patterns: unary, server streaming, client streaming, and bidirectional streaming. Built-in features include authentication (TLS, token), deadline propagation, cancellation, and load balancing. Dominant for microservice communication in cloud-native environments.

**Difficulty:** Intermediate
**Category:** Dev

---

## GRUB — Grand Unified Bootloader

The default bootloader for most Linux distributions, part of the GNU project. GRUB loads the kernel and initramfs, provides a boot menu with timeout, and supports chainloading. GRUB2 supports UEFI (installed to the EFI System Partition), GPT, multiple file systems (ext4, Btrfs, XFS, ZFS), scripting, and dynamic module loading. Configuration generated via update-grub/grub2-mkconfig from /etc/grub.d/.

**Difficulty:** Intermediate
**Category:** OS

---

## GSON — Google JSON

A Java library by Google for converting Java objects to JSON representation and back. GSON uses reflection to serialize/deserialize fields without requiring annotations by default. It supports custom serializers, deserializers, type adapters, and handles complex generics. Widely used in Android development. The main alternative in the Java ecosystem is Jackson, which generally offers better performance and richer annotation support.

**Difficulty:** Intermediate
**Category:** Dev

---

## GSLB — Global Server Load Balancing

A DNS and routing technique distributing traffic across servers in multiple geographically distributed data centers. GSLB uses DNS TTL manipulation, health checks, geographic proximity, and latency measurements to route users to the optimal data center. Differs from local load balancing (single data center): GSLB operates at the DNS layer across sites. Used by CDNs and multi-region active-active deployments.

**Difficulty:** Advanced
**Category:** Cloud

---

## GSM — Global System for Mobile Communications

The dominant 2G digital cellular standard (3GPP), using TDMA and frequency division to multiplex voice calls and SMS. GSM introduced the SIM card, encrypted air interface (A5/1 cipher, now broken), and roaming via the SS7 signaling network. GSM operates in 850/900/1800/1900 MHz bands. Despite 3G/4G/5G superseding it for data, GSM voice/SMS remains active in fallback scenarios and many IoT devices.

**Difficulty:** Intermediate
**Category:** Networking

---

## GTLD — Generic Top-Level Domain

A top-level domain (TLD) not tied to a specific country: .com, .net, .org, .info, .biz, and ICANN's 2012 new gTLD program adding over 1,200 TLDs (.tech, .cloud, .app, .dev). gTLDs are managed by ICANN-accredited registries; registration is open to anyone globally (unlike ccTLDs like .it, .uk which have country-specific eligibility rules). The .com gTLD managed by Verisign has over 160 million registrations.

**Difficulty:** Base
**Category:** Networking

---

## GUI — Graphical User Interface

A type of interface using visual components (windows, icons, buttons, menus, pointers) rather than text commands. GUIs rely on a windowing system (X11, Wayland, Win32, Cocoa/AppKit) and an event loop processing user input. While more accessible than CLIs, GUIs are harder to automate and script; remote management of GUI applications requires VNC, RDP, or X11 forwarding.

**Difficulty:** Base
**Category:** OS

---

## GUID — Globally Unique Identifier

A 128-bit label (synonymous with UUID) used to uniquely identify resources without central coordination. GUIDs appear in Windows registry keys, COM object class identifiers (CLSID), partition table entries (GPT), Active Directory object identifiers, and database primary keys. The standard format is 32 hex digits in 5 groups: {550e8400-e29b-41d4-a716-446655440000}. Version 4 (random) is most common.

**Difficulty:** Base
**Category:** Dev

---

## GZIP — GNU Zip

A file compression program and format (RFC 1952) using DEFLATE compression (LZ77 + Huffman coding). gzip compresses a single file and adds a header with original filename and CRC32 checksum. For multiple files, gzip is combined with tar (.tar.gz / .tgz). HTTP/1.1 and later support Content-Encoding: gzip for response compression; gzip reduces typical JSON/HTML payloads by 60–80%.

**Difficulty:** Base
**Category:** OS

---

## GPU — Graphics Processing Unit

A massively parallel processor with thousands of small cores optimized for SIMD operations on floating-point data. Originally designed for rasterizing 3D graphics, modern GPUs are general-purpose compute engines (GPGPU) via CUDA/OpenCL/ROCm. GPUs dominate ML training and inference due to their matrix multiplication throughput. Integrated GPUs (Intel UHD, Apple GPU) share system RAM; discrete GPUs have dedicated GDDR/HBM memory.

**Difficulty:** Intermediate
**Category:** Hardware

---

## GWLB — Gateway Load Balancer
AWS service (and similar in Azure) that provides transparent layer 3/4 load balancing for network virtual appliances (firewalls, IDS/IPS). Uses GENEVE encapsulation to forward traffic to appliance fleets while preserving the original packet flow. Scales appliance capacity without changing route tables or application configuration.
**Difficulty:** Advanced
**Category:** Cloud
