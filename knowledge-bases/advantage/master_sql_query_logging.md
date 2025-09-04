SQL Query Logging




Advantage Database Server 12  

SQL Query Logging

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Query Logging  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - SQL Query Logging Advantage SQL Engine master\_Sql\_query\_logging Advantage SQL > SQL Functionality > SQL Query Logging / Dear Support Staff, |  |
| SQL Query Logging  Advantage SQL Engine |  |  |  |  |

SQL query logging provides a convenient method for a developer to determine all queries executed against an Advantage Database Server or an Advantage Local Server. When query logging is enabled, each query executed will be logged to an Advantage Database Table. Because logging the query requires the Advantage Database Server or Advantage Local Server to update a table, query logging degrades performance and it is suggested that this feature only be used during development.

Only the administrative user, ADSSYS, can enable query logging for an Advantage Data Dictionary. All queries will be logged to an Advantage Database Table that is bound to that data dictionary. This allows the ADSSYS to fully control access to the table.

When logging queries ran on free connections, a single table is used to log all queries. This table can be encrypted to prevent unauthorized access.

The system procedure [sp\_EnableQueryLogging](master_sp_enablequerylogging.htm) is used to enable query logging and the system procedure [sp\_DisableQueryLogging](master_sp_disablequerylogging.htm) is used to disable query logging. If the Advantage Database Server is restarted, query logging will be disabled. Query logging must be enabled for each instance of Advantage Local Server. For example, if two different instances of Advantage Data Architect are opened, each instance of Advantage Data Architect will need to have query logging enabled on it.

See Also

[sp\_ViewQueryLogging](master_sp_viewquerylogging.htm)