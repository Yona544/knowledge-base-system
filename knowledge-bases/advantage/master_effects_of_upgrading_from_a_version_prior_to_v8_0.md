Effects of Upgrading from a Version Prior to v8.0




Advantage Database Server 12  

Effects of Upgrading from a Version Prior to v8.0

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Effects of Upgrading from a Version Prior to v8.0  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Effects of Upgrading from a Version Prior to v8.0 Advantage Database Server master\_Effects\_of\_upgrading\_from\_a\_version\_prior\_to\_v8\_0 Advantage Database Server > Introduction > Effects of Upgrading from a Version Prior to v8.0 / Dear Support Staff, |  |
| Effects of Upgrading from a Version Prior to v8.0  Advantage Database Server |  |  |  |  |

In addition to the [Effects of Upgrading to Version 9.0](master_effects_of_upgrading_to_9_0.htm) and the [Effects of Upgrading to Version 8.1](master_effects_of_upgrading_to_advantage_8_1.htm), the following Advantage functionality changes may affect your applications if you upgrade from a version of Advantage prior to version 8.0.

Effects of Upgrading

General

Attempts to open tables in nonexistent directories will now return 7041 errors. Previous versions would return 7008 errors for this condition.

More specific error codes (7123, 7124) for table corruption may be returned in place of the generic 7016 error code.

Changed behavior of AFTER triggers. AFTER triggers that modify the base table they are defined upon will no longer cause a recursive call to the trigger.

Reduced the timeout period for connections that are lost due to communications failures or server failures. In previous versions, the timeout period could range from 1 to 2 or more minutes for a lost connection to the Advantage Database Server. It now will be closer to 15 seconds. If, for some reason, network speeds are such that it takes longer than 15 seconds for a round trip between client and server, you can increase the MAX\_TIMEOUTS value in the ADS.INI file. Refer to the "ads.ini File Support" topic in the Advantage help file for more information.

The Advantage Client Engine will no longer return errors when an application closes tables, cursors, indexes, or statement handles on a connection where the underlying communications channel to the Advantage Database Server has been lost. This improves the ability of an application to clean up resources in a timely manner after a connection is lost. This is particularly useful for applications that connect to Advantage Database Server running on a cluster. If a cluster node goes down, the application can close resources (tables, cursors, etc.) and reconnect quickly.

Index orders of dictionary tables were changed to be consistent with documentation. In general, this change may affect the order of index orders returned in an array fashion, thus affecting code that references index orders by number. Primarily, this affects the AdsGetAllIndexes ACE API. Moving forward, all index orders will be returned in the order the orders were created.

The behavior of using parameters in SQL scripts has changed. In previous releases, all SQL statements in a script were required to have an identical number of parameters with identical types, and the number of parameters supplied for the execution had to match the number of parameters in each SQL statement in the script. For example, given the script: UPDATE customer SET name = ? WHERE id = ?; UPDATE customer SET name = ? WHERE id = ?; Only two parameters could be supplied to execute the script. The two parameters would be applied to both statements. In Advantage v8.0 and greater, all parameters in the SQL script are independent of each other. The above sample SQL script will require four parameters to execute. Advantage v8.0 and greater also allows the following sample script that is not allowed in the previous version due to the different number of parameters in the two statements: UPDATE customer SET name = ? WHERE id = 1; SELECT \* FROM customer WHERE id = 1;

The behavior of SQL scripts has changed when the last statement in the script is a "SELECT ... " statement. In previous versions, no cursor is ever returned after executing an SQL script. In Advantage v8.0 and greater, a cursor is returned if the last statement in the script is a "SELECT ..." statement. The returned cursor must be closed before the statement handle can be used to execute another SQL query.

Outer references in subselect queries in INSERT statements are no longer allowed. For example, this SQL statement is no longer allowed in Advantage 8.0 and greater: INSERT INTO customers1 SELECT lastname, empid FROM customers2 WHERE customers1.empid = customers2.empid

The following are new SQL reserved keywords: CLOSE, CURSOR, DECLARE, ESCAPE, FETCH, FOR, FULL, OF, OPEN, RIGHT, SAVEPOINT. If your existing application has SQL statements that use any of these reserved keywords as column names or table names, they must be delimited with double quotes or square brackets in Advantage v8.0 and greater to avoid an error being returned.

In versions prior to 8.0, specifying "short" instead of "shorti" or "shortint" when creating a new table or restructuring an existing table would generate a "shortdate" field. In v8.0 and greater, "short" will be interpreted as a short integer. To eliminate any ambiguity, however, it is recommended you always use the complete field type name.

The AVG aggregate function in SQL now conforms to the SQL standard in regard to the data type, precision, and scale of the resulting column. In previous releases, the AVG aggregate function always resulted in a column with the DOUBLE data type. In Advantage v8.0 and greater, the resulting column will have the same data type, precision, and scale as the column or expression specified in the AVG aggregate. If your application uses the AVG aggregate on an integer expression and expects the result to be a DOUBLE, you will need to change the SQL statement to explicitly cast the expression into a DOUBLE, i.e. AVG( CAST( int\_column AS SQL\_DOUBLE )). If the integer expression is not cast into a DOUBLE, any fractional value from calculating the average will be truncated.

A bug was fixed where getting a record count on a table would sometimes affect the record position and the bof/eof flags. This bug has been fixed, but the fix may cause some changes to applications that depend on or expect record movement after the record count is retrieved.

