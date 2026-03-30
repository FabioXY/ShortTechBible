## CDN — Content Delivery Network

A geographically distributed network of proxy servers and data centers that serves content to users from the node closest to them. CDNs cache static assets (images, JS, CSS, video), reducing origin server load and latency. They also provide DDoS mitigation and TLS termination at the edge.

**Difficulty:** Intermediate
**Category:** Cloud

---

## CLI — Command-Line Interface

A text-based interface where users interact with a program by typing commands. Unlike GUIs, CLIs are scriptable, composable via pipes, and reproducible. Every serious infrastructure tool (git, kubectl, docker, openssl) exposes a CLI because it enables automation, logging, and integration into CI/CD pipelines.

**Difficulty:** Base
**Category:** OS

---

## CPU — Central Processing Unit

The primary processor of a computer that executes instructions from programs. A CPU fetches instructions from memory, decodes them, and executes them through functional units (ALU, FPU). Modern CPUs contain multiple cores, cache hierarchies (L1/L2/L3), branch predictors, and hardware support for virtualization and encryption.

**Difficulty:** Base
**Category:** Hardware

---

## CRC — Cyclic Redundancy Check

An error-detection algorithm that treats data as a polynomial and computes a remainder when divided by a generator polynomial. The resulting checksum (typically 16 or 32 bits) is appended to data and recomputed on receipt; a mismatch indicates corruption. Used in Ethernet frames, ZIP files, storage protocols, and firmware images.

**Difficulty:** Intermediate
**Category:** Protocol

---

## CIDR — Classless Inter-Domain Routing

A method for allocating IP addresses and routing that replaced the rigid Class A/B/C system. CIDR notation expresses a network as an IP address followed by a prefix length (e.g., 192.168.1.0/24). This allows arbitrary-sized allocations, reducing IP address waste and enabling route aggregation (supernetting) on the internet.

**Difficulty:** Intermediate
**Category:** Networking

---

## CORS — Cross-Origin Resource Sharing

A browser security mechanism that controls how web pages can request resources from a different origin (domain, protocol, or port). The browser sends a preflight OPTIONS request; the server responds with headers (Access-Control-Allow-Origin, etc.) indicating whether the cross-origin request is permitted. Misconfiguration is a common web security vulnerability.

**Difficulty:** Intermediate
**Category:** Security

---

## CSRF — Cross-Site Request Forgery

An attack that tricks an authenticated user's browser into sending unintended requests to a web application where the user is logged in. The attacker exploits the fact that browsers automatically attach cookies. Mitigated by CSRF tokens (random secret values per session) and the SameSite cookie attribute.

**Difficulty:** Intermediate
**Category:** Security
