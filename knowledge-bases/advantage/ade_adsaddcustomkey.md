AdsAddCustomKey




Advantage Database Server 12  

TAdsTable.AdsAddCustomKey

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsAddCustomKey  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsAddCustomKey Advantage TDataSet Descendant ade\_Adsaddcustomkey Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsAddCustomKey  Advantage TDataSet Descendant |  |  |  |  |

Adds a key built on the current record to the custom index order.

Syntax

procedure AdsAddCustomKey (strTag : string);

Parameter

|  |  |
| --- | --- |
| strTag | Tag name of an open index. |

Description

Custom indexes are empty when created and require keys to be explicitly added and removed. AdsAddCustomKey will add a key based on the current record to the custom index order. This key will be updated if the values in the record change.

Note When the index is shared, adding a custom key will fail if the record is locked by another application. If the index is opened exclusively, custom keys can be added even when the record is locked by another application. To open an index exclusively, open the table exclusively or open the table in shared mode and create a custom index without closing it.

Example

AdsTable1.Exclusive := TRUE;  
AdsTable1.Active := TRUE;  
AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optCUSTOM, optCOMPOUND ] );  
{ the tag1 index contains no records }  
   
AdsTable1.First;  
AdsTable1.AdsAddCustomKey( 'Tag1' );

{ the tag1 index contains one record }  
   
AdsTable1.AdsDeleteCustomKey( 'Tag1' );  
{ the tag1 index contains no records }  
   
AdsTable1.IndexName := 'Tag1';  
Adstable1.First;

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsIsIndexCustom](ade_adsisindexcustom.htm)

[AdsDeleteCustomKey](ade_adsdeletecustomkey.htm)