## TFTP — Trivial File Transfer Protocol

Simplified UDP-based file transfer protocol (RFC 1350) using a lock-step
acknowledgment model. No authentication, no directory listing, no security.
Used for network booting (PXE), CISCO IOS image transfers, and loading firmware
to network devices where simplicity and small code footprint matter more than features.

**Difficulty:** Intermediate
**Category:** Protocol

---

## TLS — Transport Layer Security

Cryptographic protocol (RFC 8446 for TLS 1.3) providing authenticated and encrypted
communication over a network. Replaced SSL. TLS 1.3 removes legacy ciphers, mandates
forward secrecy, and achieves 1-RTT handshakes (0-RTT for session resumption).
Used by HTTPS, SMTPS, IMAPS, and virtually every modern secure network service.

**Difficulty:** Intermediate
**Category:** Security

---

## TOTP — Time-based One-Time Password

Algorithm (RFC 6238) generating a one-time passcode using the current time and
a shared secret, producing a new 6-8 digit code every 30 seconds. Based on
HOTP. Used in authenticator apps (Aegis, Google Authenticator). Both parties
must have synchronized clocks within a tolerance window (typically ±1 step).

**Difficulty:** Intermediate
**Category:** Security

---

## TSIG — Transaction Signature

HMAC-based DNS security mechanism (RFC 8945) authenticating DNS messages between
two parties sharing a secret key. Used to secure AXFR/IXFR zone transfers and
dynamic DNS updates (RFC 2136). Prevents unauthorized zone transfers or malicious
DNS record modification without requiring DNSSEC zone signing.

**Difficulty:** Advanced
**Category:** Protocol

---

## TTL — Time to Live

IP packet field decremented by 1 at each router hop; the packet is discarded
when TTL reaches zero, preventing infinite routing loops. Also used in DNS as
the cache duration (in seconds) for a record. Common traceroute technique exploits
TTL expiration to map each hop along a network path.

**Difficulty:** Base
**Category:** Networking

---

## TURN — Traversal Using Relays around NAT

Extension to STUN (RFC 8656) that provides a relay when direct peer-to-peer
communication through NAT is impossible. A TURN server in the public Internet
receives media from one peer and forwards it to the other. Used by WebRTC as
a fallback when STUN and direct connection both fail.

**Difficulty:** Intermediate
**Category:** Protocol

---

## TPUT — Throughput

Actual rate of successful data transfer over a network or storage channel,
measured in bits/bytes per second. Distinct from bandwidth (maximum theoretical
rate). Reduced by protocol overhead, packet loss, retransmissions, and network
congestion. The `iperf3` tool measures TCP/UDP throughput between endpoints.

**Difficulty:** Base
**Category:** Networking

---

## TRAP — SNMP Trap

Unsolicited notification sent by an SNMP agent to a manager when a significant
event occurs, rather than waiting for the manager to poll. Defined in SNMPv1/v2c;
SNMPv2c introduced INFORM (acknowledged trap). Common traps: linkDown, linkUp,
coldStart, authentication failure. Timely alerting requires reliable trap delivery.

**Difficulty:** Intermediate
**Category:** Networking

---

## TCAM — Ternary Content-Addressable Memory

Specialized hardware memory used in network switches and routers for ultra-fast
packet classification. Unlike regular RAM (reads by address), TCAM searches
by content. The ternary aspect means each bit can be 0, 1, or "don't care" (X),
allowing wildcard matching of ACLs and routing rules in a single clock cycle.

**Difficulty:** Advanced
**Category:** Hardware

---

## TMPF — Temporary Filesystem

Linux `tmpfs` virtual filesystem that stores files in RAM and optional swap,
providing fast temporary storage. Mounted by default at `/tmp`, `/run`, and
`/dev/shm`. Files do not survive reboots. Size is dynamically adjustable;
defaults to half of total RAM. Used for fast IPC via shared memory files.

**Difficulty:** Intermediate
**Category:** OS

---

## TPMD — Trusted Platform Module Daemon

Background service managing access to and operations of the TPM hardware security
chip. On Linux: `tpm2-abrmd` (access broker and resource manager) multiplexes
access to the TPM 2.0 chip among multiple processes. Required by `tpm2-tools`
and systemd-measured boot for key operations and attestation.

**Difficulty:** Advanced
**Category:** Security

---

## TFTD — TFTP Daemon

Server process implementing the TFTP protocol on port 69/UDP for serving files
to network clients. Common implementations: `tftpd-hpa` (Linux). Used in PXE
boot infrastructure to serve bootloaders (pxelinux, grubx64.efi), kernel images,
and network device firmware upgrade files.

**Difficulty:** Intermediate
**Category:** OS

---

## TKIP — Temporal Key Integrity Protocol

WPA (Wi-Fi Protected Access) encryption protocol designed as a quick fix for
WEP's severe vulnerabilities while keeping compatibility with older hardware.
Wraps WEP with per-packet key mixing, a message integrity code (Michael MIC),
and replay protection. Now cryptographically broken and removed from WPA3.

