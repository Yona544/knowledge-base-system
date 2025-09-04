---
title: Arc Creating Or Modifying A View
slug: arc_creating_or_modifying_a_view
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_a_view.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: faf5167fd44938353cb5189da205e14c2520198a
---

# Arc Creating Or Modifying A View

Creating or Modifying a View

Creating or Modifying a View

Advantage Data Architect

| Creating or Modifying a View  Advantage Data Architect |  |  |  |  |

A view is a virtual table that is not physically stored in the database, but appears exactly like a "real" table. A view can contain data from one or more tables or other views and is used to store often used queries or query sets in a database. Views can be updateable views or read-only views. By giving users access rights to the views but not to the base tables, views can also provide a limited means of security. For example, a view can be defined to only allow the user to see certain columns in a table while hiding the data in other columns that contain sensitive information.

To create or modify a View, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with CREATE VIEW or ALTER permissions on the specific view in order to add or modify Views in a database.

To add a new View, from the tree view within the Connection Repository, right-click the VIEWS icon and select Create.

To modify an existing View's properties, from the tree view within the Connection Repository, right-click the View's name icon and select Properties.

View Field Descriptions

Name (required)

Name of the view.

View SQL (required)

SQL SELECT statement definition of the view.

Description (optional)

Description for the view.

OK

Click OK to create the view. Once the view has been created, an icon will be added to the database tree.

Open

Opens the view.

Cancel

Cancels any input or changes and exits the screen.
