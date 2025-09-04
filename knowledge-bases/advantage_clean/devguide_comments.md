---
title: Devguide Comments
slug: devguide_comments
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_comments.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c5687218f9059432bb236ad738b7caee5efea0df
---

# Devguide Comments

Comments

     Comments

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Comments  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You use comments in a SQL statement to document the statement's purpose as well as temporarily disable one or more parts of the statement. When Advantage is executing the query, it ignores all comments. Advantage supports three types of comments in SQL statements. Of these, two are single-line comments, and the third is a multiline comment.

A single-line comment instructs Advantage to ignore all text to the right of the comment indicator. There are two single-line comment indicators: // (two consecutive forward slashes), and -- (two consecutive dashes). The following is an example of a SQL statement containing a single-line comment:

SELECT \* FROM INVOICE //WHERE "Customer ID" IS NULL

In this example, the WHERE clause has been temporarily disabled. This type of comment can be useful while you are testing a SQL statement. Here is another example:

// Delete the customer records where the  
// customer has already been processed  
DELETE FROM CUSTOMER   
  WHERE [Customer ID] IN   
    (SELECT [Customer ID] FROM PROCESSED)

This time, the comment is designed to document what task the query is performing. Multiline comments are enclosed between two delimiters. The comment begins with the /\* (forward slash, asterisk) delimiter and concludes with the \*/ (asterisk, forward slash) delimiter. The following shows how this comment could have been used in the preceding query:

/\* Delete the customer records where the  
   customer has already been processed \*/  
DELETE FROM CUSTOMER  
  WHERE [Customer ID] IN  
    (SELECT [Customer ID] FROM PROCESSED)

Unlike single-line comments, which comment out everything to the right of the comment indicator, a multiline comment can begin and conclude within a single line. For example, the following query will select only one field:

SELECT [Customer ID]/\*, [State]\*/ FROM CUSTOMER

In this query, the field name State has been commented out. This use of the multiline comment is quite valuable while you are testing your queries.
