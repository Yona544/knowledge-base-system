---
title: Error 2121 Column Not Found
slug: error_2121_column_not_found
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2121_column_not_found.htm
source: Advantage CHM
tags:
  - error
checksum: cb82cd96dfa8186823afc76cb9189992646e2a50
---

# Error 2121 Column Not Found

2121 Column not found

2121 Column not found

Advantage Error Guide

| 2121 Column not found  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine could not find a specified column. For example, a SELECT statement referred to a column that does not exist.

Solution: Verify that the columns referenced in the SQL statement all exist in the table. Also verify that you are using the correct alias on column names. For example, if you use an alias on a table name, you must use that alias with the column name rather than the table name. Example: "SELECT a.field FROM mytable a". The alias "a" is used on "mytable". "SELECT mytable.field FROM mytable a" is not correct.
