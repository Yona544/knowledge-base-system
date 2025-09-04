---
title: Master Online Backup
slug: master_online_backup
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_online_backup.htm
source: Advantage CHM
tags:
  - master
checksum: 0f3c82bfe8fe1e746dd7769f4b2f66a09459f65f
---

# Master Online Backup

Online Backup

Online Backup

Advantage Concepts

| Online Backup  Advantage Concepts |  |  |  |  |

Online Backup (or "hot" backup) functionality allows you to capture and save a snapshot of your database. If users currently have tables opened and are making changes, the resulting backup image will not include their new modifications, it will only include the data as it existed when the snapshot was taken.

When a backup is started, it goes through a synchronization process in order to take the snapshot. This synchronization process guarantees the backup will not start while other users are in the middle of any operation that would violate the integrity of the snapshot. For example, the backup will wait to start if another user is in the middle of an RI cascade operation, which would cause the backup to have a logically incorrect snapshot.

A typical backup operation will specify a backup directory that you would like the backup image to be placed into. The tables, memo files, and indexes in this directory should never be used directly; they should only be used after executing a database restore command. Opening tables in the backup image directly will result in unexpected behavior.

Backup and restore functionality is accessible via four canned procedures; [sp\_BackupDatabase](master_sp_backupdatabase.md), [sp\_BackupFreeTables](master_sp_backupfreetables.md), [sp\_RestoreDatabase](master_sp_restoredatabase.md), and [sp\_RestoreFreeTables](master_sp_restorefreetables.md).

In addition to these canned procedures, the server installation directory also includes a command line utility for Microsoft Windows and a command line utility for Linux. These command line utilities can be called by operating system schedulers to facilitate scheduled backups.

The backup image does not have to be placed on the same server as the database. [Server-Side Aliases](master_server_side_aliases.md) can be used on Windows servers to specify an alternate destination on a remote PC, CD-ROM drive, ZIP drive, etc. Linux users can specify any mount point as a destination.

Both the backup and restore procedures allow you to specify table inclusion and exclusion lists. These lists can be used to specify tables that you want to involve in the operations. The default behavior is to include all tables in the database, or all free tables that match the free table mask specified in the backup/restore command.

It is possible to use the [ArchiveFile and ArchiveFileCompressed options](master_backup_and_restore_options.md) to specify that the backup image be placed in a single archive file. If an archive file is specified for the backup (and subsequent restore), it can be simpler to manage individual backup images since they will be contained entirely in a single file. A benefit to this is that a backup image will not be accidentally mistaken for a valid database image.

Restore

The restore command restores a backup image to a target directory. The target directory can be a working directory that already includes an existing database (or a portion of that database), or it can be an empty directory.

The sp\_RestoreDatabase and sp\_RestoreFreeTables canned procedures are used to restore a database. The adsbackup utility can also be used to restore a database.

Restrictions

Incremental backups are not supported. As an alternative approach if incremental backups are required, you could run an Advantage backup each day, and then use a third-party backup utility that supports incremental backups to save the Advantage backup image (not the live data).

Online backup and restore functionality is only supported with the Advantage Database Server. Advantage Local Server data can be backed up using any third-party backup utility. When backing up local server data, it will not be possible to get a snapshot of the database. You will also likely have to configure your backup utility to ignore data locking errors if you are backing up your data while users are accessing it.

Related Topics

[The adsbackup Utility](master_adsbackup_utility.md)

[Backup and Restore Canned Procedures](master_backup_and_restore_canned_procedures.md)

[Differential Backups](master_differential_backups.md)

[Backup and Restore Options](master_backup_and_restore_options.md)

[Backup and Restore Canned Procedure Result Sets](master_backup_and_restore_canned_procedure_result_sets.md)

[sp\_BackupDatabase](master_sp_backupdatabase.md)

[sp\_RestoreDatabase](master_sp_restoredatabase.md)

[sp\_BackupFreeTables](master_sp_backupfreetables.md)

[sp\_RestoreFreeTables](master_sp_restorefreetables.md)