**Difficulty:** Intermediate
**Category:** Security

---

## TLDR — Too Long Didn't Read

Internet abbreviation for summarized or condensed versions of long documents.
In IT documentation culture: `tldr-pages` is an open-source project providing
simplified, example-focused man page alternatives. The `tldr` command-line tool
retrieves practical usage examples for common commands from the community-maintained
repository.

**Difficulty:** Base
**Category:** Dev

---

## TOPO — Topology

Physical or logical arrangement of network nodes and connections. Physical topologies:
bus, ring, star, mesh, tree. Logical topologies describe how data flows regardless
of physical layout. Network topology maps are critical for capacity planning,
redundancy analysis, and blast-radius assessment during incidents.

**Difficulty:** Base
**Category:** Networking

---

## TPGW — Transparent Proxy Gateway

Network device intercepting and proxying traffic without client configuration,
inserting itself invisibly between clients and servers. Uses policy routing or
WCCP (Web Cache Communication Protocol) to redirect traffic. Enables content
filtering, caching, and inspection without configuring each client to use the proxy.

**Difficulty:** Intermediate
**Category:** Networking

---

## TRIM — TRIM Command (SSD)

ATA command (analogous to SCSI UNMAP) informing an SSD which data blocks are
no longer in use by the filesystem and can be erased. Without TRIM, the SSD
must erase old data during write operations, degrading performance over time.
Enabled in Linux with `fstrim` or `discard` mount option; critical for SSD longevity.

**Difficulty:** Intermediate
**Category:** Hardware

---

## TSDB — Time Series Database

Database optimized for storing and querying time-indexed data (metrics, sensor
readings, events). Typically compresses adjacent time-series data efficiently
and supports range queries and aggregations over time windows. Examples:
InfluxDB, TimescaleDB (PostgreSQL extension), VictoriaMetrics, Prometheus.

**Difficulty:** Intermediate
**Category:** Database

---

## TUNL — Network Tunnel

Virtual point-to-point link encapsulating one protocol inside another for
transport across an incompatible network. Types: IP-in-IP, GRE, VXLAN, WireGuard,
OpenVPN. On Linux, tunnel interfaces (tun0, vxlan0, gre0) appear as regular
network interfaces configurable with `ip link` and `ip tunnel` commands.

**Difficulty:** Intermediate
**Category:** Networking

---

## TASK — Task Scheduler

OS component or application framework responsible for managing and executing
deferred, periodic, or event-driven work. OS-level: Linux cron, systemd timers,
Windows Task Scheduler. Application-level: Celery (Python), Sidekiq (Ruby),
Quartz (Java). Ensures background jobs run reliably even under high system load.

**Difficulty:** Base
**Category:** OS

---

## TNAM — Tenant Name

Identifier for an isolated logical partition within a multi-tenant cloud platform
or SaaS application. Each tenant has its own namespace, data isolation, and
access control scope. Kubernetes namespaces, AWS accounts, and Azure subscriptions
serve as tenant name boundaries in their respective platforms.

**Difficulty:** Intermediate
**Category:** Cloud

---

## TAPM — Threat and Patch Management

Combined security discipline covering the identification of vulnerabilities
through threat intelligence and CVE tracking, prioritization based on risk scoring
(CVSS, EPSS), and timely application of patches. Measured by mean time to patch
(MTTP) and patching coverage across the asset inventory.

**Difficulty:** Intermediate
**Category:** Security

---

## TLSC — TLS Certificate

X.509 digital certificate used to authenticate a server (or client in mTLS)
during TLS handshakes. Contains the public key, subject name (CN/SAN), issuing
CA, validity period, and digital signature. Certificate transparency logs (RFC 6962)
publicly record all issued certificates, enabling detection of misissued certs.

**Difficulty:** Intermediate
**Category:** Security

---

## TPGP — Trust and Privacy Governance Program

Organizational framework combining data privacy compliance (GDPR, CCPA) with
security trust policies into unified governance. Covers data classification,
consent management, access logging, and third-party risk assessment. Implemented
in enterprise DLP, identity governance, and privacy management platforms.

**Difficulty:** Intermediate
**Category:** Security

---

## TBIT — Test Bit

Single binary flag within a hardware register, protocol field, or network header
used to indicate or test a specific condition. In TCP headers: URG, ACK, PSH,
RST, SYN, FIN flags are individual TBITs. Hardware registers expose TBITs for
status checks that avoid full register reads in tight polling loops.

**Difficulty:** Intermediate
**Category:** Dev

---

## TCPD — TCP Daemon

Historical term for the TCP wrappers program (`tcpd`) that provided host-based
access control for network services before application-level firewalls were
common. Inspects connections to inetd-launched services and allows or denies
based on `/etc/hosts.allow` and `/etc/hosts.deny` rules.

