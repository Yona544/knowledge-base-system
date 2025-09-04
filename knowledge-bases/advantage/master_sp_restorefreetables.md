sp\_RestoreFreeTables




Advantage Database Server 12  

sp\_RestoreFreeTables

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_RestoreFreeTables  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - sp\_RestoreFreeTables Advantage Concepts master\_Sp\_restorefreetables Advantage SQL > System Procedures > Procedures > sp\_RestoreFreeTables / Dear Support Staff, |  |
| sp\_RestoreFreeTables  Advantage Concepts |  |  |  |  |

Restore a set of free tables using a backup image from a previous call to sp\_BackupFreeTables.

Note Free table restorations will only restore structural indexes (index files with the same base filename as the table). If you need to restore non-structural index files you need to put your tables and indexes into a data dictionary and use the sp\_BackupDatabase and sp\_RestoreDatabase procedures.

Syntax

sp\_RestoreFreeTables(

SourcePath, MEMO,

DestinationPath, MEMO,

Options, MEMO,

FreeTablePasswords, MEMO );

 

Parameters

|  |  |
| --- | --- |
| SourcePath (I) | Path to the existing backup image. This path can be any form recognized by the server operating system. For example, in Microsoft Windows this path can be UNC ( \\myserver\myshare\mydir ) or a local drive letter ( c:\mydir ). If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the restore command are irrelevant. If using a drive letter for the source path, the drive must be a "local" drive, it cannot be a mapped drive. |
| DestinationPath (I) | Path to restore the database to. This path can be any form recognized by the server operating system. For example, in Microsoft Windows this path can be UNC ( \\myserver\myshare\mydir ) or a local drive letter ( c:\mydir ). If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the restore command are irrelevant. Mapped network drive letters are not supported, and should not be used. |
| Options (I) | Options. See [Backup and Restore Options](master_backup_and_restore_options.htm) for details. |
| FreeTablePasswords (I) | A single password or a list of passwords to use to decrypt encrypted tables. If a single password is passed, the same password will be used whenever an encrypted table is encountered. To specify multiple passwords, pass table/password pairs of the following form: "table1=password1;table2=password2", etc. |

Remarks

The sp\_RestoreFreeTables procedure can be used to restore a database from a backup image created with the sp\_BackupFreeTables procedure.

As an alternative to using this canned procedure, you can also use the command-line utility [adsbackup](master_adsbackup_utility.htm).

Result Set

See [Backup and Restore Canned Procedure Result Sets](master_backup_and_restore_canned_procedure_result_sets.htm)

Examples

Restore a set of free tables:

EXECUTE PROCEDURE sp\_RestoreFreeTables(

 '\\server\share\backupdir',

 '\\server\share\restoredir',

 NULL,

 NULL );

 

Restore two specific tables from an archive file:

EXECUTE PROCEDURE sp\_RestoreFreeTables(

 '\\server\share\backupdir',

 '\\server\share\restoredir',

 'include=table1.adt,table2.adt;ArchiveFile=backup.tar',

 NULL );