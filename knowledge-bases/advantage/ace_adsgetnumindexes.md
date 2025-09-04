AdsGetNumIndexes




Advantage Database Server 12  

AdsGetNumIndexes

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetNumIndexes  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetNumIndexes Advantage Client Engine ace\_Adsgetnumindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetNumIndexes  Advantage Client Engine |  |  |  |  |

Retrieves the total number of open index orders associated with the given table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetNumIndexes (ADSHANDLE hTable,  UNSIGNED16 \*pusNum); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusNum (O) | Return number of index orders. For example, if the user opened a CDX file with 5 tags and an IDX, this function would return the total 6. |

Remarks

The number of indexes returned does not necessarily correspond to the number of index files opened for the table. A compound index may contain multiple index orders. Calling this function before calling [AdsGetAllIndexes](ace_adsgetallindexes.htm) will provide the number of index orders that will be returned. AdsGetNumIndexes does not return information for full text search indexes.

Example

[Click Here](ace_examples.htm#adsgetnumindexesexample)

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsGetAllIndexes](ace_adsgetallindexes.htm)

[AdsGetNumFTSIndexes](ace_adsgetnumftsindexes.htm)