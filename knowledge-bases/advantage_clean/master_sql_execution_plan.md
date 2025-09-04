---
title: Master Sql Execution Plan
slug: master_sql_execution_plan
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sql_execution_plan.htm
source: Advantage CHM
tags:
  - master
checksum: 95b5da123466e45af578dd43e37552afcdfbfffb
---

# Master Sql Execution Plan

SQL Execution Plan

SQL Execution Plan

Advantage SQL Engine

| SQL Execution Plan  Advantage SQL Engine |  |  |  |  |

The SQL execution plan contains detailed information on how a particular query or a set of queries will be executed by the Advantage Database Server. By reviewing the SQL execution plan for inefficient queries, the query author may be able to improve performance of applications and reports with modifications to the SQL statement or the database design

The SQL execution plan is available in a table format as a static cursor. The execution plan may also be viewed in a graphical representation in the Native SQL Window in the Advantage Data Architect utility. The following topics discuss the information available in the table format of the SQL execution plan. The usage of the graphical interface is discussed in separate topics in the help file for the Advantage Data Architect.

SHOW PLAN FOR

By adding the SHOW PLAN FOR clause to the beginning of an SQL statement, the Advantage Database Server returns a static cursor that contains the information on how the query will be executed. The statement following the SHOW PLAN FOR clause is not executed but it is verified for correctness. For example, executing the following statement will return a static cursor containing the execution plan for a two-table inner join.

SHOW PLAN FOR

SELECT \* FROM customers c, orders o WHERE c.customer\_id = o.customer\_id

 

The SHOW PLAN FOR clause can also be added to the beginning of a set of SQL statements (SQL Scripts) to retrieve the execution plans for all statements in the set. The following example returns the execution plans for the three SQL statements following the SHOW PLAN FOR clause.

 

SHOW PLAN FOR

SELECT \*

FROM customers c, orders o

WHERE c.customer\_id = o.customer\_id;

 

UPDATE customers SET zip\_code = 90210 WHERE customer\_id = 69;

 

INSERT INTO orders

SELECT \* FROM NewOrder

WHERE customer\_id IN

( SELECT customer\_id FROM customers )

AND order\_date > 2004-01-01;

 

The server will execute none of the three statements; instead, a static cursor containing three disjoined execution plans will be returned.

Note The SHOW PLAN FOR clause can only appear once in an SQL statement or an SQL script. Also, the SHOW PLAN FOR clause must be the first clause in an SQL statement, or the first clause of the first SQL statement in an SQL script. An error will be returned if the SHOW PLAN FOR clause is encountered in the middle of an SQL script.

Table Structure

The static cursor returned when requesting the SQL execution using the SHOW PLAN FOR clause has nine columns. The following table describes the structure of the static cursor:

| Column Ordinal | Column name | Column Type | Description |
| 1 | NodeID | Integer | A unique value identifying the row in the execution plan table. |
| 2 | ParentID | Integer | The NodeID of the row that is the parent of current row in this execution plan table. By linking each row to its parents, the SQL execution plan of an SQL statement can be drawn as a tree. The root node of the tree will have a value 0 in this column. When retrieving the execution plan for an SQL script, the execution plan for each statement in the script is a separate tree in the table. |
| 3 | RowType | Char(30) | The type of the row. The root row of the execution plan of an SQL statement will have the statement type in this column. For all other rows, the RowType column will have the value "PLAN". |
| 4 | StatementText | Memo | For the root node of an execution plan, (i.e., RowType != "PLAN"), this column contains the original text of the SQL statement.  For all other rows, (i.e., RowType = "PLAN"), this column contains the statement information related to the operation. |
| 5 | StatementID | Integer | A number identifying the SQL statement whose execution plan is returned. Each statement in a SQL script will have its own unique StatementID. The number returned in this column represents the total number of SQL statements that have been executed or have had an execution plan retrieved on this connection. |
| 6 | Operator | Char(30) | Operation to be performed by the Advantage SQL engine. The possible values for this column are described in the sections after this table. This row will be empty unless the RowType = "PLAN" . |
| 7 | Arguments | Memo | Provides supplemental information about the operation being performed. The contents of this column depend on the Operator. |
| 8 | EstimatedExecution | Integer | Estimated number of times this operator will be executed while running the current query. |
| 9 | Warnings | Memo | Contains a list of warning message relating to the current operation. For example, if a temporary index is created due to lack of index on the join condition, a NO INDEX( column1, column2, ) will be returned (where column1 and column2, etc are the missing index columns). |

Most of operators in the execution are set operators that take a row set from the children rows as input and returns another rows as output to the parent row. Using the possible values of the Operator column as the key, the following sections explain in more detail the execution plan information in each row. The Operator column can have the following values:

[DISTINCT](master_distinct.md)

[EVALUATE](master_evaluate.md)

[GROUP BY](master_group_by.md)

[INDEX SCAN](master_index_scan.md)

[JOIN/LEFT OUTER JOIN](master_join_left_outer_join.md)

[SORT](master_sort.md)

[TABLE SCAN, AOF SCAN](master_table_scan.md)

[UNION ALL](master_union_all.md)

[INSERT INTO](master_insert_into.md)

[UPDATE](master_update_sql_execution_plan.md)

[DELETE](master_delete_sql_execution_plan.md)
