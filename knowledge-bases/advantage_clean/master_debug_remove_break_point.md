---
title: Master Debug Remove Break Point
slug: master_debug_remove_break_point
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_remove_break_point.htm
source: Advantage CHM
tags:
  - master
checksum: 9c64d6208f276e76f9b04b026e2a5ae44dfb5bf5
---

# Master Debug Remove Break Point

DEBUG REMOVE BREAK POINT

DEBUG REMOVE BREAK POINT

| DEBUG REMOVE BREAK POINT |  |  |  |  |

Removes a break point

Syntax

DEBUG REMOVE BREAK POINT <break\_name>

 

break\_name ::= identifier

Remark

The DEBUG REMOVE BREAK POINT statement removes a break point that was created by the [DEBUG BREAK POINT](master_debug_break_point.md) statement. The break\_name identifies the break point to remove and it must match the one specified by the DEBUG BREAK POINT statement.

Successful execution of this command removes a row from the [::DEBUG\_BREAKS](master__debug_breaks.md) table.

Example

// Sets and removes a break point

DEBUG BREAK POINT 'CONN0001xxxx' STATEMENT 'STMT0001yyyy' AT 0 ID my\_break;

DEBUG REMOVE BREAK POINT my\_break;

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
