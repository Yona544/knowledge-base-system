---
title: Master Advantage Data Dictionary
slug: master_advantage_data_dictionary
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_data_dictionary.htm
source: Advantage CHM
tags:
  - master
checksum: 544c9a5bff173b005b7653e0b574181aa347d932
---

# Master Advantage Data Dictionary

Advantage Data Dictionary

Advantage Data Dictionary

Advantage Concepts

| Advantage Data Dictionary  Advantage Concepts |  |  |  |  |

The Advantage Data Dictionary introduces additional features and functionality that compliment the [Advantage Database Server](master_advantage_database_server.md) and [Advantage Local Server](master_advantage_local_server.md). With the Advantage Data Dictionary, a database can be clearly defined with its associated tables and indexes. Access to the database tables) can be more securely guarded by the Advantage servers because users and user groups can be defined in the database and specific rights can be assigned to the users and user groups. The Advantage Data Dictionary allows the Advantage server to ensure the logical validity of the data in the database through the use of field level constraints, record level constraint, and referential integrity with ADT tables. The Advantage Data Dictionary also supports the use of stored procedures. Descriptions of the database, tables, fields, indexes, and default field values can be stored in the Advantage Data Dictionary to allow developers to develop and deploy applications more efficiently. Much of the Advantage Data Dictionary functionality is available to both ADT and DBF tables.

These features can be implemented programmatically using the Advantage Client Engine API. They can also be implemented interactively using the Advantage Data Architect (arc32.exe) included in the Advantage Product CD. The Advantage Data Architect utility can also be downloaded from the Downloads page on the Advantage Database Server Web site, < http://www.AdvantageDatabase.com>.

The following are brief overviews of the features supported by the Advantage Data Dictionary.

Referential Integrity

Referential Integrity (RI) is the means by which primary/foreign key relationships are enforced in a database. By specifying RI rules you can have the database guarantee, for example, that every sales representative is assigned to a valid office. Through the use of RI constraints, many business rules can be enforced by the database server, instead of your application. See [Referential Integrity](master_referential_integrity.md) for more information. Referential Integrity functionality is available with ADT and Visual FoxPro (VFP) tables only.

Default Field Values

Normally, when a new record is added to a table, the record is either filled with NULL values (ADT tables) or empty values (DBF tables) for each field. With a database table), default field values can be defined for the fields in a table so when a new record is added to the table, it can be filled with values other than all NULL/empty. An example is to automatically fill in the date of record creation. Note that default field values use [expression engine](master_advantage_expression_engine.md) functions, as opposed to SQL [scalar functions](master_supported_scalar_functions.md).

Field Level Constraints

Field level constraints can be used to ensure that the data entered for each individual field in a record is logically valid. For example, the price of an item for sale must not be negative. The field level constraints include the minimum/maximum allowed value for the field, whether the field can have NULL value, and the error message associated with the constraint verification. The field level constraints are checked when a record is modified. If any of the fields in the record fails the constraint, the update will not be posted to the database and the error messaged associated with the failed constraint can be retrieved.

This functionality was originally available to ADT tables only, but beginning with v9.0, it can be used with DBF table types as well. Note, though, that it is not possible to prevent DBF tables from being opened as free tables. If a DBF is opened outside the data dictionary, field level constraints will not be enforced.

Record Level Constraints

Record level constraints can be used to ensure that the data entered for related fields in a record is logically valid before posting the record to the database. For example, the price of an item for sale must be greater than the cost of the item. The record level constraints include a logical expression that defines the relationship between the fields in the record and the error message associated with the constraint verification. The record level constraint is checked when a record is modified. The update to the record is aborted if the record does not meet the constraint.

This functionality was originally available to ADT tables only, but beginning with v9.0, it can be used with DBF table types as well. Note, though, that it is not possible to prevent DBF tables from being opened as free tables. If a DBF is opened outside the data dictionary, record level constraints will not be enforced.

Flexible User Access Control

The data dictionary provides means to allow the administrator to set up a user account to control the access to the database tables), views, and stored procedures. To effectively guard against unauthorized access to the database, it is recommended that all database tables) be stored in a secured server directory that is only visible to the system process. With the database tables not visible to the user, the only way to access the tables will be through the Advantage Database Server and the Advantage Data Dictionary. The access control mechanism consists of two database properties: login requirement and access rights verification. By default, the database is created with no login required and no access rights verification. In this state, a user can connect to the database through the data dictionary with no user name and no password and have full access to all tables, views, and stored procedures. The next level of access control will be to require the user connecting to the database to enter a valid combination of user name and password. Once the user is authenticated, access to all tables, views, and stored procedures are granted. The next higher level will have both database properties set to TRUE. The user is verified when connecting to the data dictionary and the user access to an individual table, view, or stored procedure is also verified to make sure that proper rights have been granted to the user. The administrator will be responsible for setting up individual user access to the tables, views, or stored procedures. User groups can be defined in the database to ease the task of setting up users with similar access rights. Flexible User Access Control functionality is available with both ADT and DBF tables. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for additional specifics on granting and revoking a variety of permissions to users and [Database Roles](master_database_base_roles.md) for information on predefined user groups.

More Secure Encryption

