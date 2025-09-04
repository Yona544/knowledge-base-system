2222 Invalid cursor column reference




Advantage Database Server 12  

2222 Invalid cursor column reference

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2222 Invalid cursor column reference  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2222 Invalid cursor column reference Advantage Error Guide error\_2222\_invalid\_cursor\_column\_reference Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2222 Invalid cursor column reference  Advantage Error Guide |  |  |  |  |

Problem: A cursor column reference in an expression is not valid. The column name may not be valid or the data type of the column may not be valid for the expression.

Solution: Check the error message for the location of the error in the script. Check that the column is in the cursor. If the cursor is opened and closed with a different cursor definition, the column name must correspond to a column in the cursor that is currently open.