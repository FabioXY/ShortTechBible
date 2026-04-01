
## VPN — Virtual Private Network

Encrypted tunnel over a public network providing secure connectivity. Site-to-site
VPNs connect networks; client VPNs provide remote access. Protocols: WireGuard,
OpenVPN, IPsec/IKEv2, L2TP/IPsec. VPNs protect traffic confidentiality but
do not make connections anonymous if the VPN provider can log and share data.

**Difficulty:** Base
**Category:** Security

---

## VXLAN — Virtual Extensible LAN

Network virtualization protocol (RFC 7348) encapsulating Layer 2 Ethernet frames
inside UDP packets to create overlay networks across Layer 3 infrastructure.
Uses a 24-bit VNI (VXLAN Network Identifier) supporting up to 16 million isolated
virtual networks. Standard overlay for Kubernetes CNI plugins and OpenStack Neutron.

**Difficulty:** Advanced
**Category:** Networking

---

## VCPU — Virtual CPU

CPU resource presented to a VM or container by a hypervisor. A vCPU is a scheduled
share of a physical CPU core, not a dedicated hardware thread. Overprovisioning
vCPUs beyond physical threads causes CPU steal time and performance contention.
Monitored via `%steal` in `vmstat` and cloud provider metrics.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VDSL — Very High Speed DSL

DSL variant delivering speeds up to 100 Mbps downstream over short copper loops
(under 500 meters). VDSL2 with vectoring achieves up to 300 Mbps and is deployed
by telecoms for fiber-to-the-cabinet (FTTC) last-mile connectivity. Crosstalk
from adjacent pairs is the main performance limiter.

**Difficulty:** Intermediate
**Category:** Networking

---

## VMDK — Virtual Machine Disk

Virtual hard disk format used by VMware hypervisors. A VMDK consists of a flat
binary data file and a descriptor file. Supports thin provisioning (growing on
demand), thick provisioning (pre-allocated), and split into 2 GB chunks for
FAT32 compatibility. Also used by VirtualBox, QEMU, and Proxmox with converters.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VMFS — Virtual Machine File System

VMware proprietary cluster filesystem optimized for storing VMware virtual machine
files (VMDKs) on shared storage (SAN/NFS). Supports concurrent access from
multiple ESXi hosts to the same volume, enabling vMotion live migration and HA
features. VMFS6 is the current version supporting drives larger than 2 TB.

**Difficulty:** Advanced
**Category:** Cloud

---

## VNIC — Virtual Network Interface Card

Software-emulated network interface presented to a VM or container. A vNIC connects
to a virtual switch (vSwitch or OVS) within the hypervisor. The guest OS sees
the vNIC as a real hardware device. SR-IOV provides hardware-backed vNICs with
near-native performance by assigning Physical Functions (PFs) and Virtual Functions
(VFs) directly to VMs.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VRRP — Virtual Router Redundancy Protocol

IETF open standard (RFC 5798) providing automatic failover of a default gateway
IP address between routers. One router is elected Master and owns the virtual
IP; Backup routers take over if the Master fails. Similar to Cisco HSRP.
Configured for highly available gateway setups in enterprise and home labs.

**Difficulty:** Intermediate
**Category:** Networking

---

## VSTP — Virtual STP (Spanning Tree Protocol)

Juniper Networks implementation of a per-VLAN spanning tree protocol on EX-series
switches. Similar in function to Cisco PVST+, running separate STP instances
per VLAN to allow different root bridges and load balancing across redundant
links for different traffic flows.

**Difficulty:** Advanced
**Category:** Networking

---

## VTEP — VXLAN Tunnel Endpoint

Network device or software component that encapsulates and decapsulates VXLAN
packets. VTEPs are the ingress and egress points of VXLAN tunnels. Can be
implemented in hardware (switches with VXLAN offload), in hypervisor virtual
switches (OVS), or in Linux kernel (vxlan interface). VTEP IP addresses are
exchanged via BGP EVPN control plane.

