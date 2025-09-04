---
title: Master Debug Break
slug: master_debug_break
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_break.htm
source: Advantage CHM
tags:
  - master
checksum: 76dd441864923103495ef3e338aed27a326f4bfa
---

# Master Debug Break

DEBUG BREAK

DEBUG BREAK

| DEBUG BREAK |  |  |  |  |

Suspends execution on a specified debuggee or all debuggees.

Syntax

DEBUG BREAK <connection\_name | ALL> [NO WAIT]

connection\_name ::= identifier

Remark

The DEBUG BREAK statement suspends execution on the specified debuggee or on all debuggees owned by the current debugger. If the debuggee is not executing any SQL script, it will be suspended when attempting to execute the next SQL script.

The debugger session is put into the wait mode (see [DEBUB WAIT](master_debug_wait.md)) unless the NO WAIT clause is specified.

This command is most useful when trying to identify long running or infinite loops in a script. After suspending the execution of a script, the execution stack may be examined to find suspicious loops.

A useful application of the DEBUG BREAK ALL command is found in conjunction with the [DEBUG DATABASE](master_debug_database.md) command to debug SQL scripts executed by applications for which the source code is not available.

Example

// Suspend execution on a debuggee

DEBUG BREAK "CONN0001xxxx"

See Also

[DEBUG BEGIN](master_debug_begin.md)

[DEBUG CONNECTION](master_debug_connection.md)

DEBUG BREAK POINT

[DEBUG RUN](master_debug_run.md)

[DEBUG WAIT](master_debug_wait.md)

[::DEBUG\_CONNECTIONS](master__debug_connections.md)

[::DEBUG\_STACK](master__debug_stack.md)

[::DEBUG\_BREAKS](master__debug_breaks.md)

[::DEBUG\_VARIABLES](master__debug_variables.md)

[::DEBUG\_SOURCES](master__debug_sources.md)
