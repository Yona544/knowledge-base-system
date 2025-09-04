---
title: Ace Adsclearallscopes
slug: ace_adsclearallscopes
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearallscopes.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 06c850a9a40ee8d9af71ddb9b5083b090be00f0d
---

# Ace Adsclearallscopes

AdsClearAllScopes

AdsClearAllScopes

Advantage Client Engine

| AdsClearAllScopes  Advantage Client Engine |  |  |  |  |

Clears scopes on all indexes open for the given table

Syntax

| UNSIGNED32 | AdsClearAllScopes (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table or cursor. |

Remarks

This function will clear both top and bottom scopes for all index orders open for this table.

Example

[Click Here](ace_examples.md#adsclearallscopesexample)

See Also

[AdsSetScope](ace_adssetscope.md)

[AdsClearScope](ace_adsclearscope.md)

[AdsGetScope](ace_adsgetscope.md)