**Difficulty:** Advanced
**Category:** Networking

---

## VETH — Virtual Ethernet Pair

Linux kernel construct creating a pair of interconnected virtual network interfaces.
Packets sent into one end appear on the other. Used to connect containers and
network namespaces: one end lives in the container namespace, the other in the
host or bridge namespace. Core building block of Docker and Kubernetes networking.

**Difficulty:** Intermediate
**Category:** OS

---

## VIRT — Virtualization

Abstraction layer enabling multiple isolated operating system instances (VMs)
to share physical hardware resources. Hardware-assisted: Intel VT-x/VT-d, AMD-V/AMD-Vi.
Hypervisor types: Type 1 (bare-metal: KVM, Hyper-V, ESXi) and Type 2 (hosted:
VirtualBox, Parallels). Container virtualization (Docker, LXC) shares the host kernel.

**Difficulty:** Base
**Category:** Cloud

---

## VLSM — Variable Length Subnet Masking

Technique subdividing an IP address space using subnet masks of different lengths
rather than a single uniform mask. Allows efficient allocation of address ranges
sized to actual network needs. Example: allocating a /30 (4 addresses) for a
point-to-point link rather than wasting a /24. Part of CIDR addressing.

**Difficulty:** Intermediate
**Category:** Networking

---

## VPLS — Virtual Private LAN Service

MPLS-based Layer 2 VPN service emulating an Ethernet LAN across a service provider
network. Multiple customer sites see each other as if connected to the same
Ethernet switch. Uses pseudowires (PW) between PE routers and MAC learning
within the VPN. More complex than L3 VPN; supports bridge-mode customer devices.

**Difficulty:** Advanced
**Category:** Networking

---

## VPNC — VPN Concentrator

Network device aggregating many VPN connections from remote users or sites,
terminating the VPN tunnels and routing the decrypted traffic into the corporate
network. Can be dedicated hardware (Cisco ASA, Juniper SRX) or software-based.
High-availability designs use active/passive or active/active concentrator pairs.

**Difficulty:** Intermediate
**Category:** Security

---

## VRFS — VRF Instances (Plural)

Multiple Virtual Routing and Forwarding tables active simultaneously on a single
router, each maintaining an independent routing table, forwarding table, and set
of interfaces. A packet's VRF is determined by which interface it arrived on.
Enables network segmentation (management VRF isolation) and MPLS L3 VPN services.

**Difficulty:** Advanced
**Category:** Networking

---

## VSAN — Virtual SAN

VMware software-defined storage product (vSAN) aggregating locally attached disks
in ESXi hosts into a shared distributed datastore accessible by all cluster members.
Uses a hybrid (SSD + HDD) or all-flash configuration with data striping, mirroring,
and erasure coding for protection. Alternative to SAN hardware for vSphere clusters.

**Difficulty:** Advanced
**Category:** Cloud

---

## VENV — Virtual Environment

Isolated Python runtime environment containing its own Python interpreter, pip,
and installed packages independent of the system Python. Created with `python -m venv`.
Prevents package version conflicts between projects. Used alongside `pip` and
`requirements.txt` or `pyproject.toml` for reproducible Python development environments.

**Difficulty:** Base
**Category:** Dev

---

## VHBA — Virtual Host Bus Adapter

Software-emulated HBA presented to a VM for Fibre Channel connectivity. Combined
with NPIV (N-Port ID Virtualization) on physical HBAs, each VM gets its own
WWPN (World Wide Port Name) visible to the FC fabric and storage array for
direct LUN access and per-VM zoning.

**Difficulty:** Advanced
**Category:** Hardware

---

## VOLT — Voltage Level (Hardware Context)

Electrical potential difference measured in volts between two points in a circuit.
In IT hardware: CPU core voltage (VCore, typically 0.8–1.4V), DDR DRAM voltage
(1.1V DDR5, 1.2V DDR4), PCIe slot power rails (3.3V, 12V). Undervolting reduces
power consumption and heat; overvolting risks chip damage.

