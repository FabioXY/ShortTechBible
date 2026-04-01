## XACL — Extended Access Control List

Access control list that supports additional match criteria beyond basic source/destination IP and port filtering. Extended ACLs (e.g. Cisco IOS extended ACL, Linux iptables) can match on protocol, DSCP, TCP flags, ICMP type, and application-layer attributes. Distinguished from standard ACLs, which match only on source IP.

**Difficulty:** Intermediate
**Category:** Security


---

## XATT — Extended Attribute

Metadata key-value pair associated with a filesystem object (file, directory, symlink) beyond standard POSIX attributes (owner, permissions, timestamps). In Linux, managed via getfattr/setfattr; stored in xattr namespace prefixes (user., security., trusted., system.). Used by SELinux labels, ACLs (system.posix_acl_access), and backup tools.

**Difficulty:** Intermediate
**Category:** OS


---

## XBMC — Xbox Media Center

Open-source media player application originally developed for the original Xbox. Evolved into Kodi (rebranded in 2014) and became a cross-platform home theater software. The codebase is maintained by the XBMC Foundation and supports plugins, streaming sources, and PVR backends.

**Difficulty:** Base
**Category:** OS


---

## XCSR — Cross-Site Request

HTTP request initiated by a browser that targets a different origin than the page that loaded the script. At the core of CSRF attacks, where a malicious page causes the browser to send authenticated requests to another site. Mitigated by SameSite cookies, CSRF tokens, and CORS policies.

**Difficulty:** Intermediate
**Category:** Security


---

## XDCM — Extended Data Center Management

Management layer that provides unified visibility and control across heterogeneous data center components (servers, storage, networking, cooling). Integrates vendor APIs, IPMI, SNMP, and Redfish endpoints into a single control plane for capacity planning, fault management, and lifecycle operations.

**Difficulty:** Advanced
**Category:** Cloud


---

## XDSL — x Digital Subscriber Line

Umbrella term for all DSL variants (ADSL, VDSL, SDSL, HDSL, IDSL) that transmit digital data over existing telephone copper pairs. The x denotes the variable prefix representing the specific technology. Modulation (DMT, QAM) and frequency plan vary by variant, determining achievable speed and range.

**Difficulty:** Intermediate
**Category:** Networking


---

## XFER — Transfer

Generic abbreviation for data transfer operations in IT contexts. Appears in protocol documentation, system call parameters, CLI tools (xferd in curl), and storage metrics (xfer/s). Denotes the movement of data between source and destination regardless of transport protocol.

**Difficulty:** Base
**Category:** Networking


---

## XHCI — Extensible Host Controller Interface

Intel-defined USB host controller specification (USB 3.x). Replaces OHCI (USB 1.1) and EHCI (USB 2.0) with a unified architecture supporting USB 3.2 (SuperSpeed, 10 Gbps) and USB4. Uses a single ring buffer structure per endpoint and supports native power management. Drivers: xhci_hcd in Linux.

**Difficulty:** Advanced
**Category:** Hardware


---

## XIDS — Extended Intrusion Detection System

IDS deployment that augments signature-based detection with behavioral analysis, anomaly detection, and threat intelligence feeds. Correlates events across network, endpoint, and application layers. Positioned as an evolution toward modern NDR (Network Detection and Response) platforms.

**Difficulty:** Advanced
**Category:** Security


---

## XKMS — XML Key Management Specification

W3C specification for managing public keys and X.509 certificates via XML-based web service requests. Defines two sub-protocols: X-KISS (Key Information Service Specification) for key lookup and X-KRSS (Key Registration Service Specification) for key registration. Largely superseded by REST-based PKI APIs.

**Difficulty:** Advanced
**Category:** Security


---

## XLOG — Extended Log Format

