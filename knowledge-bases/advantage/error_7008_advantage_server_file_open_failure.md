7008 Advantage server file open failure




Advantage Database Server 12  

7008 Advantage server file open failure

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7008 Advantage server file open failure  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7008 Advantage server file open failure Advantage Error Guide error\_7008\_advantage\_server\_file\_open\_failure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7008 Advantage server file open failure  Advantage Error Guide |  |  |  |  |

Problem 1: The specified table, memo file, or index file was unable to be opened.

Solution 1: Verify the following:

|  |  |
| --- | --- |
| · | The file exists and the user has sufficient access rights to open the file. (The location and name of the file that received the 7008 error can be found in the ADS\_ERR.ADT or ADS\_ERR.DBF file.) |

|  |  |
| --- | --- |
| · | The file is not already open exclusively by another Advantage user. |

|  |  |
| --- | --- |
| · | When opening a table, index, or memo file, verify a non-Advantage application does not already have the file open. If this scenario exists, a file open error will be logged in the Advantage Database Server error log, ADS\_ERR.ADT or ADS\_ERR.DBF. If an error sequence in consecutive records in the error log exists with error codes 32 and 7008 (for the Advantage Database Server for Windows), this indicates that a non-Advantage application already has the file open, and the Advantage application is attempting to open the file using Advantage Proprietary Locking or in an Exclusive mode. Note that the other application that has the file open could also be backup software or a report writer. If opening a DBF table in a writeable mode, and that DBF is to be shared with a non-Advantage database application, make sure to open the table using Advantage Compatible Locking mode. |

|  |  |
| --- | --- |
| · | When creating a table, index, or memo file, verify that it already exists and another application does not have it opened. |

|  |  |
| --- | --- |
| · | If re-indexing or packing a table using Advantage Data Architect, verify the index, table or memo file is not opened by another application. |

|  |  |
| --- | --- |
| · | If attempting to open a table via the Advantage Local Server, make sure it is not already opened by another connection via the Advantage Database Server. |

|  |  |
| --- | --- |
| · | If attempting to open a table previously referenced by an SQL query, verify that the handle to the query (the cursor handle) was explicitly closed by calling AdsCloseSQLStatement after the executing the query. If the cursor handle was not explicitly closed by calling AdsCloseSQLStatement, the underlying table(s) will remain open in a "cached open" state by the Advantage server to improve the performance of subsequent queries. However, this "cached open" state will cause subsequent attempts to open the underlying table(s) in an exclusive mode to fail with a 7008 error. |

Problem 2: This error can occur when the connection to the Advantage Data Dictionary was made using a local-drive-letter path and tables within the dictionary are not on the same drive. Advantage stores the file path of the table relative to the data dictionary file in the data dictionary. If the file path of the table cannot be converted to a relative path, this error is returned.

Solution 2: Open the Advantage Data Dictionary using UNC or through a network drive (the network drive will be converted to UNC). This allows the tables and indexes to be located on a different drive then the one the data dictionary is on. Note that the files must be accessible using a UNC path (i.e., the must be on a share).

Problem 3: This error can occur when making a connection or opening a table from inside a server-side module (such as an extended procedure or a trigger) on a Windows server and using a drive letter. Services cannot resolve a drive letter to a local path, which can lead to a 7008 error.

Solution 3: Use UNC (\\SERVERNAME\SHARE) when making connections or opening tables from inside a server-side module. Also use UNC for any TDataSet aliases that are used from inside a server-side module.

Problem 4: This error can occur if you have a trigger on the table you are trying to open, or if you have a trigger that uses the table you are trying to open.

Solution 4: Triggers often cache the statement they use to execute the trigger code. If this cached statement references the table you are trying to open exclusively, you can get a 7008 error. All users who have modified the table with the trigger need to close the table (the table the trigger is defined on) before you can gain exclusive access to ANY table modified inside the trigger.