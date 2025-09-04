---
title: Ace Adsisindexcustom
slug: ace_adsisindexcustom
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexcustom.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fc68dee7ff2d397a91cf5b30f4824e9d410531c7
---

# Ace Adsisindexcustom

AdsIsIndexCustom

AdsIsIndexCustom

Advantage Client Engine

| AdsIsIndexCustom  Advantage Client Engine |  |  |  |  |

Determines if the given index order was built as a custom index.

Syntax

| UNSIGNED32 | AdsIsIndexCustom (ADSHANDLE hIndex,  UNSIGNED16 \*pbCustom); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbCustom (O) | Return True if it is a custom index order. |

Special Return Codes

| AE\_INVALID\_INDEX\_TYPE | NTX indexes cannot be custom. |

Remarks

A custom index is built without keys. Keys are added to the custom index explicitly by calls to [AdsAddCustomKey](ace_adsaddcustomkey.md) and [AdsDeleteCustomKey](ace_adsdeletecustomkey.md). This allows a user to build a very small and specific index.

Custom indexes can only be built on tables opened with the ADS\_CDX or ADS\_ADT option.

Example

[Click Here](ace_examples.md#adsisindexcustomexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsAddCustomKey](ace_adsaddcustomkey.md)

[AdsDeleteCustomKey](ace_adsdeletecustomkey.md)
