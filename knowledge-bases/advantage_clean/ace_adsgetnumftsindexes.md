---
title: Ace Adsgetnumftsindexes
slug: ace_adsgetnumftsindexes
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetnumftsindexes.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e032c4036e3f6413314d76a8c7e6de556960febe
---

# Ace Adsgetnumftsindexes

AdsGetNumFTSIndexes

AdsGetNumFTSIndexes

Advantage Client Engine

| AdsGetNumFTSIndexes  Advantage Client Engine |  |  |  |  |

Retrieves the total number of full text search index orders associated with the given table.

Syntax

UNSIGNED32 AdsGetNumFTSIndexes ( ADSHANDLE hTable,

UNSIGNED16 \*pusNum );

Parameters

| hTable (I) | Handle of table. |
| pusNum (O) | Return number of full text search (FTS) index orders. |

Remarks

Use this API to determine how many full text search indexes exist in all open index files for the given table. Calling this function before calling AdsGetFTSIndexes will provide the number of index orders that will be returned.

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.md)

[AdsGetFTSIndexes](ace_adsgetftsindexes.md)

[AdsGetNumIndexes](ace_adsgetnumindexes.md)
