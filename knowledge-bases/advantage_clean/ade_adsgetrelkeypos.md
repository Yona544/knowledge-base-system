---
title: Ade Adsgetrelkeypos
slug: ade_adsgetrelkeypos
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetrelkeypos.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 01665f2a042fdc52acb246dc80c8816bda7e1088
---

# Ade Adsgetrelkeypos

AdsGetRelKeyPos

TAdsTable/TAdsQuery.AdsGetRelKeyPos

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsGetRelKeyPos  Advantage TDataSet Descendant |  |  |  |  |

Returns the relative position of the current record in given index order.

Syntax

function AdsGetRelKeyPos : Double;

Description

AdsGetRelKeyPos returns an estimation of the position in the current key in the indicated index order. The value returned will be between 0.0 and 1.0, inclusive. If there are scopes set on the index order, the position returned will be relative to the visible records.

Example

AdsTable1.FindKey( ['Smith'] );

dPercentage := AdsTable1.AdsGetRelKeyPos;

{ dPercentage equals .785 to indicate that Smith was locaed at about 78% through the entire index }

See Also

[AdsGetKeyCount](ade_adsgetkeycount.md)

[AdsGetKeyNum](ade_adsgetkeynum.md)

[AdsGetRecordNum](ade_adsgetrecordnum.md)

[AdsSetRelKeyPos](ade_adssetrelkeypos.md)
