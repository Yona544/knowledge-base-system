AdsGetFTSIndexes




Advantage Database Server 12  

AdsGetFTSIndexes

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetFTSIndexes  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetFTSIndexes Advantage Client Engine ace\_Adsgetftsindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetFTSIndexes  Advantage Client Engine |  |  |  |  |

Returns an array of full text search index order handles for the given table.

Syntax

UNSIGNED32 AdsGetFTSIndexes ( ADSHANDLE hTable, ADSHANDLE ahIndex[],

UNSIGNED16 \*pusArrayLen );

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. |
| ahIndex (O) | Return index order handles in the given array. |
| pusArrayLen (I/O) | Number of entries (not bytes) in the array on input, number of returned entries on output. |

Remarks

This API returns the full text search indexes that are currently open on the given table. If the array passed to this function is insufficient for all index handles, the array will be filled with all handles that fit, the pusArrayLen parameter will return the number of available handles, and the function will return the error code AE\_INSUFFICIENT\_BUFFER. Use AdsGetNumFTSIndexes before calling this API to determine how many will be returned.

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.htm)

[AdsGetNumFTSIndexes](ace_adsgetnumftsindexes.htm)

[AdsGetAllIndexes](ace_adsgetallindexes.htm)