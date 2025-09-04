---
title: Ace Adsgotobookmark
slug: ace_adsgotobookmark
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgotobookmark.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 770c732614d6f7bbe86713b13b28c33282e3c6cb
---

# Ace Adsgotobookmark

AdsGotoBookmark

AdsGotoBookmark

Advantage Client Engine

| AdsGotoBookmark  Advantage Client Engine |  |  |  |  |

Positions the given table to the given bookmark

Syntax

| UNSIGNED32 | AdsGotoBookmark (ADSHANDLE hTable,  ADSHANDLE hBookmark); |

Parameters

| hTable (I) | Handle of table or cursor. |
| hBookmark (I) | Bookmark from a call to AdsGetBookmark. |

Remarks

This function is equivalent to [AdsGotoRecord](ace_adsgotorecord.md). Currently, hBookmark as returned from AdsGetBookmark is the record number.

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

Example

[Click Here](ace_examples.md#adsgotobookmarkexample)

See Also

[AdsGetBookmark](ace_adsgetbookmark.md)

[AdsGotoRecord](ace_adsgotorecord.md)
