What's New In Advantage 11




Advantage Database Server 12  

What's New in Advantage 11

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What's New in Advantage 11  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - What's New in Advantage 11 Advantage Database Server Whats\_New\_In\_Advantage\_11 Advantage Database Server > Introduction > What's New In Advantage 11 / Dear Support Staff, |  |
| What's New in Advantage 11  Advantage Database Server |  |  |  |  |

Online Table Maintenance

Added the capability to perform the following maintenance operations while a table is in use by one or more clients. Prior to ADS v11, it was necessary to open a table exclusively (thus disallowing any other use of the table) during the operation.  See [Online Table Maintenance](master_online_table_maintenance.htm).

|  |  |
| --- | --- |
| · | Online Pack - remove deleted records from a table while it is in use |

|  |  |
| --- | --- |
| · | Online Reindex - rebuild a table's indexes while it is in use |

|  |  |
| --- | --- |
| · | Online Alter - change a table's structure while it is in use (Add, delete, modify fields) |

Advantage Web Platform

The [Advantage Web Platform](web_advantage_web_platform.htm) is a web service that allows client-less access to Advantage data from any device, platform, or development environment that can make Internet (HTTP) calls. This includes but is not limited to devices such as desktop/laptops, mobile phones, PDAs, and tablets. It allows access from any current operating system including previously unsupported systems such as Mac OS and Android because no Advantage client is required. The Advantage Web Platform extends your application development opportunities and opens up endless possibilities to access Advantage from many different types of architectures, hardware, and business scenarios.

The Advantage Web Platform is a web service built on the standard OData web protocol to access data (www.odata.org).  The OData standard, follows RESTful principles, and allows you to build web applications that can run in limitless scenarios. You can write one application that can run equally well on an iPhone, Android, or a Windows or Mac desktop machine.

Advantage Web Administrator

The [Advantage Web Administrator](web_administrator_utility.htm) is an Advantage Database Server management utility that can be accessed from web browsers. It provides the ability to view server status, manage user connections, run SQL statements, etc.

New SQL Scalar Functions

The following scalar functions are now supported: [LastRowID](master_miscellaneous_functions.htm), [StartsWith](master_string_functions.htm), [EndsWith](master_string_functions.htm) and [SubstringOf](master_string_functions.htm).

Stored Procedures with Varying Output

SQL script stored procedures were enhanced with the capability to return the last SELECT or EXECUTE PROCEDURE statement in the script as the output of the stored procedure. This allows a stored procedure to return cursors (including live cursors) having a varying structure from call to call. See [Create Procedure](master_create_procedure.htm).

Improved Stored Procedure & Trigger Input Parameters

|  |  |
| --- | --- |
| · | It is now easier to reference input parameters in the [stored procedure](master_create_procedure.htm) script. The input parameters may now be referenced as \_paramX, \_paramY, etc. where paramX and paramY are the actual name of the stored procedure inputs. |

|  |  |
| --- | --- |
| · | [Trigger](master_create_trigger.htm) \_\_new cursors are automatically declared and can be accessed directly without a FETCH. |

New SQL Operator

The modulo operator, %, is now supported.

New Database Roles

New [database roles](master_database_base_roles.htm) SERVER:Admin and SERVER:Monitor have been added.

Root Dictionary

Advantage now supports a [root dictionary](master_root_dictionary.htm).  The root dictionary allows better control over security when using the Advantage Web Administrator Utility. System procedures through the Advantage Web Platform can only be run when connected to the root dictionary. Some of the changes include:

|  |  |
| --- | --- |
| · | [sp\_mgKillUser](master_sp_mgkilluser.htm) now requires [DB:Admin or SERVER:Admin](master_database_base_roles.htm) membership. Also, you must be connected to a dictionary to kill users on that dictionary. |

|  |  |
| --- | --- |
| · | sp\_mgKillUser allows a wild card (using an asterisk) to be given as the user name when run by a SERVER:Admin member on the root dictionary. |

|  |  |
| --- | --- |
| · | [sp\_GetSQLStatements](master_sp_getsqlstatements.htm) now requires DB:Admin membership and, with remote server, retrieves statements only from the current dictionary. |

New System Variables

