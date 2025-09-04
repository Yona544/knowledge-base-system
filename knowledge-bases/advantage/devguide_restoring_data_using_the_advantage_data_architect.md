Restoring Data Using the Advantage Data Architect




Advantage Database Server 12  

     Restoring Data Using the Advantage Data Architect

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Restoring Data Using the Advantage Data Architect  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Restoring Data Using the Advantage Data Architect Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Restoring\_Data\_Using\_the\_Advantage\_Data\_Architect Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 9 - Backups > Restoring Data Using the Advantage Data Architect / Dear Support Staff, |  |
| Restoring Data Using the Advantage Data Architect  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

To restore a database, right-click the connection representing the database you want to restore and select Restore.

Unlike a backup, which can be performed even while the database is in use, restoring a database cannot be performed while other users are accessing data. This is not a problem, however, since restoring a database is something you do only because your current database has been damaged or compromised. (A hard-drive crash, fire, flood, or theft are just a few of the incidences that may compromise a database). Such a database would have no users.

You use the General page of the Restore dialog box to identify the data you want to restore and where to put the restored data. For a data dictionary connection, the General page, shown Figure 9-7, permits you to select the previously created backup you want to restore from, the destination to which you want to restore it, and the ADSSYS password for the database you are restoring.

Figure 9-7: The General page of the Restore dialog box for a data dictionary connection

For a free table connection, you use the General page, shown in Figure 9-8, to identify the directory to which free tables were backed up, and the directory to which you want them restored.

Figure 9-8: The General page of the Restore dialog box for a free table connection

If you want to restore less than all of the backed up tables, select the Advanced tab to display the Advanced page of the Restore dialog box shown in Figure 9-9. Here you can place a checkmark next to only those tables that you want restored.

Figure 9-9: The Advanced page of the Restore dialog box

As with the Backup dialog box, the Preview SQL page and the Command Line page of the Restore dialog box can be used to review the EXECUTE PROCEDURE command and command-line code for the restoration options that you configure from the General and Advanced pages.

An in-memory result set table is created as a byproduct of a restore operation. This result set table has the same structure and content as that created when performing a backup (see Table 9-2).

As is the case when backing up, this result set is written to disk when restoring using the command-line utilities. When restoring from the Advantage Data Architect or the system stored procedures, if errors are encountered during the restore process you must specifically take steps to save this result set if you want to keep a copy.