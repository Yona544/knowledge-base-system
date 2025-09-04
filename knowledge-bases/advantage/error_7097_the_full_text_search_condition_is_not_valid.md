7097 The full text search condition is not valid




Advantage Database Server 12  

7097 The full text search condition is not valid

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7097 The full text search condition is not valid  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7097 The full text search condition is not valid Advantage Error Guide error\_7097\_the\_full\_text\_search\_condition\_is\_not\_valid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7097 The full text search condition is not valid  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has extraneous information at the end of the condition, or it does not have balanced parentheses.

Solution: Verify that the parentheses and logical operators are balanced. For example, the search condition "medical and doctor)" is not valid because it does not have an opening parenthesis.