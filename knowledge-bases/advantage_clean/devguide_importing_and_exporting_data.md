---
title: Devguide Importing And Exporting Data
slug: devguide_importing_and_exporting_data
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_importing_and_exporting_data.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: e338bf7eafa7646ee13264ce6867f1c4432356e2
---

# Devguide Importing And Exporting Data

Importing and Exporting Data

     Importing and Exporting Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Importing and Exporting Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Earlier in this chapter you learned how to create a table from scratch. But that is not always necessary if your data already exists. For example, if you are converting an old Paradox table (or any other of the many supported formats) to Advantage, you can import your existing data, creating an ADT table with a structure based on the existing table. The newly created table will be populated with the data from the existing table.

Data can go the other way, as well. The Advantage Data Architect permits you to export data to a wide variety of formats. This permits you to share your data with other applications. For example, you can export data from an Advantage table to an Excel spreadsheet, permitting you to use the business graphing capabilities of Excel to create a pie chart, a bar chart, or whatever kind of chart is suitable for your data. Alternatively, you can export your data in HTML format, permitting you to easily publish it to a World Wide Web site.

The following sections describe how to import and export data using the Advantage Data Architect. This discussion begins with importing.

Importing Data into ADS Tables

When you import data, you are making a copy of an existing data source, placing that copy into one or more ADT tables. Whether you get one or more tables depends on what you import. If you are importing a Microsoft Access database (an MDB file), you will end up with one ADT table for each table in the Access database. By comparison, if you are importing from Paradox or dBase tables, you will get one ADT table for each Paradox or dBase table you select to import.

The Advantage Data Architect permits you to import data using a wide variety of data access mechanisms. One of the most flexible involves OLE DB/ADO (ActiveX Data Objects), which you can use if you have the necessary OLE DB provider. This solution is flexible since most Windows databases have an OLE DB provider. There are also mechanisms to import Paradox tables, xBASE tables, and Pervasive SQL (Btrieve) tables, and to import both fixed-length and CSV (comma-separated value) text files.

   
NOTE: If you have an ODBC driver for a data format that you want to import, you can import that data using Microsoft's OLE DB Provider for ODBC.  
 

Before you import data, you should decide whether you want to import your data as free tables or into a data dictionary. If you want to import your data into a new data dictionary, you must create that data dictionary before you start.

You initiate the import process by selecting Tools | Import Data from the Advantage Data Architect's main menu. The Advantage Data Architect responds by displaying the Advantage Data Import Wizard dialog box shown in Figure 2-8.

Figure 2-8: The Advantage Data Import Wizard

The Advantage Data Import Wizard walks you through the process of importing data. It begins by asking you to select which import mechanism you want to use to import the data. Use the Import Data Type combo box to select which of the available import options you want to use.

Depending on the data import mechanism you choose, you are provided with a means of identifying the data you want to import. For example, if you select to use an OLE DB Provider (the OLE DB/ADO Data Source option), the Advantage Data Import Wizard provides you with a field to enter a connection string, along with a Build button that invokes the Data Link Properties Editor, which assists you with the building of the connection string.

By comparison, if you select to import Paradox/dBase data, you will be asked to select the file (or files) that you want to import. A Browse button permits you to select the directory and table you want to import. To import more than one table using the Browse button, use the browser to select a single table from the directory from which you want to import, and click OK. Then, in File Name field of the Advantage Data Import Wizard, change that table name to a wildcard pattern, such as \*.db, to indicate the multiple tables that you want to import.

Once you select the mechanism you want to use to import the data, indicate the data you want to import (through connection strings, BDE aliases, filename wildcard patterns, and so forth), and specify any other options presented by the Advantage Data Import Wizard, click the Next button to advance to the Select Destination page of the Advantage Data Import Wizard, shown in Figure 2-9.

Figure 2-9: The Select Destination page of the Advantage Data Import Wizard

You use the Select Destination page to select the connection to which you want to import the tables. If you select a free table connection, your ADT tables will be imported as free tables. Select a data dictionary connection to bind the imported tables to an existing data dictionary. If you select a data dictionary connection as the destination, the Advantage Data Import Wizard will prompt you for a user name and a password that has create privileges for the data dictionary.

The Select Destination page of the Advantage Data Import Wizard also provides you with a button to create a new connection. Use this button to create a new free table or create a new connection to an existing data dictionary. Once you select the connection to which you want to import your data, click Finish to begin importing (or click Cancel to exit without importing the selected data).

