## JAR — Java Archive

ZIP-based package format that bundles compiled Java class files, metadata, and
resources into a single distributable file. JARs are the primary unit of
deployment for Java libraries, applications, and OSGi bundles. Executable JARs
include a manifest specifying the Main-Class entry point.

**Difficulty:** Base
**Category:** Dev

---

## JAXB — Java Architecture for XML Binding

Standard API for converting Java objects to XML (marshalling) and XML back to
Java objects (unmarshalling). Uses annotations to map class fields to XML
elements and attributes. Removed from JDK in Java 11 and distributed as a
standalone Jakarta EE component; Gradle/Maven dependency required.

**Difficulty:** Intermediate
**Category:** Dev

---

## JAXP — Java API for XML Processing

Java API providing a pluggable interface for XML parsing and transformation.
Supports DOM (tree-based), SAX (event-driven), and StAX (streaming pull) parsing
models, plus XSLT transformations. Allows switching XML processor implementations
(Xerces, Saxon) without modifying application code.

**Difficulty:** Intermediate
**Category:** Dev

---

## JBOD — Just a Bunch of Disks

Storage configuration presenting multiple drives to the OS as independent volumes
with no RAID striping, mirroring, or parity. Maximizes usable capacity with zero
overhead but provides no redundancy. A drive failure loses only data on that
specific drive, not the entire array.

**Difficulty:** Base
**Category:** Hardware

---

## JDBC — Java Database Connectivity

Standard Java API (javax.sql) providing a uniform interface for connecting to
relational databases regardless of vendor. Applications load a vendor-specific
driver, then use common JDBC classes to execute queries, handle result sets,
manage transactions, and work with prepared statements safely.

**Difficulty:** Intermediate
**Category:** Dev

---

## JCOP — Java Card Open Platform

Smart card operating system implementing the Java Card specification. Allows
multiple isolated applets to be installed on a single chip. Used in SIM cards,
EMV banking cards, and identity documents. Applets run in a constrained Java
subset on hardware with only a few kilobytes of RAM.

**Difficulty:** Advanced
**Category:** Security

---

## JCE — Java Cryptography Extension

Framework within the Java Security API providing encryption, key generation, key
agreement, and MAC algorithms. Pluggable provider architecture allows third-party
implementations like Bouncy Castle to extend or replace default JDK algorithms
without requiring application code changes.

**Difficulty:** Advanced
**Category:** Security

---

## JDWP — Java Debug Wire Protocol

Protocol for communication between a JVM debugger front-end and the target JVM.
Transmitted over a socket or shared memory transport. IDEs connect via JDWP to
set breakpoints, inspect variables, evaluate expressions, and step through code
in remote, containerized, or local JVM processes.

**Difficulty:** Advanced
**Category:** Dev

---

## JDK — Java Development Kit

Complete software package for developing Java applications. Includes the JRE
(runtime), compiler (`javac`), archiver (`jar`), debugger (`jdb`), documentation
generator (`javadoc`), and diagnostic tools (`jmap`, `jstack`, `jcmd`). Oracle
JDK and OpenJDK are the main distributions.

**Difficulty:** Base
**Category:** Dev

---

## JFET — Junction Field-Effect Transistor

Semiconductor device where current through a channel is controlled by a
reverse-biased p-n junction gate rather than an insulated gate as in MOSFETs.
JFETs exhibit low noise and are used in amplifier input stages and analog RF
circuits. Less common in digital logic than MOSFETs.

**Difficulty:** Advanced
**Category:** Hardware

---

## JFFS — Journaling Flash File System

Log-structured filesystem designed for NAND and NOR flash memory in embedded
Linux systems. Performs wear leveling across flash erase blocks and provides
crash consistency through journaling. Superseded by JFFS2 and then UBIFS for
large NAND devices requiring better garbage collection performance.

**Difficulty:** Advanced
**Category:** OS

---

## JFIF — JPEG File Interchange Format

Container wrapping raw JPEG-compressed image data with standardized metadata
headers. Defines how to store color space, pixel aspect ratio, and optional
thumbnails. Most files with `.jpg` or `.jpeg` extensions are technically JFIF
files rather than raw JPEG bitstreams.

**Difficulty:** Intermediate
**Category:** Dev

---

## JIT — Just-In-Time Compilation

Runtime optimization technique that compiles bytecode or interpreted code to
native machine instructions at execution time, after profiling identifies hot
paths. Provides near-native performance for managed runtimes like JVM and .NET
CLR without requiring full ahead-of-time compilation.

**Difficulty:** Intermediate
**Category:** Dev

---

## JMAP — Java Memory Analysis Tool

JDK diagnostic command that generates heap dumps, prints class histograms,
and reports live object statistics for a running JVM process. Output is analyzed
with Eclipse MAT or VisualVM to identify memory leaks and excessive object
retention. Equivalent to `jcmd <pid> GC.heap_dump` in modern JDKs.

