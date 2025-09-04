---
title: Master Cursor Types
slug: master_cursor_types
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_cursor_types.htm
source: Advantage CHM
tags:
  - master
checksum: 22e026f7911beb279f00f74562b26db1e2a7878e
---

# Master Cursor Types

Cursor Types

Cursor Types

Advantage SQL Engine

| Cursor Types  Advantage SQL Engine |  |  |  |  |

Cursors are produced by executing SQL SELECT statements. Technically, a cursor is considered to be the mechanism by which the results of a query are manipulated and traversed. More generally, however, a cursor is often equated with the rowset itself. Cursors produced by Advantage are either live or static.

An Advantage live cursor represents a dynamic, server-side, scrollable cursor. With live (dynamic) cursors, updates to the base table are reflected in the cursor. For example, consider "select \* from employee where lastname = Smith". If a record is appended to the employee table and the new records lastname field is set to Smith, that new record will be inserted into the cursor. Likewise, an update will remove a record from the cursor if the lastname field is changed.

Advantage static cursors cannot be updated, nor are updates to the base tables of a static cursor reflected in the cursor itself. An example of a query that results in a static cursor is "select \* from orders, customers where order.custid = customers.custid." Once the rowset produced by that query is fully populated, updates to the orders and customers tables will have no effect on the cursor.

It is important to note that there are two specific cases where table updates made by one user are not reflected in another user's dynamic cursor. Advantage Local Server does not automatically detect changes in tables that are made by other clients. This means that updates made by applications using Advantage Local Server are propagated only to cursors owned by that same application. Similarly, another situation where updates are not reflected in live cursors is with Advantage Database Server when it uses the compatibility locking mode in order to share DBF tables with third-party applications. If a third-party application updates a table, the Advantage Database Server does not automatically detect that update and, therefore, it will not update cursors based on that table.

See [Live versus Static Cursors](master_live_versus_static_cursors.md) for more information about how live and static cursors are constructed and how they each affect performance.
