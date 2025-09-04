---
title: Master Compress Dump Files
slug: master_compress_dump_files
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_compress_dump_files.htm
source: Advantage CHM
tags:
  - master
checksum: 5a8c08a54378660b525016b791514afc0197e072
---

# Master Compress Dump Files

Compress\_Dump\_Files

Compress\_Dump\_Files

Advantage Database Server

| Compress\_Dump\_Files  Advantage Database Server |  |  |  |  |

Default = 1 (compress dump files)

When Advantage creates a [dump file](master_adsdump_files.md), the default behavior is to compress the dump file after it is created. While this typically reduces the file size significantly, it can take a relatively long time to complete the compression. To disable the compression step, add the following configuration parameter and set the value to zero (0).

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\Compress\_Dump\_Files=0
