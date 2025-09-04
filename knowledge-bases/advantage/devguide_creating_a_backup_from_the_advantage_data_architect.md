Creating a Backup from the Advantage Data Architect




Advantage Database Server 12  

     Creating a Backup from the Advantage Data Architect

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Backup from the Advantage Data Architect  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating a Backup from the Advantage Data Architect Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Backup\_from\_the\_Advantage\_Data\_Architect Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 9 - Backups > Creating a Backup from the Advantage Data Architect / Dear Support Staff, |  |
| Creating a Backup from the Advantage Data Architect  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create a backup from the Advantage Data Architect by right-clicking a connection in the Connection Repository and selecting Backup from the displayed context menu. In response, the Advantage Data Architect displays the backup dialog box shown in Figure 9-1.

Figure 9-1: The Backup dialog box

Use the General page of the Backup dialog box to define the location where the backup will be saved.

Select the Advanced page of the Backup dialog box, shown in   
Figure 9-2, to either prepare for a differential backup, to perform a differential backup, or to back up only selected tables.

Figure 9-2: The Advanced page of the Backup dialog box

You use the Advanced page to prepare for a differential backup, as well as to perform a differential backup. In addition, this page permits you to selectively back up specific tables in your database.

As mentioned earlier, there are two programmatic ways to initiate a backup. The two remaining pages of the Backup dialog box provide you with insight into how to structure these commands.

You use the Preview SQL page, shown in Figure 9-3, to view the system stored procedure invocation that would produce the same backup as that which your currently configured Backup dialog box produces.

In order to view the corresponding invocation of the AdsBackup command-line utility, select the Command Line tab. The Command Line page of the Backup dialog box is shown in Figure 9-4.

Figure 9-3: The SQL Preview page of the Backup dialog box

Figure 9-4: The Command Line page of the Backup dialog box

After selecting your backup options, click the OK button to create or prepare your backup.

Use the following steps to create a backup of your DemoDictionary data dictionary using the Advantage Data Architect. This backup will be used to demonstrate a restore operation later in this chapter. That restored database, in turn, will be used in Chapter 10 to demonstrate the ADS 8 replication feature.

With the DemoDictionary connection open and current in the Advantage Data Architect, right-click the connection and select Backup.

Click the Browse button on the General page of the Backup dialog box. Select the directory in which the DemoDictionary.ADD resides and click Make New Folder. Select this folder, press F2, and change its name to Backup. If you have placed your data in the directory suggested in Appendix A, this directory will be c:\AdsBook\Backup. Click OK after selecting this directory.

The Destination field of the Backup dialog box now contains the path c:\AdsBook\Backup.

Click OK to initiate the backup. A progress bar depicts the progress of the backup, which due to this database's relatively small size, and no additional users accessing it, takes very little time.

A result set (cursor) is created during the backup process. If one or more errors are encountered during the backup process, this result set is displayed within the Advantage Data Architect once the backup operation is complete. The result set is discarded once you close it or exit the Advantage Data Architect. If you want to keep a copy of the result set for later use, right-click it and select Export to export its contents to a new or existing table.