---
title: Ace Adsgetallindexes
slug: ace_adsgetallindexes
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetallindexes.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2963e5d5450be8a74affc267086f9a6daaba4ac1
---

# Ace Adsgetallindexes

AdsGetAllIndexes

AdsGetAllIndexes

Advantage Client Engine

| AdsGetAllIndexes  Advantage Client Engine |  |  |  |  |

Returns an array of open index order handles for the given table.

Syntax

| UNSIGNED32 | AdsGetAllIndexes (ADSHANDLE hTable,  ADSHANDLE ahIndex[],  UNSIGNED16 \*pusArrayLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| ahIndex[] (O) | Return index order handles in the given array. |
| pusArrayLen (I/O) | Number of entries (not bytes) in the array on input, number of returned entries on output. |

Remarks

The index order handles are returned in the order they were opened. For CDX and ADI indexes, the index order handles are returned in the order they were created within the index file. If the array passed to this function is insufficient for all index handles, the array will be filled with all handles that fit, the pusArrayLen parameter will return the number of available handles, and the function will return the error code AE\_INSUFFICIENT\_BUFFER. AdsGetAllIndexes does not return information for full text information in full text search indexes.

Example

[Click Here](ace_examples.md#adsgetallindexesexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsGetNumIndexes](ace_adsgetnumindexes.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)

[AdsGetFTSIndexes](ace_adsgetftsindexes.md)
