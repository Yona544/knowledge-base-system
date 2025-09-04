---
title: Arc Deleting A Database
slug: arc_deleting_a_database
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_deleting_a_database.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 3aa434f15cc0628dadd58f2a7dfddd374d388d6a
---

# Arc Deleting A Database

Deleting a Database

Deleting a Database

Advantage Data Architect

| Deleting a Database  Advantage Data Architect |  |  |  |  |

Deleting a database will remove the three data dictionary files (.add, .am, .ai ) and will free all tables associated with the database. After deleting a database, the tables can be opened without a database connection. All referential integrity objects, views, stored procedures, users, groups, and constraints will be removed.

The tables can then be added to other data dictionaries.

CAUTION Be careful when deleting objects! You cannot undo a deletion.

To delete a database:

| 1. | Open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as the ADSSYS user in order to delete a database. |

| 2. | Right-click the Database name in the Connection Repository and select Delete Dictionary. |

| 3. | Click Yes to delete the database. |
