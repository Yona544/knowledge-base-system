---
title: Ade Adsgetindexexpr
slug: ade_adsgetindexexpr
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetindexexpr.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 477d41a624141524840d420c8766ce5f45db7234
---

# Ade Adsgetindexexpr

AdsGetIndexExpr

TAdsTable.AdsGetIndexExpr

Advantage TDataSet Descendant

| TAdsTable.AdsGetIndexExpr  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the index key expression of this index order.

Syntax

function AdsGetIndexExpr : String;

Description

The index expression returned by AdsGetIndexExpr is the expression evaluated against records in the table to generate index keys. This expression can evaluate to a numeric value, a string value, a date, or a logical.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

AdsTable1.IndexName := 'Tag1';

 

strExpression := AdsTable1.AdsGetIndexExpr;

{ strExpression equals LASTNUM;DEPTNUM }

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsIsExprValid](ade_adsisexprvalid.md)

[AdsOpenIndex](ade_adsopenindex.md)
