---
title: Ade Adsgetkeytype
slug: ade_adsgetkeytype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetkeytype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3e77ff447a9e4e792461779bc8b610cde2d9a183
---

# Ade Adsgetkeytype

AdsGetKeyType

TAdsTable.AdsGetKeyType

Advantage TDataSet Descendant

| TAdsTable.AdsGetKeyType  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine data type of the evaluated index keys.

Syntax

type TAdsExpressionTypes = ( etLOGICAL, etNUMERIC, etDATE, etSTRING, etRAW );

 

function AdsGetKeyType : TAdsExpressionTypes;

Description

Returns the data type of the key as evaluated by the Advantage Client Engine. Possible key types are etSTRING, etNUMERIC, etDATE, etRAW, and etLOGICAL. etRAW is returned for any index that uses the binary concatenation operator ";" and for indexes created on time, timestamp, and raw fields.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.IndexName := 'Tag1';

eKeyType := AdsTable1.AdsGetKeyType;

{ eKeyType equals etString }

 

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

AdsTable1.IndexName := 'Tag2';

eKeyType := AdsTable1.AdsGetKeyType;

{ eKeyType equals etNUMERIC }

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsGetIndexExpr](ade_adsgetindexexpr.md)

[AdsGetKeyLength](ade_adsgetkeylength.md)

[AdsOpenIndex](ade_adsopenindex.md)
