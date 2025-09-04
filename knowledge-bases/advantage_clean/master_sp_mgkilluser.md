---
title: Master Sp Mgkilluser
slug: master_sp_mgkilluser
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mgkilluser.htm
source: Advantage CHM
tags:
  - master
checksum: 60575f19294fa956675fe81fc554d91fa3209d62
---

# Master Sp Mgkilluser

sp\_mgKillUser

sp\_mgKillUser

Advantage SQL Engine

| sp\_mgKillUser  Advantage SQL Engine |  |  |  |  |

Disconnects the specified user name from the Advantage Database Server.

Syntax

EXECUTE PROCEDURE sp\_mgKillUser ( UserName,Character,200 )

Parameters

| UserName (I) | Name of a connected user to disconnect. When connected to the [root dictionary](master_root_dictionary.md) as [SERVER:Admin](master_database_base_roles.md), this parameter can be an asterisk (\*) to indicate that all connections be disconnected. |

Remarks

The UserName must be the client computer name associated with the connection.

sp\_mgKillUser is a potentially dangerous operation and should be used with extreme caution. sp\_mgKillUser will cause the specified user to be abnormally disconnected from the Advantage Database Server. If the user is currently in the midst of an operation, that operation may not be able to run to completion. If the specified user is currently in a transaction, that transaction will be rolled back before the user is disconnected. All records locked by the specified user will be unlocked. All files open by the specified user will be closed. The specified user will then be disconnected. Unpredictable Advantage errors may be received by the Advantage application immediately after it has been "killed".

sp\_mgKillUser should NOT be used to disconnect the current application from the Advantage Database Server. The clients normal disconnect method should be used in this instance.

Beginning with v11 of Advantage, additional restrictions have been added. This procedure requires [DB:Admin](master_database_base_roles.md) membership when connected to a data dictionary, and only other users connected to the same dictionary can be killed. When connected with a free connection, it can be used to remove other free connections. When connected to the [root dictionary](master_root_dictionary.md) as [SERVER:Admin](master_database_base_roles.md), it is possible to remove any connection (similar to pre-v11 behavior).

Note sp\_mgKillUser has no effect when used with the Advantage Local Server.

Example

EXECUTE PROCEDURE sp\_mgKillUser( 'username' );

See Also

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.md)
