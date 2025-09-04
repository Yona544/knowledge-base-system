3215 Invalid field type found in conditional index expression




Advantage Database Server 12  

3215 Invalid field type found in conditional index expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3215 Invalid field type found in conditional index expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3215 Invalid field type found in conditional index expression Advantage Error Guide error\_3215\_invalid\_field\_type\_found\_in\_conditional\_index\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3215 Invalid field type found in conditional index expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The conditional index expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the conditional index expression. Memo fields are not supported by the Advantage Expression Engine parser.