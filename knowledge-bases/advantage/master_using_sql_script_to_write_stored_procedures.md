Using SQL Script to Write Stored Procedures




Advantage Database Server 12  

Using SQL Script to Write Stored Procedures

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using SQL Script to Write Stored Procedures  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Using SQL Script to Write Stored Procedures Advantage SQL Engine master\_Using\_sql\_script\_to\_write\_stored\_procedures Advantage SQL > SQL PSM (SCRIPT) > Using SQL Script to Write Stored Procedures / Dear Support Staff, |  |
| Using SQL Script to Write Stored Procedures  Advantage SQL Engine |  |  |  |  |

Accessing the input and the output parameters

Input parameters may now be referenced as \_paramX, \_paramY, etc. where paramX and paramY are the actual names of the input parameters.  For example, the len parameter is available through the automatically-declared variable \_len.  Output parameters of a stored procedure can only be returned through the \_\_output table. For example, the following stored procedure concatenates a string to itself until it reaches the required length.

CREATE PROCEDURE testproc( str char( 20 ), len integer, strResult memo OUTPUT )

BEGIN

 DECLARE strVal String;

 strVal = ( trim( \_str ) );

 WHILE length( strVal ) < \_len DO

   strVal = strVal + strVal;

 END WHILE;

 INSERT INTO \_\_output VALUES ( strVal );

END

Recursion

Recursion, executing a stored procedure within another stored procedure, is allowed by the Advantage SQL engine. However, the current implementation of recursive execution of stored procedures in the SQL engine is not optimized for memory usage. Care must be taken to ensure that the depth of the recursion is limited as much as possible. The maximum depth of recursion before the database server develops serious errors is dependant on the size and the complexity of the stored procedure being executed recursively. However, a recursion depth of 10 or more executions should generally be avoided. Using a loop instead of recursion will provide a more effective use of server resources.

Using Free Table

[Free tables](javascript:hhpopuplink.TextPopup(popid_1535016085X,FontFace,-1,-1,-1,-1)) can be used in SQL Script stored procedures. However, since there is no way to specify the table type for tables used in the stored procedure, only ADT free tables can be used in SQL Script stored procedures. To use DBF tables in a script-stored procedure, the tables must be [database tables](javascript:hhpopuplink.TextPopup(popid_484727561X,FontFace,-1,-1,-1,-1)).