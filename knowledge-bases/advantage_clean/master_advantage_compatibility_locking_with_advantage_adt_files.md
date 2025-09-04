---
title: Master Advantage Compatibility Locking With Advantage Adt Files
slug: master_advantage_compatibility_locking_with_advantage_adt_files
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_compatibility_locking_with_advantage_adt_files.htm
source: Advantage CHM
tags:
  - master
checksum: 20ff6167b4fc27ab641f21d141ba4410113019e5
---

# Master Advantage Compatibility Locking With Advantage Adt Files

Advantage Compatibility Locking With Advantage ADT Files

Advantage Compatibility Locking with Advantage ADT Files

Advantage Concepts

| Advantage Compatibility Locking with Advantage ADT Files  Advantage Concepts |  |  |  |  |

With Advantage ADT files, the Advantage Compatibility Locking mode allows data to be shared by Advantage Local Server applications simultaneously. Locks in one Advantage Local Server application are made visible to other Advantage Local Server applications by obtaining network operating system locks. Files are opened in the mode specified by the application. Therefore, multiple Advantage Local Server applications can have the same files open at the same time in a read/write mode.

With ADT files, Advantage Compatibility locking is not available with the Advantage Database Server. Advantage Compatibility locking is only available with the Advantage Local Server.

[Explicit and Implicit Record Locking with the Advantage Client Engine](master_explicit_and_implicit_record_locking_with_the_advantage_client_engine.md)
