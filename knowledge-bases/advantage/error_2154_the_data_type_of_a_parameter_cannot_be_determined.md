2154 The data type of a parameter cannot be determined




Advantage Database Server 12  

2154 The data type of a parameter cannot be determined

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2154 The data type of a parameter cannot be determined  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2154 The data type of a parameter cannot be determined Advantage Error Guide error\_2154\_the\_data\_type\_of\_a\_parameter\_cannot\_be\_determined Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2154 The data type of a parameter cannot be determined  Advantage Error Guide |  |  |  |  |

Problem: A parameter by itself in the SELECT list or ORDER BY clause has an ambiguous data type. For example, given the statements "SELECT ? FROM mytable" or "SELECT \* FROM myTable ORDER BY ?", the data type of the parameter in either statement cannot be determined.

Solution: Remove the ambiguous parameter from the statement. The use of the parameter in the SELECT list or ORDER BY clause is generally not meaningful.