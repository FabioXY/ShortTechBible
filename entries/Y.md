## YAML — YAML Ain't Markup Language

Human-readable data serialization format commonly used for configuration files and data exchange. Uses indentation for structure, supports scalars, lists, and mappings. Widely adopted in DevOps tooling: Kubernetes manifests, Ansible playbooks, GitHub Actions, Docker Compose, and Helm charts. Strict on tabs vs spaces (tabs are forbidden).

**Difficulty:** Base
**Category:** Dev


---

## YARA — Yet Another Ridiculous Acronym

Pattern-matching tool and rule language used for malware identification and threat hunting. YARA rules describe file or memory patterns using string literals, byte sequences, regular expressions, and boolean conditions. Used by SIEM platforms, EDR tools, VirusTotal, and threat intelligence workflows to classify malware families.

**Difficulty:** Intermediate
**Category:** Security


---

## YARN — Yet Another Resource Negotiator

Resource management layer introduced in Hadoop 2 to decouple cluster resource management from MapReduce execution. Consists of a ResourceManager (global scheduler), NodeManagers (per-node agents), and ApplicationMasters (per-job coordinators). Allows multiple computation frameworks (Spark, Tez, Flink) to share a single Hadoop cluster.

**Difficulty:** Intermediate
**Category:** Cloud


---

## YAST — Yet Another Setup Tool

System administration and configuration tool used in SUSE Linux Enterprise and openSUSE. Provides both a graphical (Qt/GTK) and text-based ncurses interface. Handles installation, package management (via zypper backend), network configuration, storage partitioning, firewall, and user management.

**Difficulty:** Intermediate
**Category:** OS


---

## YOLO — You Only Look Once

Family of real-time object detection neural network architectures. Uses a single convolutional network pass to simultaneously predict bounding boxes and class probabilities across the entire image, enabling detection at video frame rates. Versions from YOLOv1 to YOLOv9+ progressively improve accuracy and speed on COCO benchmarks.

**Difficulty:** Advanced
**Category:** AI


---

## YDBM — Yellowfin Database Manager

Database management and analytics platform that embeds BI, reporting, and collaborative analytics within SaaS applications. Provides white-label dashboards, self-service analytics, and REST API integration for embedding charts and reports directly in third-party applications without exposing raw database access.

**Difficulty:** Intermediate
**Category:** Database


---

## YMSG — Yahoo Messenger Protocol

Proprietary binary protocol used by Yahoo Messenger for instant messaging, presence notification, file transfer, and voice/video calls. Operated over TCP port 5050. The protocol was reverse-engineered and supported by multi-protocol clients (Pidgin, Trillian). Yahoo Messenger was discontinued in 2018.

**Difficulty:** Intermediate
**Category:** Protocol


---

## YPBR — Y-Pb-Pr Component Video

Analog component video signal format that separates a video signal into luminance (Y) and two color difference channels (Pb, Pr). Used in DVD players, game consoles, and professional video equipment for higher quality than composite or S-Video. Relevant in AV-over-IP systems and legacy capture card interfaces.

**Difficulty:** Base
**Category:** Hardware


---

## YSQL — Yugabyte SQL

PostgreSQL-compatible distributed SQL query layer in YugabyteDB. Provides full ACID transactions, joins, and stored procedures across a horizontally sharded, multi-node cluster. YSQL is distinct from YCQL (Cassandra-compatible API) in the same database, offering familiarity for PostgreSQL developers.

**Difficulty:** Advanced
**Category:** Database


---

## YTDL — YouTube Downloader

Command-line tool (yt-dlp, originally youtube-dl) for downloading video and audio content from YouTube and hundreds of other video platforms. Supports format selection, subtitle extraction, playlist downloads, and post-processing via FFmpeg. Written in Python; invoked as yt-dlp [options] URL.

**Difficulty:** Base
**Category:** Dev


---

## YDEV — Yard Device (YardStick One)

