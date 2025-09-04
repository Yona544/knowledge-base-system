---
title: Master Sp Mggettableindexes
slug: master_sp_mggettableindexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggettableindexes.htm
source: Advantage CHM
tags:
  - master
checksum: 14776592bb16faaa556cf8a0ea5c8efcc7be9ef0
---

# Master Sp Mggettableindexes

sp\_mgGetTableIndexes

sp\_mgGetTableIndexes

Advantage SQL Engine

| sp\_mgGetTableIndexes  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all indexes opened on the specified table.

Syntax

EXECUTE PROCEDURE sp\_mgGetTableIndexes( TableName,Character,255 )

Parameters

| TableName (I) | Full qualified path to the table. |
| IndexName (O) | Full qualified path to the index file. |

Remarks

Tables can have zero or more index files associated with them. This procedure returns the fully qualified path to the index files associated with the table.

Note With Advantage Local Server, sp\_mgGetTableIndexes will only return indexes opened on this table in the instance of Advantage Local Server currently loaded into memory. Information about indexes opened on the table in other instances of the Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetTableIndexes( '\\server\share\data\table.adt' );

See Also

[sp\_mgGetAllIndexes](master_sp_mggetallindexes.md)

[sp\_mgGetAllTables](master_sp_mggetalltables.md)

[sp\_mgGetUserIndexes](master_sp_mggetuserindexes.md)
