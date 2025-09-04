---
title: Ace Adsddremovetrigger
slug: ace_adsddremovetrigger
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddremovetrigger.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: afd77f12fd9736dcd4828809c6f034650cd586f4
---

# Ace Adsddremovetrigger

AdsDDRemoveTrigger

AdsDDRemoveTrigger

Advantage Client Engine

| AdsDDRemoveTrigger  Advantage Client Engine |  |  |  |  |

Removes a trigger from the database.

Syntax

UNSIGNED32 AdsDDRemoveTrigger( ADSHANDLE hDictionary,

UNSIGNED8 \*pucName );

Parameters

| hDictionary (I) | A data dictionary connection. |
| pucName (I) | The name of the trigger to be deleted. |

Remarks

Removes the specified trigger from the database.

The pucName property should be qualified with the table name the trigger belongs to followed by two colon characters ( :: ). For example, "Customers::AfterInsertTrig" would specify you want to remove the trigger called "AfterInsertTrig" that belongs to the "Customers" table.

If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.

Note ALTER permissions on the associated table are required to create a trigger. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Example

ulRetVal = AdsDDRemoveTrigger( hConn, "MyTrigger" );

See Also

[AdsDDCreateTrigger](ace_adsddcreatetrigger.md)