Open-source sub-GHz RF transceiver hardware used for testing and attacking wireless protocols below 1 GHz (433 MHz, 868 MHz, 915 MHz). Used in security research to capture, replay, and analyze signals from garage doors, remote controls, car key fobs, and ISM-band IoT devices.

**Difficulty:** Advanced
**Category:** Security


---

## YCBR — Y-Cb-Cr Color Space

Digital color encoding format used in video compression and display systems. Separates luminance (Y) from blue-difference (Cb) and red-difference (Cr) chroma channels, allowing chroma subsampling (4:2:0, 4:2:2, 4:4:4) to reduce bandwidth without significant perceptual quality loss. Used in JPEG, H.264, H.265, and broadcast standards.

**Difficulty:** Intermediate
**Category:** Hardware


---

## YDNS — Dynamic DNS Service

DNS provider specializing in dynamic DNS (DDNS) that maps a hostname to a frequently changing IP address. Clients run a local agent or use router DDNS support to update the DNS record whenever the ISP-assigned IP changes. Used for self-hosted services on residential connections without a static IP.

**Difficulty:** Base
**Category:** Networking


---

## YMAN — Your Management Area Network

Informal term used in enterprise documentation for the management network plane dedicated to out-of-band device administration (IPMI, iDRAC, iLO, console servers). Kept logically separate from the production network to ensure management access even when production interfaces fail.

**Difficulty:** Intermediate
**Category:** Networking


---

## YGGD — Yggdrasil Network

Experimental end-to-end encrypted IPv6 overlay network using a distributed spanning tree routing algorithm. Assigns addresses based on cryptographic public keys, eliminating centralized routing authorities. Designed as a self-organizing, scalable mesh for decentralized networking research.

**Difficulty:** Advanced
**Category:** Networking


---

## YPCA — Yellow Pages Certificate Authority

Legacy informal term for directory-integrated certificate authorities in early enterprise PKI deployments that coupled certificate issuance with LDAP/NIS directory services. Enrollment, revocation, and distribution were managed through directory queries rather than dedicated OCSP or CRL infrastructure.

**Difficulty:** Advanced
**Category:** Security


---

## YKNF — Yokohama Key Network Framework

IEEE P1906.1-inspired nanonetwork framework for defining communication architectures at the nanoscale. Addresses channel modeling, modulation, and protocol design for molecular, electromagnetic, and acoustic nanonetworks in biomedical and materials science applications.

**Difficulty:** Advanced
**Category:** Networking


---

## YTFS — YottaByte File System

Theoretical file system design concept addressing storage at the yottabyte (10^24 bytes) scale. Explores metadata indexing, distributed namespace management, and consistency models for petascale-to-exascale object stores. Referenced in academic research on future-scale distributed storage architecture.

**Difficulty:** Advanced
**Category:** OS


---

## YRTP — Yield-Responsive Traffic Policy

QoS policy mechanism that dynamically adjusts bandwidth allocation based on real-time traffic demand and link utilization. High-priority flows hold guaranteed minimums but yield excess capacity to lower-priority flows during idle periods. Reduces over-provisioning while maintaining SLA commitments.

**Difficulty:** Advanced
**Category:** Networking


---

## YIDL — Yet another Interface Description Language

Informal category term for IDL variants beyond CORBA IDL and Microsoft IDL. Encompasses Protocol Buffers .proto files, Thrift IDL, Avro Schema, FlatBuffers, and Cap'n Proto schema files. Each defines RPC service interfaces and data structures for generating typed client/server stubs in multiple languages.

**Difficulty:** Intermediate
**Category:** Dev


---

## YCQL — Yugabyte Cassandra Query Language

Cassandra-compatible API in YugabyteDB that provides CQL syntax over a distributed, strongly consistent storage engine. Unlike Apache Cassandra (eventual consistency), YCQL in YugabyteDB uses Raft-based replication, offering tunable consistency while maintaining API compatibility with existing Cassandra applications.

**Difficulty:** Advanced
**Category:** Database


---

## YAPP — Yet Another Push Protocol

