3415 Invalid field type found in "is expression valid" function expression




Advantage Database Server 12  

3415 Invalid field type found in "is expression valid" function expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3415 Invalid field type found in "is expression valid" function expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3415 Invalid field type found in "is expression valid" function expression Advantage Error Guide error\_3415\_invalid\_field\_type\_found\_in\_is\_expression\_valid\_function\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3415 Invalid field type found in "is expression valid" function expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The "is expression valid" function expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the "is expression valid" function expression. Memo fields are not supported by the Advantage Expression Engine parser.