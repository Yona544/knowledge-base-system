---
title: Master Sp Mggetuserindexes
slug: master_sp_mggetuserindexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetuserindexes.htm
source: Advantage CHM
tags:
  - master
checksum: 060756c25a55d5819f5d1b9dcffb34ba82fc4c95
---

# Master Sp Mggetuserindexes

sp\_mgGetUserIndexes

sp\_mgGetUserIndexes

Advantage SQL Engine

| sp\_mgGetUserIndexes  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all open index files for the specified user.

Syntax

EXECUTE PROCEDURE sp\_mgGetUserIndexes( UserName,Character,200 )

Parameters

| UserName (I) | Name of the connected user. |
| IndexName (O) | Fully qualified path to the index file. |

Remarks

The index names returned are the fully qualified paths to the index files on the server. To be more specific with the user name parameter, the user name (client computer name) and the operating system user login name can be specified together (computer name first), separated by a backslash '\'.

Note With Advantage Local Server, sp\_mgGetUserIndexes will only return indexes open by this user in the instance of Advantage Local Server currently loaded into memory. Information about tables the user has opened in other instances of the Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetUserIndexes( 'username');

To retrieve index names using a computername and username combo, separate them with a backslash:

EXECUTE PROCEDURE sp\_mgGetUserIndexes( 'workstation\username' )

 

Trailing backslash characters after the computer name are ignored:

EXECUTE PROCEDURE sp\_mgGetUserIndexes( 'workstation\' )

 

See Also

[sp\_mgGetAllIndexes](master_sp_mggetallindexes.md)

[sp\_mgGetIndexUsers](master_sp_mggetindexusers.md)

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.md)
