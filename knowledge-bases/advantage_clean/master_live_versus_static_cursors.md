---
title: Master Live Versus Static Cursors
slug: master_live_versus_static_cursors
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_live_versus_static_cursors.htm
source: Advantage CHM
tags:
  - master
checksum: e2b9d37c6be613b2bcde7d75188b9320a43d8173
---

# Master Live Versus Static Cursors

Live versus Static Cursors

Live versus Static Cursors

Advantage SQL Engine

| Live versus Static Cursors  Advantage SQL Engine |  |  |  |  |

A live cursor is constructed by essentially putting a filter on the base table so that only the requested rows are visible. Conversely, a static cursor is actually a new table dynamically built with the requested rows of the original table or tables. Because the live cursor does not move any records around, it is faster to retrieve as a rowset. However, a static cursor is not completely populated when it is created.

A form of "caching" is used to add a certain number of rows at a time to the static cursor, so that control is returned to client in a reasonable time. The static cursor is populated as the rowset is traversed. This results in a more immediate response to the query, and processing is not wasted if only the first portion of the rowset is traversed. Note that the following operations will cause the static cursor rowset to be fully populated: Last (or Go Bottom), RecCount, Create Index.

For either live or static cursors, a cursor handle is utilized in a manner analogous to a table handle. This cursor handle can be used to navigate the resulting cursor in a fully scrollable manner. For all intents and purposes, the cursor can be treated like a table. Static cursors cannot be modified, but modifications on live cursors are reflected in the source table.

A live cursor can be much faster than a static cursor. However, this performance difference has a trade-off against features that can only be used on a static cursor. A live cursor is used if the SELECT statement does not contain any of the following:

- DISTINCT in the SELECT clause

- Joins (inner, outer, self, or UNION)

- Any aggregate function

- GROUP BY or HAVING clauses

- Subqueries

- Certain scalar functions (see [Indexes with Expressions](master_indexes_with_expressions.md))

- If a memo field is used in a WHERE clause (e.g., WHERE memo is null)

- LIKE operator is used in a WHERE clause (e.g.,. WHERE lastname LIKE 'Smith%)

- Expressions or scalar functions in the select list (e.g., select UCASE(lastname) )

- TOP in the SELECT clause

- WHERE clause contains a large expression that is not supported by the expression engine

It is possible to force Advantage to produce a static cursor on a SELECT statement that would normally result in a live cursor. To do this, use the {static} escape sequence after the SELECT keyword. For example:

 

SELECT {static} \* FROM emp WHERE hire\_date < '1990-01-14'

 

Without the escape sequence, Advantage would create a live cursor for that query. With {static} specified, though, Advantage will create a static cursor. From a performance standpoint, it is probably better in most circumstances to allow Advantage to create live cursors when possible.

If, though, the WHERE clause is very restrictive (thus producing a small rowset) and the base table is very large, it may be faster to force a static cursor. This is because the live cursor would be implemented with a filter on the server. If the client application were to traverse the rowset multiple times, the server would have to filter the rowset each time. If the client forced the cursor to be static, however, the server may be able to quickly seek directly to the data for the rowset with minimal cost. And once the cursor is created, the server would not be required to do any filtering when the client traversed the rowset.

See Also

[Cursor Types](master_cursor_types.md)
