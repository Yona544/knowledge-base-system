---
title: Devguide Conditional Selection
slug: devguide_conditional_selection
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_conditional_selection.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2bc1db4b373f911b8485e54e46dc0901addc9b1d
---

# Devguide Conditional Selection

Conditional Selection

     Conditional Selection

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Conditional Selection  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The preceding queries select all records, which is fine when your tables are small. However, in many instancesespecially when you have a lot of datayou want to restrict your selections to a specific group of records. You use the WHERE clause in a SELECT statement to perform record selection. (The HAVING keyword can also influence record selection, but only when you are working with groups of records. HAVING is discussed later in this chapter.)

You follow the WHERE keyword with a Boolean expression. In most cases, this expression will include one or more field references. For example, the following query selects all fields from the ITEMS table where the Discount field contains the value 15 or higher:

SELECT \* FROM ITEMS WHERE Discount >= 15

WHERE clauses often have many expressions combined using the AND and/or OR operators. For example, the following query selects these same records, but only where the Product Code field contains the value G54039:

SELECT \* FROM ITEMS  
  WHERE Discount >= 15 AND "Product Code" = 'G54039'

   
NOTE: The performance of queries that include WHERE clauses can be dramatically improved by the presence of one or more appropriate indexes. Also, if you use a MEMO or BLOB field in a WHERE clause, the query returns a static cursor.  
 

Advantage SQL also supports several keywords that can be used in the WHERE clause. These include BETWEEN, IN, and LIKE. Each of these keywords is described in the following sections.

Using BETWEEN

Use BETWEEN to test whether an expression is within a range of values. If the value is in the range, BETWEEN evaluates to a Boolean True, and False otherwise. For example, the following query selects all invoices between May 7th and June 17th, 2005:

SELECT \* FROM INVOICE   
  WHERE "Invoice Date" BETWEEN '2005-05-07' AND '2005-06-17'

You can precede the BETWEEN keyword with the NOT keyword to select records that are not in the range.

Using IN

You use IN to compare an expression to either a list of values or a subquery. (Subqueries are introduced in Chapter 11.) The expression evaluates to True if the expression on the left-hand side of the comparison is in the list or subquery on the right-hand side.

Assuming that employees in the Administration department and in the Sales and Marketing department can initiate invoices, and that these departments have the corresponding department codes 101 and 108, the following query returns the records for employees who can initiate invoices:

SELECT \* FROM EMPLOYEE  
  WHERE "Department Code" IN (101, 108)

Although this same result could also be achieved using a series of WHERE clauses with OR operators, using IN is much simpler.

The following query performs the same task as the preceding one, but uses a subquery instead of a list of values:

SELECT \* FROM EMPLOYEE  
  WHERE "Department Code" IN   
    (SELECT "Department Code" FROM DEPARTMENTS  
       WHERE "Department Name" = 'Administration' OR  
         "Department Name" = 'Sales and Marketing')

Precede the IN keyword with the NOT keyword to return records that are not in the set.

   
NOTE: The use of a subquery with the IN operator in a WHERE clause always returns a static cursor.  
 

Using LIKE

You use the LIKE operator to compare an expression to a pattern that includes one or more wildcard characters. The % (match any) wildcard character matches zero or more characters, and the \_ (match one) wildcard character matches any one character. For example, the following query will return all customer records where the last name begins with the letter S:

SELECT \* FROM CUSTOMER WHERE "Last Name" LIKE 'S%'

By comparison, the next query will return all customer records where the last name begins with S and is exactly five characters in length (there are four underscore characters following the S):

SELECT \* FROM CUSTOMER WHERE "Last Name" LIKE 'S\_\_\_\_'

   
NOTE: The use of trailing wildcard characters permits an appropriate index to be used for searching data, leading to faster queries. If you include a leading wildcard character (such as %s), indexes cannot be used, and Advantage must search the physical records of the table. Also, the use of LIKE in a WHERE clause always produces a static cursor.  
 

When you are using a LIKE operator, and the value that you are searching for actually includes a % or \_ character, you need to define and use an escape character. An escape character instructs Advantage to interpret the character that follows it literally, rather than treating it in some special way. You define an escape character by following the LIKE comparison value with the keyword ESCAPE followed by the escape character. For example, the following query selects records where the first character in the Notes field is an underscore (\_):

SELECT \* FROM CUSTOMER   
  WHERE [Notes] LIKE '&\_%' ESCAPE '&'

You can define only one escape character for each LIKE clause. Also, if you need to refer to the literal instance of your escape character within the LIKE comparison value, escape it. For example, the following query selects records where the Notes field begins with the value \_&:

SELECT \* FROM CUSTOMER   
  WHERE [Notes] LIKE '&\_&&%' ESCAPE '&'
