## DDL — Data Definition Language

The subset of SQL used to define and modify database schema: CREATE, ALTER, DROP, TRUNCATE, and RENAME. DDL statements modify the data dictionary (catalog) and are auto-committed in most RDBMS implementations, meaning they cannot be rolled back. Contrast with DML (data manipulation) and DCL (data control).

**Difficulty:** Base
**Category:** Database

---

## DHCP — Dynamic Host Configuration Protocol

A network management protocol (UDP ports 67/68) that automatically assigns IP addresses, subnet masks, default gateways, DNS servers, and other parameters to hosts on a network. The exchange follows a four-step process: Discover → Offer → Request → Acknowledge (DORA). Leases are time-limited; clients must renew before expiry.

**Difficulty:** Base
**Category:** Networking

---

## DKIM — DomainKeys Identified Mail

An email authentication method that lets a domain owner cryptographically sign outgoing messages. The sending mail server attaches a signature header derived from a private key; the recipient's server retrieves the public key from DNS (via a TXT record) and verifies the signature. DKIM protects against message tampering and is required for effective DMARC enforcement.

**Difficulty:** Intermediate
**Category:** Security

---

## DMA — Direct Memory Access

A capability that allows hardware peripherals (NIC, GPU, storage controller) to read/write main memory directly without involving the CPU for each byte. The CPU sets up a DMA transfer (source, destination, size), then the DMA controller handles the actual data movement, freeing the CPU to do other work. Critical for high-throughput I/O.

**Difficulty:** Intermediate
**Category:** Hardware

---

## DNS — Domain Name System

A hierarchical, distributed database that maps human-readable domain names to IP addresses (and vice versa) and stores other records (MX, TXT, CNAME, NS). Queries traverse a resolver → root server → TLD server → authoritative server chain. DNS operates over UDP/TCP port 53 and is fundamental to virtually every internet service.

**Difficulty:** Base
**Category:** Networking

---

## DRAM — Dynamic Random-Access Memory

The most common type of RAM used as main memory in computers. DRAM stores each bit in a capacitor that leaks charge and must be refreshed thousands of times per second (hence "dynamic"). It is denser and cheaper than SRAM but slower due to refresh cycles. Modern variants include DDR4 and DDR5.

**Difficulty:** Intermediate
**Category:** Hardware
