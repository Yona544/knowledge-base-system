7098 The full text search condition has invalid operands specified for the NEAR operator




Advantage Database Server 12  

7098 The full text search condition has invalid operands specified for the NEAR operator

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7098 The full text search condition has invalid operands specified for the NEAR operator  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7098 The full text search condition has invalid operands specified for the NEAR operator Advantage Error Guide error\_7098\_the\_full\_text\_search\_condition\_has\_invalid\_operands\_specified\_for\_the\_near\_operator Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7098 The full text search condition has invalid operands specified for the NEAR operator  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has invalid operands specified for the NEAR operator. The NEAR operator cannot have a NOT condition as an operand..

Solution: Verify the operands to the NEAR operator do not contain NOT conditions. For example, the following two search conditions are not valid:

"(medical and not doctor) near hospital"

"landscaping near () (not shrubbery)"

The following two are valid:

"medical near hospital and not (doctor near hospital)"

"not (landscaping near shrubbery)"