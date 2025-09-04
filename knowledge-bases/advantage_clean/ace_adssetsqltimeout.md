---
title: Ace Adssetsqltimeout
slug: ace_adssetsqltimeout
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetsqltimeout.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 913c652fdf8eb9aca6294d89ae8827ac79ecf3ab
---

# Ace Adssetsqltimeout

AdsSetSQLTimeout

AdsSetSQLTimeout

Advantage Client Engine

| AdsSetSQLTimeout  Advantage Client Engine |  |  |  |  |

Sets the SQL Timeout on a Connection or Statement.

Syntax

| UNSIGNED32 | AdsSetSQLTimeout( ADSHANDLE hObj,  UNSIGNED32 ulTimeout ); |

Parameters

| hObj (I) | Handle of connection or statement. |
| ulTimeout (I) | Timeout value in seconds. |

Remarks

AdsSetSQLTimeout sets the optional SQL timeout value (in seconds) for a given connection or statement handle. When a timeout is specified for a connection handle, that timeout value will apply to all SQL statement handles created on that connection. When a timeout is specified for a statement handle, the SQL timeout applies only queries executed on that statement object. For any query that exceeds the Timeout value, the query is cancelled, and error 7209 (SQL query aborted by user) is returned to the client.

If an SQL timeout is specified for both the statement and the associated connection, the statement SQL timeout will be used.

The SQL Timeout setting will independently apply to the initial query execution, and to any operation that supports Advantage callback functionality, such as record movement operations (AdsSkip, AdsGotoRecord, AdsGotoTop, etc.). See [Callback Functionality](master_callback_functionality.md) for an exhaustive list of operations that support callback functionality and for more information.

Note

The SQL timeout setting applies to an entire SQL operation from start to finish. (For instance, if a table that has a trigger defined is updated via SQL, the timeout value applies to the update operation, in addition to the trigger execution time.)

Example

AdsCreateSQLStatement( hConnect, &hStatement );

// Set a 5-second SQL Timeout

AdsSetSQLTimeout( hStatement, 5 );

// This query will have 5 seconds to finish

AdsExecuteSQLDirect( hStatement,

"select \* from demo10",

&hCursor );

// This call will also have 5 seconds to finish

AdsGotoBottom( hCursor );

// Now clear the SQL timeout

AdsSetSQLTimeout( hStatement, ADS\_DEFAULT\_SQL\_TIMEOUT );

See Also

[Callback Functionality](master_callback_functionality.md)
