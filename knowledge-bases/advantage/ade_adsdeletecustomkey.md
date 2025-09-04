AdsDeleteCustomKey




Advantage Database Server 12  

TAdsTable.AdsDeleteCustomKey

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsDeleteCustomKey  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsDeleteCustomKey Advantage TDataSet Descendant ade\_Adsdeletecustomkey Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsDeleteCustomKey  Advantage TDataSet Descendant |  |  |  |  |

Removes the key built from the current record from the custom index order.

Syntax

procedure AdsDeleteCustomKey (strTag : string);

Parameter

|  |  |
| --- | --- |
| strTag | Tag name of an open index. |

Description

AdsDeleteCustomKey will remove the key corresponding to the current record from the custom index order. If a key for this record was not added to the index, AdsDeleteCustomKey will not raise an exception.

Note When the index is shared, deleting a custom key will fail if the record is locked by another application. If the index is opened exclusively, custom keys can be deleted even when the record is locked by another application. To open an index exclusively, open the table exclusively or open the table in shared mode and create a custom index without closing it.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optCUSTOM ] );

{ the tag1 index contains no records }

 

AdsTable1.First;

AdsTable1.AdsAddCustomKey( 'Tag1' );

{ the tag1 index contains one record }

 

AdsTable1.AdsDeleteCustomKey( 'Tag1' );

{ the tag1 index contains no records }

 

AdsTable1.IndexName := 'Tag1';

Adstable1.First;

See Also

[AdsAddCustomKey](ade_adsaddcustomkey.htm)

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsIsIndexCustom](ade_adsisindexcustom.htm)