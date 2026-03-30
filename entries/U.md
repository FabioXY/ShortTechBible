## UART — Universal Asynchronous Receiver-Transmitter

A hardware circuit for serial communication that converts data between parallel (bus) and serial (wire) formats. UART transmits data as a framed bit stream: start bit, data bits (5–9), optional parity bit, stop bit(s). The baud rate must match on both ends. UART is the underlying interface for RS-232, debug consoles, and serial connections on embedded systems and SBCs.

**Difficulty:** Intermediate
**Category:** Hardware

---

## UDP — User Datagram Protocol

A connectionless, unreliable, minimal transport protocol (RFC 768) that sends datagrams with no handshake, no ordering, no retransmission, and no flow control. UDP's simplicity makes it faster than TCP for latency-sensitive applications where occasional packet loss is acceptable: DNS queries, VoIP, video streaming, online games, and QUIC (which builds reliability on top of UDP at the application layer).

**Difficulty:** Intermediate
**Category:** Protocol

---

## UEFI — Unified Extensible Firmware Interface

The modern replacement for BIOS, defined by the UEFI Forum. UEFI runs in 32/64-bit mode (no 16-bit limitation), supports GPT disks (beyond 2 TB), provides a pre-OS execution environment with drivers and a shell, and implements Secure Boot (verifying bootloader signatures against a key database). UEFI applications (bootloaders, diagnostics) reside in the EFI System Partition.

**Difficulty:** Intermediate
**Category:** Hardware

---

## URI — Uniform Resource Identifier

A string that uniquely identifies a resource. URIs are the superset: a URL (Uniform Resource Locator) is a URI that also specifies how to locate the resource (scheme + authority + path), while a URN (Uniform Resource Name) identifies a resource without implying its location. All URLs are URIs; not all URIs are URLs. Defined in RFC 3986.

**Difficulty:** Base
**Category:** Protocol

---

## URL — Uniform Resource Locator

A reference to a web resource that specifies its location on a computer network and the mechanism for retrieving it. A URL consists of: scheme (https://), authority (user:password@host:port), path (/path/to/resource), query (?key=value), and fragment (#section). URL encoding (percent-encoding) escapes characters not allowed in the syntax.

**Difficulty:** Base
**Category:** Protocol

---

## UUID — Universally Unique Identifier

A 128-bit label (RFC 4122) used to uniquely identify information in computer systems without central coordination. UUIDs are formatted as 32 hex digits in 5 groups (e.g., 550e8400-e29b-41d4-a716-446655440000). Version 4 (random) is most common; Version 1 is time+MAC-based; Version 5 is name-based (SHA-1 hash). The probability of collision is negligible in practice.

**Difficulty:** Base
**Category:** Dev
