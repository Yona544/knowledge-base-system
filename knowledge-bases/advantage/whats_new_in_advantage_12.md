What's New In Advantage 12




Advantage Database Server 12  

What's New In Advantage 12

                                                                                                                                         Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What's New In Advantage 12                                                                                                                                           Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - What's New In Advantage 12 Advantage Database Server Whats\_New\_In\_Advantage\_12 Advantage Database Server > Introduction > What's New In Advantage 12 / Dear Support Staff, |  |
| What's New In Advantage 12                                                                                                                                           Advantage Database Server |  |  |  |  |

Security Warning!

Please note that for the Advantage Database Server (ADS), the password for the default ADS user, ADSSYS, is blank. This is a security risk since a malicious user can login to the database using the ADSSYS login and access or modify the data. This can result in data privacy violation and data loss situations. Hence, it is strongly recommended that during creation of every data dictionary, the password of the default ADS user, ADSSYS, be changed to a password that is secure. 

 

New Client

 

Advantage Delphi OData Client

Added a [new Delphi based client](advantage_delphi_odata_client.htm) that consumes OData and allows developers to interact with the data using familiar TDataSet data store. Applications developed using this can be deployed across platforms, using Embarcadero's cross-platform technology.

 

Updated Support for Clients

 

Delphi XE8 Support

The Advantage Delphi Components now include support for Delphi XE8.

Visual Studio 2013 Support

The Advantage .NET Data Provider now includes support for Visual Studio 2013

PHP 5.5 and PHP 5.6 Support

The Advantage PHP Extension is now available for PHP 5.5 and PHP 5.6

New Features and Enhancements

GROUP\_CONCAT

Added support for the [GROUP\_CONCAT()](master_supported_aggregate_column_functions.htm) aggregate function. It is used to combine string values in a group into a single string value. This provides a nice mechanism for producing a result set where each row contains all values for a single group in one string.

 

Multi-row INSERT Syntax

With support for multi-row [INSERT](master_insert.htm) statements in SQL, it is possible to write a single SQL INSERT statement that inserts multiple rows into a table.

 

Improved Scalar Functionality

Additional scalar functions are now supported in both SQL and navigational environments. This can enable better [optimization for SQL statements](master_indexes_with_expressions.htm) in some situations. Additional scalar functions now supported in SQL statements include [ALLTRIM](master_alltrim.htm), [AT](master_at.htm), [CTOD](master_ctod.htm), [CTOT](master_ctot.htm), [CTOTS](master_ctots.htm), [DATE](master_date.htm), [DELETED](master_deleted.htm), [DTOC](master_dtoc.htm), [DTOS](master_dtos.htm), [RAT](master_rat.htm), [RECNO](master_recno.htm), [REVERSE](master_reverse.htm), [STOD](master_stod.htm), [STOTS](master_stots.htm), [STR](master_str.htm), [STRZERO](master_strzero.htm), [TIME](master_time.htm), [TSTOD](master_tstod.htm), [TTOC](master_ttoc.htm), and [VAL](master_val.htm). Additional scalar functions now supported in navigational usage (as index expressions) include [ASCII](master_ascii.htm), [CEILING](master_ceiling.htm), [COALESCE](master_coalesce.htm), [CREATETIMESTAMP](master_createtimestamp.htm), [DIFFERENCE](master_difference.htm), [FLOOR](master_floor.htm), [FRAC\_SECOND](master_frac_second.htm), [LENGTH](master_length.htm), [REPEAT](master_repeat.htm), [SIGN](master_sign.htm), and [SOUNDEX](master_soundex.htm).

For example, it is possible to refer to a specific record number directly within SQL now:  SELECT \* FROM table WHERE recno() = 123

Other new scalar functions include:

|  |  |
| --- | --- |
| · | [BASE64ENCODE](master_base64encode.htm) |

|  |  |
| --- | --- |
| · | [BASE64DECODE](master_base64decode.htm). |

|  |  |
| --- | --- |
| · | [LASTROWVERSION](master_lastrowversion.htm) |

Performance Improvements

|  |  |
| --- | --- |
| · | Sped up parsing of expressions.  This, among other things, improves building filters for SQL optimization. |

|  |  |
| --- | --- |
| · | Sped up expression evaluation for situations when optimized bitmap (AOF) filtering cannot be used. |

|  |  |
| --- | --- |
| · | Reduced memory consumption in the cache system. In particular, static SQL cursors involving memo files by about 33%. |

|  |  |
| --- | --- |
| · | Increased performance of [Online Reindex](master_online_table_maintenance.htm) and removed the transition during the final stage. |

|  |  |
| --- | --- |
| · | Improved the performance of queries involving extremely large intermediate sort files. |

Create Index Online

Added the capability to create indexes while a table is open by other users.  Prior to ADS v12 it was necessary to open a table exclusively (thus disallowing any other use of the table) when a new index is created.  See [Online Table Maintenance](master_online_table_maintenance.htm) for more information.

 

Archive File for Online Backup

Updated the online backup/restore functionality to be able to backup to and restore from a single archive file that can optionally be compressed. This makes it simpler to move or copy a backup image to other locations (just copy a single file). Search for the ArchiveFile option in [Backup and Restore Options](master_backup_and_restore_options.htm).

 

Improved Differential Online Backup