**Difficulty:** Intermediate
**Category:** Hardware

---

## VXRM — VXLAN Route Map

Policy construct in BGP EVPN control planes filtering or modifying VXLAN route
advertisements between VTEPs. Used to control which MAC/IP bindings and type-2/type-5
EVPN routes are distributed to specific peers, enabling route policy enforcement
in multi-tenant VXLAN fabrics.

**Difficulty:** Advanced
**Category:** Networking

---

## VDOM — Virtual Domain

FortiGate (Fortinet) virtualization feature dividing a single physical firewall
into multiple independent virtual firewall instances. Each VDOM has its own
policies, routing tables, interfaces, and administrators. Similar concept to
VRF but with full security policy separation rather than just routing isolation.

**Difficulty:** Advanced
**Category:** Security

---

## VMSS — Virtual Machine Scale Set

Azure compute service automatically managing a group of identical VMs behind
a load balancer, scaling in or out based on metrics or schedule. Analogous to
AWS Auto Scaling Groups. VMs in a scale set are created from the same base
image and configuration and are considered disposable, stateless instances.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VPAS — Virtual Private Application Server

Isolated application hosting environment providing dedicated compute, storage,
and networking resources within a shared physical or cloud infrastructure. Positioned
between shared hosting and dedicated server deployments. Customers get root-level
OS access without managing the underlying hypervisor infrastructure.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VBIO — Virtual BIOS

Firmware layer in a virtual machine exposing hardware initialization services
to the guest OS in place of physical BIOS/UEFI. Implemented by the hypervisor
(SeaBIOS for QEMU legacy BIOS, OVMF for UEFI VMs). OVMF is UEFI-compliant and
required for Windows 11, Secure Boot, and TPM emulation in KVM/QEMU virtual machines.

**Difficulty:** Advanced
**Category:** Cloud

---

## VTBL — Virtual Table (C++ vtable)

Internal compiler-generated structure implementing C++ virtual function dispatch.
Each class with virtual methods has a vtable containing pointers to its virtual
function implementations. Objects carry a vptr (hidden pointer) to the class
vtable, enabling runtime polymorphism. vtable hijacking is a classic memory
corruption exploitation technique.

**Difficulty:** Advanced
**Category:** Dev

---

## VECS — VMware Endpoint Certificate Store

VMware infrastructure component managing TLS certificates for vCenter, ESXi,
and other vSphere services. Handles certificate generation, storage, and renewal
for internal VMware SSL infrastructure. Failures in VECS are a common cause of
vSphere service startup failures after certificate expiry.

**Difficulty:** Advanced
**Category:** Cloud

---

## VPMD — Virtual Port Metadata

In DPDK (Data Plane Development Kit), per-port configuration data describing
the network interface characteristics, queue configuration, offload capabilities,
and driver-specific settings used by the Poll-Mode Driver (PMD) for zero-copy,
kernel-bypass packet I/O at line rate.

**Difficulty:** Advanced
**Category:** Networking

---

## VRAM — Video RAM

Dedicated memory on a GPU used to store framebuffers, textures, shader programs,
and intermediate render targets. Bandwidth-optimized: GDDR6X (1 TB/s) on NVIDIA
RTX 4090. Distinct from system RAM. Insufficient VRAM causes texture thrashing
and severe performance degradation in 3D workloads and AI model inference.

**Difficulty:** Intermediate
**Category:** Hardware

---

## VDIF — VLBI Data Interchange Format

Open standard for packetizing Very Long Baseline Interferometry (VLBI) data
from radio telescopes. Designed for high-bandwidth recording (up to tens of Gbps)
with precise timing metadata. Relevant to IT engineers building data acquisition
and transport systems for scientific radio telescope arrays.

**Difficulty:** Advanced
**Category:** Networking

