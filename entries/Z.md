## ZFS — Z File System

An advanced combined file system and logical volume manager developed by Sun Microsystems and open-sourced under CDDL. ZFS provides end-to-end checksums on all data and metadata (silent corruption detection), copy-on-write transactional semantics, snapshots and clones, RAID-Z (software RAID with variable parity), inline compression, and deduplication. The ARC (Adaptive Replacement Cache) manages read caching in RAM.

**Difficulty:** Advanced
**Category:** OS

---

## ZIP — ZIP archive format

A lossless data compression and archiving format created by Phil Katz (1989). Unlike gzip, ZIP archives can contain multiple files, each independently compressed (using DEFLATE by default). The central directory at the end of the archive allows random access to individual files without reading the whole archive. Supported natively by all major operating systems.

**Difficulty:** Base
**Category:** OS

---

## ZTP — Zero-Touch Provisioning

An automated device provisioning process that configures network equipment (switches, routers, access points) without manual intervention. On first boot, the device contacts a DHCP server for an IP and the location of a configuration script or file, downloads it, and applies the full configuration automatically. ZTP eliminates manual on-site configuration for large-scale deployments.

**Difficulty:** Intermediate
**Category:** Networking

---

## ZRAM — Zram (compressed RAM block device)

A Linux kernel module that creates compressed block devices in RAM, used as a swap device or tmpfs backing store. Instead of swapping to disk, compressed pages are stored in ZRAM, trading CPU cycles (compression/decompression) for dramatically reduced I/O. Used by Android, ChromeOS, and low-RAM Linux systems to extend effective memory at minimal latency cost.

**Difficulty:** Intermediate
**Category:** OS

---

## ZTNA — Zero Trust Network Access

A security model and product category that replaces VPN-based remote access by applying least-privilege, identity-aware access controls to every application request, regardless of network location. ZTNA assumes no implicit trust based on network location; every access request must be verified against identity, device posture, and context. Implemented by products like Cloudflare Access, Zscaler ZPA, and Tailscale.

**Difficulty:** Advanced
**Category:** Security

---

## ZXDB — Zabbix External Database (unofficial abbreviation)

An unofficial shorthand used in Zabbix monitoring deployments referring to configurations where Zabbix stores its monitoring data in an externally managed database server (MySQL, PostgreSQL, TimescaleDB) rather than on the same host. Not an official acronym in the Zabbix documentation, but frequently used in community forums and deployment guides to distinguish single-node from distributed setups.

**Difficulty:** Intermediate
**Category:** Database
