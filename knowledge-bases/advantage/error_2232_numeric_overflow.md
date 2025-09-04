2232 Numeric Overflow




Advantage Database Server 12  

2232 Numeric Overflow

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2232 Numeric Overflow  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2232 Numeric Overflow Advantage Error Guide error\_2232\_numeric\_overflow Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2232 Numeric Overflow  Advantage Error Guide |  |  |  |  |

Problem: The evaluation of an exact numeric expression exceeds the predetermined precision. This is a run time error. In addition, subtraction and multiplication operations, the scale of the exact numeric expression is determined following the SQL standards guideline and the precision is capped at the maximum supported value (30). If the result of evaluating exceed the supported precision, this error is returned.

Solution: Cast one of the operands to the approximate numeric (i.e., Double).

See Also

[Exact Numeric vs Approximate Numeric](master_exact_numeric_vs_approximate_numeric.htm)