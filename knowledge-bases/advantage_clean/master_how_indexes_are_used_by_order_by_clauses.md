---
title: Master How Indexes Are Used By Order By Clauses
slug: master_how_indexes_are_used_by_order_by_clauses
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_how_indexes_are_used_by_order_by_clauses.htm
source: Advantage CHM
tags:
  - master
checksum: e0c78cb4c14ea73bc7050e531f2ecefe3adfa500
---

# Master How Indexes Are Used By Order By Clauses

How Indexes are Used by ORDER BY Clauses

How Indexes are Used by ORDER BY Clauses

Advantage SQL Engine

| How Indexes are Used by ORDER BY Clauses  Advantage SQL Engine |  |  |  |  |

Existing indexes may be used to sort live cursors when the index expression matches the expression in the ORDER BY clause. For example, "select \* from employee order by lastname" will result in a live cursor that will use an index built on lastname if one exists. If such an index does not exist, a temporary one will be created by the server and deleted when the cursor is closed. If a specific query is common, it probably makes sense to create a permanent index on the field or fields used in the ORDER BY clause.
