---
title: Devguide The Structure Of Sql Stored Procedures
slug: devguide_the_structure_of_sql_stored_procedures
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_structure_of_sql_stored_procedures.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c9a2e0e88abcce945ee2d781720043c9f020cd61
---

# Devguide The Structure Of Sql Stored Procedures

The Structure of SQL Stored Procedures

     The Structure of SQL Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The Structure of SQL Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While all AEPs have a definite structure, a SQL stored procedure is nothing more than a SQL script. There is no Startup, Shutdown, or GetVersionInfo function. When the SQL stored procedure is invoked, the SQL script is loaded and executed. Following the execution of the stored procedure, the SQL script is unloaded.

When Advantage executes a SQL stored procedure, it does so within the context of the client connection that invoked the associated stored procedure object. As a result, SQL stored procedures have access to any temporary tables available to the connection from which the stored procedure was called. However, unlike the client connection, which may have limited rights to data dictionary objects, stored procedures (and AEPs as well) have all rights to all data dictionary objects.

In addition to the objects accessible to the client connection, SQL stored procedures have access to the same three temporary tables available to stored procedure functions in an AEP library. If parameters are passed to a SQL stored procedure, your SQL script must read these from the \_ \_input table. Similarly, if your SQL stored procedure returns data, it does so by inserting data into the \_ \_output table. Finally, if an error condition is detected in your SQL stored procedure, you report the error by writing to the \_ \_error table.

Unlike AEPs, which are libraries external to a data dictionary, SQL stored procedures are stored in your data dictionary. As a result, when using SQL stored procedures, there are no additional installation issues when deploying your data dictionaries.
