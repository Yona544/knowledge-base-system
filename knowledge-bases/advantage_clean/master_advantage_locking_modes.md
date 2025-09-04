---
title: Master Advantage Locking Modes
slug: master_advantage_locking_modes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_locking_modes.htm
source: Advantage CHM
tags:
  - master
checksum: 3dc288890116b2b9b37d982c14250f0725a6abb9
---

# Master Advantage Locking Modes

Advantage Locking Modes

Advantage Locking Modes

Advantage Concepts

| Advantage Locking Modes  Advantage Concepts |  |  |  |  |

Locking records and files is critical to sharing data on a network. Locking operations help enforce database stability by preventing other users from accessing the data while it is being updated. In non-client/server environments, lock management operations occur from the client and can be quite slow. The Advantage Database Server provides data locking from the server which significantly increases application locking management and performance. The Advantage Database Server provides an intelligent, high performance Proprietary locking mode and a Compatibility locking mode for sharing data with non-Advantage applications.

The Advantage locking method used by the Advantage Database Server can be specified per table.

[Advantage Proprietary Locking](master_advantage_proprietary_locking.md)

[Advantage Compatibility Locking With Xbase Files](master_advantage_compatibility_locking_with_xbase_files.md)

[Advantage Compatibility Locking With Advantage ADT Files](master_advantage_compatibility_locking_with_advantage_adt_files.md)
