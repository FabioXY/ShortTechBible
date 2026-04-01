## FAB — Semiconductor Fabrication Facility

A manufacturing plant producing integrated circuits by depositing and patterning material layers on silicon wafers via photolithography. Process nodes (28nm, 7nm, 3nm) describe feature sizes; smaller nodes yield higher transistor density and lower power. Major fabs: TSMC, Samsung, Intel Foundry. Fabless companies (NVIDIA, AMD, Qualcomm) design chips but outsource fabrication entirely.

**Difficulty:** Advanced
**Category:** Hardware

---

## FACK — Forward Acknowledgment

A TCP congestion control enhancement using SACK information to track the highest sequence number transmitted, providing more accurate in-flight packet estimation during recovery. FACK allows faster cwnd recovery after loss without unnecessary retransmissions caused by the standard conservative SACK-based approach. Reduces throughput loss during recovery phases on high-bandwidth, high-latency links.

**Difficulty:** Advanced
**Category:** Protocol

---

## FAT — File Allocation Table

A file system using a table indexed by cluster number to track file ownership of clusters and free space. FAT12/FAT16/FAT32 variants differ in table entry width, directly limiting maximum volume and file size (FAT32: 4 GB file limit). exFAT removes the 4 GB limit and is the standard for SD cards and USB drives. FAT has no permissions, journaling, or integrity features.

**Difficulty:** Intermediate
**Category:** OS

---

## FCFS — First Come, First Served

The simplest CPU and I/O scheduling algorithm: processes are dispatched in arrival order. FCFS is non-preemptive, easy to implement, but produces high average waiting times in the presence of long jobs (convoy effect). On HDDs, FCFS seek scheduling is replaced by SSTF or LOOK algorithms to minimize mechanical seek time. In queuing theory, FCFS queues (M/M/1) are the baseline model.

**Difficulty:** Intermediate
**Category:** OS

---

## FDDI — Fiber Distributed Data Interface

An ANSI (X3T9.5) standard for 100 Mbit/s token-ring networks over optical fiber, widely used in campus backbone networks in the 1990s before Gigabit Ethernet made it obsolete. FDDI uses a dual counter-rotating ring for fault tolerance: if one ring breaks, traffic wraps to the secondary ring. FDDI introduced the concept of timed token rotation for deterministic access.

**Difficulty:** Intermediate
**Category:** Networking

---

## FDMA — Frequency Division Multiple Access

A channel access method dividing available bandwidth into separate frequency channels, allocating each to a different user. Each user has exclusive use of their assigned frequency channel for the duration of the connection. FDMA is used in first-generation (1G) cellular systems and traditional radio broadcasting. Contrast with TDMA (time-based slots) and CDMA (code-based separation).

**Difficulty:** Intermediate
**Category:** Protocol

---

## FDIR — Fault Detection, Isolation, and Recovery

An automated systems engineering discipline detecting failures, isolating the faulty component, and executing recovery procedures without human intervention. Used in spacecraft, nuclear plant control systems, and critical industrial infrastructure where human response latency is unacceptable. FDIR systems use redundant sensors, voting logic, watchdog timers, and predefined recovery sequences (safe modes, reconfiguration).

**Difficulty:** Advanced
**Category:** Dev

---

## FECN — Forward Explicit Congestion Notification

A Frame Relay header bit set by a switch to notify the destination that frames traversed a congested path. The receiver can relay this information back to the sender via the BECN (Backward Explicit Congestion Notification) bit. FECN/BECN were Frame Relay's congestion management mechanism, analogous to ECN in modern IP networks, enabling senders to reduce transmission rates before buffers overflow and frames are dropped.

**Difficulty:** Advanced
**Category:** Networking

---

## FFDC — First Failure Data Capture

An IBM-originated diagnostic philosophy and mechanism that captures comprehensive system state information at the exact moment of the first detected error, before any recovery or cleanup occurs. FFDC logs are written to stable storage atomically, preserving the pristine failure state for post-mortem analysis. Critical in production environments where reproducing a rare failure is difficult or impossible.

**Difficulty:** Advanced
**Category:** Dev

---

## FHS — Filesystem Hierarchy Standard

A specification defining the directory structure of Linux and Unix-like systems: /bin (essential binaries), /etc (configuration), /var (variable data, logs), /tmp (temporary files), /dev (device nodes), /proc and /sys (virtual kernel filesystems), /usr (user programs). Adherence ensures scripts and tools work across distributions; systemd and containers sometimes deviate from the traditional FHS layout.