During importation, the Advantage Data Import Wizard displays its progress by listing the operations it is performing. In some cases, when importation is complete the Advantage Data Import Wizard will display a dialog box with information about the imported data. After accepting this dialog box, if displayed, the Advantage Data Import Wizard will look something like that in Figure 2-10. Here you will find the complete log of the importation. This log appears in a memo field. If you like, you can select the contents of this memo field, copy it to the clipboard, and then paste it into a text document that you then save. This is useful if you want to maintain a record of the importation results.

Figure 2-10: When importation is complete, a record of the importation is displayed

Exporting Data from ADS Tables

The Advantage Data Architect permits you to export data from Advantage tables using either the Table Browser or the SQL Utility. Using the Table Browser, you can either export the entire table's contents, or you can set either a scope (an index-based range) or a filter (a Boolean selection expression) to export only a subset of records from the table. Using the SQL Utility, you can execute a SQL SELECT statement to select some or all records and columns from a table (or view or stored procedure), and then export only the selected data. Only by using the SQL Utility can you export fewer than all columns of your data.

   
NOTE: While the preceding description is technically true, when you open a view, the results are displayed in the Table Browser. Consequently, if the view retrieves fewer than all columns of a table, the Table Browser for a view will export only that subset of columns. See Chapter 6 for information on views.  
 

Whether you use the Table Browser or the SQL Utility, there are three general categories of export options. The first is to export your data to another, new ADT table, and the second is to export your data to an existing ADT table. If you want to export to an existing ADT table, the existing table must have a structure that is compatible with the table from which you are exporting. These first two export options make it easy to copy and append data, but are not necessarily useful if you want to make your data available to other programs.

The third export option is to export to a non-ADS format. This export option permits you to export your data into a variety of useful formats, including Excel, comma-delimited text, tab-delimited text, HTML, and MS Word, among others. Most applications that you might want to use your data with will likely support at least one of the export format options provided for by this feature.

Use the following steps to demonstrate the export feature of the Advantage Data Architect:

If the FreeTableConnection connection is not open, click the '+' symbol next to this connection. This will also make this connection the active connection. If it is already open, make sure it is the current connection. (The current connection name appears in the Active Connection section of the toolbar of the Advantage Data Architect.) If you have more than one connected connection, click the FreeTableConnection to make it the active connection.

Select Tools | SQL Utility from the Advantage Data Architect main menu.

Enter the following SQL statement into the SQL editor (the multiline edit at the top of the SQL Utility):

SELECT "First Name", "Last Name", "Date Account Opened"  
  FROM CUST WHERE "Customer ID" = 12688

If there are already other SQL statements in the SQL Editor, highlight the preceding SQL statement. When you highlight one or more SQL statements in the SQL Editor of the SQL Utility, only those highlighted statements are executed. Otherwise, all SQL statements in the SQL Editor are executed.

Click the Execute button in the SQL Utility's toolbar. This is the button that displays the green, right-arrow icon. (If, after the query's execution, there are no records in the returned result set, check your SQL statement. If it is correct, verify that the Customer ID in the first record of the CUST table matches the WHERE clause of your SQL statement. Make corrections and execute the query again.)

Right-click in the Results pane (the area at the bottom of the SQL Utility that displays the query results when the Data tab at the bottom is selected) to display a popup menu with the following three options for exporting the result set: Export to New Table, Export to Existing Table, Export to HTML, Excel, , Select Export to HTML, Excel,. The SQL Utility shown in Figure 2-11 is displayed.

Figure 2-11: The Export Items dialog box

Select Comma-Delimited Text (CSV) from the Export Format dropdown list, and set the Export to File option. Uncheck the options under Options. Click OK.

You will now see a browser window that you can use to provide the filename and directory to which to export the data. Use this browser to navigate to the directory where your CUST.ADT table is stored, and enter CUST.CSV for the File Name. Click Save.

Now use Windows Notepad, or any other text file viewer, to open the CUST.CSV file you just exported. This file should look like that shown here:

Close this window or viewer. Also, close the SQL Utility window when you are done.

The preceding example demonstrated how to export specific rows and columns from an existing Advantage table using the SQL Utility. To export using the Table Browser, set a scope or a filter if you want to export fewer than all rows of data, and then right-click the Table Browser. Select the export option that you want from the context menu, and then proceed as you did with the SQL Utility.
