IF




Advantage Database Server 12  

IF

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IF  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - IF Advantage SQL Engine master\_If\_script Advantage SQL > SQL PSM (SCRIPT) > IF / Dear Support Staff, |  |
| IF  Advantage SQL Engine |  |  |  |  |

The IF statement can be used in a script to branch the execution based on a Boolean expression. The optional ELSE or ELSEIF clauses can be used to simulate the CASE WHEN control structure type.

Syntax

IF condition\_expr THEN

 statement\_block

[elseif\_clause\_list]

[ELSE statement\_block]

END IF | END | ENDIF;

 

statement\_block :: statement | statement;

condition\_expr ::= Boolean | FETCH cursor\_name

 

elseif\_clause\_list ::= ELSEIF condition\_expr THEN

 statement\_block

[elseif\_clause\_list]

 

Note that the condition\_expr may be a regular Boolean expression or it may be a [FETCH statement](master_open_close_fetch.htm) . The FETCH statement, when used in this context, evaluates to TRUE if the cursor is located on a valid row after the fetch operation; otherwise, it evaluates to FALSE. This provides a convenient method for testing the "end of file" condition when scrolling through a cursor.

Description

The IF statement is similar to the general branching statement in other programming languages. If the condition\_expr evaluates to TRUE, the statement\_block after the THEN keyword is executed. The statement block is terminated when an ELSE, ELSEIF, ELIF or END keyword is encountered. If the condition\_expr evaluates to FALSE, the execution jumps to the elseif\_clause\_list if present. If no elseif\_clause\_list is present but there is an ELSE section, the execution jumps to the ELSE section. If there is no elseif\_clause\_list and no ELSE section, the execution continues to the statement after the END [IF].

The execution of the elseif\_clause is the same as the execution of a regular IF statement.

Example 1

// A sample script demonstrates the IF statement

 

DECLARE dVal Double;

 

dVal = 3 \* Rand();

 

IF dVal < 1 THEN

 SELECT \* FROM employees;

ELSEIF dVal < 2 THEN

 dVal = dVal + 3;

 SELECT \* FROM employees WHERE empid > dVal;

ELSE

 UPDATE employees SET empid = empid + dVal;

 dVal = dVal \* dVal;

ENDIF;

 

Example 2

// A sample script demonstrates the IF statement using the FETCH result

 

DECLARE cursor1 CURSOR AS SELECT \* FROM employees;

 

OPEN cursor1;

 

IF FETCH Cursor1 THEN

 INSERT INTO ErrorLog ( msg ) VALUES ( 'employees is not empty' );

ENDIF;

 

CLOSE cursor1;