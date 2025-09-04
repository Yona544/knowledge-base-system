---
title: Ade Task 1 Perform Data Conversion Using The Advantage Data Architect
slug: ade_task_1_perform_data_conversion_using_the_advantage_data_architect
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_task_1_perform_data_conversion_using_the_advantage_data_architect.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3535618d8268a614f564a86fc59247d9b330b657
---

# Ade Task 1 Perform Data Conversion Using The Advantage Data Architect

Task 1: Perform Data Conversion Using the Advantage Data Architect

Task 1: Perform Data Conversion Using the Advantage Data Architect

Advantage TDataSet Descendant

| Task 1: Perform Data Conversion Using the Advantage Data Architect  Advantage TDataSet Descendant |  |  |  |  |

The first task in creating this sample application is to convert a paradox table to an Advantage Database Table (ADT table). It is possible to write your own Delphi application for this purpose, but you will most likely find it easier to use the [Advantage Data Architect](ade_advantage_data_architect.md).

- Close Delphi if it is currently running.

- Create a new data directory to store your Advantage files. For this example we will use X:\ADS\DATA.

- Open Data Architect.

- Select Connection, Create New Connection from the main menu.

- In the ConnectionPath property, enter the path you created in Step 1.

- In the DatabaseName property enter a name for this new connection.

- Click the OK button.

- Choose Import Data from the Tools menu.

- From the Import Data Type combo box, select Paradox, / dBASE.

- In the source file name edit box, enter the path to your data, or click the browse button to search. By default Delphi installs demo data to C:\PROGRAM FILES\COMMON FILES\BORLAND SHARED\DATA. We will convert all of the demo tables to the Advantage file format for this example, so use C:\PROGRAM FILES\COMMON FILES\BORLAND SHARED\DATA\\*.DB\*.

Note If you cannot find the data directory, reference your Delphi installation documentation for details on how to re-install with this option. There is also the possibility that you will already have the files from a previous Delphi 1 installation, in this case the default directory is C:\DELPHI\DEMOS\DATA.

- Click the Next button.

- Enter the destination alias. This should be the connection name that references the directory you created in Step 2 above. This is where all of your new Advantage tables will be created.

- Click the Next button to begin the data conversion.

- When the conversion is finished, click Close and exit Advantage Data Architect.

Note You will encounter a Paradox Import Note when converting Paradox tables that have primary indexes defined. By default, the PRIMARY index is not the default index with an Advantage application. The PRIMARY index can be set as the default index in the Advantage Data Dictionary or otherwise; the PRIMARY indexes will need to be explicitly activated in your application. Click OK to continue.
