sp\_mgGetAllIndexes




Advantage Database Server 12  

sp\_mgGetAllIndexes

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetAllIndexes  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetAllIndexes Advantage SQL Engine master\_Sp\_mggetallindexes Advantage SQL > System Procedures > Procedures > sp\_mgGetAllIndexes / Dear Support Staff, |  |
| sp\_mgGetAllIndexes  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all the index files that are currently opened on the server.

Syntax

EXECUTE PROCEDURE sp\_mgGetAllIndexes()

Parameters

|  |  |
| --- | --- |
| IndexName (O) | Full path and file name of each index file currently open on the server. |

Remarks

This procedure returns the fully qualified path names of all index files that are opened on the server by all users.

Note With Advantage Local Server, sp\_mgGetAllIndexes will only return information about indexes opened by the instance of Advantage Local Server currently loaded into memory. Information about indexes opened by other instances of Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetAllIndexes();

See Also

[sp\_mgGetTableIndexes](master_sp_mggettableindexes.htm)

[sp\_mgGetUserIndexes](master_sp_mggetuserindexes.htm)

[sp\_mgGetAllTables](master_sp_mggetalltables.htm)