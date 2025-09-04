AdsCopyTableStructure




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsCopyTableStructure

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsCopyTableStructure  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsCopyTableStructure Advantage TDataSet Descendant ade\_Adscopytablestructure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsCopyTableStructure  Advantage TDataSet Descendant |  |  |  |  |

Creates a new table with the same structure as the given dataset.

Syntax

procedure AdsCopyTableStructure( strFileName : String );

Parameter

|  |  |
| --- | --- |
| strFileName | File to create with the current dataset structure. |

Description

The table created does not contain records, but has field structure identical to the original table. Indexes are not copied by AdsCopyTableStructure. The empty table must be opened in a separate table instance.

Example

AdsTable1.TableName := x:\data\employee.adt;

AdsTable1.Active := TRUE;

AdsTable1.AdsCopyTableStructure( x:\data\empty employee file.adt );

See Also

[AdsCopyTable](ade_adscopytable.htm)

[AdsCopyTableContents](ade_adscopytablecontents.htm)

[AdsConvertTable](ade_adsconverttable.htm)