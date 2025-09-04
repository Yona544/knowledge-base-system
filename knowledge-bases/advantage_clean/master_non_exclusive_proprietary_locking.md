---
title: Master Non Exclusive Proprietary Locking
slug: master_non_exclusive_proprietary_locking
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_non_exclusive_proprietary_locking.htm
source: Advantage CHM
tags:
  - master
checksum: 5753363e98a04d4c87c65b2467bf2382fbb95372
---

# Master Non Exclusive Proprietary Locking

Non-Exclusive Proprietary Locking

Non-Exclusive Proprietary Locking

Advantage Database Server

| Non-Exclusive Proprietary Locking  Advantage Database Server |  |  |  |  |

In older versions of Advantage, proprietary locking did not open files using an exclusive mode, instead it used a "deny write" open mode. While this would allow applications that do not use Advantage Database Server to have access to the data files, it could also lead to index corruption. These other applications could still lock bytes in the files causing Advantage read and write operations to fail. For this reason the default proprietary open mode was changed. If, however, you require applications that do not use Advantage Database Server (such as backup software, or reporting software, or applications using Advantage Local Server) to open files in a shared, read-only mode, this server option is available to revert to the older behavior.

For more details on proprietary locking, see [Advantage Proprietary Locking](master_advantage_proprietary_locking.md).

To turn off the exclusive proprietary locking file open mode, perform one of the following:

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf).

NONEXCLUSIVE\_PROPRIETARY\_LOCKING=1

For Windows:

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry, and set its value to 1.

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\NONEXCLUSIVE\_PROPRIETARY\_LOCKING