The count of the number of rows modified by an SQL script may be different from previous versions. In version 8.0 and newer, the cumulative number of rows modified by DML statements will be returned.

The list of tables, columns, views, stored procedures and links that are returned from calling the AdsDDFindFirstObject API, the AdsFindFirstTable62 API, or any other functions that return a similar list may be different from previous releases. Specifically, if the data dictionary is configured to verify user's access permissions and the connection is made to the data dictionary not as the ADSSYS user, then the list of objects returned will only include objects that the user has some permissions to access. In ARC, this affects the list of tables, columns, views, stored procedures and links displayed in the database manager. In the Advantage TDataSet Descendant, the design time dropdown list of the TAdsTable.TableName property will only include the tables the user has access permissions to.

The Advantage Optimized Filter (AOF) engine no longer optimizes on ADI composite (multi-segment) indexes that are combined with the + (plus) operator. Version 7.0.0.X and earlier would incorrectly use composite ADI indexes that used the + operator for optimization. The + operator results in the entire expression being NULL if either operand is NULL (standard SQL processing). When creating composite ADI indexes, you should use the semicolon (;) operator. For example, instead of the index expression "lastname+firstname", you should use "lastname;firstname".

The constant ADS\_MAX\_KEY\_LENGTH that is found in various header files including ace.h, ace.pas, and ace32.bas has been increased from 256 to 4082. This may affect the size of structures, stack usage, etc. if you have used this constant in your application.

The error code returned from performing a data dictionary related operation may be different from previous versions. Specifically, in previous releases, the error code 5176 (AE\_ILLEGAL\_USER\_OPERATION) was returned when performing an operation that required connecting to the database as the ADSSYS user. Now, the same operation may return the error code 5054 (AE\_PERMISSION\_DENIED).

To support new permissions features in the data dictionary, the internal version of the data dictionary is now automatically upgraded when a new permission is granted or revoked. The new version of the data dictionary is not compatible with older servers. In other words, the newer version of the data dictionary cannot be used on pre 7.1 versions of ADS or ALS. However, older client applications should still work without problem with the newer version of the data dictionary if the application is run against version 7.1 or greater of Advantage. The exception in this situation is that the old client application cannot connect as the ADSSYS user.

Some properties in the data dictionary that used to be readable by any non-adssys user are now available only to users with additional permissions granted to them. An AE\_PERMISSION\_DENIED error is returned when the user does not have permissions to read those properties.

The '#' character, when used in SQL statements as the leading character of a table name, now denotes the usage of a temporary table in the context of the current connection. Existing applications that use the '#' character as the leading character of any table name in SQL statements may need to be modified to delimit the affected table name inside double quotes.

When using the data dictionary, the user group name "PUBLIC" is now reserved for future use. Attempts to create a new user group named "PUBLIC" will fail with a 5132 (AE\_INVALID\_OBJECT\_NAME) error code. Existing user groups in the data dictionary with this name will not be affected.

System table string fields are now case insensitive fields. System tables are tables like system.indexes, system.columns, etc.

Fail tables used when manipulating a dictionary must be located on the server when using a remote server connection. This affects record level, field level, and RI validation fail tables. When providing these table paths, you must now specify a path to the remote server, not a local path to the current workstation.

With the addition of new permissions (ALTER and DROP), the definition of ADS\_PERMISSION\_ALL has changed to include these new permission values.

TDataSet Descendant

The confusing error message "No parseable expressions in setting key fields" has been replaced with "An index must be active to perform this operation. Set the IndexName property." If your application is trapping this error string, its behavior will change if upgrading to version 8.0 or greater.

A bug was fixed in the CreateTable method. When connected to a data dictionary that has a default table creation path specified, the CreateTable method used to ignore this default path. The bug has been fixed, which means applications that use a dictionary that has a default path that is not the same as the dictionary path may need to be modified to expect this new behavior.

If only a table name is provided to TAdsDictionary.CreateRI as the fail table (no path) the table will now be created in the temp table directory configured in the data dictionary.

In versions prior to 8.0 if you put the dataset into the dsSetKey state, via a call to SetRangeStart, SetRangeEnd, EditRangeEnd, EditRangeStart, etc. and then set a field that was not included in the index, no error was raised. This bug has been fixed. If you were accidentally setting a field that is not included in the index you may receive an error similar to: "Field 'X' is not indexed and cannot be modified"

A bug was fixed in the Locate method that could affect record position after a call to Locate. In versions prior to 8.0, if an index was active the Locate method still might use one of the other existing indexes on the table to perform the locate operation. When multi-field indexes are used this could sometimes result in a Locate that did not position to the first record that matched the search condition. Any changes this bug fix causes upon upgrade should be positive (meaning the record placement should be correct, where in the past it may have missed some records).

Added support for the ixPrimary TIndexDef option. This option will now be respected when creating new tables with indexes. This may affect some existing applications. The option will also be populated when a table is opened. The ixPrimary option is only supported on ADT tables inside a data dictionary.

Advantage .NET Data Provider

Changed the behavior of setting/clearing filters, ranges, and active indexes to fit better with the ADO.NET programming model. After setting or clearing a filter, range, or active index, the reader will now be positioned at BOF (beginning of file) so that a "while ( reader.Read() )" loop can be used to traverse the recordset.

PHP Driver

The minimum required version of PHP for version 8.0 and greater of the Advantage PHP extension is 4.3.10.