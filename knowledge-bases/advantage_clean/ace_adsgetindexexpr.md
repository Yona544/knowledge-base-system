---
title: Ace Adsgetindexexpr
slug: ace_adsgetindexexpr
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexexpr.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0c3175edf7e26801063cbe64bb7c5ed16c02f03f
---

# Ace Adsgetindexexpr

AdsGetIndexExpr

AdsGetIndexExpr

Advantage Client Engine

| AdsGetIndexExpr  Advantage Client Engine |  |  |  |  |

Retrieves the index key expression of this index order.

Syntax

| UNSIGNED32 | AdsGetIndexExpr (ADSHANDLE hIndex,  UNSIGNED8 \*pucKeyExpr,  UNSIGNED16 \*pusLen); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pucKeyExpr (O) | Returns the index order key expression in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

The index expression returned by AdsGetIndexExpr is the expression that is evaluated against records in the table to generate index keys. This expression can evaluate to a numeric value, a string value, a date, or a logical.

Example

[Click Here](ace_examples.md#adsgetindexexprexample)

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsIsExprValid](ace_adsisexprvalid.md)
