2166 SELECT sub-query returns more than one column




Advantage Database Server 12  

2166 SELECT sub-query returns more than one column

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2166 SELECT sub-query returns more than one column  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2166 SELECT sub-query returns more than one column Advantage Error Guide error\_2166\_select\_sub\_query\_returns\_more\_than\_one\_column Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2166 SELECT sub-query returns more than one column  Advantage Error Guide |  |  |  |  |

Problem: A sub-query incorrectly specified more than one column in the SELECT list. For example, "SELECT field1, field2 FROM table1 WHERE field1 IN (SELECT \* FROM table2)" is not valid if table2 contains more than one field.

Solution: Change the sub-query so that it selects only a single column.