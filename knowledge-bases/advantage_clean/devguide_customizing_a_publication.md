---
title: Devguide Customizing A Publication
slug: devguide_customizing_a_publication
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_customizing_a_publication.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 0465e29663a8adb1985835033a0cdea259a0c366
---

# Devguide Customizing A Publication

Customizing a Publication

     Customizing a Publication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Customizing a Publication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If you need to make an adjustment to a publication, such as adding or removing tables, or adjusting which fields are used to identify the corresponding record on the target data dictionary, you use the Publication dialog box. You also use this dialog box to create publication filters, which are a feature that you cannot add from the Advantage Publication Wizard.

To display the Publication dialog box, expand the PUBLICATIONS node in the active Administrative connection for your data dictionary. Right-click the publication whose properties you want to adjust and select Properties from the displayed context menu. (Alternatively, you can double-click on the publication.) The Advantage Data Architect responds by displaying the Publication dialog box shown in Figure 10-9.

Figure 10-9: The General page of the Publication dialog box

You use the General page of this dialog box to add and remove articles (tables), as well as to configure how destination records are located and which fields to replicate.

To add a table to the publication, click the New Article button. You use the displayed dialog box to choose a table from your data dictionary that is not already part of the publication. To remove a table from the publication, select the table name in the Articles list and click Delete Article.

You use the Row Identifiers list to adjust which fields are used to located corresponding records on the target database. If you refer back to Figure 10-6, you will see that the publication used the primary indexes of the CUSTOMER and EMPLOYEE tables, but selected all fields for all remaining tables. If you inspect Figure 10-9, you will notice that CUST\_BAK is selected, and all of its fields (except for Notes, a BLOB field) are checked in the Row Identifiers list. BLOB fields (including memo fields) cannot be used to uniquely identify records.

If prior to creating this publication you had set Customer ID to be the primary key for the CUST\_BAK table, only Customer ID would be checked. You can correct this now by removing the checkmarks from the checkboxes for all other fields except for Customer ID. By selecting each table in the Articles list in turn, you can inspect, verify, and adjust which fields the publication will use for identifying corresponding records on the destination database.

If you wish to replicate only selected columns, use either the Include Column or Exclude Column checkboxes to identify those fields whose values should be replicated. Checkmark each field you want to include or exclude (use Include or Exclude, but not both). To check or clear all checks in a column, right-click the column and select Include/Exclude All or Clear All.

You use the Filter field on this dialog box to define conditional replication. With conditional replication, only those records that meet the criteria you specify get replicated.

A filter is a Boolean expression, and whatever you enter into the Filter field of the Publication dialog box applies to the table in the Articles list that is currently selected. During replication, when the value of a filter evaluates to True for the affected source database record, that record will be replicated to the target defined by the corresponding subscription.

The Boolean expressions used by filters can include any expressions supported by the Advantage Expression Engine. These include table fields, comparison operators, literal values, and functions of the Advantage Expression Engine.

Filters are most often used in hub and spoke replication scenarios in order to replicate changes from the hub to a single spoke. In a situation like this, the hub data dictionary would have one publication and subscription for each spoke. Each of these publications would include a filter for those tables where data needs only be replicated to the corresponding spoke.

You can also use the Description page to update the description of your publication. When you are done customizing your publication, click OK to save your changes and close the Publication dialog box. If you want to close this dialog box without saving any of your changes, click Cancel.
