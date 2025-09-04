WHILE




Advantage Database Server 12  

WHILE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| WHILE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - WHILE Advantage SQL Engine master\_While Advantage SQL > SQL PSM (SCRIPT) > WHILE / Dear Support Staff, |  |
| WHILE  Advantage SQL Engine |  |  |  |  |

The WHILE statement is a general loop control statement. It allows a block of statement to be executed repeatedly until a predefined condition is met.

Syntax

WHILE condition\_expr DO

 loop\_statement\_block

END WHILE | END | ENDWHILE;

 

condition\_expr ::= Boolean | FETCH cursor\_name

 

loop\_statement\_block ::= script\_statement | LEAVE; | CONTINUE;

[loop\_statement\_block]

 

Note that the condition\_expr may be a regular Boolean expression or it may be a [FETCH statement](master_open_close_fetch.htm). The FETCH statement, when used in this context, evaluates to TRUE if the cursor is located on a valid row after the fetch operation and evaluates to FALSE otherwise. This provides a convenient method for testing the "end of file" condition when scrolling through a cursor.

Description

The WHILE statement is similar to the looping functionality that is available in other programming language. If the result of evaluating the condition\_expr is TRUE, the statements in the loop\_statement\_block are executed. After executing all statements in the loop\_statement\_block, execution returns back to the beginning of the WHILE statement and the process repeats until the condition\_expr evaluates to FALSE.

LEAVE and CONTINUE

LEAVE and CONTINUE are script statements that can only be used inside the WHILE statement block. When the LEAVE statement is encountered, the execution of the loop\_statement\_block is terminated and the execution continues on the next statement after the WHILE statement. When the CONTINUE statement is encountered, the current iteration of the loop is terminated and the next iteration of the loop is started by evaluating the WHILE condition.

An error is returned if LEAVE or CONTINUE is not used inside of a WHILE loop statement block.

Inside nested loops, the LEAVE and CONTINUE statements only affect the innermost loop statement block.

Example 1

// Count the number or records in a table

 

DECLARE iCount Integer;

DECLARE cursor1 CURSOR AS SELECT \* FROM test;

 

OPEN cursor1;

iCount = 0;

 

WHILE FETCH cursor1 DO

 iCount = iCount + 1;

END WHILE;

 

Example 2

// A sample script demonstrates nested loops and

// the usage of LEAVE and CONTINUE

 

DECLARE i Integer;

DECLARE cursor1 CURSOR AS SELECT \* FROM test1;

 

OPEN cursor1;

 

// Calculate the multiplication up to 50 of a

// column in one table and store the result in another

// table. Do not include any results that are zero or

// greater than 50

 

WHILE FETCH cursor1 DO

 IF ( cursor1.val = 0 ) OR ( cursor1.val > 50 ) THEN

   CONTINUE; // Do not include zero in results

 

 i = 1;

 

 WHILE i <= 50 DO

   IF cursor1.val \* i > 50 THEN

     LEAVE;

 

   INSERT INTO results VALUES( cursor1.val, i, cursor1.val \* i );

   i = i + 1;

 ENDWHILE;

 

ENDWHILE;