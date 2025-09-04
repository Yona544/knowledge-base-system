SQL Statement Limit




Advantage Database Server 12  

SQL Statement Limit

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Statement Limit  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - SQL Statement Limit Advantage Database Server Master\_sql\_statement\_limit Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SQL Statement Limit  Advantage Database Server |  |  |  |  |

Default = 50

Keyword = SQL\_STATEMENT\_LIMIT

This configuration parameter controls the maximum number of SQL statements that a single connection can keep open at one time. To completely remove the limitation for all connections on the server, this value can be set to zero (0). To modify the limit for a specific connection, an application call [sp\_SetStatementLimit](master_sp_setstatementlimit.htm).

See Also

[sp\_SetStatementLimit](master_sp_setstatementlimit.htm)

[7216 Error](error_7216_query_limit_exceede.htm)