---
title: Error 2196 Column Not Found In Group By Clause
slug: error_2196_column_not_found_in_group_by_clause
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2196_column_not_found_in_group_by_clause.htm
source: Advantage CHM
tags:
  - error
checksum: 7b9b870ec0cb56d577d7d29173c8ea6a20fbef19
---

# Error 2196 Column Not Found In Group By Clause

2196 Column not found in GROUP BY clause

2196 Column not found in GROUP BY clause

Advantage Error Guide

| 2196 Column not found in GROUP BY clause  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine expected to find the specified column in the GROUP BY clause.

Solution: If you use an aggregate function and a non-aggregated column name in a SELECT statement, then you must use a GROUP BY clause. For example, an application will get this error if it executes this statement: "SELECT lastname, COUNT(lastname) FROM employee".

The statement must also include the clause "GROUP BY lastname". In addition, if a GROUP BY clause is used, then every column that is not in an aggregate function in the SELECT list must be included in the GROUP BY clause.
