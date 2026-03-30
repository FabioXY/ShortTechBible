## HBA — Host Bus Adapter

A hardware component that connects a host system to a storage network or device. In SAN environments, HBAs provide Fibre Channel (FC) or iSCSI connectivity between servers and shared storage arrays. An HBA offloads storage protocol processing from the CPU, similar to how a NIC offloads network processing.

**Difficulty:** Intermediate
**Category:** Hardware

---

## HDD — Hard Disk Drive

A magnetic storage device that stores data on rotating platters coated with a ferromagnetic material. Read/write heads on actuator arms access data as platters spin (typically 5400 or 7200 RPM). HDDs have higher latency than SSDs due to mechanical seek time but offer higher capacity at lower cost per gigabyte. Susceptible to physical shock.

**Difficulty:** Base
**Category:** Hardware

---

## HDMI — High-Definition Multimedia Interface

A proprietary audio/video interface standard that transmits uncompressed digital video and audio over a single cable. HDMI versions (1.4, 2.0, 2.1) differ in maximum bandwidth, supported resolutions, and feature sets (4K, 8K, HDR, eARC). HDMI includes HDCP copy protection and a CEC channel for device control.

**Difficulty:** Base
**Category:** Hardware

---

## HMAC — Hash-based Message Authentication Code

A specific construction for a message authentication code (MAC) that uses a cryptographic hash function (e.g., SHA-256) combined with a secret key. HMAC provides both integrity (the message has not been altered) and authenticity (only the key holder could have produced it). Used in API authentication, JWT signatures (HS256), and TLS.

**Difficulty:** Intermediate
**Category:** Security

---

## HTML — HyperText Markup Language

The standard markup language for web pages. HTML defines the structure and meaning of web content using a hierarchy of elements (tags) such as headings, paragraphs, links, images, and forms. HTML5 added semantic elements, native audio/video support, and APIs for offline storage and drawing (Canvas). Rendered by the browser's layout engine.

**Difficulty:** Base
**Category:** Dev

---

## HSTS — HTTP Strict Transport Security

A web security policy mechanism (RFC 6797) that instructs browsers to only communicate with a server over HTTPS, never HTTP. The server sends the Strict-Transport-Security header with a max-age directive. Once received, the browser enforces HTTPS for all future requests to that origin, preventing SSL stripping attacks even if the user types HTTP.

**Difficulty:** Intermediate
**Category:** Security
