Bugs Fixed in 10.10.0.6




Advantage Database Server 12  

Bugs Fixed in 10.10.0.6

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bugs Fixed in 10.10.0.6  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Bugs Fixed in 10.10.0.6 Advantage Database Server master\_Bugs\_Fixed\_in\_10.10.0.6 Advantage Database Server > Introduction > What's New in Advantage 10.1 > Bugs Fixed in 10.10.0.6 / Dear Support Staff, |  |
| Bugs Fixed in 10.10.0.6  Advantage Database Server |  |  |  |  |

The following bugs were fixed in the 10.10.0.6 service update:

10.10.0.6 - Advantage Client Engine (ACE)

This Service Update of the Advantage Client Engine (ACE) addresses the following issues:

Fixed an issue where a Linux application using local server and Unicode data could get 1500 errors or cause a segmentation fault if the Unicode library (libaicu.so) and icudt40l.dat files were not found.

Fixed a bug that caused repeated execution of SQL statements using local server to be much slower than using pre-10.0 releases.

Changed the error message for a 5035 error, AE\_LOCK\_FAILED, to include the table name and record number.

Fixed a bug in the client that resulted in an access violation when attempting a Transport Layer Security (TLS) connection when the necessary OpenSSL libraries were not available.

Added support for the new FIPS, AES, and TLS connection options to the ADO.NET provider, the OLE DB provider, and the ODBC driver.

10.10.0.6 - Advantage Data Architect (ARC)

This Service Update of the Advantage Data Architect (ARC) addresses the following issues:

Fixed a bug that prevented Advantage Data Architect from using the ADSINI\_PATH environment variable to locate the ADS.INI file.

Fixed an issue where double and curdouble parameters could not be added to an existing UDF.

Modified ARC to allow sorting user defined functions inside a package.

Copy/Paste functionality was broken in the ARC SQL Utility, data grid has been updated to allow multi-row select which the copy/paste modules require.

Fixed a bug in Advantage Data Architect that caused the size of the new connection dialog to be too small.

10.10.0.6 - Advantage Database Server

This Service Update of the Advantage Database Server addresses the following issues:

Updated the server to not log the 7160 code on startup.  This was an information message logged if the server could not load the libraries required for strong encryption support.

Update the server to return a 7069 error when a pre v10.1 client connects to a data dictionary using AES encryption instead of the misleading 6423 error.

Improved the code that looks for the TLS (SSL) certificate for TLS communications. The server configuration parameter TLS\_KEY\_FILE and the client connection option TLSCertificate can specify the certificate files without path information if the file is located in the Advantage search path (e.g., in the folder containing the Advantage binaries).

Fixed an issue that would result in a 7060 (ERR\_INVALID\_PASSWORD) when decrypting a Dictionary-bound encrypted table when the dictionary's Table Encryption password was 20 bytes in length.

Fixed a bug that could cause server to crash when opening a DBF table with incorrect table header information.

Fixed a bug in the server that could result in an access violation in the server if some rare conditions were met and the sp\_mgKillUser or AdsMgKillUser APIs were used while a connection was in progress.

Fixed a bug in the server that could result in record locks being held indefinitely after a record with RowVersion or ModTime fields was inserted in a transaction.

Fixed a bug that caused incorrect SQL progress information being returned when "CREATE INDEX ..." statement is part of the SQL script. This bug may lead to an "Invalid floating point operation" error when the SQL script is very large.

Fixed a bug in the server that could result in a 9021 error when online backup was used on connections with AES encryption specified.  The error could occur on tables that were not encrypted.

Fixed a bug in the server that could result in possible index corruption and possible 7017 errors on tables encrypted with AES.

Fixed an issue where the server can crash if a corrupted index is automatically rebuilt after a crash.

Fixed a bug in the server that caused sp\_SetDDEncryptionType to produce an invalid .ai file when a Visual FoxPro collation was in use.

Update the online help to include a search box on the index tab.

Fix a bug in the server that could result in a crash when using online backup functionality on a data dictionary that is using 128-bit AES encryption.

Fixed a bug that could result in a corrupt free table when using AES encryption.  If a table is decrypted and then immediately encrypted again with a different password and without closing the table between the operations, the resulting table was encrypted with incorrect encryption information and could not be recovered.

Changed the install to propagate the LAN\_IP\_ADDRESS setting during an upgrade from 9.x to 10.10.x

