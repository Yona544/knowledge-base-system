---
title: Master Sp Mggetconnectedusers
slug: master_sp_mggetconnectedusers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetconnectedusers.htm
source: Advantage CHM
tags:
  - master
checksum: 4a52c1cfb38da47d85e9056dfbb22d6c40cc09bb
---

# Master Sp Mggetconnectedusers

sp\_mgGetConnectedUsers

sp\_mgGetConnectedUsers

Advantage SQL Engine

| sp\_mgGetConnectedUsers  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all users currently connected to the server.

Syntax

EXECUTE PROCEDURE sp\_mgGetConnectedUsers()

Parameters

| UserName (O) | Name of the connected user. |
| ConnNumber (O) | NetWare connection number. (Deprecated) |
| DictionaryUser (O) | Name of user that has authenticated to an Advantage Data Dictionary. |
| Address (O) | IP or IPX address of the connected user. |
| OSUserLoginName (O) | Operating system login name of the connected user. |
| TSAddress (O) | Terminal Server Client IP address if the connection is made from a Terminal Server session. |
| ApplicationID (O) | Application ID for the connected user. See [sp\_SetApplicationID.](master_sp_setapplicationid.md) |
| AverageCost (O) | The estimated average cost per server request for the connection. If this value is less than or equal to the current threshold (see [sp\_mgGetActivityInfo](master_sp_mggetactivityinfo.md)), the next request will be placed in the [Express Queue](master_express_queue.md). |

Remarks

sp\_mgGetConnectedUsers returns the names of each connected user. UserName will be the name of the computer the user is connected from.  OSUserLoginName will be the operating system user name of the user. DictionaryUser will be the data dictionary user name if the user is authenticated to a data dictionary.

Note With Advantage Local Server, sp\_mgGetConnectedUses will only return information about users of the instance of Advantage Local Server currently loaded into memory. Information about users from other instances of the Advantage Local Server will not be returned.

 

Example

EXECUTE PROCEDURE sp\_mgGetConnectedUsers();

See Also

[sp\_mgGetTableUsers](master_sp_mggettableusers.md)

[sp\_mgGetUserIndexes](master_sp_mggetuserindexes.md)

[sp\_mgGetUserLocks](master_sp_mggetuserlocks.md)

[sp\_mgGetUserTables](master_sp_mggetusertables.md)
