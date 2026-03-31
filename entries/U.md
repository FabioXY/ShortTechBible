## UEFI — Unified Extensible Firmware Interface

Modern replacement for BIOS providing a standardized firmware interface between
hardware and OS. Features: graphical pre-boot environment, Secure Boot (blocking
unsigned bootloaders), network boot, support for GPT disks larger than 2 TB,
and a modular driver model (EFI drivers) independent of the OS.

**Difficulty:** Intermediate
**Category:** Hardware

---

## UDP — User Datagram Protocol

Connectionless transport protocol (RFC 768) providing low-overhead packet delivery
without reliability, ordering, or flow control guarantees. Applications tolerate
or handle losses themselves. Used by DNS, DHCP, TFTP, NTP, QUIC, and real-time
media (RTP) where latency matters more than reliability.

**Difficulty:** Base
**Category:** Networking

---

## UDEV — Userspace Device Manager

Linux device management daemon (part of systemd) that handles dynamic device
events from the kernel. When hardware is connected or disconnected, `udev` processes
udev rules to name devices consistently, set permissions, load kernel modules,
and trigger other actions like creating symlinks in `/dev/disk/by-id/`.

**Difficulty:** Intermediate
**Category:** OS

---

## UEAP — Unified Extensible Authentication Protocol

Generalized reference to EAP (Extensible Authentication Protocol) unified with
UEFI-based pre-boot authentication environments. Used in network access control
scenarios where authentication must occur before an OS boots, integrating with
802.1X RADIUS infrastructure from the UEFI firmware level.

**Difficulty:** Advanced
**Category:** Security

---

## ULID — Universally Unique Lexicographically Sortable Identifier

Alternative to UUID designed to be both globally unique and lexicographically
sortable by generation time. Consists of a 48-bit millisecond timestamp and 80
bits of randomness, encoded in 26-character Crockford Base32. Useful in distributed
systems where sorted ordering of generated IDs is important for indexing.

**Difficulty:** Intermediate
**Category:** Dev

---

## UMTS — Universal Mobile Telecommunications System

Third-generation (3G) mobile broadband standard developed by 3GPP. Uses WCDMA
(Wideband CDMA) radio access. Provides data rates up to 42 Mbps with HSPA+
evolution. Succeeded by LTE (4G). Still used as fallback in areas without 4G/5G
coverage, with global sunset underway.

**Difficulty:** Intermediate
**Category:** Networking

---

## UNFS — User-space NFS Server

NFS server implementation running entirely in user space rather than the Linux
kernel. Examples: `unfs3`, `nfs-ganesha`. Allows more flexible configuration,
container deployment, and support for non-traditional backends (object storage,
distributed filesystems) compared to the in-kernel NFS server.

**Difficulty:** Advanced
**Category:** OS

---

## UNIX — Unix Operating System

Family of multitasking, multiuser operating systems originating at Bell Labs in
1969 (Thompson, Ritchie). Key design principles: everything is a file, small
tools doing one thing well, pipelines composing tools. Linux, macOS, FreeBSD,
and Solaris are Unix-like systems. POSIX standardizes the Unix API.

**Difficulty:** Base
**Category:** OS

---

## UPNP — Universal Plug and Play

Set of networking protocols enabling devices on a LAN to automatically discover
and configure services without manual setup. Used by media servers (UPnP AV),
routers (port forwarding via IGD), and printers. Historically exploited by malware
for automatic port opening; should be disabled on internet-facing interfaces.

**Difficulty:** Intermediate
**Category:** Networking

---

## UPSR — Unidirectional Path Switching Ring

SONET/SDH network protection topology using two unidirectional fiber rings
(one working, one protect). Traffic is simultaneously transmitted on both rings;
the receiver selects the better signal. Failover is sub-50ms when the working
path fails. Used in metropolitan fiber rings for carrier-grade resilience.

**Difficulty:** Advanced
**Category:** Networking

---

## URLL — URL Encoding

Wait, URLL is not standard. Replacing with: ## URLP — URL Path Hierarchical part of a URL between the authority component and query string, identifying a specific resource within a web server or application. RESTful API design uses the URL path to identify resources (nouns) while HTTP methods (verbs) define operations. Path parameters encode resource identifiers (e.g., `/users/42`).

**Difficulty:** Base
**Category:** Dev

---

## USBA — USB Audio

USB device class standard defining how audio devices (headsets, microphones,
speakers, audio interfaces) communicate with a host over USB without requiring
vendor-specific drivers. USB Audio Class 1.0 (UAC1) is natively supported on
all platforms; UAC2 adds high-resolution audio (24-bit/192 kHz) and requires
driver support (standard on macOS and Linux, third-party on Windows).

**Difficulty:** Intermediate
**Category:** Hardware

---

## USBC — USB Type-C

