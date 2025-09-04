---
title: Ade Sqltimeout Tadsconnection
slug: ade_sqltimeout_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_sqltimeout_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 51ef885d670e794d9eba9ddebc74226d3935b6e1
---

# Ade Sqltimeout Tadsconnection

SQLTimeout

TAdsConnection.SQLTimeout

Advantage TDataSet Descendant

| TAdsConnection.SQLTimeout  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the SQL Timeout value for this connection.

Syntax

property SQLTimeout: integer

Description

Use SQLTimeout to specify a timeout (in seconds) for this connection. When the timeout is specified, that timeout will apply to any query component that is associated with this connection. For any query that exceeds the SQLTimeout value, the query is cancelled, and error 7209 (SQL Query aborted by user) is returned to the client.

The SQLTimeout setting will independently apply to the initial query execution, and to any operation that supports Advantage callback functionality, such as record movement operations (TAdsQuery.First, TAdsQuery.Last, etc.) See [Callback Functionality](master_callback_functionality.md) for an exhaustive list of operations that support callback functionality and for more information.

NOTE: The SQL timeout setting applies to an entire SQL operation from start to finish. (For instance, if a table that has a trigger defined is updated via SQL, the timeout value applies to the update operation, in addition to the trigger execution time.)

See also

[TAdsQuery.SQLTimeout](ade_sqltimeout_tadsquery.md)

[AdsSetSQLTimeout](ace_adssetsqltimeout.md)

[Callback Functionality](master_callback_functionality.md)
