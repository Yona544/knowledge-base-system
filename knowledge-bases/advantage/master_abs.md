ABS()




Advantage Database Server 12  

ABS()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ABS()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ABS() Advantage Concepts master\_Abs Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ABS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the absolute value of a numeric expression.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

ABS(<nExp>) à nPositive

Parameters

<nExp>  The numeric expression to be evaluated.

Returns

ABS() returns a number representing the absolute value of its argument. The return value is a positive number or zero.

Description

ABS() is a numeric function that determines the magnitude of a numeric value independent of its sign. It lets you, for example, obtain the difference between two numbers as a positive value without knowing in advance which of the two is larger.

As a formalism, ABS(x) is defined in terms of its argument, x, as follows: if x >= 0, ABS(x) returns x; otherwise, ABS(x) returns the negation of x.

Examples

The following examples show typical results from ABS():

ABS(100 - 50) // Result: 50

ABS(50 - 100) // Result: 50

ABS(-12) // Result: 12

ABS(0) // Result: 0

See Also

None.