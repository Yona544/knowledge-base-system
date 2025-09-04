Linked Data Dictionaries




Advantage Database Server 12  

Linked Data Dictionaries

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Linked Data Dictionaries  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Linked Data Dictionaries Advantage SQL Engine master\_Linked\_data\_dictionaries Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Linked Data Dictionaries  Advantage SQL Engine |  |  |  |  |

Advantage Data Dictionaries can be linked so that tables from multiple databases may be queried in the same SQL statement. The links are created using either the AdsDDCreateLink API in ACE or the sp\_CreateLink stored procedure in SQL.

For example, suppose a link named DB2 is created in the database A to reference database B, a connection made to database A can then reference the tables in database B using the dot notation "SELECT \* FROM DB2.table1".

Tables in the linked data dictionary can be used in an SQL statement but they cannot be opened directly using the ACE API. However, this limitation can be worked around by defining a view that references the linked table. For example, given the same set up as the previous example, a view named "DB2\_TABLE1" may be defined as "SELECT \* FROM DB2.table1". The view DB2\_TABLE1 can be opened directly using the ACE API and all of the navigational commands will be available on this view. The only limitation is that the table cannot be opened exclusively and commands that require exclusive access to the table are not available.

See [Using Table from Multiple Data Dictionaries](master_using_tables_from_multiple_data_dictionaries.htm) for additional information.