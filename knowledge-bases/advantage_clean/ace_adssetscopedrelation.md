---
title: Ace Adssetscopedrelation
slug: ace_adssetscopedrelation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetscopedrelation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d4dbbe6923015c80f353db8ec1aa99477e635d30
---

# Ace Adssetscopedrelation

AdsSetScopedRelation

AdsSetScopedRelation

Advantage Client Engine

| AdsSetScopedRelation  Advantage Client Engine |  |  |  |  |

Sets a relation that causes a scope to be set on the child with each parent movement

Syntax

| UNSIGNED32 | AdsSetScopedRelation (ADSHANDLE hTableParent,  ADSHANDLE hIndexChild,  UNSIGNED8 \*pucExpr); |

Parameters

| hTableParent (I) | Handle of parent table in relation. |
| hIndexChild (I) | Handle of child index order (not child) in relation. |
| pucExpr (I) | Expression to use for the relation. |

Remarks

In addition to performing the same functionality as [AdsSetRelation](ace_adssetrelation.md), AdsSetScopedRelation sets a scope on the child table with each movement of the parent table. The high and low value of the scope will be the same and will be the key from the current parent record. Movement in the child table using the child tables handle will ignore relations. Movement using the child index order will obey the scope set by the relation.

Note Any existing scope set with [AdsSetScope](ace_adssetscope.md) on the child table will be cleared by AdsSetScoped Relation. Scopes set by a relation are not cleared by calling [AdsClearRelation](ace_adsclearrelation.md).

Example

[Click Here](ace_examples.md#adssetscopedrelationexample)

See Also

[AdsClearScope](ace_adsclearscope.md)

[AdsSetRelation](ace_adssetrelation.md)

[AdsClearRelation](ace_adsclearrelation.md)
