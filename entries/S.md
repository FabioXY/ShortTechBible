## SAML — Security Assertion Markup Language

An XML-based open standard for exchanging authentication and authorization data between an identity provider (IdP) and a service provider (SP). SAML 2.0 is the dominant SSO protocol in enterprise environments, allowing users to authenticate once with the IdP and access multiple SPs without re-entering credentials. Used by Okta, Azure AD, and ADFS.

**Difficulty:** Advanced
**Category:** Security

---

## SCSI — Small Computer System Interface

A set of standards for physically connecting and transferring data between computers and peripheral devices (originally HDDs, scanners, tape drives). SCSI defines a command set that persists in modern storage: SAS (Serial Attached SCSI), iSCSI (SCSI over IP), and NVMe share SCSI command-layer heritage. The SCSI command set underpins enterprise storage communication globally.

**Difficulty:** Intermediate
**Category:** Hardware

---

## SDK — Software Development Kit

A collection of tools, libraries, documentation, APIs, sample code, and build utilities that allow developers to build applications for a specific platform, framework, or service. SDKs abstract low-level details and provide idiomatic interfaces. Examples: Android SDK, AWS SDK, iOS SDK. Contrast with an API (just the interface) — an SDK includes the implementation.

**Difficulty:** Base
**Category:** Dev

---

## SMTP — Simple Mail Transfer Protocol

The standard protocol (TCP port 25, 587 for submission, 465 for SMTPS) for sending email between mail servers and from clients to servers. SMTP is a push protocol: the sender initiates the connection. Modern SMTP requires STARTTLS or implicit TLS, SASL authentication, and SPF/DKIM/DMARC records for deliverability. Receiving mail uses IMAP or POP3.

**Difficulty:** Intermediate
**Category:** Protocol

---

## SNMP — Simple Network Management Protocol

A UDP-based protocol (ports 161/162) for monitoring and managing network devices (routers, switches, servers, printers). SNMP uses a manager/agent model: agents expose a Management Information Base (MIB) of OIDs; the manager polls (GET) or receives unsolicited alerts (TRAP). SNMPv3 adds authentication and encryption; v1/v2c send community strings in plaintext.

**Difficulty:** Intermediate
**Category:** Networking

---

## SSH — Secure Shell

A cryptographic network protocol (TCP port 22, RFC 4251–4254) providing secure remote login, command execution, port forwarding, and file transfer (SCP, SFTP) over an unsecured network. SSH uses asymmetric cryptography for authentication (public/private key pairs) and symmetric encryption for the session. It replaced Telnet, rsh, and rlogin.

**Difficulty:** Base
**Category:** Security

---

## SSD — Solid-State Drive

A storage device that uses NAND flash memory chips instead of spinning magnetic platters. SSDs have no moving parts, giving them lower latency (microseconds vs. milliseconds), higher IOPS, lower power consumption, and greater shock resistance than HDDs. NVMe SSDs connect via PCIe, bypassing the AHCI protocol overhead; SATA SSDs use the legacy interface.

**Difficulty:** Base
**Category:** Hardware
