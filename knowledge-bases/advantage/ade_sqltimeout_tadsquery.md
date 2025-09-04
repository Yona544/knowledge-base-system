SQLTimeout




Advantage Database Server 12  

TAdsQuery.SQLTimeout

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.SQLTimeout  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.SQLTimeout Advantage TDataSet Descendant ade\_Sqltimeout\_tadsquery Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.SQLTimeout  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Specifies the SQL Timeout value for this TAdsQuery component.

Syntax

property SQLTimeout: integer

Description

Use SQLTimeout to specify a timeout (in seconds) for this query component. For any query that exceeds the SQLTimeout value, the query is cancelled, and error 7209 (SQL Query aborted by user) is returned to the client.

NOTE: If an SQLTimeout value is configured for this component, that value will override the SQLTimeout value configured for the associated TAdsConnection component.

The SQLTimeout setting will independently apply to the initial query execution, and to any operation that supports Advantage callback functionality, such as record movement operations (TAdsQuery.First, TAdsQuery.Last, etc.) See [Callback Functionality](master_callback_functionality.htm) for an exhaustive list of operations that support callback functionality and for more information.

NOTE: The SQL timeout setting applies to an entire SQL operation from start to finish. (For instance, if a table that has a trigger defined is updated via SQL, the timeout value applies to the update operation, in addition to the trigger execution time.)

See also

[TAdsConnection.SQLTimeout](ade_sqltimeout_tadsconnection.htm)

[AdsSetSQLTimeout](ace_adssetsqltimeout.htm)

[Callback Functionality](master_callback_functionality.htm)