**Difficulty:** Advanced
**Category:** Security

---

## TFHS — Trusted File Hashing System

Security mechanism computing cryptographic hashes (SHA-256, SHA-3) of system
files and storing them in a signed, tamper-evident database. Integrity monitoring
tools (AIDE, Tripwire) detect unauthorized file modifications by comparing
current file hashes against the stored baseline.

**Difficulty:** Advanced
**Category:** Security

---

## TPOL — Traffic Policy

Network QoS configuration defining how different types of traffic are treated
on an interface: rate limiting, prioritization, queuing, and marking (DSCP).
Implemented in routers via policy maps (Cisco) or traffic control rules (`tc`
on Linux). Critical for enforcing SLAs and preventing low-priority traffic from
starving critical applications.

**Difficulty:** Intermediate
**Category:** Networking

---

## TSCL — TLS Certificate Lifecycle

End-to-end process managing TLS certificates from issuance through renewal to
revocation. Lifecycle stages: CSR generation, validation (DV/OV/EV), issuance,
deployment, monitoring expiry, renewal automation (ACME/Let's Encrypt), and
emergency revocation. Automation via `cert-manager` in Kubernetes prevents outages
from expired certificates.

**Difficulty:** Intermediate
**Category:** Security

---

## TCPW — TCP Window

Sliding window size advertised by the TCP receiver indicating how much data it
can accept before requiring an acknowledgment. Window scaling (RFC 7323) extends
the 16-bit field to allow windows larger than 65535 bytes, essential for high-bandwidth,
high-latency links. Small windows bottleneck throughput on long-fat network paths.

**Difficulty:** Advanced
**Category:** Networking

---

## TELF — ELF Binary Format (Testing)

Wait, TELF is not standard. Replacing with: ## TRNG — True Random Number Generator Hardware device generating random numbers from genuinely unpredictable physical phenomena: thermal noise, radioactive decay, photon shot noise, or hardware jitter measurements. Unlike PRNGs, TRNGs are not deterministic. Most modern CPUs include a TRNG accessible via the `RDRAND`/`RDSEED` instructions on x86 or `/dev/hwrng` on Linux.

**Difficulty:** Advanced
**Category:** Hardware

---

## TLOG — Transaction Log

Sequential record of all changes applied to a database, written before committing
changes to data files (write-ahead logging). Used for crash recovery (replaying
the log restores data consistency), point-in-time recovery, and replication
(streaming the log to standby servers). PostgreSQL calls it WAL; MySQL calls it
the binary log (binlog).

**Difficulty:** Advanced
**Category:** Database

---

## TNML — Terminal Node Markup Language

Wait, TNML is not standard. Replacing with: ## TPDK — DPDK (Data Plane Development Kit) — T context Not valid. Replacing with: ## TTFB — Time to First Byte Web performance metric measuring the time from a client's HTTP request to the first byte of the response body being received. Includes DNS resolution, TCP handshake, TLS negotiation, server processing, and network transfer time for the initial byte. A key indicator of server-side responsiveness and network latency in web application performance monitoring.

**Difficulty:** Intermediate
**Category:** Networking

---

## TWIN — Time-Wait State (Network)

TCP connection state where a socket remains after the active close side sends
the final ACK, waiting 2×MSL (Maximum Segment Lifetime, typically 60-120 seconds)
to ensure the remote end received the ACK and to prevent delayed packets from
a closed connection from confusing a new connection reusing the same port tuple.

**Difficulty:** Advanced
**Category:** Networking

---

## TPDU — Transport Protocol Data Unit
The unit of data exchanged between transport layer entities. In OSI terminology, a TPDU includes the transport header plus the data payload passed up from the session layer. Used in X.224/ISO 8073 connection-oriented transport and referenced in SCTP and TCP protocol analysis.
**Difficulty:** Advanced
**Category:** Protocol

---

## TRIB — Tributary
A lower-rate signal component multiplexed into a higher-rate transmission stream in SDH/SONET and OTN hierarchies. For example, multiple T1 tributaries are combined into a T3 signal. The term is also used in optical transport to describe sub-channels within an OTU frame.
**Difficulty:** Advanced
**Category:** Networking

---

## TGID — Thread Group ID
Linux kernel identifier shared by all threads belonging to the same process. The TGID equals the PID of the process's main thread. Visible in /proc/<pid>/status as Tgid. System calls like kill() target TGIDs; getpid() returns TGID while gettid() returns the per-thread PID. Essential for understanding Linux thread/process model.
**Difficulty:** Advanced
**Category:** OS

---

## TNLS — Transport Network Layer Security
Security framework applied at the transport/network layer boundary in carrier and enterprise networks. Refers to encrypting traffic at OSI layer 3-4 using MACsec (layer 2), IPsec (layer 3), or DTLS (layer 4) rather than relying on application-layer TLS. Used in carrier Ethernet and SD-WAN deployments.
**Difficulty:** Advanced
**Category:** Security
