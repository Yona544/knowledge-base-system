AddIndexEx




Advantage Database Server 12  

TAdsDataSet.AddIndexEx

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDataSet.AddIndexEx  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDataSet.AddIndexEx Advantage TDataSet Descendant ade\_Addindexex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDataSet.AddIndexEx  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

Creates a new index for the table.

Syntax

type TIndexOptions = set of (ixPrimary, ixUnique, ixDescending, ixCaseInsensitive, ixExpression);

 

procedure AddIndexEx( strFileName : string; strIndexName : string; strFields: string; poOptions : TIndexOptions );

Description

AddIndexEx behaves the same as the [TAdsDataSet.AddIndex](ade_addindex.htm) method, except AddIndexEx allows the caller to specify the index file the new index tag will belong to.

Use AddIndexEx when you find it necessary to create a non-auto-open index.

The most common use of AddIndexEx is to create temporary index files when using an Advantage Data Dictionary. Indexes created by users without administrative rights are not included in the data dictionary, which makes it necessary for the caller to specify the index file the new index tag will belong to.