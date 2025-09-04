What's New in Advantage 9




Advantage Database Server 12  

What's New in Advantage 9

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What's New in Advantage 9  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - What's New in Advantage 9 Advantage Database Server master\_What\_s\_new\_in\_advantage\_9\_0 Advantage Database Server > Introduction > What's New in Advantage 9 / Dear Support Staff, |  |
| What's New in Advantage 9  Advantage Database Server |  |  |  |  |

Visual SQL Debugger

A fully functional SQL debugger is integrated into the Advantage Data Architect (ARC) SQL Utility. The debugger can be used to set breakpoints, step through scripts line by line, view variable data, call stack information, and other useful debugging information. The debugger can be used to find problems in existing SQL scripts, and can be helpful when writing and testing new scripts.

The SQL debugger provides the following functionality:

|  |  |
| --- | --- |
| · | Line breakpoints |

|  |  |
| --- | --- |
| · | Object breakpoints (breakpoints in stored procedures, triggers, functions, etc.) |

|  |  |
| --- | --- |
| · | Line-by-line statement execution |

|  |  |
| --- | --- |
| · | Variable inspection |

|  |  |
| --- | --- |
| · | Call stack inspection |

|  |  |
| --- | --- |
| · | Debug connections made by external applications (applications other than ARC) |

|  |  |
| --- | --- |
| · | "Break" into script execution at any point. Useful for finding infinite loops or portions of a script that are consuming too much time. |

|  |  |
| --- | --- |
| · | Persist changes made to database objects (stored procedures, triggers, etc) back to the database by simply choosing to save the editor buffer. |

64-bit Windows and Linux Servers

In order to further enhance scalability, support for the x86\_64 architecture was added to the Advantage Database Servers for Windows and Linux. On computers with an x86\_64 processor and a 64 bit Operating System the Advantage Database Server will now be able to use memory in excess of 4GB. The extra memory will allow more users to access the server concurrently and increase the amount of information the server can cache when processing queries.

Dynamic Server Configuration

Advantage is no longer limited to the initially configured number of connections, tables, indexes, work areas, and locks. If all the available resources are in use, Advantage will allocate more resources, as opposed to returning an error as it has in the past. The configuration values are no longer maximum values, but used as initial allocation values. This can be convenient if the majority of your installations never need more resources than originally configured, but a few outliers often exceed your initial configuration values. Instead of returning errors, Advantage will automatically adjust to handle the new requirements. See the [Advantage Database Server Configuration Overview](master_advantage_database_server_configuration_overview.htm) help page for more details.

Notifications

Notifications are a mechanism that allows an action at the server to proactively notify clients that an event they are interested in has occurred. For example, an event can be signaled by a trigger on a table. When the trigger is executed all connections waiting on the event will be notified.

Clients use the canned procedure sp\_CreateEvent to register for event notifications. Once registered, the client can call sp\_WaitForEvent or sp\_WaitForAnyEvent to efficiently wait for the event to be signaled. Events are signaled using the sp\_SignalEvent procedure.

See the [Notifications](master_events_notifications_.htm) help page for more details.

Visual FoxPro 9 File Format Support

Advantage support for FoxPro DBF tables and CDX/IDX index files has been enhanced to include all data types supported by Visual FoxPro 9. This includes support for Auto-increment, BLOB (Binary Large Objects), Currency, DateTime (timestamp), VarBinary, and VarChar field types.

Null field support has also been added to give true SQL-style NULL handling for Visual FoxPro DBF tables. Support for true unique (candidate) indexes is now also available on DBF tables; this allows for better SQL optimization, the definition of primary keys, and the creation of referential integrity rules.

Additionally, support for long field names with DBF tables has been added. In addition to supporting the robust and high-performance Advantage proprietary locking on the new table format, Advantage also supports Visual FoxPro compatibility locking, which allows you to use Advantage-enabled applications to share tables with existing Visual FoxPro applications that are not using Advantage.

