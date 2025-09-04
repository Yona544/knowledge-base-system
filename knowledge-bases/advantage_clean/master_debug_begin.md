---
title: Master Debug Begin
slug: master_debug_begin
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_begin.htm
source: Advantage CHM
tags:
  - master
checksum: 1afcdcafd42cd5e45b2ff8f94e96c411505570bb
---

# Master Debug Begin

DEBUG BEGIN

DEBUG BEGIN

Advantage SQL Engine

| DEBUG BEGIN  Advantage SQL Engine |  |  |  |  |

Starts a debugger session on the current connection.

Syntax

DEBUG BEGIN

Remark

The DEBUG BEGIN statement starts a debugger session on the current connection. All other DEBUG commands are not valid until a debugger session has been started. After the successful execution of this statement, the debug related temporary tables become available on the current connection and may be examined before performing other debug related operations.

Once the debugger session is started, depending on the role of the connected user, it can be used to debug SQL scripts running on any other connections connected to the same database, or it can be used to debug any query executed on any free connection.

Note With Advantage Local Server, the debugger session can only debug SQL scripts running in the same process (application).

See Also

[DEBUG END](master_debug_end.md)

[DEBUG CONNECTION](master_debug_connection.md)

[DEBUG DATABASE](master_debug_database.md)

[::DEBUG\_CONNECTIONS](master__debug_connections.md)

[::DEBUG\_STACK](master__debug_stack.md)

[::DEBUG\_BREAKS](master__debug_breaks.md)

[::DEBUG\_VARIABLES](master__debug_variables.md)

[::DEBUG\_SOURCES](master__debug_sources.md)
