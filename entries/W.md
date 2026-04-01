## WAMP — Windows Apache MySQL PHP

Software stack bundling Apache HTTP server, MySQL (or MariaDB), and PHP on Windows for local web development. Common tools include WampServer and XAMPP. Equivalent to LAMP on Linux. Used to run and test PHP applications locally without a dedicated server.

**Difficulty:** Base
**Category:** Dev


---

## WASM — WebAssembly

Binary instruction format and compilation target for high-performance code in web browsers. Runs at near-native speed in a sandboxed environment, enabling C, C++, Rust, and Go programs to execute in the browser. Standardized by W3C; also used in serverless edge runtimes (Fastly, Cloudflare Workers) outside the browser.

**Difficulty:** Intermediate
**Category:** Dev


---

## WBEM — Web-Based Enterprise Management

DMTF standard framework for enterprise system management over networks. Uses CIM as the information model and defines a set of transport protocols (CIM-XML over HTTP). Implemented in tools like WMI (Windows), OpenPegasus (Linux), and HP SIM.

**Difficulty:** Advanced
**Category:** Networking


---

## WCCP — Web Cache Communication Protocol

Cisco protocol that transparently redirects HTTP and HTTPS traffic from a router or switch to a web cache or proxy appliance. Supports load balancing across multiple cache engines. Used in enterprise networks to offload bandwidth and enforce web filtering policies.

**Difficulty:** Intermediate
**Category:** Networking


---

## WDAC — Windows Defender Application Control

Windows security feature (previously Device Guard) that enforces application whitelisting policies at the kernel level. Allows only trusted, signed executables and scripts to run, blocking unsigned or unauthorized code regardless of user privilege. Configured via Group Policy or MEMCM.

**Difficulty:** Advanced
**Category:** Security


---

## WEAP — Wireless Extensible Authentication Protocol

Generic term for EAP methods deployed over wireless 802.1X authentication. The term encompasses PEAP, EAP-TLS, EAP-TTLS, and other EAP variants used between a Wi-Fi supplicant, authenticator (AP), and RADIUS server to establish identity before granting network access.

**Difficulty:** Intermediate
**Category:** Security


---

## WEP — Wired Equivalent Privacy

Original IEEE 802.11 wireless encryption standard (1997), now deprecated. Used RC4 stream cipher with static 40-bit or 104-bit keys and a weak 24-bit IV, making it vulnerable to statistical attacks. Broken in minutes with passive traffic capture. Replaced by WPA and WPA2.

**Difficulty:** Base
**Category:** Security


---

## WEXT — Wireless Extensions

Legacy Linux kernel API (also known as iwext or Wireless Extensions interface) for configuring 802.11 devices via ioctls. Used by iwconfig and iwlist. Deprecated in favor of the cfg80211/nl80211 framework used by iw and wpa_supplicant since kernel 2.6.22+.

**Difficulty:** Intermediate
**Category:** OS


---

## WFAS — Windows Firewall with Advanced Security

Host-based stateful firewall built into Windows, manageable via MMC snap-in, Group Policy, or PowerShell (NetSecurity module). Supports inbound/outbound rules, IPsec integration, connection security rules, and profile-based policies (Domain, Private, Public). Available since Windows Vista.

**Difficulty:** Intermediate
**Category:** Security


---

## WIDS — Wireless Intrusion Detection System

System that monitors the radio frequency spectrum for unauthorized access points, rogue clients, deauthentication attacks, and other 802.11 threats. Can operate passively (dedicated sensors) or in-line. Often integrated with WLAN controllers (Cisco WLC, Aruba, Meraki).

**Difficulty:** Intermediate
**Category:** Security


---

## WISP — Wireless Internet Service Provider

Internet service provider that delivers broadband connectivity to customers using wireless radio links instead of wired infrastructure. Uses licensed or unlicensed spectrum (2.4 GHz, 5 GHz, 900 MHz, CBRS) and point-to-multipoint equipment. Common in rural areas where fiber deployment is cost-prohibitive.

**Difficulty:** Base
**Category:** Networking


---

## WLAN — Wireless Local Area Network

Local area network that uses radio frequency transmission instead of physical cables, standardized by IEEE 802.11. Operates in 2.4 GHz, 5 GHz, and 6 GHz (Wi-Fi 6E) bands. Key parameters: SSID, channel width, security protocol (WPA2/WPA3), and AP placement for coverage and throughput.

