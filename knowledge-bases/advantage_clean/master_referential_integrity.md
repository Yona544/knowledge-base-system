---
title: Master Referential Integrity
slug: master_referential_integrity
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_referential_integrity.htm
source: Advantage CHM
tags:
  - master
checksum: 09afb4a12b542c1178b636440622af5b4789e940
---

# Master Referential Integrity

Referential Integrity

Referential Integrity

Advantage Concepts

| Referential Integrity  Advantage Concepts |  |  |  |  |

Referential Integrity (RI) is the means by which primary/foreign key relationships are enforced in a database. By specifying RI rules you can have the database guarantee, for example, that every sales representative is assigned to a valid office. Through the use of RI constraints, many business rules can be enforced by the database server, instead of your application.

The terms "primary key" and "foreign key" are used throughout this documentation.

- Primary Key - A unique identifier for a table. A column or column combination with the property that, at any given time, no two rows of the table contain the same value in that column or column combination.

- Foreign Key - A foreign key is a column or combination of columns whose values match the primary key of some other table. A foreign key does not have to be unique; in fact, foreign keys are often in a many-to-one relationship to a primary key. Foreign key values should be copies of the primary key values; no value in the foreign key except NULL should ever exist unless the same value exists in the primary key. A foreign key may be NULL; if any part of a composite foreign key is NULL, the entire foreign key is NULL.

Referential Integrity rules are stored in an Advantage Data Dictionary.

Note Referential Integrity is only supported with the Advantage proprietary tables and Visual FoxPro (VFP) tables. When using RI with VFP tables, you should add "!DELETED()" conditions to your primary and foreign keys. This will make sure that cascades are triggered when records are deleted. Without the !DELETED() clause, the key value will not change when the record is deleted, and RI operation will not be triggered.

Example

Lets look at a simple example using two tables: SALES\_REPS and OFFICES. The following SQL statement is syntactically correct, and with the current state of our example database this statement would execute and add a new sales rep, "Doug Henry", who works in office number 45:

INSERT INTO SALES\_REPS (EMPL\_NUM, NAME, REP\_OFFICE)

VALUES (69, Doug Henry, 45)

No validity checking has been enforced, and even if office number 45 does not exist in the OFFICES table, Doug Henry will still exist in our database.

To remedy this situation, well define one RI rule linking the OFFICES.OFFICE field (as the primary key) to the SALES\_REPS.REP\_OFFICE field (as the foreign key). With this rule in place, the previous SQL statement would not execute without returning an error. Before adding Doug to the SALES\_REPS table, the Advantage Database Server will first ensure that all foreign keys in this new row reference existing primary keys in their parent tables. Because office number 45 does not exist, the INSERT operation will fail. The application developer does not write any code to enforce this rule. The database server does all the work; the developer can simply catch this error, notify the user of the violation, and request correct data.

Update and Delete Rules

Referential Integrity allows update and delete rules to be specified for each relation you define. These rules affect the behavior of the Advantage Database Server when updating and deleting existing parent rows. There are four possible update/delete rules that can be performed:

Delete Rules

- RESTRICT - Prevents deletion of a row from a parent table if children of the row still exist in a child table. If applied to our example above, this would make it illegal to delete an office if any sales representatives were still assigned to the office.

- CASCADE - When a parent row is deleted, automatically delete all child rows. If applied to our example above, deleting an office would automatically delete every sales representative assigned to the office.

- SET\_NULL - When a parent row is deleted, automatically set all foreign key values to NULL. If applied to our example above, this would make deleting an office set every sales representatives office assignment to an unknown office. When using Visual FoxPro (VFP) tables, you should probably make sure that the foreign key field(s) can be NULL. If it does not have the NULL option, then the field(s) will be set to empty and the RI enforcement check will fail unless there is an empty parent key.

- SET\_DEFAULT - When a parent row is deleted, automatically set all foreign key values to their default values. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information on default field values. If applied to our example above, this rule would assign sales representatives to some default office if their office were ever removed. The default office is stored within the data dictionary and is the default field value for the office field.

Update Rules

- RESTRICT - Prevents updating a primary key if foreign key values still exist in a child table. If applied to our example above, this would make it illegal to change an office number if sales representatives were still assigned to the office.

- CASCADE - When a primary key is updated, automatically update all foreign key values. If applied to our example above, updating an office number would also update the REP\_OFFICE field for each sales representative currently assigned to the office.

- SET\_NULL - When a primary key is updated, automatically set all foreign key values to NULL. If applied to our example above, this would make updates to the office number set every sales representatives office assignment to an unknown office. When using Visual FoxPro (VFP) tables, you should probably make sure that the foreign key field(s) can be NULL. If it does not have the NULL option, then the field(s) will be set to empty and the RI enforcement check will fail unless there is an empty parent key.

- SET\_DEFAULT - When a primary key is updated, automatically set all foreign key values to their default values. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information on default field values. If applied to our example above, this rule would assign sales representatives to some default office if their office number were ever updated. The default office is stored within the data dictionary and is the default field value for the office field.

NULL Values

Advantage primary keys can contain one NULL value. Advantage foreign keys (as long as they are not defined with the unique index type) can contain multiple NULL values. NULL values in foreign keys are often a necessity when dealing with updates to a database that utilizes RI constraints to break a dependency between primary and foreign keys.

Behind The Scenes

If you have defined multiple RI rules in your database (a very likely scenario) it is important to keep in mind the operations that the server will be performing on your behalf. Tables involved in RI rules are grouped together into graphs. The server must have all tables in the graph open to enforce the RI rules that you have placed on the database.

For example, if your application is designed to use the example database described above, and opens the OFFICES table, no extra work will be done. But the first time you attempt an update operation on the OFFICES table, the server will also open the SALES\_REPS table in the background, to maintain your RI constraint.

How to Define RI Rules

There are three different ways to define and modify RI rules; Advantage Data Architect, TAdsDictionary component in the Advantage TDataSet Descendant, and Advantage Client Engine (ACE) API calls.

At design-time, the easiest way to define and view your database dictionary setup is through the Advantage Data Architect utility. See the Advantage Data Architect Help (ARC.HLP) for more information. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

If you would like run-time access to data dictionary information, and if you are using the Advantage TDataSet Descendant, see TAdsDictionary (see ADE.HLP). (Note that each of the Advantage products and their corresponding Help files are installed separately.)

Direct access to the Database Dictionary is also available through Advantage Data Dictionary API's (prefixed AdsDD, for example AdsDDCreateRefIntegrity) by accessing the Advantage Client Engine API directly.

Server Configuration

There is no additional server configuration related to the use of referential integrity. Note, though, that the Advantage Database Server will use more work areas when enforcing referential integrity rules. Also, cascading deletes may often need to acquire a large number of record locks (depending on the number of records affected by the cascade) before performing the actual cascade operation. Beginning with v9.0, Advantage will automatically increase the configuration sizes as necessary, so you should not need to adjust any parameters. For more information on configuration parameters, see [Advantage Database Server Configuration](master_advantage_database_server_configuration_overview.md).

Recommended Reading

Advantage Data Dictionary documentation

James R. Groff & Paul N. Weinberg Lan Times Guide to SQL. Berkeley, CA: Osborne McGraw-Hill

ISBN: 007882026X
