## XMPP — Extensible Messaging and Presence Protocol

An open standard (RFC 6120) for real-time messaging based on XML streams. XMPP uses a federated architecture where servers communicate using server-to-server (S2S) dialback, similar to email. It supports presence (online/offline/away), roster management, and is extensible via XEPs (XMPP Extension Protocols). Used by WhatsApp (historically), Jabber, and many enterprise chat systems.

**Difficulty:** Intermediate
**Category:** Protocol

---

## XSLT — Extensible Stylesheet Language Transformations

A language for transforming XML documents into other XML documents, HTML, plain text, or other formats. An XSLT stylesheet defines template rules that match XML nodes and produce output. XSLT processors are Turing-complete and can perform complex transformations. Used in document processing pipelines, web services, and configuration generation from XML data sources.

**Difficulty:** Intermediate
**Category:** Dev

---

## XSS — Cross-Site Scripting

A web security vulnerability where an attacker injects malicious client-side scripts into web pages viewed by other users. Stored XSS persists in the database; reflected XSS is in a URL parameter echoed back immediately; DOM-based XSS manipulates the DOM client-side without server involvement. Mitigated by output encoding, Content Security Policy (CSP), and avoiding innerHTML.

**Difficulty:** Intermediate
**Category:** Security

---

## XACL — Extended Access Control List

An extended variant of traditional ACLs that supports additional match criteria beyond basic IP/port rules, such as MAC addresses, DSCP values, protocol fields, or user identity (in identity-aware firewalls). The exact feature set varies by vendor and platform. XACLs are used in environments where standard ACL capabilities are insufficient for granular traffic classification.

**Difficulty:** Advanced
**Category:** Security

---

## XDCR — Cross Data Center Replication

A Couchbase-specific feature for replicating data between Couchbase buckets across geographically distributed data centers. XDCR operates asynchronously using a push model, enabling active-active or active-passive multi-region topologies. Conflict resolution is handled by document revision (sequence number) or timestamp. Represents a pattern now generalized across distributed databases.

**Difficulty:** Advanced
**Category:** Database

---

## XSRF — Cross-Site Request Forgery

An alternative acronym for CSRF (Cross-Site Request Forgery), used interchangeably in web security literature. XSRF appears in some frameworks' anti-forgery token implementations (e.g., ASP.NET uses "XSRF token" in its documentation). The attack, mitigations, and principles are identical to those described under CSRF. See CSRF for the canonical entry.

**Difficulty:** Intermediate
**Category:** Security
