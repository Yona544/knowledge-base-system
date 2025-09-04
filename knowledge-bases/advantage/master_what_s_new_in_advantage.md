What's New in Advantage




Advantage Database Server 12  

What's New in Advantage 8.0

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What's New in Advantage 8.0  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - What's New in Advantage 8.0 Advantage Database Server master\_What\_s\_new\_in\_advantage Advantage Database Server > Introduction > What's New in Advantage 8.0 / Dear Support Staff, |  |
| What's New in Advantage 8.0  Advantage Database Server |  |  |  |  |

Development & Usability Features

Redesign of Advantage Data Architect

Advantage Data Architect (ARC) is the primary database designer and database administration tool for Advantage Database Server. ARC 8.0 has been redesigned to be the most efficient, cohesive, and productive Advantage developer tool to date. Benefits of ARC 8.0 include a redesigned graphical interface with more efficient workflow and an updated design. Users of modern IDEs such as Delphi 2005 and MS Visual Studio will find ARC 8.0 to be a simple extension of their chosen development environment.

Advantage Replication Support

The uses and benefits of replicating data from one server to another are obvious. Now, replication support is built in to Advantage Database Server and can easily be added to any 8.0 server as a separately licensed module. Advantage Replication is based upon an asynchronous push model in order to minimize performance impact on applications and to minimize latency in delivery of updates to target databases. Replication provides the capability to transmit all updates in a source database to structurally equivalent tables in one or more target databases. If two-way replication is necessary, rules can be specified at the target database to replicate changes back to the source or to other databases. If multiple target databases are used where each target has only a subset of the data, filters can be specified at the source in order to control the delivery of data to the target databases. Transactional and referential integrity is maintained during replication. If a target database is not available, the source server will queue up all updates and transmit them to the target when it becomes available. Conflict resolution can be handled by "CONFLICT" triggers on target tables. Replication will only be available for "remote" server (i.e., Advantage Database Server, not Advantage Local Server) and will be limited to Data Dictionary tables only (including DBF tables specified in the data dictionary).

Advantage Online Backup Functionality

The capability to perform database backup procedures is an extremely important database process and allows database users the ability to keep multiple copies of database files on different servers and at different physical locations. Advantage remote server (i.e., Advantage Database Server, not the Advantage Local Server) includes backup functionality providing Advantage users an easy to use and powerful database backup option. Advantage backup functionality includes full backups and differential backups. A full backup is a complete backup of the entire database. A differential backup will only backup the changes made since the last full backup operation. All backups can be performed while the database is in use and will provide a logically correct "snapshot" of the database at the time the backup is started. Differential backup functionality is not supported on DBF tables.

SQL Scripting Language

An ANSI SQL PSM 2003 standard scripting language has been added to the Advantage SQL engine. New constructs include, but are not limited to:

|  |  |
| --- | --- |
| · | If/Else statements |

|  |  |
| --- | --- |
| · | Do/While loops |

|  |  |
| --- | --- |
| · | Local variables |

|  |  |
| --- | --- |
| · | Local cursor variables populated via SELECT statements |

|  |  |
| --- | --- |
| · | Exception handling |

This new scripting language is not limited to triggers and stored procedures. It can be used by any client interface that supports executing SQL statements. This means you can embed scripting code in your Delphi TAdsQuery components, ADO.NET command objects, Advantage Data Architect, PHP applications, etc.

Trigger Enhancements

|  |  |
| --- | --- |
| · | New scripting language support |

|  |  |
| --- | --- |
| · | AFTER triggers can now be used to update the same record that caused the trigger to fire. This operation would create a locking error in previous versions of Advantage. INSTEAD OF triggers are no longer required to update the same record that caused the trigger to fire, resulting in much simpler trigger statements. For example, if you want to maintain a specific field after each update to a record, you no longer have to write an INSTEAD OF trigger and worry about posting changes to all fields. The same functionality can now be implemented with a simple AFTER trigger that only modified the field in question. |

|  |  |
| --- | --- |
| · | Added the ability to temporarily disable a trigger. A specific trigger can be disabled for all users, for the active connection, or for an entire database. |

|  |  |
| --- | --- |
| · | Added the ability to update a trigger DLL while it is in use, without the requirement to disconnect existing users first. |

|  |  |
| --- | --- |
| · | Added the ability to update static views via an INSTEAD OF trigger. An INSTEAD OF trigger can be defined on a view, and then the trigger is responsible for updating the base tables involved in the view. |

SQL Enhancements

