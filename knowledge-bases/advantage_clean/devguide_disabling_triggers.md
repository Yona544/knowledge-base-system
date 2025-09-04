---
title: Devguide Disabling Triggers
slug: devguide_disabling_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_disabling_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 77f4de40076f8ed1d1221c7beb47a8decd0c641e
---

# Devguide Disabling Triggers

Disabling Triggers

     Disabling Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Disabling Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Beginning with Advantage 8, it is possible to disable triggers. This can be done for the entire data dictionary, a specific connection, a specific table, or on a trigger-by-trigger basis. Normally, disabling triggers is something that an administrator will do during a maintenance operation. For example, you might want to disable an INSTEAD OF INSERT trigger prior to importing a large amount of data into one of your tables.

With the exception of certain maintenance operations, triggers should normally not be disabled. The value of triggers is that they always execute in response to record-level events, regardless of which client is performing the operation (at least with ADT tables). When you disable a trigger, those operations are no longer guaranteed.

When disabling triggers for a maintenance operation, you will normally disable triggers only on the connection through which the maintenance operation will be performed, enabling triggers once again or simply dropping the connection after the maintenance operation is complete. This approach ensures that the triggers are still enabled for all other users of the database.

To disable triggers on a specific connection, call the sp\_DisableTriggers system stored procedure, passing NULL in the first parameter and False in the third parameter. See the Advantage help for details about using sp\_DisableTriggers.

To disable triggers for the entire data dictionary, right-click the data dictionary node in the Connection Repository and select Properties. From the Advanced page of the Data Dictionary properties dialog box, check the Disable Triggers checkbox.

To disable only a single trigger, right-click the table to which the trigger is assigned in the TABLES node of your administrative data dictionary connection and select Triggers. Use the Name dropdown menu to select the trigger you want to disable. With that trigger displayed, check the Disabled checkbox. Enable the trigger once again by unchecking this checkbox.

To disable triggers for an entire table, right-click the table and select Properties to display the Table Designer. Select the Table Properties tab, and then set the Triggers Disabled option to Yes. Set Triggers Disabled to No to re-enable the table's triggers.

 

In the next chapter you will learn how to back up your data using the ADS online backup capabilities.
