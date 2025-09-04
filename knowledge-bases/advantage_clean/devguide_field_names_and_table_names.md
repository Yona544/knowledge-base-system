---
title: Devguide Field Names And Table Names
slug: devguide_field_names_and_table_names
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_field_names_and_table_names.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 88b46edb3c556448197a2fbaaf713ec20a692426
---

# Devguide Field Names And Table Names

Field Names and Table Names

     Field Names and Table Names

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Field Names and Table Names  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Many SQL statements refer to at least one table, and most of these refer to one or more fields. For example, consider the following statement:

SELECT Picture FROM PRODUCTS

Picture, in this statement, refers to the Picture field, and PRODUCTS refers to the PRODUCTS table.

Whether a reference is interpreted by Advantage to be a field name or a table name depends on the location of the reference in the statement. In the preceding statement, Picture is interpreted to be the field name because field names, but not table names, can appear in this location of the SELECT statement. By the same token, PRODUCTS is interpreted to be the table name, because table names are expected in the FROM list of the SELECT statement.

When a field name or table name begins with a numeral, or contains characters other than 09 and AZ, the name must be enclosed between either double quotes or square braces [ ]. For example, if you want to include the Product Name field in the preceding query, you enclose it in delimiters as follows:

SELECT Picture, "Product Name" FROM PRODUCTS

Likewise, the following query is equivalent:

SELECT Picture, [Product Name] FROM PRODUCTS

Advantage does not care which delimiter pair you use. Which you choose to use will often depend on the development environment you are using. For example, in C# you must escape double-quotation characters in string literals, preceding the double-quotation character with a backslash. Square braces, however, do not need to be escaped. Consequently, for readability, we prefer:

oCommand.CommandText = "DELETE FROM CUSTOMER " +  
  "WHERE [Customer ID] IN (SELECT [Customer ID] FROM \_\_old)";

over:

oCommand.CommandText = "DELETE FROM CUSTOMER " +  
  "WHERE \"Customer ID\" IN (SELECT \"Customer ID\" FROM \_\_old)";

Even when a field name or table name does not need to be delimited, you might consider doing so anyway. By always delimiting field and table names, you ensure that Advantage will correctly interpret what you are asking it to do. For example, imagine that you have a table named ACCOUNTS, and it has a logical field named Open. Prior to Advantage 8, the following SQL statement would be acceptable:

SELECT \* FROM ACCOUNTS WHERE Open = True

OPEN is now a keyword in Advantage 8, and the preceding statement will generate an error if you attempt to execute it. However, if you had originally written the SQL statement like the following, it would have run then and will still run now:

SELECT \* FROM [ACCOUNTS] WHERE [Open] = True
