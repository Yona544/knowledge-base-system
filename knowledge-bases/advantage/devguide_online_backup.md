Online Backup




Advantage Database Server 12  

     Online Backup

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Online Backup  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Online Backup Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Online\_Backup Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Online Backup / Dear Support Staff, |  |
| Online Backup  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Online backup permits you to create a copy of your database even while users are making changes to it. This backup can then be used to restore your database after a catastrophic failure of the database, such as a hard disk crash, destruction of the server, or other similar disaster.

Advantage supports two types of backups: full and differential. A full backup makes a complete copy of your database, including data dictionary, tables, and memos. A differential backup only backs up records that were changed since the last differential backup. Since differential backups typically involve fewer records, they are faster. Online backup is not available with ALS. Online backups are discussed in detail in Chapter 9.