**Difficulty:** Intermediate
**Category:** Dev

---

## JMX — Java Management Extensions

Java technology for managing and monitoring applications via standardized
Management Beans (MBeans). MBeans expose attributes and operations accessible
through JConsole, VisualVM, or remote JMX clients. Widely used for tuning JVM
garbage collection parameters and monitoring thread pool health at runtime.

**Difficulty:** Intermediate
**Category:** Dev

---

## JMS — Java Message Service

Jakarta EE API defining a standard interface for message-oriented middleware.
Supports point-to-point (queues) and publish/subscribe (topics) messaging models.
Implementations include ActiveMQ, IBM MQ, and HornetQ. Decouples producers from
consumers and enables reliable asynchronous communication between enterprise components.

**Difficulty:** Intermediate
**Category:** Dev

---

## JNI — Java Native Interface

Framework enabling Java code to call and be called by native C or C++ libraries.
Used for performance-critical operations requiring direct hardware access or when
wrapping existing native code. Bypasses JVM memory safety guarantees, making JNI
a frequent source of crashes and security vulnerabilities.

**Difficulty:** Advanced
**Category:** Dev

---

## JNDI — Java Naming and Directory Interface

Java API for interacting with naming and directory services such as LDAP, DNS,
and RMI registries. Allows applications to look up objects by name at runtime
without hardcoding connection details. Became critical security knowledge in 2021
when Log4Shell exploited JNDI lookups for remote code execution via Log4j.

**Difficulty:** Advanced
**Category:** Dev

---

## JNLP — Java Network Launch Protocol

XML-based file format used by Java Web Start to launch and update Java applications
from a web server. Specifies resources, JVM version requirements, security
permissions, and update policy. Deprecated in Java 9 and removed in Java 11;
replaced by native application installers and modern browser-based deployment.

**Difficulty:** Intermediate
**Category:** Dev

---

## JPA — Java Persistence API

Jakarta EE specification defining a standard ORM interface for Java. Maps Java
objects to relational tables using annotations or XML descriptors. JPA is the
specification; Hibernate and EclipseLink are the dominant implementations.
Manages entity lifecycle, lazy loading relationships, and JPQL queries.

**Difficulty:** Intermediate
**Category:** Dev

---

## JPDA — Java Platform Debugger Architecture

Unified debugging architecture comprising three layers: JVM TI (native profiling
and event API), JDWP (wire protocol), and JDI (high-level Java debugger API).
IDEs and APM tools use JDWP/JDI to control execution, set breakpoints, and
inspect state of local or remote JVM processes.

**Difficulty:** Advanced
**Category:** Dev

---

## JPEG — Joint Photographic Experts Group

Lossy image compression standard (ISO/IEC 10918) for continuous-tone photographs.
Applies a Discrete Cosine Transform to 8×8 pixel blocks, quantizes coefficients
based on a quality setting, then applies Huffman coding. Increasing compression
ratios introduce visible blocking and ringing artifacts around sharp edges.

**Difficulty:** Intermediate
**Category:** Dev

---

## JPQL — Java Persistence Query Language

Object-oriented query language defined by the JPA specification. Operates on
entity objects and their mapped relationships rather than raw database tables.
Database-agnostic: the JPA provider translates JPQL to the target SQL dialect
at runtime, allowing seamless switching between database vendors.

**Difficulty:** Intermediate
**Category:** Dev

---

## JRE — Java Runtime Environment

Software package required to run compiled Java applications. Contains the JVM,
core class libraries, and supporting binaries but not the compiler or development
tools. The JDK is a strict superset of the JRE. Starting with Java 9, modular
JREs can be created with only the required modules using `jlink`.

**Difficulty:** Base
**Category:** Dev

---

## JRMP — Java Remote Method Protocol

Wire protocol used by Java RMI for communication between JVMs on different hosts.
Transmits serialized Java objects over TCP. JRMP is the default RMI transport;
IIOP is an alternative enabling interoperability with CORBA systems. Historically
exploited via Java deserialization attacks targeting RMI endpoints.

**Difficulty:** Advanced
**Category:** Dev

---

## JSON — JavaScript Object Notation

Lightweight, human-readable data interchange format based on a subset of JavaScript
syntax. Supports objects (key-value pairs), arrays, strings, numbers, booleans,
and null. Dominant format for REST APIs and configuration files. More compact
binary alternatives include CBOR and MessagePack for performance-critical paths.

**Difficulty:** Base
**Category:** Dev

---

## JOSE — JSON Object Signing and Encryption

Framework of IETF standards (RFCs 7515-7518) defining cryptographic operations
on JSON data. Includes JWS (signing), JWE (encryption), JWK (key representation),
and JWA (algorithm identifiers). Forms the cryptographic foundation for JWT tokens
and is central to OAuth 2.0 and OpenID Connect token security.

