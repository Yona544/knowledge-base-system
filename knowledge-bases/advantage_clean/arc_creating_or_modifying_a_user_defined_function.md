---
title: Arc Creating Or Modifying A User Defined Function
slug: arc_creating_or_modifying_a_user_defined_function
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_a_user_defined_function.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 219a20cfc11d9157f0808f42395d88811d87c401
---

# Arc Creating Or Modifying A User Defined Function

Creating or Modifying a User Defined Function

Creating or Modifying a User Defined Function

Advantage Data Architect

| Creating or Modifying a User Defined Function  Advantage Data Architect |  |  |  |  |

A User Defined Function (UDF) allows a developer to create a reusable function that can be used in an SQL statement or script just like an existing scalar function. By encapsulating frequently performed or complex operations into UDFs, SQL statements and scripts become easier to write, understand, and debug. In a sense, UDFs makes it possible to extend the functionality of the SQL engine. The Connection Repository will allow UDFs to to be added to your database.

To create or modify a UDF, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must be logged into the database as a user with the CREATE FUNCTION or ALTER permission to add or modify UDFs.

To add a new UDF, from the tree view within the Connection Repository, right-click the FUNCTION icon and select Create Function.

To modify a UDF, from the tree view within the Connection Repository, right-click on the function and select Properties.

User Defined Function Field Descriptions

Name (required)

Enter the name for the UDF. This will be the name used to invoke the function.

Parameters

Enter input and result parameters for the function in this grid.

Script

Enter one or more SQL statements to be executed when the function is invoked.

OK

Click OK to add the UDF to the database or modify an existing UDF.

Cancel

Cancels the current operation and exits the screen.

See Also

[Deleting a User Defined Function](arc_deleting_a_user_defined_function.md)
