## KABI — Kernel Application Binary Interface

Stable interface between the Linux kernel and loadable kernel modules or user-space
programs. Kernel developers aim to preserve KABI across minor releases so that
out-of-tree drivers do not need recompilation. Enterprise Linux distributions
(RHEL, SLES) provide explicit KABI stability guarantees with each major release.

**Difficulty:** Advanced
**Category:** OS

---

## KASM — Kernel Address Space Mapping

Refers to the organization of the kernel's virtual address space in OS memory
management. The kernel occupies a fixed region of the virtual address map (upper
half in 64-bit Linux). KASLR randomizes the base of this mapping at boot to
prevent exploitation of hardcoded kernel symbol addresses.

**Difficulty:** Advanced
**Category:** OS

---

## KASL — Kernel Address Space Layout

Base virtual address at which the kernel image is loaded in memory. KASLR
(Kernel Address Space Layout Randomization) randomizes this value at each boot,
making it significantly harder for exploits to target fixed kernel symbols.
Entropy is sourced from firmware-provided random values or hardware timing.

**Difficulty:** Advanced
**Category:** OS

---

## KCFI — Kernel Control Flow Integrity

Security mitigation that restricts indirect branches in kernel code to valid
targets, preventing attackers from hijacking control flow by overwriting function
pointers. Implemented in Linux via Clang's CFI sanitizer when building the kernel
with compiler-based CFI support on arm64 and x86-64 architectures.

**Difficulty:** Advanced
**Category:** Security

---

## KCOV — Kernel Coverage

Linux kernel subsystem providing code coverage information for fuzzing. When
enabled, it records which kernel code paths are exercised by each system call,
allowing fuzzers like syzkaller to guide input generation toward unexplored
code paths and discover kernel bugs more efficiently.

**Difficulty:** Advanced
**Category:** OS

---

## KDC — Key Distribution Center

Central authentication server in a Kerberos deployment. Combines the Authentication
Server (AS), which issues Ticket-Granting Tickets (TGT), and the Ticket-Granting
Server (TGS), which issues service tickets. All Kerberos authentication flows
through the KDC; its compromise affects every protected service in the realm.

**Difficulty:** Advanced
**Category:** Security

---

## KDF — Key Derivation Function

Cryptographic algorithm that derives secret keys from a master secret or password.
Adds computational cost (PBKDF2, bcrypt, Argon2) to slow brute-force attacks
on password hashes. Also used in key agreement protocols (HKDF) to produce
session keys from Diffie-Hellman shared secrets.

**Difficulty:** Advanced
**Category:** Security

---

## KDMP — Kernel Dump

Mechanism that captures kernel memory when a system crashes or panics. On Linux,
kdump uses a secondary crash kernel loaded at boot into reserved memory that
survives the crash event. The captured dump is analyzed offline with `crash`
and `gdb` to identify the exact code path and root cause.

**Difficulty:** Advanced
**Category:** OS

---

## KERN — Kernel

Core component of an operating system managing hardware resources and providing
services to user-space processes. Handles process scheduling, memory management,
device drivers, system calls, and IPC. Kernel architectures: monolithic (Linux),
microkernel (QNX, Mach), and hybrid (Windows NT, macOS XNU).

**Difficulty:** Base
**Category:** OS

---

## KERS — Kernel Event Recording System

Generic term for kernel-level event tracing infrastructure used for debugging
and performance analysis. In Linux, this role is fulfilled by ftrace, perf_events,
and eBPF. Captured events include context switches, page faults, system calls,
and hardware performance counter overflows.

**Difficulty:** Advanced
**Category:** OS

---

## KEXT — Kernel Extension

macOS mechanism for loading driver code into kernel space at runtime. KEXTs run
with full kernel privileges and cause system panics when they malfunction. Apple
deprecated KEXTs in macOS 10.15 Catalina, requiring vendors to migrate to
DriverKit, which runs drivers in user space with hardware entitlements.

**Difficulty:** Advanced
**Category:** OS

---

## KGDB — Kernel GDB

Built-in Linux kernel debugger that allows connecting a remote GDB instance to
a live or crashed kernel over a serial port or network (kgdboe over Ethernet).
Supports setting breakpoints, inspecting kernel variables, and stepping through
kernel code. Requires compiling the kernel with `CONFIG_KGDB=y`.

