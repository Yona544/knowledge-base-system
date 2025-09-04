---
title: Ace Adsgetindexhandlebyexpr
slug: ace_adsgetindexhandlebyexpr
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexhandlebyexpr.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5f1ab118185e207ca4f49a32ace1e6a5da681c67
---

# Ace Adsgetindexhandlebyexpr

AdsGetIndexHandleByExpr

AdsGetIndexHandleByExpr

Advantage Client Engine

| AdsGetIndexHandleByExpr  Advantage Client Engine |  |  |  |  |

Retrieves the index handle given the indexs expression

Syntax

| UNSIGNED32 | AdsGetIndexHandleByExpr( ADSHANDLE hTbl,  UNSIGNED8\*pucExpr,  UNSIGNED32 ulDescending,  ADSHANDLE \*phIndex ) |

Parameters

| hTbl (I) | Handle of a table. |
| pucExpr (I) | Expression to retrieve index handle for. |
| ulDescending (I) | ADS\_ASCENDING or ADS\_DESCENDING. AdsGetIndexHandleByExpr will find the index with the expression that is of the same "scending" value. |
| phIndex (O) | Handle of an index order. |

Remarks

This function returns the index handle corresponding to the indicated index expression.

Example

[Click Here](ace_examples.md#adsgetindexhandlebyexprexample)

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)

[AdsGetIndexHandleByOrder](ace_adsgetindexhandlebyorder.md)

[AdsGetIndexName](ace_adsgetindexname.md)
