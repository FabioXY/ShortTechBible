## TCP — Transmission Control Protocol

A connection-oriented, reliable, ordered, and error-checked transport protocol (RFC 793) that provides byte-stream delivery between applications. TCP uses a three-way handshake (SYN, SYN-ACK, ACK) to establish connections, sequence numbers and acknowledgments for reliability, sliding windows for flow control, and congestion control algorithms (Reno, CUBIC, BBR) to avoid network saturation.

**Difficulty:** Intermediate
**Category:** Protocol

---

## TDD — Test-Driven Development

A software development methodology where tests are written before the code they test. The cycle is: write a failing test (Red), write the minimum code to pass it (Green), refactor without breaking tests (Refactor). TDD drives API design from the consumer perspective, ensures high coverage by construction, and creates a regression safety net for refactoring.

**Difficulty:** Intermediate
**Category:** Dev

---

## TFTP — Trivial File Transfer Protocol

A simple lockstep file transfer protocol (UDP port 69, RFC 1350) with no authentication, no directory listing, and no encryption. TFTP is used specifically in environments where simplicity is paramount: PXE network booting, router firmware transfers, and embedded device provisioning. Its simplicity makes it feasible to implement in ROM with minimal code.

**Difficulty:** Intermediate
**Category:** Protocol

---

## TLS — Transport Layer Security

A cryptographic protocol (successor to SSL) that provides confidentiality, integrity, and authentication for network communications. TLS operates over TCP (or DTLS over UDP) and uses asymmetric cryptography for key exchange and authentication, then symmetric ciphers for bulk data. TLS 1.3 (RFC 8446) removed weak cipher suites, reduced handshake round-trips to 1-RTT, and mandated forward secrecy.

**Difficulty:** Intermediate
**Category:** Security

---

## TPM — Trusted Platform Module

A dedicated microcontroller (ISO/IEC 11889) embedded in hardware that provides cryptographic functions: secure key generation and storage, attestation (proving hardware/software state), random number generation, and sealed storage (data accessible only in a specific measured system state). TPM 2.0 is required for Windows 11 and underpins BitLocker, secure boot, and remote attestation.

**Difficulty:** Advanced
**Category:** Security

---

## TTL — Time to Live

A counter in IP packet headers (and DNS records) that limits the lifespan of data in a network. In IP, TTL is decremented by 1 at each router hop; when it reaches 0, the packet is discarded and an ICMP "Time Exceeded" is sent back (the mechanism traceroute exploits). In DNS, TTL specifies how long a resolver may cache a record before re-querying the authoritative server.

**Difficulty:** Base
**Category:** Networking

---

## TOTP — Time-based One-Time Password

An algorithm (RFC 6238) that generates a short-lived numeric code using a shared secret and the current Unix timestamp divided into 30-second windows. TOTP is the mechanism behind authenticator apps (Google Authenticator, Authy). The code is computed as HMAC-SHA1(secret, floor(time/30)), then truncated to 6–8 digits.

**Difficulty:** Intermediate
**Category:** Security
