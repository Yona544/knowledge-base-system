---
title: Devguide Field Aliases And Table Aliases
slug: devguide_field_aliases_and_table_aliases
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_field_aliases_and_table_aliases.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 3cb9b9d82e405f6649cf16a16938897f998c1971
---

# Devguide Field Aliases And Table Aliases

Field Aliases and Table Aliases

     Field Aliases and Table Aliases

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Field Aliases and Table Aliases  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

It is not uncommon to reference field names from two or more tables in a single SQL statement. For example, consider the following query:

SELECT "Customer ID", "Employee ID", "Last Name"  
  FROM INVOICE, EMPLOYEE  
  WHERE "Employee ID" = "Employee Number"

This is a valid query because the field names in the SELECT list and the WHERE clause are unique to the tables listed in the FROM list. Nonetheless, this query is a bit more difficult to read unless you know for certain that Employee ID is a field of the INVOICE table and Employee Number is a field of the EMPLOYEE table.

If the field names are not unique, the problem is more serious. Consider the following query:

SELECT "Invoice No", "First Name", "Last Name"   
  FROM INVOICE, CUSTOMER  
  WHERE "Customer ID" = "Customer ID"

This is an invalid query, since the references to "Customer ID" in the WHERE clause are ambiguous. In cases like these, you have two options. The first is to use dot notation to qualify the field name with the table name. For example, the preceding query can be rewritten to look like the following:

SELECT INVOICE.[Invoice No], CUSTOMER.[First Name],  
  CUSTOMER.[Last Name]   
  FROM INVOICE, CUSTOMER   
  WHERE INVOICE.[Customer ID] = CUSTOMER.[Customer ID]

The drawback to this approach is that table names are often not short. As a result, using this technique may result in a lot of extra typing.

Instead of using the entire table name, you can define aliases for the table name in the FROM clause of the query, and then qualify the field names using the aliases. This is demonstrated in the following query:

SELECT Inv.[Invoice No], Cust.[First Name], Cust.[Last Name]  
  FROM INVOICE Inv, CUSTOMER Cust  
  WHERE Inv.[Customer ID] = Cust.[Customer ID]

Here, each table is associated with an alias, and that alias is used in dot notation to qualify the field references. As a result, there is no ambiguity, making this a valid query.

Now consider the following query:

SELECT Inv."Customer ID", Inv."Employee ID", Emp."Last Name"  
  FROM INVOICE Inv, EMPLOYEE Emp  
  WHERE Inv."Employee ID" = Emp."Employee Number"

While the aliases in the preceding query were not required, they produced a more readable query, one that will be easier to read, and hence, maintain, in the long run.

Aliases can also be created for field names. In most cases, aliased fields are used in SELECT statements in order to control the name of the corresponding field as it appears in the result set.

You define a field alias by following the field name in a SELECT statement with the keyword AS, followed by the name you want the field to use in the result set. For example, the following statement produces a result set that includes two fields, one called Random, and the other called Customer ID:

SELECT RAND() as Random, [Customer ID] FROM CUSTOMER
