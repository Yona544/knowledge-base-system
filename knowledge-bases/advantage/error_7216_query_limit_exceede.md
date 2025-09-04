7216 SQL Statement Limit Exceeded




Advantage Database Server 12  

7216 SQL Statement Limit Exceeded

 

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7216 SQL Statement Limit Exceeded     Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7216 SQL Statement Limit Exceeded  Advantage Error Guide Error\_7216\_query\_limit\_exceede Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7216 SQL Statement Limit Exceeded     Advantage Error Guide |  |  |  |  |

Problem:  The configured SQL statement limit was exceeded.  Beginning with v12 of Advantage, the default number of SQL statements that a connection can obtain at a given time is 50. This limitation is intended to help application developers manage resources. In some development environments, it is possible to "leak" statement handles due to programming errors.

Solution:  It is possible to increase or disable the limit for a given connection by executing the SQL statement [sp\_SetStatementLimit](master_sp_setstatementlimit.htm). Note that this must be executed on an existing statement handle if the error has already been encountered (the irony is not lost). The limit for the server itself can be changed by setting the [SQL\_STATEMENT\_LIMIT](master_sql_statement_limit.htm) configuration parameter.