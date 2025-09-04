RETURN




Advantage Database Server 12  

RETURN

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| RETURN  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - RETURN Advantage SQL Engine master\_Return Advantage SQL > SQL PSM (SCRIPT) > RETURN / Dear Support Staff, |  |
| RETURN  Advantage SQL Engine |  |  |  |  |

Terminates the execution of the current script.

Syntax

RETURN [expr];

Description

The RETURN statement terminates the execution of the current script. The optional expr may be specified to return the result of a [user defined function](master_user_defined_function.htm). If the script is not part of the user defined function, it is an error to specify expr.

Example 1

// This sample script opens a cursor. If there is an error opening the

// cursor, exit without returning an error

 

DECLARE cursor1 AS SELECT \* FROM #Inpupt;

 

TRY

 OPEN cursor1;

CATCH ALL

 RETURN;

END TRY;

 

// Other processing using the cursor

Example 2

// Create a user defined function calculates the square

// of an integer number

CREATE FUNCTION square( i Integer )

RETURNS Integer

BEGIN

 RETURN i \* i;

END;