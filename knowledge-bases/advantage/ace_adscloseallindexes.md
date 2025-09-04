AdsCloseAllIndexes




Advantage Database Server 12  

AdsCloseAllIndexes

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCloseAllIndexes  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCloseAllIndexes Advantage Client Engine ace\_Adscloseallindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCloseAllIndexes  Advantage Client Engine |  |  |  |  |

Closes all index orders for a given table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCloseAllIndexes (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Close all indexes for this table or cusor. |

Remarks

It is not possible to close an AutoOpen index. If the table has an AutoOpen index, AdsCloseAllIndexes will return SUCCESS, but index order handles from the AutoOpen index will still be valid.

Note Updating data in a table without all associated indexes being opened can result in index corruption. If such corruption occurs, it can be repaired by calling [AdsReindex](ace_adsreindex.htm) on the table handle.

 

Note It is illegal to close all index orders during a transaction.

Example

[Click Here](ace_examples.htm#adscloseallindexesexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsReindex](ace_adsreindex.htm)