2211 CONTAINS(\*) not allowed in GROUP BY statement




Advantage Database Server 12  

2211 CONTAINS(\*) not allowed in GROUP BY statement

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2211 CONTAINS(\*) not allowed in GROUP BY statement  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2211 CONTAINS(\*) not allowed in GROUP BY statement Advantage Error Guide error\_2211\_contains\_not\_allowed\_in\_group\_by\_statement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2211 CONTAINS(\*) not allowed in GROUP BY statement  Advantage Error Guide |  |  |  |  |

Problem: A SELECT statement with a GROUP BY clause contained the scalar function CONTAINS with the "all columns" wild card (\*) as the first parameter.

Solution: When appearing in a statement with a GROUP BY clause, the CONTAINS scalar function can only be of the form where the first parameter is an explicit field name. It cannot use the \* (all columns) operator.