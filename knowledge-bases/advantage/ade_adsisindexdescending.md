AdsIsIndexDescending




Advantage Database Server 12  

TAdsTable.AdsIsIndexDescending

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsIndexDescending  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsIndexDescending Advantage TDataSet Descendant ade\_Adsisindexdescending Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsIsIndexDescending  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order is descending.

Syntax

function AdsIsIndexDescending : Boolean;

Description

A descending index has keys sorted in the order of largest to smallest. The default is an ascending index. An AdsGotoTop on a descending order will position at the largest key in the index. An AdsGotoBottom will position at the smallest key in the index order.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optDESCENDING ] );

AdsTable1.IndexName := Tag1;

 

bIsDescending := AdsTable1.AdsIsIndexCustom;

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)