Generic term applied to various proprietary or experimental server-push notification protocols developed before WebSockets and SSE became standard. Examples include Comet, long-polling adaptations, and custom TCP-based push daemons. The term is used in protocol comparison literature to highlight protocol proliferation.

**Difficulty:** Intermediate
**Category:** Protocol


---

## YTCP — YAMI Transfer Control Protocol

Proprietary messaging protocol in the YAMI4 (Yet Another Messaging Infrastructure) library. Provides reliable, ordered delivery of structured messages between C++, Java, and Python processes. Used as a lightweight alternative to AMQP or ZeroMQ in embedded and HPC messaging scenarios.

**Difficulty:** Advanced
**Category:** Protocol


---

## YAPS — Yet Another Proxy Server

Informal designation for lightweight or minimal HTTP/HTTPS proxy implementations. The term appears in project names and documentation to distinguish small, single-purpose proxy tools from enterprise platforms. Examples include simple Python-based MITM proxies used in security testing and API development workflows.

**Difficulty:** Intermediate
**Category:** Networking


---

## YARD — Yet Another Ruby Documentation

Documentation generation tool for Ruby code. Parses inline Ruby comments with a structured tag syntax (@param, @return, @raise, @example) to generate HTML, JSON, and plaintext API documentation. More expressive than RDoc; used by most Ruby gems and Rails projects for public API documentation.

**Difficulty:** Intermediate
**Category:** Dev


---

## YOLZ — You Only Look Zero-shot

Emerging object detection paradigm that applies zero-shot learning to YOLO-family architectures. Enables detection of object categories not seen during training by leveraging text-image embeddings (CLIP, ALIGN). Relevant in open-vocabulary detection tasks where annotating every possible class is impractical.

**Difficulty:** Advanced
**Category:** AI


---

## YMIR — Yield Management and Infrastructure Reporting

IT operations reporting framework for correlating infrastructure capacity metrics with service delivery costs and business outcomes. Integrates data from hypervisors, cloud billing APIs, and APM tools to produce chargeback reports and capacity forecasts for IT finance management.

**Difficulty:** Advanced
**Category:** Cloud


---

## YNIX — Y-Network Interface Extension

Abstraction layer in some network virtualization stacks that extends the standard network interface model with Y-branching topology support. Allows a single virtual interface to simultaneously connect to multiple network segments, used in test bed environments for traffic duplication and analysis.

**Difficulty:** Advanced
**Category:** Networking


---

## YPRM — Yum Package Repository Manager

Backend component of the Yum (Yellowdog Updater Modified) and DNF package management systems on Red Hat-based Linux distributions. Manages repository metadata caching (repomd.xml, primary.sqlite), dependency resolution, and GPG signature verification for RPM packages. Configured via /etc/yum.repos.d/.

**Difficulty:** Intermediate
**Category:** OS


---

## YOTT — Yottabyte

Unit of digital storage equal to 10^24 bytes (SI) or 2^80 bytes (binary, also written YiB). The largest named standard prefix for byte quantities. Relevant in discussions of global internet traffic scale, future storage architectures, and theoretical limits of distributed file systems. No commercial storage system currently operates at this scale.

**Difficulty:** Base
**Category:** Hardware


---

## YAFE — Yet Another Front-End

Informal term for new JavaScript frameworks and build tools that emerge in rapid succession in the web development ecosystem. Reflects the high churn rate of frontend tooling: from Grunt/Gulp to Webpack to Vite to Turbopack. Used in developer discourse to highlight framework fatigue and toolchain complexity.

**Difficulty:** Base
**Category:** Dev


---

## YLOG — Yum Transaction Log

Log file maintained by Yum/DNF recording all package installation, update, and removal operations with timestamps and user context. Located at /var/log/dnf.log (DNF) or /var/log/yum.log (legacy Yum). Used for auditing package changes, rollback planning, and compliance reporting on RPM-based systems.

**Difficulty:** Base
**Category:** OS


---

## YPRX — YAMI Proxy

Proxy component in the YAMI4 messaging library that forwards messages between endpoints in different network segments or transport types (TCP, UDP, Unix sockets). Enables message routing without requiring direct connectivity between all participants in a distributed messaging topology.

