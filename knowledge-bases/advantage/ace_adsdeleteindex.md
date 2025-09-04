AdsDeleteIndex




Advantage Database Server 12  

AdsDeleteIndex

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDeleteIndex  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDeleteIndex Advantage Client Engine ace\_Adsdeleteindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDeleteIndex  Advantage Client Engine |  |  |  |  |

Deletes the given index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsDeleteIndex (ADSHANDLE hIndex); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order to delete. If it is the only index order (tag) in a compound index file or if it is an index order in a non-compound index file, the file will be deleted as well. |

Remarks

If the index order is a tag in a CDX or ADI, the tag will be marked for deletion and will no longer be used. If it is the last non-deleted tag in the file, the file will be deleted. If the index order is an IDX or NTX, the file will be deleted. Remove deleted tags out of compound index files by reindexing (see [AdsReindex](ace_adsreindex.htm) ).

Note It is illegal to delete an index order during a transaction.

Example

[Click Here](ace_examples.htm#adsdeleteindexexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCloseIndex](ace_adscloseindex.htm)