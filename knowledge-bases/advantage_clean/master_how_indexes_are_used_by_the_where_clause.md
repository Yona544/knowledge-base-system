---
title: Master How Indexes Are Used By The Where Clause
slug: master_how_indexes_are_used_by_the_where_clause
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_how_indexes_are_used_by_the_where_clause.htm
source: Advantage CHM
tags:
  - master
checksum: b0aa6e54c02f2f120c4f2198599c07212f6ae343
---

# Master How Indexes Are Used By The Where Clause

How Indexes are Used by the WHERE Clause

How Indexes are Used by the WHERE Clause

Advantage SQL Engine

| How Indexes are Used by the WHERE Clause  Advantage SQL Engine |  |  |  |  |

Indexes are also used to aid in filtering tables to assist in optimizing queries. The most obvious case of this is to optimize WHERE clauses. For example, the query "select \* from employee where lastname = 'Jones'" results in a live cursor. The SQL engine uses Advantage Optimized Filters (AOFs) to create the filter. The AOFs automatically use available indexes in the filter evaluation.

If no index exists on the field "lastname", then the AOF will behave as a traditional record filter, and the server must read each record once in order to determine if the record passes the filter (the AOF is dynamically updated so a subsequent traversal will be faster). If an index does exist for "lastname", then the AOF evaluation can quickly determine the rowset for the query by reading only the necessary index pages. Note that in both cases, though, only records in the rowset that are requested by the client application will be transferred from the server to the client.

If WHERE clauses contain multiple fields, the SQL engine generally optimizes most efficiently if single-field indexes are available for each field. It can fully utilize multiple-field indexes (e.g., lastname;firstname) for WHERE clauses when the comparisons are strict equality comparisons and are logically combined with the AND operator. For example, the query "select \* from employee where lastname = 'Jones' and firstname = 'Allen'" can be fully optimized using an index of the form lastname;firstname. However, for a query of the form "select \* from employee where lastname > 'J' and firstname > 'D'", the SQL engine will use only the first field of a multiple-field index to resolve the individual comparisons. The query "select \* from employee order by lastname, firstname" will also make full use of an existing multiple-field index built on "lastname;firstname".

If a WHERE clause uses scalar functions, the server will use indexes for optimization only if the SQL scalar functions can be mapped to Advantage expression engine functions (see [Indexes with Expressions](master_indexes_with_expressions.md)). This set of scalar functions is the same set that can be used in SELECT statements that result in live cursors. For example, the query "select \* from employee where ucase(lastname) = 'JONES'" will be optimized if an index with the key expression "upper(lastname)" exists. The SQL scalar UCASE maps directly to the Advantage expression engine function UPPER.

If a table has a relatively high number of deleted records (whether the table is a DBF and deleted records are being filtered or if it is an ADT), it might be useful to add a [binary index](master_binary_indexes.md) with the expression "DELETED()" to the table. This can help with both AOF optimization and traversing data in natural record order.
