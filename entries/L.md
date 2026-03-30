## LAN — Local Area Network

A network that interconnects devices within a limited geographical area (building, floor, home) using Ethernet (IEEE 802.3) or Wi-Fi (IEEE 802.11). LANs typically operate at Layer 2, with switches forwarding frames by MAC address. Contrast with WAN (wide area) and MAN (metropolitan area). The broadcast domain boundaries are typically defined by VLANs.

**Difficulty:** Base
**Category:** Networking

---

## LACP — Link Aggregation Control Protocol

An IEEE 802.3ad protocol that negotiates and maintains link aggregation (bonding) between two network nodes. LACP dynamically detects compatible partners, forms a logical aggregate link from multiple physical links, and handles failure by redistributing traffic. Provides increased bandwidth and redundancy compared to a single link.

**Difficulty:** Intermediate
**Category:** Networking

---

## LDAP — Lightweight Directory Access Protocol

A protocol (TCP port 389, 636 for LDAPS) for accessing and maintaining distributed directory information services. LDAP directories store hierarchical data in a tree structure (Distinguished Names, Organizational Units, Common Names). Used for centralized authentication, address books, and authorization policies. Active Directory exposes an LDAP interface.

**Difficulty:** Intermediate
**Category:** Protocol

---

## LLDP — Link Layer Discovery Protocol

An IEEE 802.1AB vendor-neutral protocol that allows network devices (switches, routers, phones) to advertise their identity, capabilities, and neighbors to directly connected devices. LLDP frames are multicast and not forwarded by switches. Used by network management systems to auto-discover and map physical topology.

**Difficulty:** Intermediate
**Category:** Networking

---

## LUKS — Linux Unified Key Setup

The standard disk encryption specification for Linux, implemented in the kernel via dm-crypt. LUKS stores all setup information in a partition header, allowing multiple passphrases or key files (up to 8 keyslots per device). LUKS2 (the current version) uses Argon2 for key derivation and adds integrity checking support via dm-integrity.

**Difficulty:** Intermediate
**Category:** Security

---

## LRU — Least Recently Used

A cache eviction policy that discards the item that has not been accessed for the longest time when the cache is full. LRU approximates temporal locality: recently accessed items are more likely to be accessed again. Implemented efficiently with a doubly-linked list and hash map (O(1) get and put). Used in CPU caches, OS page replacement, and application-level caches.

**Difficulty:** Intermediate
**Category:** OS
