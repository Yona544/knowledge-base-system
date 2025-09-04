---
title: Ade Adsgetnumfields
slug: ade_adsgetnumfields
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetnumfields.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 267f0c2b9741ee9c1fadffe96f096a0809062b90
---

# Ade Adsgetnumfields

AdsGetNumFields

TAdsTable.AdsGetNumFields

Advantage TDataSet Descendant

| TAdsTable.AdsGetNumFields  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the number of fields in the given table.

Syntax

function AdsGetNumFields : Word;

Description

The returned field count does not include the deleted byte.

Example

AdsTable1.Active := TRUE;

wNumFields := AdsTable1.AdsGetNumFields;

wFieldCount := AdsTable1.FieldCount;

{ wNumFields is equal to the wFieldCount because both methods are identical }

See Also

[AdsCreateTable](ade_adscreatetable.md)

[AdsGetFieldName](ade_adsgetfieldname.md)
