---
title: Ace Adsdeleteindex
slug: ace_adsdeleteindex
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdeleteindex.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 6208aa3a9a5bfb2ef20a056b4c0a65d1b4b26429
---

# Ace Adsdeleteindex

AdsDeleteIndex

AdsDeleteIndex

Advantage Client Engine

| AdsDeleteIndex  Advantage Client Engine |  |  |  |  |

Deletes the given index order.

Syntax

| UNSIGNED32 | AdsDeleteIndex (ADSHANDLE hIndex); |

Parameters

| hIndex (I) | Handle of index order to delete. If it is the only index order (tag) in a compound index file or if it is an index order in a non-compound index file, the file will be deleted as well. |

Remarks

If the index order is a tag in a CDX or ADI, the tag will be marked for deletion and will no longer be used. If it is the last non-deleted tag in the file, the file will be deleted. If the index order is an IDX or NTX, the file will be deleted. Remove deleted tags out of compound index files by reindexing (see [AdsReindex](ace_adsreindex.md) ).

Note It is illegal to delete an index order during a transaction.

Example

[Click Here](ace_examples.md#adsdeleteindexexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCloseIndex](ace_adscloseindex.md)
