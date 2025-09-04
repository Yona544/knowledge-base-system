---
title: Master How Indexes Are Used In Joins
slug: master_how_indexes_are_used_in_joins
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_how_indexes_are_used_in_joins.htm
source: Advantage CHM
tags:
  - master
checksum: 4874fd3b33a421306fde6761f5e4bc7759462bf7
---

# Master How Indexes Are Used In Joins

How Indexes are Used in Joins

How Indexes are Used in Joins

Advantage SQL Engine

| How Indexes are Used in Joins  Advantage SQL Engine |  |  |  |  |

With joins, indexes are used in much the same fashion for optimization. For example, the query "select \* from customer left outer join orders on customer.id = orders.custid where customer.id = 22" is optimized most efficiently if indexes exist on the "id" field in the customer table and the "custid" field in the orders table. This is because the "id" index can be used to efficiently find "customer.id = 22". The SQL engine then uses the "custid" index on the orders table to find the matching record(s) for the join.
