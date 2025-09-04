---
title: Arc Creating Or Modifying A Trigger
slug: arc_creating_or_modifying_a_trigger
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_a_trigger.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 91ce7fcbf42a43e8b64cfcbb32d93d6190d2f6f9
---

# Arc Creating Or Modifying A Trigger

Creating or Modifying a Trigger

Creating or Modifying a Trigger

Advantage Data Architect

| Creating or Modifying a Trigger  Advantage Data Architect |  |  |  |  |

A trigger is a piece of code (similar to a stored procedure) that is executed on the server. Triggers differ from stored procedures because triggers are not called by the client, but instead are executed automatically in response to an insert, update, or delete operation.

See [Triggers](master_triggers.md) for topics containing detailed trigger information.

To create or modify a trigger, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with ALTER permissions on the associated table in order to add or modify triggers in a database. To create a [database trigger](master_database_triggers.md), you must have ALTER permissions on the database.

To add a new trigger, from the tree view within the Connection Repository, right-click the table you want to add the trigger to and select Triggers. Fill in the trigger options and then click OK.

To modify a trigger, from the tree view within the Connection Repository, right-click the table that owns the trigger you want to modify and select Triggers. Select the trigger in question from the Name combo box. Make your modifications, and then click OK.

To add or modify a database trigger, right-click the database object in the Connection Repository and select Database Triggers. The same dialog will be presented as for table triggers.

Note If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.

Advantage Trigger Field Descriptions

Name

Name of the trigger being modified or created. If creating a new trigger the value in this field will be <new>.

Trigger Type

The type of trigger to create. The trigger type will specify when the trigger should fire. See [Triggers](master_triggers.md) for detailed trigger type information.

Event Type

The event that will cause the trigger to fire. See [Triggers](master_triggers.md) for detailed trigger event information.

Priority

The triggers firing priority. If multiple triggers exist for the same event this value can be used to specify what order the triggers will fire in.

Description (optional)

Text description of the trigger.

Trigger Container

Script

Enter the SQL script here. The script can contain any number of SQL statements separated by semi-colons.

Windows DLL or Linux Shared Object

Container Path and Filename

The path and filename of the trigger container.

Function Name in Container

The name of the function to call in the container.

COM Object or .NET Assembly

Program ID (ProgID)

The ProgID of the COM object or .NET assembly that contains the trigger function.

Method Name in Class

The name of the function to call in the container.

Options

Trigger options. See [Triggers](master_triggers.md) for detailed trigger option information. For database triggers, the only option available is the Disabled option; the other options are not applicable to database triggers.

Delete

This button can be used to delete an existing trigger.

Verify Syntax

This can be used when entering a script trigger to verify the SQL syntax before saving the trigger.

Debug/Test

This can be used to start the SQL debugger for script triggers. An SQL window will be opened with an initial SQL statement that can be used to cause the trigger to fire. For some triggers, it may be necessary to edit the SQL appropriately. For example, a CLOSE\_TABLE database trigger requires a valid table name. Make sure the SQL script refers to a valid table.

The Debug/Test button is disabled for CONNECT and DISCONNECT database triggers. See [Debugging an External Application](arc_debugging_an_external_application.md) for general information on debugging objects such as triggers from another application. For a CONNECT trigger, you can set a breakpoint on the trigger of interest and then make a connection from another application. Be aware that if you cause a connect within the debugging instance of Advantage Data Architect while debugging the CONNECT trigger, it will not be able to respond to the debug event and the application will freeze. So while you are debugging a CONNECT or DISCONNECT trigger, you should not open additional windows in that instance of Advantage Data Architect, because that can result in new connections.

Note that when debugging OPEN\_TABLE triggers, cursor caching is turned off in order to ensure that tables are physically opened rather than being pulled from the cache. In order to restore the default cache settings, it is necessary to close and reopen Advantage Data Architect.
