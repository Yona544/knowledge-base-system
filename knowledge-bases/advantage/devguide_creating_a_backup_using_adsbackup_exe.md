Creating a Backup Using AdsBackup.exe




Advantage Database Server 12  

     Creating a Backup Using AdsBackup.exe

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Backup Using AdsBackup.exe  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating a Backup Using AdsBackup.exe Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Backup\_Using\_AdsBackup\_exe Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 9 - Backups > Creating a Backup Using AdsBackup.exe / Dear Support Staff, |  |
| Creating a Backup Using AdsBackup.exe  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

AdsBackup.exe is a command-line utility that calls the sp\_BackupDatabase or sp\_BackupFreeTables system stored procedures. This utility is available for both Windows and Linux versions of ADS. For Novell versions of ADS, there is a Java version available in the AdsBackup.jar file. (The use of AdsBackup.jar is similar to that of AdsBackup.exe, so only AdsBackup.exe is described in this chapter.) These utilities are located in the same directory as the Advantage Database Server.

AdsBackup.exe is used to back up both data dictionaries and free tables, as well as to restore backed up data. You pass command-line parameters to AdsBackup.exe in order to control the backup and restore operations.

In order to see what command-line parameters are available, as well as to see examples of the invocation of AdsBackup.exe, run AdsBackup.exe without any parameters. The resulting help screen displayed by AdsBackup.exe is shown in Figure 9-5.

It is not uncommon to call AdsBackup.exe from a batch file, with this batch file containing all of the command-line options that you need for your backup. This batch file can then be called by a scheduler, such as the Windows Task Scheduler. By scheduling regular backups of your data (such as one every morning at 2:00 a.m. when fewer users are online), you ensure that you will be able to restore your data if something happens to your database.

   
NOTE: A special file, called the backup result table, is created during every execution of AdsBackup.exe. If you schedule backups on a regular basis, you should make sure that someone checks the backup result table, looking for any errors that were encountered during the backup. The backup result table is described in the following section.  
 

Figure 9-5: The AdsBackup.exe help

When you call AdsBackup.exe to back up a data dictionary, you pass the ADSSYS password in the p command-line option (since backups are usually only created for deployed databases, it is unlikely that you will have a blank password for the ADSSYS account). You also pass the fully qualified name of the data dictionary you are backing up, as well as the directory to which you want the backup placed.

For example, to create the same backup of DemoDictionary using AdsBackup.exe as that created in the steps you followed earlier in chapter, you would use the following command (note the blank password in this case):

adsbackup -p "C:\AdsBook\DemoDictionary.add"  
  "C:\AdsBook\Backup"

Like with system stored procedures, calls to AdsBackup.exe are not difficult to write. Nonetheless, you can have your command-line call to AdsBackup.exe generated for you by the Backup dialog box. After configuring your backup using the Backup dialog box, select the Command Line tab to view the Command Line page. This page was shown earlier in this chapter in Figure 9-4.