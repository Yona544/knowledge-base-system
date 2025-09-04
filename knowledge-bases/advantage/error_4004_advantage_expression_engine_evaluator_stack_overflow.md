4004 Advantage Expression Engine evaluator stack overflow




Advantage Database Server 12  

4004 Advantage Expression Engine evaluator stack overflow

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 4004 Advantage Expression Engine evaluator stack overflow  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 4004 Advantage Expression Engine evaluator stack overflow Advantage Error Guide error\_4004\_advantage\_expression\_engine\_evaluator\_stack\_overflow Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 4004 Advantage Expression Engine evaluator stack overflow  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine evaluator. The result of the parsed index key expression is too long to fit on the internal evaluator stack.

Solution: 4004 errors are typically caused by modifying a table's structure without deleting and re-building the index. 4004 errors are also caused by variable length index keys being created, often as a result of using a TRIM function in the index expression without using a PAD function.

Problem: A string literal specified in the Advantage Optimized Filter expression is too long.

Solution: 4004 error can be caused by a string literal value that is longer than 4KB. Such expression cannot be evaluated by the Advantage expression engine.