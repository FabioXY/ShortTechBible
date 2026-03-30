## MAC — Media Access Control (address)

A 48-bit hardware identifier assigned to a network interface at the factory, written as six colon-separated hex octets (e.g., 00:1A:2B:3C:4D:5E). The first three octets identify the vendor (OUI). MAC addresses operate at Layer 2 and are used by switches to forward frames within a network segment. They can be spoofed in software.

**Difficulty:** Base
**Category:** Networking

---

## MBR — Master Boot Record

A 512-byte sector at the very start of a disk (LBA 0) containing the bootstrap code (446 bytes), the partition table (64 bytes, up to 4 primary partitions), and a boot signature (2 bytes: 0x55AA). The BIOS loads and executes the MBR code. MBR is limited to 2 TB disks and 4 primary partitions; GPT replaces it on modern systems.

**Difficulty:** Intermediate
**Category:** OS

---

## MFA — Multi-Factor Authentication

An authentication method that requires the user to present two or more independent factors: something they know (password), something they have (TOTP token, hardware key), and something they are (biometric). MFA drastically reduces the risk of account compromise from credential theft, since an attacker needs all factors simultaneously.

**Difficulty:** Base
**Category:** Security

---

## MIME — Multipurpose Internet Mail Extensions

A standard (RFC 2045–2049) that extends email to support non-ASCII text, attachments, and multipart messages. MIME defines Content-Type headers (e.g., text/html, application/json, image/png) used in both email and HTTP. The Content-Type header is how a browser or mail client knows how to interpret and render a received payload.

**Difficulty:** Intermediate
**Category:** Protocol

---

## MPLS — Multiprotocol Label Switching

A data-forwarding technique that routes traffic using short labels attached to packets rather than long IP prefixes. Routers (Label Switching Routers) swap labels at each hop based on a pre-established Label Switched Path (LSP). MPLS provides traffic engineering, QoS, and VPN services in carrier and enterprise backbone networks with lower per-hop processing overhead.

**Difficulty:** Advanced
**Category:** Networking

---

## MQTT — Message Queuing Telemetry Transport

A lightweight publish/subscribe messaging protocol (ISO/IEC 20922) designed for constrained devices and low-bandwidth, high-latency networks. MQTT clients connect to a broker; publishers push messages to topics; subscribers receive messages on topics they have subscribed to. QoS levels (0, 1, 2) trade off delivery guarantees against overhead. The de facto IoT messaging protocol.

**Difficulty:** Intermediate
**Category:** Protocol

---

## MMU — Memory Management Unit

A hardware component (integrated in modern CPUs) that translates virtual addresses to physical addresses using page tables. The MMU enforces memory protection between processes (preventing one process from accessing another's memory) and enables virtual memory (pages can be swapped to disk). The TLB (Translation Lookaside Buffer) caches recent translations.

**Difficulty:** Advanced
**Category:** Hardware
