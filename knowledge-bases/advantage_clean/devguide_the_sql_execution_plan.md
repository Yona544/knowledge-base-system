---
title: Devguide The Sql Execution Plan
slug: devguide_the_sql_execution_plan
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_sql_execution_plan.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 945df16120677f11032d3bdd94d2e0b7abb3ba28
---

# Devguide The Sql Execution Plan

The SQL Execution Plan

     The SQL Execution Plan

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The SQL Execution Plan  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage can provide you with information about what is needed in order to execute a given query. This information is called the execution plan, and you can use it to write better queries and identify tables for which you should create additional indexes.

There are two ways to view the execution plan. The easiest to interpret is to generate a graphical execution plan. With the SQL statement that you want the execution plan for in the SQL pane of the SQL Utility (or highlighted in the SQL utility), click the Show Plan button on the SQL Utility toolbar. An example graphical execution plan is shown in Figure 11-9.

A graphical node appears in the execution plan graph for each operation required to produce the query result. Each node is accompanied by a label identifying the node's role. For example, in Figure 11-9 the fourth node from the left the node is identified as a left outer join.

Figure 11-9: A graphical representation of an execution plan

Not only is the graphical representation relatively easy to read, it also provides you with insight and support into optimizing your query. For example, if your query needs an index that you have not created, a red dot will appear to the right of one or more of the nodes. If you then right-click that node and select Create Indexes, the Table Designer for the table requiring the index is displayed. After creating the necessary index, you can close the Table Designer and regenerate the execution plan to look for additional tips on optimizing your query.

Furthermore, for some nodes, you can pause your mouse over the node and additional information is displayed. This information is associated with the Operator, Arguments and Warnings fields of the execution plan result set. This result set is the basis for the graphical representation.

To see the execution plan result set tabular form, precede your SQL statement with the SHOW PLAN FOR command. When you request an execution plan this way, Advantage returns a static cursor to a result set that contains the plan. Figure 11-10 shows the result set returned by a SHOW PLAN FOR statement.

Figure 11-10: The result set for an execution plan

This result set contains two or more records. The first record is always the root row, and it represents the query being executed. The remaining rows represent elements of the execution plan. Table 11-8 describes the fields of this table.

While the first record represents the query, the remaining records contain detail information about the query's execution. (For a simple query, there may be only one remaining record, after the root.) For these remaining records, the critical field in this table is Operator, and it contains one of the following values: DELETE, DISTINCT, EVALUATE, GROUP BY, INDEX SCAN, INSERT INTO, JOIN/LEFT OUTER JOIN, SORT, TABLE SCAN, UNION ALL, or UPDATE. Depending on the operation (as described in Table 11-8), the Statement Text, Arguments, and Warning fields may contain additional information about the operation.
