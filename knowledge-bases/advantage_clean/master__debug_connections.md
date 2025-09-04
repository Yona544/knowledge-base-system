---
title: Master Debug Connections
slug: master__debug_connections
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master__debug_connections.htm
source: Advantage CHM
tags:
  - master
checksum: 8c9c3f9ddd46b373059d57ade59ed1c0f5e5d728
---

# Master Debug Connections

::DEBUG\_CONNECTIONS

::DEBUG\_CONNECTIONS

| ::DEBUG\_CONNECTIONS |  |  |  |  |

The ::DEBUG\_CONNECTIONS table holds information about the connections that are available to the current debugger session.

Definition

| Field Name | Field Type | Field Size | Description |
| user\_id | Integer | 4 | Primary key of the table. It uniquely identifies the connection. |
| conn\_name | CiChar | 50 | Name of the connection. This value may be used in DEBUG commands where a connection\_name value is required.  The value in this column is unique to the table.  The value is the same as the ::conn.name system variable. |
| Status | CiChar | 20 | Status of this connection. Possible values for this column are:  Suspended: The debuggee was suspended. The [DEBUG RUN](master_debug_run.md) command may be issued on this debuggee to resume execution.  Running (debug): The debuggee was running in debug mode and may be suspended using the [DEBUG BREAK](master_debug_break.md) command. The execution may also suspend when a break point is encountered.  Running: The connection is currently not running in debug mode. It is either not executing any statement currently or the connection is not a debuggee owned by the current debugger session. |
| Type | CiChar | 30 | Type of this connection. Possible values are:  Not in debug mode: The connection is not a debuggee.  Debugging connection: The connection is a debuggee owned by the current debugger session and all query handles, when executing queries, will be running in debug mode.  Debugging statements: The connection is a debuggee owned by the current debugger session but only certain query handles are being debugged. The query handles that are being debugged can be found in the [::DEBUG\_STATEMENTS](master__debug_statements.md) table.  Debugged by other debugger: The connection is being debugged by other debugger.  Connection is a debugger: The connection is a debugger. |
| Debugger | Integer | 4 | A numeric representation of the connection type, values 0 4 repectively. |

Remark

If the current debugger session is on a database connection, the ::DEBUG\_CONNECTIONS table will contain all connections to the same database. If the current debugger connection is a free connection, the ::DEBUG\_CONNECTIONS table will only contain debuggees that are owned by the current debugger session.

If using Advantage Local Server, only connections in the same process will be in the table.

The debugger can retrieve the value from the conn\_name column and put specified connection into debug mode if the debugger has sufficient privilege.
