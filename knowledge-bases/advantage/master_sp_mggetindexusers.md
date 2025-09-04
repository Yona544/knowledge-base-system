sp\_mgGetIndexUsers




Advantage Database Server 12  

sp\_mgGetIndexUsers

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetIndexUsers  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetIndexUsers Advantage SQL Engine master\_Sp\_mggetindexusers Advantage SQL > System Procedures > Procedures > sp\_mgGetIndexUsers / Dear Support Staff, |  |
| sp\_mgGetIndexUsers  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all users that have the specified index file opened.

Syntax

EXECUTE PROCEDURE sp\_mgGetIndexUsers( IndexName,Character,255 )

Parameters

|  |  |
| --- | --- |
| IndexName (I) | Name of the index in question. |
| UserName (O) | Name of the connected user. |
| ConnNumber (O) | NetWare connection number. (Deprecated) |
| DictionaryUser (O) | Name of user that has authenticated to an Advantage Data Dictionary. |
| Address (O) | IP or IPX address of the connected user. |
| OSUserLoginName (O) | Operating system login name of the connected user. |
| TSAddress (O) | Terminal Server Client IP address if the connection is made from a Terminal Server session. |

Remarks

The given IndexName should be a fully qualified UNC path to the index file. UserName will be the name of the computer the user is connected from.  OSUserLoginName will be the operating system user name of the user. DictionaryUser will be the data dictionary user name if the user is authenticated to a data dictionary.

Note With Advantage Local Server, sp\_mgGetIndexUsers will only return users who have the index opened by the instance of Advantage Local Server currently loaded into memory.

 

Example

EXECUTE PROCEDURE sp\_mgGetIndexUsers( '\\server\share\data\index.adi' );

See Also

[sp\_mgGetAllIndexes](master_sp_mggetallindexes.htm)

[sp\_mgGetUserIndexes](master_sp_mggetuserindexes.htm)