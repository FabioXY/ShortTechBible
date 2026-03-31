## CAP — Consistency, Availability, Partition tolerance

A theorem formulated by Eric Brewer stating that a distributed system can guarantee at most two of three properties simultaneously: Consistency (every read receives the most recent write), Availability (every request receives a non-error response), and Partition tolerance (the system continues operating despite network partitions). Real distributed systems must handle partitions, so the real trade-off is C vs A.

**Difficulty:** Advanced
**Category:** Database

---

## CDN — Content Delivery Network

A geographically distributed network of proxy servers and data centers that serves content to users from the node closest to them. CDNs cache static assets (images, JS, CSS, video), reducing origin server load and latency. They also provide DDoS mitigation and TLS termination at the edge.

**Difficulty:** Intermediate
**Category:** Cloud

---

## CGI — Common Gateway Interface

A specification (RFC 3875) for how web servers execute external programs to generate dynamic content. When a request matches a CGI script path, the server spawns the script as a process, passes request data via environment variables and stdin, and returns the script's stdout as the HTTP response. CGI has largely been replaced by FastCGI, WSGI, and application servers.

**Difficulty:** Intermediate
**Category:** Dev

---

## CID — Content Identifier

A self-describing, content-addressed label used in distributed systems (especially IPFS) to uniquely reference data by its cryptographic hash rather than its location. A CID encodes the hash function used (SHA-256, BLAKE2), the codec (DAG-PB, CBOR), and the hash digest. The same content always produces the same CID regardless of where it is stored.

**Difficulty:** Advanced
**Category:** Dev

---

## CIDR — Classless Inter-Domain Routing

A method for allocating IP addresses and routing that replaced the rigid Class A/B/C system. CIDR notation expresses a network as an IP address followed by a prefix length (e.g., 192.168.1.0/24). This allows arbitrary-sized allocations, reducing IP address waste and enabling route aggregation (supernetting) on the internet.

**Difficulty:** Intermediate
**Category:** Networking

---

## CIFS — Common Internet File System

Microsoft's implementation and extension of the SMB protocol, providing shared access to files, printers, and serial ports over a network. CIFS added features to SMB such as opportunistic locking (oplocks), Unicode support, and larger file size support. The term "CIFS" is now often used interchangeably with SMB, though technically CIFS refers to the dialect released with Windows 2000.

**Difficulty:** Intermediate
**Category:** Protocol

---

## CLI — Command-Line Interface

A text-based interface where users interact with a program by typing commands. Unlike GUIs, CLIs are scriptable, composable via pipes, and reproducible. Every serious infrastructure tool (git, kubectl, docker, openssl) exposes a CLI because it enables automation, logging, and integration into CI/CD pipelines.

**Difficulty:** Base
**Category:** OS

---

## CMS — Content Management System

A software platform that enables users to create, manage, and publish digital content without requiring direct code editing. CMS platforms like WordPress, Drupal, and Contentful abstract the database and templating layers. Headless CMS architectures decouple the content backend from the presentation frontend, serving content via API.

**Difficulty:** Base
**Category:** Dev

---

## COM — Component Object Model

A binary interface standard developed by Microsoft (1993) that enables inter-process communication and dynamic object creation in a language-neutral way. COM objects expose interfaces (collections of function pointers) identified by GUIDs. COM is the foundation of OLE, ActiveX, DirectX, and the Windows Shell. The distributed variant is DCOM; the .NET successor is CCW/RCW interop.

**Difficulty:** Advanced
**Category:** Dev

---

## COW — Copy-On-Write

A resource management strategy where multiple callers sharing the same resource each get a reference to the same data; a private copy is made only when one caller attempts to modify it. COW is used in process forking (Linux fork()), file system snapshots (ZFS, APFS, Btrfs), virtual machine disk images (QCOW2), and string handling in some programming languages.

**Difficulty:** Intermediate
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

## CORS — Cross-Origin Resource Sharing

A browser security mechanism that controls how web pages can request resources from a different origin (domain, protocol, or port). The browser sends a preflight OPTIONS request; the server responds with headers (Access-Control-Allow-Origin, etc.) indicating whether the cross-origin request is permitted. Misconfiguration is a common web security vulnerability.

**Difficulty:** Intermediate
**Category:** Security

---

## CSP — Content Security Policy

An HTTP response header (and meta tag) that instructs browsers which sources of scripts, styles, images, and other content are allowed to load. CSP mitigates XSS by preventing the browser from executing inline scripts or loading resources from unauthorized origins. Policies are expressed as directives: script-src, img-src, connect-src, etc.

**Difficulty:** Intermediate
**Category:** Security

---

## CSRF — Cross-Site Request Forgery

An attack that tricks an authenticated user's browser into sending unintended requests to a web application where the user is logged in. The attacker exploits the fact that browsers automatically attach cookies. Mitigated by CSRF tokens (random secret values per session) and the SameSite cookie attribute.

**Difficulty:** Intermediate
**Category:** Security

---

## CSS — Cascading Style Sheets

A style sheet language used to describe the presentation of HTML documents: layout, colors, typography, spacing, and responsive behavior. CSS uses a cascade (specificity + source order) to resolve conflicts when multiple rules apply to the same element. CSS3 introduced flexbox, grid, custom properties (variables), and animations.

**Difficulty:** Base
**Category:** Dev

---

## CTF — Capture The Flag

A cybersecurity competition format where participants solve security challenges to find hidden strings ("flags") worth points. CTF challenges cover binary exploitation, reverse engineering, web security, cryptography, forensics, and network analysis. CTFs are used for training, recruitment, and skill assessment in the security community.

