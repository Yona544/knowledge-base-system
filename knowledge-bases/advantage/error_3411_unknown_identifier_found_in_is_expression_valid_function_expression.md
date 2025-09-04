3411 Unknown identifier found in "is expression valid" function expression




Advantage Database Server 12  

3411 Unknown identifier found in "is expression valid" function expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3411 Unknown identifier found in "is expression valid" function expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3411 Unknown identifier found in "is expression valid" function expression Advantage Error Guide error\_3411\_unknown\_identifier\_found\_in\_is\_expression\_valid\_function\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3411 Unknown identifier found in "is expression valid" function expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the "is expression valid" function expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the "is expression valid" function expression. The Advantage Expression Engine does not support memory variables. The variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.