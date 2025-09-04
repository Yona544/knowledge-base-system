Creating a Backup Using System Stored Procedures




Advantage Database Server 12  

     Creating a Backup Using System Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Backup Using System Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating a Backup Using System Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Backup\_Using\_System\_Stored\_Procedures Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 9 - Backups > Creating a Backup Using System Stored Procedures / Dear Support Staff, |  |
| Creating a Backup Using System Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As you learned earlier in this chapter, if you want to permit a user (presumably only administrative users) to initiate backups from within one or more of your client applications, you will want to use one of the available Advantage system stored procedures for that purpose.

You use sp\_BackupDatabase to create a backup of a data dictionary, while you use sp\_BackFreeTables with free tables. There are corresponding stored procedures that you use to restore databases and free tables, respectively. These stored procedures are described later in this chapter.

The sp\_BackupDatabase stored procedure takes two parameters, which are both of the data type memo. The first parameter is the path to the directory in which you want the backup to be placed. This can be either a fully qualified drive path (for Windows) or a UNC (universal naming convention) path. If you use a drive path, the drive letter must be a local drive letter that the server recognizes, and it cannot be a mapped drive.

The second parameter contains a semicolon-separated list of options. These options are listed in Table 9-1.

 

|  |  |
| --- | --- |
| Option | Description |
| Include | Include one or more tables. When using Include, follow it with an equals sign followed by a comma-separated list of tables you want to include. |
| Exclude | Exclude one or more tables. When using Exclude, follow it with an equals sign followed by a comma-separated list of tables you want to exclude. |
| DontOverwrite | Use DontOverwrite to prevent backup from replacing an existing table during a restore operation. If you include DontOverwrite and a table being restored already exists at the restored destination, the result set will include a warning. |
| MetaOnly | Use MetaOnly if you want to make a backup of the data dictionary files without actually backing up any of the database's tables. |
| PrepareDiff | Use PrepareDiff to prepare a database for a differential backup. PrepareDiff needs to be executed only once, prior to initiating a differential backup. |
| Diff | Use Diff to initiate a differential backup. Before you create your first differential backup, you must first execute sp\_BackupDatabase (or sp\_BackupFreeTables) with the PrepareDiff option. Differential backups are only supported with ADT tables. |

Table 9-1: Options for Backup and Restore System Stored Procedures

For example, the following SQL statement demonstrates how you would have performed the same backup as demonstrated in the preceding section using sp\_BackupDatabase:

EXECUTE PROCEDURE sp\_BackupDatabase('c:\AdsBook\Backup', '')

If you wanted to create a differential backup of this same database, you would use the following statement to first prepare for a differential backup:

EXECUTE PROCEDURE sp\_BackupDatabase('c:\AdsBook\Backup',   
  'PrepareDiff')

and this statement to create the differential backup:

EXECUTE PROCEDURE sp\_BackupDatabase('c:\AdsBook\Backup','Diff')

Note that the options listed in Table 9-1 serve both the backup and restore system stored procedures. Furthermore, some only apply to backup or restore operations. For example, the Prepare option is used only for preparing a differential backup. By comparison, the DontOverWrite option only applies to restore operations. Restoring data from a backup is discussed in detail later in this chapter.

The sp\_BackupFreeTables system stored procedure takes five parameters, again all of data type memo. The first parameter is the directory path or UNC path to the directory in which the free tables reside.

The second parameter contains a mask indicating which tables to back up. Normally you will use this mask to identify Advantage table types, such as \*.adt to back up only ADT tables, or \*.dbf to back up DBF files.

The third parameter contains the directory path or UNC path to the destination directory, while the fourth parameter contains the backup options. These are the same options as shown in Table 9-1.

The fifth parameter is used to provide free table encryption passwords. This parameter is in the form of a semicolon-separated list of name/value pairs, where the name is a free table name and the value is its encryption password. Names and values for each pair are separated by an equals sign (=). If the free tables are not encrypted, pass an empty string or the value NULL in this parameter.

The following is an example of a backup command to back up the CUST.ADT free table associated with the FreeTableConnection connection you used in Chapter 2. In this case, the backup is placed in the c:\AdsBook\FreeTabs\Backup directory. If you want to actually test this SQL statement, you must first create the c:\AdsBook\FreeTabs\Backup directory:

EXECUTE PROCEDURE sp\_BackupFreeTables('c:\AdsBook\FreeTabs',  
  '\*.adt', 'c:\AdsBook\FreeTabs\Backup', 'include=cust.adt',  
  NULL)

Writing calls to the backup system stored procedures is not difficult. However, if you are unsure how to write your EXECUTE PROCEDURE statement, use the Backup dialog box for the connection you want to back up in the Advantage Data Architect to manually configure the backup. You can then view (and copy) the code that appears on the SQL Preview page of this dialog box. The Preview SQL page of the Backup dialog box was shown earlier in this chapter in Figure 9-3.