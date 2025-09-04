---
title: Error 2148 Unable To Group By This Column
slug: error_2148_unable_to_group_by_this_column
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2148_unable_to_group_by_this_column.htm
source: Advantage CHM
tags:
  - error
checksum: 1a61f30fa602062cda3137e5f2d5ed3c8e37b63e
---

# Error 2148 Unable To Group By This Column

2148 Unable to GROUP BY this column

2148 Unable to GROUP BY this column

Advantage Error Guide

| 2148 Unable to GROUP BY this column  Advantage Error Guide |  |  |  |  |

Problem: The GROUP BY clause contained a column that cannot be ordered (e.g., memo, binary, or character field longer than 1024 characters).

Solution: Use only fixed-length fields that are 1024 characters or less in the GROUP BY clause.
