2149 Aggregate function not allowed in this context




Advantage Database Server 12  

2149 Aggregate function not allowed in this context

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2149 Aggregate function not allowed in this context  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2149 Aggregate function not allowed in this context Advantage Error Guide error\_2149\_aggregate\_function\_not\_allowed\_in\_this\_context Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2149 Aggregate function not allowed in this context  Advantage Error Guide |  |  |  |  |

Problem: An SQL statement used an aggregate function (SUM, AVG, MIN, MAX, COUNT) in an incorrect manner.

Solution: Do not use aggregate functions in column lists. For example, "INSERT INTO mytable (field) VALUES (MIN(field))" is not valid.