Backing Up and Restoring Data




Advantage Database Server 12  

     Backing Up and Restoring Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Backing Up and Restoring Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Backing Up and Restoring Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Backing\_Up\_and\_Restoring\_Data Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 9 - Backups > Backing Up and Restoring Data / Dear Support Staff, |  |
| Backing Up and Restoring Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Probably one of the most anticipated and welcome additions found in Advantage 8.0 is online backup. With online backup, you can create backups of your database even while it is in use. Online backup requires the Advantage Database Server (ADS).

When you initiate a backup, ADS attempts to synchronize a snapshot of the database. A snapshot is a moment in time where no records are being modified by users, no users are in the middle of an RI cascade operation, no transactions are being rolled back, and no other operations are proceeding that would prevent the backup from being in a logically consistent state. Once the snapshot is synchronized, ADS begins keeping copies of records that are modified or deleted. Furthermore, it notes when records are inserted.

As the backup proceeds, the backup image of the database reflects the moment that the snapshot is taken. Specifically, if a record is updated after the snapshot is taken, it is only the original value of the record that is written to the backup. Similarly, if a record is deleted during the backup, it will nonetheless appear in the backup. Records inserted during the backup do not appear in the backup.

Sometimes it is not possible for ADS to acquire a snapshot in a reasonable period of time. This happens if there is always at least one record involved in a parent-child relationship participating in a transaction while the snapshot is being attempted. In these cases, the snapshot is nonetheless taken, but it is noted as being a blurry snapshot. A blurry snapshot may contain slightly inconsistent data, depending on what happened to records involved in transactions associated with parent-child relationships. In short, Advantage considers it more important to take a blurry snapshot and continue with the backup as opposed to making no backup at all.

Advantage's online backup utility supports both complete and differential backups. Differential backups take less time to execute than complete backups by updating only those records that were changed, deleted, or added since the last backup. Creating a complete backup requires no preparation. By comparison, you must prepare the differential backup before you can perform the differential backup. This preparation must also be repeated if the structures of any of your tables that you are including in the backup have changed. Options for preparing a differential backup are described later in this chapter.

   
CAUTION: You must reprepare for a differential backup each time you make a change to any of your tables or indexes involved in the backup. Failure to reprepare for a differential backup after a change to tables or indexes will result in the failure of the differential backup.  
 

 

   
NOTE: Differential backups are distinct from incremental backups. With incremental backups, many backup images, each associated with a different incremental backup, may be required to restore your database. Differential backups create a single image from which you restore your database. Advantage does not support incremental backups.