**Difficulty:** Base
**Category:** Networking


---

## WLDP — Windows Lockdown Policy

Windows kernel feature that enforces code integrity policies on PowerShell, .NET, and COM objects at the operating system level. Part of the Virtualization-Based Security (VBS) suite. Prevents script-based attacks by restricting language modes and blocking unsigned DLL injection.

**Difficulty:** Advanced
**Category:** Security


---

## WMIC — Windows Management Instrumentation Command-line

Command-line interface to the WMI infrastructure. Allows querying system information (hardware, processes, services, registry) and executing management operations without GUI tools. Deprecated in Windows 11 21H1 in favor of PowerShell Get-WmiObject and Get-CimInstance equivalents.

**Difficulty:** Intermediate
**Category:** OS


---

## WMTS — Web Map Tile Service

OGC standard protocol for serving pre-rendered, cached map tiles over HTTP. Tiles are addressed by layer, style, tile matrix set, and row/column coordinates. Used in GIS platforms (ArcGIS, GeoServer, QGIS) and web mapping libraries (Leaflet, OpenLayers) for fast map rendering.

**Difficulty:** Intermediate
**Category:** Protocol


---

## WOR — Wake-on-Ring

System configuration that powers on a sleeping or powered-off computer when the modem detects an incoming phone call or ring signal on a serial port. Historically used for remote access via dial-up; largely superseded by Wake-on-LAN and remote management cards (IPMI, iDRAC).

**Difficulty:** Base
**Category:** Hardware


---

## WORM — Write Once Read Many

Storage model in which data, once written, cannot be modified or deleted. Used for regulatory compliance (SEC 17a-4, HIPAA), legal hold, and audit logs. Implemented in optical media (CD-R, BD-R), tape (WORM cartridges), and object storage platforms (NetApp SnapLock, AWS S3 Object Lock).

**Difficulty:** Base
**Category:** Hardware


---

## WPAD — Web Proxy Auto-Discovery

Protocol that allows web clients to automatically discover the URL of a proxy configuration file (PAC file) using DNS or DHCP. Clients query wpad.domain.com or receive option 252 from DHCP. Historically abused for MITM attacks on corporate networks via DNS poisoning.

**Difficulty:** Intermediate
**Category:** Protocol


---

## WPA2 — Wi-Fi Protected Access 2

IEEE 802.11i wireless security standard ratified in 2004. Uses AES-CCMP for encryption (replacing TKIP from WPA) and supports both Personal mode (PSK) and Enterprise mode (802.1X/RADIUS). WPA2-Personal with a strong passphrase is still widely deployed; WPA2-Enterprise provides per-user authentication.

**Difficulty:** Intermediate
**Category:** Security


---

## WPA3 — Wi-Fi Protected Access 3

Wi-Fi Alliance security standard released in 2018. Replaces the PSK handshake with SAE (Simultaneous Authentication of Equals), eliminating offline dictionary attacks. Enterprise mode mandates 192-bit cryptographic strength. WPA3-Enhanced Open adds opportunistic encryption on open networks via OWE.

**Difficulty:** Intermediate
**Category:** Security


---

## WPAN — Wireless Personal Area Network

Short-range wireless network designed for communication between devices within an individual's personal space (typically under 10 meters). Technologies include Bluetooth (IEEE 802.15.1), Zigbee (802.15.4), Z-Wave, UWB, and NFC. Used in IoT, wearables, and home automation.

**Difficulty:** Base
**Category:** Networking


---

## WRED — Weighted Random Early Detection

Active queue management algorithm that probabilistically drops packets before a queue fills, based on traffic class weights and average queue depth. Prioritizes high-priority traffic by applying lower drop probability. Used in routers to prevent TCP global synchronization and enforce QoS under congestion.

**Difficulty:** Advanced
**Category:** Networking


---

## WREP — Write Replication

Storage mechanism that writes data simultaneously to multiple locations (local and remote) to ensure durability and disaster recovery readiness. Implemented synchronously (zero data loss, higher latency) or asynchronously (potential data loss in failure, lower latency impact). Common in SAN, NAS, and cloud object storage.

**Difficulty:** Intermediate
**Category:** Hardware


---

## WSGI — Web Server Gateway Interface

