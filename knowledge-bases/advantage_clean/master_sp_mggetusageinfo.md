---
title: Master Sp Mggetusageinfo
slug: master_sp_mggetusageinfo
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetusageinfo.htm
source: Advantage CHM
tags:
  - master
checksum: 168a937ca319fc2213f92a287af2f4cc955e35aa
---

# Master Sp Mggetusageinfo

sp\_mgGetUsageInfo

sp\_mgGetUsageInfo

Advantage SQL Engine

| sp\_mgGetUsageInfo  Advantage SQL Engine |  |  |  |  |

Returns information about the current activity on the Advantage Database Server.

Syntax

EXECUTE PROCEDURE sp\_mgGetUsageInfo()

Parameters

| Item (O) | Name of the activity. |
| InUse (O) | Number of items in use. |
| MaxUsed (O) | Maximum number of items ever used. |
| Configured (O) | Number configured on the server. |
| Rejected (O) | Number of items rejected. |

Remarks

This procedure returns the following items:

Users

Connections

Work Areas

Tables

Indexes

Locks

TPS Header Elems

TPS Visibility Elems

TPS Memo Elems

Worker Threads

Stateful Users

Stateless Users

To get the server up-time, errors logged, or number of operations use the sp\_mgGetActivityInfo procedure.

Note With the Advantage Local Server, sp\_mgGetUsageInfo will only return information for the instance of Advantage Local Server currently loaded into memory.

Example

EXECUTE PROCEDURE sp\_mgGetusageInfo();

See Also

[sp\_mgGetActivityInfo](master_sp_mggetactivityinfo.md)

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.md)

[sp\_mgGetConfigMemory](master_sp_mggetconfigmemory.md)

[sp\_mgGetInstallInfo](master_sp_mggetinstallinfo.md)
