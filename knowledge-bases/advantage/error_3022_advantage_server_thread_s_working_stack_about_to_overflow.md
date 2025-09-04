3022 Advantage server thread's working stack about to overflow




Advantage Database Server 12  

3022 Advantage server thread's working stack about to overflow

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3022 Advantage server thread's working stack about to overflow  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3022 Advantage server thread's working stack about to overflow Advantage Error Guide error\_3022\_advantage\_server\_thread\_s\_working\_stack\_about\_to\_overflow Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3022 Advantage server thread's working stack about to overflow  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The Advantage server thread's working stack was about to overflow. The problem is most likely due to an expression with a very large nesting of parentheses (hundreds of levels deep). This can occur when evaluating an Advantage Optimized Filter expression with a large number of OR operators on fields that are not indexed. It can also occur when evaluating the IN clause of an SQL statement on a field that is not indexed. For example, a query of the form "select \* from T where F in (1, 2, 3, 4, .... 3000 )" could produce a very deep nesting if the field "F" is not indexed.

Solution: Either reduce the number of items in the filter or query, or create an index on the field so that it is fully optimized.