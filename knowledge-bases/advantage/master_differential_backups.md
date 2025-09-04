Differential Backups




Advantage Database Server 12  

Differential Backups

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Differential Backups  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Differential Backups Advantage Concepts master\_Differential\_backups Advantage Concepts > Advantage Functionality > Backup > Differential Backups / Dear Support Staff, |  |
| Differential Backups  Advantage Concepts |  |  |  |  |

A differential backup only backs up record data that has changed since the last differential backup was performed. For example, if you have a large database or large tables that cause a slow backup, you could instead initialize a differential backup (with '[PrepareDiff](master_backup_and_restore_options.htm)'), and then call all subsequent backups sending the differential option ([Diff](master_backup_and_restore_options.htm) ). The initial differential backup would perform a complete backup of the data. The subsequent backups would only process tables and records that had been modified since the last backup was performed. This can significantly improve backup performance. Note that the subsequent Diff backup must be made to the same location as the initial PrepareDiff. If you perform a Diff backup to a new folder, it will behave the same as PrepareDiff and perform the full backup.

There are a number of operations that cause an existing differential backup to become invalid.  These include packing of a table, zapping (emptying) a table, altering it, and encrypting it. Prior to v12 of Advantage, it was required that you perform a re-initialization (PrepareDiff) of the backup when one of these operations was performed. With v12 and later, Advantage detects when a re-initialization of the differential backup is necessary and automatically performs it.

Differential backups are only supported on Advantage proprietary tables (ADT tables).