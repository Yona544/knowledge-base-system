---
title: Ace Adsgotobookmark60
slug: ace_adsgotobookmark60
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgotobookmark60.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b42fe96e9c2c945e92aac4de1c1f9141ffe3d2ea
---

# Ace Adsgotobookmark60

AdsGotoBookmark60

AdsGotoBookmark60

Advantage Client Engine

| AdsGotoBookmark60  Advantage Client Engine |  |  |  |  |

Positions the given table to the given bookmark.

Syntax

| UNSIGNED32 | AdsGotoBookmark60 (ADSHANDLE hObj,  UNSIGNED8 \*pucBookmark); |

Parameters

| hObj (I) | Handle of table or cursor. |
| pucBookmark (I) | Bookmark from a call to AdsGetBookmark60. |

Remarks

Position the table/cursor to the bookmark previously retrieved from a call to [AdsGetBookmark60](ace_adsgetbookmark60.md).

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

See Also

[AdsGetBookmark60](ace_adsgetbookmark60.md)

[AdsGetBookmarkLength](ace_adsgetbookmarklength.md)

[AdsCompareBookmarks](ace_adscomparebookmarks.md)
