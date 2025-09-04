Using Access Rights and Groups




Advantage Database Server 12  

     Using Access Rights and Groups

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Access Rights and Groups  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Using Access Rights and Groups Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Access\_Rights\_and\_Groups Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Using Access Rights and Groups / Dear Support Staff, |  |
| Using Access Rights and Groups  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As you probably concluded from the preceding discussions concerning users, groups, and access rights, how you set up the security for your data dictionary depends largely on your application's needs. In the case of the data dictionary created in this chapter, a simple security model will be employed. You will create two groups, one with readonly access to the data dictionary's tables, and one with full read and write access (lacking only create, grant, alter, and drop rights). You will then assign adsuser to the read and write group.

Use the following steps to configure security for this data dictionary:

Right-click the GROUPS node in the DemoDictionary connection and select Create. The Group dialog box, shown in Figure 4-8, is displayed.

Figure 4-8: The Group dialog box

Set Name to ReadWrite.

Click the Description tab and enter Sample group with read and write permissions.

Click the General tab to return to the General page, and then click Permissions to display the Permissions dialog box shown in Figure 4-9.

Figure 4-9: The Permissions dialog box

The Permissions dialog box includes a combo box at the top center. You use this dialog box to select the type of data dictionary object to which you want to grant rights. By default, this combo box is set to Table. Since our data dictionary only contains tables at this point, there is no need to change this setting.   
   
You set permissions by clicking on the checkboxes to toggle among three settings: the ability to perform the task (checked), the ability to perform the table as well as grant rights to the task (checked with a + sign), or no rights (unchecked). Which task depends on which column the checkbox appears in. For example, for the Select rights column, the three options are Grant SELECT, Grant SELECT with GRANT (can grant select rights to others), or Revoke SELECT.  
   
If you right-click in a column, a context menu appears that permits you to grant or revoke rights to the table in that column in a single step. For example, you can right-click in the Select column and select Grant SELECT to All, which will grant Select rights to all tables.

Right-click the Select, Insert, Update, and Delete columns, in turn, and grant those rights to all tables in the column, as shown in Figure 4-9.

The settings on the Permissions dialog box with Table selected apply to entire tables. If you want to configure field-level permissions, select (highlight) a table name from the Permissions dialog box, and click the Field Permissions button. For example, if you select the ITEMS table in the Permissions dialog box and click Field Permissions, you will see the Field Permissions dialog box shown in Figure 4-10. This dialog box permits you to set the Select, Update, and Insert permissions for the fields in the ITEMS table.  
   
You set permissions by clicking on the checkboxes to toggle among three settings: Grant, Grant with GRANT, or Revoke. Similar to table-level rights, you can right-click a column to display a context menu that permits you to grant or revoke rights to all fields in the column in a single step.

Figure 4-10: The Field Permissions dialog box

As long as no checkboxes are checked on the Field Permissions dialog box, the group's members have access to all of the table's fields granted by the table's rights. If at least one checkbox is checked, that group's members will have only those permissions explicitly granted by the field-level permissions. Do not select any field permissions. Click OK to close the Field Permissions dialog box and return to the Permissions dialog box.

If there were additional objects in the data dictionary, you could now select the next type of object to which you want to grant rights. At this point, however, we are done. Click OK to close the Permissions dialog box and return to the Group dialog box (shown in Figure 4-8).

From the Group dialog box, click the Members button to display the Group Members dialog box, shown in Figure 4-11, where you can add one or more members to this new group:

Select the adsuser user from the Users list and click the right arrow to move adsuser into the Group Members list. If there were additional users in this database, you could repeat this step for each additional user you want to add to group. Click OK to close the Group Members dialog box and return to the Group dialog box.

Figure 4-11: The Group Members dialog box

Click Create on the Group dialog box to complete the creation of this group. Click Close.

Instead of adding users to a group's members list, you can add a group to a user's groups list. To do this, double-click on an existing user from the USERS node. From the User dialog box, click the Groups button. The available groups are listed in this Groups dialog box. The groups to which this user currently belongs are checked.