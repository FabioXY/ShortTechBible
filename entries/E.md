## EAP — Extensible Authentication Protocol

A framework (not a protocol itself) used in wireless and point-to-point connections that supports multiple authentication methods: certificates, tokens, passwords, SIM cards. EAP runs over 802.1X in Wi-Fi networks, with the access point acting as an authenticator passing EAP messages between the supplicant and a RADIUS server.

**Difficulty:** Advanced
**Category:** Security

---

## ECC — Error-Correcting Code (memory)

A type of computer data storage that detects and corrects common types of internal data corruption. ECC memory uses extra bits (typically adding 8 bits per 64-bit word) to detect and correct single-bit errors, and detect double-bit errors. Required in servers, workstations, and any environment where silent data corruption is unacceptable.

**Difficulty:** Intermediate
**Category:** Hardware

---

## EOF — End of File

A condition or marker indicating that no more data can be read from a data source (file, stream, socket). In Unix-like systems, EOF is not a character in the file; it is a condition returned by read() when the file position reaches the end. On a terminal, Ctrl+D sends EOF. In binary protocols, explicit length fields are preferred to EOF-detection.

**Difficulty:** Base
**Category:** OS

---

## ETL — Extract, Transform, Load

A data integration process that pulls data from one or more sources (Extract), applies cleaning, normalization, and business logic (Transform), and writes it to a target system such as a data warehouse (Load). ETL pipelines are the backbone of data engineering and BI systems. Modern variants include ELT (transform after load) for cloud data warehouses.

**Difficulty:** Intermediate
**Category:** Database

---

## ESB — Enterprise Service Bus

A middleware architecture pattern that provides a centralized communication layer between heterogeneous services and applications in an enterprise. The ESB handles message routing, transformation, protocol mediation, and orchestration. Largely replaced by microservices architectures and lightweight message brokers (Kafka, RabbitMQ) in modern stacks.

**Difficulty:** Advanced
**Category:** Dev

---

## ECDH — Elliptic-Curve Diffie–Hellman

A key agreement protocol that allows two parties to establish a shared secret over an insecure channel using elliptic-curve cryptography. ECDH provides the same security as classical Diffie–Hellman with much smaller key sizes, making it efficient for TLS handshakes. The ephemeral variant (ECDHE) provides forward secrecy.

**Difficulty:** Advanced
**Category:** Security
