DEBUG BEGIN




Advantage Database Server 12  

DEBUG BEGIN

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DEBUG BEGIN  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DEBUG BEGIN Advantage SQL Engine master\_Debug\_begin Advantage SQL > Debugging SQL Script > SQL Debugging Statements > DEBUG BEGIN / Dear Support Staff, |  |
| DEBUG BEGIN  Advantage SQL Engine |  |  |  |  |

Starts a debugger session on the current connection.

Syntax

DEBUG BEGIN

Remark

The DEBUG BEGIN statement starts a debugger session on the current connection. All other DEBUG commands are not valid until a debugger session has been started. After the successful execution of this statement, the debug related temporary tables become available on the current connection and may be examined before performing other debug related operations.

Once the debugger session is started, depending on the role of the connected user, it can be used to debug SQL scripts running on any other connections connected to the same database, or it can be used to debug any query executed on any free connection.

Note With Advantage Local Server, the debugger session can only debug SQL scripts running in the same process (application).

See Also

[DEBUG END](master_debug_end.htm)

[DEBUG CONNECTION](master_debug_connection.htm)

[DEBUG DATABASE](master_debug_database.htm)

[::DEBUG\_CONNECTIONS](master__debug_connections.htm)

[::DEBUG\_STACK](master__debug_stack.htm)

[::DEBUG\_BREAKS](master__debug_breaks.htm)

[::DEBUG\_VARIABLES](master__debug_variables.htm)

[::DEBUG\_SOURCES](master__debug_sources.htm)