Reversible USB connector standard defined in USB 3.2 and USB4 specifications.
Physically the same connector for USB 2.0 through USB4 Gen 3×2 (40 Gbps) and
DisplayPort Alt Mode. Can carry power (USB Power Delivery up to 240W), data,
video, and audio simultaneously. Replaces legacy Type-A, Type-B, micro, and mini.

**Difficulty:** Base
**Category:** Hardware

---

## USBF — USB Firmware

Firmware running on the microcontroller inside a USB device implementing the
USB protocol stack and device-specific functionality. USB firmware vulnerabilities
(BadUSB attack exploits firmware reprogramming) can make devices impersonate
other device classes (HID keyboard) to execute malicious payloads on a host.

**Difficulty:** Advanced
**Category:** Security

---

## USMM — USM (User-based Security Model) for SNMP

SNMPv3 security model providing authentication (HMAC-MD5 or HMAC-SHA) and optional
privacy (DES, AES) for SNMP messages. Eliminates the insecure community string
approach of SNMPv1/v2c. Users are defined with authentication and privacy
passphrases that are converted to keys using a key derivation function.

**Difficulty:** Advanced
**Category:** Protocol

---

## UTFT — Universal TFT Display Library

Open-source display driver library for Arduino and similar microcontroller platforms
supporting a wide range of TFT LCD display controllers. Provides a hardware
abstraction layer for drawing text, shapes, and bitmaps across different display
chipsets via common SPI or parallel interfaces.

**Difficulty:** Intermediate
**Category:** Hardware

---

## UUID — Universally Unique Identifier

128-bit identifier formatted as 8-4-4-4-12 hexadecimal groups (RFC 4122).
Version 1: time + MAC address. Version 4: random (most common). Version 5:
SHA-1 hash of namespace + name. Used as primary keys in distributed databases,
correlation IDs in logging, and resource identifiers in APIs.

**Difficulty:** Intermediate
**Category:** Dev

---

## ULMT — Ulimit Setting

Per-process resource limit configured via `ulimit` command or `pam_limits` module.
Controls maximum open file descriptors (`nofile`), process count (`nproc`), virtual
memory (`as`), CPU time (`cpu`), and core dump size (`core`). Low `nofile` limits
cause "too many open files" errors in network servers handling thousands of connections.

**Difficulty:** Intermediate
**Category:** OS

---

## ULOG — Userspace Netfilter Logging

Linux netfilter target redirecting matched packets to a userspace daemon for
logging or processing rather than kernel-level logging. `ULOG` (deprecated) and
`NFLOG` (current) forward packet data to userspace via netlink sockets. Used
by `ulogd2` for high-performance firewall log collection and storage.

**Difficulty:** Advanced
**Category:** OS

---

## UNTC — Untrusted Certificate

TLS/PKI term for a certificate that cannot be validated against a trusted root
or intermediate CA in the receiver's trust store. Causes browser warnings (NET::ERR_CERT_AUTHORITY_INVALID)
and API client errors. Common causes: self-signed certificates, expired intermediate
CAs, or missing chain certificate files in server configuration.

**Difficulty:** Intermediate
**Category:** Security

---

## URNG — Userspace RNG

Random number generation happening in application or library code rather than
the kernel. Userspace libraries implement CSPRNGs (ChaCha20 in libsodium) seeded
from kernel entropy (`/dev/urandom`, `getrandom()`). After seeding, the CSPRNG
can generate large volumes of random bytes efficiently without system call overhead.

**Difficulty:** Advanced
**Category:** Security

---

## UGID — UID/GID Mapping

Mapping of user and group identifiers between different namespace contexts in
Linux containerization. User namespaces allow containers to have an internal UID 0
(root) mapped to an unprivileged UID (e.g., 100000) on the host kernel, providing
isolation. Configured via `/proc/<pid>/uid_map` and `/proc/<pid>/gid_map` files.

**Difficulty:** Advanced
**Category:** OS

---

## USMT — User State Migration Tool

Microsoft utility transferring user data, application settings, and Windows
customizations between PCs during OS migrations or refreshes. Operates in two
phases: `scanstate` (capture from source) and `loadstate` (restore to destination).
Used in enterprise Windows deployment projects managed via SCCM/Intune.

**Difficulty:** Intermediate
**Category:** OS

---

## ULNX — Linux Utilities (Generic Label)

Informal abbreviation referring to the collection of GNU core utilities (coreutils),
util-linux, and procps packages providing standard command-line tools on Linux
systems: `ls`, `cp`, `mv`, `kill`, `df`, `mount`, `ps`, `top`. The Linux
Standard Base (LSB) defines which utilities must be present.

**Difficulty:** Base
**Category:** OS

---

## UPGR — Upgrade Process

Managed procedure of advancing software, firmware, or an operating system to a
newer version. Upgrade strategies: in-place (overwrite existing installation),
blue-green (switch traffic between two identical environments), canary (roll
out to a subset), and rolling (update nodes sequentially in a cluster).

