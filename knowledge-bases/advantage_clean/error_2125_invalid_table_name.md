---
title: Error 2125 Invalid Table Name
slug: error_2125_invalid_table_name
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2125_invalid_table_name.htm
source: Advantage CHM
tags:
  - error
checksum: cbdeb532e2f6cc059c3c88ea61264b294ff4efff
---

# Error 2125 Invalid Table Name

2125 Invalid table name

2125 Invalid table name

Advantage Error Guide

| 2125 Invalid table name  Advantage Error Guide |  |  |  |  |

Problem 1: The SQL statement contains a table name that is too long.

Solution 1: Verify that the combined connect path and table name is 255 characters or less.

Problem 2: A drive letter is used in the table name and the Advantage Database Server is used to execute the SQL statement. For example, "SELECT \* INTO "c:\temp\tmpTable" FROM MyTable" or "CREATE TABLE "c:\temp\tmpTable" ( fld1 integer )". Because the drive letter mappings of the Advantage Database Server is likely to be different from the client computer's drive letter mappings, a drive letter is not allowed when executing SQL statements that require creating a table.

Solution 2: Use a UNC path or relative path. For example, "SELECT \* INTO "\\MyAdsServer\temp\tmpTable" FROM MyTable".
