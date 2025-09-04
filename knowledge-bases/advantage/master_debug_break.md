DEBUG BREAK




Advantage Database Server 12  

DEBUG BREAK

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DEBUG BREAK |  |  | Feedback on: Advantage Database Server 12 - DEBUG BREAK master\_Debug\_break Advantage SQL > Debugging SQL Script > SQL Debugging Statements > DEBUG BREAK / Dear Support Staff, |  |
| DEBUG BREAK |  |  |  |  |

Suspends execution on a specified debuggee or all debuggees.

Syntax

DEBUG BREAK <connection\_name | ALL> [NO WAIT]

connection\_name ::= identifier

Remark

The DEBUG BREAK statement suspends execution on the specified debuggee or on all debuggees owned by the current debugger. If the debuggee is not executing any SQL script, it will be suspended when attempting to execute the next SQL script.

The debugger session is put into the wait mode (see [DEBUB WAIT](master_debug_wait.htm)) unless the NO WAIT clause is specified.

This command is most useful when trying to identify long running or infinite loops in a script. After suspending the execution of a script, the execution stack may be examined to find suspicious loops.

A useful application of the DEBUG BREAK ALL command is found in conjunction with the [DEBUG DATABASE](master_debug_database.htm) command to debug SQL scripts executed by applications for which the source code is not available.

Example

// Suspend execution on a debuggee

DEBUG BREAK "CONN0001xxxx"

See Also

[DEBUG BEGIN](master_debug_begin.htm)

[DEBUG CONNECTION](master_debug_connection.htm)

DEBUG BREAK POINT

[DEBUG RUN](master_debug_run.htm)

[DEBUG WAIT](master_debug_wait.htm)

[::DEBUG\_CONNECTIONS](master__debug_connections.htm)

[::DEBUG\_STACK](master__debug_stack.htm)

[::DEBUG\_BREAKS](master__debug_breaks.htm)

[::DEBUG\_VARIABLES](master__debug_variables.htm)

[::DEBUG\_SOURCES](master__debug_sources.htm)