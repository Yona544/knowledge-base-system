---
title: Master Backup And Restore Options
slug: master_backup_and_restore_options
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_backup_and_restore_options.htm
source: Advantage CHM
tags:
  - master
checksum: cc0fde9a4694e0120506298c4e998af300f4c12b
---

# Master Backup And Restore Options

Backup and Restore Options

Backup and Restore Options

Advantage Concepts

| Backup and Restore Options  Advantage Concepts |  |  |  |  |

The following options can be passed in the options parameter to the [Backup and Restore Canned Procedures](master_backup_and_restore_canned_procedures.md). These options are similar to, but should not be confused with the [adsbackup utility command line parameters](master_adsbackup_utility.md).

If you do not want to pass any options you can pass an empty string () or NULL.

If you want to pass multiple options separate each option with a semi-colon (;).

Example: include=table1;PrepareDiff

Include

Use this option to specify a list of tables to include in the backup or restore. Only the tables in this list will be processed. The option should include the keyword "include" followed by an equal sign and then a comma-delimited list of table names.

Example: include=table1, table2

If backing up or restoring a data dictionary, use the table object names. If backing up or restoring free tables, use the base filename and the file extension. For example:

Example: include=table1.adt, table2.adt

Exclude

Use this option to specify a list of tables to exclude from the backup or restore. Tables in this list will not be processed. The option should include the keyword "exclude" followed by an equal sign and then a comma-delimited list of table names.

Example: exclude=table1, table2

If backing up or restoring a data dictionary, use the table object names. If backing up or restoring free tables, use the base filename and the file extension. For example:

Example: exclude=table1.adt, table2.adt

ArchiveFile

This option is used to specify the name of an archive file that will contain the individual backed up files. If this option is used with a backup, the backed up files will be placed in a tar archive file, and the individual files will be removed from disk. For a restore operation, this option specifies the archive file that contains the backup image.

Example: ArchiveFile=mybackup.tar

The location of the archive file is relative to the backup folder location. In the above example it would be placed in the specified backup folder. For a restore, it is expected to be in the source backup folder location.

Note: The maximum file name length for individual files is 99 characters. If a table has a file name on disk that exceeds this, then the archive file will not be created.

Note: If the archive file cannot be created (e.g., there was not enough disk space), the backup image will still exist on disk in the form of the individual files (the same as if the archive option had not been provided). The information about the failure to create the archive file will be in the [system procedure result set](master_backup_and_restore_canned_procedure_result_sets.md), but the system procedure itself will return success.

ArchiveFileCompressed

This option is the same as ArchiveFile except that the resulting archive file is compressed. It can result in a much smaller backup image in some cases. If your tables are encrypted, though, then this option may not result in saving very much space since encrypted data does not compress well. If you specify this option for the backup, you need to also specify it for the restore operation.

Example: ArchiveFileCompressed=mybackup.tar.gz

Note that the tar and gz extensions are not required but are the standard naming convention used for tar files and compressed tar files. The archive file name is used as given; the .tar and .gz extensions are not added automatically. If you specify the option as 'ArchiveFileCompressed=backup.data', then the file name will be 'backup.data'.

ForceArchiveExtract

When using archive files (ArchiveFile or ArchiveFileCompressed), this option controls the behavior when a file (table) to be extracted from the archive already exists on disk. The default behavior is to not overwrite the file on disk. If this option is supplied, then the file on disk will be overwritten with the file from the archive. Note that under normal circumstances this situation should not exist. But it is possible to occur. For example, it could occur if you performed an online backup to an archive file and then used a 3rd party archive file tool to extract the files to disk.

Example: ForceArchiveExtract;ArchiveFile=back.tar

DontOverwrite

Specify the "DontOverwrite" keyword if you do not want the restore operation to overwrite existing tables. A warning will be logged to the result set and the file will not be restored. This option applies only to restore operations.

Example: DontOverwrite

MetaOnly

Specify the "MetaOnly" keyword if you only want to backup or restore the data dictionary file.

Example: MetaOnly

PrepareDiff

Specify the "PrepareDiff" keyword if you want to initialize a [differential backup](master_differential_backups.md). Note that with Advantage v12 and later, it is not essential that you initialize a backup with PrepareDiff.  It is valid to simply use the 'Diff' keyword. Advantage will detect if a differential backup is not possible and will automatically initialize it. When Advantage detects this situation, it logs information to the backup result set. If you use the PrepareDiff option, these warnings are not logged. Note that differential backups are only supported with the ADT table type.

Example: PrepareDiff

Diff

Specify the "Diff" keyword if you want to perform a [differential backup](master_differential_backups.md) on a database that you have previously initialized using the "PrepareDiff" keyword. The Diff backup must be made to the same location as the previous PrepareDiff or Diff backup. Beginning with v12, Advantage verifies on a table-by-table basis if the differential backup is possible. If it is not, it will automatically re-initialize the backup for the table and log an information message about this to the backup result set. Note that differential backups are only supported with the ADT table type.

Example: Diff

TableTypeMap

Use this option to specify what table type should be used for a specific table extension. Only necessary for free table backup/restore operations. This option can be used to backup and/or restore a directory of free tables that consists of both ADT and DBF tables. The option should include a three byte extension, followed by an equal sign, followed by the Advantage table type constant. Each mapping is separated by a comma. For example:

TABLETYPEMAP=adt=ADS\_ADT,dbf=ADS\_CDX

could be used to specify files with the extension "adt" should be opened using the ADS\_ADT table type, and files with the extension "dbf" should be opened with the ADS\_CDX table type. This mapping allows the caller to specify the table type at a more granular level (as opposed to a single table type global setting).

User

By default, restore operations attempt to connect to the backed up database with the ADSSYS user. If you want to specify a different user for a restore, this option can be used. Note that the password is provided as a parameter to [sp\_RestoreDatabase](master_sp_restoredatabase.md).

Example: User=OtherUser

DDPassword

Specify the data dictionary password to use on a restore operation for a dictionary that uses [AES encryption](master_encryption.md). This is only needed for a restore operation. A backup operation, by definition, occurs on a valid connection to the dictionary, which means that the dictionary password would already have been provided.

NoWarnings

By default [sp\_RestoreDatabase](master_sp_restoredatabase.md) will log entries to the error log (ads\_err.adt) for information purposes if the restore operation creates a table. The error numbers for each table created typically include 5168, 7041, and a system code 2. If the 'NoWarnings' option is included, the logging of these entries will be supressed.

Example: NoWarnings
