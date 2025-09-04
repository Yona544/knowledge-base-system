---
title: Master File Size Support Greater Than 4 Gigabytes
slug: master_file_size_support_greater_than_4_gigabytes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_file_size_support_greater_than_4_gigabytes.htm
source: Advantage CHM
tags:
  - master
checksum: 30d1f049cbfb878a04f180b963cad265d322becd
---

# Master File Size Support Greater Than 4 Gigabytes

File Size Support Greater Than 4 Gigabytes

File Size Support Greater Than 4 Gigabytes

Advantage Concepts

| File Size Support Greater Than 4 Gigabytes  Advantage Concepts |  |  |  |  |

The Advantage proprietary file format (ADT/ADM/ADI) can support files sizes greater than 4 GB when used on NTFS or Linux file systems.

Beginning with v8.0, Advantage Database Server can utilize DBF tables and their associated memo files (FPT and DBT) with file sizes greater than 4 GB. Index files associated with DBF tables (CDX, IDX, NTX) cannot exceed the 4 GB limit due to file format limitations, but this problem can be avoided by using multiple index files. When using DBF tables over 4 GB in size, you must use Advantage Proprietary Locking. Also, note that CA-Clipper applications must turn off rights checking (AX\_RightsCheck( .F. )) when opening tables that exceed 4 GB in size.
