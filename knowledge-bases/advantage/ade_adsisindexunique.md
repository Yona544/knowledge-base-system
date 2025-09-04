AdsIsIndexUnique




Advantage Database Server 12  

TAdsTable.AdsIsIndexUnique

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsIndexUnique  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsIndexUnique Advantage TDataSet Descendant ade\_Adsisindexunique Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsIsIndexUnique  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order is unique.

Syntax

function AdsIsIndexUnique : Boolean;

Description

A unique index will have no repeated key values.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optUNIQUE ] );

AdsTable1.IndexName := Tag1;

 

bIsUnique := AdsTable1.AdsIsIndexUnique;

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)