Python standard (PEP 3333) defining the interface between web servers and Python web application frameworks. Allows frameworks (Django, Flask, Pyramid) to run behind any WSGI-compatible server (Gunicorn, uWSGI, mod_wsgi). Being gradually replaced by ASGI for async support.

**Difficulty:** Intermediate
**Category:** Dev


---

## WSDL — Web Services Description Language

XML-based language for describing the interface of SOAP web services. Defines available operations, input/output message formats, and transport bindings. Used by clients to auto-generate stubs and by tooling (e.g. Apache CXF, WCF) to implement service contracts. Less common since REST replaced SOAP in most new APIs.

**Difficulty:** Intermediate
**Category:** Dev


---

## WSMP — WAVE Short Message Protocol

Lightweight protocol in the IEEE 1609 WAVE (Wireless Access in Vehicular Environments) stack used for exchanging short messages between vehicles and roadside infrastructure (V2X). Operates directly over 802.11p (DSRC) without TCP/IP overhead, enabling sub-100 ms latency for safety-critical applications.

**Difficulty:** Advanced
**Category:** Protocol


---

## WSRP — Web Services for Remote Portlets

OASIS standard for integrating portlets (reusable UI components) across different web portals via SOAP. Allows a portlet hosted on one server to be consumed and rendered by a portal on another server. Used in enterprise portal platforms (IBM WebSphere Portal, SAP NetWeaver Portal).

**Difficulty:** Advanced
**Category:** Dev


---

## WSUS — Windows Server Update Services

Microsoft server role that downloads Windows and Microsoft product updates from Microsoft Update and distributes them to client machines on the local network. Reduces external bandwidth usage, provides update approval control, and generates compliance reports. Commonly replaced or supplemented by MEMCM/SCCM.

**Difficulty:** Intermediate
**Category:** OS


---

## WVAN — Wireless Virtual Area Network

Logical network overlay on a WLAN infrastructure that separates wireless clients into isolated segments, similar to VLAN tagging on wired networks. WLAN controllers map SSIDs to WVANs and apply independent security, QoS, and routing policies per segment. Also called SSID-to-VLAN mapping in many implementations.

**Difficulty:** Intermediate
**Category:** Networking


---

## WAVE — Wireless Access in Vehicular Environments

IEEE 1609 family of standards enabling V2X (Vehicle-to-Everything) communication using DSRC (802.11p) in the 5.9 GHz band. Defines the full communication stack from PHY to application layer, including security (1609.2), multi-channel operation (1609.4), and resource management (1609.3).

**Difficulty:** Advanced
**Category:** Protocol


---

## WWID — World Wide Identifier

Globally unique identifier assigned to a storage device or host bus adapter in SAN environments. Used to persistently identify LUNs and paths regardless of port or connection changes. The OS uses WWIDs (visible via /dev/disk/by-id/ on Linux) for consistent device naming in multipath setups.

**Difficulty:** Intermediate
**Category:** Hardware


---

## WWNN — World Wide Node Name

64-bit unique identifier assigned to a Fibre Channel node (HBA or storage controller) that persists across port changes. Used alongside WWPNs to identify the physical device. Assigned by the vendor using the IEEE OUI-based NAA format. Stored in the HBA firmware.

**Difficulty:** Intermediate
**Category:** Hardware


---

## WWPN — World Wide Port Name

64-bit globally unique identifier for a specific Fibre Channel port on an HBA or storage array. Used in FC zoning to control which initiators can communicate with which targets. Each physical port has its own WWPN; NPIV allows multiple virtual WWPNs per physical port.

**Difficulty:** Intermediate
**Category:** Hardware


---

## WEVT — Windows Event Log

Binary structured logging system in Windows (Vista and later) that replaced the older .evt format with the .evtx format. Events are stored in XML with a strict schema, queried via XPath, and managed through the Windows Event Log service (wevtsvc). Accessible via Event Viewer, wevtutil, and Get-WinEvent.

**Difficulty:** Intermediate
**Category:** OS


---

## WINS — Windows Internet Name Service

Microsoft implementation of NetBIOS Name Service (NBNS). Resolves NetBIOS names to IP addresses in pre-Active-Directory Windows networks. Deprecated since Windows Server 2008 but still present for backward compatibility. Superseded by DNS with SRV records in AD environments.

