sp\_ViewQueryLogging




Advantage Database Server 12  

sp\_ViewQueryLogging

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ViewQueryLogging  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ViewQueryLogging Advantage SQL Engine master\_Sp\_viewquerylogging Advantage SQL > System Procedures > Procedures > sp\_ViewQueryLogging / Dear Support Staff, |  |
| sp\_ViewQueryLogging  Advantage SQL Engine |  |  |  |  |

Displays which connections are logging queries.

Syntax

sp\_ViewQueryLogging()

Parameters

|  |  |
| --- | --- |
| Database (O) | Fully qualified path to the data dictionary logging queries. |
| Table (O) | Fully qualified path to the table queries are being logged in. |

Remarks

sp\_ViewQueryLogging returns a result set of all connections currently logging queries.

See Also

[sp\_EnableQueryLogging](master_sp_enablequerylogging.htm)

[sp\_DisableQueryLogging](master_sp_disablequerylogging.htm)

[sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.htm)