**Difficulty:** Advanced
**Category:** Security

---

## JSF — JavaServer Faces

Component-based web UI framework for Jakarta EE applications. Developers build
UIs from reusable UI components backed by managed beans, with lifecycle management
handled by the framework. PrimeFaces and OmniFaces are popular component libraries.
Largely superseded by modern SPA frameworks in new development.

**Difficulty:** Intermediate
**Category:** Dev

---

## JSP — JavaServer Pages

Server-side Java technology allowing developers to embed Java code within HTML
using scriptlets and tag libraries. The JSP is compiled to a servlet on first
request. Largely replaced by Thymeleaf, FreeMarker, and modern front-end frameworks,
but still present in legacy enterprise Java web applications.

**Difficulty:** Intermediate
**Category:** Dev

---

## JSSE — Java Secure Socket Extension

Framework implementing SSL and TLS within the Java Security API. Provides
`SSLSocket`, `SSLServerSocket`, and `SSLEngine` (non-blocking NIO). Supports
configurable cipher suites, server certificate validation, and mutual TLS for
client authentication in Java HTTPS and secure socket applications.

**Difficulty:** Advanced
**Category:** Security

---

## JTAG — Joint Test Action Group

IEEE 1149.1 standard defining a serial interface for testing PCBs and programming
embedded devices. Uses TDI, TDO, TCK, and TMS signal lines. A JTAG debug probe
allows reading and writing CPU registers, setting hardware breakpoints, and
flashing firmware directly without requiring a software bootloader.

**Difficulty:** Advanced
**Category:** Hardware

---

## JWT — JSON Web Token

Compact, URL-safe token format (RFC 7519) with three Base64URL-encoded sections:
header (algorithm), payload (claims), and signature. Used for stateless authentication:
the server signs the token and the client presents it on each request; the server
validates the signature without querying a session store.

**Difficulty:** Intermediate
**Category:** Security

---

## JVM — Java Virtual Machine

Abstract computing machine that executes Java bytecode, providing platform
independence by translating bytecode to native instructions at runtime. Modern
JVMs (HotSpot, GraalVM) include a JIT compiler, generational garbage collector,
and thread scheduler. Also runs Kotlin, Scala, Groovy, and Clojure.

**Difficulty:** Intermediate
**Category:** Dev

---

## JXTA — Juxtapose Peer-to-Peer Protocol

Open P2P protocol framework initiated by Sun Microsystems in 2001. Defined XML-based
protocols allowing heterogeneous devices to form ad-hoc peer groups, advertise
services, and exchange messages without central servers. Discontinued, but its
concepts influenced modern DHT-based decentralized networking systems.

**Difficulty:** Advanced
**Category:** Networking

---

## JAIN — Java APIs for Integrated Networks

Suite of Java APIs enabling development of intelligent network services and signaling
protocol stacks. Covers SIP (JAIN SIP), SS7 (JAIN SS7), and MGCP for building
carrier-grade Java telecom applications including softswitches, IVR systems,
and VoIP infrastructure components.

**Difficulty:** Advanced
**Category:** Networking

---

## JLAN — Java LAN Server

Open-source pure-Java implementation of the CIFS/SMB file server protocol. Allows
Java applications to expose file shares accessible by Windows clients over the
network. Used in enterprise content management systems where SMB file access
must coexist with a Java application server tier.

**Difficulty:** Advanced
**Category:** Networking

---

## JPOX — Java Persistent Objects

Early open-source JDO (Java Data Objects) implementation that later evolved into
the DataNucleus project. Provided ORM capabilities before JPA became dominant,
and uniquely supported non-relational backing stores including LDAP and object
databases alongside traditional RDBMS.

**Difficulty:** Advanced
**Category:** Dev

---

## JRSS — Joint Regional Security Stacks

United States DoD architecture consolidating cybersecurity infrastructure across
regional network access points. Centralizes firewalls, IDS/IPS, and security
monitoring into shared stacks rather than per-agency deployments, reducing total
attack surface and improving cross-domain visibility.

**Difficulty:** Advanced
**Category:** Security

---

## JTLS — Joint Theater Level Simulation

High-level military wargaming simulation used for operational planning and training.
Relevant to IT infrastructure in defense environments requiring integration with
military simulation frameworks and strict handling of classified data with mandatory
access controls, audit logging, and compartmentalization.

**Difficulty:** Advanced
**Category:** Security

---

## JLOG — Journal Log
Structured, append-only log format used in some messaging and replication systems (e.g. OmniTI's Jlog library) to provide durable, multi-subscriber log consumption. Subscribers maintain independent read positions; data is retained until all subscribers have consumed it. Used in Resmon and other monitoring infrastructure.
**Difficulty:** Advanced
**Category:** Dev
