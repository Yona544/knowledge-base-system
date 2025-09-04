---
title: Ace Adsgetbookmark
slug: ace_adsgetbookmark
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetbookmark.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 430f525d8d21d87aff3dc72d71d7f36a41818e7b
---

# Ace Adsgetbookmark

AdsGetBookmark

AdsGetBookmark

Advantage Client Engine

| AdsGetBookmark  Advantage Client Engine |  |  |  |  |

Retrieves a bookmark for a later call to AdsGotoBookmark

Syntax

| UNSIGNED32 | AdsGetBookmark (ADSHANDLE hTable,  ADSHANDLE \*phBookmark); |

Parameters

| hTable (I) | Handle of table or cursor. |
| PhBookmark (O) | Return a handle that refers to the current record. |

Remarks

AdsGetBookmark returns the physical record number. It is the equivalent of [AdsGetRecordNum](ace_adsgetrecordnum.md) called with ADS\_IGNOREFILTERS.

Example

[Click Here](ace_examples.md#adsgetbookmarkexample)

See Also

[AdsGotoBookmark](ace_adsgotobookmark.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)

[AdsGotoRecord](ace_adsgotorecord.md)
