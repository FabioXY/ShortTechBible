## FAT — File Allocation Table

A file system architecture developed by Microsoft in 1977. FAT uses a table indexed by cluster number to track which clusters belong to which files and which are free. Variants (FAT12, FAT16, FAT32) differ in table entry width, limiting maximum volume and file sizes. exFAT is a modern successor used on flash media due to no file-size limit and simpler structure.

**Difficulty:** Intermediate
**Category:** OS

---

## FIFO — First In, First Out

A data structure and scheduling discipline where the first element added is the first to be removed, analogous to a queue. In OS contexts, FIFO refers to named pipes (mkfifo), process scheduling (tasks run in arrival order), and I/O queues. Contrast with LIFO (stack) and priority queues.

**Difficulty:** Base
**Category:** OS

---

## FQDN — Fully Qualified Domain Name

A domain name that specifies the complete path from the root of the DNS hierarchy, unambiguously identifying a host. An FQDN includes the hostname, all domain labels, and the trailing dot representing the root zone (e.g., mail.example.com.). The trailing dot is often omitted in practice but is required for technical correctness in DNS zone files.

**Difficulty:** Intermediate
**Category:** Networking

---

## FTP — File Transfer Protocol

A standard network protocol (TCP ports 20/21) for transferring files between a client and server. FTP has two modes: active (server initiates data connection back to client) and passive (client initiates both connections). FTP transmits credentials in plaintext; it has been superseded by SFTP (SSH-based) and FTPS (TLS-wrapped) for secure transfers.

**Difficulty:** Base
**Category:** Protocol

---

## FPU — Floating-Point Unit

A specialized component of a CPU (or coprocessor) that handles arithmetic operations on floating-point numbers according to the IEEE 754 standard. FPUs implement operations like addition, multiplication, division, and square root on 32-bit (single) and 64-bit (double) precision numbers with hardware-accelerated rounding and exception handling.

**Difficulty:** Intermediate
**Category:** Hardware

---

## FTPS — File Transfer Protocol Secure

An extension of FTP that adds support for TLS encryption. FTPS has two modes: explicit (FTPES), where the client upgrades to TLS after connecting, and implicit, where TLS is negotiated immediately on a separate port (990). Not to be confused with SFTP, which is a completely different protocol running over SSH.

**Difficulty:** Intermediate
**Category:** Security
