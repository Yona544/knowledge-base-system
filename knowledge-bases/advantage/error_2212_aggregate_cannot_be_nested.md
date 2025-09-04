2212 Aggregate cannot be nested




Advantage Database Server 12  

2212 Aggregate cannot be nested

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2212 Aggregate cannot be nested  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2212 Aggregate cannot be nested Advantage Error Guide error\_2212\_aggregate\_cannot\_be\_nested Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2212 Aggregate cannot be nested  Advantage Error Guide |  |  |  |  |

Problem: The expression for an aggregate function (MIN, MAX, SUM, AVG or COUNT) contains another aggregate function. For example: SUM( MIN( id )).

Solution: The nested aggregate is not a valid SQL expression.