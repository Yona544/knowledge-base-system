---
title: Master Effects Of Upgrading To Advantage 8 1
slug: master_effects_of_upgrading_to_advantage_8_1
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_effects_of_upgrading_to_advantage_8_1.htm
source: Advantage CHM
tags:
  - master
checksum: cea2225ce2cae61ff7fd53e8a3a40105627efbf2
---

# Master Effects Of Upgrading To Advantage 8 1

Effects of Upgrading to Version 8.1

Effects of Upgrading to Version 8.1

Advantage Database Server

| Effects of Upgrading to Version 8.1  Advantage Database Server |  |  |  |  |

The following Advantage functionality changes may affect your applications if you upgrade to Advantage version 8.1.

Effects of Upgrading

General

Support for the Numeric field type was added to the proprietary Advantage ADT table format. This can affect your application if it creates ADT tables using the Numeric field specification either though SQL or through the AdsCreateTable API. In older versions of Advantage, a Numeric field specification for an ADT would result in a short integer, long integer, or floating point field type being created depending on the precision and scale of the specification. Beginning with v8.1, the Numeric field specification will result in a Numeric field. It is important to note that the size in the field specification refers to the total length of the field. This is the same as with DBF tables, however with ADT tables, Advantage reserves one byte for the sign even for positive integers. For example, creating a table through SQL with the definition "num Numeric(2,0)" will produce a two byte numeric field with no decimal places. If it is in a DBF table, the range of values that can be stored in it is -9 to 99. With ADTs, the maximum precision is the same for both positive and negative numbers. The range of values that can be stored is -9 to 9 for this two byte field.

The SORT\_BUFFER configuration parameter that controls the amount of memory used by the server during index builds was changed from a 16-bit value to a 32-bit value to allow a larger buffer size to be specified. The corresponding member variable in the ADS\_MGMT\_CONFIG\_PARAMS structure was renamed from usSortBuffSize to ulSortBuffSize. If you reference this value in an application, you will get a compile-time error when you rebuild the application with new header files. When retrieving the configuration parameters via the AdsMgGetConfigInfo API with an old client, only the low two bytes of the SORT\_BUFFER configuration value will be returned in usSortBuffSize.

The AdsConvertTable function no longer converts the DBF numeric field type into a Double or Integer type in the destination ADT table. The DBF numeric field type is now converted directly into an ADT numeric field type.

SQL queries which use the TOP limiter on UNION-ed statements may return different result sets. This is due to the new support for TOP on subqueries. For example, the statement SELECT TOP 1 \* FROM table1 UNION ALL SELECT \* FROM table2 in the past would only return one record. Moving forward, the same query will return one record from the first SELECT statement, plus all records from the second SELECT statement. To apply the TOP 1 to the entire result set and achieve the same result as in the past, a statement of the following form can be used: SELECT TOP 1 \* FROM (SELECT \* FROM

table1 UNION ALL SELECT \* FROM table2)

Three new reserved SQL keywords have been introduced: FUNCTION, RETURN and RETURNS. If existing SQL statements use any of these keywords as column or table identifiers, they will need to be enclosed in double quotes or square brackets.

Static cursors that use DBF tables as base tables may now use the "Numeric" column type in place of Double or Integer. The Numeric field type is supported by the ADT table type now and the static cursor no longer maps DBF numeric field types into ADT double or Integer fields.

Integer division expressions now follow the SQL standard of returning results as an integer data type. The fractional portion will be truncated.

Routines that manage trigger metadata, including trigger deletion, have been modified. If you use any of the following functions or canned procedures, read the function/procedure specific help page for details on identifying the trigger:

- AdsDDRemoveTrigger

- DROP TRIGGER

- sp\_RenameDDObject

- AdsDDRenameObject

- AdsDDGetTriggerProperty

- TAdsDictionary.GetTriggerNames

- TAdsDictionary.GetTriggerProperty

- TAdsDictionary.RemoveTrigger

These functions and procedures will still work when used on existing triggers in a database. If, however, new triggers are created, or if triggers are modified (via ARC, or by dropping and re-creating them), 5132 (object not found) errors will be returned. The trigger name now has to be qualified with a table name. See the function/ procedure specific help file page for details on the qualifier format.

Adding a new trigger to an existing database created by versions of Advantage older than 8.1 (or modifying trigger properties in Advantage Data Architect) will cause an internal database version update. This update will prevent pre-8.1 servers from opening the database.

Version 1 AEPs are effectively obsolete with this release. If you must use a version 1 AEP, there are now some limitations. 1) You must use AdsOpenTable to open the input and output parameter tables and pass ADS\_TEMP\_CURSOR\_TABLE as the ulOptions flag. 2) If the AEP is called from Advantage Database Server, you cannot open the input and output parameter tables with Advantage Local Server.

Script triggers now cache their statement handles. This means if a trigger modifies tables other than the table it is defined on, those tables will be held open until the table the rigger is defined on is closed. This behavior could cause 7008 or other open errors if attempts are made to gain exclusive access to the tables referenced by the trigger.

TDataSet Descendant

An internal function that locates the correct ads.ini file has been modified to use the host computer's search path to locate the file. The application path and system directory are still searched first, as in previous versions, but if an ads.ini file now exists in any directory in the search path, it will also be found and used.

Due to numeric field changes described above, applications that make use of persistent fields on TAdsQuery components will encounter errors when executing statements on DBF base tables that result in static cursors. These errors will only occur if the DBF table contains numeric fields. The error text will be: "Type mismatch for field 'XXXX', expeting: Float actual: BCD" In prior versions, those DBF numeric fields were converted to float fields in the resulting static cursor. The fields are now consistently maintained as numeric fields. The recommended fix is to modify the persistent field definitions by removing them and re-adding them. This will result in either a ftBCD field or a ftFmtBcd field. A second option is to use the new AdsTableOptions.AdsNumericsAsFloats option, which will force the old behavior of converting DBF numeric fields to float fields in static cursor results.

The following extended methods have been modified to post any pending edits before changing the restrictions on the dataset: AdsSetAOF, AdsSetFilter and AdsSetScope. This means if these methods are called when a record is in the edit state, the pending changes will be flushed before the method continues, and the dataset will no longer be in the edit state when the method returns. These changes were necessary to eliminate 5062 errors after these methods were called, which were caused because the dataset was out of sync with the Advantage Client Engine (ACE).

See Also

[Effects of Upgrading to Version 9.0](master_effects_of_upgrading_to_9_0.md)

[Effects of Upgrading from a Version Prior to v8.0](master_effects_of_upgrading_from_a_version_prior_to_v8_0.md)
