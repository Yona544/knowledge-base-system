---
title: Devguide Sql Scripts
slug: devguide_sql_scripts
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_sql_scripts.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9be9a8ebb4064ed96e2a2ad058e9f89c8c5052c6
---

# Devguide Sql Scripts

SQL Scripts

     SQL Scripts

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| SQL Scripts  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Since Advantage 7, you can use SQL scripts anywhere a simple SQL statement is expected, except within View definitions. A SQL script is two or more SQL statements separated by semicolons. SQL scripts permit you to package several SQL statements together when you send them to the server. They are particularly useful when you must communicate to the server over a slow connection, thereby reducing the number of round-trips required to complete a complicated task.

While SQL scripts permit you to send two or more queries to Advantage in a single statement, they introduce a potential security risk that you must be aware of. Specifically, if you construct a query at runtime by concatenating literal SQL statements with data input by a user, you must check the user's input to prevent the unwanted introduction of semicolons. If a user enters a semicolon, and you subsequently concatenate that entry with your SQL query, Advantage will interpret the semicolon as a SQL statement separator.

Initially, this might not sound like a security threat. After all, wouldn't the presence of the semicolon surely lead to a syntax error, causing Advantage to return an error code? The answer is, "It depends." A user familiar with the use of semicolons to separate SQL statements, and knowledge of SQL, could exploit this feature to undermine your database.

   
NOTE: This security risk is referred to as SQL injection.  
 

Here's an example. Imagine that your client application includes a query that is constructed at runtime based on the user's entry of a Customer ID. The following is an example of how a query might be created from a user's input. This example is written in Delphi:

//Construct the query  
AdsQuery1.SQL.Text := 'SELECT \* FROM CUSTOMER ' +  
  'WHERE [Customer ID] = ' + Edit1.Text;  
//Execute the query  
AdsQuery1.Open;

Here, the value entered into the input field named Edit1 is concatenated to the query being assigned to the SQL property of an AdsQuery. Now consider what would happen if the user enters the following data into the edit:

12037; DROP TABLE CUSTOMER; DROP TABLE ITEMS

The resulting query would actually be a SQL script, and would look like the following:

SELECT \* FROM CUSTOMER   
  WHERE [Customer ID] =12037;  
DROP TABLE CUSTOMER;  
DROP TABLE ITEMS

Obviously, if you were to execute this SQL script, it would seriously compromise your database.

The easiest way to prevent SQL injection is to use parameterized queries where you bind the user's input to query parameters. Because of the way parameterized queries are executed, Advantage will never confuse a semicolon in a parameter as a statement separator.

If it is not feasible to use parameterized queries when building SQL statements based on user input, you can do several things. First of all, you can limit the amount of text that the user can enter. If a Customer ID is never more than ten characters, don't accept more than ten characters. Similarly, if the input is necessarily an integer value, verify that the user entered an integer. Second, examine the contents of the user's input. If it contains a semicolon, or any other element that it should not, reject the entered data.

Another solution is to use user and group rights to explicitly prohibit a user from dropping, deleting, or creating objects. But in the end, the most important point is that semicolons can be abused. You need to keep this in mind when working with user input that will contribute to a SQL statement.

SQL Scripts and Result Sets

If the last statement in a SQL script is a SELECT statement, the result set returned by that statement is the result set returned by the SQL script. In earlier versions of Advantage, SQL scripts did not return result sets.
