3315 Invalid field type found in index while expression




Advantage Database Server 12  

3315 Invalid field type found in index while expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3315 Invalid field type found in index while expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3315 Invalid field type found in index while expression Advantage Error Guide error\_3315\_invalid\_field\_type\_found\_in\_index\_while\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3315 Invalid field type found in index while expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The index while expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the while expression. Memo fields are not supported by the Advantage Expression Engine parser.