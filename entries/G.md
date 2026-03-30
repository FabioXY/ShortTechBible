## GPU — Graphics Processing Unit

A massively parallel processor originally designed to accelerate rasterization and rendering of 3D graphics. GPUs contain thousands of smaller cores optimized for SIMD operations on floating-point data. Modern GPUs are general-purpose compute engines (GPGPU) used for ML training, scientific simulation, and cryptography via APIs like CUDA and OpenCL.

**Difficulty:** Intermediate
**Category:** Hardware

---

## GUI — Graphical User Interface

A type of user interface that uses visual components (windows, icons, buttons, menus) rather than text commands to interact with software. GUIs rely on a windowing system (X11, Wayland, Win32, Cocoa) and an event loop to handle user input. While more accessible than CLIs, GUIs are harder to automate and script.

**Difficulty:** Base
**Category:** OS

---

## GRUB — Grand Unified Bootloader

The default bootloader for most Linux distributions, part of the GNU project. GRUB is installed in the MBR or EFI System Partition and is responsible for loading the OS kernel and initramfs into memory. GRUB2 supports UEFI, GPT, multiple file systems, scripting, and boot menu customization via /etc/grub.d/ and grub.cfg.

**Difficulty:** Intermediate
**Category:** OS

---

## GZIP — GNU Zip

A file compression format and program (RFC 1952) using DEFLATE compression (a combination of LZ77 and Huffman coding). gzip compresses a single file; for multiple files, it is combined with tar (producing .tar.gz or .tgz archives). HTTP/1.1 and later support gzip content encoding for compressing HTTP responses in transit.

**Difficulty:** Base
**Category:** OS

---

## GPT — GUID Partition Table

A partitioning scheme that replaces MBR, defined as part of the UEFI specification. GPT stores partition entries in a header and backup at the end of the disk, supports up to 128 partitions by default, and handles disks larger than 2 TB. Each partition has a 128-bit GUID identifying its type and unique identity.

**Difficulty:** Intermediate
**Category:** Hardware

---

## GDT — Global Descriptor Table

A data structure in x86 architecture that defines memory segments for the CPU. The GDT is loaded via the LGDT instruction and contains segment descriptors specifying base address, limit, privilege level, and type (code, data, system). In 64-bit long mode, segmentation is largely vestigial but the GDT still exists for privilege-level switching (syscalls, TSS).

**Difficulty:** Advanced
**Category:** OS
