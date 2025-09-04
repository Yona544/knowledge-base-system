---
title: Ace Adsgetindexhandle
slug: ace_adsgetindexhandle
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexhandle.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fc096592c63100b3c0f096b3fca926e8a61d9c4f
---

# Ace Adsgetindexhandle

AdsGetIndexHandle

AdsGetIndexHandle

Advantage Client Engine

| AdsGetIndexHandle  Advantage Client Engine |  |  |  |  |

Retrieves the handle of an index order given the index order name.

Syntax

| UNSIGNED32 | AdsGetIndexHandle (ADSHANDLE hTable,  UNSIGNED8 \*pucIndexOrder,  ADSHANDLE \*phIndex); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucIndexOrder (I) | Name of index order for which to search. |
| phIndex (O) | Return index order handle corresponding to given name. |

Special Return Codes

| AE\_INVALID\_INDEX\_ORDER\_NAME | The index order name given is invalid. |

Remarks

For non-compound indexes, the index order name is the base of the filename (up to 8 characters). For compound indexes, the index order name is the tag name (up to 10 characters).

If there is more than one index order open with the same name, the Advantage Client Engine will return the first one it finds.

Example

[Click Here](ace_examples.md#adsgetindexhandleexample)

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsGetIndexName](ace_adsgetindexname.md)
