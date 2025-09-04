---
title: Error 2145 Unable To Order By This Column
slug: error_2145_unable_to_order_by_this_column
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2145_unable_to_order_by_this_column.htm
source: Advantage CHM
tags:
  - error
checksum: a5858926e6ca295e2bce82ddd208cffb4e962550
---

# Error 2145 Unable To Order By This Column

2145 Unable to ORDER BY this column

2145 Unable to ORDER BY this column

Advantage Error Guide

| 2145 Unable to ORDER BY this column  Advantage Error Guide |  |  |  |  |

This error is returned when the SQL engine is not able to supported the ORDER BY clause of the SQL statement. The following are some possible causes and solutions.

Problem: If the ORDER BY is used in a SELECT statement that defines a cursor in an SQL script, or that is a value subquery, then there are additional restriction on the columns in the ORDER BY  clause. For example, the column cannot be from a system table.

Solution: Use table expression to create an intermediate result set and then SELECT ... ORDER BY... on the intermediate result.

Example:

// This script returns 2145 error

DECLARE Columns CURSOR AS

       SELECT \*

       FROM System.Columns

       WHERE field\_default\_value is not null

       ORDER BY [Parent];

OPEN Columns;

// Rewrite to this to avoid error

DECLARE Columns CURSOR AS

       SELECT \* FROM

          ( SELECT \*

            FROM System.Columns

            WHERE field\_default\_value is not null ) t

       ORDER BY [Parent];

OPEN Columns;

Problem: The ORDER BY clause contained a column that cannot be ordered (e.g., memo, binary, or character field longer than 1024 characters).

Solution: Use only fixed-length fields that are 1024 characters or less in the ORDER BY clause.
