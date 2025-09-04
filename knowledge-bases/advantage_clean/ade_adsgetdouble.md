---
title: Ade Adsgetdouble
slug: ade_adsgetdouble
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetdouble.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2db23fe9a33e87aa037a9420314952c9a2dfe641
---

# Ade Adsgetdouble

AdsGetDouble

TAdsTable.AdsGetDouble

Advantage TDataSet Descendant

| TAdsTable.AdsGetDouble  Advantage TDataSet Descendant |  |  |  |  |

Retrieves an 8-byte double value from the given field.

Syntax

function AdsGetDouble( strFieldName : String ) : Double;

Parameter

| strFieldName | Name of the field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsFloat. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetDouble returns the IEEE 64-bit double representation of the value in a numeric, integer, short integer, double, CurDouble, Money, RowVersion, or autoincrement field. This function provides the most precision available in the Advantage Client Engine for retrieving numeric values.

Example

fValue := AdsTable1.FieldByName( Salary ).AsFloat;

See Also

[AdsGetField](ade_adsgetfield.md)

[AdsGetLong](ade_adsgetlong.md)

[AdsSetDouble](ade_adssetdouble.md)
