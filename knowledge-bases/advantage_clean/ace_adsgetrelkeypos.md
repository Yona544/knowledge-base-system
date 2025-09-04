---
title: Ace Adsgetrelkeypos
slug: ace_adsgetrelkeypos
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetrelkeypos.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 06d1ca381bd3fe95100b515fee2869982fcba359
---

# Ace Adsgetrelkeypos

AdsGetRelKeyPos

AdsGetRelKeyPos

Advantage Client Engine

| AdsGetRelKeyPos  Advantage Client Engine |  |  |  |  |

Returns the relative position of the current record in the given index order.

Syntax

| UNSIGNED32 | AdsGetRelKeyPos (ADSHANDLE hIndex, DOUBLE \*pdPos); |

Parameters

| hIndex (I) | Handle of index order. |
| pdPos (O) | Return relative position. The value will be between 0.0 and 1.0 inclusive. |

Special Return Codes

| AE\_NOT\_FOUND | The desired index key was not found. It may not exist. |

Remarks

AdsGetRelKeyPos returns an estimation of the position in the current key in the indicated index order. The value returned will be between 0.0 and 1.0, inclusive. If there are scopes set on the index order, the position returned will be relative to the visible records.

Example

[Click Here](ace_examples.md#adsgetrelkeyposexample)

See Also

[AdsSetRelKeyPos](ace_adssetrelkeypos.md)

[AdsGetKeyNum](ace_adsgetkeynum.md)

[AdsGetKeyCount](ace_adsgetkeycount.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)
