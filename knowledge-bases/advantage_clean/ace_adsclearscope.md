---
title: Ace Adsclearscope
slug: ace_adsclearscope
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearscope.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d00372c158d46a540009175bb0f23f4be7b74bb9
---

# Ace Adsclearscope

AdsClearScope

AdsClearScope

Advantage Client Engine

| AdsClearScope  Advantage Client Engine |  |  |  |  |

Clears scope on the given index order.

Syntax

| UNSIGNED32 | AdsClearScope (ADSHANDLE hIndex,  UNSIGNED16 usScopeOption); |

Parameters

| hIndex (I) | Handle index order. |
| usScopeOption (I) | Indicates which scope value to clear. Options are ADS\_TOP and ADS\_BOTTOM. |

Special Return Codes

| AE\_NO\_SCOPE | No scope was set, so a scope cannot be returned or cleared. |

Remarks

If the top or bottom scope is cleared, any other scope settings remain. If currently positioned at EOF or BOF and a scope is cleared, it is necessary to reposition by performing a movement to see any records.

Example

[Click Here](ace_examples.md#adsclearscopeexample)

See Also

[AdsSetScope](ace_adssetscope.md)

[AdsGetScope](ace_adsgetscope.md)

[AdsSeek](ace_adsseek.md)

[AdsSkip](ace_adsskip.md)

[AdsGotoTop](ace_adsgototop.md)

[AdsGotoBottom](ace_adsgotobottom.md)

[AdsClearAllScopes](ace_adsclearallscopes.md)
