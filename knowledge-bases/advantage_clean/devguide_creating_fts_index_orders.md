---
title: Devguide Creating Fts Index Orders
slug: devguide_creating_fts_index_orders
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_fts_index_orders.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 0910c8968189ae6bc1c940785318cb77f6881dd9
---

# Devguide Creating Fts Index Orders

Creating FTS Index Orders

     Creating FTS Index Orders

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating FTS Index Orders  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create FTS index orders using the Full Text Search Index Definitions page of the Table Designer dialog box. This section demonstrates how to create FTS index orders, by walking you through the process of creating an FTS index on a table. In order for this process to be meaningful, it is best if the table on which you are creating the FTS has either a large text field or a memo field. And although the simple CUST.ADT table that you have been working with up to this point does have a comment field of type MEMO, that field contains very little data.

The following steps makes use of one of the free tables located on the sample code download associated with this book.

   
CODE DOWNLOAD: Before you continue, you should copy the tables in the sample database from the code download to a directory on your computer's hard drive. See Appendix A for a description of these files, including how to download these files.  
 

Use the following steps to demonstrate the creation of an FTS index:

Select File | Open Table. Set Path to the directory into which you copied the sample ADT tables for this book (for example, C:\AdsBook), and set Files to CUSTOMER.ADT. The CUSTOMER.ADT table will be opened in Table Browser, as shown in Figure 3-6.

Figure 3-6: The CUSTOMER.ADT table opened in the Table Browser

Right-click the Table Browser and select Properties from the displayed context menu.

Select the Full Text Search Index Definitions tab on the Table Designer. The Full Text Search Index Definitions page is displayed, as shown in Figure 3-7.

Figure 3-7: The Full Text Search Index Definitions page of the Table Designer dialog box

You use the options on the Full Text Search Index Definitions page of the Table Designer dialog box to add, change, and remove FTS indexes. Create a new FTS index by clicking the Add Index button.

In the field in the FTS Index Names list, enter Notes. (For the first FTS index you add, you could also enter the index name in the FTS Index Names field without first clicking the Add Index button. You do use the Add Index button to add additional FTS indexes.)

From the FTS Index Properties list on the right, set Key Field to Notes. In some cases, not all FTS index properties are visible in the FTS Index Properties pane. In those cases, use the scroll bar on the FTS Index Properties pane to view those additional properties.

Leave all other options set to their defaults. How these FTS index options affect your FTS index order is discussed later in this section. Click OK to create your new FTS index.

Now that you have created your FTS index, you are ready to test it.
