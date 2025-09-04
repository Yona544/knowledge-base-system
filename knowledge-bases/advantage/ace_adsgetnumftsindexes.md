AdsGetNumFTSIndexes




Advantage Database Server 12  

AdsGetNumFTSIndexes

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetNumFTSIndexes  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetNumFTSIndexes Advantage Client Engine ace\_Adsgetnumftsindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetNumFTSIndexes  Advantage Client Engine |  |  |  |  |

Retrieves the total number of full text search index orders associated with the given table.

Syntax

UNSIGNED32 AdsGetNumFTSIndexes ( ADSHANDLE hTable,

UNSIGNED16 \*pusNum );

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. |
| pusNum (O) | Return number of full text search (FTS) index orders. |

Remarks

Use this API to determine how many full text search indexes exist in all open index files for the given table. Calling this function before calling AdsGetFTSIndexes will provide the number of index orders that will be returned.

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.htm)

[AdsGetFTSIndexes](ace_adsgetftsindexes.htm)

[AdsGetNumIndexes](ace_adsgetnumindexes.htm)