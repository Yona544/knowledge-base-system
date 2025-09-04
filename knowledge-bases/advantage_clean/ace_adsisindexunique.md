---
title: Ace Adsisindexunique
slug: ace_adsisindexunique
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexunique.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 14dd1e31378a85a0c14d66d17c4b2ca71bf33f2f
---

# Ace Adsisindexunique

AdsIsIndexUnique

AdsIsIndexUnique

Advantage Client Engine

| AdsIsIndexUnique  Advantage Client Engine |  |  |  |  |

Determines if the given index order is unique.

Syntax

| UNSIGNED32 | AdsIsIndexUnique (ADSHANDLE hIndex,  UNSIGNED16 \*pbUnique); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbUnique (O) | Return True if index order was built with the ADS\_UNIQUE option. |

Remarks

A unique index will have no repeated key values.

Example

[Click Here](ace_examples.md#adsisindexuniqueexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsIsIndexCandidate](ace_adsisindexcandidate.md)
