---
title: Devguide The Sql Utility
slug: devguide_the_sql_utility
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_sql_utility.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 3b654aaddcfabf1b53d67bf01eb0efada6b5cfb2
---

# Devguide The Sql Utility

The SQL Utility

     The SQL Utility

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The SQL Utility  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The SQL Utility, shown in Figure11-1, is a valuable tool for testing SQL statements. To display the SQL Utility for your currently active connection, select Tools | SQL Utility from the Advantage Data Architect main menu. Alternatively, click the Test Queries button from the Advantage Data Architect toolbar to open the SQL Utility for your current active connection.

Figure 11-1: The SQL Utility

If you attempt to open the SQL Utility without an active connection, the Choose a Connection dialog box shown here is displayed:

Select a connection and click OK. If the selected connection requires a password, you will be asked to enter it before the SQL Utility opens.

You use the SQL Utility by entering one or more SQL statements into the SQL pane (in the top section), and then clicking the Execute Query button in the SQL Utilities toolbar. (Pressing F5 also executes the SQL in the SQL pane.)

   
TIP: If you accidentally erase one or more lines of code while editing your SQL in the SQL pane, or make some other similar mistake, press Ctrl-Z one or more times to undo your last edit(s).   
 

You can execute a subset of text in the SQL pane by highlighting the text you want to execute before clicking the Execute button (or pressing F5). If your SQL statement or statements produce a result set, the returned records are shown in the Data page, shown in Figure 11-2.

Figure 11-2: The Data page of the SQL Utility

   
TIP: If you want to save the data from a result set returned by a query, you can right-click the Data page of the SQL Utility and select Export to New Table, Export to Existing Table, or Export to Excel, HTML. Exporting is discussed in Chapter 2.  
 

You can view information about the executed statement or script by selecting the Messages tab to display the Messages page. If you execute a query that does not return a result set, the Messages page is displayed by default. The Messages page of the SQL Utility is shown in Figure 11-3.

Figure 11-3: The Message page of the SQL Utility

If your query or script returns a result set, both the Messages and Data tabs appear in the SQL Utility. If your query or script does not return a result set, only the Message tab is visible.

Additional information about the query appears in the status bar of the SQL Utility. As you can see from Figure 11-3, the associated DELETE statement took 62 milliseconds to complete

If a SQL query takes more than two seconds to complete, a progress bar showing the progress of the query execution is displayed. Click Cancel SQL if you want to cancel the execution of a query in progress. This is useful for a query that is taking a long time to execute and either you do not want to wait for it to finish execution, or you suspect that something is wrong with the query even though it is syntactically correct.

The toolbar buttons in the SQL Utility provide a number of additional features. The New SQL Script button gives you a fresh SQL pane. Use the Open SQL Script button to load a previously saved text file containing SQL, while the Save SQL Script button permits you to save the current contents of the SQL pane to disk.

You use the Cut, Copy, and Paste buttons to perform these actions on the text with the SQL pane, and the Clear All button erases the contents of the SQL pane.

The Verify SQL button (F7) performs a syntax check on the contents of the SQL pane (or the highlighted text), while the Execute Query button (F5) executes the contents of the SQL pane or of the highlighted text.

The Cancel Query button (Shift F5) permits you to cancel a query that is currently executing, and the Show Plan button displays the execution plan for the SQL statements in the SQL pane (or the highlighted SQL statements). If the SQL pane (or highlighted text) contains a SQL script, the Show Plan button shows the execution plan for the last SELECT statement. Execution plans are discussed later in this section.

If you are connected to a remote server, you will also find the Begin Transaction, Commit Transaction, and Rollback Transaction buttons on the toolbar. These buttons permit you to control transactions on the statements in the SQL pane (although you can also do so with transaction-related SQL statements that you enter in the SQL pane).

The SQL pane also has a context menu, which you view by right-clicking the SQL pane. The SQL pane context menu contains the same items as the SQL main menu item of the Advantage Data Architect, which is only visible when a SQL Utility window is the active window in the Advantage Data Architect. Two items on these menus, Parameters and Link Manager, do not appear on the SQL Utility's toolbar.

Select Parameters from the SQL pane context menu to display the Query Parameters dialog box, shown here:

If the SQL in the SQL pane (or the highlighted SQL) contains one or more parameters, you use the Query Parameters dialog box to assign data to these parameters before executing the SQL. This feature permits you to test parameterized queries and stored procedures (executed using the EXECUTE PROCEDURE SQL statement).

You use the Link Manager menu item from the SQL pane context menu to display the Active Links dialog box. You use this dialog box to define temporary links to other data dictionaries for the purpose of testing SQL that uses data from two or more data dictionaries. The Active Links dialog box is discussed in detail in Chapter 4.

When you are through testing queries using the SQL Utility, click the Close icon in the upper-right corner of the SQL Utility window to close it.

   
NOTE: You can have two or more SQL Utility windows open at the same time. These can be connected to a common connection or to different connections, depending on your needs.
