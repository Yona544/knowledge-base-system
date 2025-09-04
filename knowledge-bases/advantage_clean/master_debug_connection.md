---
title: Master Debug Connection
slug: master_debug_connection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_connection.htm
source: Advantage CHM
tags:
  - master
checksum: 57f037c9a5bf6a155e11cfe933c3fb7304373b2c
---

# Master Debug Connection

DEBUG CONNECTION

DEBUG CONNECTION

| DEBUG CONNECTION |  |  |  |  |

Start or end debugging of a specific connection or a specific query handle.

Syntax

DEBUG CONNECTION connection\_name [STATEMENT statement\_name][END]

connection\_name ::= identifier

statement\_name ::= identifier

Remark

The DEBUG CONNECTION statement makes the connection specified by connection\_name into a debuggee of the current debugger session. After the connection becomes a debuggee of the current debugger session, the debugger may debug any SQL scripts executed on the debuggee connection by utilizing the other debug commands such setting the break points, stepping or tracing in the SQL scripts, and view the local variables on the execution stack.

The optional STATEMENT clause indicates that the debugger only wishes to gain debugging control of the specified query handle.

If the current debugger connection is a database connection, it may debug other connections without the optional STATEMENT clause, provided that the user of debugger session is a member of the [DB:Admin](master_database_base_roles.md) or [DB:Debug](master_database_base_roles.md) groups. If the current debugger connection is a free connection, then the debugger can only debug a specific query handle and the STATEMENT clause is required.

The END clause terminates the debugging process on the specified connection or the specified query. Ending the debug session will allow the SQL script(s) being debugged to continue normal execution.

The connection\_name and statement\_name are normally obtained via the ::conn.name and ::stmt.name system variables of the debuggee connection. However, if the current debugger connection is a database connection, the connection\_name can also be obtained from the [::DEBUG\_CONNECTIONS](master__debug_connections.md) table.

One debugger session can own multiple debuggee but a debuggee can belong to only one debugger session.

Example

// The following example illustrates the basic procedure to debug an

// SQL script.

// 1. Make a debuggee connection. This is the connection on which

// to run the script that will be debugged

// 2. Create a query handle on the debuggee connection and obtain the

// connection name and statement name with the following SQL:

//

// SELECT

// ::conn.name AS connection\_name,

// ::stmt.name AS statement\_name

// FROM system.iota

//

// Note the connection\_name and statement\_name from the result set.

// 3. Make a debugger connection. This is the connection where we

// execute debug commands to control the execution of the SQL

// script on the debuggee connection.

//

// 4. Execute the following script on the debugger connection to

// put the debuggees query into debug mode and set a break point

// to have the execution of the debuggee SQL script stopping

// before executing the first statement in the script.

// Assuming that the connection\_name and statement\_name from

// step 2 are 'CONN0001xxxx' and 'STMT0001yyyy' respectively:

 

DEBUG BEGIN;

DEBUG CONNECTION 'CONN0001xxxx' STATEMENT 'STMT0001yyyy';

DEBUG BREAK POINT 'CONN0001xxxx' STATEMENT 'STMT0001yyyy' AT 0 TRANSIENT;

 

// 5. Execute the script to be debugged using the query element

// on the debuggee connection. Suppose the script to be debugged

// is the following:

//

// DECLARE i Integer;

// i = 0;

// WHILE i < 3 DO

// INSERT INTO iTable ( iVal ) VALUES ( i );

// END;

//

// Because of the break point set by the debugger, the execution of the

// script on the debuggee will stop before executing the statement 'i = 0;',

// and it will require further commands from the debugger to continue the

// execution.

// 6. Once the debuggee execution is stopped, the debugger can examine the

// the call stack and local variables of the stopped script. To detect

// stopped the script, the debugger can either poll the ::DEBUG\_CONNECTIONS

// table or use the DEBUG WAIT command.

// 7. After done with debugging the script, allows the debuggee to finish

// normally by ending the debugging process on the debuggee:

 

DEBUG CONNECTION 'CONN0001xxxx' END;

See Also

[DEBUG BEGIN](master_debug_begin.md)

[DEBUG DATABASE](master_debug_database.md)

[::DEBUG\_CONNECTIONS](master__debug_connections.md)

[::DEBUG\_STACK](master__debug_stack.md)

[::DEBUG\_BREAKS](master__debug_breaks.md)

[::DEBUG\_VARIABLES](master__debug_variables.md)

[::DEBUG\_SOURCES](master__debug_sources.md)