**Difficulty:** Intermediate
**Category:** Networking


---

## WTLS — Wireless Transport Layer Security

Security protocol defined in the WAP stack for encrypting communications between mobile devices and WAP gateways over wireless links (GPRS-era). Adapted from TLS with optimizations for low-bandwidth, high-latency links. Obsolete; replaced by TLS end-to-end as mobile browsers adopted HTTPS directly.

**Difficulty:** Advanced
**Category:** Security


---

## WVPN — Wireless VPN

VPN deployment model where tunnel endpoints are wireless clients or access points rather than wired infrastructure. Addresses the additional attack surface of wireless links by encrypting traffic before it leaves the device. Common in public Wi-Fi scenarios and enterprise split-tunneling policies.

**Difficulty:** Intermediate
**Category:** Security


---

## WSFL — Web Services Flow Language

IBM XML-based language for composing web services into workflows and business processes. Predecessor to BPEL (Business Process Execution Language). Defined graph-based flow models for service orchestration. Merged with Microsoft XLANG to form BPEL4WS and later standardized as WS-BPEL by OASIS.

**Difficulty:** Advanced
**Category:** Dev


---

## WTTX — Wireless to the X

Generic wireless last-mile connectivity model where the final segment to the subscriber is delivered over radio rather than fiber or copper. Encompasses FWA (Fixed Wireless Access) using LTE/5G, mmWave, and licensed microwave. Used by telcos to bypass costly trench-and-cable deployments.

**Difficulty:** Intermediate
**Category:** Networking


---

## WKSP — Workspace

Logical environment grouping tools, configurations, files, and sessions for a specific project or user context. In IDEs (VS Code, IntelliJ), a workspace defines the root directory and project settings. In container and cloud platforms, it defines resource and access boundaries for a development or deployment unit.

**Difficulty:** Base
**Category:** Dev



---

## WAFFW — WAF Firewall

Web Application Firewall inspecting HTTP/HTTPS traffic and blocking requests matching known attack signatures (OWASP Core Rule Set), rate limits, or custom rules. Deployed inline (reverse proxy), out-of-band, or as a cloud service (AWS WAF, Cloudflare WAF, F5 AWAF). Protects against SQLi, XSS, CSRF, LFI, RFI, and automated bot attacks.

**Difficulty:** Intermediate
**Category:** Security

---

## WRKFL — Workflow Engine

System orchestrating task execution sequences, decisions, and data transformations. Examples: Apache Airflow (DAG-based ETL), Temporal.io (durable workflow execution), AWS Step Functions (serverless state machine), Argo Workflows (Kubernetes-native). Key features: retry logic, dependency management, parallel execution, and durable state persistence across failures.

**Difficulty:** Intermediate
**Category:** Dev

---

## WINHV — Windows Hypervisor

Hyper-V: Microsoft's native type-1 hypervisor integrated into Windows Server and Windows 10/11 Pro/Enterprise. Uses Intel VT-x/AMD-V hardware virtualization. Manages VMs via Hyper-V Manager, PowerShell, or Windows Admin Center. Supports nested virtualization, live migration, generation 2 VMs (UEFI, Secure Boot), and ReFS/VHDX virtual disk formats.

**Difficulty:** Intermediate
**Category:** Cloud

---

## WEBGL — WebGL Graphics API

JavaScript API for GPU-accelerated 2D and 3D rendering in browsers without plugins. WebGL 1.0 is based on OpenGL ES 2.0; WebGL 2.0 on OpenGL ES 3.0. Executes GLSL shader programs on the GPU. Used for data visualization (deck.gl, three.js), browser games, and CAD tools. WebGPU is the next-generation successor with compute shader support.

**Difficulty:** Intermediate
**Category:** Dev

---

## WINSV — Windows Server OS

Microsoft's server OS providing Active Directory, DNS, DHCP, SMB file sharing, IIS web hosting, Hyper-V, failover clustering, and WSUS patch management. Available in Standard, Datacenter, and Essentials editions. Licensed per-core with CALs. Current release: Windows Server 2025. Server Core installation option provides a minimal footprint without GUI.

**Difficulty:** Base
**Category:** OS

---

## WEBPK — Webpack JS Bundler

