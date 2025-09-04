---
title: Master Views
slug: master_views
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_views.htm
source: Advantage CHM
tags:
  - master
checksum: eabf06a075acf4cd144c1cd093ae8db1ac77efaa
---

# Master Views

Views

Views

Advantage SQL Engine

| Views  Advantage SQL Engine |  |  |  |  |

A view is a "virtual table" in a database whose contents are defined by an SQL SELECT statement. To the database user, the view appears just like a real table, with a set of named columns and rows of data. In reality, a VIEW is simply an SQL statement that is dynamically executed by the Advantage SQL engine when a view is being utilized, and the result set of the query is treated as a table. All users in the database can have permissions to open a view or execute queries against views but only the data dictionary administrator can create or drop views.

Note Parameters are not allowed in the definition of a view.

Views can be created and dropped from an Advantage Data Dictionary in three ways (Note that each of the Advantage products and their corresponding Help files are installed separately):

- •   Direct Advantage Client Engine (ACE) API calls can be made to create/drop views. Reference AdsDDAddView and AdsDDRemoveView in the Advantage Client Engine Help (ACE.HLP) for more information.

- •   CREATE VIEW and DROP VIEW sql commands can be used.

- •   The Advantage Data Architect (ARC) utility can be used to create/drop views. Reference the Advantage Data Architect Help (ARC.HLP) for more information.

A view SELECT statement can be any valid Advantage SQL statement, including joins or unions. If the view SELECT statement would result in a live cursor when executed on its own, the view will be a live (updateable) view. If the view SELECT statement would result in a static cursor when executed on its own (for example, a join), the view will be a static (read only) view. (See [Live versus Static Cursors](master_live_versus_static_cursors.md) and [Cursor Types](master_cursor_types.md) for more information about cursors.)

Examples of live cursors based on VIEWs:

CREATE VIEW GoodCust AS SELECT \* FROM customers WHERE credit\_limit > 50000

SELECT \* FROM GoodCust ORDER BY customer\_name ; live result set

SELECT customer\_name FROM GoodCust WHERE sales\_rep = 169 ; live result set

Examples of static cursors based on VIEWs:

CREATE VIEW GoodCust AS SELECT \* FROM customers WHERE credit\_limit > 50000

SELECT customer\_name, rep\_name

FROM GoodCust, salesreps

WHERE GoodCust.sales\_rep = salesreps.rep\_id ; static cursor based on live view

CREATE VIEW CustAndReps AS SELECT customer\_name, rep\_name

FROM customers, salesreps

WHERE customers.sales\_rep = salesreps.rep\_id

SELECT \* FROM CustAndReps ; static cursor, because CustAndReps is a static view
