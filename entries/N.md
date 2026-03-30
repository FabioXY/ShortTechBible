## NAT — Network Address Translation

A method of remapping one IP address space to another by modifying IP header information in transit. Most commonly used to allow multiple devices on a private network (RFC 1918 addresses) to share a single public IP. NAT breaks the end-to-end connectivity model of the internet and complicates protocols that embed IP addresses in payloads (FTP, SIP).

**Difficulty:** Intermediate
**Category:** Networking

---

## NFS — Network File System

A distributed file system protocol (originally developed by Sun Microsystems, RFC 7530 for NFSv4) that allows a client to mount and access remote file systems over a network as if they were local. NFS uses RPC/XDR for communication. NFSv4 added stateful operations, strong authentication (Kerberos), and compound operations to reduce round-trips.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NIC — Network Interface Card

A hardware component that provides a device with network connectivity. A NIC implements the physical and data link layers: it converts data to electrical/optical signals (or radio waves for Wi-Fi) and handles MAC addressing, framing, and error detection. Modern NICs support offloading functions like checksums, TSO, and RSS from the CPU.

**Difficulty:** Base
**Category:** Hardware

---

## NTFS — New Technology File System

The proprietary journaling file system developed by Microsoft and used by default in Windows NT and all subsequent Windows versions. NTFS supports file permissions (ACLs), journaling (for crash recovery), file compression, encryption (EFS), alternate data streams, hard/symbolic links, and volumes larger than 2 TB. The MFT (Master File Table) is the core metadata structure.

**Difficulty:** Intermediate
**Category:** OS

---

## NTP — Network Time Protocol

A networking protocol (UDP port 123, RFC 5905) for clock synchronization between computer systems over packet-switched networks. NTP uses a hierarchical structure of time sources (strata): stratum 0 is an atomic clock or GPS receiver; stratum 1 servers sync directly to it; clients typically sync to stratum 2 or 3 servers. Accurate time is critical for logs, certificates, and distributed systems.

**Difficulty:** Intermediate
**Category:** Protocol

---

## NUMA — Non-Uniform Memory Access

A memory design used in multi-processor systems where memory access time depends on the physical location of memory relative to the processor. Each CPU has local memory (fast) and can access remote memory (attached to another CPU socket) via an interconnect (slower). OS schedulers and applications must be NUMA-aware to avoid performance penalties from remote memory access.

**Difficulty:** Advanced
**Category:** Hardware
