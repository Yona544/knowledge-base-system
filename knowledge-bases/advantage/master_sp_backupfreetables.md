sp\_BackupFreeTables




Advantage Database Server 12  

sp\_BackupFreeTables

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_BackupFreeTables  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - sp\_BackupFreeTables Advantage Concepts master\_Sp\_backupfreetables Advantage SQL > System Procedures > Procedures > sp\_BackupFreeTables / Dear Support Staff, |  |
| sp\_BackupFreeTables  Advantage Concepts |  |  |  |  |

Backup a set of free tables.

Note Free table backups will only backup structural indexes (index files with the same base filename as the table). If non-structural index file support is required, you need to put your tables and indexes into a data dictionary and use the sp\_BackupDatabase and sp\_RestoreDatabase procedures.

Syntax

sp\_BackupFreeTables(

 SourcePath, MEMO,

 SourceMask, MEMO,

 DestinationPath, MEMO,

 Options, MEMO,

 FreeTablePasswords, MEMO );

 

Parameters

|  |  |
| --- | --- |
| SourcePath (I) | Path to the tables you want to backup. This path can be UNC ( \\myserver\myshare\mydir ) or if connecting to a Microsoft Windows server, it can be a local drive letter ( c:\mydir ). If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the backup command are irrelevant. If using a drive letter for the source path, the drive must be a "local" drive, it cannot be a mapped drive. If connecting to a Linux server UNC, paths are recommended. |
| SourceMask (I) | A file mask similar to "\*.adt" or "\*.dbf" which will be used to determine what tables should be included in the backup image. Multiple masks can be used in a single backup/restore by separating them with a semicolon. For example, "\*.adt;\*.dbf". |
| DestinationPath (I) | Path to place the backup image in. This path can be UNC ( \\myserver\myshare\mydir ) or a local drive letter ( c:\mydir ) if connecting to a Microsoft Windows server. If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the backup command are irrelevant. Mapped network drive letters are not supported, and should not be used. If connecting to a Linux server UNC, paths are recommended. |
| Options (I) | Options. See [Backup and Restore Options](master_backup_and_restore_options.htm) for details. |
| FreeTablePasswords (I) | A single password or a list of passwords to use to decrypt encrypted tables. If a single password is passed, the same password will be used whenever an encrypted table is encountered. To specify multiple passwords, pass table/password pairs of the following form: "table1=password1;table2=password2", etc. |

Remarks

The sp\_BackupFreeTables canned procedure can be used to make a backup image of any free tables on the server. The source path input parameter does not have to match the path of the free connection that the canned procedure is called on. Use the SourcePath parameter and the SourceMask parameter to specify the tables to be included in the backup image.

As an alternative to using this canned procedure, you can also use the command line utility [adsbackup](master_adsbackup_utility.htm).

Note The backup image that is created should not be used directly. The backup image is not structurally complete. You must use sp\_RestoreFreeTables to restore the backup image before using it.

Result Set

See [Backup and Restore Canned Procedure Result Sets](master_backup_and_restore_canned_procedure_result_sets.htm)

Examples

Backup a free table directory to an archive file:

EXECUTE PROCEDURE sp\_BackupFreeTables( '\\myserver\myshare\sourcedir',

 '\*.adt',

 '\\myserver\myshare\backupdir',

 'ArchiveFile=backup.tar',

 NULL );

 

Backup two specific tables:

EXECUTE PROCEDURE sp\_BackupFreeTables( '\\myserver\myshare\sourcedir',

 '\*.adt',

 '\\myserver\myshare\backupdir',

 'include=table1.adt,table2.adt',

 NULL );

 

Backup free tables and place the backup image in a drive local to the server Advantage Database Server is running on:

EXECUTE PROCEDURE sp\_BackupFreeTables( '\\myserver\myshare\sourcedir',

 '\*.adt',

 'd:\backupdir',

 NULL,

 NULL );

 

Initialize a differential backup:

EXECUTE PROCEDURE sp\_BackupFreeTables( '\\myserver\myshare\sourcedir',

 '\*.adt',

 '\\myserver\myshare\backupdir',

 'PrepareDiff',

 NULL );

 

Perform a differential backup:

EXECUTE PROCEDURE sp\_BackupFreeTables( '\\myserver\myshare\sourcedir',

 '\*.adt',

 '\\myserver\myshare\backupdir',

 'Diff',

 NULL );

 

Perform a backup and use a single password for all encrypted tables:

EXECUTE PROCEDURE sp\_BackupFreeTables( '\\myserver\myshare\sourcedir',

 '\*.adt',

 '\\myserver\myshare\backupdir',

 NULL,

 'mypassword' );

 

Perform a backup and use table-specific passwords:

EXECUTE PROCEDURE sp\_BackupFreeTables( '\\myserver\myshare\sourcedir',

 '\*.adt',

 '\\myserver\myshare\backupdir',

 NULL,

 't1.adt=pass1;t2.adt=pass2' );