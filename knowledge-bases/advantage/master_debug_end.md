DEBUG END




Advantage Database Server 12  

DEBUG END

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DEBUG END  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DEBUG END Advantage SQL Engine master\_Debug\_end Advantage SQL > Debugging SQL Script > SQL Debugging Statements > DEBUG END / Dear Support Staff, |  |
| DEBUG END  Advantage SQL Engine |  |  |  |  |

Stops the debugger session on the current connection.

Syntax

DEBUG END

Remark

The DEBUG END statement terminates the debugger session that was started with the [DEBUG BEGIN](master_debug_end.htm) statement on the current connection. An error will be returned if the statement is not executed in an active debugger session. Execution of this statement will terminate all debuggee sessions owned by this debugger all break points will be cleared and debuggee connections will resume normal execution. After the successful execution of this statement, all debug related temporary tables will be deleted and no longer available.

See Also

[DEBUG BEGIN](master_debug_begin.htm)