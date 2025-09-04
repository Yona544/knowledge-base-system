error\_5226\_query\_logging\_error




Advantage Database Server 12  

5226 Query Logging Error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5226 Query Logging Error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5226 Query Logging Error Advantage Error Guide Error\_5226\_query\_logging\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5226 Query Logging Error  Advantage Error Guide |  |  |  |  |

An operation involving query logging failed.  The error text associated with this error should contain additional information on identifying the problem.

Problem:  Query Logging is already enabled on this database.

Solution:  Query logging can only be enabled once per dictionary or once for all free table connections.  Details regarding the running query log job can be found using the [sp\_ViewQueryLogging](master_sp_viewquerylogging.htm) system stored procedure.

Problem:  Schema is not compatible with the current query logging table.

Solution:  If using an existing query logging table, ensure the schema of the table matches the schema required by query logging. Note, the schema may change between major versions of Advantage.

Problem:  Query Logging is not enabled on this database.

Solution:  Ensure that query logging is enabled prior to calling the [sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.htm) system procedure.