JavaScript module bundler transforming application source files (JS, CSS, images) into optimized browser bundles. Concepts: entry points, loaders (transforming non-JS assets), plugins (HTML generation, optimization), code splitting (dynamic imports), and tree shaking (dead code elimination). Being supplemented by Vite, esbuild, and Turbopack in modern toolchains.

**Difficulty:** Intermediate
**Category:** Dev

---

## WSHKL — Web Shell Malware

Malicious script (PHP, ASP, JSP) uploaded to a web server to provide remote command execution via HTTP. Deployed after exploiting file upload vulnerabilities, RCE flaws, or CMS plugin vulnerabilities. Detection: file integrity monitoring (Tripwire, AIDE), EDR behavioral analysis, web server access log anomalies (unusual POST to image directories). Examples: China Chopper, b374k.

**Difficulty:** Advanced
**Category:** Security

---

## WCORS — CORS Web Policy

Cross-Origin Resource Sharing (W3C specification) controlling which origins can make cross-origin HTTP requests in browsers. Server responds with Access-Control-Allow-Origin, Access-Control-Allow-Methods, and Access-Control-Allow-Headers. Preflight OPTIONS request checks permissions before state-changing requests. Misconfigured wildcard CORS with credentials enables cross-site data theft.

**Difficulty:** Intermediate
**Category:** Security

---

## WRKLD — Cloud Workload

Defined set of computing tasks running on cloud infrastructure. In Kubernetes: managed via Deployment, StatefulSet, DaemonSet, Job, and CronJob resources. Workload Identity Federation allows pods to authenticate to cloud APIs (S3, GCS, KMS) using Kubernetes service account tokens without static credentials stored as Secrets.

**Difficulty:** Base
**Category:** Cloud

---

## WPAPI — WordPress REST API

WordPress REST API providing JSON endpoints for programmatic access to posts, pages, users, and taxonomies at /wp-json/wp/v2/. Authentication: Application Passwords, OAuth 1.0a, or JWT plugins. Enables headless WordPress architectures (Next.js/React frontend consuming WP content), mobile app backends, and third-party content integrations.

**Difficulty:** Intermediate
**Category:** Dev

---

## WMIRM — WMI Remote Management

Windows Management Instrumentation for remote system management: querying hardware inventory, monitoring performance counters, executing remote commands, and managing services via DCOM/RPC. PowerShell uses Get-CimInstance (WS-Man transport, recommended) or Get-WmiObject (deprecated). WMI lateral movement is heavily monitored by EDR solutions.

**Difficulty:** Intermediate
**Category:** OS


---

## WINRM — Windows Remote Management

Microsoft implementation of the WS-Management SOAP protocol enabling remote command execution and system management on Windows. Uses HTTP (port 5985) or HTTPS (port 5986). PowerShell Remoting (Enter-PSSession, Invoke-Command) runs over WinRM. Ansible uses WinRM for Windows automation. Requires explicit enablement (Enable-PSRemoting) and firewall rule configuration.

**Difficulty:** Intermediate
**Category:** OS

---

## WAZUH — Open-Source SIEM and XDR

Open-source security platform combining HIDS (host intrusion detection), log analysis, vulnerability detection, and incident response. Agents installed on endpoints forward security data to the Wazuh manager, which correlates events using rules and integrates with OpenSearch/Elasticsearch for storage and visualization. Successor to OSSEC with active commercial development.

**Difficulty:** Intermediate
**Category:** Security

---

## WARP — Cloudflare WARP Protocol

Cloudflare's VPN and DNS-over-HTTPS client using the WireGuard protocol with Cloudflare's network as the carrier. Routes all device traffic through Cloudflare's 1.1.1.1 infrastructure for filtering and acceleration. WARP+ adds intelligent routing for performance. WARP for Teams integrates with Cloudflare Access for Zero Trust network policies.

**Difficulty:** Intermediate
**Category:** Security

---

## WEBDAV — Web Distributed Authoring and Versioning

HTTP extension (RFC 4918) enabling collaborative document editing over the web. Adds methods PROPFIND, PROPPATCH, MKCOL, COPY, MOVE, LOCK, and UNLOCK to standard HTTP. Allows clients to mount remote filesystems over HTTP(S). Used by calendar (CalDAV) and contact (CardDAV) sync protocols and legacy document management systems. Supported natively by Windows, macOS, and Linux file managers.

**Difficulty:** Intermediate
**Category:** Protocol
