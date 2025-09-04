---
title: Master Sp Backupdatabase
slug: master_sp_backupdatabase
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_backupdatabase.htm
source: Advantage CHM
tags:
  - master
checksum: e83e4f4d31e5abc558c36797317d79584fcabc9a
---

# Master Sp Backupdatabase

sp\_BackupDatabase

sp\_BackupDatabase

Advantage Concepts

| sp\_BackupDatabase  Advantage Concepts |  |  |  |  |

Backup a data dictionary and its associated tables.

Syntax

sp\_BackupDatabase(

DestinationPath, MEMO,

Options, MEMO );

 

Parameters

| DestinationPath (I) | Path to place the backup image in. This path can be any form recognized by the server operating system. For example, in Microsoft Windows this path can be UNC ( \\myserver\myshare\mydir ) or a local drive letter ( c:\mydir ). If using drive letters keep in mind the drive letter must be recognized by the server machine, any drives mapped on the client executing the backup command are irrelevant. Mapped network drive letters are not supported, and should not be used. |
| Options (I) | Options. See [Backup and Restore Options](master_backup_and_restore_options.md) for details. |

Remarks

The sp\_BackupDatabase canned procedure can be used to make a backup image of the data dictionary you are currently connected to. It cannot be called from a free connection.

You must be logged in as the ADSSYS user or a user in the DB:Backup group in order to call sp\_BackupDatabase.

As an alternative to using this canned procedure, you can also use the command-line utility [adsbackup](master_adsbackup_utility.md).

Note The backup image that is created should not be used directly. The backup image is not structurally complete. You must use [sp\_RestoreDatabase](master_sp_restoredatabase.md) to restore the backup image before using it.

Result Set

See [Backup and Restore Canned Procedure Result Sets](master_backup_and_restore_canned_procedure_result_sets.md)

Examples

Backup a data dictionary:

EXECUTE PROCEDURE sp\_BackupDatabase( '\\myserver\myshare\mybackupdir', NULL );

 

Backup two specific tables from the database:

EXECUTE PROCEDURE sp\_BackupDatabase( '\\myserver\myshare\mybackupdir',

         include=table1,table2 );

 

Backup a data dictionary and place the backup image in a drive local to the server on which Advantage Database Server is running and store the backup image in a compressed archive file:

EXECUTE PROCEDURE sp\_BackupDatabase( 'd:\mybackupdir',

         'ArchiveFileCompressed=backup.tar.gz' );

 

Initialize a differential backup:

EXECUTE PROCEDURE sp\_BackupDatabase( 'd:\mybackupdir', 'PrepareDiff' );

 

Perform a differential backup:

EXECUTE PROCEDURE sp\_BackupDatabase( 'd:\mybackupdir', 'Diff' );