**Difficulty:** Intermediate
**Category:** OS

---

## FIDO — Fast Identity Online

An open authentication standard family providing strong, phishing-resistant authentication. FIDO2 = WebAuthn (W3C browser API) + CTAP2 (authenticator protocol). Authentication uses public-key cryptography: the private key never leaves the authenticator (hardware key or platform biometric); credentials are origin-bound, preventing phishing. Passkeys are FIDO2 credentials synchronized via cloud for multi-device use.

**Difficulty:** Intermediate
**Category:** Security

---

## FIFO — First In, First Out

A data structure (queue) and scheduling discipline where the first element enqueued is the first removed. In OS: named pipes (mkfifo), process scheduling, and packet queues. In networking, FIFO queuing is fair but subject to head-of-line blocking: one large flow delays all others. Contrast with LIFO (stack), LRU (cache eviction), and priority queues used in QoS scheduling.

**Difficulty:** Base
**Category:** OS

---

## FILO — First In, Last Out

Synonymous with LIFO (Last In, First Out) — the ordering discipline of a stack. The first element pushed is the last popped. FILO/LIFO describes CPU call stacks, undo buffers, browser history navigation, and depth-first search implementations. The term is less common than LIFO but used in hardware documentation (stack machine ISAs) and some storage media (tape backup rotation policies).

**Difficulty:** Base
**Category:** Dev

---

## FIPS — Federal Information Processing Standards

Mandatory security standards for US federal information systems developed by NIST. FIPS 197 standardizes AES; FIPS 180 defines SHA hash functions; FIPS 186 defines DSA/ECDSA signatures; FIPS 140-3 specifies security requirements for cryptographic modules (four levels). "FIPS mode" in OpenSSL and OS libraries restricts algorithms to FIPS-approved ones, disabling MD5, RC4, DES, and non-approved elliptic curves.

**Difficulty:** Advanced
**Category:** Security

---

## FLAC — Free Lossless Audio Codec

An open-source lossless audio compression format reducing file size 40–60% vs uncompressed PCM without any quality loss. FLAC supports sample rates up to 655 kHz, bit depths up to 32 bits, and up to 8 channels. Files include embedded CRC checksums for corruption detection. Widely supported in audiophile hardware, music servers (Plex, Navidrome), and streaming platforms offering lossless tiers.

**Difficulty:** Base
**Category:** Protocol

---

## FLOP — Floating-Point Operation Per Second

A benchmark unit measuring processor performance in floating-point arithmetic. One FLOP/s = one floating-point multiply or add per second. Modern GPUs deliver TFLOP/s (10¹²) or PFLOP/s (10¹⁵) for FP16/BF16 tensor operations. Useful for comparing AI training hardware: NVIDIA H100 delivers ~2,000 TFLOP/s in FP16 with sparsity. FLOP count also quantifies the computational cost of an ML model.

**Difficulty:** Intermediate
**Category:** Hardware

---

## FOSS — Free and Open Source Software

Software distributed with source code under licenses granting rights to use, study, modify, and redistribute. Copyleft licenses (GPL, LGPL, AGPL) require derivative works to remain open; permissive licenses (MIT, BSD, Apache 2.0) allow proprietary derivatives. FOSS forms the bedrock of modern infrastructure: Linux, OpenSSL, PostgreSQL, Python, Kubernetes, nginx, and the Android base all depend on it.

**Difficulty:** Base
**Category:** Dev

---

## FPGA — Field-Programmable Gate Array

A reconfigurable integrated circuit with an array of logic blocks, configurable routing, and I/O cells programmable after manufacturing. FPGAs are configured in HDL (Verilog, VHDL) or via HLS tools. Used for ASIC prototyping, SDR, HFT, video processing, and cloud acceleration (AWS F1, Azure FPGA). FPGAs offer lower latency than CPUs for specific workloads but require specialist hardware design skills.

**Difficulty:** Advanced
**Category:** Hardware

---

## FPU — Floating-Point Unit

A CPU component performing IEEE 754 floating-point arithmetic: add, subtract, multiply, divide, square root, and transcendental functions. FPUs handle 32-bit (single) and 64-bit (double) precision with hardware rounding modes and exception flags (NaN, infinity, underflow, overflow). Modern CPUs include SIMD FPU extensions (SSE, AVX-512, NEON) performing parallel floating-point on vectors.

**Difficulty:** Intermediate
**Category:** Hardware

---

## FQBN — Fully Qualified Board Name