**Difficulty:** Advanced
**Category:** OS

---

## KGD — Known Good Die

Semiconductor quality term for a tested and verified bare die confirmed functional
before assembly into a multi-chip package or system-in-package. Testing bare
dies is more challenging than packaged chips; KGD programs ensure only functional
dies are committed to expensive advanced packaging processes.

**Difficulty:** Advanced
**Category:** Hardware

---

## KGID — Kernel Group ID

Kernel-internal representation of a group identifier used in the Linux security
model. Distinct from user-space GID in that it tracks namespace mappings in
containerized environments. The kernel uses KGID internally while translating
to namespace-relative GIDs when returning values to user-space processes.

**Difficulty:** Advanced
**Category:** OS

---

## KISS — Keep It Simple, Stupid

Design principle stating that systems work best when built simply. Applied in
software architecture to avoid over-engineering, unnecessary abstractions, and
premature optimization. Closely related to YAGNI (You Aren't Gonna Need It)
and directly counters gold-plating tendencies in software development teams.

**Difficulty:** Base
**Category:** Dev

---

## KLOC — Kilo Lines of Code

Unit of software size measurement equal to one thousand source lines of code.
Historically used to estimate development cost and defect density. Criticized
as a productivity metric because it incentivizes verbosity over quality. Replaced
in modern practice by story points, function points, and cycle time metrics.

**Difficulty:** Base
**Category:** Dev

---

## KMIP — Key Management Interoperability Protocol

OASIS standard defining a communication interface between enterprise key management
systems and cryptographic clients. Allows applications to request key creation,
retrieval, and lifecycle operations from any KMIP-compliant KMS without vendor
lock-in. Widely used in storage encryption and HSM integrations.

**Difficulty:** Advanced
**Category:** Security

---

## KMAP — Kernel Map

Linux kernel function (`kmap()`) that creates a temporary virtual address mapping
for a physical memory page in the high-memory region (32-bit systems). Necessary
when the kernel needs to access memory beyond the directly-mapped low-memory
zone. On 64-bit systems, all physical memory is directly addressable so kmap
is a no-op.

**Difficulty:** Advanced
**Category:** OS

---

## KMOD — Kernel Module

Loadable object file extending Linux kernel functionality at runtime without
rebooting. Modules implement device drivers, filesystems, and network protocols.
Commands: `insmod` (load), `rmmod` (remove), `lsmod` (list), `modprobe` (load
with automatic dependency resolution). Signed modules prevent unauthorized injection.

**Difficulty:** Intermediate
**Category:** OS

---

## KMS — Key Management Service

Centralized system for creating, storing, rotating, and auditing cryptographic
keys. Cloud implementations (AWS KMS, GCP Cloud KMS, Azure Key Vault) use
hardware security modules for key storage with fine-grained access policies
and automatic rotation. Applications reference key IDs rather than raw key material.

**Difficulty:** Intermediate
**Category:** Security

---

## KNET — Kernel Networking Stack

Collection of kernel subsystems implementing network protocol processing, socket
management, and packet I/O. In Linux: socket layer, TCP/IP implementation,
Netfilter (iptables/nftables hooks), and the network device driver interface.
Tuned via sysctls, NAPI polling, interrupt coalescing, and XDP programs.

**Difficulty:** Advanced
**Category:** Networking

---

## KNOT — Knot DNS

High-performance authoritative DNS server developed by CZ.NIC. Focuses on
correctness and throughput. Supports DNSSEC signing, zone transfer over TLS
(XoT), and dynamic DNS updates via RFC 2136. An alternative to BIND in
high-throughput DNS infrastructure where latency and stability are critical.

**Difficulty:** Advanced
**Category:** Networking

---

## KEYS — Kernel Key Retention Service

Linux kernel subsystem providing secure in-kernel storage for cryptographic keys,
authentication tokens, and configuration data. Used by Kerberos, NFS Kerberos
authentication, and encrypted filesystems. Accessible from user space via
`keyctl` and the `add_key()` / `request_key()` system calls.

**Difficulty:** Advanced
**Category:** OS

---

## KOBJ — Kernel Object

Fundamental data structure in the Linux kernel representing a generic object
with reference counting, a name, and a sysfs representation. KObjects form the
basis of the Linux device model; every device, driver, and bus is represented
as a kobject with a reference count managed by `kobject_get()` and `kobject_put()`.

**Difficulty:** Advanced
**Category:** OS

---

## KPI — Key Performance Indicator

Quantifiable metric used to evaluate success of an IT system or service against
defined objectives. In IT operations: uptime percentage, MTTR, ticket resolution
time, deployment frequency. Effective KPIs must be Specific, Measurable,
Achievable, Relevant, and Time-bound (SMART) to drive actionable decisions.

**Difficulty:** Base
**Category:** Dev

---

## KPIS — Key Performance Indicators Suite

Aggregated set of KPIs grouped into a monitoring dashboard for holistic service
health assessment. In SRE practice, combined with SLOs and error budgets. Common
suites track availability, latency percentiles (p50/p99), error rates, and
saturation aligned with Google's Four Golden Signals framework.

**Difficulty:** Intermediate
**Category:** Dev

---

## KPSS — Kubernetes Pod Security Standards

Policy framework replacing the deprecated Pod Security Policy (PSP) in Kubernetes
1.25+. Defines three policy levels: Privileged (unrestricted), Baseline (minimal
restrictions), and Restricted (hardened). Enforced by the built-in Pod Security
Admission controller configured via namespace-level labels.

**Difficulty:** Intermediate
**Category:** Cloud

---

## KPTI — Kernel Page Table Isolation

Linux and Windows kernel mitigation for the Meltdown vulnerability (CVE-2017-5754).
Maintains separate page tables for kernel and user space, preventing user processes
from reading kernel memory via speculative side channels. Introduced measurable
performance overhead on pre-hardware-mitigation Intel processors.

**Difficulty:** Advanced
**Category:** OS

---

## KPTR — Kernel Pointer Restriction

Linux security feature controlled by the `kptr_restrict` sysctl that hides kernel
pointer values in `/proc` output and kernel logs from unprivileged users. Prevents
attackers from reading kernel symbol addresses to bypass KASLR. Values: 0 (unrestricted),
1 (hidden from non-root), 2 (hidden from all users).

**Difficulty:** Advanced
**Category:** Security

---

## KREF — Kernel Reference Count

Atomic reference counting mechanism in the Linux kernel used to track the number
of active users of a kernel object. When the count reaches zero, a release function
frees the associated memory. Prevents use-after-free bugs in concurrent kernel
code where multiple subsystems share ownership of the same object.

**Difficulty:** Advanced
**Category:** OS

---

## KRNG — Kernel Random Number Generator

Kernel component collecting entropy from hardware events (interrupt timing, disk
I/O, keyboard) to produce cryptographically secure random bytes. In Linux:
`/dev/random` blocks when entropy pool is insufficient; `/dev/urandom` uses a
CSPRNG and never blocks. Critical for TLS handshakes and session token generation.

**Difficulty:** Advanced
**Category:** OS

---

## KRSK — Key Risk Score

Composite metric in security risk management quantifying the potential impact
and likelihood of a threat. Combines vulnerability severity (CVSS), asset
criticality, threat intelligence feeds, and control effectiveness into a single
score used to prioritize remediation efforts and security investment allocation.

**Difficulty:** Intermediate
**Category:** Security

---

## KSMD — Kernel Samepage Merging Daemon

Linux kernel thread that scans physical memory looking for pages with identical
content across different virtual addresses. Merges duplicates into a single
copy-on-write physical page to reduce RAM usage. Most effective in virtualization
environments where multiple VMs share the same OS image and application binaries.

**Difficulty:** Advanced
**Category:** OS

---

## KTLS — Kernel TLS

Linux kernel feature (since 4.13) implementing TLS record-layer processing in
kernel space. Reduces data copies by allowing the kernel's networking stack to
encrypt and decrypt TLS records directly, eliminating user-to-kernel boundary
crossings for each record. Significantly improves throughput in high-volume
HTTPS server deployments.

**Difficulty:** Advanced
**Category:** OS

---

## KUBE — Kubernetes

Open-source container orchestration platform originally developed by Google,
donated to the CNCF in 2016. Manages deployment, scaling, networking, and
lifecycle of containerized workloads across clusters of nodes using declarative
YAML manifests and a reconciliation control loop.

**Difficulty:** Base
**Category:** Cloud

---

## KVDB — Key-Value Database

Database storing data as key-value pairs where each unique key maps to an arbitrary
value (string, binary blob, JSON document). Optimized for high-speed single-key
lookups and writes. Examples: Redis, RocksDB, etcd, DynamoDB. The simplest NoSQL
model; scales horizontally but lacks relational query capabilities.

**Difficulty:** Base
**Category:** Database

---

## KVM — Kernel-based Virtual Machine

Linux kernel module (merged 2007) that turns the kernel into a Type-1 hypervisor
by exposing hardware virtualization extensions (Intel VT-x, AMD-V) to user space.
Guest VMs run as regular Linux processes executing most instructions natively.
Foundation of QEMU, Proxmox VE, and OpenStack compute nodes.

**Difficulty:** Intermediate
**Category:** OS

---

## KUID — Kernel User ID

Kernel-internal representation of a user identifier in the Linux security model.
In containerized environments, KUID tracks user namespace mappings: a process
running as UID 0 inside a container may map to KUID 100000 in the host kernel,
providing privilege isolation without true root access on the host.

**Difficulty:** Advanced
**Category:** OS

---

## KYLO — Know Your Local Operations

Internal IT best practice of maintaining documented awareness of local infrastructure
specifics: hardware inventory, IP assignments, service dependencies, and runbooks.
Analogous to KYC in financial compliance but applied to operational IT knowledge
management and incident response readiness.

**Difficulty:** Base
**Category:** Dev

---

## KSFT — Kernel Selftests Framework
Linux kernel testing infrastructure located in tools/testing/selftests/. Provides a standardized way to write and run userspace tests that exercise kernel subsystems (networking, memory, cgroups, BPF, etc.). Tests are run via make -C tools/testing/selftests run_tests and integrated into kernel CI pipelines.
**Difficulty:** Advanced
**Category:** OS


---

## KAFKA — Apache Kafka

Distributed event streaming platform for high-throughput, fault-tolerant publish-subscribe messaging. Data organized into topics partitioned across brokers; consumers track offsets enabling replay. KRaft mode (KIP-500) removes ZooKeeper dependency. Used for event-driven architectures, change data capture (CDC), real-time analytics pipelines, and microservice decoupling.

**Difficulty:** Intermediate
**Category:** Database

---

## KIALI — Kiali Service Mesh Console

Open-source observability console for Istio service mesh. Provides topology visualization, traffic flow graphs, health status, distributed tracing integration (Jaeger/Zipkin), and Istio configuration validation. Displays telemetry collected by Prometheus. Installed as an Istio addon or standalone via Helm chart; accessible via kubectl port-forward.

**Difficulty:** Intermediate
**Category:** Cloud

---

## KNFSD — Kernel NFS Daemon

Linux kernel-space NFS server providing higher performance than user-space alternatives. Runs as kernel threads (nfsd, lockd, mountd). Configured via /etc/exports and managed with exportfs, nfsstat, and rpcinfo. Supports NFSv3, NFSv4, and NFSv4.1 (pNFS). NFS over RDMA (NFSoRDMA) available since kernel 4.20 for low-latency storage networks.

**Difficulty:** Advanced
**Category:** OS

---

## KIBNA — Kibana Dashboard

Elasticsearch's visualization and exploration platform (part of Elastic Stack). Provides Discover (log search), Dashboard (metric panels), Lens (visual editor), and Maps (geo visualization). Integrates with Elastic APM, Security (SIEM), and Observability solutions. Configures index patterns, saved searches, alerting rules, and Canvas presentations.

**Difficulty:** Intermediate
**Category:** Database

---

## KSMEM — KSM Memory Merging

Kernel Samepage Merging: Linux feature scanning memory pages across processes and merging identical pages into a single copy-on-write page. Reduces memory consumption in KVM virtualization environments where multiple VMs run the same OS image. Controlled via /sys/kernel/mm/ksm/. Disabled for security-sensitive workloads to prevent side-channel timing attacks.

**Difficulty:** Advanced
**Category:** OS

---

## KRBTG — Kerberos TGT Ticket

Kerberos Ticket Granting Ticket issued by the Authentication Service (AS) after successful initial authentication. Allows the client to request service tickets from the Ticket Granting Service (TGS) without re-authenticating. Default lifetime: 10 hours (renewable up to 7 days). Golden Ticket attacks forge TGTs by compromising the krbtgt account's NTLM hash.

**Difficulty:** Advanced
**Category:** Security

---

## KYVNO — Kyverno Policy Engine

Kubernetes-native policy engine validating, mutating, and generating Kubernetes resources using declarative YAML policies without Rego. Enforces Pod Security Standards, auto-injects labels and annotations, generates ConfigMaps from templates, and verifies container image signatures (Cosign, Notary v2). CNCF incubating project with active adoption in GitOps pipelines.

**Difficulty:** Advanced
**Category:** Cloud

---

## KPROB — Kprobe Kernel Tracing

Linux kernel dynamic tracing mechanism placing breakpoints at arbitrary kernel function entry and return points without recompiling the kernel. Accessed via /sys/kernel/debug/kprobes/ or eBPF kprobe programs. Used for performance analysis, kernel code path debugging, and security monitoring of kernel function invocations in production systems.

**Difficulty:** Advanced
**Category:** OS

---

## KPACK — Kubernetes Buildpack

CNCF project (kpack) implementing Cloud Native Buildpacks on Kubernetes. Automatically builds OCI container images from source code without Dockerfiles. Triggered by source code changes or buildpack updates; rebuilt images are pushed to a registry. Used in enterprise developer platforms (VMware Tanzu, Paketo) for secure, opinionated image builds.

**Difficulty:** Advanced
**Category:** Cloud

---

## KVLOG — Key-Value Log

Append-only log format storing entries as key-value pairs, enabling efficient key lookup and chronological replay. Used in Kafka (topic-compacted logs), etcd (MVCC key history), and LSM-tree databases (LevelDB, RocksDB) as the write path before compaction into sorted string tables (SSTables). Provides durability and ordered event history in distributed systems.

**Difficulty:** Intermediate
**Category:** Database

---

## KVERS — Kernel Version String

String identifying the specific version of the OS kernel. On Linux: uname -r returns major.minor.patch-build-arch (e.g. 6.8.0-45-generic). Critical for module compatibility, security patch verification, and feature availability checks in automation scripts. Linux follows time-based rolling releases; distributions maintain separate versioning schemes with backported patches.

**Difficulty:** Base
**Category:** OS


---

## KASAN — Kernel Address Sanitizer

Dynamic memory error detector for the Linux kernel. Instruments memory accesses at compile time to detect out-of-bounds reads/writes and use-after-free bugs in kernel code. Uses shadow memory (1 byte per 8 bytes of kernel memory) to track valid access ranges. KASAN reports with full stack traces. Available in generic (slow) and SW/HW tag-based (faster) modes.

**Difficulty:** Advanced
**Category:** OS

---

## KCSAN — Kernel Concurrency Sanitizer

Dynamic race condition detector for the Linux kernel using compile-time instrumentation to detect data races on shared kernel memory. When two concurrent accesses to the same memory location occur without proper synchronization (and at least one is a write), KCSAN reports the race with stack traces for both threads. Replaces KTSAN for mainline use.

**Difficulty:** Advanced
**Category:** OS

---

## KFENCE — Kernel Electric Fence

Low-overhead kernel memory safety detector (Linux 5.12+) designed for production use. Samples a small fraction of kernel allocations into a guarded memory pool where each allocation is surrounded by guard pages. Page faults on guard pages immediately detect out-of-bounds accesses. Negligible performance impact compared to KASAN.

**Difficulty:** Advanced
**Category:** OS

---

## KSMBD — Kernel SMB Daemon

In-kernel SMB3 server implementation (Linux 5.15+) providing file sharing without a userspace daemon overhead. Processes SMB2/3 requests directly in kernel context for lower latency and higher throughput than Samba's userspace approach. Managed via ksmbd-tools (ksmbd.adduser, ksmbd.addshare). Still considered experimental for production use by many distributions.

**Difficulty:** Advanced
**Category:** OS
