2137 Column found in multiple tables




Advantage Database Server 12  

2137 Column found in multiple tables

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2137 Column found in multiple tables  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2137 Column found in multiple tables Advantage Error Guide error\_2137\_column\_found\_in\_multiple\_tables Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2137 Column found in multiple tables  Advantage Error Guide |  |  |  |  |

Problem: A column name in an SQL statement was found in multiple tables and, thus, was not uniquely identifiable.

Solution: Use a table alias or table name with the column name to uniquely identify it. For example, "SELECT field FROM table1, table2" is not valid if "field" exists in both "table1" and "table2" because it is ambiguous. You must specifically identify which table to use. For example, "SELECT table1.field from table1, table2".