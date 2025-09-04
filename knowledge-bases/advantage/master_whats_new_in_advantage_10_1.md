What's New in Advantage 10.1




Advantage Database Server 12  

What's New in Advantage 10.1

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| What's New in Advantage 10.1  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - What's New in Advantage 10.1 Advantage Database Server master\_Whats\_New\_in\_Advantage\_10.1 Advantage Database Server > Introduction > What's New in Advantage 10.1 / Dear Support Staff, |  |
| What's New in Advantage 10.1  Advantage Database Server |  |  |  |  |

Strong Encryption and FIPS Compliance

Advantage Database Server now supports [strong cryptographic functionality](master_encryption.htm) that can be used in Federal Information Processing Standard ([FIPS](master_fips.htm)) 140-2 compliant products. The cryptographic functionality in versions prior to 10.1 is based on RC4, which is not a FIPS-compliant encryption algorithm. Beginning with v10.1, new encryption and communications support are available through libraries from The OpenSSL project.

The new cryptographic functionality is not available by default in Advantage products. It must be purchased separately with the FIPS Encryption Security Option Add-on. Please contact your Advantage sales representative or visit <http://www.sybase.com/products/databasemanagement/advantagedatabaseserver/encryption> for additional licensing information.

Note that enabling and using FIPS-compliant cryptography in Advantage Database Server does not make an application conform to FIPS 140-2; all parts of the application must be examined and possibly updated for FIPS-compliance.

The following summarizes the new cryptographic functionality:

|  |  |
| --- | --- |
| · | Added support for Transport Layer Security (TLS) v1.0 [communications](master_communications_encryption.htm). TLS operates over TCP/IP and uses RSA for the key exchange, 128-bit or 256-bit Advanced Encryption Standard (AES) for encryption and SHA-1 (Secure Hash Algorithm) for message authentication. These cipher suites are referred to as AES128-SHA and AES256-SHA. |

|  |  |
| --- | --- |
| · | In addition, the cipher suite RC4-MD5, which uses RSA for the key exchange, RC4 for encryption and MD5 for message authentication, is also available. This cipher suite is not FIPS-compliant. |

|  |  |
| --- | --- |
| · | Added support for data (table) encryption using 128-bit and 256-bit AES. |

|  |  |
| --- | --- |
| · | Enhanced data encryption using 64-bit message numbers for each piece of encrypted data (e.g., record, memo, index page, etc.) to ensure unique initialization vectors (and, therefore, unique cipher streams) across a database. Each time a record is updated, a new message number is generated for it. |

|  |  |
| --- | --- |
| · | Improved key strength by salting and hashing keys. This makes attacks via password dictionaries (rainbow tables) infeasible and makes brute force attacks much more expensive. |

|  |  |
| --- | --- |
| · | Added the capability to encrypt the data dictionary files (.add, .am, .ai) with an externally provided password. |

|  |  |
| --- | --- |
| · | Added the capability to run Advantage Database Server and the Advantage client in FIPS mode. This ensures that it is not possible to use any cryptographic functionality that is not FIPS approved. For example, if Advantage Database Server is running in FIPS mode, it is not possible to open data dictionaries that support RC4 or tables encrypted with RC4. |

|  |  |
| --- | --- |
| · | Added system procedures sp\_DecryptTable and sp\_EncryptTable that can be used to change table structures to support AES encryption. |

|  |  |
| --- | --- |
| · | Added system procedure sp\_ChangeDDEncryptionType to convert data dictionaries to support AES encryption. |

|  |  |
| --- | --- |
| · | Added system procedure sp\_GetTableEncryptionType to retrieve the type of encryption used on a table. |

|  |  |
| --- | --- |
| · | Added system procedure sp\_GetSecurityInfo to retrieve information such as a connection's default encryption type, the communication type, the communication encryption type, and dictionary encryption state. |

 

 

Delphi XE and Lazarus Support

The Advantage Delphi Components now include support for Delphi XE.

Modifications were also made to support Lazarus (cross-platform class libraries for Free Pascal that emulate Delphi). The Windows installer must still be used to get the Lazarus packages and source code, which can then be used on the Windows platform, or copied to a Linux image (Macintosh is not supported, as our components still use the Advantage Client Engine, which only supports Windows and Linux). For details, see [Getting Started with Lazarus](ade_getting_started_with_tdataset_for_lazarus.htm).

 

 

Unicode Full Text Search Support

The Advantage Database Server now supports Full Text Search (FTS) on Unicode data.

