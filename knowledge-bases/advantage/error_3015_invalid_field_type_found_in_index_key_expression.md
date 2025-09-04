3015 Invalid field type found in index key expression




Advantage Database Server 12  

3015 Invalid field type found in index key expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3015 Invalid field type found in index key expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3015 Invalid field type found in index key expression Advantage Error Guide error\_3015\_invalid\_field\_type\_found\_in\_index\_key\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3015 Invalid field type found in index key expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The index key expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the key expression. Memo fields are not supported by the Advantage Expression Engine parser.