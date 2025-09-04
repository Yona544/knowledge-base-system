---
title: Master Debug Run
slug: master_debug_run
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debug_run.htm
source: Advantage CHM
tags:
  - master
checksum: 1140a55a1f09bb2e35796381f5047fa47c207e96
---

# Master Debug Run

DEBUG RUN

DEBUG RUN

| DEBUG RUN |  |  |  |  |

Resumes execution on a suspended debuggee.

Syntax

DEBUG RUN <connection\_name> [STEP INTO | STEP OVER | STEP OUT | TO <offset> [IN <ObjectType> [<ParentName>.]<ObjectName>] | IN BASE SCRIPT>] [NO WAIT]

connection\_name ::= identifier

offset ::= integer

ObjectType ::= TRIGGER | PROCEDURE | FUNCTION

ParentName ::= identifier

ObjectName ::= identifier

Remark

The DEBUG RUN statement resumes a suspended debuggee with various options. The debuggee specified by the connection\_name must be suspended as indicated in the [::DEBUG\_CONNECTIONS](master__debug_connections.md) table.

The options for resuming the execution are:

STEP INTO: The current statement will be executed and if the current statement cause another SQL script to be executed because of a trigger, stored procedure or user defined function, the execution will be suspended immediately upon entering the script.

STEP OVER: The current statement will be executed and execution will be suspended before the next statement in the current SQL script. If there are no more statements in the script, execution will be suspended in any parent script.

STEP OUT: All remaining statements in the current script will be executed unless a break point is encountered. The execution will be suspended upon returning to the parent script.

TO offset [IN <ObjectType> [<ParentName>.]<ObjectName>] | IN BASE SCRIPT: Execution on the specified debuggee will be resumed only suspending when the specified offset is reached or a break point is encountered. The offset may be in a database object or the base original script. For a description of the offset value see [DEBUG BREAK POINT](master_debug_break_point.md). If the specified location is never reached, the execution will continue until completion of the scrip. This is identical to setting a transient break point at the specified location.

If no option is specified, execution will resume until the next break point is encountered or the script finishes.

The DEBUB RUN command also puts the debugger session into wait mode (see [DEBUG WAIT](master_debug_wait.md)) unless the NO WAIT clause is specified.

Example 1

// Resumes a suspend script and suspends the execution after executing

// the current statement in the script

DEBUG RUN "CONN0001xxxx" STEP OVER

 

Example 2

// Resumes a suspend script and continues the execution until we entered

// the user defined function GetMaxID()

DEBUG RUN "CONN0001xxxx" TO 0 IN FUNCTION myTestFuncs.GetMaxID

Example 3

// Resumes execution on three suspended debuggees then wait for

// the execution suspension signal again.

DEBUG RUN "CONN0001xxxx" NO WAIT;

DEBUG RUN "CONN0002yyyy" NO WAIT;

DEBUG RUN "CONN0003zzzz" NO WAIT;

DEBUG WAIT;

See Also

[DEBUG BEGIN](master_debug_begin.md)

[DEBUG CONNECTION](master_debug_connection.md)

DEBUG BREAK POINT

[DEBUG WAIT](master_debug_wait.md)

[::DEBUG\_CONNECTIONS](master__debug_connections.md)

[::DEBUG\_STACK](master__debug_stack.md)

[::DEBUG\_BREAKS](master__debug_breaks.md)

[::DEBUG\_VARIABLES](master__debug_variables.md)

[::DEBUG\_SOURCES](master__debug_sources.md)