Visual FoxPro Upsizing Utility

To complement the enhanced support for Visual FoxPro tables, this release includes an upsizing utility that aids in updating your application to use your existing Visual FoxPro tables with Advantage Database Server.

It is not necessary to update your tables or indexes to allow them to be used with Advantage Database Server. However, the upsizing utility will export much of the information in your Visual FoxPro Database Container (.DBC) to an Advantage Data Dictionary (.add) to allow support for features such as long field names, primary keys, referential integrity, and triggers.

This utility, written as a Visual FoxPro application that you can modify, currently has the ability to export view definitions, referential integrity rules, default field values, field and table validation rules, and primary keys.

Advantage Data Architect (ARC) Enhancements

The SQL Utility has been modified to include a visual SQL debugger. The debugger allows developers to step line-by-line through SQL scripts, stored procedures, triggers and user defined functions. Users can set breakpoints, inspect variables, inspect the call stack, etc.

The SQL Utility now uses a multi-tabbed editor, allowing multiple documents to be opened at once.

All windows in the SQL Utility are now dockable.

Keyboard shortcuts in the SQL Utility can be modified via the SQL options dialog.

Added find and replace functionality to the SQL Utility.

ARC now supports Windows themes.

Many designers have been changed from modal dialogs to non-modal dialogs, allowing multiple designers to be open at the same time. For example, multiple Table Designers can be open in one ARC instance.

ARC now has the ability to automatically detect and install new service updates.

Added the Application ID to information returned by the management API and in the ARC Remote Management Utility.

Replication Enhancements

A new pause property has been added to replication subscriptions. This new property can be used to pause replication processing on a specific subscription.

New merge functionality has been added. By enabling the MERGE UPDATE article option, if a record being updated is not found at the target, it is then inserted instead of returning an error. Likewise with the MERGE INSERT article option enabled, if a record being inserted already exists at the target, it will be updated rather than returning an error.

Added Support for the SQL MERGE Statement

The [MERGE](master_merge.htm) statement attempts to match each record of one table with one or more records of another table. For each matching record found in the first table, an UPDATE on the record is performed using the UPDATE specification. If no matching record is found, an INSERT into the first table is performed using the INSERT specification. If the UPDATE specification is not defined, no action will be taken when a match occurs. Likewise if the INSERT specification is not defined, no action will be taken when no matches occur.

SQL Engine and AOF Performance Enhancements

The server will now attempt to optimize multi-segmented AOFs connected with the logical AND operator by evaluating the most restricted segment first. When the evaluation of the more restrictive segments results in only a few rows passing the filter, the server will short-circuit the index scan of the less restrictive segments, avoiding the cost of scanning many index pages. This optimization is most useful when the filter is applied to a very large table (>1000000 rows) and when one or more conditions are significantly more restrictive than the others. Since AOFs are used extensively by the SQL engine, this optimization will provide a positive impact on the performance of certain SQL statements.

New SQL RDD for Visual Objects

The VO AXSQL RDDs (AXSQLADT, AXSQLCDX, AXSQLNTX) are now fully supported. These new drivers provide a native way to utilize the Advantage SQL Engine using the existing VO RDD architecture. Previously these drivers were released only as prototypes.

Support for VarChar and VarBinary Field Types

Support has been added for two new field types for storing variable length data in Advantage ADT tables. These new VarChar and VarBinary fields are created with a maximum length that can be up to 64,000 bytes. These fields are similar in usage to the existing Char and Raw field types except that when the data is retrieved from the field it is not space or zero padded (unless the data was specifically stored with spaces or zeros on the end). Data for these field types is stored entirely in the table and does not result in memo file usage.

Support for Visual FoxPro-Compatible Collation Tables

