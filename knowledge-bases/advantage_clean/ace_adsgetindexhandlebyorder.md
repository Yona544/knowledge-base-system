---
title: Ace Adsgetindexhandlebyorder
slug: ace_adsgetindexhandlebyorder
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexhandlebyorder.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b1f3eada5fb07ea33956439e617ede57583073fb
---

# Ace Adsgetindexhandlebyorder

AdsGetIndexHandleByOrder

AdsGetIndexHandleByOrder

Advantage Client Engine

| AdsGetIndexHandleByOrder  Advantage Client Engine |  |  |  |  |

Returns the index handle indicated by an order number.

Syntax

| UNSIGNED32 | AdsGetIndexHandleByOrder (ADSHANDLE hTable,  UNSIGNED16 usOrder,  ADSHANDLE \*phIndex); |

Parameters

| hTable (I) | Handle of a table or cursor. |
| usOrder (I) | Order number to retrieve index handle for. |
| phIndex (O) | Handle of an index order. |

Remarks

This function returns the index handle corresponding to the indicated order number. The index order number is a number from 1 to the number of index orders currently open. The index orders are arranged by the order they are opened. If an index file is closed, the index orders in it are no longer available, and index orders opened after it are moved down so there is a continuous list of index orders. If an AutoOpen index exits, the index orders in it are always the first ones in the order list.

Example

None.

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)

[AdsGetIndexName](ace_adsgetindexname.md)

[AdsCloseIndex](ace_adscloseindex.md)