A unique identifier in the Arduino ecosystem specifying the target hardware platform for compilation, formatted as vendor:architecture:board[:options] (e.g., arduino:avr:uno). FQBNs are used by arduino-cli and the Arduino IDE 2.x to select the correct compiler toolchain, bootloader, and linker flags. Required when scripting builds in CI/CD pipelines or cross-compiling for multiple embedded targets.

**Difficulty:** Intermediate
**Category:** Hardware

---

## FQDN — Fully Qualified Domain Name

A hostname specifying the complete absolute path in the DNS hierarchy, including all labels and the trailing root dot (e.g., mail.example.com.). The trailing dot is often omitted in practice but required in DNS zone files. Without it, the name is relative and resolved against the search domain. FQDNs are required in TLS certificates (SAN entries), SSL pinning, and Kerberos service principal names.

**Difficulty:** Intermediate
**Category:** Networking

---

## FRAM — Ferroelectric RAM

A non-volatile memory technology combining DRAM-like read/write speeds with flash-like persistence. FRAM stores bits using the polarization state of a ferroelectric material (PZT or SBT) rather than charge in a capacitor. Unlike NAND flash, FRAM has near-unlimited write endurance and no erase cycle. Used in smart meters, RFID tags, industrial PLCs, and medical implants requiring fast non-volatile storage.

**Difficulty:** Advanced
**Category:** Hardware

---

## FSB — Front Side Bus

The parallel bus connecting the CPU to the memory controller hub (northbridge) in pre-2008 Intel PC architectures. All CPU-to-RAM and CPU-to-PCIe traffic shared the FSB, creating a system-wide bottleneck. Replaced by Intel QPI (later UPI) and AMD HyperTransport: point-to-point, serial, high-bandwidth links that eliminate the shared bus and integrate the memory controller directly into the CPU die.

**Difficulty:** Intermediate
**Category:** Hardware

---

## FSCK — File System Check

A Unix utility checking and repairing file system consistency: superblocks, inode tables, block allocation bitmaps, and directory entries. Run automatically at boot after unclean shutdowns. Modern journaling file systems (ext4, XFS) rarely need manual fsck runs — the journal enables fast recovery. ZFS and Btrfs perform continuous checksumming and scrubbing, detecting and repairing corruption without fsck.

**Difficulty:** Intermediate
**Category:** OS

---

## FTP — File Transfer Protocol

A TCP-based protocol (ports 20/21) for transferring files. FTP has two connection modes: active (server initiates data connection to client, problematic with NAT) and passive (client initiates both connections). FTP transmits credentials and data in plaintext — insecure on untrusted networks. Replaced by SFTP (SSH-based, port 22) and FTPS (TLS-wrapped FTP) for secure transfers.

**Difficulty:** Base
**Category:** Protocol

---

## FTDI — Future Technology Devices International

A semiconductor company known for its USB-to-serial bridge ICs (FT232, FT2232, FT4232) widely used in embedded development for connecting microcontrollers and FPGAs to a PC via USB. FTDI chips provide a virtual COM port and are found in Arduino boards, logic analyzers, and JTAG adapters. In 2014, FTDI released controversial driver updates that bricked counterfeit FTDI chips.

**Difficulty:** Intermediate
**Category:** Hardware

---

## FTPS — File Transfer Protocol Secure

FTP extended with TLS encryption. Explicit FTPS (FTPES) upgrades a plaintext FTP connection to TLS via the AUTH TLS command; implicit FTPS negotiates TLS immediately on port 990. Distinct from SFTP, which is an entirely different protocol over SSH. FTPS reuses FTP commands and responses (LIST, RETR, STOR) over encrypted channels; SFTP uses a different command set (SSH_FXP_* packets).

**Difficulty:** Intermediate
**Category:** Security

---

## FTTH — Fiber to the Home

A last-mile broadband architecture delivering optical fiber directly to residential premises. FTTH enables symmetric multi-gigabit speeds with no distance-based degradation. PON (Passive Optical Network) architectures use wavelength multiplexing to share a single feeder fiber among 32–128 homes. FTTH provides decades of bandwidth headroom by changing only endpoint transceivers rather than re-cabling infrastructure.

**Difficulty:** Intermediate
**Category:** Networking

---

## FUSE — Filesystem in Userspace

A Linux/macOS kernel interface allowing non-privileged code to implement file systems as user-space programs. The kernel forwards VFS operations (open, read, write, readdir) to the FUSE daemon via /dev/fuse. Used for SSHFS, cloud mounts (S3Fuse, gcsfuse), encrypted filesystems (EncFS, gocryptfs), and archive mounts (archivemount). The kernel/userspace boundary crossing adds latency compared to in-kernel filesystems.

