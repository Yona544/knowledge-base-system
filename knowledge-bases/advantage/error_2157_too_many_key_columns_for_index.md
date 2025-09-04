2157 Too many key columns for index




Advantage Database Server 12  

2157 Too many key columns for index

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2157 Too many key columns for index  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2157 Too many key columns for index Advantage Error Guide error\_2157\_too\_many\_key\_columns\_for\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2157 Too many key columns for index  Advantage Error Guide |  |  |  |  |

Problem: A CREATE INDEX statement contained too many columns.

Solution: The maximum number of columns allowed in an SQL CREATE INDEX statement is 15. Content indexes (for full text searches) can only have one column.