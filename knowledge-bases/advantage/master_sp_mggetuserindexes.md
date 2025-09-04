sp\_mgGetUserIndexes




Advantage Database Server 12  

sp\_mgGetUserIndexes

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetUserIndexes  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetUserIndexes Advantage SQL Engine master\_Sp\_mggetuserindexes Advantage SQL > System Procedures > Procedures > sp\_mgGetUserIndexes / Dear Support Staff, |  |
| sp\_mgGetUserIndexes  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all open index files for the specified user.

Syntax

EXECUTE PROCEDURE sp\_mgGetUserIndexes( UserName,Character,200 )

Parameters

|  |  |
| --- | --- |
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

[sp\_mgGetAllIndexes](master_sp_mggetallindexes.htm)

[sp\_mgGetIndexUsers](master_sp_mggetindexusers.htm)

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.htm)