W3C standard log format for web server access logs, extending the Common Log Format with configurable fields. Used by IIS natively and supported by Apache via mod_log_config. Fields are declared in a header line (#Fields:), allowing flexible inclusion of request time, bytes, referrer, user agent, and custom headers.

**Difficulty:** Intermediate
**Category:** Dev


---

## XMP — Extensible Metadata Platform

Adobe-defined metadata standard based on RDF/XML. Embeds structured metadata (author, copyright, keywords, GPS coordinates, color profiles) directly inside media files (JPEG, PDF, PNG, TIFF) in a dedicated XMP packet. Supported by Lightroom, Photoshop, ExifTool, and most DAM systems.

**Difficulty:** Intermediate
**Category:** Dev


---

## XMPP — Extensible Messaging and Presence Protocol

Open IETF-standardized protocol (RFC 6120) for real-time messaging, presence, and roster management based on XML streams over TCP. Originally Jabber. Extensible via XEPs (XMPP Extension Protocols) to add file transfer, multi-user chat (MUC), VoIP (Jingle), and IoT messaging. Used by WhatsApp, Slack (internally), and many enterprise IM systems.

**Difficulty:** Intermediate
**Category:** Protocol


---

## XNET — Experimental Network

MIT research network from the 1970s used to prototype early packet-switching concepts. Also a generic term for experimental or out-of-band network segments used in lab and research environments to test new protocols without impacting production infrastructure.

**Difficulty:** Advanced
**Category:** Networking


---

## XNTP — Extended Network Time Protocol

Early implementation of NTP developed at the University of Delaware that extended the original NTP RFC with additional algorithms and daemon features. The xntpd daemon eventually evolved into the reference ntpd implementation. The name predates the modern NTP daemon naming conventions.

**Difficulty:** Advanced
**Category:** Protocol


---

## XORP — Extensible Open Router Platform

Open-source routing software platform designed to run on standard x86 hardware. Supports BGP, OSPF, RIP, PIM, and IGMP with a modular architecture separating routing logic from the forwarding plane. Used in academic research and as a reference implementation for routing protocol development.

**Difficulty:** Advanced
**Category:** Networking


---

## XPRT — Express Protocol Runtime Transport

Generic term for high-performance transport libraries optimized for low-latency data exchange in distributed systems. Used in HPC and financial trading infrastructure where standard TCP/IP overhead is unacceptable. Implementations leverage RDMA, kernel bypass (DPDK), and custom serialization.

**Difficulty:** Advanced
**Category:** Networking


---

## XRPC — XML Remote Procedure Call

Remote procedure call protocol that encodes method calls and responses in XML over HTTP. Precursor to SOAP and still used in some legacy integrations and blog APIs (MetaWeblog, WordPress XML-RPC). Simpler than SOAP but lacks WSDL-based contracts and WS-* security extensions.

**Difficulty:** Intermediate
**Category:** Protocol


---

## XSLT — XML Stylesheet Language Transformations

W3C specification (XSL Transformations) for transforming XML documents into other XML, HTML, or plain text formats using template rules. Processors include Saxon, Xalan, and libxslt. Used in data integration pipelines, document publishing, and converting between XML schemas (e.g. WSDL to documentation).

**Difficulty:** Intermediate
**Category:** Dev


---

## XSRF — Cross-Site Request Forgery

Web security attack that tricks an authenticated user's browser into sending unauthorized requests to a target site. Exploits the browser's automatic inclusion of session cookies. Mitigated by synchronizer CSRF tokens, Double Submit Cookie pattern, and SameSite=Strict/Lax cookie attribute. Also written as CSRF.

**Difficulty:** Intermediate
**Category:** Security


---

## XSSO — Extensible Single Sign-On

Framework for federating identity across heterogeneous SSO systems and protocols. Defines gateway adapters that translate between incompatible authentication schemes (Kerberos, SAML, LDAP, proprietary tokens) allowing cross-domain SSO without requiring protocol standardization at each endpoint.

**Difficulty:** Advanced
**Category:** Security


---

## XTLS — eXtended Transport Layer Security

TLS extension framework that adds features beyond the base TLS 1.3 specification, such as inner protocol multiplexing, traffic camouflage, and flow control extensions. Used in anti-censorship tools (Xray, V2Ray) to make encrypted proxy traffic indistinguishable from standard HTTPS.

**Difficulty:** Advanced
**Category:** Security


---

## XUID — Extended Unique Identifier

128-bit globally unique identifier used in some protocol and database contexts as an extension of the standard 64-bit UID. In SAN environments, refers to extended identifiers for storage volumes and initiators beyond the WWPN address space.

**Difficulty:** Intermediate
**Category:** Database


---

## XVFB — X Virtual Framebuffer

X11 display server that performs all graphical operations in memory rather than on a physical display. Used for headless rendering: running GUI applications, Selenium browser tests, and screenshot tools in CI/CD pipelines and server environments without a monitor. Invoked as Xvfb :99 -screen 0 1280x1024x24.

**Difficulty:** Intermediate
**Category:** OS


---

## XWIN — X Window System

Cygwin/X implementation of the X11 display server for Windows. Part of the Cygwin environment, it allows running Linux/Unix graphical applications natively on Windows by providing a full X11 server. An alternative to VcXsrv and Xming for X forwarding over SSH on Windows clients.

**Difficulty:** Intermediate
**Category:** OS


---

## XML — Extensible Markup Language

W3C-defined markup language for encoding structured documents and data in a format readable by both humans and machines. Uses nested tags with attributes, supports namespaces, and validates against DTD or XML Schema (XSD). Foundation for SOAP, XHTML, SVG, OpenDocument, DOCX (OOXML), and many enterprise data formats.

**Difficulty:** Base
**Category:** Dev


---

## XMSG — XML Message

Generic term for a data payload encoded in XML format, transmitted between systems in messaging architectures, web service calls, or event buses. XML messages carry schema-validated structured content and are parsed by DOM or SAX parsers on the receiving side. Common in SOAP-based integrations and ESB platforms.

**Difficulty:** Base
**Category:** Dev


---

## XPOL — Cross-Polarization

Antenna technique that uses two orthogonally polarized signals (horizontal and vertical, or +45/-45 degrees) on the same frequency to double spectral efficiency. Used in 4G/5G MIMO antennas, microwave backhaul links, and satellite communications. Cross-polarization discrimination (XPD) measures isolation between the two polarizations.

**Difficulty:** Advanced
**Category:** Networking


---

## XDEV — Cross-Device Development

Software development methodology targeting simultaneous deployment on multiple hardware platforms (desktop, mobile, embedded) from a single codebase. Frameworks include Flutter, React Native, Xamarin, and Tauri. Reduces duplication but introduces abstraction overhead and platform-specific edge cases.

**Difficulty:** Intermediate
**Category:** Dev


---

## XGBE — Ten Gigabit Ethernet

IEEE 802.3ae standard for 10 Gbit/s Ethernet over fiber (10GBASE-SR, LR, ER) and copper (10GBASE-T). Common in server uplinks, spine-leaf fabric interconnects, and storage networks. Transceivers available in SFP+, XFP, and QSFP form factors. Requires Cat6A or better for 10GBASE-T over copper.

**Difficulty:** Intermediate
**Category:** Hardware


---

## XACM — XML Access Control Markup

XML-based policy language for expressing access control rules in identity federation and web service authorization frameworks. Defines subject, resource, and action-based permit/deny rules in an interoperable format, used as a precursor to the more comprehensive XACML standard.

**Difficulty:** Advanced
**Category:** Security


---

## XSCL — XML Schema Constraint Language

Formal language for expressing structural and semantic constraints on XML documents beyond what XML Schema (XSD) alone can enforce. Used in DITA, DocBook, and specialized industry schemas (HL7, SWIFT) to enforce co-occurrence constraints and cross-field validation rules.

**Difficulty:** Advanced
**Category:** Dev


---

## XFRM — Transform (IPsec)

Linux kernel IPsec framework responsible for applying Security Associations (SAs) to network packets. Handles encryption, authentication, and encapsulation transforms (ESP, AH, IPIP). Managed via ip xfrm commands (iproute2) and used internally by strongSwan, Libreswan, and WireGuard-over-IPsec implementations.

**Difficulty:** Advanced
**Category:** Security


---

## XPCM — Extended Pulse Code Modulation

PCM variant that extends the standard 8-bit, 8 kHz G.711 telephony encoding with higher sample rates (16 kHz, 32 kHz) and bit depths (16-bit) for wideband and super-wideband voice codecs. Used in VoIP systems (G.722, G.722.2/AMR-WB) to improve voice quality over HD telephony links.

**Difficulty:** Advanced
**Category:** Protocol


---

## XCON — Centralized Conferencing

IETF framework (RFC 5239) for managing multi-party multimedia conferences via SIP. Defines a centralized conference server model with a focus object (conference object), manipulation via XCAP, and event notification via SIP NOTIFY. Used in enterprise UC platforms and carrier-grade conferencing systems.

**Difficulty:** Advanced
**Category:** Protocol


---

## XMIT — Transmit

Shorthand for the transmission operation in data communications and networking. Appears in EBCDIC/mainframe contexts, hardware register names (XMIT buffers), Cisco CLI (xmit-queue-limit), and telco documentation. Refers to the outgoing direction of a link, paired with RECV (receive).

**Difficulty:** Base
**Category:** Networking


---

## XDMCP — X Display Manager Protocol

X11 protocol (X Display Manager Control Protocol) used to manage connections between X terminals and X display managers (XDM, GDM, LightDM). Operates on UDP/TCP port 177. Allows thin clients to request a graphical login session from a remote display manager over the network.

**Difficulty:** Intermediate
**Category:** Protocol


---

## XPLM — X-Plane Plugin Manager

Plugin API and SDK for X-Plane flight simulator. Allows developers to extend the simulator with custom aircraft systems, avionics, AI, and hardware integration. Used in aviation training simulators for implementing realistic flight management systems and interfacing with physical cockpit hardware.

**Difficulty:** Advanced
**Category:** Dev


---

## XSCG — Cross-Site Code Generation

Code generation attack pattern where malicious input causes a code generator, template engine, or transpiler to emit unintended executable code. Related to template injection and SSTI (Server-Side Template Injection). Mitigated by input sanitization, output encoding, and sandboxed code generation pipelines.

**Difficulty:** Advanced
**Category:** Security


---

## XAAS — X as a Service

Umbrella term for any technology capability delivered as a cloud service over a network, where X represents the resource type (Infrastructure, Platform, Software, Database, Security, Network, etc.). Encapsulates the consumption model shift from owned assets to subscription-based, on-demand provisioning (SaaS, PaaS, IaaS, DBaaS, SECaaS).

**Difficulty:** Base
**Category:** Cloud



---

## XPATH — XPath Query Language

W3C query language for selecting nodes from XML documents. Syntax: /root/child (absolute), //element (any descendant), @attr (attribute), [predicate] (filter condition). Used in XSLT, XQuery, Selenium (element locators), and XML configuration systems. XPath 2.0 adds a type system; XPath 3.1 adds maps, arrays, and JSON support.

**Difficulty:** Intermediate
**Category:** Dev

---

## XAUTH — X11 Authorization

Authentication mechanism for X Window System connections. xauth manages .Xauthority files containing MIT-MAGIC-COOKIE-1 tokens. SSH X11 forwarding (ssh -X/-Y) creates synthetic cookies preventing unauthorized local X connections. Without XAUTH any local process can connect to the X server and capture keystrokes or take screenshots.

**Difficulty:** Intermediate
**Category:** Security

---

## XMLRP — XML-RPC Protocol

Remote procedure call protocol encoding calls and responses in XML over HTTP. Simpler than SOAP: no WSDL, no namespaces. Supports basic types: int, string, boolean, double, dateTime, base64, array, struct. Used in WordPress XML-RPC API, Bugzilla, Confluence, and legacy blog publishing tools. Largely replaced by REST and gRPC in new systems.

**Difficulty:** Intermediate
**Category:** Protocol

---

## XSSER — XSS Testing Framework

Open-source penetration testing tool for discovering and exploiting Cross-Site Scripting vulnerabilities. Automates XSS payload injection, vector testing (GET, POST, cookie, HTTP header), WAF bypass detection, and result reporting. Supports DOM-based, reflected, and stored XSS testing. Used in authorized web application security assessments.

**Difficulty:** Advanced
**Category:** Security

---

## XSLTF — XSLT Transform File

XSL Transformation file (.xsl/.xslt) containing template rules for transforming XML source documents into XML, HTML, or plain text. Processors: Saxon, Xalan, libxslt. Templates match input nodes and produce output fragments. Used in data integration pipelines, document publishing workflows, and converting between XML schemas (e.g. WSDL to HTML documentation).

**Difficulty:** Intermediate
**Category:** Dev


---

## XUNIT — xUnit Testing Framework

Family of unit testing frameworks following a common architecture originally defined by SUnit (Smalltalk). Implementations exist for every major language: JUnit (Java), NUnit/.NET (C#), PyTest/unittest (Python), CppUnit (C++), RSpec (Ruby). Core concepts: test fixtures (setUp/tearDown), test cases, test suites, and test runners with assertion libraries.

**Difficulty:** Base
**Category:** Dev

---

## XFCE — Xfce Desktop Environment

Lightweight GTK-based desktop environment for Unix-like systems. Designed for low resource consumption while remaining visually complete and functionally capable. Components include Xfwm4 (window manager), Thunar (file manager), and Xfce Panel. Popular in Linux distributions targeting older hardware (Xubuntu, MX Linux) and as a lightweight alternative on full-spec systems.

**Difficulty:** Base
**Category:** OS

---

## XDGBP — XDG Base Directory Protocol

Freedesktop.org specification defining standard locations for user-specific configuration, data, and cache files on Unix systems. Defines XDG_CONFIG_HOME (~/.config), XDG_DATA_HOME (~/.local/share), XDG_CACHE_HOME (~/.cache), and XDG_RUNTIME_DIR. Applications following XDG avoid cluttering the home directory with dot-files and enable clean multi-user environments.

**Difficulty:** Intermediate
**Category:** OS
