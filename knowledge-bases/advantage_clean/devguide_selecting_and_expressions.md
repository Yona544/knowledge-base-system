---
title: Devguide Selecting And Expressions
slug: devguide_selecting_and_expressions
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_selecting_and_expressions.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: b1732998498437c03b37fdb869d72764cc69064b
---

# Devguide Selecting And Expressions

Selecting and Expressions

     Selecting and Expressions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Selecting and Expressions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

This section demonstrates how you populate one or more columns and zero or more rows of a result set using the SELECT statement.

Selecting Fields

In its simplest form, SELECT is used to unconditionally retrieve one or more fields from a table. For example, the following statement selects the First Name field from the EMPLOYEE table:

SELECT [First Name] FROM EMPLOYEE

If you have two or more fields to select from, you enter a comma-separated list of fields you want to select. For example, this query returns the First Name and Last Name fields:

SELECT [First Name], [Last Name] FROM EMPLOYEE

If you want to select all fields, you use the \* (asterisk) character, like this:

SELECT \* FROM EMPLOYEE

Selecting Using Expressions

You are not limited to simple field selections in the SELECT list. You can include expressions that make use of one or more of the following: field references, literals, SQL scalar functions, user defined functions, subqueries, and operators. For example, the following query returns the concatenation of the First Name and Last Name fields:

SELECT [First Name] + ' ' + [Last Name] FROM EMPLOYEE

If you execute this query, you will notice something interesting, as shown in Figure 12-1. There is a large space between the first-name and last-name values, even though the query concatenates these values with a single space. This is because the First Name and Last Name fields include trailing blank spaces. To produce a more normal-looking full name, you need to trim these trailing values using the RTRIM function, as shown in the following query:

SELECT RTRIM([First Name]) + ' ' + RTRIM([Last Name])  
  FROM EMPLOYEE

Figure 12-1: Concatenated fields included trailing spaces

Actually, your SELECT list doesn't need to include any field names at all. For example, the following query returns a random value for each record in the CUSTOMER table:

SELECT RAND() FROM CUSTOMER

Normally, the result set returned from a SELECT query will use the names of the selected columns, or a temporary name such as EXPR, EXPR\_1, EXPR\_2, and so forth, for the columns that are returned. Alternatively, you can provide specific names for the columns by following the expression with the AS keyword, followed by an alias. Just as you do with field names, if the alias name begins with a number or contains special characters, you must enclose it in either double quotation marks or square brace delimiters, as shown here:

SELECT RTRIM("First Name") + ' ' + RTRIM("Last Name")   
  AS "Full Name"  
  FROM EMPLOYEE

   
NOTE: The use of expressions, subqueries, user defined functions, or scalar functions in the SELECT list always produces a static cursor.  
 

Using CASE Statements

There is a special control structure, called CASE, that you can use to create conditional expressions in the SELECT clause. The CASE statement can evaluate two or more expressions, and always results in a single expression that will return a column in the result table.

There are two forms of the CASE statement. In the simplest form, CASE is followed by an expression that is evaluated by one or more WHEN clauses. Each WHEN clause compares a value to the CASE expression, and includes an expression following the THEN keyword that the CASE clause will evaluate to if the comparison returns a Boolean True.

If none of the WHEN clauses evaluate to True, you can include an optional ELSE clause, which returns the expression of the CASE clause. The CASE clause evaluates to the expression defined by the first WHEN clause that evaluates to True, or the value of the ELSE clause, if provided, when none of the WHEN clauses evaluate to True.

The following query demonstrates this form of the CASE statement. This example is executed against the FreeTableConnection created in Chapter 2.

SELECT "Customer ID", "First Name", "Last Name",  
    CASE Active  
      WHEN True THEN 'Account is active'  
      WHEN False THEN 'Account is closed'  
      ELSE 'Account status unknown' //if NULL  
    END  
  FROM CUST

This query produces the result set shown in Figure 12-2.

Figure 12-2: An example of the CASE statement

