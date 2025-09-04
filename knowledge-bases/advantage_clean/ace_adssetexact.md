---
title: Ace Adssetexact
slug: ace_adssetexact
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetexact.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 9ac268865a369ac6e7d30b78a6996409a2684b11
---

# Ace Adssetexact

AdsSetExact

AdsSetExact

Advantage Client Engine

| AdsSetExact  Advantage Client Engine |  |  |  |  |

Affects how string comparisons are performed with certain relational operators

Syntax

| UNSIGNED32 | AdsSetExact( UNSIGNED16 bIgnoreSpaces ); |

Parameters

| bIgnoreSpaces (I) | A non-zero value causes string comparisons with certain relational operators to ignore trailing spaces. The default is False. |

Remarks

The AdsSetExact setting affects how string comparisons are performed with the relational operators =, >, <, >=, and <=. The exact equal, ==, operator is not affected by this setting. In general, if the AdsSetExact setting is True, trailing spaces are ignored during the comparison. The AdsSetExact setting is not that simple, however. It is somewhat complex and affects the various relational operators differently. See [Expression Engine Operators](master_expression_engine_operators.md) for detailed information on how the AdsSetExact setting affects relational operators.

AdsSetExact will affect string comparisons for all currently opened tables and all tables opened in the future for all connections. Changing the exact setting via AdsSetExact has an immediate effect on all string comparisons in existing traditional record filters set via AdsSetFilter, but has no effect on existing Advantage Optimized Filters set via AdsSetAOF until AdsRefreshAOF is called. Changing the set exact setting via AdsSetExact also affects all string comparisons in index expressions.

Note AdsSetExact does not affect [AdsSeek](ace_adsseek.md).

 

Note AdsSetExact affects all tables on all connections. See [AdsSetExact22](ace_adssetexact22.md) for information on how to set "exact" on the individual table or connection.

Example

[Click Here](ace_examples.md#adssetexactexample)

See Also

[AdsSetExact22](ace_adssetexact22.md)

[AdsGetExact22](ace_adsgetexact22.md)

[AdsGetExact](ace_adsgetexact.md)

[AdsSetFilter](ace_adssetfilter.md)

[AdsSetAOF](ace_adssetaof.md)
