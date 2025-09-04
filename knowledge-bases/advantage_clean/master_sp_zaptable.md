---
title: Master Sp Zaptable
slug: master_sp_zaptable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_zaptable.htm
source: Advantage CHM
tags:
  - master
checksum: b129048a1cf5091944c356f8c623174a8c99b80e
---

# Master Sp Zaptable

sp\_ZapTable

sp\_ZapTable

Advantage SQL Engine

| sp\_ZapTable  Advantage SQL Engine |  |  |  |  |

Removes all data from a table and re-indexes it.

Syntax

sp\_ZapTable( TableName,CHARACTER,515 )

Parameters

| TableName (I) | Name and/or path of a table to zap. |

Remarks

sp\_ZapTable performs a zap of a table which removes all records from the table and all data from the memo file then re-indexes the table. This operation requires exclusive access to the table; no process can have this table open when calling this procedure. Only auto-open indexes will be re-indexed. sp\_ZapTable is illegal in a transaction. The TableName parameter must specify the table name of a dictionary bound table, or the table path of a free table).

See Also

[AdsZapTable](ace_adszaptable.md)

[sp\_PackTable](master_sp_packtable.md)
