---
title: Ace Adsisexprvalid
slug: ace_adsisexprvalid
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisexprvalid.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 020fe06469f00ecfcca8c0ad85b8535aa0d8296e
---

# Ace Adsisexprvalid

AdsIsExprValid

AdsIsExprValid

Advantage Client Engine

| AdsIsExprValid  Advantage Client Engine |  |  |  |  |

Determines if a filter or index expression is valid

Syntax

| UNSIGNED32 | AdsIsExprValid (ADSHANDLE hTable,  UNSIGNED8 \*pucExpr,  UNSIGNED16 \*pbValid); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucExpr (I) | Expression to check. |
| pbValid (O) | Set to True if expression is valid. |

Remarks

AdsIsExprValid tests whether an expression can be handled by the Advantage Expression Engine. If the expression is not valid, an application can call AdsGetLastError to retrieve the specific error code that will indicate why the expression is not valid. If the table type is not ADS\_ADT and the expression contains the binary concatenation operator (e.g., "lastname;firstname") or data types that are specific to ADT tables, then pbValid will be set to False.

Example

[Click Here](ace_examples.md#adsisexprvalidexample)

See Also

[AdsSetFilter](ace_adssetfilter.md)

[AdsLocate](ace_adslocate.md)

[AdsCreateIndex](ace_adscreateindex.md)