|  |  |
| --- | --- |
| · | Logging of all SQL queries and their optimization levels. This is an extension of the SQL query optimization and execution plan functionality created in Advantage 7.1. Now all queries can be logged as an application runs (through a test suite, for example) and be reviewed later to determine if there are optimization issues with SQL queries. This can be much easier than performing a specific optimization check for each query in your application. |

|  |  |
| --- | --- |
| · | Added ESCAPE character functionality to the SQL LIKE operator and updated the LIKE operator to allow expressions for both of its arguments. |

|  |  |
| --- | --- |
| · | Added support for subqueries anywhere an expression is allowed. |

|  |  |
| --- | --- |
| · | Added support for alias column names in the HAVING clause. |

|  |  |
| --- | --- |
| · | Added support for FULL and RIGHT [OUTER] JOIN syntax. |

|  |  |
| --- | --- |
| · | When executing an SQL script, if the last statement in the script is a SELECT statement, a cursor will be returned. This change makes using temporary tables that are populated using SQL statements more convenient. For example, the following script can be used to return a cursor with a final result set: SELECT DISTINCT name INTO #temp FROM demo; SELECT Count(\*) As "Number of Distinct Names" FROM #temp. Refer to the Advantage 8.0 README "Effects of Upgrading" section for implications to existing programs that expect the old behavior. |

|  |  |
| --- | --- |
| · | SQL scripts now allow different numbers and different types of parameters for the statements in the script. For example, the following script is now allowed: UPDATE demo SET name = ? WHERE id = 1; SELECT \* FROM customer WHERE id = 1. Refer to the Advantage 8.0 README "Effects of Upgrading" section for implications to existing programs that expect the old behavior. |

|  |  |
| --- | --- |
| · | Enhanced parameter support in SQL statements. Parameters may now be used as arguments to scalar functions. |

|  |  |
| --- | --- |
| · | Significant improvement of the execution speed of large SQL scripts. |

Transaction Savepoints

Transaction savepoints are markers inside of a transaction to which an application can return by partially rolling back the work performed in a transaction. When rolling back to a savepoint, all work performed after the savepoint was set is undone, and all work performed prior to the savepoint being set is unaffected. Savepoints are commonly used for modeling the consequences of different scenarios.

Application Identifier Support

A new per-application setting called ApplicationID has been added. This new identifier is initialized to the application (.exe) name and configurable via the sp\_SetApplicationID and sp\_GetApplicationID system procedures. The application identifier can be used, for example, to uniquely identify applications modifying a database when your product has many different interfaces.

DBF Tables and Memos Greater Than 4 Gigabytes

DBF tables can now be greater than 4 Gigabytes. This removes an artificial limitation upon DBF tables. Advantage is the only database management system that supports DBF tables this large. See the [DBF file specifications](master_dbf_field_types_and_specifications.htm) topic in the Advantage help file for the new size limitations, as limitations vary depending on the operating system and the file system.

Auto-Reconnect Functionality

Auto-reconnect functionality is designed to provide an enhanced and more graceful method for application developers to resolves circumstances where the Advantage Server goes down and then comes back up (e.g., another cluster node), but the application needs to be restarted to properly connect to the Advantage Server. Auto-reconnect will provide a better mode of support for applications that require 24/7 uptime and will help avoid situations where the application must be restarted. To aid in these situations, the Advantage Client Engine (ACE) timeout periods can be adjusted by the developer and the default timeout values have been lowered. Also, operations that release resources (e.g., closing a table or cursor) will no longer return errors to the client after a connection is lost.

Data Dictionary Additions

|  |  |
| --- | --- |
| · | Added the ability to rename dictionary objects without removing and re-adding them to the dictionary. |

|  |  |
| --- | --- |
| · | Added the ability to move a data dictionary object file (table, index, etc) without removing and re-adding it to the dictionary. |

New Error Log Table

Support has been added to the Advantage server for logging errors to an ADT table rather than a DBF table. This new log file is capable of storing more detailed error information. The default behavior now is to log to ads\_err.adt. If it is not possible to use this file, Advantage will revert to logging to the ads\_err.dbf file. The server configuration parameter ERROR\_LOG\_TYPE can be used to control which log file to use.

New Field Types

Two new field types have been added to the ADT table type. The RowVersion field type is a 64-bit integer value that is automatically updated by Advantage whenever a record is updated. The value is unique to the entire table. The ModTime field type contains a timestamp value that is automatically updated by Advantage with the current server time each time the record is inserted or updated.

Performance Features

Aggressive Caching

