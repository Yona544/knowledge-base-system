---
title: Error 2191 Union Statement Can Only Be Ordered By Ordinal Number
slug: error_2191_union_statement_can_only_be_ordered_by_ordinal_number
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2191_union_statement_can_only_be_ordered_by_ordinal_number.htm
source: Advantage CHM
tags:
  - error
checksum: 491d1d3a0a739e305971f70fb93fd8584bf8a7a7
---

# Error 2191 Union Statement Can Only Be Ordered By Ordinal Number

2191 Invalid Data Type

2191 Invalid Data Type

Advantage Error Guide

| 2191 Invalid Data Type  Advantage Error Guide |  |  |  |  |

Problem: The data type of an expression in the SQL statement is not valid in the specified context.

Solution: Use Cast() or Convert() function to force the expression into the required type.

Problem: Incompatible data types are given to the UNION statements, IFNULL, IIF, or CASE expressions. For example: "SELECT 1 FROM system.iota UNION SELECT 'abc' FROM system.iota" will resulted in 2191 error because the integer value in the first SELECT is not compatible with the string value in the second SELECT for the purpose of the UNION. Similarly, "SELECT IIF( bVal, 1, 'abc' ) FROM system.iota" will also return 2191 error.

Solution: Use Cast() or Convert() function to force the expressions into the compatible type.

Note: In version 8.0 and earlier releases, the error 2191 means "UNION statement can only be ordered by ordinal number". The problem and solution for this error are below.

Problem: The combined result set of the UNION statement can be ORDER BY ordinal numbers only. Individual queries in the UNION statement cannot be sorted with the ORDER BY clause. For example, "SELECT lastname, firstname FROM table1 UNION SELECT lastname, firstname FROM table2 ORDER BY lastname" is not valid because the ORDER BY is not specified with ordinal number.

Solution: Adjust the ORDER BY clause in the UNION statement to use ordinal number columns.