---

## VLBI — Very Long Baseline Interferometry

Radio astronomy technique combining signals from geographically separated antennas
to achieve extremely high angular resolution. Data is recorded with precise atomic
clock timestamps and correlated in post-processing. IT infrastructure for VLBI
requires high-capacity storage, precise timing via GPS, and high-bandwidth data
transport.

**Difficulty:** Advanced
**Category:** Hardware

---

## VMID — Virtual Machine Identifier

Unique integer assigned by a hypervisor to each virtual machine within a cluster.
In Proxmox VE, the VMID (100–999999999) identifies VMs and LXC containers across
the cluster, used in CLI commands (`qm start 100`), configuration file paths
(`/etc/pve/qemu-server/100.conf`), and API calls.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VNET — Virtual Network

Software-defined network isolated from the physical network fabric and other
virtual networks. In cloud platforms (Azure VNet, AWS VPC, GCP VPC), a VNet
provides IP addressing, subnetting, routing, and security group policies for
cloud resources. VNets can be peered or connected via VPN gateways.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VIOS — Virtual I/O Server
IBM PowerVM component that runs on a dedicated LPAR and provides virtualized storage and network resources to client LPARs. Acts as a shared I/O hub: client partitions access physical adapters (FC HBAs, NICs) through VIOS via NPIV and virtual Ethernet.
**Difficulty:** Advanced
**Category:** OS

---

## VXML — VoiceXML
W3C standard markup language for creating voice-based interactive applications. Defines dialog flows, speech recognition grammars, audio playback, and DTMF input handling. Used in IVR systems and telephony platforms (Cisco CVP, Genesys) to build automated call handling without custom code.
**Difficulty:** Intermediate
**Category:** Dev

---

## VCSA — vCenter Server Appliance
VMware vCenter Server packaged as a preconfigured Linux-based virtual appliance (Photon OS). Manages ESXi hosts, vSphere clusters, vMotion, HA, and DRS. Replaced the Windows-based vCenter installation as the standard deployment model since vSphere 6.5.
**Difficulty:** Intermediate
**Category:** Cloud

---

## VDPA — vDPA (virtio Data Path Acceleration)
Linux kernel framework that offloads the virtio data plane from the host CPU to dedicated hardware (SmartNICs, DPUs). The control plane stays in the kernel while the data path runs on the NIC, reducing CPU overhead for VM and container networking at high packet rates.
**Difficulty:** Advanced
**Category:** OS

---
## VTSS — Virtual Terminal Session State
Representation of a terminal emulator session stored server-side, allowing reconnection after network interruption. Used in session multiplexers (tmux, screen) and enterprise terminal servers to preserve CLI state independently of the TCP connection lifecycle.
**Difficulty:** Intermediate
**Category:** OS

---

## VLAN — Virtual Local Area Network
Layer 2 network segmentation technique defined by IEEE 802.1Q. Tags Ethernet frames with a 12-bit VLAN ID (1-4094) to logically separate broadcast domains on shared physical infrastructure. Requires trunk ports between switches to carry multiple VLANs. Foundational in enterprise and data center networking.
**Difficulty:** Intermediate
**Category:** Networking


---

## VXDB — Virtual Extensible Database
Distributed database layer used in some SDN controllers and network virtualization platforms to replicate VXLAN tunnel endpoint tables and overlay network state across controller cluster nodes. Ensures consistent forwarding tables without a single point of failure.
**Difficulty:** Advanced
**Category:** Database


---

## VAULT — HashiCorp Vault

Secrets management platform providing centralized storage, access control, dynamic credential generation, and encryption-as-a-service. Secret engines: KV (static secrets), PKI (certificate issuance), AWS/GCP/Azure (dynamic cloud credentials), database (dynamic DB credentials). Auth methods: AppRole, Kubernetes, AWS IAM, LDAP. Key rotation and lease expiry enforce least-privilege access.

