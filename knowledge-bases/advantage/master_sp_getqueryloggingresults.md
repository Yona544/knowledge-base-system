sp\_GetQueryLoggingResults




Advantage Database Server 12  

sp\_GetQueryLoggingResults

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_GetQueryLoggingResults  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_GetQueryLoggingResults Advantage SQL Engine master\_sp\_GetQueryLoggingResults Advantage SQL > System Procedures > Procedures > sp\_GetQueryLoggingResults / Dear Support Staff, |  |
| sp\_GetQueryLoggingResults  Advantage SQL Engine |  |  |  |  |

Retrieves the contents of the active query logging table.

Syntax

sp\_GetQueryLoggingResults(

 EncryptionPassword, Character, 255 )

Parameters

|  |  |
| --- | --- |
| EncryptionPassword (I) | On free connections, the password to use if the log table is encrypted. |

Output

|  |  |
| --- | --- |
| ID (O) | Unique identifier for the query. |
| Start Time (O) | Time and date that the query was began. |
| Optimized (O) | True if the query is properly optimized. |
| Return Code (O) | Return Value of the query. |
| Rows Affected (O) | Number of rows affected by the query. |
| End Time (O) | Time and date that the query was ended. |
| Run Time (O) | Elapsed time the query was processed by the server in milliseconds. |
| Database (O) | Name of the database the user is connected to. |
| User Name (O) | User name for data dictionary connections. |
| Connection Name (O) | Connection name. |
| Application ID (O) | Application ID of the application executing the query. |
| Query (O) | The query that was executed. |

Remarks

sp\_getQueryLoggingResults can be used to retrieve the contents of the Query Logging output table while query logging is currently active.  While the results can be retrieved either by directly opening the table or using an SQL statement, this procedure is useful if Query Logging is currently enabled to retrieve the results of the active query log.  To retrieve logging information on a data dictionary, the user must be logged in as the administrative user, ADSSYS or be a member of the DB:Admin group.

Example

EXECUTE PROCEDURE sp\_GetQueryLoggingResults( null );

See Also

[sp\_EnableQueryLogging](master_sp_enablequerylogging.htm)

[sp\_DisableQueryLogging](master_sp_disablequerylogging.htm)

[sp\_ViewQueryLogging](master_sp_viewquerylogging.htm)