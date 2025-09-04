---
title: Ace Adsmgkilluser
slug: ace_adsmgkilluser
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsmgkilluser.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b573d38e7114334e831a413538f29924e9a2cc88
---

# Ace Adsmgkilluser

AdsMgKillUser

AdsMgKillUser

Advantage Client Engine

| AdsMgKillUser  Advantage Client Engine |  |  |  |  |

Will disconnect the specified user from the Advantage Database Server

Syntax

| UNSIGNED32 | AdsMgKillUser ( ADSHANDLE hMgmtConnect,  UNSIGNED8 \*pucUserName,  UNSIGNED16 usConnNumber ); |

Parameters

| hMgmtConnect (I) | Management API connection handle of server which contains user to kill. |
| pucUserName (I) | User name of the user to kill. The user name of an Advantage client is the client computer name or the client computer name then the client OS user login name separated by a backslash '\'. When connected to the [root dictionary](master_root_dictionary.md) as [SERVER:Admin](master_database_base_roles.md), this parameter can be an asterisk (\*) to indicate that all connections be disconnected. |
| usConnNumber (I) | Deprecated and now ignored. |

Remarks

AdsMgKillUser will disconnect the specified Advantage user from the Advantage Database Server. AdsMgKillUser is a potentially dangerous operation and should be used with extreme caution. AdsMgKillUser will cause the specified user to be abnormally disconnected from the Advantage Database Server. If the user is currently in the midst of an operation, that operation may not be able to run to completion. If the specified user is currently in a transaction, that transaction will be rolled back before the user is disconnected. All records locked by the specified user will be unlocked. All files open by the specified user will be closed. The specified user will then be disconnected. Unpredictable Advantage errors may be received by the Advantage application immediately after it has been "killed".

AdsMgKillUser should NOT be used to disconnect the current application from the Advantage Database Server. AdsDisconnect should be used in this instance.

If more that one Advantage client that is connected to the Advantage Database Server has the specified user name, they will all be disconnected from the Advantage Database Server. That is, if two users named "BRAD" are connected to the Advantage Database Server, then a call to AdsMgKillUser( nHandle, "BRAD", 0 ) will disconnect both BRAD users. To be more specific with the pucUserName parameter, the operating system user login name can be specified along with the regular user name (i.e., client's computer name). For example, if BRAD and SUZY are logged into two different computers with the same name (WORKSTATION), their connections can be killed individually by specifying "WORKSTATION\BRAD" or "WORKSTATION\SUZY" for the pucUserName parameter. Trailing backslash characters on the regular user name are ignored. For example, the backslash character is ignored in "WORKSTATION\" or "BRAD\", but not in "WORKSTATION\BRAD\".

Either pucUserName must contain a user name or usConnNumber must be non-zero. If both pucUserName contains a user name and usConnNumber is non-zero, then usConnNumber will be ignored.

Beginning with v11 of Advantage, additional restrictions have been added. This procedure requires [DB:Admin](master_database_base_roles.md) membership when connected to a data dictionary, and only other users connected to the same dictionary can be killed. When connected with a free connection, it can be used to remove other free connections. When connected to the [root dictionary](master_root_dictionary.md) as [SERVER:Admin](master_database_base_roles.md), it is possible to remove any connection (similar to pre-v11 behavior).

Note In a future release of Advantage, the user name and password passed to the AdsMgConnect API may be checked to verify the application has sufficient management API privileges to access this dangerous management API.

Note AdsMgKillUser has no effect when used with the Advantage Local Server.

Example

[Click Here](ace_advantage_management_api_examples.md#adsmgkilluser_example)

See Also

[AdsMgConnect](ace_adsmgconnect.md)

[AdsMgDisconnect](ace_adsmgdisconnect.md)

[AdsMgGetUserNames](ace_adsmggetusernames.md)

[AdsMgGetOpenTables](ace_adsmggetopentables.md)

[AdsMgGetOpenIndexes](ace_adsmggetopenindexes.md)

[AdsMgGetLockOwner](ace_adsmggetlockowner.md)
