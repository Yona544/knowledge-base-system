---
title: Master Debug Wait
slug: master_debug_wait
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_wait.htm
source: Advantage CHM
tags:
  - master
checksum: fec16df44eedce7551f56d742191203a671691d9
---

# Master Debug Wait

DEBUG WAIT

DEBUG WAIT

| DEBUG WAIT |  |  |  |  |

Waits for the execution of any debuggee in the current debugger session to end.

Syntax

DEBUG WAIT

 

Remarks

The DEBUG WAIT statement causes the current debugger session to wait until a debuggee is suspended or the DEBUG WAIT is cancelled. Putting the debugger into wait mode allows the debugger to respond to a break point immediately without the need to poll the [::DEBUG\_CONNECTIONS](master__debug_connections.md) table. Once the statement returns, the [::DEBUG\_CONNECTIONS](master__debug_connections.md) table can be examined to determine the connection that has been suspended and the appropriate [DEBUG RUN](master_debug_run.md) command to issue.

If there is already a suspended debuggee when this statement is executed, the statement will return immediately.

To cancel the statement, see AdsRegisterCallBackFunction(). When the statement is cancelled success is returned.

Example

// Set a transient break point at the beginning of the script

// execution on a query handle and do not return until the

// break point was hit.

DEBUG BREAK POINT "CONN0001xxxx" STATEMENT "STMT0001yyyy" AT 0 TRANSIENT;

DEBUG WAIT; // wait for the debuggee suspension

See Also

[DEBUG BEGIN](master_debug_begin.md)

[DEBUG CONNECTION](master_debug_connection.md)

DEBUG BREAK POINT

[DEBUG RUN](master_debug_run.md)

[::DEBUG\_CONNECTIONS](master__debug_connections.md)

[::DEBUG\_STACK](master__debug_stack.md)

[::DEBUG\_BREAKS](master__debug_breaks.md)

[::DEBUG\_VARIABLES](master__debug_variables.md)

[::DEBUG\_SOURCES](master__debug_sources.md)
