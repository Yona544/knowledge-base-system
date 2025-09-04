---
title: Ace Adsclearrelation
slug: ace_adsclearrelation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclearrelation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 719bcbfd973745fb44d637a837d0c73d234814e2
---

# Ace Adsclearrelation

AdsClearRelation

AdsClearRelation

Advantage Client Engine

| AdsClearRelation  Advantage Client Engine |  |  |  |  |

Clears all relations for the given parent table

Syntax

| UNSIGNED32 | AdsClearRelation (ADSHANDLE hTableParent); |

Parameters

| hTableParent (I) | Handle of parent table. |

Remarks

This function clears relations set by [AdsSetRelation](ace_adssetrelation.md) and [AdsSetScopedRelation](ace_adssetscopedrelation.md). If this table is the child in another relation, that relation is not cleared.

Example

[Click Here](ace_examples.md#adsclearrelationexample)

See Also

[AdsSetRelation](ace_adssetrelation.md)

[AdsSetScopedRelation](ace_adssetscopedrelation.md)
