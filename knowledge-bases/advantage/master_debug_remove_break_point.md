DEBUG REMOVE BREAK POINT




Advantage Database Server 12  

DEBUG REMOVE BREAK POINT

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DEBUG REMOVE BREAK POINT |  |  | Feedback on: Advantage Database Server 12 - DEBUG REMOVE BREAK POINT master\_Debug\_remove\_break\_point Advantage SQL > Debugging SQL Script > SQL Debugging Statements > DEBUG REMOVE BREAK POINT / Dear Support Staff, |  |
| DEBUG REMOVE BREAK POINT |  |  |  |  |

Removes a break point

Syntax

DEBUG REMOVE BREAK POINT <break\_name>

 

break\_name ::= identifier

Remark

The DEBUG REMOVE BREAK POINT statement removes a break point that was created by the [DEBUG BREAK POINT](master_debug_break_point.htm) statement. The break\_name identifies the break point to remove and it must match the one specified by the DEBUG BREAK POINT statement.

Successful execution of this command removes a row from the [::DEBUG\_BREAKS](master__debug_breaks.htm) table.

Example

// Sets and removes a break point

DEBUG BREAK POINT 'CONN0001xxxx' STATEMENT 'STMT0001yyyy' AT 0 ID my\_break;

DEBUG REMOVE BREAK POINT my\_break;

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