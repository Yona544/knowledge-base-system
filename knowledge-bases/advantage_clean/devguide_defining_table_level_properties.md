---
title: Devguide Defining Table Level Properties
slug: devguide_defining_table_level_properties
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_defining_table_level_properties.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 30717887b19a38c46ee75f95527537b2ddb0c23c
---

# Devguide Defining Table Level Properties

Defining Table-Level Properties

     Defining Table-Level Properties

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Defining Table-Level Properties  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You define a table's table-level properties from the Table Properties page of the Table Designer. The CUSTOMER table's properties are shown in Figure 5-4.

Figure 5-4: The Table Properties page of the Table Designer

The Table Properties page includes all properties that apply to the entire table. These properties control auto creation, index designations, encryption and security, memo block size, trigger availability, description, and record-level constraints. Each of these features is described in the following sections.

   
NOTE: Table properties only apply to dictionary-bound tables. Consequently, the Table Designer for a free table does not include the Table Properties tab.  
 

Enabling Automatic Table Creation

When Auto Create is set to On, the data dictionary uses information it stores about the table's metadata and indexes to re-create the table and all of its indexes at runtime if the table is not found when a client application attempts to open the table. This is a particularly useful feature for developers who distribute empty databases. For these developers, they can deploy only the data dictionary, permitting the tables and indexes to be created on-the-fly when needed.

In addition, if a table exists but its index files do not, setting Auto Create to On causes index files to be auto-created when that table is opened by the client application as long as the indexes were previously included in the data dictionary definition.

   
NOTE: ADS writes an error 5168 to the error log file whenever a table or index is auto-created. The client application never sees an error message, however, since this is an informational error and is only written to the log file to let the developer know that auto-creation has occurred.  
 

Default and Primary Indexes

The Table Properties dialog box also permits you to designate primary and default indexes. The primary index definition is used by Advantage to create referential integrity constraints. A primary index must be a unique index. More will be said about primary indexes later in this chapter.

A default index, when accessed using the Advantage TDataSet Descendant or the Advantage OLE DB Provider (when using ADO and opening a table directly using adCmdTableDirect), is the index order that a table will make active by default. In other words, if you have not specifically set an active index, the default index order (if designated) will be used. If you do not select a default index, a table that has no active index is displayed in its natural order.

Table Encryption and Permissions

In Chapter 2 you learned how to encrypt and decrypt a table from the TABLES node in the Connection Repository. You can also control table encryption from the Table Properties page of the Table Designer. Use the Encrypted property to enable or disable table encryption.

As is the case with all dictionary-bound tables, all tables in a common dictionary are encrypted with the same password. This password is defined from the Security page of the Data Dictionary dialog box.

You use Permissions Level to control how Advantage handles client requests for fields for which the client does not have rights. Field-level access privileges and permissions levels are discussed in Chapter 4.

Memo Block Size

The Memo Block Size property permits you to explicitly set the block size for a table's memo file. If you leave Memo Block Size blank, the default memo block size for that particular table type is used.

To choose a custom memo block size, set Memo Block Size to the size of the number of bytes you want in each memo block. Refer to the Advantage help for a detailed discussion of memo block sizes for the various types of tables Advantage supports.

Disabling Triggers

Use the Triggers Disabled property to specifically disable all triggers for a single table. This feature was introduced in Advantage 8 to permit triggers to be temporarily disabled during maintenance or large batch operations. Triggers should be re-enabled as soon as the maintenance or batch operation is completed.

Table Description

Like individual field descriptions, the Description property on the Table Properties page permits you to enter a description of the table. This description can be used within an application to provide data dictionarydriven help for your applications.

Table descriptions can be read from the system.tables system table. The following parameterized query demonstrates how you can retrieve the description for a particular table at runtime:

SELECT [Comment] FROM system.tables WHERE [Name] = :Table

Record-Level Constraints

Record-level constraints are defined using a Boolean expression. This expression can include field references, constants, comparison operators, and functions available from the Advantage expression engine. This expression is evaluated each time a record is inserted or updated in a table. If the validation expression evaluates to a Boolean False, an error is generated and the record is rejected.

Once the record-level constraint has been applied, if you attempt to post a record that violates a record-level constraint to the table, Advantage will generate a 5150 error that will look something like the following:

This particular error is the one that is generated if you do not specify a validation message. If you do specify a validation message, your custom message appears in the error along with the error code. For example, if your validation message is "When payment type is check, a check number must be supplied," the error will look like the following:

Record-Level Constraint Example

Use the following steps to add a record-level constraint to the PRODUCTS table:

Open the Table Designer for the PRODUCTS table.

Select the Table Properties tab to view the Table Properties page of the Table Designer.

At Validation Expression, enter the following value:

NOT ((Product Name = NULL) AND (Description = NULL))

At Validation Message, enter You must supply a value for either the Product Name or Description field (or both).

Click OK to close the Table Designer and apply the new constraint.

Since no data in the PRODUCTS table violated the constraints, the constraint is applied without removing records from the PRODUCTS table. If one or more records did violate this new constraint, the offending records would have been removed from the PRODUCTS table and displayed in a dialog box similar to the one shown in Figure 5-2.

When records are removed due to record-level constraints, your available options are the same as when records are removed due to field-level constraints. You can either fix the records you want to keep and select Save to return them to the original table, you can export the records to a new or existing table, or you can discard them.
