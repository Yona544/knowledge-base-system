---
title: Ace Adsgetkeytype
slug: ace_adsgetkeytype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetkeytype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f147b9f25ef371cb853cd96fb19fb4441e6a6ea7
---

# Ace Adsgetkeytype

AdsGetKeyType

AdsGetKeyType

Advantage Client Engine

| AdsGetKeyType  Advantage Client Engine |  |  |  |  |

Returns the Advantage Client Engine data type of the evaluated index keys.

Syntax

| UNSIGNED32 | AdsGetKeyType (ADSHANDLE hIndex,  UNSIGNED16 \*pusType); |

Parameters

| hIndex (I) | Handle of an index order. |
| pusType (O) | Returns the data type of keys in this index order. |

Remarks

Returns the data type of the key as evaluated by the Advantage Client Engine. Possible key types are ADS\_STRING, ADS\_NUMERIC, ADS\_DATE, ADS\_LOGICAL, and ADS\_RAW. ADS\_RAW is returned for any index that uses the binary concatenation operator (;) and for indexes created on time, timestamp, and raw fields.

Example

None.

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsGetIndexExpr](ace_adsgetindexexpr.md)

[AdsGetKeyLength](ace_adsgetkeylength.md)