Updated the operation of [differential backups](master_differential_backups.htm). A differential backup is a backup that copies only records that have changed since the last backup. In previous versions of Advantage, it was required that you re-initialize the differential backup when certain operations occurred (packing of a table, altering a table, etc.). Beginning with v12, Advantage will detect if a differential backup for a given table requires re-initialization and will automatically perform it. In addition Advantage will now detect if indexes in a [free table differential backup](master_sp_backupfreetables.htm) have changed and automatically backup the changed indexes.

 

Memo Block Size Configuration

More options exist for configuring memo block sizes on tables:

|  |  |
| --- | --- |
| · | The maximum memo block size for ADT tables has been increased from 1024 bytes per block to 32768 bytes per block. |

|  |  |
| --- | --- |
| · | The memo block size of an existing table can be changed through a pack operation ([sp\_PackTable](master_sp_packtable.htm), [sp\_PackTableOnline](master_sp_packtableonline.htm), [AdsPackTable120](ace_adspacktable.htm)). |

|  |  |
| --- | --- |
| · | The memo block size of an existing table can be changed when altering the table ([ALTER TABLE](master_alter_table.htm), [AdsRestructureTable120](ace_adsrestructuretable.htm)). |

|  |  |
| --- | --- |
| · | When creating a new table with SQL, the memo block size can be specified ([CREATE TABLE](master_create_table.htm)). |

|  |  |
| --- | --- |
| · | When modifying table properties in Advantage Data Architect, the memo block size for both data dictionary and free tables can be modified. Note that when the OK button is pressed on the property dialog, a table restructure operation will be triggered if the memo block size property was changed. |

 

Improved Memo Recycling

The ADT table type now has an improved recycling scheme for memo files.  This scheme will reduce memo file bloat by using a binning algorithm for small memos.

 

AdsFileToBinaryW and AdsBinaryToFileW

AdsFileToBinaryW and AdsBinaryToFileW allow Unicode filenames to be used as the source and destination for these APIs.  See [AdsFileToBinary](ace_adsfiletobinary.htm) and [AdsBinaryToFile](ace_adsbinarytofile.htm) for more information.

 

Memo and Blob Compression

The ADT table type now has the option to store memo (ANSI and Unicode) and blob data in compressed format to reduce memo file size. See [ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm) for more information.

 

Option to Disable Compression of Dump Files

If Advantage Database Server triggers the creation of a [crash dump file](master_adsdump_files.htm), it compresses the dump file. The compression step can be relatively slow compared to the creation of the dump file in the first place. The new [COMPRESS\_DUMP\_FILES](master_compress_dump_files.htm) configuration option provides the capability to disable the compression step.

 

Improved Online ALTER TABLE

Improved the behavior of Online ALTER TABLE to not require all users to close the table for for most types of table changes.  Some table structure changes do still require all users to close the table for the online ALTER to finish.  Also changed online ALTER to set default field values and NOT NULL flags for added fields before populating the new table with the existing data.  The result is that you can now add a field and initialize it with a default field value during an online ALTER.  This applies to dictionary bound as well as free tables.  See [Online Table Maintenance](master_online_table_maintenance.htm) for more information.  As a result of these new features, a checkbox has been added to the table designer in Advantage Data Architect to cause changes to a table to be performed online.

 

Maximum Failed Login Attempts for All Remote Server Connections

Previously Advantage only enforced the Maximum Failed Login Attempts for Internet Connections.  A new option has been added to the data dictionary to have Advantage enforce the Maximum Failed Login Attempts limit for all remote server connections.  See [Maximum Failed Login Attempts](master_maximum_failed_login_attempts.htm) for more information.

 

ETag Support for the Advantage Web Platform

The OData server supports [optimistic concurrency](master_optimistic_concurrency.htm) through Entity Tags (ETag) values. If you set the TABLE\_CONCURRENCY\_ENABLED property for a table (e.g., in Advantage Data Architect in the table properties), then OData clients that support ETags such as the Advantage OData Client for Delphi and the Windows Communication Foundation (WCF) client will use ETag values in If-Match headers to for optimistic concurrency control.

 

GUID and 64-bit Integer Field Types

Advantage server and clients now support GUID and Long Integer (64-bit) data types in all table formats. The 64-bit integer type can be used to store integer values between -9,223,372,036,854,775,807 and 9,223,372,036,854,775,807 with no loss of precision. The GUID (Global Unique Identifier) field type is a 16-byte data structure. A new scalar function NewID() is available in the expression engine and SQL engine to generate new GUID. See [ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm) and [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm) for more information.

 

Database Triggers

Support for [database triggers](master_database_triggers.htm) has been added to provide the ability to fire triggers in response to certain types of events.

 

\_\_rootdd System Alias

A system alias called \_\_rootdd has been added which resolves to the path of the [root dictionary](master_root_dictionary.htm) configured for the server.  Connections to the root dictionary can then be made to \\server\\_\_rootdd.

 

Added Max Login Attempt Enforcement for all Remote Connections

Previously the [max login attempts](master_maximum_failed_login_attempts.htm) enforcement only applied to internet connections.  A new database property (ADS\_DD\_ENFORCE\_MAX\_FAILED\_LOGINS) has been added which when enabled will enforce the max login attempts for all remote server connections (including internet connections).  The property may be set on the Security tab of the Database Properties dialog in Advantage Data Architect or by calling [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm)/[sp\_ModifyDatabaseProperty](master_sp_modifydatabase.htm).

 

Added $select Web Platform Option

The $select URI option can be used to limit which columns of a collection are returned from a request.  See [collections](web_collections.htm) for more information.