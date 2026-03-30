## RAID — Redundant Array of Independent Disks

A data storage virtualization technology that combines multiple physical drives into one logical unit for redundancy, performance, or both. Common levels: RAID 0 (striping, speed, no redundancy), RAID 1 (mirroring), RAID 5 (striping + distributed parity, tolerates 1 disk failure), RAID 6 (tolerates 2), RAID 10 (striping + mirroring). RAID does not replace backups.

**Difficulty:** Intermediate
**Category:** Hardware

---

## RBAC — Role-Based Access Control

An access control model that assigns permissions to roles rather than directly to users. Users are assigned roles; roles carry permissions. RBAC simplifies administration in large systems: adding a new employee means assigning roles, not configuring hundreds of individual resource permissions. Contrast with ABAC (attribute-based) and DAC (discretionary).

**Difficulty:** Intermediate
**Category:** Security

---

## RAM — Random-Access Memory

Volatile memory that provides the CPU with fast, directly addressable working storage. Unlike sequential storage (tapes) or HDDs, any RAM location can be read or written in constant time regardless of address. RAM loses its contents when power is removed. The term encompasses DRAM (main memory) and SRAM (CPU cache), though colloquially it refers to DRAM.

**Difficulty:** Base
**Category:** Hardware

---

## REST — Representational State Transfer

An architectural style for distributed hypermedia systems, defined by Roy Fielding in his 2000 dissertation. REST constraints include statelessness (no session state on server), uniform interface (resource identification via URI, manipulation via representations), and layered system. RESTful APIs use HTTP methods (GET, POST, PUT, DELETE, PATCH) semantically and return representations (typically JSON or XML).

**Difficulty:** Intermediate
**Category:** Dev

---

## RFC — Request for Comments

The publication format used by the IETF and related organizations to define internet standards, protocols, and best practices. RFCs are numbered sequentially and never modified after publication (corrections are issued as new RFCs). Not all RFCs are standards — they can be Informational, Experimental, or Historic. Key examples: RFC 791 (IP), RFC 793 (TCP), RFC 2616 (HTTP/1.1).

**Difficulty:** Base
**Category:** Protocol

---

## RPC — Remote Procedure Call

A protocol that allows a program to execute a procedure (function) on a remote system as if it were a local call, abstracting the network communication. The caller serializes arguments, sends them to the remote, waits for a result, and deserializes the response. Implementations include gRPC (Google, uses Protocol Buffers over HTTP/2), JSON-RPC, and XML-RPC.

**Difficulty:** Intermediate
**Category:** Dev
