Debugging SQL Script




Advantage Database Server 12  

Debugging SQL Script Overview

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Debugging SQL Script Overview  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Debugging SQL Script Overview Advantage SQL Engine master\_Debugging\_sql\_script Advantage SQL > Debugging SQL Script > Debugging SQL Script Overview / Dear Support Staff, |  |
| Debugging SQL Script Overview  Advantage SQL Engine |  |  |  |  |

The Advantage Query Engine supports a set of statements that allows the developer to debug SQL scripts. In addition to SQL scripts that are executed directly, scripts embedded in triggers, stored procedures, and user defined functions can be debugged as well. Advantage Data Architects interactive SQL debugger is implemented using this set of SQL statements. While, the information on specific "DEBUG " statements will mostly be useful for developers who wish to implement their own SQL debugger, the generally information on the capability of the debugger should be useful for all users.

The SQL debug commands are available for both Advantage Local Server and Advantage Database Server. They can be used to debug a specific query, a specific connection or all connections to a specific database. The debugging process starts when a debugger session is initiated on a connection (debugger). The debugger can then designate one or more other connection(s) as debuggee, though the common scenario is that one debugger controls one debuggee. SQL statements or scripts executed on the debuggee connection(s) may be suspended or otherwise controlled by the debugger. The status of the debuggee(s) and the execution of the SQL script are reported to the debugger via the "::DEBUG\_XXX" temporary tables.

With Advantage Local Server, the only connections that can be debugged are the ones in the same process (application) as the debugger and there can be only one default database debugger active, see [DEBUG DATABASE](master_debug_database.htm).

With Advantage Database Server, a debugger with proper permissions can debug SQL scripts running on any connection and more than one default database debugger can be active as long as they are connected to different databases.

A limitation with Advantage Database Server is that the number of connections that may be debugged (debuggees) at the same time is limited by the number of configured worker threads. Specifically, the number of debuggees is limited to number of configured worker threads minus one. The reason for this limitation is that when the execution of the SQL script on a debuggee is suspended, a worker thread is suspended. Limiting the number of debuggees eliminates the possibility of locking up the server when all worker threads are suspended.

See Also

[DEBUG BEGIN](master_debug_begin.htm)

[DEBUG END](master_debug_end.htm)

[DEBUG DATABASE](master_debug_database.htm)

[DEBUG CONNECTION](master_debug_connection.htm)

[DEBUG BREAK POINT](master_debug_break_point.htm)

[DEBUG REMOVE BREAK POINT](master_debug_remove_break_point.htm)

[DEBUG BREAK](master_debug_break.htm)

[DEBUG RUN](master_debug_run.htm)

[DEBUG WAIT](master_debug_wait.htm)

[::DEBUG\_CONNECTIONS](master__debug_connections.htm)

[::DEBUG\_STATEMENTS](master__debug_statements.htm)

[::DEBUG\_STACK](master__debug_stack.htm)

[::DEBUG\_BREAKS](master__debug_breaks.htm)

[::DEBUG\_VARIABLES](master__debug_variables.htm)

[::DEBUG\_SOURCES](master__debug_sources.htm)

[::conn.name](master_system_variables.htm)

[::stmt.name](master_system_variables.htm)