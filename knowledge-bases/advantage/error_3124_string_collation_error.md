3124 String collation error




Advantage Database Server 12  

3124 String collation error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3124 String collation error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3124 String collation error Advantage Error Guide error\_3124\_string\_collation\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3124 String collation error  Advantage Error Guide |  |  |  |  |

Problem 1: Comparison operator encountered operands of two different collations.

Solution 1: Coerce one of the operands using the collate function.

Problem 2: Result of an expression was a string with an undetermined collation.

Solution2: Coerce the result to a specific collation using the collate function.