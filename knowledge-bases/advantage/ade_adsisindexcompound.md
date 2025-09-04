AdsIsIndexCompound




Advantage Database Server 12  

TAdsTable.AdsIsIndexCompound

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsIndexCompound  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsIndexCompound Advantage TDataSet Descendant ade\_Adsisindexcompound Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsIsIndexCompound  Advantage TDataSet Descendant |  |  |  |  |

Determines if the given index order is from a compound index file.

Syntax

function AdsIsIndexCompound : Boolean;

Description

AdsIsIndexCompound will return True only if the index order specified is in a compound index file (a Foxpro-compatible CDX file or Advantage proprietary ADI file). Indexes built with NTX and FoxPro-compatible IDX files are not compound indexes.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'FirstName', '', '', [ optCOMPOUND ] );

AdsTable1.IndexName := Tag1;

bIsCompound := AdsTable1.AdsIsIndexCompound;

{ bIsCompound equals True since within a compound index }

 

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)