---
title: Arc Creating Or Modifying An Ri Object
slug: arc_creating_or_modifying_an_ri_object
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_an_ri_object.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: a943e5db8daa4db3ce21e5246f8f7a23f438d7e9
---

# Arc Creating Or Modifying An Ri Object

Creating or Modifying an RI Object

Creating or Modifying an RI Object

Advantage Data Architect

| Creating or Modifying an RI Object  Advantage Data Architect |  |  |  |  |

Referential Integrity (RI) is the means by which primary/foreign key relationships are enforced in a database. By specifying RI rules you can have the database guarantee, for example, that every sales representative is assigned to a valid office. Through the use of RI constraints, many business rules can be enforced by the database server, instead of by your application. See [Referential Integrity](master_referential_integrity.md) for more information.

To create or modify an RI object, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with ALTER permissions on both related tables in order to add or modify RI objects in a database.

To add a new RI object, right-click the RI OBJECTS icon and select Create.

To modify RI object properties, from the tree view within the Connection Repository, right-click the RI object's name icon and select Properties.

To access the RI Object screen from the ER diagram, click the link between the two tables.

RI Field Descriptions

General Tab

Name (required)

RI object name.

Fail Table (optional)

The path for the RI fail table. Be sure to specify a unique name per RI object so that a different RI object's failures will not overwrite this file.

Parent Table

Name (required)

Name of the parent table in the RI relationship.

Primary Key (required)

The primary index of the Parent Table.

Child Table

Name (required)

Name of the child table in the RI relationship.

Foreign Key (required)

Index of the child table to use as the foreign key in the child table.

Update and Delete Rules (required)

Update Rules (required)

The action that the server is to perform when any update to the parent or foreign table does not maintain the referential integrity.

Delete Rules (required)

The action that the server is to perform when a delete in the parent or foreign table does not maintain the referential integrity.

Advanced Tab

Custom Error Messages (optional)

"No Primary Key" Error String

If specified this string will be used in error messages resulting from an insert or update operation which violates a primary key dependency. If left blank the default error string will be returned.

Cascade Error String

If specified this string will be used in error messages resulting from a failed cascade operation. If left blank the default error string will be returned.

OK

Saves input and exits the screen. If a change is made to an existing RI object, the old RI object will be deleted and a new RI object will be created.

Cancel

Cancels input or changes and exits the screen.
