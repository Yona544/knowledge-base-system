---
title: Ace Adslocate
slug: ace_adslocate
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adslocate.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 12ba7e07552303237099b37dbad1b75712c94e81
---

# Ace Adslocate

AdsLocate

AdsLocate

Advantage Client Engine

| AdsLocate  Advantage Client Engine |  |  |  |  |

Performs a sequential search for a record that matches the given expression

Syntax

| UNSIGNED32 | AdsLocate (ADSHANDLE hTable,  UNSIGNED8 \*pucExpr,  UNSIGNED16 bForward,  UNSIGNED16 \*pbFound); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucExpr (I) | Expression that defines desired records. |
| bForward (I) | If True, then search forward. If False, search backward. |
| pbFound (O) | Return True (1) if record found. |

Remarks

AdsLocate performs an exhaustive search of the table for records that meet the given expression. The expression given must evaluate to True or False. AdsLocate and AdsContinue do respect any filters set on the table, therefore, for best performance set a filter before calling this function. If the bForward parameter is True, the search is performed from the top of the table. Subsequent calls to [AdsContinue](ace_adscontinue.md) search in the same direction as the AdsLocate call.

If there is an existing index order, it is much more efficient to perform an indexed seek using [AdsSeek](ace_adsseek.md) than to perform an AdsLocate. If there is not an existing index order, it would be faster to call [AdsSetFilter](ace_adssetfilter.md) and use [AdsSkip](ace_adsskip.md) to step through the records because the server performs the filtering.

Example

[Click Here](ace_examples.md#adslocateexample)

See Also

[AdsIsFound](ace_adsisfound.md)

[AdsContinue](ace_adscontinue.md)

[AdsSeek](ace_adsseek.md)
