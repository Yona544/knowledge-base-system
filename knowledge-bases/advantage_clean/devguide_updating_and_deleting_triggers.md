---
title: Devguide Updating And Deleting Triggers
slug: devguide_updating_and_deleting_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_updating_and_deleting_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9b19aba74ab99ef0be73d1a834aec4a7cfa8bf04
---

# Devguide Updating And Deleting Triggers

Updating and Deleting Triggers

     Updating and Deleting Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Updating and Deleting Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You can update a trigger's description, as well as change which library and function/method to use for the trigger, the trigger type, or even the trigger event type. To do this, right-click the table name to which the trigger is assigned in the TABLES node of your data dictionary connection and select Triggers. Use the Name dropdown menu to select the existing trigger you want to modify. Make your changes and select OK to save your new settings. To delete a trigger, select it from the Name dropdown menu and click the Delete button.

If you change your trigger's library or function/method name, the new trigger will be used once the old trigger can be unloaded. With triggers implemented as .NET class libraries, this will occur when the last user to use a trigger in the trigger's container drops their connection to ADS.

With DLLs under ADS, you can often replace the trigger container even while the old container is loaded by ADS. Then, the updated trigger will be used the next time each user calls a function in the trigger container, on a user-by-user basis. This behavior is provided by an ADS feature called DLL caching. DLL caching is turned on by default, though you may want to disable it during debugging. For more information on DLL caching, please search for DLL Caching in the Advantage help index.

   
NOTE: DLL caching also applies to AEPs.
