---
title: Ace Adsisindexcandidate
slug: ace_adsisindexcandidate
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexcandidate.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 80f2e0b24e7cd20652ba13c6f98dca35a7f526bc
---

# Ace Adsisindexcandidate

AdsIsIndexCandidate

AdsIsIndexCandidate

Advantage Client Engine

| AdsIsIndexCandidate  Advantage Client Engine |  |  |  |  |

Determines if the given index order is a candidate index.

Syntax

| UNSIGNED32 | AdsIsIndexCandidate ( ADSHANDLE hIndex,  UNSIGNED16 \*pbCandidate ); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbCandidate (O) | Return True if it is a candidate index. |

Remarks

AdsIsIndexCandidate returns whether or not an index order was created with the ADS\_CANDIDATE option.

Note AdsIsIndexCandidate can only be called on indexes of ADS\_ADT or ADS\_VFP tables.

Example

ulRetCode = AdsIsIndexCandidate( hIndex, &usCandidate );

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsIsIndexUnique](ace_adsisindexunique.md)
