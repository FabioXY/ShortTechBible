## JAR — Java Archive

A package file format (based on ZIP) used to aggregate Java class files, associated metadata, and resources (images, configuration) into a single distributable file. JARs can be executable (if a Main-Class manifest entry is defined), library-only, or web archives (.war). The JVM classloader reads class files directly from JARs on the classpath.

**Difficulty:** Base
**Category:** Dev

---

## JBOD — Just a Bunch Of Disks

A storage configuration where multiple physical drives are exposed to the OS as independent, unrelated volumes — with no RAID striping, mirroring, or parity. JBOD is used when data loss protection is handled at a higher layer (application-level replication, ZFS, etc.) or when maximum usable capacity per disk is needed without overhead.

**Difficulty:** Intermediate
**Category:** Hardware

---

## JDBC — Java Database Connectivity

A Java API (part of the Java SE standard library) that defines a standard interface for connecting Java applications to relational databases. JDBC drivers are provided by database vendors (PostgreSQL, MySQL, Oracle) and implement the Connection, Statement, and ResultSet interfaces, allowing the same application code to work with different databases.

**Difficulty:** Intermediate
**Category:** Database

---

## JNDI — Java Naming and Directory Interface

A Java API for accessing naming and directory services (LDAP, DNS, RMI registries, file system). JNDI became widely known due to the Log4Shell vulnerability (CVE-2021-44228), where user-supplied strings were passed to JNDI lookups, allowing remote class loading and arbitrary code execution in any application using Log4j 2.x.

**Difficulty:** Advanced
**Category:** Dev

---

## JSON — JavaScript Object Notation

A lightweight, text-based data interchange format based on a subset of JavaScript object syntax. JSON supports objects (key-value maps), arrays, strings, numbers, booleans, and null. It is the dominant format for REST API payloads, configuration files, and data serialization due to its human readability and universal parser availability.

**Difficulty:** Base
**Category:** Dev

---

## JWT — JSON Web Token

A compact, URL-safe token format (RFC 7519) consisting of three Base64URL-encoded parts separated by dots: Header.Payload.Signature. The header specifies the signing algorithm; the payload contains claims (sub, exp, iat, custom fields); the signature verifies integrity. JWTs are stateless: the server verifies the signature without database lookup, at the cost of non-revocability.

**Difficulty:** Intermediate
**Category:** Security
