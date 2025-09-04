---
title: Ace Adssetdecimals
slug: ace_adssetdecimals
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetdecimals.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 35305c8806b817e66cb92a92ce7dbb5f37311797
---

# Ace Adssetdecimals

AdsSetDecimals

AdsSetDecimals

Advantage Client Engine

| AdsSetDecimals  Advantage Client Engine |  |  |  |  |

Controls the resulting number of decimal places in a division, modulus, or exponentiation operation in an index or filter expression evaluated in the expression engine

Syntax

| UNSIGNED32 | AdsSetDecimals (UNSIGNED16 usDecimals); |

Parameters

| usDecimals (I) | Number of decimals. The default is 2. |

Remarks

AdsSetDecimals determines the number of decimal places saved in the results of numeric functions and calculations.

AdsSetDecimals is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.md#adssetdecimalsexample)

See Also

[AdsGetDecimals](ace_adsgetdecimals.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsSetFilter](ace_adssetfilter.md)

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsBuildRawKey](ace_adsbuildrawkey.md)
