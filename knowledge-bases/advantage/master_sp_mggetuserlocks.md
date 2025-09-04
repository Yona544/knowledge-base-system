sp\_mgGetUserLocks




Advantage Database Server 12  

sp\_mgGetUserLocks

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetUserLocks  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetUserLocks Advantage SQL Engine master\_Sp\_mggetuserlocks Advantage SQL > System Procedures > Procedures > sp\_mgGetUserLocks / Dear Support Staff, |  |
| sp\_mgGetUserLocks  Advantage SQL Engine |  |  |  |  |

Returns a result containing the record numbers of all records locked on the specified table by the specified user.

Syntax

EXECUTE PROCEDURE sp\_mgGetUserLocks( TableName,Character,255;

UserName,Character,200 )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Fully qualified path to the table. |
| UserName (I) | Name of the connected user. |
| LockedRecNo (O) | Record number of locked record. |

Remarks

The table name must be the fully qualified path to the table on the server. The user name must be the Advantage clients computer name. To be more specific with the user name parameter, the user name (client computer name) and the operating system user login name can be specified together (computer name first), separated by a backslash '\'.

Note With Advantage Local Server, sp\_mgGetUserLocks will only return locks instantiated by the user in the instance of Advantage Local Server currently loaded into memory. Information about locks the user has instantiated in other instances of the Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetUserLocks( '\\server\share\data\table.adt', 'user' );

 

To retrieve user locks using a computername and username combo, separate them with a backslash:

EXECUTE PROCEDURE sp\_mgGetUserLocks( '\\server\share\data\table.adt', 'workstation\username' )

 

Trailing backslash characters after the computer name are ignored:

EXECUTE PROCEDURE sp\_mgGetUserLocks( '\\server\share\data\table.adt', 'workstation\' )

 

See Also

[sp\_mgGetAllLocks](master_sp_mggetalllocks.htm)

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.htm)