The second form of the CASE statement permits you to evaluate two or more different expressions. In this form, the CASE statement is not followed by an expression. Instead, it is followed by one or more WHEN clauses, each of which evaluates an expression and includes the expression that the CASE statement will return if that WHEN clause evaluates to True.

Like the first form of CASE, there is also an optional ELSE clause, which includes the expression that the CASE statement will evaluate to if none of the WHEN clauses evaluate to True. The CASE statement evaluates to the expression associated with the first WHEN clause to evaluate to True; otherwise, it evaluates to the ELSE clause expression, if provided. The following is an example of this form of the CASE statement. As you can see, each of the WHEN clauses evaluates a different expression:

SELECT "Invoice No", "Customer ID", "Invoice Date",  
  "Date Payment Received", "Invoice Due Date",  
    CASE   
      WHEN "Invoice Due Date" <= CURDATE()   
        AND "Date Payment Received" IS NULL   
        THEN 'Waiting for payment'  
      WHEN "Invoice Due Date" > CURDATE()   
        AND "Date Payment Received" IS NULL  
        THEN 'Invoice is overdue'  
      WHEN "Date Payment Received" > "Invoice Due Date"  
        AND "Date Payment Received" IS NOT NULL  
        THEN 'Invoice was paid late'  
      ELSE 'Invoice was paid on time'   
    END AS "Invoice Payment Status"   
  FROM INVOICE

Using ROWID

You can use the special ROWID identifier to retrieve the internal record identifier in a query. Unlike any other field in a table, the ROWID of a particular record never changes, making it the most reliable means by which you can access the same record repeatedly.

SELECT ROWID, "First Name", "Last Name" FROM CUSTOMER

Querying Free Tables and Other Dictionary Tables

In the FROM list of the preceding queries, the name of a table in the current data dictionary is listed. It is also possible to include both free tables as well as tables that are bound to another data dictionary in your SELECT statements.

If your free table is in the same directory as your data dictionary, simply include the table name as though it were bound to the data dictionary. So long as the CUST.ADT table that you created in Chapter 2 is still in the same directory as the DemoDictionary data dictionary, the following query should select all fields and all records from it:

SELECT \* FROM CUST

If the free table is not in the same directory as the data dictionary, you can include a path (either a relative or a fully qualified path) to the table. For fully qualified paths, you are strongly encouraged to use UNC (universal naming convention) names. For example, if the CUST.ADT table is on the DATASERV computer in the directory named AppData in the C$ share, your SELECT statement might look something like the following:

SELECT \* FROM "\\DATASERV\C$\AppData\cust.adt"

If the table you want to query is bound to another data dictionary, you have two alternative techniques that you can use to access that table. So long as the table is accessible in the other data dictionary to a user whose name and password you used to connect to your current data dictionary, you can qualify the table name with the name of the data dictionary, using dot notation. For example, if the CUST table is bound to the Share.ADD data dictionary, and Share.ADD is in the same directory as DemoDictionary, you can use the following statement:

SELECT \* FROM "Share.ADD".CUST

If the Share.ADD data dictionary is not in the same directory, you still use dot notation but you must specify the path, as you did with a free table not in the same directory. For example, if Share.ADD is on the DATASERV computer in the directory named AdsBook in the C$ share, the following SELECT statement would access the CUST table:

SELECT \* FROM "\\DATASERV\C$\AdsBook\Share.ADD".CUST

If the data dictionary to which the CUST.ADT table is bound does not include a user name and password that has rights to the CUST.ADT table, you must use the second alternative, which is to use a data dictionary link. For example, imagine that you have a data dictionary link named AccountLink in your current data dictionary, and this link specifies a user name and password in the data dictionary to which CUST.ADT is bound. You can access the CUST table from your current data dictionary using the link name in dot notation with the table name. This is shown in the following query:

SELECT \* FROM AccountLink.CUST

If the link name includes special characters, you must enclose it in double quotation marks or square braces. Data dictionary links are discussed in Chapter 4.
