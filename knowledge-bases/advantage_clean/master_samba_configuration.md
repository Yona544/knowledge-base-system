---
title: Master Samba Configuration
slug: master_samba_configuration
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_samba_configuration.htm
source: Advantage CHM
tags:
  - master
checksum: 1df7237fbc0406c83a393066ae359774aa308b63
---

# Master Samba Configuration

Samba Configuration

Samba Configuration

Advantage Concepts

| Samba Configuration  Advantage Concepts |  |  |  |  |

Locking

If you will be sharing tables between Linux and Windows machines using the Advantage Local Server, or using the Advantage Database Server and the Compatibility Locking mode, there are two Samba configuration options that must be modified. Samba takes a fairly aggressive stance on file locking, and in many cases its default options optimize its performance at the sake of correctness. If these configuration options are not modified, record locks will not be respected and index locking will not occur. This will undoubtedly lead to corruption.

Disable Optimistic Locking

oplocks = False

Disable OLE Locking Compatibility

ole locking compatibility = no

Drive Letters

If you use drive letters, you must use Samba share names that map directly to a directory name. For example, if you have a Samba share named "adsdata", then in order for the Advantage Database Server to be able to find the data, the directory it refers to must be /adsdata. The Advantage Database Server does not parse the Samba configuration file. Therefore, it is not possible for it to know the share mappings.

As an example, assume that a Linux server has a Samba share named "adsdata". If you map a drive from a Win32 machine to that share (e.g., net use x: \\xyz\adsdata), and then open a table named x:\testing\test.adt, the Advantage Database Server for Linux will attempt to open the table /adsdata/testing/test.adt.
