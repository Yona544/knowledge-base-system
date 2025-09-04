2231 Numeric Result Out Of Range




Advantage Database Server 12  

2231 Numeric Result Out Of Range

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2231 Numeric Result Out Of Range  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2231 Numeric Result Out Of Range Advantage Error Guide error\_2231\_numeric\_result\_out\_of\_range Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2231 Numeric Result Out Of Range  Advantage Error Guide |  |  |  |  |

Problem: The result of an exact numeric expression exceeds the range of resultant data type. An example is multiplication of two exact numeric values with large-scale (digits after the decimal point) values. This error may be returned during query preparation or query evaluation. Another example will be when the result of an expression with integer operands exceed the range of a signed 32 bit integer value.

Solution: Cast one of the operands to the approximate numeric (i.e., Double) or to an exact numeric with larger range.

See Also

[Exact Numeric vs Approximate Numeric](master_exact_numeric_vs_approximate_numeric.htm)