**Difficulty:** Advanced
**Category:** Networking


---

## YKMS — YubiKey Management Suite

Administrative toolset for managing YubiKey hardware authentication tokens at scale. Handles key provisioning, PIN policy enforcement, certificate enrollment (PIV slots), OATH credential loading, and remote attestation verification. Used in enterprise MFA deployments and FIDO2 security key rollouts.

**Difficulty:** Intermediate
**Category:** Security


---

## YENC — Y-Encoder

Binary-to-text encoding scheme used in Usenet newsgroups to transfer binary files (images, archives, executables) over text-based NNTP. Encodes each byte by adding 42 modulo 256, escaping only three special characters. More efficient than uuencoding (~98% efficiency vs ~75%), with integrated CRC32 checksums for error detection.

**Difficulty:** Intermediate
**Category:** Protocol


---

## YSTR — YAML Stream

Sequence of multiple YAML documents within a single file or network stream, separated by the --- document start marker. Used in Kubernetes to bundle multiple resource manifests in a single file applied with kubectl apply -f, and in Ansible to chain multiple plays in a single playbook file.

**Difficulty:** Intermediate
**Category:** Dev


---

## YWAF — YAML-defined Web Application Firewall

WAF configuration model where all rule sets, IP blocklists, rate limits, and routing policies are expressed as declarative YAML files and managed through GitOps pipelines. Implemented in tools like Coraza YAML ruleset loaders and cloud-native WAF configurations (AWS WAF via CloudFormation/Terraform YAML).

**Difficulty:** Advanced
**Category:** Security


---

## YRFC — YAMI Request/Response Framework

Request-response communication pattern implemented in the YAMI4 messaging library. Provides synchronous and asynchronous RPC semantics over the YAMI transport layer. Used in scientific computing and simulation environments where lightweight, low-overhead IPC between processes is preferred over full AMQP or gRPC stacks.

**Difficulty:** Advanced
**Category:** Dev


---

## YTLS — YAML-Template Language System

Templating subsystem that processes YAML configuration files with variable substitution, conditional blocks, and loop constructs before applying them to a target system. Implemented in Helm (Go templates over YAML), Kustomize (patch overlays), and Jinja2-rendered Ansible tasks, enabling reusable parameterized infrastructure definitions.

**Difficulty:** Intermediate
**Category:** Dev


---

## YNMS — Yum/DNF Network Management Script

Automation script that wraps Yum or DNF commands to orchestrate coordinated package updates across multiple servers via SSH. Handles pre-update snapshots, rollback triggers on failure, and post-update health checks. Used in environments without a full configuration management platform (Ansible, Puppet) for managed patching workflows.

**Difficulty:** Intermediate
**Category:** OS



---

## YCBCR — YCbCr Color Space

Digital color encoding separating luminance (Y) from blue-difference (Cb) and red-difference (Cr) chroma channels. Allows chroma subsampling (4:2:0, 4:2:2, 4:4:4) to reduce bandwidth without significant perceptual quality loss. Used in JPEG compression, H.264, H.265, AV1, and broadcast video standards (BT.601, BT.709, BT.2020).

**Difficulty:** Intermediate
**Category:** Hardware


---

## YACC — Yet Another Compiler Compiler

LALR(1) parser generator developed at Bell Labs. Takes a grammar specification in BNF-like notation and produces a C parser that recognizes the language defined by that grammar. Paired with Lex (lexer generator). GNU Bison is the modern compatible replacement. Historical importance: used to build the original Unix C compiler (cc) and many subsequent language parsers.

**Difficulty:** Advanced
**Category:** Dev

---

## YAJL — Yet Another JSON Library

Streaming SAX-style JSON parser written in C with a minimal footprint. Designed for parsing arbitrarily large JSON documents without loading the entire document into memory. Provides callback-based event notifications (string, number, boolean, null, array start/end, map start/end). Used in systems-level applications where memory allocation must be tightly controlled.

**Difficulty:** Advanced
**Category:** Dev
