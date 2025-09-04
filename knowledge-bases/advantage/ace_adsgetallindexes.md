AdsGetAllIndexes




Advantage Database Server 12  

AdsGetAllIndexes

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetAllIndexes  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetAllIndexes Advantage Client Engine ace\_Adsgetallindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetAllIndexes  Advantage Client Engine |  |  |  |  |

Returns an array of open index order handles for the given table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetAllIndexes (ADSHANDLE hTable,  ADSHANDLE ahIndex[],  UNSIGNED16 \*pusArrayLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| ahIndex[] (O) | Return index order handles in the given array. |
| pusArrayLen (I/O) | Number of entries (not bytes) in the array on input, number of returned entries on output. |

Remarks

The index order handles are returned in the order they were opened. For CDX and ADI indexes, the index order handles are returned in the order they were created within the index file. If the array passed to this function is insufficient for all index handles, the array will be filled with all handles that fit, the pusArrayLen parameter will return the number of available handles, and the function will return the error code AE\_INSUFFICIENT\_BUFFER. AdsGetAllIndexes does not return information for full text information in full text search indexes.

Example

[Click Here](ace_examples.htm#adsgetallindexesexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsGetNumIndexes](ace_adsgetnumindexes.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)

[AdsGetFTSIndexes](ace_adsgetftsindexes.htm)