## IANA — Internet Assigned Numbers Authority

The organization responsible for coordinating the global pool of IP addresses, ASNs, DNS root zone management, and protocol parameter registries (port numbers, protocol types, MIME types). IANA is operated by ICANN. Regional registries (ARIN, RIPE, APNIC, etc.) receive address blocks from IANA and distribute them to ISPs and organizations.

**Difficulty:** Intermediate
**Category:** Networking

---

## ICMP — Internet Control Message Protocol

A Layer 3 protocol used by network devices to send operational information and error messages. ICMP is not used to transport application data; it carries diagnostics: echo request/reply (ping), destination unreachable, time exceeded (used by traceroute), and redirect messages. ICMPv6 also handles Neighbor Discovery, replacing ARP in IPv6 networks.

**Difficulty:** Intermediate
**Category:** Networking

---

## IMAP — Internet Message Access Protocol

An email retrieval protocol (TCP port 143, 993 for TLS) that keeps messages on the mail server and synchronizes state (read, deleted, flagged) across multiple clients. Unlike POP3, which downloads and deletes messages, IMAP supports folders, server-side search, and partial message fetch. The dominant protocol for email clients connecting to hosted mailboxes.

**Difficulty:** Base
**Category:** Protocol

---

## IPMI — Intelligent Platform Management Interface

A standardized hardware management interface embedded in server motherboards (via a Baseboard Management Controller, BMC) that allows out-of-band management independent of the main CPU and OS. IPMI provides remote power control, console access (SOL), sensor monitoring (temperature, voltage, fan speed), and event logging via a dedicated network interface.

**Difficulty:** Advanced
**Category:** Hardware

---

## IPV4 — Internet Protocol version 4

The fourth version of the Internet Protocol, using 32-bit addresses written in dotted-decimal notation (e.g., 192.168.1.1), providing approximately 4.3 billion unique addresses. IPv4 defines packet structure, fragmentation, TTL, and addressing. Address exhaustion (mitigated by NAT) drove the development of IPv6. Still the dominant protocol for actual internet traffic.

**Difficulty:** Base
**Category:** Networking

---

## IPV6 — Internet Protocol version 6

The successor to IPv4, using 128-bit addresses (written as eight groups of four hex digits, e.g., 2001:db8::1) to provide a virtually inexhaustible address space. IPv6 eliminates the need for NAT, mandates IPSec support, and introduces Stateless Address Autoconfiguration (SLAAC) and the Neighbor Discovery Protocol as replacements for DHCP and ARP.

**Difficulty:** Intermediate
**Category:** Networking
