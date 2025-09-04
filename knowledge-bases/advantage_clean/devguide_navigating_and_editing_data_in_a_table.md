---
title: Devguide Navigating And Editing Data In A Table
slug: devguide_navigating_and_editing_data_in_a_table
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_navigating_and_editing_data_in_a_table.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 278f95747f2bd230e7076cb4bb26596797c03ce7
---

# Devguide Navigating And Editing Data In A Table

Navigating and Editing Data in a Table

     Navigating and Editing Data in a Table

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Navigating and Editing Data in a Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You use the Table Browser to add, remove, and modify records in a table. For all basic data types, such as character, integer, logical, and date, you can simply navigate to the field whose data you want to change and enter or edit the data using your keyboard. The standard keyboard shortcuts allow you to cut (Ctrl-X), copy (Ctrl-C), and paste (Ctrl-V) data. For memo fields, you can enter data in the field, but it is easier to simply double-click the memo field to display a small editor window for data entry. Close this window when you are done changing the contents of the memo field. You can also double-click image fields to view their contents in a small editor window, although it displays a limited subset of the data. You can add, remove, and modify image data using the keyboard shortcuts.

Basic navigation is supplied by the navigator control (shown here) that appears in the lower-left corner of the Table Browser. The available navigator buttons, from left to right, perform the following tasks: Move to first record, Move backward one page, Move forward one page, Move to last record, Insert new record, Delete current or selected record(s), Edit current record, Post changes to current record, Cancel changes made to current record, and Refresh the contents of the current dataset. Pause your mouse pointer over one of the buttons of the navigator briefly to see a fly-by help window describing the purpose of that button.

   
NOTE: In addition to posting changes to a record using the Post changes button of the navigator, any changes that you made to a record are posted automatically if you then navigate to another record in the Table Browser.  
 

You can also navigate your table using the cursor keys on your keyboard. For example, Left Arrow, Right Arrow, Tab, and Shift-Tab permit you to navigate between columns on the current record. Similarly, Up Arrow, Down Arrow, Page Up, and Page Down permit you to scroll between records.

You can also navigate with your mouse. To select a particular record/column cell that is currently visible in the Table Browser, click on the cell. To navigate to a record that is not currently visible in the grid, click on the grid's scrollbar until the record you want is visible.

So long as you have not opened a table in exclusive mode, the Table Browser permits you to modify the contents of a table in a multiuser environment, meaning that other users could possibly be viewing and even editing this same table at the same time you are. When you open a table exclusively, you are the only one who can access the table until you release the exclusive lock by closing the table.

When a table is opened in shared mode, just as you begin editing a record, a record lock is placed on that record in order to coordinate the edits by multiple users. While this record lock is in place, other users will be able to view that record, but no other user can edit that same record until you have released the lock by posting your changes.

Use the following steps to demonstrate the editing of a table's contents:

With the new CUST table open in the Table Browser, move to the Customer ID field and enter 12688. For First Name enter Frank, and for Last Name enter Jones. Similarly, set Date Account Opened to 5/9/1983 and Active to T.

Click in the Comments field to display the text insert cursor. Now double-click this Comments field for this first record. The blank memo opens in a window like this:

Enter the following text into the memo window: Our first customer. Close the memo window when you are done.

Click the Post changes button on the navigator (the button with the checkmark). Notice that after the record is posted, the first few characters of the memo field's contents appear in the grid. This data does not appear until after you post the record.

With your cursor still on the first record in the table, press Down Arrow. Doing this opens a new record. Enter data for three more records using these same techniques. The data that you should enter can be found in Table 2-4. Once you have entered data for the last record, click the Post changes button or move to a different record to post the last record's data.
