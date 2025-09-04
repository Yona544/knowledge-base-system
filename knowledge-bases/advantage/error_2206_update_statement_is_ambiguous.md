2206 Update statement is ambiguous




Advantage Database Server 12  

2206 Update statement is ambiguous

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2206 Update statement is ambiguous  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2206 Update statement is ambiguous Advantage Error Guide error\_2206\_update\_statement\_is\_ambiguous Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2206 Update statement is ambiguous  Advantage Error Guide |  |  |  |  |

The table to be updated is listed more than once in the FROM clause of an UPDATE statement. A sample ambiguous update statement is:

UPDATE table1 SET col1 = 2 FROM table1 a INNER JOIN table1 b WHERE a.id = b.id2

It is not possible for the SQL engine to determine whether the instance "a" of table1 or the instance "b" of table1 should be updated.