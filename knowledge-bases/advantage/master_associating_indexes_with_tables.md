Associating Indexes with Tables




Advantage Database Server 12  

Associating Indexes with Tables

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Associating Indexes with Tables  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Associating Indexes with Tables Advantage SQL Engine master\_Associating\_indexes\_with\_tables Advantage SQL > SQL Functionality > Associating Indexes with Tables / Dear Support Staff, |  |
| Associating Indexes with Tables  Advantage SQL Engine |  |  |  |  |

If SQL statements are used on free connections (connections that are not associated with an Advantage Data Dictionary), the SQL engine only uses auto-open index files (those with the same base name as the table) because the SQL engine does not know the names of the index files. To use indexes other than auto-open indexes, use a Database Connection, which is a connection made to Advantage Database Server or Advantage Local Server using an Advantage Data Dictionary file as the connection path. The data dictionary, among other functions, associates tables to index files.