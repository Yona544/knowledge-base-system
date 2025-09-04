---
title: Devguide Using Subqueries
slug: devguide_using_subqueries
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_subqueries.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 73a1d08dbf8bafc3b07a3321726edc461f75ed36
---

# Devguide Using Subqueries

Using Subqueries

     Using Subqueries

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using Subqueries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A subquery is a SQL SELECT query within another query. As discussed in more detail in Chapter 12, SELECT queries produce a result set of zero or more records. The values returned by the subquery are used to define which records are affected by the operation defined in the query that contains the subquery. For example, a subquery may select all customers who have a perfect record of payment. Those records can then be used to select the employees responsible for the greatest number of sales to those customers.

A subquery can appear in the values section of INSERT queries, the HAVING clause of SELECT queries, and the WHERE clause of DELETE, SELECT, and UPDATE queries. For example, the following query includes a subquery in the WHERE clause of a SELECT query:

SELECT \* FROM EMPLOYEE  
  WHERE "Employee Number" IN  
    (SELECT Contact FROM DEPARTMENTS)

This SELECT query selects all fields for those records where the employee number appears in the Contact field of the DEPARTMENTS table. Assuming that the Contact integer field contains the employee number of the department head, this query will select all employees who are department heads.

Here is a SQL script that employs a subquery, which assumes that an INV\_BAK table (an archive table) exists:

INSERT INTO INV\_BAK   
  SELECT \* FROM INVOICE  
    WHERE "Date Payment Received" < CURDATE() - 365;  
DELETE FROM INVOICE  
  WHERE "Date Payment Received" < CURDATE() 365

The first SQL statement in this script is an INSERT query that inserts records into the INV\_BAK table from the INVOICE table where the payment was received more than one year ago. The second query then removes these records from the active INVOICE table.

In both of the subquery examples presented here, the subquery is one that can be optimized. Furthermore, because these subqueries do not include references to fields outside the table they are selecting from, Advantage is able to execute the subquery once, and reuse that result for all operations performed by the query containing it.

Since subqueries can contain any valid statements that can appear in a SELECT statement, it is possible to include links to fields outside of the table the subquery is selecting from. These subqueries are referred to as correlated subqueries, and unless you have small tables that you are querying, they should probably be avoided for performance reasons. Consider the following query:

SELECT \* FROM EMPLOYEE Emp WHERE "Employee Number" IN  
  (SELECT "Employee ID" FROM INVOICE Inv   
    WHERE Emp."Employee Number" = Inv."Employee ID"  
    AND "Date Payment Received" IS NULL)

This query selects all fields from each employee record where that employee made a sale and the customer's payment was never entered. In this case, the WHERE clause in the subquery includes a Boolean comparison with a value from the outer query. Unlike the previous queries, this one requires the subquery to be executed repeatedly, once for each employee in the EMPLOYEE table. If the EMPLOYEE table has few records, this query will execute quickly. However, if the EMPLOYEE table is very large, this query could take a substantial amount of time to execute.

This discussion is not meant to dissuade you from using subqueries. Quite the opposite; subqueries are exceptionally powerful. However, if performance is an important element of your database design, you should consider what you are asking Advantage to do in your subqueries, and balance the power of these queries with your performance requirements.
