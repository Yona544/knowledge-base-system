AdsIsIndexCustom




Advantage Database Server 12  

TAdsTable.AdsIsIndexCustom

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsIndexCustom  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsIndexCustom Advantage TDataSet Descendant ade\_Adsisindexcustom Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsIsIndexCustom  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order was built as a custom index.

Syntax

function AdsIsIndexCustom : Boolean;

Description

A custom index is built without keys. Keys are added to the custom index explicitly by calls to AdsAddCustomKey and AdsDeleteCustomKey. This allows a user to build a very small and specific index.

Custom indexes can only be built on tables opened with the ttAdsCDX or ttAdsADT option.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optCUSTOM ] );

AdsTable1.IndexName := Tag1;

 

bIsCustom := AdsTable1.AdsIsIndexCustom;

See Also

[AdsAddCustomKey](ade_adsaddcustomkey.htm)

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsDeleteCustomKey](ade_adsdeletecustomkey.htm)

[AdsOpenIndex](ade_adsopenindex.htm)