**Difficulty:** Intermediate
**Category:** Security

---

## CVE — Common Vulnerabilities and Exposures

A standardized dictionary of publicly disclosed cybersecurity vulnerabilities, maintained by MITRE and funded by the US government. Each CVE entry has a unique identifier (CVE-YYYY-NNNNN), a description, and references. CVSS scores (0–10) quantify severity. Vendors, SIEMs, and patch management tools use CVE IDs to correlate vulnerability data across sources.

**Difficulty:** Intermediate
**Category:** Security

---

## CVSS — Common Vulnerability Scoring System

A framework for rating the severity of software vulnerabilities on a scale of 0.0 to 10.0. CVSS v3.1 uses a Base Score (attack vector, complexity, privileges required, user interaction, confidentiality/integrity/availability impact), Temporal Score (exploit maturity, patch availability), and Environmental Score (organizational context). Maintained by FIRST.

**Difficulty:** Intermediate
**Category:** Security

---

## CNAME — Canonical Name (DNS record)

A DNS record that maps an alias domain name to the true (canonical) domain name. When a resolver encounters a CNAME, it follows the chain until reaching an A or AAAA record. CNAMEs enable flexible pointing of multiple names to one host and are used for CDN integration, load balancers, and service aliasing. A CNAME cannot coexist with other records at the zone apex.

**Difficulty:** Intermediate
**Category:** Networking

---

## CRL — Certificate Revocation List

A time-stamped list signed by a Certificate Authority containing the serial numbers of certificates that have been revoked before their expiry date. Clients download CRLs to check if a presented certificate is still valid. CRLs can grow large and have high latency; OCSP was introduced as a more efficient alternative. CRL distribution points are embedded in certificates.

**Difficulty:** Advanced
**Category:** Security

---

## CSR — Certificate Signing Request

A block of encoded text sent to a Certificate Authority to request a digital certificate. A CSR contains the public key, organizational information (CN, O, OU, C), and is signed with the private key to prove ownership. The CA verifies the CSR, signs it with its own private key, and returns an X.509 certificate. Generated with tools like openssl req.

**Difficulty:** Intermediate
**Category:** Security

---

## CLI — Command Line Interface

See CLI entry. Canonical reference.

**Difficulty:** Base
**Category:** OS

---

## CRUD — Create, Read, Update, Delete

The four basic operations of persistent storage, forming the foundation of most data-driven applications. CRUD maps to SQL (INSERT, SELECT, UPDATE, DELETE), HTTP methods (POST, GET, PUT/PATCH, DELETE), and REST resource semantics. A "CRUD application" refers to any app whose primary function is managing data through these four operations.

**Difficulty:** Base
**Category:** Database

---

## CTR — Counter Mode (encryption)

A block cipher mode of operation that turns a block cipher into a stream cipher by encrypting successive values of a counter and XORing the output with plaintext. CTR mode is parallelizable (unlike CBC), requires no padding, and supports random access to encrypted data. Used in AES-CTR, which is the basis for AES-GCM when combined with GHASH authentication.

**Difficulty:** Advanced
**Category:** Security

---

## CAS — Compare-And-Swap

An atomic CPU instruction that compares the contents of a memory location to a given value, and only if they match, replaces it with a new value. CAS is the foundation of lock-free data structures and synchronization primitives in concurrent programming. It is implemented as CMPXCHG on x86 and LDREX/STREX on ARM.

**Difficulty:** Advanced
**Category:** Hardware

---

## CDR — Call Detail Record

A data record produced by a telephone exchange or PBX that documents the details of a telephone call: originating number, destination number, start time, duration, and call outcome. CDRs are used for billing, fraud detection, and capacity planning in VoIP and traditional telephony systems.

**Difficulty:** Intermediate
**Category:** Networking

---

## CAN — Controller Area Network

A robust serial communication bus standard (ISO 11898) designed for microcontrollers and devices to communicate without a host computer, particularly in automotive, industrial, and embedded environments. CAN supports multi-master operation, message-based addressing, built-in error detection (CRC, bit stuffing), and automatic retransmission.

**Difficulty:** Advanced
**Category:** Protocol

---

## CAM — Content-Addressable Memory

A special type of memory that searches its entire contents in parallel for a given data pattern and returns the address where the data is found, rather than requiring the caller to specify an address. CAM is used in CPU TLBs, network switches (for MAC address and routing table lookups), and firewalls for high-speed table searches.

**Difficulty:** Advanced
**Category:** Hardware

---

## CFG — Control Flow Graph

A directed graph representation of a program where each node is a basic block (a sequence of instructions with no branches) and edges represent possible control flow transfers (jumps, branches, calls). CFGs are used by compilers for optimization, by static analysis tools for vulnerability detection, and by binary analysis frameworks for reverse engineering.

**Difficulty:** Advanced
**Category:** Dev

---

## CDW — Cloud Data Warehouse

A managed analytics database service in the cloud optimized for large-scale OLAP workloads. CDWs (Snowflake, BigQuery, Redshift) separate compute from storage, allowing independent scaling. They support columnar storage, massively parallel processing (MPP), and semi-structured data formats like JSON and Parquet natively.

**Difficulty:** Intermediate
**Category:** Cloud

---

## CIM — Common Information Model

An open standard by DMTF that defines how managed elements in an IT environment (hardware, software, networks) are represented and how management data is exchanged. CIM provides the conceptual foundation for WBEM and is used by systems management tools, including those in VMware, Microsoft (WMI), and SNIA storage management.

**Difficulty:** Advanced
**Category:** Protocol
