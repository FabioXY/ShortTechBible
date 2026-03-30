## BGP — Border Gateway Protocol

The routing protocol that drives the global internet. BGP exchanges reachability information between autonomous systems using TCP port 179. It is a path-vector protocol: each route advertisement carries the full AS path, enabling loop detection and policy-based routing. Misconfigurations can cause large-scale internet outages (route leaks, hijacks).

**Difficulty:** Advanced
**Category:** Networking

---

## BFD — Bidirectional Forwarding Detection

A lightweight, protocol-agnostic hello mechanism designed to detect link failures in milliseconds rather than the seconds required by BGP/OSPF hold timers. BFD runs between two network nodes and notifies the upper-layer routing protocol when the path goes down, enabling sub-second convergence.

**Difficulty:** Advanced
**Category:** Networking

---

## BSD — Berkeley Software Distribution

A Unix derivative developed at UC Berkeley from the late 1970s onward. BSD introduced many foundational networking concepts including the BSD socket API and the TCP/IP stack later adopted by virtually all operating systems. Modern descendants include FreeBSD, OpenBSD, NetBSD, and macOS (which uses a BSD-derived kernel called XNU).

**Difficulty:** Intermediate
**Category:** OS

---

## BLE — Bluetooth Low Energy

A wireless personal area network technology introduced in Bluetooth 4.0, optimized for low power consumption at the cost of throughput. BLE operates in the 2.4 GHz ISM band and uses a different channel/packet structure than Classic Bluetooth. It is the foundation for IoT sensors, wearables, and proximity-based services (beacons).

**Difficulty:** Intermediate
**Category:** Networking

---

## BIOS — Basic Input/Output System

Firmware stored in a chip on the motherboard that initializes hardware (POST), locates a bootable device, and hands control to the bootloader. BIOS uses a 16-bit real-mode interface and is limited to MBR-based booting from disks under 2 TB. Largely replaced by UEFI on modern systems, though the term is still widely used colloquially.

**Difficulty:** Base
**Category:** Hardware

---

## BLOB — Binary Large Object

A data type in databases and storage systems used to store arbitrary binary data (images, video, compiled code, encrypted files) as a single opaque unit. BLOBs are typically stored outside the main table rows (in an overflow segment or separate object store) because their size is unpredictable and often large.

**Difficulty:** Base
**Category:** Database
