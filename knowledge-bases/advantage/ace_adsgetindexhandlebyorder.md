AdsGetIndexHandleByOrder




Advantage Database Server 12  

AdsGetIndexHandleByOrder

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexHandleByOrder  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexHandleByOrder Advantage Client Engine ace\_Adsgetindexhandlebyorder Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexHandleByOrder  Advantage Client Engine |  |  |  |  |

Returns the index handle indicated by an order number.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexHandleByOrder (ADSHANDLE hTable,  UNSIGNED16 usOrder,  ADSHANDLE \*phIndex); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor. |
| usOrder (I) | Order number to retrieve index handle for. |
| phIndex (O) | Handle of an index order. |

Remarks

This function returns the index handle corresponding to the indicated order number. The index order number is a number from 1 to the number of index orders currently open. The index orders are arranged by the order they are opened. If an index file is closed, the index orders in it are no longer available, and index orders opened after it are moved down so there is a continuous list of index orders. If an AutoOpen index exits, the index orders in it are always the first ones in the order list.

Example

None.

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)

[AdsGetIndexName](ace_adsgetindexname.htm)

[AdsCloseIndex](ace_adscloseindex.htm)