Support has been added for Visual FoxPro-compatible collations for code pages 437, 620, 737, 850, 852, 857, 861, 865, 866, 895, 1250, 1251, 1252, 1253, and 1254. This includes the Visual FoxPro collations CZECH, DUTCH, GENERAL, GERMAN, GREEK, HUNGARY, ICELAND, MACHINE, NORDAN, POLISH, RUSSIAN, SLOVAK, SPANISH, SWEFIN, TURKISH, and UNIQWT.

These collations can be used with Visual FoxPro tables and Advantage ADT tables. One benefit of these tables is that they provide the ability to give case-sensitive query and filter capabilities to normal character fields. In addition, they provide for better sorting characteristics when using characters with diacritics. They also provide support for expansion and contraction characters. For example, when using one of the Spanish collations, the character pairs "ch" and "ll" are handled and sorted as a single collation element. These collations are dynamically loaded on demand and do not have to be stamped into the server.

TDataSet Descendant Version Management Utility

The TDataSet Switch utility allows developers to maintain multiple projects on a single PC, even if each project uses a different version of the Advantage TDataSet Descendant.

The utility provides an automated mechanism which modifies the version of the Advantage TDataSet Descendant that the IDE uses, in addition to updating the Advantage Client Engine DLLs in the path.

The utility is installed with the Advantage TDataSet Descendant (Delphi 3 through 7) and the Advantage Delphi Components. The TDataSet\_Switch.exe program is installed in the "Switch" subdirectory of the Advantage TDataSet Descendant installation directory. By default, the utility is installed to:

C:\Program Files\Advantage X.X\TDataSet\Switch\TDataSet\_Switch.exe

Miscellaneous SQL Engine Changes

Named and unnamed parameters are now supported in all script statements, except when they are in the cursor definition or in the text of an EXECUTE IMMEDIATE statement.

Added support for the ALTER PROCEDURE and ALTER TRIGGER statements.

The SQL engine will use existing indexes that have !DELETED() condition clauses on them in more situations. If deleted DBF records are being filtered, indexes with !DELETED() conditions will be used for optimizations such as ORDER BY clauses and aggregate functions. In addition, Visual FoxPro candidate indexes with !DELETED() conditions will be used for additional SQL optimizations. Note that the client version must be at least 9.0 or greater in order to use these optimizations.

New Default User Groups

The Data dictionary now has predefined roles for administrators (DB:Admin), backup users (DB:Backup), and SQL debuggers (DB:Debug). These user groups have predefined access permissions that allow the users in the group to perform the specified functionality.

In addition, the Data dictionary now has a predefined role (DB:Public) that includes all users in the database. This predefined role makes it possible to grant permissions on specific database objects to all users in the database.

Added Support for Field and Record Constraints to DBF Tables

Previously only available on ADT tables, field and record level constraints are now available for use on DBF tables that are part of a data dictionary. Constraints include, but are not limited to: default field values, minimum field values, maximum field values, etc.

Note that when using constraints on DBFs, you must always open the table through the Advantage data dictionary in order for the constraints to be enforced. DBF tables can be opened as free tables both by Advantage enabled applications and non-Advantage applications; in this situation, the constraints will not be enforced.

Binary Concatenation Operator Supported in DBF Tables

Support for the binary concatenation operator (specified with the semicolon character) has been added to the DBF table format and can be used when you open DBF/CDX tables with the new ADS\_VFP table type. This provides an efficient mechanism for combining different field types in a single index without the use of conversion functions as well as the ability to avoid having completely NULL keys when one field in an index expression is NULL. Note that if you use this operator, the resulting index will not be compatible with Visual FoxPro.

Variable Length Key Expressions Supported

The ability to specify index expressions that may result in variable length data is now supported. For example, if you use the TRIM() function in index expressions without having to use other functions to pad the result to a fixed length.

Miscellaneous Full Text Search Enhancements

FTS indexes can be created using the new extended collations. When using the non-MACHINE collations, searches will be accent-insensitive. For example a search for "resume" will find "résumé"

