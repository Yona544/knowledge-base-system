3011 Unknown identifier found in index key expression




Advantage Database Server 12  

3011 Unknown identifier found in index key expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3011 Unknown identifier found in index key expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3011 Unknown identifier found in index key expression Advantage Error Guide error\_3011\_unknown\_identifier\_found\_in\_index\_key\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3011 Unknown identifier found in index key expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the index key expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the key expression. Memory variables are not supported by the Advantage Expression Engine as the variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.