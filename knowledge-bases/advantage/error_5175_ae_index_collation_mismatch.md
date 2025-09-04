5175 AE\_INDEX\_COLLATION\_MISMATCH




Advantage Database Server 12  

5175 AE\_INDEX\_COLLATION\_MISMATCH

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5175 AE\_INDEX\_COLLATION\_MISMATCH  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5175 AE\_INDEX\_COLLATION\_MISMATCH Advantage Error Guide error\_5175\_ae\_index\_collation\_mismatch Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5175 AE\_INDEX\_COLLATION\_MISMATCH  Advantage Error Guide |  |  |  |  |

Problem: Beginning with version 6.2, Advantage stores a collation sequence identifier in the header of Advantage proprietary index (.ADI) files when it creates a new index file. When opening the index again, it can use that identifier to determine whether the current collation sequence matches the one used to create the index. The 5175 error code is returned when Advantage detects a mismatch between the collation sequence used to create the index file and the current collation sequence.

The TAdsTable property IndexCollationMismatch and table open options available in the AdsOpenTable API allow applications to control what action Advantage takes when it encounters a collation mismatch when opening tables directly. If the application chooses to have Advantage rebuild the indexes automatically (icmReindex or ADS\_REINDEX\_ON\_COLLATION\_MISMATCH), it is still possible that this error will be returned if Advantage is not able to acquire the necessary locks to rebuild the index. Normally this would only happen when using Advantage Local Server when different clients are using different collation sequences (an undesirable situation).

Solution: Make sure no applications have the table open. Then open the table with Advantage Data Architect, which will detect the collation mismatch and provide the opportunity to rebuild the index file.

It is possible to build the automatic reindex functionality into your own application either by using the option to ignore the collation error (icmIgnore or ADS\_IGNORE\_COLLATION\_MISMATCH) and rebuild the indexes with a call to AdsReindex or to use the rebuild option (icmReindex or ADS\_REINDEX\_ON\_COLLATION\_MISMATCH) when opening the table. It is not possible to specify these options for tables opened through SQL statements.

Advantage will always attempt to reindex the data dictionary index (.AI) file if it detects a collation mismatch. If for some reason, it is unable to rebuild the index file, it will return the 5175 error. If this happens, you can simply delete the .AI file; Advantage rebuilds the .AI file if it does not find it when opening the associated Advantage Data Dictionary (.ADD) file.

To permanently rid your applications of 5175 errors, make sure all servers running the Advantage Database Server, and any client applications accessing the database via the Advantage Local Server, are using the identical ANSI collation sequence specified in the Advantage configuration. The steps specified in the [Avoiding ANSI Collation Mismatch Errors](master_avoiding_ansi_collation_mismatch_errors.htm) topic to avoid 5092 errors are the same steps that should be applied to avoid 5175 errors. Namely, the same ANSI language should be specifically selected from the list of available collation languages when installing the Advantage Database Server, and this same language should be specified for the ANSI\_CHAR\_SET keyword in the Advantage Local Server configuration file, adslocal.cfg, on all client workstations using the Advantage Local Server.