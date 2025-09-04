---
title: Master Sp Mggetlockowner
slug: master_sp_mggetlockowner
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetlockowner.htm
source: Advantage CHM
tags:
  - master
checksum: 3ae79475223ba2766045bdcc7b429d4990df1e5b
---

# Master Sp Mggetlockowner

sp\_mgGetLockOwner

sp\_mgGetLockOwner

Advantage SQL Engine

| sp\_mgGetLockOwner  Advantage SQL Engine |  |  |  |  |

Returns user information for the specified table and record number.

Syntax

EXECUTE PROCEDURE sp\_mgGetLockOwner( TableName,Character,255;

RecordNumber,Integer )

Parameters

| TableName (I) | Full qualified path to the table. |
| RecordNumber (I) | Locked Record number. |
| UserName (O) | Name of the connected user |
| ConnNumber (O) | NetWare connection number. (Deprecated) |
| DictionaryUser (O) | Name of user that has authenticated to an Advantage Data Dictionary. |
| Address (O) | IP or IPX address of the connected user. |
| LockType (O) | Type of lock. The value will be File Lock, Record Lock or No Lock. |
| OSUserLoginName (O) | Operating system login name of the connected user. |
| TSAddress (O) | Terminal Server Client IP address if the connection is made from a Terminal Server session. |

Remarks

You must use the fully qualified path and file name for the TableName parameter. The RecordNumber is an integer value representing the locked record number (or 0 if you are checking for a table lock). You can get a list of locked records on a table using the sp\_mgGetAllLocks procedure.

Note With the Advantage Local Server, sp\_mgGetLockOwner will only return information, if the lock was instantiated by the instance of Advantage Local Server currently loaded into memory. It is not possible to determine the owner of a lock instantiated from other instances of the Advantage Local Server.

 

Example

EXECUTE PROCEDURE sp\_mgGetLockOwner( '\\server\share\data\table.adt', 1 );

See Also

[sp\_mgGetAllLocks](master_sp_mggetalllocks.md)

[sp\_mgGetUserLocks](master_sp_mggetuserlocks.md)
