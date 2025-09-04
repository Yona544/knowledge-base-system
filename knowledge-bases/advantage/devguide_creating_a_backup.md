Creating a Backup




Advantage Database Server 12  

 

     Creating a Backup

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Backup  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Creating a Backup Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Backup Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 9 - Backups > Creating a Backup / Dear Support Staff, |  |
| Creating a Backup  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage's online backup is implemented through a collection of system stored procedures. These procedures can be executed through a number of different mechanisms. They can be invoked through a special backup dialog box in the Advantage Data Architect, through direct calls to the system stored procedures, or through a command-line utility. Which mechanism you use depends on your needs.

If you are managing a database using the Advantage Data Architect, you will likely prefer using Advantage Data Architect to create the backup. On the other hand, if you want to expose backup operations from your client applications, the system stored procedures are invaluable. Finally, if you want to schedule backups using a scheduler, such as the Scheduled Tasks applet located on the Windows Control Panel, you will use the AdsBackup.exe utility.

Regardless of which option you use, if you are backing up a data dictionary, you must be connected using the Administrative account. With free table connections, you will need the free table passwords if you are backing up encrypted tables.

The following sections describe how to back up your data using each of the available backup options.