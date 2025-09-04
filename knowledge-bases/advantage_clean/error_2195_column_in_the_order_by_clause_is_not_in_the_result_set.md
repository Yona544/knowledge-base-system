---
title: Error 2195 Column In The Order By Clause Is Not In The Result Set
slug: error_2195_column_in_the_order_by_clause_is_not_in_the_result_set
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2195_column_in_the_order_by_clause_is_not_in_the_result_set.htm
source: Advantage CHM
tags:
  - error
checksum: cbb13694c51d11ec14f6453a5d8a9e886950e5a8
---

# Error 2195 Column In The Order By Clause Is Not In The Result Set

2195 Column in the ORDER BY clause is not in the result set

2195 Column in the ORDER BY clause is not in the result set

Advantage Error Guide

| 2195 Column in the ORDER BY clause is not in the result set  Advantage Error Guide |  |  |  |  |

Problem: In certain cases, the ORDER BY clause cannot contain columns that are not in the result set. Two such cases are: 1) a UNION statement and 2) an ORDER BY clause containing any column that is an expression. For example, "SELECT lastname FROM table1 UNION SELECT lastname FROM table2 ORDER BY 1, firstname" is not valid because the column firstname is not in the result set. "SELECT UCASE( lastname ) FROM table1 ORDER BY 1, firstname" is not valid because the ordinal number 1 in the ORDER BY clause specifies an expression column and firstname column is not in the result set.

Solution: Adjust the ORDER BY clause so it conforms to the restriction.
