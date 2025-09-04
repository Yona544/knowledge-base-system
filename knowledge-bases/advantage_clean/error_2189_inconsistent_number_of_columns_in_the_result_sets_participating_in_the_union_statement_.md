---
title: Error 2189 Inconsistent Number Of Columns In The Result Sets Participating In The Union Statement
slug: error_2189_inconsistent_number_of_columns_in_the_result_sets_participating_in_the_union_statement_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2189_inconsistent_number_of_columns_in_the_result_sets_participating_in_the_union_statement_.htm
source: Advantage CHM
tags:
  - error
checksum: eef71fef8f17073f757d033c89c20305d84574de
---

# Error 2189 Inconsistent Number Of Columns In The Result Sets Participating In The Union Statement

2189 Inconsistent number of columns in the result sets participating in the UNION statement

2189 Inconsistent number of columns in the result sets participating in the UNION statement

Advantage Error Guide

| 2189 Inconsistent number of columns in the result sets participating in the UNION statement  Advantage Error Guide |  |  |  |  |

Problem: The individual queries in the UNION statement do not return the same number of columns in the result set. The queries in the UNION statement must contain the same number of columns in the result set. For example, "SELECT Lastname FROM table1 UNION SELECT lastname, firstname FROM table2" is not valid because the second SELECT returns 2 columns in the result set while the first SELECT returns only 1 column in the result set.

Solution: Adjust the SELECT clauses in the UNION statement so they all return the same number of columns.
