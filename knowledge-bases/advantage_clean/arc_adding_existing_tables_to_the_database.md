---
title: Arc Adding Existing Tables To The Database
slug: arc_adding_existing_tables_to_the_database
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_adding_existing_tables_to_the_database.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 5f452b50428be912783cf8a664635532943dc7fc
---

# Arc Adding Existing Tables To The Database

Adding Existing Tables to the Database

Adding Existing Tables to a Database

Advantage Data Architect

| Adding Existing Tables to a Database  Advantage Data Architect |  |  |  |  |

To add existing tables to the database:

| 1. | Open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with CREATE TABLE permissions in order to add an existing table to the data dictionary. |

| 2. | Right-click the Tables icon in the Connection Repository and select Add Existing Table(s). |

| 3. | In the dialog box that appears, holding down the Ctrl key and clicking the left mouse button can select multiple tables. Once the tables are selected, click Open. |

The tables will now be displayed in the tree view.

Adding tables to the database will ensure that all changes made to that table will be in accordance with the constraints and RI set up in the database. This will prevent possible logical table corruption.

Adding an ADT table to the database will change the table header so that the table is bound to the database. The ADT table will not open without a database connection.

Note The table header is only changed for ADT tables. Non-ADT tables (DBF tables with CDX and NTX indexes) will still be able to be accessed outside the database. This could lead to logical corruption of these tables if they are updated outside an Advantage database connection.