Added new [system variables](master_system_variables.htm) ::conn.OSUserLoginName, ::conn.ClientHostName, ::conn.NetworkAddress, ::conn.IsRoot, and ::conn.TerminalClientAddress.

New System Procedures

The following system procedures have been added:

|  |  |
| --- | --- |
| · | [sp\_PackTableOnline](master_sp_packtableonline.htm) |

|  |  |
| --- | --- |
| · | [sp\_PackAllTablesOnline](master_sp_packtableonline.htm) |

|  |  |
| --- | --- |
| · | [sp\_ReindexOnline](master_sp_reindexonline.htm) |

|  |  |
| --- | --- |
| · | [sp\_ChangeCurrentUserPassword](master_sp_changecurrentuserpassword.htm) |

|  |  |
| --- | --- |
| · | [sp\_mgGetCrashDumpInfo](master_sp_mggetcrashdumpinfo.htm) |

|  |  |
| --- | --- |
| · | [sp\_GetLinks](master_sp_getlinks.htm) |

|  |  |
| --- | --- |
| · | [sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.htm) |

|  |  |
| --- | --- |
| · | [sp\_mgGetErrorLog](master_sp_mggeterrorlog.htm) |

|  |  |
| --- | --- |
| · | [sp\_DeleteReplicationEntry](master_sp_deletereplicationentry.htm) |

|  |  |
| --- | --- |
| · | [sp\_GetReplicationEntryDetails](master_sp_getreplicationentrydetails.htm) |

|  |  |
| --- | --- |
| · | [sp\_TestReplicationConnection](master_sp_testreplicationconnection.htm) |

Explicit Date, Time, and Timestamp Literals

Added support for explicit [date, time and timestamp](master_sql_literals.htm) literals.

Binary Literals

Support for [binary literals](master_sql_literals.htm).

Transaction Logs > 4GB

The transaction processing system has been updated to support transactions that result in writing more than 4GB of data to the transaction log file.

Support for SQL Intermediate Files > 4GB

SQL statements that produce intermediate files (for sorting, grouping, etc.) exceeding 4GB are now supported.

Improved Checks for Corrupt Memo Files

Improved the Memo and BLOB handling logic for the Advantage proprietary memo format (.adm) to more reliably detect memo corruption.

Reserve Connections for LAN or Web Platform Usage

Users connecting to Advantage through the Advantage Web Platform are counted as [separate users](master_web_platform_users.htm). To prevent the possibility of all Advantage user connections being taken up by traditional fully connected applications and leaving none available for web applications, Advantage now allows the total user count to be partitioned into two categories. The user count can be divided between users for traditional connected applications and Advantage Web Platform applications.

Connection Pooling

Connection pooling has been added to the Advantage Client Engine. The Advantage Web Platform uses pooling to provide high performance connection capability. This functionality is also available to your own applications through the [AdsConnect101](ace_adsconnect101.htm) API.

Restore Database NoWarnings Option

The system procedure sp\_RestoreDatabase now recognizes the option "[NoWarnings](master_backup_and_restore_options.htm)". This option turns off the logging of messages to the error log when tables are automatically created during an online restore operation.  Without this option, informational entries (5168, 7041, and system code 2) are logged when a restore operation creates a table.

FIPS-Enabled Server AES encryption Enhancements

|  |  |
| --- | --- |
| · | Improved error codes when old clients connect to FIPS-enabled servers. |

|  |  |
| --- | --- |
| · | [Adsbackup](master_adsbackup_utility.htm) utility updated to support FIPS and SSL settings and be able to use connection string options. |

|  |  |
| --- | --- |
| · | Client updates to support FIPS and SSL settings. |

|  |  |
| --- | --- |
| · | Simplified specification of SSL certificate where no path is necessary if certificate is in same folder as ADS. See [TLS Key File](master_tls_key_file.htm). |

 

SQL Command Line Utility

A new SQL command line utility is included in the Advantage Database Server, ACE SDK, and Advantage Data Architect installation. The command line utility supports running SQL query or script either interactively or from script files. See [SQL Command Line Utility](master_sql_command_line_utility_overview.htm).

64-bit Delphi Support

Advantage now supports Delphi's 64-bit cross-compiler. This means that Delphi can now be used to build and debug 64-bit binaries. Moreover, this also allows AEPs and Triggers written in Delphi to be used with 64-bit versions of Advantage Database Server.

