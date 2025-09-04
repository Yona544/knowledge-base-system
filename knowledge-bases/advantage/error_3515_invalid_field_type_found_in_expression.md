3515 Invalid field type found in expression




Advantage Database Server 12  

3515 Invalid field type found in expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3515 Invalid field type found in expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3515 Invalid field type found in expression Advantage Error Guide error\_3515\_invalid\_field\_type\_found\_in\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3515 Invalid field type found in expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the expression. Memo fields are not supported by the Advantage Expression Engine parser.