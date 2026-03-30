## QOS — Quality of Service

A set of techniques for managing network traffic to ensure predictable performance for specific applications or traffic classes. QoS mechanisms include traffic classification (DSCP marking), policing (dropping excess traffic), shaping (buffering to smooth bursts), and queuing algorithms (FIFO, WFQ, CBWFQ, LLQ). Critical for VoIP, video conferencing, and real-time applications on congested links.

**Difficulty:** Intermediate
**Category:** Networking

---

## QUIC — Quick UDP Internet Connections

A transport layer protocol developed by Google and standardized by the IETF (RFC 9000) that runs over UDP. QUIC combines TLS 1.3 handshake with transport setup (0-RTT or 1-RTT), eliminates head-of-line blocking at the transport layer (unlike TCP), and supports connection migration (survives IP changes). QUIC is the transport layer for HTTP/3.

**Difficulty:** Advanced
**Category:** Protocol

---

## QEMU — Quick Emulator

A free and open-source machine emulator and virtualizer. In emulation mode, QEMU translates guest CPU instructions to host instructions using dynamic binary translation (TCG). In virtualization mode (paired with KVM), guest code runs directly on the host CPU at near-native speed. QEMU provides device emulation (VirtIO, SCSI, USB) for all major hypervisors.

**Difficulty:** Advanced
**Category:** OS

---

## QTLS — QUIC Transport Layer Security

The integration of TLS 1.3 within the QUIC protocol, where TLS is used not as a record layer wrapping transport but as a cryptographic handshake producing keying material for QUIC's own record protection. QTLS eliminates the separate TCP+TLS layering, reducing connection setup latency. Not to be confused with generic TLS running over standard TCP.

**Difficulty:** Advanced
**Category:** Security

---

## QCOW — QEMU Copy On Write (disk image format)

A disk image format used by QEMU/KVM that supports sparse allocation (the file only grows as data is written), snapshots, compression, and AES encryption. QCOW2 (version 2) is the standard format, widely used in Proxmox, libvirt, and OpenStack environments. QCOW2 has lower performance than raw images but is far more flexible for VM management.

**Difficulty:** Intermediate
**Category:** Cloud
