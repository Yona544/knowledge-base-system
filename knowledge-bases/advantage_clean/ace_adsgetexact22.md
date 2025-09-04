---
title: Ace Adsgetexact22
slug: ace_adsgetexact22
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetexact22.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: eddaf6e6dd8ff7358902c8721a8ccbfa4a4e62a1
---

# Ace Adsgetexact22

AdsGetExact22

AdsGetExact22

Advantage Client Engine

| AdsGetExact22  Advantage Client Engine |  |  |  |  |

Retrieves the "exact" setting

Syntax

| UNSIGNED32 | AdsGetExact22 (ADSHANDLE hObj,  UNSIGNED16 \*pbExact); |

Parameters

| hObj (I) | Handle of a table or connection. If this is 0, the result is the same as calling AdsGetExact. |
| pbExact (O) | Returns the current "exact" setting. |

Remarks

If a connection handle is specified in hObj, AdsGetExact22 returns the "exact" setting of the connection. The connection's "exact" setting is the default "exact" setting for tables that will be opened in the future on the specified connection. The connection's "exact" setting also affects string comparisons in index expressions in indexes created on tables opened on the connection.

If a table handle is specified in hObj, AdsGetExact22 returns the "exact" setting of the table. The "exact" setting of the table affects string comparisons in traditional record filters set via AdsSetFilter and string comparisons in Advantage Optimized Filters set via AdsSetAOF.

If 0 (zero) is specified in hObj, AdsGetExact22 is equivalent to AdsGetExact which returns the default "exact" settings used on new connections.

Note AdsGetExact22 expands the functionality available in AdsGetExact with the addition of a parameter for specifying a table or connection. Since a new parameter was added, a new API had to be created. The "22" indicates the Advantage Client Engine version (i.e., version 2.2) in which this new supplementary API was first available.

Example

[Click Here](ace_more_examples.md#adsgetexact22_example)

See Also

[AdsSetExact22](ace_adssetexact22.md)

[AdsSetFilter](ace_adssetfilter.md)

[AdsSetAOF](ace_adssetaof.md)

[AdsSetExact](ace_adssetexact.md)
