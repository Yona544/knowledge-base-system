---
title: Devguide How Field Level Permissions Are Enforced
slug: devguide_how_field_level_permissions_are_enforced
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_how_field_level_permissions_are_enforced.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: b4c7b836c87ad31899d9ff10884073e4b45c1eb7
---

# Devguide How Field Level Permissions Are Enforced

How Field-Level Permissions Are Enforced

     How Field-Level Permissions Are Enforced

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| How Field-Level Permissions Are Enforced  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

We did not assign field-level permissions to any of the tables in this data dictionary. In fact, some developers avoid using field-level permissions altogether, and use alternative mechanisms to restrict access to certain fields. Consider the example given earlier in this chapter in which a user can view all but the Salary field of the EMPLOYEE table. Instead of using field-level permissions, the user could be denied read access to the EMPLOYEE table, but be granted read access to a view that includes all fields other than the Salary field from the EMPLOYEE table. In the end, the results are similar. That user cannot access the Salary field.

But what happens when you do employ field permissions to limit a user's access to a field? Specifically, what would happen if you try to show a user a record that contains a field whose field-level permissions prohibit the field from being read?

The answer depends on the permission level associated with the table to which the field belongs. You can view and change a table's permission level by right-clicking the table name in the TABLES node and selecting Properties. Click the Table Properties tab to display the Table Properties page of the Table Designer shown in Figure 4-12.

Figure 4-12: The Table Properties page of the Table Designer

There are three possible values for the Permission Level table property. These are Allow Hidden Field Filters, Prevent Hidden Field Filters, and SQL Access Only.

If you set a table's Permission Level property to Allow Hidden Field Filters, reading a field that does not have read permissions does not cause an error, it simply returns a null value. If you try to display that data to a user who does not have read permissions, the field appears empty. However, you can use the field in a SQL WHERE clause, a filter, or a scope, which means that a user could possibly infer the value of the field based on the results of one of these operations.

The Prevent Hidden Field Filters permission level also returns a null value if you attempt to read a field that does not have read permissions. However, attempting to use that field in a SQL WHERE clause, a scope, or a filter will generate an error. This is the default permission level.

The SQL Access Only permission level is very restrictive. Tables with this permission level can only be accessed using SQL. Furthermore, any field without read rights cannot appear in a WHERE, HAVING, or ORDER BY clause. Otherwise, the SQL statement will produce an error.
