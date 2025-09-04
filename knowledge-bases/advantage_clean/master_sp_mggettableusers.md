---
title: Master Sp Mggettableusers
slug: master_sp_mggettableusers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggettableusers.htm
source: Advantage CHM
tags:
  - master
checksum: 68f649d7fed0fb6a7e33fc70ec5ac0bcabb51695
---

# Master Sp Mggettableusers

sp\_mgGetTableUsers

sp\_mgGetTableUsers

Advantage SQL Engine

| sp\_mgGetTableUsers  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all users who have the specified table open.

Syntax

EXECUTE PROCEDURE sp\_mgGetTableUsers( TableName,Character,255 )

Parameters

| TableName (I) | Full qualified path to the table. |
| UserName (O) | Name of the connected user. |
| ConnNumber (O) | NetWare connection number. (Deprecated) |
| DictionaryUser (O) | Name of user that has authenticated to an Advantage Data Dictionary. |
| Address (O) | IP or IPX address of the connected user. |
| OSUserLoginName (O) | Operating system login name of the connected user. |
| TSAddress (O) | Terminal Server client IP address if the connection is made from a Terminal Server session. |

Remarks

The table name is the fully qualified path to the table on the server.

Note With the Advantage Local Server, sp\_mgGetTableUsers will only return users who have opened the table in the instance of Advantage Local Server currently loaded into memory. It is not possible to determine other users who have opened the table from other instances of the Advantage Local Server.

 

Example

EXECUTE PROCEDURE sp\_mgGetTableUsers( '\\server\share\data\table.adt' );

See Also

[sp\_mgGetAllTables](master_sp_mggetalltables.md)

[sp\_mgGetUserTables](master_sp_mggetusertables.md)
