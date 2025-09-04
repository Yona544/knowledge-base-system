SQL Script Overview




Advantage Database Server 12  

SQL Script Overview

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Script Overview  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - SQL Script Overview Advantage SQL Engine master\_Sql\_script\_overview Advantage SQL > SQL PSM (SCRIPT) > SQL Script Overview / Dear Support Staff, |  |
| SQL Script Overview  Advantage SQL Engine |  |  |  |  |

The Advantage SQL engine supports a subset of the ANSI SQL 2003 PSM (Persistent Stored Module) scripting language standard including variables, cursors, branches, loops, and exception handling. SQL scripts provide a convenient method for moving complex processing to the server and are the ideal platform for implementing most stored procedures and triggers.

SQL script-based stored procedures and triggers can be created in using either SQL statements, [CREATE PROCEDURE](master_create_procedure.htm) and [CREATE TRIGGER](master_create_trigger.htm); or the Advantage Client Engine API AdsDDAddProcedure and AdsDDCreateTrigger.

Implementing the stored procedures or triggers using an SQL script provides the following advantages over using external libraries:

•   The stored procedures or triggers can be implemented without the need for a third-party compiler.

•   The same stored procedure or trigger can be run on any Advantage Database Server regardless of the operating system.

•   No additional files must be deployed because the stored procedures and triggers are contained completely inside the Advantage Data Dictionary.

•   The Advantage Database Server has greater control over the execution of SQL script-based stored procedures and triggers. This reduces the chance that a faulty stored procedure or trigger can crash the database server. In addition, it allows stored procedures to be more easily canceled.

Writing a stored procedure using an SQL script may not be suitable for all situations:

•   The functionality supported by the Advantage SQL Script language may not be sufficient for a particular requirement. For example, an SQL script cannot make system calls. For further limitations, see [Using SQL Scripts to Write Stored Procedures](master_using_sql_script_to_write_stored_procedures.htm).

•   Debugging complex SQL scripts may be difficult. However, this may improve as the support for SQL scripting in Advantage continues to evolve.

Security Issues

If your application builds SQL statements based on user-provided values, those values must be checked for validity.

Consider a web page that asks for a username and password, and intends on building the following SQL statement:

SELECT \* FROM orders WHERE customer\_name = the\_customer

If instead of typing in a valid name, the user entered:

the\_customer; DROP TABLE orders; //

the following valid SQL statements would be generated:

SELECT \* FROM orders WHERE customer\_name=the\_customer;

DROP TABLE orders; //

There are techniques you can use to protect your application from this sort of attack. A web search on "sql security semicolon" will return a number of pages worth reading.

Each statement in an SQL script must be terminated with a semi-colon. The following sections describe the script statements that are supported as well as other general SQL script related information:

The BNF of an SQL script is defined as:

script ::= declare\_statements | declare\_statements;statement\_block | statement\_block

statement\_block ::= script\_statement | script\_statement;statement\_block

script\_statement ::= assignment\_statement | if\_statement | while\_statement |

cursor\_statement | execute\_statement | try\_statement |

raise\_statement | return\_statement | cache\_statement |

sql\_statement

See

[DECLARE](master_declare.htm)

[Assignment Statements](master_assignment.htm)

[IF](master_if_script.htm)

[WHILE](master_while.htm)

[OPEN, CLOSE, FETCH](master_open_close_fetch.htm)

[EXECUTE IMMEDIATE](master_execute_immediate.htm)

[TRY. . . CATCH. . . FINALLY](master_try_catch_finally.htm)

[RAISE](master_raise.htm)

[RETURN](master_return.htm)

[CACHE](master_cache.htm)

[Any SQL Statement](master_supported_sql_statements.htm)

[System Variables](master_system_variables.htm)

[Parameters](master_parameters.htm)

[Using SQL Scripts to Write Stored Procedures](master_using_sql_script_to_write_stored_procedures.htm)

The following statements are defined in the ANSI PSM standard but are not supported in this release of the Advantage SQL Engine. However, their functionality may be implemented using other supported statements:

FOR, REPEAT and LOOP: All loop functionality can be implemented using the [WHILE](master_while.htm) statement.

SIGNAL and RESIGNAL: Exception handling can be implemented using the [TRY. . . CATCH. . . FINALLY](master_try_catch_finally.htm) statement.

TIP: When a script is executed as a query and the last statement in the script is a SELECT statement, a cursor is returned to the client.