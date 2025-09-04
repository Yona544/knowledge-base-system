2133 Column on list multiple times




Advantage Database Server 12  

2133 Column on list multiple times

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2133 Column on list multiple times  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2133 Column on list multiple times Advantage Error Guide error\_2133\_column\_on\_list\_multiple\_times Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2133 Column on list multiple times  Advantage Error Guide |  |  |  |  |

Problem: A column list in the SQL statement contained a column name multiple times. For example, "INSERT INTO mytable (field1, field1) VALUES (1, 2)" is not valid.

Solution: Verify that the column list names each field only once.