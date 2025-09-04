---
title: Devguide User Defined Functions
slug: devguide_user_defined_functions
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_user_defined_functions.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9a8f99a0fb9000007b521245b60c6e15dc6a4497
---

# Devguide User Defined Functions

User Defined Functions

 

     User Defined Functions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| User Defined Functions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A user defined function (UDF) is a routine that you write using the Advantage scripting language. Once written, the user defined function can be called from any client connected to the data dictionary in which the user defined function declaration appears.

Calls to user defined functions can appear anywhere one of Advantage's SQL scalar functions can be called. For example, you can call your user defined function from the field list of a SELECT statement or from the right-hand side of an assignment statement.

There are three major benefits to user defined functions. The first, and most obvious, is that it permits you to create new expressions that you can use from queries. If a SQL scalar function that you want is not available, and it is possible to write that function using the Advantage scripting language, create a user defined function.

The second benefit is that user defined functions can embody complex operations in a single function call. This improves both the maintainability and readability of your code.

Finally, user defined functions can eliminate large or complicated segments of code, replacing them with a single function call. For complex operations that you need to perform either from various parts of your client application, or from multiple client applications, user defined functions permit you to define the operation just once. Improvements or corrections to the operations performed by a user defined function are immediately available to all clients who call it.

This final benefit is similar to the benefit provided by stored procedures. However, user defined functions can be called from places where stored procedures cannot. For example, you can use a user defined function in the field list of a SELECT statement, something you cannot do with a stored procedure.