**Difficulty:** Advanced
**Category:** OS

---

## FWSM — Firewall Service Module

A high-performance Cisco firewall blade for the Catalyst 6500 chassis providing stateful packet inspection, NAT, and multiple security contexts (virtual firewalls) as a line card. FWSM ran a PIX/ASA-derived OS at multi-gigabit throughput. End-of-sale in 2012, replaced by the Cisco ASA 5585-X and later Firepower NGFW. Historically significant as an early modular, multi-context firewall architecture.

**Difficulty:** Advanced
**Category:** Security

---

## FWTK — Firewall Toolkit

An early open-source firewall toolkit from Trusted Information Systems (TIS, early 1990s) pioneering application-layer proxy firewalls. FWTK provided dedicated ALG proxies for each protocol (FTP, SMTP, HTTP, Telnet) rather than packet filtering, enabling deeper inspection. FWTK concepts influenced the design of all subsequent application-aware firewalls. Now historically obsolete but foundational to the field.

**Difficulty:** Advanced
**Category:** Security

---

## FWUP — Firmware Update

The process of replacing firmware in non-volatile memory (flash, EEPROM). Firmware updates patch vulnerabilities, add hardware support, and fix bugs. Secure update mechanisms verify update authenticity via code signing (ECDSA, RSA) before flashing. UEFI Capsule Update, OTA (Over-The-Air) for embedded devices, and FIDO Device Onboard are standardized secure update frameworks preventing malicious firmware injection.

**Difficulty:** Intermediate
**Category:** Hardware

---

## FXML — JavaFX Markup Language

An XML-based UI description language for defining JavaFX application interfaces declaratively, analogous to XAML (WPF) or HTML. FXML files describe scene graph hierarchies (layouts, controls, event handlers) that are loaded at runtime by the FXMLLoader class. FXML separates UI structure from application logic and is used with the Scene Builder visual editor for drag-and-drop JavaFX UI design.

**Difficulty:** Intermediate
**Category:** Dev

---

## FRAG — IP Fragmentation

The process of splitting an IP datagram into smaller packets to fit a link's MTU. IPv4 fragmentation can occur at any router; IPv6 restricts it to the source host (using Path MTU Discovery). All fragments carry the same identification field; the destination reassembles them. Fragmentation increases attack surface (Teardrop, overlapping fragment attacks) and reassembly overhead; Path MTU Discovery (PMTUD) avoids it by discovering the minimum MTU on the path.

**Difficulty:** Intermediate
**Category:** Networking

---

## FMEA — Failure Mode and Effects Analysis

A systematic method for identifying potential failure modes in a system or process, their causes, and their effects on system operation. FMEA assigns a Risk Priority Number (RPN = Severity × Occurrence × Detectability) to prioritize mitigation. Used in hardware design, software architecture review, and DevOps reliability engineering (chaos engineering and game day exercises operationalize FMEA findings).

**Difficulty:** Advanced
**Category:** Dev

---

## FCOS — Fedora CoreOS

A minimal, container-optimized Linux distribution that automatically applies OS updates atomically (using rpm-ostree layered image system) and reboots into the new version, with automatic rollback on failure. FCOS is the successor to CoreOS Container Linux and is designed for running containerized workloads at scale. Configuration is declarative via Ignition (JSON/YAML provisioning format) applied at first boot.

**Difficulty:** Advanced
**Category:** Cloud

---

## FTAM — File Transfer, Access and Management

An ISO OSI application-layer protocol (ISO 8571) providing file transfer and remote file manipulation capabilities in the OSI networking stack. FTAM was the OSI-stack equivalent of FTP, offering more complex virtual file store semantics including partial file access and structured file types. Never widely adopted outside of government and telecom networks; FTP and later SFTP dominated in TCP/IP environments.

**Difficulty:** Advanced
**Category:** Protocol

---

## FSCM — File System Change Monitor
Kernel or userspace subsystem that tracks filesystem events (create, modify, delete, rename) and notifies applications. Linux: inotify (per-file) and fanotify (filesystem-wide). macOS: FSEvents. Windows: ReadDirectoryChangesW. Used by IDEs, backup tools, antivirus, and live-reload development servers.
**Difficulty:** Intermediate
**Category:** OS

---

## FHRP — First Hop Redundancy Protocol

