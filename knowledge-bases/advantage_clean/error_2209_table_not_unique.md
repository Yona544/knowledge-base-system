---
title: Error 2209 Table Not Unique
slug: error_2209_table_not_unique
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2209_table_not_unique.htm
source: Advantage CHM
tags:
  - error
checksum: dca6d8648092ff007a0189beacd9b173d9951680
---

# Error 2209 Table Not Unique

2209 Table not unique

2209 Table not unique

Advantage Error Guide

| 2209 Table not unique  Advantage Error Guide |  |  |  |  |

Problem: An implied reference to a table was not unique.

Solution: If multiple tables exist in the SQL statement, table aliases must be used to qualify the reference. For example, the following statement is not valid.

 SELECT \* FROM tbl1, tbl2 WHERE tbl1.id=tbl2.id AND CONTAINS( \*, 'some words' )

It contains the \* (all columns reference) in the CONTAINS scalar function, but it does not uniquely identify a table. It would need to be changed to something like the following:

 SELECT \* FROM tbl1, tbl2 WHERE tbl1.id=tbl2.id AND CONTAINS( tbl1.\*, 'some words' )

The use of [RECNO](master_recno.md)() and [DELETED](master_deleted.md)() scalar functions may also require the use of an alias when used in SQL statements.  For example, the use of RECNO() in join statement would require that the table name be included:

 SELECT \* FROM table1, table2 WHERE RECNO(table1) = RECNO(table2);