**Difficulty:** Intermediate
**Category:** Security

---

## VIRSH — Virsh KVM CLI

Command-line interface for managing KVM/QEMU virtual machines and libvirt resources. Key commands: virsh list --all, virsh start/shutdown/destroy, virsh console, virsh snapshot-create-as, virsh edit (XML), virsh dumpxml, virsh pool-list, virsh net-list. Scriptable via bash; pairs with virt-install for VM provisioning and virt-clone for cloning.

**Difficulty:** Intermediate
**Category:** OS

---

## VCNTR — vCenter Management

VMware vCenter Server: centralized management platform for vSphere environments. Manages ESXi hosts, VMs, clusters, distributed switches, storage, and vSAN via web UI and REST API. Core features: vMotion (live VM migration), DRS (Distributed Resource Scheduler), HA (automatic VM restart), and lifecycle management. Deployed as vCSA (Linux appliance) since vSphere 7.0.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VELRO — Velero Kubernetes Backup

Open-source Kubernetes backup and restore tool (formerly Heptio Ark). Backs up Kubernetes resource definitions (from API server) and persistent volume data (via Restic/Kopia or CSI snapshots) to object storage (S3, GCS, Azure Blob). Supports cluster migration, DR, and namespace-level restore. Schedule CRDs automate recurring backup jobs.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VMBKP — VM Backup Strategy

Process creating consistent copies of VM state (disk images, configuration) for recovery. Methods: agent-based (Veeam agent inside VM), agentless (VMware VADP snapshot-based), image-level (qemu-img, AWS Backup). Consistency: VSS quiescing (Windows) or fsfreeze (Linux) during snapshot to avoid filesystem inconsistency in the backup image.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VPCRT — VPC Route Table

Cloud routing construct defining traffic direction within a VPC subnet. Each subnet associates with one route table; each route has a destination CIDR and a target (internet gateway, NAT gateway, VPC peering, transit gateway, VPN, or local). Most-specific route wins. Separate route tables for public (IGW route) and private (NAT GW route) subnets enforce network segmentation.

**Difficulty:** Intermediate
**Category:** Cloud

---

## VSFTD — vsftpd FTP Daemon

Very Secure FTP Daemon: lightweight, security-focused FTP server for Linux. Supports virtual users, SSL/TLS (FTPS via ssl_enable=YES), IPv6, bandwidth throttling, and chroot jailing of users to home directories. Configuration: /etc/vsftpd.conf. Passive mode requires pasv_min/max_port range and matching firewall rules to allow data connections.

**Difficulty:** Intermediate
**Category:** Networking

---

## VTUND — VTun VPN Daemon

Open-source VPN daemon creating virtual tunnel interfaces (tun/tap) over TCP or UDP. Supports LZO/zlib compression and bandwidth shaping. Earlier alternative to OpenVPN; less maintained but found in legacy network appliances and embedded Linux VPN implementations where a simple tunnel without PKI complexity is sufficient.

**Difficulty:** Intermediate
**Category:** Networking

---

## VXRMD — VXLAN Remote MAC DB

Database of MAC address entries learned for remote VTEPs in a VXLAN overlay, populated via BGP EVPN control plane or flood-and-learn data plane. When a frame targets a remote MAC, the local VTEP encapsulates it and forwards to the corresponding remote VTEP IP. Inspectable via bridge fdb show on Linux VXLAN interfaces.

**Difficulty:** Advanced
**Category:** Networking


---

## VBOX — VirtualBox

Open-source x86/AMD64 hypervisor (Type 2) developed by Oracle. Supports Windows, Linux, macOS, and Solaris guests with hardware virtualization (VT-x/AMD-V), paravirtualization (VirtIO, Hyper-V interface), snapshots, linked clones, NAT/bridged/internal networking, shared folders via Guest Additions, and a headless mode. Free for personal use; PUEL license for enterprise extensions.

**Difficulty:** Base
**Category:** Cloud
