---
title: Master Sp Mggetusertables
slug: master_sp_mggetusertables
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetusertables.htm
source: Advantage CHM
tags:
  - master
checksum: 8f481651e93b15e7f18e219893f8bc7ef2fb48ae
---

# Master Sp Mggetusertables

sp\_mgGetUserTables

sp\_mgGetUserTables

Advantage SQL Engine

| sp\_mgGetUserTables  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all of the tables currently opened on the server by the specified user

Syntax

EXECUTE PROCEDURE sp\_mgGetUserTables( UserName,Character,200 )

Parameters

| UserName (I) | Name of the connected user. |
| TableName (O) | Fully qualified table name |
| LockType (O) | Type of locking mode the table was opened with. |
| LockTypeValue (O) | Integer value of the lock type. This is the same value as is returned in the ADS\_MGMT\_TABLE\_INFO structure by the AdsMgGetOpenTables API. |

Remarks

The user name must be the Advantage clients computer name. The returned table name is the fully qualified path of the table on the server. To be more specific with the user name parameter, the user name (client computer name) and the operating system user login name can be specified together (computer name first), separated by a backslash '\'.

The LockType parameter returns the following values. The corresponding LockTypeValue is given in parentheses.

ADS (1) for Advantage Proprietary Locking,

CDX (2) for Advantage Compatibility Locking on a DBF/CDX file and,

NTX (3) for Advantage Compatibility Locking on a DBF/NTX file.

ADT (4) for Advantage Compatibility Locking on an ADT table opened by Advantage Local Server.

Note With Advantage Local Server, sp\_mgGetUserTables will only return tables open by this user in the instance of Advantage Local Server currently loaded into memory. Information about tables the user has opened in other instances of the Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetUserTables( 'username' );

 

To retrieve table names using a computername and username combo, separate them with a backslash:

EXECUTE PROCEDURE sp\_mgGetUserTables( 'workstation\username' )

 

Trailing backslash characters after the computer name are ignored:

EXECUTE PROCEDURE sp\_mgGetUserTables( 'workstation\' )

 

See Also

[sp\_mgGetAllTables](master_sp_mggetalltables.md)

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.md)

[sp\_mgGetTableUsers](master_sp_mggettableusers.md)