Category of protocols providing default gateway redundancy by allowing multiple routers to present a single virtual IP and MAC to hosts. Examples: HSRP (Cisco), VRRP (RFC 5798, open standard), GLBP (Cisco, load-balancing variant). The active/master router responds to ARP for the virtual IP; standby takes over on failure detection.

**Difficulty:** Intermediate
**Category:** Networking

---

## FLASK — Flask Web Framework

Lightweight Python WSGI micro web framework using Werkzeug for WSGI utilities and Jinja2 for templating. No built-in ORM or form validation. Suitable for REST APIs and small to medium web applications. Extensions (Flask-SQLAlchemy, Flask-Login, Flask-Migrate) add functionality on demand. Flask's simplicity makes it a common first framework for Python web development.

**Difficulty:** Base
**Category:** Dev

---

## FSYNC — File Sync System Call

POSIX system call flushing a file's dirty pages from the kernel page cache to persistent storage, ensuring durability before returning. Critical for database crash consistency: PostgreSQL, SQLite, and MySQL use fsync for WAL writes. fdatasync() flushes data without metadata. Disabling fsync dramatically improves write throughput at the cost of data loss on power failure.

**Difficulty:** Advanced
**Category:** OS

---

## FDISK — Fixed Disk Partition Tool

Interactive command-line partitioning utility for MBR (and GPT in modern versions) disks. Creates, deletes, resizes, and changes partition type codes. On Linux: fdisk /dev/sdb launches interactive mode; no changes are written until the user saves explicitly. For GPT disks gdisk and parted are preferred alternatives. Replaced on modern systems by partprobe for kernel notification.

**Difficulty:** Base
**Category:** OS

---

## FPERM — File Permission Bits

Set of access rights (read, write, execute) on a file or directory for owner, group, and others in POSIX systems. Represented as octal (chmod 755) or symbolic (rwxr-xr-x). Extended by ACLs (getfacl/setfacl) for per-user and per-group rules. Special bits: SUID (execute as owner), SGID (execute as group or inherit group on directory), sticky bit (restrict deletion to owner).

**Difficulty:** Base
**Category:** OS

---

## FRRTG — FRRouting Suite

Free Range Routing: open-source IP routing protocol suite for Linux and Unix, forked from Quagga and maintained by the Linux Foundation. Implements BGP, OSPF, IS-IS, RIP, EIGRP, PIM, LDP, MPLS, and EVPN via modular daemons managed by a central zebra daemon. Used in network appliances, SD-WAN, and data center routing.

**Difficulty:** Advanced
**Category:** Networking

---

## FWKNOP — FireWall KNock Operator

Single Packet Authorization (SPA) implementation keeping firewall ports closed until a valid encrypted, authenticated single UDP packet is received. Authorizes temporary access (e.g. opens SSH for a specific source IP for 30 seconds). Services are completely invisible to unauthenticated port scanners, providing stealth port access control.

**Difficulty:** Advanced
**Category:** Security

---

## FSIMG — File System Image

Binary snapshot of a complete file system stored as a single file. Created with dd, mkfs imaging options, or specialized tools. Used for OS deployment (golden images), embedded system flashing (rootfs.img), VM disk images (ext4 inside qcow2), and forensic acquisition. Mountable via loopback device (mount -o loop image.img /mnt).

**Difficulty:** Intermediate
**Category:** OS

---

## FUTEX — Fast Userspace Mutex

Linux kernel primitive (syscall futex(2)) enabling userspace synchronization with minimal kernel involvement. In the uncontended case, lock/unlock operations use atomic CPU instructions entirely in userspace memory. The kernel is invoked only on contention (futex_wait) or wakeup (futex_wake). Foundation for pthreads mutexes, semaphores, and Java monitors on Linux.

**Difficulty:** Advanced
**Category:** OS

---

## FRIDA — Dynamic Instrumentation Toolkit

Open-source dynamic binary instrumentation framework for reverse engineering and security research. Injects a JavaScript engine (Duktape/V8) into target processes, allowing runtime function hooking, memory inspection, and API interception on Android, iOS, Linux, Windows, and macOS without modifying binaries. Widely used in mobile app security testing.

**Difficulty:** Advanced
**Category:** Security

---

## FWCTL — Firmware Control

Linux kernel subsystem (introduced in 6.11) providing a standardized userspace API for firmware-specific device management operations not covered by existing subsystems. Exposes a character device per firmware interface, allowing privileged userspace tools to issue vendor-specific commands to hardware (SmartNICs, DPUs, storage controllers).

**Difficulty:** Advanced
**Category:** OS
