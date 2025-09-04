---
title: Master Debug Database
slug: master_debug_database
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_database.htm
source: Advantage CHM
tags:
  - master
checksum: 3475408988875f47983e5c6a2f38909fd354ca21
---

# Master Debug Database

DEBUG DATABASE

DEBUG DATABASE

Advantage SQL Engine

| DEBUG DATABASE  Advantage SQL Engine |  |  |  |  |

Alters the default database debugger status of the current debugger session.

Syntax

DEBUG DATABASE [END]

Remark

The DEBUG DATABASE statement makes the current debugger session the default debugger of the connected database.

The DEBUG DATABASE END statement reverses the effect of the DEBUG DATABASE statement.

This statement is only valid after starting a debugger session on the current connection with the [DEBUG BEGIN](master_debug_begin.md) statement. The debugger connection must be a database connection, and the user of the current connection must also be a member of the [DB:Admin](master_database_base_roles.md) or [DB:Debug](master_database_base_roles.md) groups. There can be only one default debugger for a database. If there is already a default debugger session to the connected database or if the connection is not a database connection, an error will be returned.

After the current debugger session becomes the default debugger of the database, any new connection to the database automatically becomes the debuggee of the current debugger. This feature makes it possible to debug SQL scripts from any application, even when the source code of the application is not available.

Note With the Advantage Database Server, there can be one default debugger per database and it can debug any SQL scripts executing on connections to that database. There may be multiple default debugger sessions active, as long as they are connected to different databases. With Advantage Local Server, only one debugger session may be designated as the default debugger per process (application).

Example

// The following script will start a debug session and

// poll the ::DEBUG\_CONNECTIONS table until the

// next connection to the database becomes a debuggee.

// Note that the script will run until the execution is

// cancelled or a new connection is made to the database

DEBUG BEGIN;

DEBUG DATABASE;

WHILE 0 = ( SELECT COUNT(\*) FROM #::DEBUG\_CONNECTIONS WHERE Debugger = 1 ) DO

END;

See Also

[DEBUG BEGIN](master_debug_begin.md)

[DEBUG CONNECTION](master_debug_connection.md)

[::DEBUG\_CONNECTIONS](master__debug_connections.md)

[::DEBUG\_STACK](master__debug_stack.md)

[::DEBUG\_BREAKS](master__debug_breaks.md)

[::DEBUG\_VARIABLES](master__debug_variables.md)

[::DEBUG\_SOURCES](master__debug_sources.md)
