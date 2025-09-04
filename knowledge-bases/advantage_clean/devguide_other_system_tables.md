---
title: Devguide Other System Tables
slug: devguide_other_system_tables
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_other_system_tables.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ad93b9ddb011768f2bf3c5c01d9f68d804c1cbd0
---

# Devguide Other System Tables

Other System Tables

     Other System Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Other System Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are three final system tables that do not fall into any of the preceding categories. These tables, system.objects, system.systemprocedures, and system.iota, can be accessed by any user.

The system.objects table returns information about the structure of each system table, with the exception of system.objects and system.iota (which do not appear in the system.objects result set). Each record includes a system table name (minus the system schema qualification), the parent table (where appropriate), the fields on which the table is sorted, and the primary key of the table.

The system.systemprocedures table creates a full list of all the currently available system stored procedures. For each system stored procedure, this table includes its name, input parameters, output parameters, and a brief description of what the procedure does.

Finally, the system.iota table is a trivial table that contains one field, named iota, and one record with the NULL value in the iota field. (Iota, the ninth letter in the Greek alphabet, is also a term that means "infinitesimally small.")

This table permits you to execute queries that select from SQL scalar functions, user defined functions, and other expressions with a minimum of overhead. For example, consider the following query:

SELECT Math.RandomRange(1, 100) FROM system.iota

This query returns a number between 1 and 100 using the RandomRange user defined function described in Chapter 13. Here is another example:

//Return the user name, application, and today's day name  
SELECT USER(), APPLICATIONID(),DAYNAME(CURDATE())  
  FROM system.iota;

When we called system.iota trivial, we were specifically speaking about its contents, with one record and a single NULL field. The utility of system.iota, by comparison, is enormous. Without it, performing calculations involving SQL scalar functions and/or user defined functions within SQL scripts would be more complicated.
