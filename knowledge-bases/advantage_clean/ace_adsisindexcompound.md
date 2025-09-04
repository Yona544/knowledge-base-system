---
title: Ace Adsisindexcompound
slug: ace_adsisindexcompound
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexcompound.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 92f68b6b111be3041f6dd6f76736bfa6a809a909
---

# Ace Adsisindexcompound

AdsIsIndexCompound

AdsIsIndexCompound

Advantage Client Engine

| AdsIsIndexCompound  Advantage Client Engine |  |  |  |  |

Determines if the given index order is from a compound index file.

Syntax

| UNSIGNED32 | AdsIsIndexCompound (ADSHANDLE hIndex,  UNSIGNED16 \*pbCompound); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbCompound (O) | Returns True if index order is from a compound index file. |

Remarks

AdsIsIndexCompound will return True only if the index order specified is in a compound index file (a Foxpro-compatible CDX file or Advantage proprietary ADI file). Indexes built with NTX and FoxPro-compatible IDX files are not compound indexes.

Example

[Click Here](ace_examples.md#adsisindexcompoundexample)

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)
