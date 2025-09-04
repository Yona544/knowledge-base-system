Deleting a Database




Advantage Database Server 12  

Deleting a Database

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Deleting a Database  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Deleting a Database Advantage Data Architect arc\_Deleting\_a\_database Advantage Data Architect > Databases > Deleting a Database / Dear Support Staff, |  |
| Deleting a Database  Advantage Data Architect |  |  |  |  |

Deleting a database will remove the three data dictionary files (.add, .am, .ai ) and will free all tables associated with the database. After deleting a database, the tables can be opened without a database connection. All referential integrity objects, views, stored procedures, users, groups, and constraints will be removed.

The tables can then be added to other data dictionaries.

CAUTION Be careful when deleting objects! You cannot undo a deletion.

To delete a database:

|  |  |
| --- | --- |
| 1. | Open a database. See [Opening a Database](arc_opening_a_database2.htm) for details. You must login to the database as the ADSSYS user in order to delete a database. |

|  |  |
| --- | --- |
| 2. | Right-click the Database name in the Connection Repository and select Delete Dictionary. |

|  |  |
| --- | --- |
| 3. | Click Yes to delete the database. |