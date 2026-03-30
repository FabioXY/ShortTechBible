## PCI — Peripheral Component Interconnect

A local computer bus standard for attaching hardware components to a motherboard. The original parallel PCI (33/66 MHz) was replaced by PCI-X and then by PCIe (PCI Express), which uses serial point-to-point lanes instead of a shared parallel bus. PCIe is the dominant expansion slot for GPUs, NVMe drives, and network cards.

**Difficulty:** Base
**Category:** Hardware

---

## PKI — Public Key Infrastructure

A framework of policies, procedures, hardware, software, and people for creating, managing, distributing, and revoking digital certificates. A PKI relies on a Certificate Authority (CA) hierarchy to sign certificates binding public keys to identities. PKI underpins TLS/HTTPS, code signing, S/MIME email encryption, and smart card authentication.

**Difficulty:** Advanced
**Category:** Security

---

## PHP — PHP Hypertext Preprocessor

A server-side scripting language designed for web development, widely embedded in HTML. PHP scripts execute on the web server and return HTML to the client. Despite criticism for inconsistent API design, PHP powers a significant portion of the web including WordPress, Drupal, and Laravel applications. Modern PHP (8.x) includes strong typing, JIT compilation, and fibers.

**Difficulty:** Base
**Category:** Dev

---

## PXE — Preboot Execution Environment

A specification (Intel/HP) that enables a client to boot from the network before loading a local OS. The client uses DHCP to obtain an IP address and the address of a TFTP server, then downloads a bootloader and kernel. PXE is used for bare-metal provisioning, diskless workstations, and OS deployment systems (Cobbler, iPXE, Windows Deployment Services).

**Difficulty:** Intermediate
**Category:** Networking

---

## PKCS — Public Key Cryptography Standards

A group of cryptography standards developed by RSA Security. Each numbered standard (PKCS#1 through PKCS#15) defines a specific aspect: PKCS#1 (RSA encryption/signatures), PKCS#7/CMS (signed/encrypted data), PKCS#8 (private key info), PKCS#10 (certificate signing requests), PKCS#12 (PFX archives for key+cert bundles). Foundational to TLS, S/MIME, and certificate management.

**Difficulty:** Advanced
**Category:** Security

---

## PAT — Port Address Translation

A variant of NAT (also called NAPT or NAT overload) that maps multiple private IP:port pairs to a single public IP address using different port numbers. PAT is what most home routers do: all internal hosts share one public IP, differentiated by their translated source port. It conserves IPv4 address space at the cost of breaking certain protocols.

**Difficulty:** Intermediate
**Category:** Networking
