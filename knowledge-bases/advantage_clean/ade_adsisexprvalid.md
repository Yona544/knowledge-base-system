---
title: Ade Adsisexprvalid
slug: ade_adsisexprvalid
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisexprvalid.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 1757abcef7313d60e739c3290ce2abdb1fcd037c
---

# Ade Adsisexprvalid

AdsIsExprValid

TAdsTable.AdsIsExprValid

Advantage TDataSet Descendant

| TAdsTable.AdsIsExprValid  Advantage TDataSet Descendant |  |  |  |  |

Determines if a filter or index expression is valid.

Syntax

function AdsIsExprValid( strExpression : String ) : Boolean;

Parameter

| strExpression | Expression to check. |

Description

AdsIsExprValid tests whether an expression can be handled by the Advantage Expression Engine. If not, the return value will be False. If the expression is not valid, an application can call AdsGetLastError to retrieve the specific error code that will indicate why the expression is not valid. Note that if the table type is not ttAdsADT and the expression contains the binary concatenation operator (e.g., 'lastname;firstname') or data types that are specific to ADT tables, then the return value will be False.

Example

strExpression := 'LastName < "C" AND DeptNum < 60 AND Left( FirstName, 1 ) == "A"';

if (AdsTable1.AdsIsExprValid( strExpression )) then

AdsTable1.AdsSetFilter( strExpression );

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsLocate](ade_adslocate.md)

[AdsSetFilter](ade_adssetfilter.md)
