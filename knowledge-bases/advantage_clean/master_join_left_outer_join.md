---
title: Master Join Left Outer Join
slug: master_join_left_outer_join
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_join_left_outer_join.htm
source: Advantage CHM
tags:
  - master
checksum: 38ed8c2721de10824f841c78538dce8d7c8ab5b0
---

# Master Join Left Outer Join

JOIN/LEFT OUTER JOIN

JOIN/LEFT/RIGHT/FULL OUTER JOIN

Advantage SQL Engine

| JOIN/LEFT/RIGHT/FULL OUTER JOIN  Advantage SQL Engine |  |  |  |  |

This row represents the join of two or more row sets. The Advantage SQL engine always performs what is called "Nested-Loop Join". With a nested-loop join of two tables, an outer table is scanned row by row, and for each row in the outer table, the inner table is scanned for rows matching the join condition. The Advantage SQL engine optimizes scan of the inner table using an index directly by performing a seek operation (INDEX SCAN) or by using an [Advantage Optimized Filter (AOF)](master_advantage_optimized_filters.md) (TABLE SCAN). In the execution plan, this operation always has two children rows. The child node with the smaller NodeID value is the outer table for the JOIN and the child node with the larger NodeID value is the inner table. When the "inner table" is another JOIN, then the outer table of the second join is the inner table of the current JOIN.

System tables and subqueries cannot be used as the "inner table" of FULL or RIGHT JOINs. Instead, a view can be created on the system table or subquery and the view can be used in the FULL or RIGHT JOIN in place of the system table. See [Views](master_views.md) for more information on views.

See Also

[How Indexes are Used in Joins](master_how_indexes_are_used_in_joins.md)
