---
title: Ace Adssetrelkeypos
slug: ace_adssetrelkeypos
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetrelkeypos.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 33614c6306fa0719f2f6c2fe276a2b09d21729bd
---

# Ace Adssetrelkeypos

AdsSetRelKeyPos

AdsSetRelKeyPos

Advantage Client Engine

| AdsSetRelKeyPos  Advantage Client Engine |  |  |  |  |

Sets the current record to the given relative position in the given index order.

Syntax

| UNSIGNED32 | AdsSetRelKeyPos (ADSHANDLE hIndex, DOUBLE dPos); |

Parameters

| hIndex (I) | Handle of index order. |
| dPos (I) | Set relative key positions. The value specified in the dPos parameter must be in the range from 0.0 to 1.0, where 0.0 would indicate the top of the index and 1.0 refers to the bottom. |

Remarks

AdsSetRelKeyPos approximates the position of the indicated percentage in the index order based on the given value. If there is a scope set, AdsSetRelKeyPos calculates and sets the relative position relative to the current scope.

Example

[Click Here](ace_examples.md#adssetrelkeyposexample)

See Also

[AdsGetRelKeyPos](ace_adsgetrelkeypos.md)

[AdsGetKeyCount](ace_adsgetkeycount.md)

[AdsGotoRecord](ace_adsgotorecord.md)