|  |  |
| --- | --- |
| · | The Contains() scalar function can now be used with Unicode data as input in the filter expressions, Advantage Optimized Filter (AOF) expressions and SQL engine expressions. |

|  |  |
| --- | --- |
| · | The Score() and ScoreDistinct() scalar functions in SQL engine now supports Unicode data as input. |

|  |  |
| --- | --- |
| · | FTS indexes may be built on NChar, NVarChar, and NMemo Field type to speed up the searches using the Contains() scalar in AOF. The indexes will also improve performance of evaluating the Contains(), Score() and ScoreDistinct() expressions in the SQL engine. |

|  |  |
| --- | --- |
| · | FTS with Unicode data is always case and diacritical insensitive. |

 

 

ARC Copy/Paste Support for Rows

Advantage Data Architect now supports Copy and Pasting records into and out of the Table Browser and the SQL Utility. These records can be pasted to another grid or SQL Utility, into Microsoft Word, Excel, and also directly into HTML email.

Support for BLOB fields is included, copy and pasting from tables with different fields can also be accomplished via the Field Mapping Utility. To access the copy and pasting functionality a new context menu button has been added. See [Field Mapping Utility](arc_field_mapping_utility.htm) and [Table Browser](arc_table_browser.htm) for more information.

 

Error Information in Replication Queue

The replication queue has been updated in v10.10.0.6 to contain some of the error information for failed updates in order to simplify the process of determining why replication failed. See [Advantage Error Log and Replication](master_advantage_error_log_and_replication.htm) for more information

Bug Fixes

Advantage 10.1 is a "roll-up" release including a variety of bug fixes:

10.10.0.0 - Advantage Client Engine (ACE)

This Service Update of the Advantage Client Engine (ACE) addresses the following issues:

Fixed a bug that caused 4004 errors to be returned when an index expression uses one of the PAD\* functions.

Fixed a problem where AdsGetLastError would return AE\_FILE\_NOT\_ON\_SERVER after a failed AdsCopyTable operation (instead of returning the actual error code).

Fixed a bug where it was possible to lose changes to a record made by a trigger when a client application made multiple updates with multiple record writes to the same record.

Fixed an issue where creating a new database would overwrite an existing database.

Fixed a bug that caused no error to be returned (or the wrong error) when NTX or CDX tables were used with VFP collations.  The bug occurred only when using data dictionary bound tables. A 5025 error will now be returned in this situation.

Fixed a bug that caused table corruption when an encrypted table was restructured, and the restructure failed due to a constraint violation.

10.10.0.0 - Advantage Data Architect (ARC)

This Service Update of the Advantage Data Architect (ARC) addresses the following issues:

Fixed an issue where ARC would generate a crash report for an ERangeCheckError after it detected a collation mismatch.

Fixed an issue in the ARC table designer where you could not drag fields up if the form was so small that only 3 or 4 fields were visible.

Fixed an ARC issue that would prevent users from browsing to select a table to open if that table was already opened by the Advantage server.

Fixed an issue where ARC would not save custom key assignments in the SQL Editor.

Fixed an issue in ARC where the scope functionality on the data grid didn't work with partial keys.

Fixed an issue where the ARC line numbers printed in the Sql Utility only contained one character.

Fixed an issue where the ARC query utility could not load scripts explicitly saved as ansi (as opposed to the default unicode encoding) if those scripts contained characters with values > 127.

Fixed an issue where ARC would not generate a valid CREATE INDEX statement for FTS indexes.

Fixed an issue where ARC would not correctly restore the main form's dimensions after being closed with the window maximized.

Fixed an issue where NTX or CDX tables opened in ARC on a connection set up to use OEM collation were not correctly opening with the OEM character type.

10.10.0.0 - Advantage Database Server

This Service Update of the Advantage Database Server addresses the following issues:

Fixed an issue that prevented adsstamp from stamping the OEM language into a Linux server on some 64-bit distributions.

Fixed a bug in the configuration utility (ads\_cfg.exe) that caused server operation counts over 2,147,483,648 to display as negative values.

Changed the DBF header date to be compatible with 3rd party utilities.

Fixed an issue where the server could fire incorrect trigger types if the client had the SHOW DELETED setting on, deleted records existed, and updates were being performed on deleted records.

Fixed an issue where indexes built prior to 9.10.0.21 or 10.0.0.3 but used with aforementioned versions or newer caused 4004 errors.

Fixed a bug that caused the server to crash when an SQL statement was executed twice.

Fixed a bug that could cause a query to be sorted in the incorrect order if there were Unicode character columns in the ORDER BY clause, and there was an existing index matching the ORDER BY clause but with a different Unicode collation.

