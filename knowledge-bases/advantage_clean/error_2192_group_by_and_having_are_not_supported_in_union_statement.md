---
title: Error 2192 Group By And Having Are Not Supported In Union Statement
slug: error_2192_group_by_and_having_are_not_supported_in_union_statement
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2192_group_by_and_having_are_not_supported_in_union_statement.htm
source: Advantage CHM
tags:
  - error
checksum: 42d227ec2826e1f75607a64109488ab14b4066df
---

# Error 2192 Group By And Having Are Not Supported In Union Statement

2192 GROUP BY and HAVING are not supported in UNION statement

2192 GROUP BY and HAVING are not supported in UNION statement

Advantage Error Guide

| 2192 GROUP BY and HAVING are not supported in UNION statement  Advantage Error Guide |  |  |  |  |

Problem: GROUP BY and HAVING clauses are not valid in a UNION statement. For example, "SELECT lastname, firstname FROM table1 GROUP BY lastname UNION SELECT lastname, firstname FROM table2 ORDER BY lastname" is not valid because of the GROUP BY clause in the statement. This limitation exists in the version 6.0 and earlier releases of the Advantage products.

Solution: Remove the GROUP BY or HAVING clause from the UNION statement or upgrade to the Advantage Database Server/Advantage Local Server 6.1 (or greater) release.
