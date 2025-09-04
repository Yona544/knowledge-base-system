Removing Tables from a Database




Advantage Database Server 12  

Removing Tables from a Database

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Removing Tables from a Database  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Removing Tables from a Database Advantage Data Architect arc\_Removing\_tables\_from\_a\_database Advantage Data Architect > Databases > Removing Tables from a Database / Dear Support Staff, |  |
| Removing Tables from a Database  Advantage Data Architect |  |  |  |  |

Removing a table from the database will release the link from the table to the database. A table that has been removed can be added to other dictionaries. Keep in mind that if a table is removed from the database, constraints, referential integrity, etc., will no longer be enforced.

To remove a table from a database:

|  |  |
| --- | --- |
| 1. | Open a database. See [Opening a Database](arc_opening_a_database2.htm) for details. You must login to the database as a user with DROP permissions on the specific table in order to delete a database table from the Data Dictionary. |

|  |  |
| --- | --- |
| 2. | Expand the TABLES icon in the tree view. |

|  |  |
| --- | --- |
| 3. | Right-click the associated table name and then click Delete. |