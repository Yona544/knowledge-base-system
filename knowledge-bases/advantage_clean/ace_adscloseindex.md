---
title: Ace Adscloseindex
slug: ace_adscloseindex
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscloseindex.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 9da7d0b994f1ee3e3a7eacb8133ee80bbd8cf7dd
---

# Ace Adscloseindex

AdsCloseIndex

AdsCloseIndex

Advantage Client Engine

| AdsCloseIndex  Advantage Client Engine |  |  |  |  |

Closes an index order.

Syntax

| UNSIGNED32 | AdsCloseIndex (ADSHANDLE hIndex); |

Parameters

| hIndex (I) | Handle of index order to close. If this is the handle of an index order (tag) within a compound index file, then the file is closed. The file is not deleted. |

Remarks

It is not possible to close an AutoOpen index. Any attempts to use an index handle that is closed with an Advantage Client Engine function will result in AE\_INVALID\_INDEX\_HANDLE being returned. The index file can be reopened as long as the table it is associated with is open.

Note Updating data in a table without all associated indexes being opened can result in index corruption. If such corruption occurs, it can be repaired by calling [AdsReindex](ace_adsreindex.md) on the table handle.

 

Note It is illegal to close an index order during a transaction.

Example

[Click Here](ace_examples.md#adscloseindexexample)

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsCloseAllIndexes](ace_adscloseallindexes.md)
