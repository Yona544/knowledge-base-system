Checking User Rights




Advantage Database Server 12  

     Checking User Rights

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Checking User Rights  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Checking User Rights Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Checking\_User\_Rights Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Checking User Rights / Dear Support Staff, |  |
| Checking User Rights  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

User rights refer to access permissions associated with the tables, fields, views, stored procedures, database links, and other objects associated with your data dictionary. For some objects, such as stored procedures, rights refer to whether or not a connection for that particular user has the right to execute the stored procedure. For other objects, such as tables, these rights are more involved. For example, you can permit one user to view a particular table, but that is all. You might provide another user with complete access to that table, permitting them to view and edit the data, and even to alter the table's structure.

The rights for tables can be extended down to the field level. For example, for the user who can only read a particular table, you can further define that there are one or more fields that this user is not even allowed to see. For example, you might let a user view the records of the employee table, but deny them the ability to view the Salary field.

There are two parts to controlling user rights. The first is to configure the data dictionary to check a user's rights prior to providing access to a data dictionary's objects. The second part involves explicitly granting rights to those resources.

Use the following steps to configure DemoDictionary to check user rights. Granting rights is discussed later in this chapter:

Right-click the DemoDictionary connection in the Connection Repository and select Properties.

Select the Security tab to display the Security page of the Data Dictionary dialog box shown in Figure 4-5.

Enable both the Logins Required and Check User Rights checkboxes in the User Access section.

Click OK to accept the security changes and close the Data Dictionary dialog box.

When the Logins Required option is enabled, a client application must submit a user name, at a minimum, before it can connect to the data dictionary. If the supplied user name also has a password, that user's password must be submitted as well.

When the Check User Rights option is enabled, the data dictionary will provide the logged-in user with access only to those objects for which that user has specifically been granted rights. These rights can be granted directly to a user, or they may be granted to one or more of the groups to which the logged-in user belongs.

Whenever you enable Check User Rights, you should consider whether or not you want to employ groups. Groups simplify the process of granting user rights, as you will learn in the following section.