Delphi XE2 Support

Added support for Delphi XE2, including support for the Windows 64-bit cross-compiler.

Locate Enhancements

Updated the TAdsQuery [Locate](ade_adslocatebehavior.htm) method to give precedence to the index implicitly set by an ORDER BY clause if one exists.

Delay Load ACE in Delphi

Updated the Advantage Delphi Components to use [delayed loading](ade_delay_loading_ace.htm) of the Advantage Client Engine. This means that an Advantage-enabled application can load and run without loading any Advantage DLLs until it first uses them. This provides the opportunity to run initialization code before loading the Advantage DLLs or to run in certain scenarios (such as non-Advantage functionality) without ever loading or needing the DLLs.

New TAdsConnection Options

|  |  |
| --- | --- |
| · | The TAdsConnection component now supports an [ExtraConnectString](ade_extraconnectstring_tadscon.htm) property which, when set, will be appended to the end of the automatically-generated Connection String and passed to AdsConnect101. This allows the user to specify settings like the DateFormat, Decimals, and Epoch on a per-connection basis. This can reduce the need to rely on global options set via the AdsSettings component. |

|  |  |
| --- | --- |
| · | New [DateFormat](ade_dateformat_tadsconnection.htm) option sets the date format for a specific connection. |

VO SQL Parameters

Added support to use [parameters](vo_axsql_parameters.htm) with AdsSQLServer objects in VO. Allows specifying parameters in initial query execution as well as changing parameters and refreshing an open AdsSQLServer object.

Python/Django Support

Added the Advantage [Python Driver](web_python_driver.htm) to provide database access from the Python environment to Advantage Database Server. In addition, added the Advantage Django Backend, which is a Python module designed to provide access from the Django environment to Advantage Database Server.

Ruby Driver

Added [Support for Ruby](web_advantage_ruby_api_support.htm). There are two different Ruby APIs supported by Advantage. First is the Advantage Ruby API. This API provides a Ruby wrapping over the interface exposed by the ACE API. This package allows Ruby code to interface with Advantage. Secondly, there is support for ActiveRecord, an object-relational mapper popularized by being part of the Ruby on Rails web development framework. This package uses (and has a dependency) on the Advantage Ruby API.

PHP PDO Driver

Added the [Advantage PDO](php_advantage_pdo_driver.htm) (PHP Data Objects) Driver to provide another option for database access from PHP to Advantage Database Server.

64-bit Lazarus Support

Improved TDataSet descendant support for [Lazarus](ade_overview_of_lazarus_support.htm) to be able to build 64-bit binaries for Linux and Windows.  Added support for Lazarus 0.9.30.

SQL Scripts over 32K (Triggers and Views) in Advantage Data Architect

Advantage Data Architect now handles SQL scripts over 32K in length for views, triggers, stored procedures, and user defined functions.

Replication Queue Record Data Display

Added the ability to display the record data for a replication queue entry. See [sp\_GetReplicationEntryDetails](master_sp_getreplicationentrydetails.htm).

Performance Improvements

|  |  |
| --- | --- |
| · | Improved performance of expression parsing, which will help with table and index opens, SQL parsing, filtering, etc. This can have a significant effect on some platforms such as Windows 2008 R2 or when the server is under a large concurrent load. |

|  |  |
| --- | --- |
| · | Improved performance of rollbacks to savepoints. |

|  |  |
| --- | --- |
| · | Optimized the function used to sort keys when building indexes. |

|  |  |
| --- | --- |
| · | Improved pack table performance. |

|  |  |
| --- | --- |
| · | Improved the efficiency of server-side initialization code required for many types of client requests. |

Improved .NET template projects for AEPs and Triggers

Updated the Visual Studio Advantage Extended Procedure (AEP) and Trigger template projects for .NET to include code to dispose of IDbCommand objects prior to exiting the external function.

Improved Error Messages

Updated many error messages to include the column name that is involved in the particular error.

Replication Queue Display Order

The replication queue is now displayed in logical order in Advantage Data Architect.

Ability to Replicate to Older Servers

Added the ability for a newer Advantage server to [replicate to an older server](master_replicating_to_older_servers.htm). For example, it is possible to replicate from a v11.x server to v9.x or v10.x.