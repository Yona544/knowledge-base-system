RAISE




Advantage Database Server 12  

RAISE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| RAISE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - RAISE Advantage SQL Engine master\_Raise Advantage SQL > SQL PSM (SCRIPT) > RAISE / Dear Support Staff, |  |
| RAISE  Advantage SQL Engine |  |  |  |  |

Raises or re-raises an exception.

Syntax

RAISE [ exception ];

 

exception ::= identifier ( integer\_expr, char\_expr )

 

The identifier must be an unquoted identifier and it must not conflict with any [reserved keyword](master_reserved_keywords.htm).

Description

The RAISE statement raises an exception and causes the script execution to jump to the inner most [catch\_clause or catchall\_clause](master_try_catch_finally.htm). If the exception is not handled by a CATCH clause, the script execution will terminate.

A RAISE statement without the optional exception specification re-raises an existing exception and it is only valid in the CATCH clause.

After the RAISE statement is executed, the identifier, integer\_expr and char\_expr values in the exception specification will be assigned to the \_\_errclass, \_\_errcode, and \_\_errtext [systems variables](master_system_variables.htm) respectively.

Example 1

// A sample script to verify the a table has the expected number of

// columns - 18. Raise an exception if the number of columns in the table

// is not the expected value.

 

DECLARE bExpected Logical;

DECLARE strTableName String;

DECLARE cursor1 CURSOR;

 

strTableName = 'DemoTable';

 

OPEN cursor1 AS SELECT IIF( count(\*) = 18, TRUE, FALSE ) goodcnt FROM system.columns  WHERE parent = strTableName;

TRY

 IF FETCH cursor1 THEN

   bExpected = cursor1.goodcnt;

 ELSE

   bExpected = FALSE;

 ENDIF;

FINALLY

 CLOSE cursor1;

ENDTRY;

 

IF bExpected = FALSE THEN

 RAISE Unexpected\_Table\_Structure( 18, strTableName );

ENDIF;

 

Example 2

// A sample script to create a new table. If there is an existing

// table with the same name, drop that table and re-create the

// table. If the error is unexpected, re-raise the exception

 

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