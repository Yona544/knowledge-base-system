---
title: Error 2126 Order By Ordinal Greater Than Select List Count
slug: error_2126_order_by_ordinal_greater_than_select_list_count
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2126_order_by_ordinal_greater_than_select_list_count.htm
source: Advantage CHM
tags:
  - error
checksum: 7793acecf60f2988ddc4bfd97876e402f6595709
---

# Error 2126 Order By Ordinal Greater Than Select List Count

2126 ORDER BY ordinal greater than select list count

2126 ORDER BY ordinal greater than select list count

Advantage Error Guide

| 2126 ORDER BY ordinal greater than select list count  Advantage Error Guide |  |  |  |  |

Problem: An ordinal value used in the ORDER BY clause is greater than the available number of columns. For example, the statement "SELECT field FROM mytable ORDER by 2" is not valid because the ordinal "2" is greater than the number of columns selected (1).

Solution: Adjust the ordinal value.
