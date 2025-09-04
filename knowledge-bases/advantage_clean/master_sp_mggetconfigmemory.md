---
title: Master Sp Mggetconfigmemory
slug: master_sp_mggetconfigmemory
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetconfigmemory.htm
source: Advantage CHM
tags:
  - master
checksum: 1c737a9e5b20f23d49d903a6a6d27a8e74e79728
---

# Master Sp Mggetconfigmemory

sp\_mgGetConfigMemory

sp\_mgGetConfigMemory

Advantage SQL Engine

| sp\_mgGetConfigMemory  Advantage SQL Engine |  |  |  |  |

Returns Advantage Database Server configuration information that affects the amount of memory required by the Advantage Database Server

Syntax

EXECUTE PROCEDURE sp\_mgGetConfigMemory()

Parameters

| Item (O) | Name of the item. |
| Value (O) | Value from the server. |
| Memory (O) | Amount of memory used in bytes. |

Remarks

This procedure returns the following items:

Connections

Work Areas

Tables

Indexes

Locks

User Buffer Size

TPS Header Elems

TPS Visibility Elems

TPS Memo Elems

Receive ECBs

Send ECBs

Worker Threads

Total Memory

Example

EXECUTE PROCEDURE sp\_mgGetConfigMemory();

See Also

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.md)
