---
title: Devguide The Backup Result Table
slug: devguide_the_backup_result_table
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_backup_result_table.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ea52815d5e3aa5ca006ddca7d8089598f4448487
---

# Devguide The Backup Result Table

The Backup Result Table

     The Backup Result Table

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The Backup Result Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As mentioned earlier, a result set (cursor) is created during the backup process. If you perform the backup using the command-line utilities, this result set is written to disk following the backup. If no errors are encountered, this result set is empty.

When using the backup feature within the Advantage Data Architect, this table is displayed if one or more errors are encountered, and must be saved if you want to keep this data. If no errors are encountered, the table is automatically deleted.

A cursor to the in-memory result set is returned by the backup system stored procedures. This result set is empty if no errors are encountered; otherwise, it contains the errors. Like with the Advantage Data Architect, you must save any errors returned by the backup system stored procedures or they will be lost.

The structure of the backup result set table is listed in Table 9-2.

 

| Field Name | Type | Description |
| Severity | Integer | A value from zero (least severe) to 10 (most severe) |
| Error Code | Integer | The Advantage error code associated with the error |
| Error Message | Memo | The text associated with the error code |
| Table Name | Memo | The name of the table associated with the error |
| Additional Info | Memo | Additional information, if available |
| Source File | Character(32) | An internal ADS source filename that can be used by a member of the Advantage technical support team to resolve backup problems |
| Source Line | Integer | The associated line number of the source code listed in the Source File field |

Table 9-2: The Fields of the Backup Result Table

Because AdsBackup.exe (or AdsBackup.jar for Java) is designed to run as an unattended batch operation, it always produces a backup result set that is written to disk. If no errors are encountered, this result set is empty. It is your responsibility to inspect this result set in order to learn if your backup was completely successful or not.

The default filename of the backup result set created by AdsBackup.exe is the word BACKUP followed by a string that contains a date/time stamp. For example, a backup completed at 3:01 p.m. and 24 seconds on January 1, 2007 will have the following name:

BACKUP\_20070101150124.ADT

The 150124 part of this filename is the time (15th hour since midnight and one minute and 24 seconds). A backup created at 3:15 a.m. and 55 seconds on January 1, 2007 will have this name:

BACKUP\_20070101031555.ADT

By default, this file is always created in the source directory. For a backup, that directory is the one in which the original data dictionary resides.

AdsBackup.exe provides you two command-line options for controlling the name and path of the backup result table. Use n to provide an alternative path for the backup result table. Alternatively, use o to provide both a filename and a path.

   
NOTE: Even if you never find errors in the backup result set, it is essential that you occasionally test restoration of your data. When testing a restore, you might want to copy the backup files to another machine and restore them there, or you may want to simply restore them to a directory that is not used by your live data. Testing your restore periodically reduces the chance that you will have a very unpleasant surprise when you actually need to restore a compromised database.
