---
title: Ace Adsgetkeylength
slug: ace_adsgetkeylength
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetkeylength.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7136286d5ad1f2270f0406d61224717dfc6119b1
---

# Ace Adsgetkeylength

AdsGetKeyLength

AdsGetKeyLength

Advantage Client Engine

| AdsGetKeyLength  Advantage Client Engine |  |  |  |  |

Retrieves the key size in bytes of the given index order.

Syntax

| UNSIGNED32 | AdsGetKeyLength (ADSHANDLE hIndex,  UNSIGNED16 \*pusKeySize ); |

Parameters

| hIndex (I) | Handle of an index order. |
| pusKeySize (O) | Length in bytes of the index key. |

Remarks

Returns the number of bytes in each physical key in the index file. If the index key evaluates to a variable-length expression, this function will return zero for the length.

Example

None.

See Also

[AdsExtractKey](ace_adsextractkey.md)

[AdsGetKeyType](ace_adsgetkeytype.md)
