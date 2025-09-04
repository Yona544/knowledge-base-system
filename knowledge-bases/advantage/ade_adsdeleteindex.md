AdsDeleteIndex




Advantage Database Server 12  

TAdsTable.AdsDeleteIndex

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsDeleteIndex  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsDeleteIndex Advantage TDataSet Descendant ade\_Adsdeleteindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsDeleteIndex  Advantage TDataSet Descendant |  |  |  |  |

Deletes the given index order.

Syntax

procedure AdsDeleteIndex( strTag : String );

Parameter

|  |  |
| --- | --- |
| strTag | Tag of index order to delete. If it is the only index order (tag) in a compound index file or if it is an index order in a non-compound index file, the file will be deleted as well. |

Description

If the index order is a tag in a CDX or ADI, it will be removed. If it is the last tag in the index, the file will be deleted. If the index order is an IDX or NTX, the file will be deleted.

Note It is illegal to delete an index order during a transaction.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', '', '', [] );

 

{. . . your code here . . .}

 

AdsTable1.AdsDeleteIndex( 'Tag1' );

 

See Also

[AdsCloseIndex](ade_adscloseindex.htm)

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)