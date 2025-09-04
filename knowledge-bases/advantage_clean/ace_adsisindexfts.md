---
title: Ace Adsisindexfts
slug: ace_adsisindexfts
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexfts.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: afa428885c844a68c106e42e298560614b79f590
---

# Ace Adsisindexfts

AdsIsIndexFTS

AdsIsIndexFTS

Advantage Client Engine

| AdsIsIndexFTS  Advantage Client Engine |  |  |  |  |

Determines if the given index order is a full text search index.

Syntax

UNSIGNED32 AdsIsIndexFTS ( ADSHANDLE hIndex,

UNSIGNED16 \*pbFTS );

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbFTS (O) | Returns True if index order is an FTS index. |

Remarks

AdsIsIndexFTS will return True for the pbFTS parameter if the index order specified is an FTS index.

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.md)

[AdsGetFTSIndexInfo](ace_adsgetftsindexinfo.md)
