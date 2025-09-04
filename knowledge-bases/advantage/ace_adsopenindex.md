AdsOpenIndex




Advantage Database Server 12  

AdsOpenIndex

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsOpenIndex  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsOpenIndex Advantage Client Engine ace\_Adsopenindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsOpenIndex  Advantage Client Engine |  |  |  |  |

Opens an index file and associates all index orders in the file with the given table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsOpenIndex (ADSHANDLE hTable,  UNSIGNED8 \*pucName,  ADSHANDLE ahIndex[],  UNSIGNED16 \*pusArrayLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. |
| pucName (I) | Filename of the index file to open. |
| ahIndex[] (O) | Return array of index orders if opened successfully. If it is a non-compound index file (NTX/IDX) then this need only be an array of length 1. If it is a compound index file (CDX or ADI), then it may be an array of length 50 (unless the user knows it is less). |
| pusArrayLen (I/O) | Number of entries in index handle array on input (not bytes), number of returned entries on output. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INDEX\_ALREADY\_OPEN | The index file specified is already open. |

Remarks

AdsOpenIndex returns all handles of index orders in the index file in the ahIndex parameter. If the index file is NOT a compound index (CDX or ADI), then it will have only one index order. If the index file is a compound CDX or ADI index, however, more than one index order handle may be returned.

Non-compact IDX files are not supported.

If an application calls AdsOpenIndex with the name of an index file that is already open, the Advantage Client Engine will return the error code AE\_INDEX\_ALREADY\_OPEN. If this happens, the Advantage Client Engine will also fill in the array of index orders (ahIndex) with the index order(s) from the index file just as if it had actually opened the file. This is a good way to retrieve the index order(s) for a specific index file if a table has multiple index files open.

Opening an index does not change the current record.

Example

[Click Here](ace_examples.htm#adsopenindexexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)

[AdsCloseIndex](ace_adscloseindex.htm)

[AdsGetAllIndexes](ace_adsgetallindexes.htm)