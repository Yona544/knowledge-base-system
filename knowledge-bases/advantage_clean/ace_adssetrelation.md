---
title: Ace Adssetrelation
slug: ace_adssetrelation
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetrelation.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c3b351896a03ccb7bc3956568a131c487aeae4aa
---

# Ace Adssetrelation

AdsSetRelation

AdsSetRelation

Advantage Client Engine

| AdsSetRelation  Advantage Client Engine |  |  |  |  |

Sets a parent/child relation on the two tables

Syntax

| UNSIGNED32 | AdsSetRelation (ADSHANDLE hTableParent,  ADSHANDLE hIndexChild,  UNSIGNED8 \*pucExpr); |

Parameters

| hTblParent (I) | Handle of parent table in relation. |
| hIndexChild (I) | Handle of child index order (not table) in relation. |
| pucExpr (I) | Expression given as a null terminated string to use for the relation. The result of this expression should result in a key that matches a key in hIndexChild. |

Remarks

AdsSetRelation associates a "child" table to a "parent" through the childs index. When the users application performs a record movement in the parent table (e.g. [AdsSkip](ace_adsskip.md) or [AdsSeek](ace_adsseek.md)), the childs current record is logically positioned. The Advantage Client Engine performs the actual movement in the child table on demand for efficiency purposes rather than with each parent movement. The child record position is determined by seeking for a key resulting from evaluating the expression (pucExpr) against the parent tables current record. The expression must be one that can be evaluated by the [Advantage Expression Engine](master_advantage_expression_engine.md). The child is repositioned after the parent moves, but it is valid to navigate anywhere in the child table between movements in the parent. Cyclic relations are not allowed because a cycle would result in an infinite Seek loop.

Example

[Click Here](ace_examples.md#adssetrelationexample)

See Also

[AdsSetScope](ace_adssetscope.md)

[AdsSetScopedRelation](ace_adssetscopedrelation.md)

[AdsClearScope](ace_adsclearscope.md)

[AdsClearRelation](ace_adsclearrelation.md)
