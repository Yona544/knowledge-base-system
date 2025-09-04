---
title: Ace Adsgetftsindexes
slug: ace_adsgetftsindexes
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetftsindexes.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d9ae5db04c21a90bb5f0572b23e24fdcc8e6de9a
---

# Ace Adsgetftsindexes

AdsGetFTSIndexes

AdsGetFTSIndexes

Advantage Client Engine

| AdsGetFTSIndexes  Advantage Client Engine |  |  |  |  |

Returns an array of full text search index order handles for the given table.

Syntax

UNSIGNED32 AdsGetFTSIndexes ( ADSHANDLE hTable, ADSHANDLE ahIndex[],

UNSIGNED16 \*pusArrayLen );

Parameters

| hTable (I) | Handle of table. |
| ahIndex (O) | Return index order handles in the given array. |
| pusArrayLen (I/O) | Number of entries (not bytes) in the array on input, number of returned entries on output. |

Remarks

This API returns the full text search indexes that are currently open on the given table. If the array passed to this function is insufficient for all index handles, the array will be filled with all handles that fit, the pusArrayLen parameter will return the number of available handles, and the function will return the error code AE\_INSUFFICIENT\_BUFFER. Use AdsGetNumFTSIndexes before calling this API to determine how many will be returned.

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.md)

[AdsGetNumFTSIndexes](ace_adsgetnumftsindexes.md)

[AdsGetAllIndexes](ace_adsgetallindexes.md)
