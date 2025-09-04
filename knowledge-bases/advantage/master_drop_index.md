DROP INDEX




Advantage Database Server 12  

DROP INDEX

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DROP INDEX  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DROP INDEX Advantage SQL Engine master\_Drop\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DROP INDEX  Advantage SQL Engine |  |  |  |  |

Deletes index orders (tags) from a CDX or ADI index file. When the last index order is deleted in an index file, the index file is deleted.

Syntax

DROP INDEX <table-name>.<index-name>

Remarks

If the table is a [database table](javascript:hhpopuplink.TextPopup(popid_484727561X,FontFace,-1,-1,-1,-1)), that is, if the table is associated with an [Advantage Data Dictionary](master_advantage_data_dictionary.htm), the DROP INDEX statement can only be executed from a user with ALTER permissions on the specified indexs associated table.

Example(s)

DROP INDEX emp.empid