A much more aggressive and performance oriented method of index and static cursor caching has been implemented to improve overall application performance.

Transaction Processing

Performance of transaction processing has been significantly optimized.

Advantage Database Server to Advantage Client Engine Direct Communication

The Advantage Database Server and the Advantage Client Engine now communicate directly with each other rather than requiring communication through the network layer if the Advantage application and the Advantage Database Server are running on the same computer. This Inter-Process Communication (IPC) can greatly improve performance when it is used. A common scenario that this optimization applies to is when Advantage Database Server and some form of web server or application server are running on the same computer.

SQL Parsing

Performance of SQL parsing has been significantly enhanced.

Improved Performance of Filtered Record Count Operations

A subset of filtered record count operations that used to be done by the client have been pushed to the server, resulting in enhanced performance.

Improved the Performance of ALTER TABLE and AdsRestructureTable

The overhead associated with altering tables in data dictionaries has been reduced, resulting in faster alter operations.

Improved Correlated Subquery

Correlated subqueries have been optimized.

Improved GROUP BY Performance

The SQL engine now optimizes GROUP BY statements on large datasets by using existing indexes, as opposed to using an internal sorting algorithm that was only fast in older versions of Advantage when used on small datasets.

Improved VIEW and SubQuery Performance

Performance of SQL statements that use views or subqueries in the FROM clause has been improved. The SQL engine now checks to see if restrictions in the parent query may be applied to the child query.

For additional information and comparison benchmarks regarding performance of Advantage 8.0, please refer to the "Advantage 7.1 vs. Advantage 8.0 Performance Comparison" whitepaper available at www.AdvantageDatabase.com.

Security Features

Encrypted Indexes

Indexes on dictionary-bound ADT tables can now be encrypted providing enhanced security.

Encrypted Communications

All communication with the Advantage Database Server can now be encrypted when using dictionary connections. In the past, this encryption functionality was limited to internet connections to the Advantage Database Server.

Server-Side Aliases

For security-sensitive environments, Advantage 8.0 includes server-side alias support that will hide the data location from client applications. The applications connection string will reference the server and alias, but not a direct path to the data. This functionality also removes the need to share a data directory on the file server.

Deployment and Configuration Improvements

Changed Collation Language Setting to be per Connection Rather Than per Client

All connections will now use the collation language configured within the Advantage server they are connected to. This allows the same application to connect to multiple Advantage servers that are using different collation languages.

Improved the User Interface and Operation of ADSSTAMP.EXE

ADSSTAMP.EXE is an important Advantage Database Server deployment utility. The improvements to its user interface and overall operation will improve the process for upgrading server versions, expanding user counts, and most importantly, improve the installation of Service Updates.

Added Language Configuration Tab to the Advantage Database Server Configuration Utility (ADS\_CFG.EXE)

A new language tab in the Advantage Database Server Configuration Utility (ADS\_CFG.EXE) makes it easier to configure the language setting of the Advantage Database Server. A drop-down list box contains all available language choices. Simply choose a language, select the Apply button, and the Advantage Database Server will be configured with the new language. Note: If the Advantage Database Server is running when the Apply button is selected, it will need to be restarted for the change to take effect.

Improved Support for Network Attached Storage (NAS) Devices

Advantage Database Server now has the ability to fully utilize Network Attached Storage (NAS) devices. Advantage Database Server can now read and write data that is located on a device or server that is physically separate from the server on which Advantage Database Server is running. (Note: This functionality is only available for Windows servers).

.NET Enhancements

Added Support for AdsHelper Class in Advantage .NET Data Provider

The AdsHelper class is a .NET component that developers can include in their applications to simplify tasks such as creating DataSet and AdsDataReader objects, executing stored procedures, and executing SQL statements. It is an Advantage-specific implementation of the Microsoft Data Access Application Block for .NET version 2.

Added Support for Typed DataSets in Visual Studio .NET

Typed DataSets allow developers to access tables and columns by name, instead of using collection-based methods. Typed DataSets provide table and column access from Intellisense and strong typing of properties.

Added a "RowVersion" Field Type

The RowVersion is a new field type that is automatically updated by the server for every record write operation. This new field type can be used to implement optimistic locking from ADO.NET applications and provides a method to detect if a record has been modified by another user since it was last read by the current user.

Enhanced the AdsExtendedReader

The following new methods have been added to the AdsExtendedReader class: IsRecordLocked, IsRecordDeleted, IsTableLocked, and DeleteIndex. An indexer was also added to the extended reader to allow setting column values by name.