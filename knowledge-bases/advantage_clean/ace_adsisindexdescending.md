---
title: Ace Adsisindexdescending
slug: ace_adsisindexdescending
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexdescending.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 420862230fe0b1aff1aa56c6abc6d228a7bc12ac
---

# Ace Adsisindexdescending

AdsIsIndexDescending

AdsIsIndexDescending

Advantage Client Engine

| AdsIsIndexDescending  Advantage Client Engine |  |  |  |  |

Determines if the given index order is descending.

Syntax

| UNSIGNED32 | AdsIsIndexDescending (ADSHANDLE hIndex,  UNSIGNED16 \*pbDescending); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbDescending (O) | Return True if index order is descending. |

Remarks

Descending index keys are sorted from largest to smallest. The default is an ascending index. An [AdsGotoTop](ace_adsgototop.md) call on a descending order will position at the largest key in the index. An AdsGotoBottom call will position at the smallest key in the index order.

Example

[Click Here](ace_examples.md#adsisindexdescendingexample)

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)
