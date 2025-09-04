Bookmark




Advantage Database Server 12  

TAdsTable/TAdsQuery.Bookmark

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.Bookmark  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.Bookmark Advantage TDataSet Descendant ade\_Bookmark Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.Bookmark  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

Specifies the current bookmark in the dataset.

Syntax

type TBookmarkStr: string;

 

property Bookmark: TBookmarkStr;

Description

Bookmark gets or sets the current bookmark in a dataset. A bookmark provides a convenient way to mark a location in a dataset so that an application can easily return to that location quickly. The string contains the record number.

Note The bookmark is the record number of the physical record. This can cause some problems with bookmark validation of a deleted record, and that record number reused due to record reuse associated to the Advantage Data Tables.