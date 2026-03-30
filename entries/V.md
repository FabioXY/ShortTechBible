## VGA — Video Graphics Array

A display standard introduced by IBM in 1987, defining a 640×480 resolution at 16 colors (or 320×240 at 256 colors) and the 15-pin D-sub analog connector still found on legacy hardware. VGA has been superseded by DVI, HDMI, and DisplayPort, but VGA output in server firmware and hypervisors (QEMU, Proxmox) remains common for fallback console access.

**Difficulty:** Base
**Category:** Hardware

---

## VLAN — Virtual Local Area Network

A Layer 2 mechanism (IEEE 802.1Q) that logically segments a physical network into multiple isolated broadcast domains without requiring separate physical infrastructure. Frames on a trunk port carry a 12-bit VLAN ID tag (1–4094). VLANs are used to separate traffic by function (management, production, DMZ), reduce broadcast domains, and enforce security boundaries between groups of hosts.

**Difficulty:** Intermediate
**Category:** Networking

---

## VMDK — Virtual Machine Disk

A file format developed by VMware for storing disk images of virtual machines. A VMDK set typically consists of a descriptor file and one or more extent files containing the actual data. VMDK supports sparse (thin-provisioned) and pre-allocated (thick) modes, snapshots via delta disk chains, and can be converted to/from QCOW2 or raw format using tools like qemu-img.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VPN — Virtual Private Network

A technology that creates an encrypted tunnel over a public network, allowing remote clients or sites to communicate as if they were on the same private network. VPN protocols include IPSec (Layer 3, common in site-to-site), OpenVPN (SSL/TLS-based, UDP/TCP), WireGuard (modern, kernel-native, ChaCha20+Poly1305), and L2TP/IPSec. Split tunneling routes only specific traffic through the VPN.

**Difficulty:** Intermediate
**Category:** Security

---

## VPS — Virtual Private Server

A virtualized server sold as a service by a hosting provider. A VPS runs on shared physical hardware but is isolated via hypervisor (KVM, Xen) or container technology (OpenVZ), giving each customer root access, dedicated CPU/RAM/disk allocations, and a dedicated IP. A VPS sits between shared hosting (no isolation) and a dedicated server (no sharing) in cost and isolation level.

**Difficulty:** Base
**Category:** Cloud

---

## VTEP — VXLAN Tunnel Endpoint

A network entity (physical or virtual) that originates and terminates VXLAN tunnels. A VTEP encapsulates Layer 2 frames in UDP packets (port 4789) adding a 24-bit VXLAN Network Identifier (VNI), then sends them to a remote VTEP which decapsulates and delivers the original frame. VTEPs are implemented in hypervisors (OVS), physical switches, and network appliances.

**Difficulty:** Advanced
**Category:** Networking
