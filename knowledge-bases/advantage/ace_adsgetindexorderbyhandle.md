AdsGetIndexOrderByHandle




Advantage Database Server 12  

AdsGetIndexOrderByHandle

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexOrderByHandle  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexOrderByHandle Advantage Client Engine ace\_Adsgetindexorderbyhandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexOrderByHandle  Advantage Client Engine |  |  |  |  |

Retrieve the order number of the indicated index handle.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexOrderByHandle (ADSHANDLE hIndex,  UNSIGNED16 \*pusIndexOrder); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| pusIndexOrder (O) | Order number of the index handle. |

Remarks

AdsGetIndexOrderByHandle returns the order number of the index handle passed in. The index order number is a number from 1 to the number of index orders currently open. The index orders are arranged by the order they are opened. If an index file is closed, the index orders in it are no longer available, and index orders opened after it are moved down. Therefore, there is a continuous list of index orders. If an AutoOpen index exits, the index orders in it are always the first ones in the order list.

Example

None.

See Also

[AdsGetIndexHandleByOrder](ace_adsgetindexhandlebyorder.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)