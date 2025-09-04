3111 Unknown identifier found in the record filter expression




Advantage Database Server 12  

3111 Unknown identifier found in the record filter expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3111 Unknown identifier found in the record filter expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3111 Unknown identifier found in the record filter expression Advantage Error Guide error\_3111\_unknown\_identifier\_found\_in\_the\_record\_filter\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3111 Unknown identifier found in the record filter expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the record filter expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the record filter expression. Memory variables are not supported by the Advantage Expression Engine as the variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.