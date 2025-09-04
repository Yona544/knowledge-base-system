---
title: Devguide Opening A Previously Created Table
slug: devguide_opening_a_previously_created_table
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_opening_a_previously_created_table.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 743cba63a75ca0d4991da4ab3bb5303b398f0b29
---

# Devguide Opening A Previously Created Table

Opening a Previously Created Table

     Opening a Previously Created Table

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Opening a Previously Created Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

After you finish creating a table using the Table Designer, you are given the opportunity to open the newly created table in the Table Browser. This feature is useful if you immediately want to enter some data into the newly created table, or to perform some table-related task such as encrypting the table. Once you are through working with your table, close the Table Browser.

The Table Browser can also be used on tables that already exist. How you open an existing table depends on whether you have previously created a connection to the table directory (or have created a connection to the data dictionary to which the table is bound.)

Use the following step to open the CUST.ADT table using the FreeTableConnection connection:

If the FreeTableConnection is opened in the Connection Repository, expand the TABLES node of the FreeTableConnection node and then double-click the CUST.ADT table name. Alternatively, you can right-click the CUST.ADT node and select Open. This step opens a table in the Table Browser in a shared mode using the connection type (local, remote, or internet) associated with the connection in which the table appears. If the FreeTableConnection connection is not yet opened, open it, and then expand the TABLES node and double-click CUST.ADT or right-click the node and select Open.

As mentioned in the preceding step, opening a table in this fashion opens the table in a default mode, which includes opening the table as a shared table using the connection type defined by the connection. In this mode, if you make a change that requires exclusive access, such as encrypting or packing a table, the Data Architect tries to obtain exclusive access to the table in order to complete the task. However, if the table is in use by another user (or another application), the Advantage Data Architect will not be able to obtain the exclusive lock and you will not be able to complete your task.

For those occasions when you need to make changes to a table that require exclusive access, and it's possible that another user might want to use the table while you are performing this task, you can ensure that you will be able to complete your work by explicitly obtaining exclusive access before making your changes. You can do this by opening the table using advanced open.

The following steps demonstrate how to use advanced open to open the CUST.ADT table:

If your CUST.ADT table is already open in the Table Browser, first close it by clicking the Close button in the upper-right corner of the Table Browser window.

Select File | Open Table from the Advantage Data Architect main menu. The Advantage Data Architect responds by displaying the Open Table(s) dialog box.

Figure 2-4: The Open Table(s) dialog box

Select the Path radio button in the top portion of the Open Table(s) dialog box. The last path used is listed in the Path field as shown in Figure 2-4. If you want to specify a different path, either click the path Browse button and use the displayed Browse for Folder dialog box to select the directory into which you saved the CUST.ADT table you created in the preceding section of this chapter, or enter the path manually.

Click the file Browse button and then select CUST.ADT from the displayed dialog box. Click OK to return to the Open Table(s) dialog box.

You probably do not have to change any of the settings on the Open Table(s) dialog box, but for our purposes, make sure that Exclusive is checked in the Misc Options section, Table Type is set to Auto Sense, and that all three checkboxes are enabled in the Server Type section.

If you are opening a free table for editing, as you are in this instance, and there is more than one index for the table you are opening (which there is not in this case), you need to click the Additional Indexes button and choose all of the indexes that are associated with this table. Failure to do so will likely result in the corruption of those indexes that are not opened if you post changes to the table. This is only a problem with free tables, as a table's nonstructural indexes are automatically opened when you work with database tables. Click OK to open this table in the Table Browser, as shown in Figure 2-3.

Using this approach, it is not necessary to have a defined connection in order to open a table. Specifically, whether a table is a free table or a dictionary bound table, you can open it from the File menu of the Advantage Data Architect.

If the table resides in a directory (free table) or a data dictionary (database table) for which you already have a connection defined, open that connection in the Connection Repository, expand the TABLES node, right-click the table you want to open and select Advanced Open from the displayed context menu. The Open Table(s) dialog box will be displayed, as shown in Figure 2-4, but the Path and File(s) fields will already be filled in for the table you right-clicked. You cannot change these fields when you display the Open Table(s) dialog box this way since this is the table you are trying to open. You then use the remaining fields on this dialog box to control exactly how the table is opened.

   
TIP: You can open two or more tables at the same time from the Open Table(s) dialog box, as long as these tables are in the same directory or the same data dictionary. To open more than one table, Select File | Open Table to display the Open Table(s) dialog box, browse for files and hold down the Ctrl key and click the tables you want to open. With these tables listed in the File name field, click the Open button. Or, you can enter a semicolon-separated list of table names in the File(s) field to open two or more tables.  
 

Once you have opened a table in the Table Browser, the caption in the Table Browser title bar provides you with information about the table. In addition to the fully qualified filename of the table you opened, the type of table (ADT in this case) and the type of connection used to open the table (REMOTE in Figure 2-3) are displayed in brackets following the filename. After the brackets are parentheses, indicating the total number of connections that were currently viewing this table at the time the Table Browser was opened.
