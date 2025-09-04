---
title: Master Sp Restoredatabase
slug: master_sp_restoredatabase
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_restoredatabase.htm
source: Advantage CHM
tags:
  - master
checksum: 379d4d9c4a426da54af43fd5e429b2d3f9baef83
---

# Master Sp Restoredatabase

sp\_RestoreDatabase

sp\_RestoreDatabase

Advantage Concepts

| sp\_RestoreDatabase  Advantage Concepts |  |  |  |  |

Restore a data dictionary and its associated tables using a backup image from a previous call to sp\_BackupDatabase.

Syntax

sp\_RestoreDatabase(

SourcePath, MEMO,

SourcePassword, MEMO,

DestinationPath, MEMO,

Options, MEMO );

 

Parameters

| SourcePath (I) | Path to the existing backup image, including the name of the .add file. An example SourcePath would be \\myserver\myshare\mybackupdir\mydd.add. This path can be any form recognized by the server operating system. For example, in Microsoft Windows this path can be UNC ( \\myserver\myshare\mydir ) or a local drive letter ( c:\mydir ). If using drive letters, keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the restore command are irrelevant. If using a drive letter for the source path, the drive must be a "local" drive, it cannot be a mapped drive. |
| SourcePassword (I) | Password to the dictionary specified in the SourcePath parameter. |
| DestinationPath (I) | Path to restore the database to, including the name of the new .add file to create. An example DestinationPath would be \\myserver\myshare\myrestoredir\mydd.add. This path can be any form recognized by the server operating system. For example, in Microsoft Windows this path can be UNC ( \\myserver\myshare\mydir ) or a local drive letter ( c:\mydir ). If using drive letters keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the restore command are irrelevant. Mapped network drive letters are not supported, and should not be used. |
| Options (I) | Options. See [Backup and Restore Options](master_backup_and_restore_options.md) for details. |

Remarks

The sp\_RestoreDatabase procedure can be used to restore a database from a backup image created with the sp\_BackupDatabase procedure.

This procedure can be called from a free connection or a dictionary connection.

If you are connected to a different data dictionary you must still be logged in as the ADSSYS user (or a user in the DB:Backup group) in that database in order to call sp\_RestoreDatabase.

As an alternative to using this canned procedure, you can also use the command line utility [adsbackup](master_adsbackup_utility.md).

Result Set

See [Backup and Restore Canned Procedure Result Sets](master_backup_and_restore_canned_procedure_result_sets.md)

Examples

Restore a data dictionary from a compressed archive file:

EXECUTE PROCEDURE sp\_RestoreDatabase(

 '\\server\share\backupdir\mydd.add',

 'password\_to\_mydd',

 '\\server\share\restoredir\mydd.add',

 'ArchiveFileCompressed=backup.tar.gz' );

 

Restore two specific tables:

EXECUTE PROCEDURE sp\_RestoreDatabase(

 '\\server\share\backupdir\mydd.add',

 'password\_to\_mydd',

 '\\server\share\restoredir\mydd.add',

 'include=table1,table2' );
