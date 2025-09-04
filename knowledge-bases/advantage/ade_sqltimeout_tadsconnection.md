SQLTimeout




Advantage Database Server 12  

TAdsConnection.SQLTimeout

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.SQLTimeout  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.SQLTimeout Advantage TDataSet Descendant ade\_Sqltimeout\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.SQLTimeout  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the SQL Timeout value for this connection.

Syntax

property SQLTimeout: integer

Description

Use SQLTimeout to specify a timeout (in seconds) for this connection. When the timeout is specified, that timeout will apply to any query component that is associated with this connection. For any query that exceeds the SQLTimeout value, the query is cancelled, and error 7209 (SQL Query aborted by user) is returned to the client.

The SQLTimeout setting will independently apply to the initial query execution, and to any operation that supports Advantage callback functionality, such as record movement operations (TAdsQuery.First, TAdsQuery.Last, etc.) See [Callback Functionality](master_callback_functionality.htm) for an exhaustive list of operations that support callback functionality and for more information.

NOTE: The SQL timeout setting applies to an entire SQL operation from start to finish. (For instance, if a table that has a trigger defined is updated via SQL, the timeout value applies to the update operation, in addition to the trigger execution time.)

See also

[TAdsQuery.SQLTimeout](ade_sqltimeout_tadsquery.htm)

[AdsSetSQLTimeout](ace_adssetsqltimeout.htm)

[Callback Functionality](master_callback_functionality.htm)