**Difficulty:** Base
**Category:** Dev

---

## UPIN — UPIN Authentication Token

Deprecated term for a PIN-based authentication credential used in early mobile
network standards (GSM) to unlock SIM cards and network services. Superseded
by the UICC PIN system in UMTS and LTE where PIN authentication gates access
to the SIM's cryptographic identity before network registration.

**Difficulty:** Advanced
**Category:** Security

---

## UPDT — Update Manager

Generic component in OS and application ecosystems responsible for fetching,
verifying, and applying software updates. On Linux: APT (Debian/Ubuntu), DNF
(Fedora/RHEL), zypper (SUSE). Verifies package signatures against distribution
keys before installation to prevent tampering.

**Difficulty:** Base
**Category:** OS

---

## UPRB — Uprobe (Userspace Probe)

Linux kernel mechanism for dynamic tracing of user-space functions without
modifying the binary. `uprobes` insert software breakpoints into the target process
at specified function offsets; BPF programs attached to the probe execute on
each trigger. Used to trace application behavior in production with minimal overhead.

**Difficulty:** Advanced
**Category:** OS

---

## URPF — Unicast Reverse Path Forwarding

Anti-spoofing technique on routers that validates the source IP of incoming packets
by checking whether the return path to that source IP would go back through the
interface the packet arrived on. Drops packets with spoofed source addresses.
Two modes: strict (exact symmetric path) and loose (any valid route exists).

**Difficulty:** Advanced
**Category:** Networking

---

## USET — User Entity

Generic security term for an identity principal representing an individual user
account in an access control system. Distinct from service accounts, machine
accounts, and group entities. In RBAC systems, user entities are assigned to
roles; in ABAC systems, user attributes determine authorization decisions.

**Difficulty:** Intermediate
**Category:** Security

---

## ULPL — User-Level Packet Library

General term for network packet processing libraries operating in user space
rather than the kernel, avoiding system call overhead for packet I/O. Examples:
DPDK (Data Plane Development Kit), libpcap, PF_RING. Critical for high-performance
line-rate packet processing in software routers and security appliances.

**Difficulty:** Advanced
**Category:** Networking

---

## UMEM — Unified Memory

Memory architecture where CPU and GPU share the same physical memory pool with
automatic migration of pages to the processor currently using them. Available
on NVIDIA GPUs (CUDA Unified Memory API) and Apple Silicon (unified memory
architecture). Eliminates explicit host-to-device memory transfers in GPU programming.

**Difficulty:** Advanced
**Category:** Hardware

---

## ULDB — User Lockdown Database

Security component maintaining a record of locked-out user accounts resulting
from repeated authentication failures. Implements account lockout policy (number
of failures, lockout duration) to prevent brute-force attacks. In Linux: managed
via `pam_tally2` or `pam_faillock`; in Active Directory, via account lockout policy.

**Difficulty:** Intermediate
**Category:** Security

---

## UCNF — User Configuration File

Generic term for per-user configuration files stored in the user's home directory.
Convention: files prefixed with `.` (dotfiles) are hidden on Unix/Linux (`.bashrc`,
`.ssh/config`, `.gitconfig`). Dotfile management tools (GNU Stow, chezmoi) synchronize
configurations across multiple machines via a version-controlled repository.

**Difficulty:** Base
**Category:** OS

---

## UPCA — User Provisioning and Configuration Automation

Process of automatically creating, configuring, and maintaining user accounts
across IT systems when personnel changes occur. Triggered by HR system events
(hire, transfer, termination). Implemented via SCIM, LDAP provisioning adapters,
and identity governance platforms (SailPoint, Saviynt).

**Difficulty:** Intermediate
**Category:** Security

---

## UAMS — Unified Access Management System

Platform centralizing authentication, authorization, and audit for all user
access across on-premises and cloud resources. Integrates SSO, MFA, PAM (Privileged
Access Management), and RBAC into a single governance layer. Examples: CyberArk,
Microsoft Entra ID, Okta.

**Difficulty:** Intermediate
**Category:** Security

---

## UTMP — Unix/Linux Login Records File
Binary file (/var/run/utmp on Linux) that tracks currently logged-in users, active terminals, and system boot time. Read by commands such as who, w, and last. Related files: wtmp (historical login records) and btmp (failed login attempts). Format defined in utmp.h.
**Difficulty:** Intermediate
**Category:** OS

---

## UREG — User Register
General-purpose processor register accessible to user-mode code without privilege escalation. Distinguished from kernel registers that are only accessible in ring 0 (x86) or EL1+ (ARM). The number and width of user registers varies by ISA (e.g. 16 in x86-64, 31 in AArch64).
**Difficulty:** Advanced
**Category:** Hardware