Fixed a bug in the server that would result in an access violation when creating a data dictionary link when using AES encryption.

Fixed a bug in the server that resulted in possible ADM memo file bloat when using AES encryption.

Fix a bug in the server that could result in triggers causing 5073 errors if the encryption type of the table did not match the connection's encryption type.

Fixed a bug that caused the restructuring of VFP tables encrypted with AES to fail with a 5097 error when the ENCRYPT\_TABLE\_PASSWORD property was set on the dictionary.

Fixed a bug that can lead to partially optimized AOF when full optimization is possible. The problem occurs when a Unicode field is part of the filter expression and the Unicode field is not the first segment of a multi-segment index.

Updated the server to log error information for replication failures directly to the replication queue table to make it easier to find the reason for the failure. If the replication queue already exists, it will not be updated with the new error information until the queue table is deleted from the dictionary.

Fixed a bug in the Linux server that could result in users being timed out incorrectly. This could result in 7020 errors being logged and possibly 7209 errors being returned to the client.

Fixed a bug in the server that could result in unexpected 5041 errors and possibly a server crash when running triggers on many threads concurrently.

Fixed a bug in the server that could cause a fully cached VFP table encrypted with AES to produce a 9124 error.

Fixed a 9094 error when executing a stored procedure in a loop using UDP on a network that has packet loss issues.

Fixed a 9066 error caused by canceling an SQL statement that caused an auto-create of an index inside of a transaction.

Enhanced the query engine to not hold table open after executing "DROP INDEX ..." or "CREATE INDEX ..." statements.

Fixed a bug that caused CREATE TABLE SQL statement to fail when a Unicode column (NCHAR or NVARCHAR) was designated as the primary key for the table.

Fixed a bug that caused the SQL command EXECUTE IMMEDIATE to fail with 5211 error when there were NON-ASCII characters in the value expression that were to be executed.

Fixed an error that caused certain queries involving the negation of a comparison expression to be unoptimized.

Fixed a bug that could cause 2111, "Out of range", error being returned when the CAST() scalar is used to convert a value into SQL\_BINARY or SQL\_VARBINARY type without specifying the precision of the result.

Fixed a bug that can cause crash dump being generated when executing a SQL statement that has a comparison involving a column from a subquery and another subquery. The crash dump would be generated when the subquery in the comparison returns zero rows, however the query execution would still complete with correct result.

Fixed a bug that caused incorrect result to be returned when "SELECT COUNT(\*) FROM \_\_input WHERE SomeCondition" is executed inside a stored procedure.

Fixed an issue where setting FTS properties via sp\_ModifyDatabase fails with an older than 10.0 version of the client (ARC or ACE) and a 10.0 or newer server.

Fixed a bug that caused MEMO data type to be returned for a column that is derived from a string variable. In previous release the data type was VARCHARFOX.

Fixed a bug that could cause more or less than expected rows being inserted when executing an "INSERT INTO ... SELECT ..." type of query. The problem occurs when the SELECT is a complex subquery with join or subquery.

Fixed a bug that caused incorrect number of rows to be inserted when an SQL statement of this form is executed: INSERT INTO ... SELECT TOP x PERCENT ... FROM ...

Fixed a bug that caused 2111 (OUT OF RANGE) error or server crash when executing SQL statement that used CASE expression with both SQL\_LONGVARBINAR (Blob) data and SQL\_BINARY (Raw) data as possible result.

During a silent install the Advantage Database Server is now stopped without prompting.

Fixed a bug where 9.10 files could be left behind when upgrading to 10.x.

10.10.0.6 - Advantage JDBC Driver

This Service Update of the Advantage JDBC Driver addresses the following issues:

Added Advantage dialect (org.hibernate.dialect.ADSDialect) to support Hibernate.

10.10.0.6 - Advantage TDataSet Descendant

This Service Update of the Advantage TDataSet Descendant addresses the following issues:

Fixed an issue that caused a 5021 error when setting the IndexName property to an index contained in a non-structural index in Lazarus.

Fixed an incorrect SNotIndexField error in Lazarus when calling FindNearest.

10.10.0.6 - Advantage Visual Objects Driver

This Service Update of the Advantage Visual Objects Driver addresses the following issues:

Fixed an issue in the VO RDD where the header length of the table was incorrect.