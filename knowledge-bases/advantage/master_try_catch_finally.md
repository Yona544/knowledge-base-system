TRY... CATCH... FINALLY...




Advantage Database Server 12  

TRY ... CATCH ... FINALLY ...

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TRY ... CATCH ... FINALLY ...  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - TRY ... CATCH ... FINALLY ... Advantage SQL Engine master\_Try\_catch\_finally Advantage SQL > SQL PSM (SCRIPT) > TRY ... CATCH ... FINALLY ... / Dear Support Staff, |  |
| TRY ... CATCH ... FINALLY ...  Advantage SQL Engine |  |  |  |  |

The TRY construct is used for exception handling and resource cleanup.

Syntax

TRY

statement\_block

[catch\_clauses]

[catchall\_clause]

[finally\_clause]

END TRY | END | ENDTRY;

 

catch\_clauses ::= CATCH error\_class statement\_block

[catch\_clauses]

 

catchall\_clause ::= CATCH ALL statement\_block

 

finally\_clause ::= FINALLY statement\_block

 

Description

The TRY construct provides a general mechanism for handling exceptions that are raised either [intentionally](master_raise.htm) by the script, or unintentionally due to a runtime error.

The statements in the TRY statement\_block are executed. If there is no exception during the execution of all statements in the block, execution continues to the finally\_clause if one is present; otherwise, the execution continues with the statement after the END [TRY] clause.

If an exception is raised while executing the statements in the statement\_block, the script execution engine will set the \_\_errcode, \_\_errclass, and the \_\_errtext [system variables](master_system_variables.htm) and execution immediately jumps to the catch\_clauses if there is one. Each CATCH error\_class clause is examined sequentially for a match. If the error\_class of a CATCH clause matches the \_\_errclass variable of the exception, the statement\_block for the CATCH will be executed. Once the CATCH clause is executed or if there is no CATCH clause, executing jumps to the finally\_clause if there is one.

The catchall\_clause can be used to handle any exception regardless of the \_\_errclass. Since the CATCH clauses, if present, are always placed in front of the catchall\_clause, the catchall\_clause will only be executed if an exception has not been handled. In effect, the CATCH clauses may be implemented using just a catchall\_clause and the IF ELSEIF END IF in the statement block of the catchall\_clause.

The statement:

TRY

 

CATCH a

 stmtblock\_a

CATCH b

 stmtblock\_b

END TRY;

 

is equivalent to:

TRY

 

CATCH ALL

 IF \_\_errclass = 'a' THEN

   Stmtblock\_a

 ELSEIF \_\_errclass = 'b' THEN

   stmtblock\_b

 ELSE

   RAISE;

 END IF;

END TRY;

 

Runtime errors not raised by an explicit RAISE statement will have the exception class ADS\_SCRIPT\_EXCEPTION and have the error code and error message corresponding to the error.

The TRY statement may be used to catch exceptions raised during recursive execution of stored procedures or triggers.

The finally\_clause of a TRY statement will always be executed regardless of errors or other execution branch statements, such as LEAVE, LOOP and RETURN.

If none of the catch\_clauses, the catchall\_clause, or the finally\_clause is present, an exception will be raised with error code 2219.

Example 1

// A sample script to create a new table. If there is an existing

// table with the same name, drop that table and re-create the

// table

 

TRY

 CREATE TABLE #Test( id integer, name char( 20 ) );

CATCH ADS\_SCRIPT\_EXCEPTION

 // Only do something if the error code indicates

 // table already exists

 IF \_\_errcode = 2010 THEN

   DROP TABLE #Test;

   CREATE TABLE #Test( id integer, name char( 20 ) );

 ELSE

   RAISE; // re-raise the exception

 END IF;

END TRY;

 

Example 2

// Create a new temporary table for storing intermediate data.

// Use the finally block to ensure that the temporary table

// is deleted after usage

 

DECLARE totalCnt Integer; nameCnt Integer; avgCnt Double;

DECLARE cursor1 CURSOR;

 

// Use SELECT INTO to create the temporary table

SELECT lastname, count(\*) cnt INTO #temp

FROM employees

GROUP BY lastname;

 

// Use TRY FINALLY to ensure the #temp is deleted

TRY

 totalCnt = 0;

 nameCnt = 0;

 

 OPEN cursor1 AS SELECT \* FROM #Temp;

 

 // Use a TRY FINALLY to ensure the cursor is closed

 TRY

   WHILE FETCH cursor1 DO

     totalCnt = totalCnt + cursor1.cnt;

     nameCnt = nameCnt + 1;

   END WHILE;

 FINALLY

   // Ensure the cursor is closed

   CLOSE cursor1;

 END TRY;

 

 // Dont calculate the avg if the nameCnt is zero to

 // avoid division by zero error

 // Although return is used, the FINALLY block will still

 // be executed.

 IF nameCnt = 0 THEN

   RETURN;

 END IF;

 

 // Calculate the average count for each name

 avgCnt = totalCnt / nameCnt;

FINALLY

 DROP TABLE #Temp;

END;