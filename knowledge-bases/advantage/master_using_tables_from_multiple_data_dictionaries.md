Using Tables from Multiple Data Dictionaries




Advantage Database Server 12  

Using Tables from Multiple Data Dictionaries

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Tables from Multiple Data Dictionaries  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Using Tables from Multiple Data Dictionaries Advantage SQL Engine master\_Using\_tables\_from\_multiple\_data\_dictionaries Advantage SQL > SQL Functionality > Using Tables from Multiple Data Dictionaries / Dear Support Staff, |  |
| Using Tables from Multiple Data Dictionaries  Advantage SQL Engine |  |  |  |  |

Tables from different data dictionaries can be used in the same SQL statement by prefixing the table name with the database name that the table belongs to using dot notation. This feature is only available when the statement is executed on a [database connection](javascript:hhpopuplink.TextPopup(popid_773697001,FontFace,-1,-1,-1,-1)). Some example statements using tables from different databases are:

SELECT \* FROM Employees a, "\Backup\Data\HR.ADD".Employees b WHERE a.employee\_id = b.employee\_id

UPDATE Customers SET address = ( SELECT address FROM backup.Customers b WHERE b.cust\_id = Customers.cust\_id )

INSERT INTO SalesDB.SalesReps VALUES ( 69, "Bob", "Hannah" )

The database name in the first example is specified directly using the path to the linked data dictionary, "\Backup\Data\HR.ADD". The second example uses a link alias named "backup" as the database name. The third example uses a link alias named "SalesDB". A link alias can be either a global alias that is defined in the data dictionary by the administrator or a local alias defined only for the current connection. Link aliases, both global and local, are created using the AdsDDCreateLink API (see ACE.HLP for more information). Global aliases can be created using the Advantage Database Manager in the Advantage Data Architect utility.

The role of the user in the linked data dictionary is dependent on how the link is created in the SQL statement. If a direct path is used to specify the linked data dictionary, the user name and password on the current connection is used for authentication in the linked data dictionary. This requires setting up an identical user with the same password in the linked data dictionary. If a link alias is used to access the linked data dictionary, the role of the user in the linked data dictionary depends on how the link alias was created, see AdsDDCreateLink in the Advantage Client Engine Help documentation (ACE.HLP or ace.htm) and sp\_CreateLink for additional information about link aliases.

Access permissions to tables in the linked data dictionary are controlled by the following elements:

|  |  |
| --- | --- |
| 1. | 1. The permissions of the user authenticated in the linked data dictionary are used to obtain the permission to the table in the linked data dictionary. |

|  |  |
| --- | --- |
| 2. | 2. If accessing a table using a global link alias defined in the data dictionary, the user must have access permission to the global link alias in the data dictionary. |

Note Views in the linked data dictionary cannot be used in the SQL statement directly. However, views can be defined based on the tables in the linked data dictionary. For example: CREATE VIEW Link\_T1 AS SELECT cust\_name FROM Link.customers WHERE credit\_limit > 50000

Replication Note When updating linked tables in a transaction, only tables from one dictionary can be replicated in a given transaction. If you begin a transaction and update tables in two different linked dictionaries that have replication defined, only the tables from the first updated dictionary will be replicated.

See [Linked Data Dictionaries](master_linked_data_dictionaries.htm) for additional information.