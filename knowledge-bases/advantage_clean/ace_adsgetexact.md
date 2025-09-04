---
title: Ace Adsgetexact
slug: ace_adsgetexact
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetexact.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 36bb371466bec00b90cc642cbcb738917e583afe
---

# Ace Adsgetexact

AdsGetExact

AdsGetExact

Advantage Client Engine

| AdsGetExact  Advantage Client Engine |  |  |  |  |

Retrieves the "exact" setting

Syntax

| UNSIGNED32 | AdsGetExact (UNSIGNED16 \*pbExact); |

Parameters

| pbExact (O) | Return the current "exact" setting. |

Remarks

AdsGetExact returns the global "exact" setting for the current application. The global "exact" setting is the default "exact" setting for any new connections. The "exact" setting affects how string comparisons are performed with the relational operators =, >, <, >=, and <=.

Example

[Click Here](ace_examples.md#adsgetexactexample)

See Also

[AdsSetExact](ace_adssetexact.md)

[AdsSetFilter](ace_adssetfilter.md)

[AdsSetAOF](ace_adssetaof.md)

[AdsGetExact22](ace_adsgetexact22.md)
