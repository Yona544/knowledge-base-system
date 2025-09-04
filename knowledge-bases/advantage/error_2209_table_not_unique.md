2209 Table not unique




Advantage Database Server 12  

2209 Table not unique

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2209 Table not unique  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2209 Table not unique Advantage Error Guide error\_2209\_table\_not\_unique Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2209 Table not unique  Advantage Error Guide |  |  |  |  |

Problem: An implied reference to a table was not unique.

Solution: If multiple tables exist in the SQL statement, table aliases must be used to qualify the reference. For example, the following statement is not valid.

 SELECT \* FROM tbl1, tbl2 WHERE tbl1.id=tbl2.id AND CONTAINS( \*, 'some words' )

It contains the \* (all columns reference) in the CONTAINS scalar function, but it does not uniquely identify a table. It would need to be changed to something like the following:

 SELECT \* FROM tbl1, tbl2 WHERE tbl1.id=tbl2.id AND CONTAINS( tbl1.\*, 'some words' )

The use of [RECNO](master_recno.htm)() and [DELETED](master_deleted.htm)() scalar functions may also require the use of an alias when used in SQL statements.  For example, the use of RECNO() in join statement would require that the table name be included:

 SELECT \* FROM table1, table2 WHERE RECNO(table1) = RECNO(table2);