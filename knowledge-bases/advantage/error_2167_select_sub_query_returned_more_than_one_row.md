2167 SELECT sub-query returned more than one row




Advantage Database Server 12  

2167 SELECT sub-query returned more than one row

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2167 SELECT sub-query returned more than one row  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2167 SELECT sub-query returned more than one row Advantage Error Guide error\_2167\_select\_sub\_query\_returned\_more\_than\_one\_row Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2167 SELECT sub-query returned more than one row  Advantage Error Guide |  |  |  |  |

Problem: A sub-query returned more than one row in a context where a single row was expected. For example, "SELECT \* FROM table1 WHERE table1.field1 = (SELECT table2.field1 FROM table2)" is not valid if table2 contains more than one row.

Solution: Adjust the WHERE clause on the sub-query so that it returns only a single row.