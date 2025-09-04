7010 Problem with Advantage server file read




Advantage Database Server 12  

7010 Problem with Advantage server file read

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7010 Problem with Advantage server file read  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7010 Problem with Advantage server file read Advantage Error Guide error\_7010\_problem\_with\_advantage\_server\_file\_read Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7010 Problem with Advantage server file read  Advantage Error Guide |  |  |  |  |

Problem 1: The Advantage server was unable to read from the specified file.

Solution 1: Check the status of the network and repeat the command.

Problem 2: An Advantage application may receive 7010 errors if:

|  |  |
| --- | --- |
| · | DBF tables with FPT memo files are being used. |

|  |  |
| --- | --- |
| · | The FPT memo file was created with a memo block size of 32 or less. |

|  |  |
| --- | --- |
| · | The FPT memo file was created with a database driver that is not completely FoxPro-compatible, such as SuccessWare's SIXCDX RDD, CA-Clipper's DBFCDX RDD, Loadstone's COMIX RDD, Vista Software's Apollo CDX driver, or the Halcyon CDX driver. |

Advantage, FoxPro, and any other FoxPro-compatible driver will not be compatible with such an FPT memo file. The above named non-Advantage database drivers do not obey the FoxPro-defined standard with memo blocks of size 32 or less. A block size of 32 is often the default when creating FPT memo files with these non-Advantage database drivers, so it is likely you will run into this incompatibility if the FPT memo files were created by these non-Advantage database drivers.

Solution 2: To alleviate the problem with 7010 errors with DBF tables and FPT memo files created by non-FoxPro compatible database drivers:

|  |  |
| --- | --- |
| · | Create a new DBF and FPT using an Advantage database driver. |

|  |  |
| --- | --- |
| · | Copy all data from the old DBF and FPT to the new DBF and FPT using the non-Advantage database drivers. |

|  |  |
| --- | --- |
| · | Delete the old DBF and FPT and use the new DBF and FPT. The new DBF and FPT (that were created by the Advantage driver) should be fully functional with both Advantage and non-Advantage database drivers. |

Problem 3: 7010 errors may occur when reading an index if the index is corrupt.

Solution 3: If the 7010 error occurs when performing a database operation that uses an index, or if the Advantage error log (ADS\_ERR.ADT or ADS\_ERR.DBF) indicates the 7010 error occurred when reading an index file, re-building the index will eliminate the index corruption and should eliminate the 7010 error.