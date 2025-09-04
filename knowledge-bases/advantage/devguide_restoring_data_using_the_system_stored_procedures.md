Restoring Data Using the System Stored Procedures




Advantage Database Server 12  

     Restoring Data Using the System Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Restoring Data Using the System Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Restoring Data Using the System Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Restoring\_Data\_Using\_the\_System\_Stored\_Procedures Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 9 - Backups > Restoring Data Using the System Stored Procedures / Dear Support Staff, |  |
| Restoring Data Using the System Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Using the restore system stored procedures to restore a backup is similar to how you use the system stored procedures to make a backup. You use sp\_RestoreDatabase to restore a previously backed up data dictionary, and sp\_RestoreFreeTables to restore previously backed up free tables.

The stored procedure sp\_RestoreDatabase takes four parameters, all of which are of the data type memo. Provide the fully qualified (or UNC) path and filename to the backed up data dictionary in the first parameter. The filename must include the .add extension. Provide the ADSSYS password to the originally backed-up data dictionary in the second parameter. If the ADSSYS password is blank, enter either an empty string or the value NULL.

Provide the fully qualified (or UNC) path and filename to the destination data dictionary in the third parameter. Normally, the filename will be identical to that of the originally backed up data dictionary, though the path may be different depending where you want the restored dictionary to be placed.

   
NOTE: From the General page of the Restore dialog box, the Destination field only asks for a path. By comparison, the sp\_RestoreDatabase system stored procedure also requires a filename.  
 

Use the fourth parameter to provide a semicolon-separated list of restore options. The available options can be found earlier in this chapter in Table 9-1. As is the case with backups, not all of these options apply to restore operations.

The sp\_RestoreFreeTable stored procedure also takes four parameters, once again all of type memo. Use the first parameter to point to the directory in which the previously backed up free tables are stored. Use the second parameter to point to the directory into which you want these tables restored.

Use the third parameter to provide any restore options. These options are the same as those used by the sp\_RestoreDatabase procedure. Finally, use the fourth parameter to provide a semicolon-separated list of name/value pairs representing the encrypted free table passwords. This list was described earlier in this chapter during the discussion of sp\_BackupFreeTables.

Just as you can use the Backup dialog box in the Advantage Data Architect to preview the calls to the backup system stored procedures, you can use the SQL Preview page of the Restore dialog box to view the corresponding call to a restore system stored procedure based on your manually configured restoration. If you want insight into how a particular stored procedure call should be written, use the Advantage Data Architect to configure the restore operation, and then view the generated SQL on the SQL Preview page of the Restore dialog box.

Imagine that you want to restore the data dictionary that you backup using the steps given previously in this chapter, except that you want to restore the database to a directory named c:\AdsBook\Restore. The following is the SQL that you can execute in the SQL Utility to create this restored database:

EXECUTE PROCEDURE  
  sp\_RestoreDatabase('c:\AdsBook\Backup\Demotionary.ADD',  
  '',  //This data dictionary has a blank password  
  'c:\AdsBook\Restore\DemoDictionary.ADD',  
  '')  //No options required for this restore

Earlier in this chapter we provided an example of an sp\_BackupFreeTables stored procedure call demonstrating how to back up the CUST.ADT table to the c:\AdsBook\FreeTabs\Backup directory. If you had actually used that procedure call to back up the CUST.ADT free table, you could use the following SQL to restore that backup to c:\AdsBook\FreeTabs\Restore (assuming that the c:\AdsBook\FreeTabs\Restore directory already exists):

EXECUTE PROCEDURE   
  sp\_RestoreFreeTables('c:\AdsBook\FreeTabs\Backup' ,  
  'c:\AdsBook\FreeTabs\Restore',  
  'include=cust.adt', '') //no passwords, table not  
                          //encrypted