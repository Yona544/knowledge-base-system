---
title: Devguide Making Views Accessible
slug: devguide_making_views_accessible
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_making_views_accessible.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 8c79d30434dac1f3be3158475b82724cb0513ee7
---

# Devguide Making Views Accessible

Making Views Accessible

     Making Views Accessible

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Making Views Accessible  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As described in Chapter 4, it is possible to restrict access of groups and specific users to data dictionary objects. Doing so provides you with additional security in your database.

If you followed the steps in Chapter 4 to enable security for your data dictionary, the view that you just created is accessible to the data dictionary administrator, but not to any of your defined users. Specifically, since the DemoDictionary connection was configured to use the data dictionary administrator's user name when you opened the SQL Utility, you were permitted to execute a query against the view. However, if you created an alternative connection using an alternative user name, an exception would have been raised when you attempted to query the view.

Use the following steps to demonstrate this:

Select Connection | Create New Connection from the Advantage Data Architect's main menu.

From the Connection Path property of the Connection Properties dialog box, select Browse for Dictionary File from the dropdown menu. Use the displayed browser to select DemoDictionary.ADD.

At DatabaseName, enter AdsUserConnection, and set Username to adsuser.

Ensure that ServerType is set to the same value as the DemoDictionary connection, which should be remote.

Leave the remaining properties set to their default values. Your Connection Properties dialog box should look something like the one shown in Figure 6-4.

Figure 6-4: The Connection Properties dialog box

Click OK to close the Connection Properties dialog box and create the new connection.

The Advantage Data Architect will now attempt to open the connection. When prompted for a password, enter password and click OK.

Make sure that your new connection is connected (Active Connection will show ADSUSERCONNECTION to the right of the Advantage Data Architect toolbar).

Attempt to expand the VIEWS node. No views can be seen.

Select Tools | SQL Utility to open the SQL Utility for this connection. Your last query may still be visible in the SQL pane, depending on your configuration. If not, reenter the following SQL statement. Then, click Execute:

SELECT \* FROM [Employee Tab]

This time you will get the error shown in Figure 6-5. This error indicates that the user (adsuser) does not have rights to the view.

Close the SQL Utility.

Figure 6-5: An error occurs if you attempt to query a view to which you do not have the necessary rights

In order to provide access to views to regular users (users other than ADSSYS), you must either explicitly grant the users rights to the view or grant rights to the view to the one or more groups to which the users belong. (This is necessary in this case since DemoDictionary is configured to check user rights to data dictionary objects. When your Advantage application does not need to check user rights, do not enable the Check User Rights option on the Security page of the Data Dictionary dialog box, after which you no longer have to explicitly grant rights to new objects you create in the data dictionary.)

The following steps show you how to add access rights to the Employee Tab view:

Select the DemoDictionary connection in the Connection Repository to make it the current connection.

Expand the GROUPS node, if it is not already expanded.

Right-click the ReadWrite group (the steps to create this group were given in Chapter 4) and select Properties from the displayed context menu. The Advantage Data Architect displays the Group dialog box.

Click the Permissions button on the Group dialog box to display the Permissions dialog box.

Select View from the provided combo box.

Check Select, Update, Insert, and Delete for the Employee Tab view, as shown in Figure 6-6. (Click once in each checkbox to place a checkmark.)

Figure 6-6: The Permissions dialog box

Click OK to close the Permissions dialog box, and then click OK once more to close the Group dialog box and save the updated privileges.

Select the AdsUserConnection connection again and open the SQL Utility.

Your previous SQL statement should still be in the SQL pane. Click Execute to execute this query.

Since adsuser has select rights to the Employee Tab view (inherited from the ReadWrite group to which this user belongs), the query executes successfully this time. Your screen should look something like that shown in Figure 6-7.

Close the SQL Utility.

Right-click the AdsUserConnection connection and select Disconnect.

Select the DemoDictionary connection to make it active.

Figure 6-7: The adsuser now has sufficient rights to the Employee Tab view
