2202 Invalid use of constant value




Advantage Database Server 12  

2202 Invalid use of constant value

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2202 Invalid use of constant value  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2202 Invalid use of constant value Advantage Error Guide error\_2202\_invalid\_use\_of\_constant\_value Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2202 Invalid use of constant value  Advantage Error Guide |  |  |  |  |

Constant values, including numeric values and string literal, are not allowed in the ORDER BY or GROUP BY clause of SELECT statement, or in the CREATE INDEX statement. For example, SELECT lastname FROM Employees ORDER BY 'lastname' is not allowed because 'lastname' is a string literal. The correct statement may be SELECT lastname FROM Employees ORDER BY "lastname" or SELECT lastname FROM Employees ORDER BY lastname.