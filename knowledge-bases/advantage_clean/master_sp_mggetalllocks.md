---
title: Master Sp Mggetalllocks
slug: master_sp_mggetalllocks
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetalllocks.htm
source: Advantage CHM
tags:
  - master
checksum: 7fed99c67f714d8cde7b099653b44a4acc37d252
---

# Master Sp Mggetalllocks

sp\_mgGetAllLocks

sp\_mgGetAllLocks

Advantage SQL Engine

| sp\_mgGetAllLocks  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all record numbers of records that are locked in the given table.

Syntax

EXECUTE PROCEDURE sp\_mgGetAllLocks( TableName,Character,255 )

Parameters

| TableName (I) | Fully qualified path to the table. |
| LockedRecNo (O) | Record Numbers of locked records. |

Remarks

This procedure returns a result set containing all record numbers of records that are currently locked in the given table. To view the name of the user that has a particular record locked, use the sp\_mgGetLockOwner procedure.

Note With the Advantage Local Server, sp\_mgGetAllLocks will only return information about locks instantiated by the instance of Advantage Local Server currently loaded into memory. Information about locks instantiated from other instances of Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetAllLocks( '\\server\share\data\table.adt' );

See Also

[sp\_mgGetLockOwner](master_sp_mggetlockowner.md)

[sp\_mgGetUserLocks](master_sp_mggetuserlocks.md)
