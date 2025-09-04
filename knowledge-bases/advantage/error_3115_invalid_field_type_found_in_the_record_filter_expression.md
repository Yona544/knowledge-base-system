3115 Invalid field type found in the record filter expression




Advantage Database Server 12  

3115 Invalid field type found in the record filter expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3115 Invalid field type found in the record filter expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3115 Invalid field type found in the record filter expression Advantage Error Guide error\_3115\_invalid\_field\_type\_found\_in\_the\_record\_filter\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3115 Invalid field type found in the record filter expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The record filter expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the record filter expression. Memo fields are not supported by the Advantage Expression Engine parser.