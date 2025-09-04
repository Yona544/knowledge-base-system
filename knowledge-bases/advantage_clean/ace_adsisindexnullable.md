---
title: Ace Adsisindexnullable
slug: ace_adsisindexnullable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexnullable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c4eaff68b7b99ac3e4a717d7d71364d5a36caf9b
---

# Ace Adsisindexnullable

AdsIsIndexNullable

AdsIsIndexNullable

Advantage Client Engine

| AdsIsIndexNullable  Advantage Client Engine |  |  |  |  |

Determines if the given index order is nullable.

Syntax

| UNSIGNED32 | AdsIsIndexNullable ( ADSHANDLE hIndex,  UNSIGNED16 \*pbNullable ); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbNullable (O) | Return True if it is a nullable index. |

Remarks

AdsIsNullable determines whether or not an index order was created on a nullable key. A nullable key is one that can evaluate to NULL.

Note AdsIsIndexNullable can only be called on indexes of ADS\_VFP tables.

Example

ulRetCode = AdsIsIndexNullable( hIndex, &usNullable );

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)
