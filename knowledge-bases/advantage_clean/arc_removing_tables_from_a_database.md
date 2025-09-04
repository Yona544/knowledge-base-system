---
title: Arc Removing Tables From A Database
slug: arc_removing_tables_from_a_database
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_removing_tables_from_a_database.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 83ee050960162a201d24d4c045563b5ca6482da0
---

# Arc Removing Tables From A Database

Removing Tables from a Database

Removing Tables from a Database

Advantage Data Architect

| Removing Tables from a Database  Advantage Data Architect |  |  |  |  |

Removing a table from the database will release the link from the table to the database. A table that has been removed can be added to other dictionaries. Keep in mind that if a table is removed from the database, constraints, referential integrity, etc., will no longer be enforced.

To remove a table from a database:

| 1. | Open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with DROP permissions on the specific table in order to delete a database table from the Data Dictionary. |

| 2. | Expand the TABLES icon in the tree view. |

| 3. | Right-click the associated table name and then click Delete. |
