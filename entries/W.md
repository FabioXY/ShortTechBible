## WAF — Web Application Firewall

A security appliance or software layer that monitors, filters, and blocks HTTP/HTTPS traffic to and from a web application. Unlike a network firewall (IP/port rules), a WAF understands HTTP and inspects request/response content for attack patterns: SQL injection, XSS, CSRF, path traversal, and OWASP Top 10 threats. WAFs operate in detection mode (log only) or prevention mode (block).

**Difficulty:** Intermediate
**Category:** Security

---

## WAN — Wide Area Network

A telecommunications network that extends over a large geographic area, connecting LANs across cities, countries, or continents. WANs use leased lines (MPLS, SD-WAN), the public internet, or point-to-point links (satellite, microwave). The internet is the world's largest WAN. WAN links have higher latency and lower bandwidth than LAN connections due to the physical distances involved.

**Difficulty:** Base
**Category:** Networking

---

## WLAN — Wireless Local Area Network

A LAN that uses radio waves (IEEE 802.11) instead of cables to connect devices. WLAN operates in the 2.4 GHz (longer range, more interference) and 5 GHz (shorter range, higher throughput) bands; Wi-Fi 6E and Wi-Fi 7 add 6 GHz. WLAN security relies on WPA2 (AES/CCMP) or WPA3 (SAE handshake, forward secrecy). The access point bridges wireless clients to the wired network.

**Difficulty:** Base
**Category:** Networking

---

## WSUS — Windows Server Update Services

A Microsoft server role that downloads Windows updates from Microsoft Update and distributes them to managed clients within an organization. WSUS allows administrators to approve, test, and schedule updates before deployment, reducing internet bandwidth consumption and giving control over the patch lifecycle. Managed via Group Policy or SCCM/Intune in larger environments.

**Difficulty:** Intermediate
**Category:** OS

---

## WPAD — Web Proxy Autodiscovery Protocol

A method for clients to automatically discover the URL of a proxy configuration file (PAC file) using DHCP option 252 or DNS resolution of the hostname "wpad". The client fetches the PAC file and uses it to determine which requests should go through a proxy. WPAD has well-documented security vulnerabilities (DNS hijacking, man-in-the-middle) and is disabled by default in modern browsers.

**Difficulty:** Advanced
**Category:** Networking

---

## WMI — Windows Management Instrumentation

Microsoft's implementation of WBEM (Web-Based Enterprise Management), providing a standardized interface for querying and managing Windows system components: hardware inventory, running processes, services, event logs, registry, and performance counters. WMI queries use WQL (a SQL-like language). Heavily used by sysadmins, monitoring tools, and attackers for lateral movement and persistence.

**Difficulty:** Intermediate
**Category:** OS
