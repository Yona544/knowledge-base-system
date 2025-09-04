---
title: Ace Adsgetnumindexes
slug: ace_adsgetnumindexes
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetnumindexes.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 65e5e77cb97bb5eb28d58d69d6da47082c34d363
---

# Ace Adsgetnumindexes

AdsGetNumIndexes

AdsGetNumIndexes

Advantage Client Engine

| AdsGetNumIndexes  Advantage Client Engine |  |  |  |  |

Retrieves the total number of open index orders associated with the given table.

Syntax

| UNSIGNED32 | AdsGetNumIndexes (ADSHANDLE hTable,  UNSIGNED16 \*pusNum); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pusNum (O) | Return number of index orders. For example, if the user opened a CDX file with 5 tags and an IDX, this function would return the total 6. |

Remarks

The number of indexes returned does not necessarily correspond to the number of index files opened for the table. A compound index may contain multiple index orders. Calling this function before calling [AdsGetAllIndexes](ace_adsgetallindexes.md) will provide the number of index orders that will be returned. AdsGetNumIndexes does not return information for full text search indexes.

Example

[Click Here](ace_examples.md#adsgetnumindexesexample)

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsGetAllIndexes](ace_adsgetallindexes.md)

[AdsGetNumFTSIndexes](ace_adsgetnumftsindexes.md)
