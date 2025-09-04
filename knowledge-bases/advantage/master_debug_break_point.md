DEBUG BREAK POINT




Advantage Database Server 12  

DEBUG BREAK POINT

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DEBUG BREAK POINT |  |  | Feedback on: Advantage Database Server 12 - DEBUG BREAK POINT master\_Debug\_break\_point Advantage SQL > Debugging SQL Script > SQL Debugging Statements > DEBUG BREAK POINT / Dear Support Staff, |  |
| DEBUG BREAK POINT |  |  |  |  |

Adds or removes a break point in the current debugger session.

Syntax 1

DEBUG BREAK POINT <connection\_name> STATEMENT <statement\_name> AT offset [ID <break\_name> | TRANSIENT | REMOVE ]

Syntax 2

DEBUG BREAK POINT [<connection\_name> [STATEMENT <statement\_name>]] AT offset IN <ObjectType> [<ParentName>.]<ObjectName> [ID <break\_name> | TRANSIENT | REMOVE]

connection\_name ::= identifier

statement\_name ::= identifier

offset ::= integer

break\_name ::= identifier

ObjectType ::= TRIGGER | PROCEDURE | FUNCTION

ParentName ::= identifier

ObjectName ::= identifier

Remarks

The DEBUG BREAK POINT statement adds or removes a break point in the current debugger session. A break point may be set in such way to affect only a script executing on a certain query handle (syntax 1), or it may be set in a database object, such as stored procedure, trigger or user defined function, so it affects any debuggee connection that executes the specified database object (syntax 2). When using the second syntax to set a break point in a database object, the connection name and statement name are optional. If no connection name is specified, the break point is in effect on all debuggee connections of the current debugger session. If no statement name is specified but the connection name is specified, the break point is in effect on all query handles on the specified debuggee connection.

The successful execution of this statement adds a row into the [::DEBUG\_BREAKS](master__debug_breaks.htm) table.

The offset is the absolute character location from the beginning of the SQL script. The beginning of the script includes the declaration section of the script although execution can never be suspended in the declaration section. The offset does not have to be at the exact starting location of a SQL statement. It can be any character in the statement where the execution should be suspended. As far as the debugger is concern, each statement in an SQL script contains all characters after the semi-colon of the previous statement up to and including the semi-colon of the current statement. Thus, 0 can always be used as the offset for a break point to suspend the execution before executing the first statement in the SQL script because there is no executable statement before the first statement.

When connection\_name is specified, it must be a debuggee connection owned by the current debugger session. See [DEBUG CONNECTION](master_debug_connection.htm) for more information.

statement\_name must specify a valid query handle on the debuggee connection. See [::DEBUG\_STATEMENTS](master__debug_statements.htm) and ::stmt.name for additional information.

The ID clause identifies a break point in the [::DEBUG\_BREAKS](master__debug_breaks.htm) table. It can be used with the [DEBUG REMOVE BREAK POINT](master_debug_remove_break_point.htm) to remove the break point.

The TRANSIENT clause specifies that break point only exists until the next stoppage in execution of the debuggee. Its main purpose is to support the Run-To or Trace-Into type of functionality.

The REMOVE clause removes all break points at the specified location.

Example 1

// Given the following script (without any comment) as the script to

// be debugged

DECLARE i Integer;

i = 0;

WHILE i < 3 DO

i = I + 1;

END;

 

// Either of the following statements will suspend the execution

// before the executing the line "i = 0":

DEBUG BREAK POINT "CONN0001xxxx" STATEMENT "STMT0001yyyy" AT 0;

DEBUG BREAK POINT "CONN0001xxxx" STATEMENT "STMT0001yyyy" AT 23 ID "B1";

 

// Setting the following break point then execute the script

// on the debuggee to simulate tracing into the script

DEBUG BREAK POINT "CONN0001xxxx" STATEMENT "STMT0001yyyy" AT 0 TRANSIENT;

DEBUG WAIT; // wait for the any debuggee suspension

 

Example 2

// Suppose a UDF is created with the following script

CREATE FUNCTION testfuncts.getMaxID() RETURNS integer

BEGIN

 DECLARE i integer;

 /\*

  \* CheckOutComments

  \*/

 i = ( SELECT max( id ) FROM myIDs );

 IF i IS NULL THEN

   i = 1;

 ENDIF;

 Return i;

END; --End function definition

 

// This statement will suspend the execution on any debuggee

// connection as soon as the UDF is entered

DEBUG BREAK POINT AT 0 IN FUNCTION testfuncts.getMaxID;

 

// This statement will suspend the execution before evaluating the

// "IF " statement in the function for any SQL script

// executed on connection "CONN0001xxxx"

DEBUG BREAK POINT "CONN0001xxxx" AT 108 IN FUNCTION testfuncts.getMaxID;

 

// This statement removes the last break point

DEBUG BREAK POINT "CONN0001xxxx" AT 108 IN FUNCTION testfuncts.getMaxID REMOVE;

See Also

[DEBUG BEGIN](master_debug_begin.htm)

[DEBUG RUN](master_debug_run.htm)

[DEBUG WAIT](master_debug_wait.htm)

[DEBUG REMOVE BREAK POINT](master_debug_remove_break_point.htm)

[::DEBUG\_CONNECTIONS](master__debug_connections.htm)

[::DEBUG\_STACK](master__debug_stack.htm)

[::DEBUG\_BREAKS](master__debug_breaks.htm)

[::DEBUG\_VARIABLES](master__debug_variables.htm)

[::DEBUG\_SOURCES](master__debug_sources.htm)