The behavior of CONTAINS(\*, 'search') has been improved. It now searches across multiple fields in a more intuitive fashion. For example, if two fields have FTS indexes, then a search such as CONTAINS(\*, 'word1 and word2') will find records where word1 is contained in one FTS-indexed field and word2 is in a different FTS-indexed field. Previously, the search would succeed only if both search words were found in the same field. The NEAR operator still requires that the related search terms be in the same field.

Added "Advantage Database Server: A Developers Guide" to the Help System

The entire contents of "Advantage Database Server: A Developers Guide" (ISBN: 978-1-4259-7726-9) by Cary Jensen and Loy Anderson is now available in the help system.

Improved Transaction Performance

Improved performance of some situations involving larger transactions (transactions involving thousands of updates). In particular, if multiple SQL statements are run during the transaction, filtering and processing of updated records can be significantly faster.

Enhanced Reindex

Reindex performance has been enhanced. In the past the table was scanned once as each index was created. In Advantage 9, all indexes are created based on a single scan of the table data, resulting in increased performance, most notably on larger tables.

Combined the Advantage U.S. and International Servers

There is no longer a server specific to the U.S. and a server specific to international regions. Advantage has been built as a single server that provides all collation options previously only available in the international build.

Enhanced Backup and Restore Functionality

Advantage [Online Backup](master_online_backup.htm) functionality will now include DLLs for Advantage Extended Procedures (AEPs) and Triggers in the backup image, and restore them when performing a restore operation.

The adsbackup utility has a new option (-x) to skip log file creation if no errors were reported.

A new option has been provided, TableTypeMap, that can be used in free table backup and restore operations to facilitate backing up and restoring a directory full of free tables of various table types, for example a directory with both ADT and DBF tables.

Added Ability to Flip Index Descend Flag at Runtime

The AdsSetIndexDirection API can be used to change the value of the descend flag, so a single index can be used to traverse data in either direction.

Added new AdsSkipUnique API

The AdsSkipUnique API will allow emulation of the SQL DISTINCT operator when operating at the table/navigational level. Each skip moves to the next unique record value in the specified index.

Added Support for Crystal Reports v11 R2 and Crystal Reports 2008

Support for Crystal Reports version 11 R2, and Crystal Reports 2008 has been added to the native Advantage Crystal Reports driver.

Note the Advantage OLE DB driver is still the recommended driver when creating new reports. See the notes in the Crystal Reports Overview help page for details.

In addition, the Crystal Reports driver has been modified to allow changing table names that a report is to be run against to temporary tables at run time.

Added Support for CodeGear RAD Studio 2007 and 2009

CodeGear RAD Studio 2007 and 2009 support has been added to the Advantage Delphi Components installation, which is the TDataSet Descendant install for Delphi versions greater than Delphi 7.

The Default Installation Path Has Changed

The default installation path of all Advantage products has changed. The new default path is c:\Program Files\Advantage 9.0\

Dropped Support for Some Platforms and Technologies

Windows NT is no longer a supported platform.

The following Delphi and C++Builder versions will no longer be supported. Most will continue to be available in the installation as a courtesy, but the Advantage Technical Services team will not provide support for them.

|  |  |
| --- | --- |
| · | Delphi 3, 4, 5, 8 and 2005 |

|  |  |
| --- | --- |
| · | C++Builder 3 and 4 |

The Advantage Borland Data Provider (BDP) will no longer be supported. Borland/CodeGear has deprecated this technology.

The following Crystal Reports versions will no longer be supported. The drivers will continue to be available in the installation as a courtesy, but the Advantage Technical Services team will not provide support for them.

|  |  |
| --- | --- |
| · | Crystal Reports version 6.X |

|  |  |
| --- | --- |
| · | Crystal Reports version 7.X |

|  |  |
| --- | --- |
| · | Crystal Reports version 8.X |