---
title: Devguide Restoring Data Using The Adsbackup Exe Command Line Utility
slug: devguide_restoring_data_using_the_adsbackup_exe_command_line_utility
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_restoring_data_using_the_adsbackup_exe_command_line_utility.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: a9e66776ea91bfa6d435c1a42e79046e2b976e15
---

# Devguide Restoring Data Using The Adsbackup Exe Command Line Utility

Restoring Data Using the AdsBackup.exe Command-Line Utility

     Restoring Data Using the AdsBackup.exe Command-Line Utility

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Restoring Data Using the AdsBackup.exe Command-Line Utility  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As described earlier in this chapter, you use AdsBackup.exe (or AdsBackup.jar) to restore the data dictionary or free tables that you previously backed up. This is the same utility that can be used to create the backup. This utility is stored in the same directory as the Advantage Database Server.

The following steps demonstrate how to restore the previously backed up DemoDictionary data dictionary using AdsBackup.exe. However, instead of restoring to the original database location (which we certainly could do if our DemoDictionary database was accidentally erased, or suffered some other problem), these steps will restore to a new location, effectively making a duplicate of the data that was backed up earlier in this chapter. This duplicate will be used to demonstrate the replication features described in Chapter 10.

   
NOTE: If you did not create a backup from the steps provided earlier in this chapter, and want to reproduce these steps, return to the section "Creating a Backup from the Advantage Data Architect" and follow the steps provided there. Also, recall that earlier in this chapter you learned that external files, such as stored procedure and trigger libraries are not included in the backup.  
 

1.        Begin by creating a new directory in which the restored database will be stored. If you have been using the directory structure described earlier in this book, this directory should be c:\AdsBook\Restore. (Use whatever tool suits your needs for this task. For example, Windows users may want to use Windows Explorer or the command prompt.) In this example, you will restore the previously created backup to a new, empty directory. In many cases, however, you will restore to a directory in which a database already exists.

| 2. | Now, open a command prompt. (From Windows, select the Start button in the Windows task bar and select Run. When prompted, for a file to open, enter CMD.EXE and press Enter. |

| 3. | Once you are at the command prompt, navigate to the directory in which ADS is installed. If you are using Windows, this directory is c:\Program Files\Extended Systems\Advantage 8.1\Server. Make the c drive the current drive and enter the following command to make the server's directory the current directory. Press Enter when you are done. |

cd "\Program Files\Extended Systems\Advantage 8.1\Server"

4.        You are now ready to restore your previously backed-up database to the c:\AdsBook\Restore directory. To do so, enter the following command and press Enter.

adsbackup -r p c:\AdsBook\Backup\DemoDictionary.add  
  c:\AdsBook\Restore\DemoDictionary.add

(Your entry should not contain a carriage return.)

| 5. | During the restore operation, the command prompt will update to display restore progress, as shown in Figure 9-10. |

Figure 9-10: During the Restore operation process

6.        When the restore operation is complete, your screen will look something like the one shown in Figure 9-11.

Figure 9-11: The Restore operation is completed

If you view the source directory, which is c:\AdsBook\Backup in this example, you will find the restore result table for this restore operation, as shown in Figure 9-12. As described earlier in this chapter, this table is always written to disk after you use AdsBackup.exe.

Figure 9-12: The contents of the c:\AdsBook\Backup directory

If no errors occurred during the restore operation, this table will be empty, as shown in Figure 9-13.

Figure 9-13: An empty restore result table

If you now inspect the destination directory, you will find that the data dictionary, tables, memo files, and index files have been restored to their original state. At this point, you should reinstall any DLLs that your data dictionary references, and install and register any .NET assemblies or COM servers used by your data dictionary. After doing so, you should be able to open this data dictionary in the Advantage Data Architect or from your client applications, assuming that your client applications still point to the location where this data dictionary resides. If you had restored this data dictionary to the location where a compromised data dictionary was previously located, your client applications should run fine. To open the restored data dictionary in the Advantage Data Architect, you will need to create a connection to it in the Connection Repository.

 

In the next chapter you will learn how to implement Advantage replication.
