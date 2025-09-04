Insert




Advantage Database Server 12  

TAdsTable.Insert

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.Insert  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.Insert Advantage TDataSet Descendant ade\_Insert Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.Insert  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Inserts a new, empty record in the dataset.

Syntax

procedure Insert;

Description

Call Insert to do the following:

|  |  |
| --- | --- |
| · | Open a new, empty record in the dataset. |

|  |  |
| --- | --- |
| · | Set the current record to the new record. |

After a call to Insert, an application can enable users to enter data in the fields of the records, and can then post those changes to the table using Post. A newly inserted record is posted to the table in one of three ways:

|  |  |
| --- | --- |
| · | For indexed tables, the record is inserted into the dataset in a position based on its index. |

|  |  |
| --- | --- |
| · | For non-indexed DBF tables, the record is added to the end of the dataset. |

|  |  |
| --- | --- |
| · | For non-indexed ADT tables, the record is either added to the end of the dataset or inserted into the position of a record that was previously deleted. |