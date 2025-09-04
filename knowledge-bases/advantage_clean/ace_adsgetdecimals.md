---
title: Ace Adsgetdecimals
slug: ace_adsgetdecimals
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetdecimals.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8e90b5c5d84e2b17f30c409122d4fd211a50aca0
---

# Ace Adsgetdecimals

AdsGetDecimals

AdsGetDecimals

Advantage Client Engine

| AdsGetDecimals  Advantage Client Engine |  |  |  |  |

Retrieves the decimals setting

Syntax

| UNSIGNED32 | AdsGetDecimals (UNSIGNED16 \*pusDecimals); |

Parameters

| pusDecimals (O) | Returns the current decimals setting. |

Remarks

AdsGetDecimals will return the current decimals setting. The value returned is either the default or the latest value set through the [AdsSetDecimals](ace_adssetdecimals.md) function.

AdsGetDecimals is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.md#adsgetdecimalsexample)

See Also

[AdsSetDecimals](ace_adssetdecimals.md)

[AdsCreateIndex](ace_adscreateindex.md)
