---
title: Error 2190 Incompatible Column Data Types In The Result Sets Participating In The Union Statement
slug: error_2190_incompatible_column_data_types_in_the_result_sets_participating_in_the_union_statement_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2190_incompatible_column_data_types_in_the_result_sets_participating_in_the_union_statement_.htm
source: Advantage CHM
tags:
  - error
checksum: e3204b3f86c91a05242b4bd86f9a888e9a9ca4f7
---

# Error 2190 Incompatible Column Data Types In The Result Sets Participating In The Union Statement

2190 Incompatible column data types in the result sets participating in the UNION statement

2190 Incompatible column data types in the result sets participating in the UNION statement

Advantage Error Guide

| 2190 Incompatible column data types in the result sets participating in the UNION statement  Advantage Error Guide |  |  |  |  |

Problem: Each resulting column of the individual queries in the UNION statement must be the same data type for all queries. For example, "SELECT lastname FROM table1 UNION SELECT DOB FROM table2" is not valid because the second SELECT returns a column with data type of date while the first SELECT returns only a column of characters.

Solution: Adjust the SELECT clauses in the UNION statement so they all return the same data type at each column position.
