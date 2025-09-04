---
title: Master Indexing The Appropriate Fields
slug: master_indexing_the_appropriate_fields
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_indexing_the_appropriate_fields.htm
source: Advantage CHM
tags:
  - master
checksum: 6fe0928f40b4803eba20b0c11cc70fa6a128c08c
---

# Master Indexing The Appropriate Fields

Indexing the Appropriate Fields

Indexing the Appropriate Fields

Advantage SQL Engine

| Indexing the Appropriate Fields  Advantage SQL Engine |  |  |  |  |

The easiest way to increase performance is to make sure that there are enough indexes available. The biggest benefit of this is for the WHERE clause that has constant restriction, such as "Lastname = 'Smith'". It also allows for faster determination of the rowset since the whole file will not have to be traversed. In some cases, the SQL engine will automatically generate indexes in order to optimize queries.

For example, if an appropriate index is not available to optimize a join, the SQL engine will build a temporary index on the fly. This improves the performance of the query greatly and can be a big benefit for ad hoc queries. This incurs the expense of building an index each time the query is executed, though, so it is generally best if permanent indexes already exist.

There is a balance, though, in the number of existing indexes to maintain. It would not be wise in most cases to have an index built on every single field in a table. Each time an indexed field is updated, the corresponding index file must be updated to reflect that change. Advantage is very efficient when updating indexes, but it is still an added cost.
