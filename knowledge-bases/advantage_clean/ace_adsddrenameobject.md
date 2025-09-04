---
title: Ace Adsddrenameobject
slug: ace_adsddrenameobject
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddrenameobject.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4d66cf526b99933c2ab525a5e5ebc67374b38bca
---

# Ace Adsddrenameobject

AdsDDRenameObject

AdsDDRenameObject

Advantage Client Engine

| AdsDDRenameObject  Advantage Client Engine |  |  |  |  |

Rename a data dictionary object.

Syntax

UNSIGNED32 AdsDDRenameObject( ADSHANDLE hDictionary,

UNSIGNED8 \*pucObjectName,

UNSIGNED8 \*pucNewObjectName,

UNSIGNED16 usObjectType,

UNSIGNED32 ulOptions );

Parameters

| hDictionary (I) | Handle of a database connection). |
| pucObjectName (I) | Name of object to rename. |
| pucNewObjectName (I) | New name for the object. |
| usObjectType (I) | Database object type.  Can be ADS\_DD\_TABLE\_OBJECT, ADS\_DD\_RELATION\_OBJECT, ADS\_DD\_VIEW\_OBJECT, ADS\_DD\_USER\_OBJECT, ADS\_DD\_USER\_GROUP\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT, ADS\_DD\_LINK\_OBJECT, ADS\_DD\_TRIGGER\_OBJECT, ADS\_DD\_PUBLICATION\_OBJECT, ADS\_DD\_SUBSCRIPTION\_OBJECT, ADS\_DD\_PACKAGE\_OBJECT, or ADS\_DD\_FUNCTION\_OBJECT. |
| ulOptions (I) | Renaming options. Specifying ADS\_KEEP\_TABLE\_FILE\_NAME when renaming table objects will not rename the physical table file. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The given new object name cannot be already in use by another dictionary object. |
| AE\_TABLE\_NOT\_EXCLUSIVE | When renaming tables, the table must not be open by any user. |

Remarks

AdsDDRenameObject can be used to rename an existing data dictionary object. Renaming tables requires that the table not be open by any user. By default, Advantage Database Sserver will rename the physical file to match the new table's object name. Specifying ADS\_KEEP\_TABLE\_FILE\_NAME will cause Advantage Database Server to not rename the physical file.

If the usObjectType parameter specifies a trigger object, the pucObjectName and pucNewObjectName parameters should be qualified with the table name the trigger belongs to followed by two colon characters ( :: ). For example, "Customers::AfterInsertTrig" would specify you want to rename the trigger called "AfterInsertTrig" that belongs to the "Customers" table. For [database triggers](master_database_triggers.md), use the unqualified name of the trigger.

If the usObjectType parameter specifies a function object that belongs to a package, the pucObjectName parameter should be qualified with the package name with a leading colon and two colons between the function and package names.  For example, ":Common::StringPad" would specify you want to rename the function called "StringPad" that belongs to the "Common" package.  Functions that do not belong to a package must not provide a package name or any colon characters in the name.  Whether or not the function belongs to a package, the pucNewObjectName parameter should simply be the new function name without any package name or colon characters.

Note Renaming a user while that user is connected is not recommended. The renamed user's permissions will not be affected in any way, but some places where the user name is logged may not reflect the user's new name.

Note Scripts, views, etc which contain references to renamed objects will not be automatically modified to reflect name changes.

See Also

[sp\_RenameDDObject](master_sp_renameddobject.md)
