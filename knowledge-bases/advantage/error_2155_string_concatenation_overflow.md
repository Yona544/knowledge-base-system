2155 String concatenation overflow




Advantage Database Server 12  

2155 String concatenation overflow

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2155 String concatenation overflow  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2155 String concatenation overflow Advantage Error Guide error\_2155\_string\_concatenation\_overflow Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2155 String concatenation overflow  Advantage Error Guide |  |  |  |  |

Problem: The result of a string concatenation (with the + operator or the CONCAT scalar function) exceeded a computed expression length. In versions 7.0 and earlier, the result of these concatenations was limited to 1024 characters. This limitation has been removed. In 7.0 and later release, this error can occur if the SQL statement contains the expression ? + strExpr where ? is a parameter and its value is set to a string longer than 1024 characters.

Solution: Adjust the SQL statement to avoid exceeding the maximum literal length, or use a cast function to explicitly specify the precision of the character string parameter. For example: Cast( ? AS SQL\_VARCHAR( 2048)).