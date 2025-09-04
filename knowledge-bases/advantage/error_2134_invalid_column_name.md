2134 Invalid column name




Advantage Database Server 12  

2134 Invalid column name

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2134 Invalid column name  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2134 Invalid column name Advantage Error Guide error\_2134\_invalid\_column\_name Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2134 Invalid column name  Advantage Error Guide |  |  |  |  |

Problem: The column name in a CREATE TABLE statement is not valid.

Solution: Verify that the column name is not too long for the table type. DBF tables are limited to 10 characters. Visual FoxPro (VFP) tables that are in a data dictionary are limited to 128 characters. ADT tables in SQL usage are limited to 128 characters.