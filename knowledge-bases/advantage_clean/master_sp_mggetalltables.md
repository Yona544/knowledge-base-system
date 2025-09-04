---
title: Master Sp Mggetalltables
slug: master_sp_mggetalltables
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetalltables.htm
source: Advantage CHM
tags:
  - master
checksum: fef88e8df6be19781a5214b8a688668c297002b7
---

# Master Sp Mggetalltables

sp\_mgGetAllTables

sp\_mgGetAllTables

Advantage SQL Engine

| sp\_mgGetAllTables  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all tables currently opened on the server.

Syntax

EXECUTE PROCEDURE sp\_mgGetAllTables()

Parameters

| TableName (O) | Fully qualified path to the table. |
| LockType (O) | Type of locking mode the table was opened with. |
| LockTypeValue (O) | Integer value of the lock type. This is the same value as is returned in the ADS\_MGMT\_TABLE\_INFO structure by the AdsMgGetOpenTables API. |

Remarks

The LockType parameter returns the following values. The corresponding LockTypeValue is given in parentheses.

ADS (1) for Advantage Proprietary Locking,

CDX (2) for Advantage Compatibility Locking on a DBF/CDX file and,

NTX (3) for Advantage Compatibility Locking on a DBF/NTX file.

ADT (4) for Advantage Compatibility Locking on an ADT table opened by Advantage Local Server.

Note With Advantage Local Server, sp\_mgGetAllTables will only return information on tables opened from the instance of Advantage Local Server currently loaded into memory. Information about tables loaded from other instances of Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetAllTables();

See Also

[sp\_mgGetTableIndexes](master_sp_mggettableindexes.md)

[sp\_mgGetTableUsers](master_sp_mggettableusers.md)

[sp\_mgGetUserTables](master_sp_mggetusertables.md)

[sp\_mgGetAllIndexes](master_sp_mggetallindexes.md)
