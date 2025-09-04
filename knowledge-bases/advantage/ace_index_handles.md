Index Handles




Advantage Database Server 12  

Index Handles

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Index Handles  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Index Handles Advantage Client Engine ace\_Index\_handles Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Index Handles  Advantage Client Engine |  |  |  |  |

Index handles need to be associated with the table on which the index is built. Index handles provide indexed movement and seek functionality. The Advantage Client Engine does not encapsulate index handles with their associated tables except through API functions such as [AdsGetIndexHandle](ace_adsgetindexhandle.htm) and [AdsGetAllIndexes](ace_adsgetallindexes.htm). It may be useful when using the Advantage Client Engine at the API level to encapsulate the index handles themselves in a data structure or class to give the programmer full control.

Table movement functions in the Advantage Client Engine accept either an index handle or a table handle. Therefore, calling [AdsSkip](ace_adsskip.htm) with a table handle will perform a natural order skip, and calling [AdsSkip](ace_adsskip.htm) immediately afterward with an index handle will have the same effect as setting the index order to the index the handle refers, and performing a skip in that index.

Another concept the Advantage Client Engine addresses is the compound index. When a compound index is opened, the Advantage Client Engine generates an index handle for each index order. These handles are available from the [AdsOpenIndex](ace_adsopenindex.htm) function, from [AdsGetAllIndexes](ace_adsgetallindexes.htm), or by calling [AdsGetIndexHandle](ace_adsgetindexhandle.htm) with the index order name. When one order in a compound index is closed, all other index handles in the file are also closed and become invalid. If a compound index file has the same base file name as the table it is built on, it is automatically opened when the table is opened. This file is termed an AutoOpen index file; some vendors refer to it as a structural CDX or structural ADI file. Use [AdsGetIndexHandle](ace_adsgetindexhandle.htm) or [AdsGetAllIndexes](ace_adsgetallindexes.htm) to retrieve the index order handles. An AutoOpen index cannot be closed until the table is closed.

Index handles are valid until either the index file that includes them are closed, the table they index is closed, the connection they ride on is disconnected, or [AdsApplicationExit](ace_adsapplicationexit.htm) is called.