---
title: Devguide Creating Ads Tables
slug: devguide_creating_ads_tables
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_ads_tables.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2fcea766cc99b19ba5a16e8ab28d378d60081bff
---

# Devguide Creating Ads Tables

Creating ADS Tables

 

     Creating ADS Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating ADS Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are a number of ways that you can create tables for use by Advantage. At runtime you can execute a CREATE TABLE SQL statement. Alternatively, if you are using either the Advantage TDataSet Descendant or the ACE (Advantage Client Engine) API, you can invoke AdsCreateTable.

The most convenient way to create an Advantage table at design time is to use the Table Designer dialog box of the Advantage Data Architect. Actually, since you can execute SQL statements in the Advantage Data Architect, you can also create a table by executing a CREATE TABLE statement. However, the Table Designer dialog box provides a GUI (graphical user interface) that makes it far easier to use than SQL, which requires you to manually code a SQL statement.

   
NOTE: If your table already exists in another database format, the Advantage Data Architect provides you with an import facility that permits you to import a wide range of table types into the ADT format. Using the import feature of Advantage Data Architect is described later in this chapter.  
 

The following steps demonstrate how to create a new ADT table using the Table Designer dialog box:

1.        Launch the Advantage Data Architect if it is not already running.

| 2. | Open the FreeTableConnection connection in the Connection Repository, if necessary. (It may already be open and display FreeTableConnection at Active Connection in the Advantage Data Architect toolbar. If it is not, double-click on FreeTableConnection to connect it.) This is the connection that you created using steps described in Chapter 1, Creating a Connection. If you did not create the FreeTableConnection connection yet, use the steps provided in Chapter 1 to create it now. |

| 3. | Right-click the TABLES node of the FreeTableConnection connection in the Connection Repository and select Create. The Table Designer is displayed, as shown in Figure 2-1. |

Figure 2-1: The Table Designer

4.        Leave the Table Type dropdown menu set to Advantage (ADT). The Table Designer is now ready for the first field definition of your table's structure. At a minimum, you create a table's structure by adding a new field and entering its field name. You do this for each field you want in the table's structure. Once you enter the name of a field in the Field Names list and press Enter, the available properties of your newly entered field appear in the Field Properties list. Here is where you select the Field Type from the available dropdown list. The available field types for ADT tables are shown in Table 2-2.

| 5. | Use the information in Table 2-3 to define the structure of your new table. Type the name of the first field listed in Table 2-3 and press Tab. |

| 6. | Now set the Data Type property of the first field to shortint and press Enter. |

| 7. | Click Add Field to create the next field. Repeat this process until you have defined all fields shown in Table 2-3.   Field numbers indicating the position of each field in the table's structure appear as you add fields. This number is for reference. If you accidentally add a field in the wrong order, you can drag the misplaced field to a different position in the Field Names list. |
