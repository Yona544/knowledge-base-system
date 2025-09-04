sp\_RenameDDObject




Advantage Database Server 12  

sp\_RenameDDObject

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_RenameDDObject  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_RenameDDObject Advantage SQL Engine master\_Sp\_renameddobject Advantage SQL > System Procedures > Procedures > sp\_RenameDDObject / Dear Support Staff, |  |
| sp\_RenameDDObject  Advantage SQL Engine |  |  |  |  |

Rename a data dictionary object.

Syntax

sp\_RenameDDObject(

 ObjectName, CHARACTER,200,

 NewObjectName, CHARACTER, 200,

 ObjectType, INTEGER,

 Options, INTEGER )

Parameters

|  |  |
| --- | --- |
| ObjectName (I) | Name of object to rename. |
| NewObjectName (I) | New name for the object. |
| ObjectType (I) | Database object type.  Can be:  1 (ADS\_DD\_TABLE\_OBJECT)  2 (ADS\_DD\_RELATION\_OBJECT)  6 (ADS\_DD\_VIEW\_OBJECT)  8 (ADS\_DD\_USER\_OBJECT)  9 (ADS\_DD\_USER\_GROUP\_OBJECT)  10 (ADS\_DD\_PROCEDURE\_OBJECT)  12 (ADS\_DD\_LINK\_OBJECT,)  14 (ADS\_DD\_TRIGGER\_OBJECT)  15 (ADS\_DD\_PUBLICATION\_OBJECT)  17 (ADS\_DD\_SUBSCRIPTION\_OBJECT)  18 (ADS\_DD\_FUNCTION\_OBJECT)  19 (ADS\_DD\_PACKAGE\_OBJECT) |
| Options (I) | Renaming options. Specifying 1 (ADS\_KEEP\_TABLE\_FILE\_NAME) when renaming table objects will not rename the physical table file. Specifying 0 (zero) will rename the tables physical file. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The given new object name cannot be already in use by another dictionary object. |
| AE\_TABLE\_NOT\_EXCLUSIVE | When renaming tables, the table must not be open by any user. |

Remarks

sp\_RenameDDObject can be used to rename an existing data dictionary object. Renaming tables requires that the table not be open by any user. By default, Advantage Database Server will rename the physical file to match the new table's object name. Specifying 1 (ADS\_KEEP\_TABLE\_FILE\_NAME) will cause Advantage Database Server to not rename the physical file.

If the ObjectType parameter specifies a trigger object, the ObjectName and NewObjectName parameters should be qualified with the table name the trigger belongs to followed by two colon characters ( :: ). For example, "Customers::AfterInsertTrig" would specify you want to rename the trigger called "AfterInsertTrig" that belongs to the "Customers" table. For database triggers, use the simple unqualified trigger name.

If the ObjectType parameter specifies a function object that belongs to a package, the ObjectName parameter should be qualified with the package name with a leading colon and two colons between the function and package names.  For example, ":Common::StringPad" would specify you want to rename the function called "StringPad" that belongs to the "Common" package.  Functions that do not belong to a package must not provide a package name or any colon characters in the name.  Whether or not the function belongs to a package, the NewObjectName parameter should simply be the new function name without any package name or colon characters.

Note Renaming a user while that user is connected is not recommended. The renamed user's permissions will not be affected in any way, but some places where the user name is logged may not reflect the user's new name.

Note Scripts, views, etc which contain references to renamed objects will not be automatically modified to reflect name changes.

Example

-- rename a table

EXECUTE PROCEDURE sp\_RenameDDObject( 'oldtable', 'newtable', 1 /\* ADS\_DD\_TABLE\_OBJECT \*/, 1 /\* ADS\_KEEP\_TABLE\_FILE\_NAME \*/ );

-- rename a table trigger

EXECUTE PROCEDURE sp\_RenameDDObject( 'mytable::oldtrigname', 'mytable::newtrigname', 14 /\* ADS\_DD\_TRIGGER\_OBJECT \*/, 0 );

-- rename a database trigger

EXECUTE PROCEDURE sp\_RenameDDObject( 'LogOpens', 'LogOpenTableCalls', 14 /\* ADS\_DD\_TRIGGER\_OBJECT \*/, 0 );

See Also

[AdsDDRenameObject](ace_adsddrenameobject.htm)