---
title: Ade Adsgetlong
slug: ade_adsgetlong
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetlong.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 45c11f56702f001ba4ae3cfa6b7b23fdd0b841c6
---

# Ade Adsgetlong

AdsGetLong

TAdsTable.AdsGetLong

Advantage TDataSet Descendant

| TAdsTable.AdsGetLong  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the long integer value from the given field.

Syntax

function AdsGetLong( strFieldName : String ) :Longint;

Parameter

| strFieldName | Name of field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsInteger. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetLong returns the signed long value stored in the numeric, integer, short integer, double, CurDouble, RowVersion, or auto-increment field. It is possible to either overflow the value or lose decimal precision by using this function. If more precision is desired, use AdsGetDouble. When using this function to retrieve an auto-increment value, be sure to treat the result as an unsigned value. If AdsGetLong is used to retrieve a Money field, the four decimal digits will be rounded to the nearest whole number.

Example

iID := AdsTable1.FieldByName( RecordID ).AsInteger;

See Also

[AdsGetField](ade_adsgetfield.md)

[AdsSetLong](ade_adssetlong.md)
