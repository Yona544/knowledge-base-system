---
title: Devguide Creating Indexes
slug: devguide_creating_indexes
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_indexes.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 3a87341da1415d18fee92b61765a326399012d81
---

# Devguide Creating Indexes

Creating Indexes

 

     Creating Indexes

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Just as you can create tables using several different approaches, you have a number of alternative ways to create indexes. At runtime, you can create indexes using SQL, and many of the Advantage data access mechanisms provide additional functions for index creation. At design time, it is easiest to use the Advantage Data Architect to add indexes to a table.

The following steps walk you through the process of creating indexes for the CUST.ADT table you created in Chapter 2. Several expression indexes and a conditional index are created in the following steps. Custom and subindexes are not recommended for most applications, so those types of indexes will not be created in this section. Creating FTS indexes is described later in this chapter.

Use the following steps to add four index orders to the table created in the section "Creating Advantage Tables" in Chapter 2:

Launch the Advantage Data Architect if it is not already running.

Open the CUST.ADT table that you created in Chapter 2 in the Table Browser.

Right-click the Table Browser and select Properties from the displayed context menu.

Select the Customer ID field from the Fields page of the Table Designer. Set Index to Unique. (Customer ID is a value that should be unique for each customer record. For fields that do not require uniqueness, set Index to Yes.)  
For single field index expressions, the Index property of a field provides the most convenient method for creating an index. For any other type of index, you will want to use the Additional Index Definitions page of the Table Designer.

Select the Additional Index Definitions tab to display the Additional Index Definitions page shown in Figure 3-1.   
You view, create, and manage expression indexes, including conditional and custom indexes, from the Additional Index Definitions page of the Table Designer. If expression indexes already exist for your table, they will appear in the Index Names list. Since you have not yet accepted changes to the Table Designer, the Customer ID index has not yet been created, which is why it doesn't appear in the Index Names list. Once you are through creating indexes and accept your changes, the Customer ID index will appear in the Index Names list of the Additional Index Definitions page of the Table Designer the next time you open it.

Figure 3-1: The Additional Index Definitions page of the Table Designer dialog box

Click the Add Index button to add a new index. For the Index Names field, enter Full Name. (Alternatively, you can simply enter a name into the index names column without clicking on the Add Index button, which works for the first index created on the table.) Next, set the Index Fields or Expression field to First Name + + Last Name. Leave all remaining properties set to field default values, including Index Filename, which will be set to the name of the table by default when you accept your changes in the Tables Designer.

Create another index by clicking the Add Index button again. Enter Active Customers as the Index Name. Use the dropdown list to set the Index Fields or Expression field to Active. Next, in the Condition Expression field, enter Active=True. Also, set the Descending property to Yes.

You are through adding indexes for now. Your two new indexes appear in the Index Names list. Click OK to close the Table Properties dialog box. Upon closing, the new indexes, including the Customer ID index, are created and are ready to use.

   
NOTE: If the Advantage Data Architect cannot obtain an exclusive lock on the table when you accept the Table Properties dialog box, an error will be displayed and your indexes will not be created. If you need to ensure that you can successfully add, change, or remove indexes from a table, open the table exclusively before accessing the Table Properties dialog box.  
 

To view the currently available indexes for a table, open the Additional Index Definitions page of the Table Properties dialog box. If you do this now for the CUST table, you should see the three indexes you just created as shown in Figure 3-2. To see the properties of an existing index, select the index of interest in the Index Names list to view its properties in the Index Properties list. If you want to remove an index, select that index from the Index Names list and click the Delete Index button. Click the Close icon to close this dialog box.

Figure 3-2: You can view, modify, and delete indexes using the Additional Index Definitions page of the Table Designer
