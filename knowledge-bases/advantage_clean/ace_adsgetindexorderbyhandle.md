---
title: Ace Adsgetindexorderbyhandle
slug: ace_adsgetindexorderbyhandle
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexorderbyhandle.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 466f5dbe18a37538856565590f50f2b5eb2320ba
---

# Ace Adsgetindexorderbyhandle

AdsGetIndexOrderByHandle

AdsGetIndexOrderByHandle

Advantage Client Engine

| AdsGetIndexOrderByHandle  Advantage Client Engine |  |  |  |  |

Retrieve the order number of the indicated index handle.

Syntax

| UNSIGNED32 | AdsGetIndexOrderByHandle (ADSHANDLE hIndex,  UNSIGNED16 \*pusIndexOrder); |

Parameters

| hIndex (I) | Handle of index order. |
| pusIndexOrder (O) | Order number of the index handle. |

Remarks

AdsGetIndexOrderByHandle returns the order number of the index handle passed in. The index order number is a number from 1 to the number of index orders currently open. The index orders are arranged by the order they are opened. If an index file is closed, the index orders in it are no longer available, and index orders opened after it are moved down. Therefore, there is a continuous list of index orders. If an AutoOpen index exits, the index orders in it are always the first ones in the order list.

Example

None.

See Also

[AdsGetIndexHandleByOrder](ace_adsgetindexhandlebyorder.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)
