---
title: Ace Adscloseallindexes
slug: ace_adscloseallindexes
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscloseallindexes.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 73f891bb6410dd40af7c5ce854fff1ae4e9d8013
---

# Ace Adscloseallindexes

AdsCloseAllIndexes

AdsCloseAllIndexes

Advantage Client Engine

| AdsCloseAllIndexes  Advantage Client Engine |  |  |  |  |

Closes all index orders for a given table.

Syntax

| UNSIGNED32 | AdsCloseAllIndexes (ADSHANDLE hTable); |

Parameters

| hTable (I) | Close all indexes for this table or cusor. |

Remarks

It is not possible to close an AutoOpen index. If the table has an AutoOpen index, AdsCloseAllIndexes will return SUCCESS, but index order handles from the AutoOpen index will still be valid.

Note Updating data in a table without all associated indexes being opened can result in index corruption. If such corruption occurs, it can be repaired by calling [AdsReindex](ace_adsreindex.md) on the table handle.

 

Note It is illegal to close all index orders during a transaction.

Example

[Click Here](ace_examples.md#adscloseallindexesexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsReindex](ace_adsreindex.md)
