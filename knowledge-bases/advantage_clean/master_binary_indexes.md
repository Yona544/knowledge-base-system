---
title: Master Binary Indexes
slug: master_binary_indexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_binary_indexes.htm
source: Advantage CHM
tags:
  - master
checksum: ccd680d2abe2eb42370db8a01a524f7adea887c6
---

# Master Binary Indexes

Binary Indexes

Binary Indexes

| Binary Indexes |  |  |  |  |

Binary indexes are a very specific type of index that can be used for logical indexes. A typical (non-binary) index contains sorted key data that points to records; a binary index contains a bitmap of ones and zeros that represent the logical data with a one-to-one correlation of bits in the index to physical record numbers. As a result, they are very compact and require relatively little disk I/O. For example, a binary index on a table with 1 million records is about 135K while a traditional logical index on the same table exceeds 3MB. These indexes cannot be used for record movement operations (skip, seek, etc.), but they are useful for certain types of optimizations.

A recommended use for these indexes is to create an index with the expression "DELETED()". When a binary index with this expression exists, Advantage can use it for optimizing the filtering of deleted records when traversing record data in natural record order and when creating [Advantage Optimized Filters (AOFs)](master_advantage_optimized_filters.md). This optimization helps with both DBFs (when filtering deleted records) and with ADTs. For example, if a table has a large number of deleted records at the physical top of the table, the server must skip over those when the table is opened and the first record is retrieved. If a binary index with the expression DELETED() exists, the speed of this operation can be much faster. Likewise, an index of this type can be used by the AOF engine to optimize some filters that would not otherwise be fully optimized.

There is some extra cost involved in maintaining a DELETED() binary index, but it is minimal and if the ratio of deleted to non-deleted records is very high, it will probably improve performance. If, for example, you have a table in which you regularly delete all records but do not pack or zap (empty) the table due to exclusive use considerations, it probably makes sense to create a binary DELETED() index.

With DBF tables, binary indexes can also be created on simple logical fields. If you are using a specific logical field in filters and SQL statements regularly, it might make sense to make the index a binary index. This is especially true if the balance of the True and False values is fairly even. If, though, the values are unbalanced, a traditional index still may be more efficient. For example, if a table has a field PROCESSED that has only a few records with True values, then a filter (AOF or SQL WHERE clause) of the form "PROCESSED = TRUE" would likely be more efficient with the traditional index. With a traditional index, the AOF engine would need to read only the keys for the True values. With a binary index, it always must read the entire index. The threshold depends on a number of factors, but if you are using Advantage Database Server (remote), a binary index is probably faster if more than 1% of the records pass the filter.

The following limitations apply to binary indexes:

- The result of the index expression must be logical.

- The result of the index expression cannot be NULL. This means that the only type of binary index usable with ADTs is one of the expression "DELETED()".

- The index cannot be conditional (it cannot have a FOR clause).

- The index cannot be descending or unique.

You can create a binary index on a table in Advantage Data Architect by right clicking on the table and accessing the table properties dialog. To create binary indexes programmatically, you can use the system procedure [sp\_CreateIndex](master_sp_createindex.md) in an SQL statement. Client-specific mechanisms are also available in certain clients.
