DROP TABLE




Advantage Database Server 12  

DROP TABLE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DROP TABLE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DROP TABLE Advantage SQL Engine master\_Drop\_table Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DROP TABLE  Advantage SQL Engine |  |  |  |  |

Deletes a table and any indexes associated with it from the database

Syntax

DROP TABLE <table-name> [FROM DATABASE [NO\_DELETE]]

 

Remarks

CASCADE, RESTRICT not supported.

If the table is a [database table](javascript:hhpopuplink.TextPopup(popid_484727561X,FontFace,-1,-1,-1,-1)), that is, if the table is associated with an [Advantage Data Dictionary](master_advantage_data_dictionary.htm), the table can only be deleted if the DROP TABLE statement is executed by a user with DROP permissions on the specified table. The NO\_DELETE option will cause a database table to be removed from the data dictionary, but not deleted from disk. The FROM DATABASE clause is not required to drop a database table, however, it is required to specify the NO\_DELETE option.

Note Encrypted database tables removed from the database, but not deleted, will be left in a decrypted state.

Example(s)

DROP TABLE sal

DROP TABLE sal FROM DATABASE NO\_DELETE