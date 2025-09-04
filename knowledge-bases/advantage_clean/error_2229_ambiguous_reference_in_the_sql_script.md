---
title: Error 2229 Ambiguous Reference In The Sql Script
slug: error_2229_ambiguous_reference_in_the_sql_script
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2229_ambiguous_reference_in_the_sql_script.htm
source: Advantage CHM
tags:
  - error
checksum: 121aa4372e2fbf3a5aa5bfff179cd78fdf61b2e8
---

# Error 2229 Ambiguous Reference In The Sql Script

2229 Ambiguous reference in the SQL script

2229 Ambiguous reference in the SQL script

Advantage Error Guide

| 2229 Ambiguous reference in the SQL script  Advantage Error Guide |  |  |  |  |

Problem: An identifier used in an SQL statement is ambiguous. It may reference either a table column or a script variable.

Solution: Check the error message for the location of the error in the script and determine the intended purpose for the identifier. Depending on the intended purpose of the identifier, the conflict may be resolved by either changing the name of the variable (see [DECLARE](master_declare.md) or making a explicit column reference using the TableAlias.ColumnName notation.
