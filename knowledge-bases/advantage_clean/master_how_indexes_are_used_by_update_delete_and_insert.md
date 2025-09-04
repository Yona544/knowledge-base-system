---
title: Master How Indexes Are Used By Update Delete And Insert
slug: master_how_indexes_are_used_by_update_delete_and_insert
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_how_indexes_are_used_by_update_delete_and_insert.htm
source: Advantage CHM
tags:
  - master
checksum: 2a3d7b7222585a15a01180e62a74452bf226d71e
---

# Master How Indexes Are Used By Update Delete And Insert

How Indexes are used by UPDATE, DELETE, and INSERT

How Indexes are Used by UPDATE, DELETE, and INSERT

Advantage SQL Engine

| How Indexes are Used by UPDATE, DELETE, and INSERT  Advantage SQL Engine |  |  |  |  |

DELETE and UPDATE statements also make use of indexes in much the same way when those statements have WHERE clauses. For example, the statement "update employee set salary = salary \* 1.05 where empid = 525" can be evaluated very efficiently if an index exists on the field "empid". If such an index does not exist, the server must read each record to determine which record matches the WHERE clause. If the index does exist, the associated AOF (and thus the SQL query) will be evaluated very quickly.

The efficiency of INSERT statements is not affected by the existence of indexes.