Fixed a bug where the ROWID returned from the same table has a different prefix depending on the case of the table name specified in the SQL statement.

Fixed a bug in the server that could result in query elements being leaked on the server by calls to sp\_WaitForEvent and sp\_WaitForAnyEvent. This could result in access violations and 9003 errors when used with .NET clients.

Fixed an issue where NMemo fields in \_\_new and \_\_old tables would only contain the first character of the Unicode string.

Fixed an issue where triggers on tables with one or more NVarChar fields would produce a 5073 error when updated.

Fixed a bug that would cause an AIS connection to hang when the client and server switched to SMC communication after doing server discovery using TCP/IP.

Fixed a bug that caused the YEAR AOF function to be incorrectly optimized when not testing for equality.

Fixed a bug that caused an incorrect optimization to be performed when evaluating filters (such as in SQL WHERE clauses). These filters were incorrect when they were of the form "FieldA < FieldB and FieldA > constant".  If an index existed on FieldA, it was possible for the index to incorrectly be used to optimize the full expression. This could result in incorrect result sets.

Fixed a bug that caused a 5133 error to be returned when creating stored procedures using a Unicode string, such as when creating a stored procedure in ARC.

Fixed a bug that could cause a trigger script to fail if the last statement executed in the script was a SELECT statement.

Fixed a bug in the query engine that caused comparison involving NULL values to fail when the column is a Unicode column in a CDX or NTX table.

Fixed a bug that caused 2119 or 2159 errors to be returned when a simple CASE expression uses a subquery as the input value.

Fixed a 7041 error when dropping a temporary table after dropping an index from the table.

Fixed a bug in the SQL query engine that caused poor query performance when a view or subquery was used as part of a multi-table join.

Fixed a bug that caused poor SQL query performance when the join condition was only partially optimized.

Fixed a bug where potential Unicode parameters in the SQL statement could cause the server to crash, or cause a variety of other errors.

Fixed an issue where an INSERT statement with a SELECT DISTINCT subquery that used a date literal would lead to a server crash or a 2203 (ERR\_FILE\_READ\_ERROR) error.

Fixed a bug that prevented cartesian joins in SQL from being canceled.

Fixed a bug that caused SQL queries to fail when no precision value was specified for the resultant data type when using the CAST() or CONVERT() scalars.

Fixed a bug with the ROWNUM function in SQL when used as part of an INSERT INTO SELECT FROM statement.

Fixed a bug that caused an unexpected failure when using EXECUTE PROCEDURE as a table expression in a SELECT statement. The failure occurred after an exception was raised in the stored procedure and caught. However, subsequent execution of the same SELECT statement would continue to fail even when no exception was raised in the stored procedure.

Fixed a bug that caused a 2136 error when using ARC to create a User Defined Function that has a Double type as an input parameter or return value.

Fixed a bug where the error 5005 could be returned when executing an SQL query using AdsExecuteSQLW, such as when executing a query in the ARC SQL window. The error was returned when the query being executed used a UDF, and there are string literals containing non-ASCII character in the UDF.

Fixed a bug that caused incorrect UDF description being stored in the data dictionary.

10.10.0.0 - Advantage .NET Data Provider

This Service Update of the Advantage .NET Data Provider addresses the following issues:

Fixed a bug where the message "This files is in use." was displayed when using the Open file dialog in the Connection String builder of the AdsDataAdapter Configuration wizard for creating a data dictionary connection.

Fixed a 2159 error when casting a numeric constant with LINQ to Entities.

10.10.0.0 - Advantage ODBC Driver

This Service Update of the Advantage ODBC Driver addresses the following issues:

Fixed an issue where the 64 bit ODBC management utility would look for 32 bit DLLs.

Fixed an issue where consuming an ODBC DSN from Excel or other applications would raise the exception "There was an error reading DSN information from the registry", instead of correctly prompting for user credentials for the DSN.

SQLFreeHandle and SQLFreeStmt with SQL\_DROP were changed to not access the user buffer set with SQLSetStmtAttr and the attribute SQL\_ATTR\_ROWS\_FETCHED\_PTR.

10.10.0.0 - Advantage OLE DB Provider

This Service Update of the Advantage OLE DB Provider addresses the following issues:

Fixed a bug that prevented OLE DB from returning foreign keys on database tables.

10.10.0.0 - Advantage TDataSet Switch Utility

This Service Update of the Advantage TDataSet Switch Utility addresses the following issues:

Fixed an issue where the TDataSet Switcher would overwrite previously backed-up files when doing a switch (with backup enabled) immediately following the installation of a new TDataSet version.