Advantage servers and clients support table encryption using an industry standard 160-bit encryption algorithm by default. It is also possible to use [AES encryption](master_encryption.md) if desired. In addition to encrypting the data in the table, if the table is an ADT database table), the tables field headers are also encrypted. Individual database tables can be either completely encrypted or not encrypted. When using the default encryption, all encrypted database tables are encrypted with a single password that is stored in the database. When using AES encryption, encrypted tables and the dictionary files are encrypted with key data generated from the [dictionary password](master_se_passwords.md). The  table password for the default encryption can be set and changed by the data dictionary administrator before any database table is encrypted. The table encryption password is securely stored in the data dictionary and it is automatically available to the users who are properly authenticated by the Advantage server to access the database. In other words, there is no need for the end user or the application to remember the table encryption password to access the encrypted database tables.

Views

A view is a virtual table that is not physically stored in the database, but appears exactly like a "real" table. A view can contain data from one or more tables or other views and is used to store often-used queries or query sets in a database. Views can be updateable views or read-only views. By giving users access rights to the views, but not giving them rights to the base tables, views can also provide a limited means of security. For example, a view can be defined to only allow the user to see certain columns in a table while hiding the data in other columns that contain sensitive information. View functionality is available with both ADT and DBF tables.

Advantage Extended Procedures (Stored Procedures)

Advantage Extended Procedures are stored procedures that are easy to develop and easy to use. Like traditional stored procedures, Advantage Extended Procedures allow you to execute a set of code at the server where the data resides. This allows you to remove data intensive tasks from the workstations and reduces your network traffic to a single send and receive operation. Unlike traditional stored procedures, however, Advantage Extended Procedures allow developers to write, store, and execute stored procedures on the server using their preferred application development tool. No database administrator is required to develop Advantage Extended Procedures. Advantage Extended Procedure functionality is available with both ADT and DBF tables.

Triggers

A trigger is a piece of code (similar to a stored procedure) that is executed on the server. Triggers differ from stored procedures because triggers are not called by the client, but instead are executed automatically in response to an insert, update, or delete operation. Triggers are supported for both SQL and navigational update operations. When a trigger is "fired" it contains some state information, which can be used inside the body of the trigger. Two in-memory tables are available inside a trigger; a \_\_new table and an \_\_old table. The \_\_new table contains new field values that were, or are about to be, inserted into the table. The \_\_old table contains old field values for the record in question. Triggers can provide a very powerful means to maintain business rules inside of a database. Advantage trigger functionality is available with both ADT and DBF tables.

Support for Non-Auto-Open Index for SQL Statements

Non-auto-open indexes, such as NTX indexes, can be associated with database tables). Once the non-auto-open indexes have been associated with a table, they are automatically opened during the opening of the table and are maintained by the Advantage servers to ensure the logical validity of those indexes. The server will also use the non-auto-open indexes to optimize the execution of SQL queries. Non-Auto-Open Index functionality is available with both ADT and DBF tables.

Deployment Functionality

Using the API, AdsDDDeployDatabase, an application or utility can be written to upgrade the current deployment of an application to take on the properties of a new Advantage Data Dictionary. This functionality will allow for existing free tables) to be added into a data dictionary of the developers design, as well as for adding constraints, referential integrity, user/group restrictions, fields, indexes, etc. This is also a great time saving utility as it frees the developer from writing extensive code to implement this same functionality or having to add all the tables and definitions by hand. See the API documentation for AdsDDDeployDatabase in either the Advantage TDataSet Descendant Help (ADE.HLP) or the Advantage Client Engine Help (ACE.HLP) for specific details on what this functionality allows as well as any restrictions that may exist. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

Default Index

The data dictionary can store a default index for each table. The default index does not have to be the primary key; it can be any existing index. When new table objects are created (in Delphi, OLE DB, etc.), they will automatically be configured to use the default index from the data dictionary. If the default index is changed in the dictionary at a later time, all tables will automatically begin using the new default index. For optimized performance, the default index is initially not set to reduce unnecessary index page reads.

Table/Index Auto-Creation

Auto-creation functionality exists for tables and indexes belonging to an Advantage Data Dictionary. When a table associated with a data dictionary is opened, if the table's file and/or index file(s) are missing, new ones will be created with the same structure they previously had but empty of data. If a deleted table file had memo fields, its memo file will be created as well. This functionality is enabled by setting a dictionary tables auto-creation property to True with the property ADS\_DD\_TABLE\_AUTO\_CREATE. It is also possible to set the memo block size for auto-created tables to something other than the default size by using the ADS\_DD\_TABLE\_MEMO\_BLOCK\_SIZE property. These properties can be set using one of the following functions/methods:

- AdsDDSetTableProperty for the Advantage Client Engine API

- TAdsDictionary.SetTableProperty for the Advantage TDataSet Descendant

Table/Index Auto-Creation functionality is available with both ADT and DBF tables.

Note Whenever auto-creation takes place, an error will be logged to the Advantage error log file, ADS\_ERR.ADT or ADS\_ERR.DBF, stating that auto-creation has occurred. This error is never returned to the client application because it is not truly an error. It exists as a warning only and is normal behavior when the auto-creation property is set. This warning, AE\_INFO\_AUTO\_CREATION\_OCCURRED, is error code 5168.

See the Advantage Client Engine Help documentation (ACE.HLP) for a list of Advantage Data Dictionary functions. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

See TAdsDictionary in the Advantage TDataSet Descendant Help documentation (ADE.HLP) for more information on the programmatically accessing the Advantage Data Dictionary via the TAdsDictionary component with the Advantage TDataSet Descendant. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

See Also

[Accessing an Advantage Data Dictionary with the Advantage TDataSet Descendant](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.md)
