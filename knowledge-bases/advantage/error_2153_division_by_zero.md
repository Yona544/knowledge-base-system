2153 Division by zero




Advantage Database Server 12  

2153 Division by zero

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2153 Division by zero  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2153 Division by zero Advantage Error Guide error\_2153\_division\_by\_zero Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2153 Division by zero  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine detected a division by zero error while executing the statement.

Solution: Modify the SQL statement so that it does not produce division by zero errors. If, for example, your statement is "SELECT 1.0 / value FROM mytable", you might want to add a WHERE clause of the form "WHERE value <> 0" to avoid division by zero.