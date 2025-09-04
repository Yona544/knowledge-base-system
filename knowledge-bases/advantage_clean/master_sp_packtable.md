---
title: Master Sp Packtable
slug: master_sp_packtable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_packtable.htm
source: Advantage CHM
tags:
  - master
checksum: 1a06c2b0dc381fd9d16ad2922ba5fb988aa325e1
---

# Master Sp Packtable

sp\_PackTable

sp\_PackTable

Advantage SQL Engine

| sp\_PackTable  Advantage SQL Engine |  |  |  |  |

Removes all deleted records from a table and re-indexes it.

Syntax

sp\_PackTable( TableName,CHARACTER,515 )

 

sp\_PackTable( TableName,CHARACTER,515,

             MemoBlockSize,INTEGER )

 

Parameters

| TableName (I) | Name and/or path of a table to pack. |
| MemoBlockSize (I) | Optional memo block size. If this is not provided or if the value is 0, the memo block size will not be changed by the pack operation. |

Remarks

sp\_PackTable performs a pack of a table which removes all deleted records from the table. Internal fragmentation in memo files will also be eliminated. It then re-indexes the table. This operation requires exclusive access to the table, no process can have this table open when calling this procedure. Only auto-open indexes will be re-indexed. sp\_PackTable is illegal in a transaction. The TableName parameter must specify the table name of a dictionary bound table, or the table path of a free table).

See Also

[AdsPackTable](ace_adspacktable.md)

[sp\_PackTableOnline](master_sp_packtableonline.md)

[sp\_ZapTable](master_sp_zaptable.md)
