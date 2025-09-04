---
title: Arc Creating Or Modifying A Stored Procedure
slug: arc_creating_or_modifying_a_stored_procedure
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_a_stored_procedure.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 9b6623d6fde01edba0946f018edc86ed701b58cd
---

# Arc Creating Or Modifying A Stored Procedure

Creating or Modifying a Stored Procedure

Creating or Modifying a Stored Procedure

Advantage Data Architect

| Creating or Modifying a Stored Procedure  Advantage Data Architect |  |  |  |  |

Advantage Extended Procedures are stored procedures that are easy to develop. Like traditional stored procedures, Advantage Extended Procedures allow you to execute a set of code at the server where the data resides. This allows you to remove data intensive tasks from workstations and reduces your network traffic to a single send and receive operation. Unlike traditional stored procedures, Advantage Extended Procedures allow developers to write, store, and execute stored procedures on the server using their preferred application development tool. No database administrator is required to develop Advantage Extended Procedures. The Connection Repository will allow you to add Advantage Extended Procedures to your database.

To create or modify an Advantage Extended Procedure, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with CREATE PROCEDURE or ALTER permissions on the specific procedure in order to add or modify Advantage Extended Procedures in a database.

To add a new Advantage Extended Procedure, from the tree view within the Connection Repository, right-click the STORED PROCS icon and select Create.

To modify an Advantage Extended Procedure, from the tree view within the Connection Repository, right-click the Procedure's name icon and select Properties.

Advantage Extended Procedure Field Descriptions

Name (required)

Enter the name for the stored procedure. This will be the name used in the EXECUTE PROCEDURE statement.

Parameters

Enter input and output parameters for the procedure into this grid.

Script Container Type

Use this area to enter on or more SQL statements or an SQL script to execute when the stored procedure is called. For more information on scripts see XXX

DLL or Shared Object Container Type

Advantage Extended Procedure File or Advantage AEP Program ID (required)

Enter the path to your DLL or shared object file. You will need to enter the relative path of the AEP container file. This is the path in relation to the .ADD, .AM, and .AI files.

Stored Procedure Name (required)

Enter the stored procedure function name. This is the function that will be called when EXECUTE PROCEDURE is called. (Note: This is case sensitive.)

.NET Assembly or COM Object Container Type

Advantage AEP Program ID (required)

Enter the ProgID of your object.

Stored Procedure Name (required)

Enter the stored procedure function name. This is the function that will be called when EXECUTE PROCEDURE is called. (Note: This is case sensitive.)

OK

Click to add the stored procedure to the database. It can now be used in the EXECUTE PROCEDURE call. If you are modifying an existing stored procedure, clicking OK will remove the current stored procedure and create a new one.

Cancel

Cancels any input or changes and exits the screen.
