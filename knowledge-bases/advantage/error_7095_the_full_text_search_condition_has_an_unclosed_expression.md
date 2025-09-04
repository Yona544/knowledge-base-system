7095 The full text search condition has an unclosed expression




Advantage Database Server 12  

7095 The full text search condition has an unclosed expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7095 The full text search condition has an unclosed expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7095 The full text search condition has an unclosed expression Advantage Error Guide error\_7095\_the\_full\_text\_search\_condition\_has\_an\_unclosed\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7095 The full text search condition has an unclosed expression  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has an unclosed expression.

Solution: Verify that the parentheses are balanced in the search condition. For example, the search condition "medical and (doctor or nurse" is not valid because there is no closing parenthesis.