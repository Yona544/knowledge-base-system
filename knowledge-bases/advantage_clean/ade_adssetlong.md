---
title: Ade Adssetlong
slug: ade_adssetlong
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetlong.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9de59bca834b5bac98b9be6a2d0ef3a0117e5efc
---

# Ade Adssetlong

AdsSetLong

TAdsTable.AdsSetLong

Advantage TDataSet Descendant

| TAdsTable.AdsSetLong  Advantage TDataSet Descendant |  |  |  |  |

Stores the given signed long integer in the given field.

Syntax

procedure AdsSetLong( strFieldName : String; lValue : Longint );

Parameters

| strFieldName | Name of field to set. |
| lValue | Long value to be stored in table. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsInteger. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetLong can be used to set values for numeric, integer, short integer, double, CurDouble, RowVersion, and Money fields. If there are decimals in a numeric field, the decimals are padded with character zeros.

Example

AdsTable1.FieldByName( RecordID ).AsInteger = 93;

See Also

[AdsGetLong](ade_adsgetlong.md)

[AdsSetField](ade_adssetfield.md)
