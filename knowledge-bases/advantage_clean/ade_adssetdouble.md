---
title: Ade Adssetdouble
slug: ade_adssetdouble
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetdouble.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 1e6cb3bf583984923d5b2ca9c2d7a6db1fbe69e5
---

# Ade Adssetdouble

AdsSetDouble

TAdsTable.AdsSetDouble

Advantage TDataSet Descendant

| TAdsTable.AdsSetDouble  Advantage TDataSet Descendant |  |  |  |  |

Stores the given floating point value (IEEE 64-bit double format) in the given field.

Syntax

procedure AdsSetDouble( strFieldName : String; dValue : Double );

Parameter

| strFieldName | Name of field to set. |
| dValue | Store this data in the field. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsFloat. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetDouble can be used to set values for numeric, integer, short integer, double, CurDouble, RowVersion, and Money fields. It is possible to lose decimal precision using AdsSetDouble depending on the size and number of decimals in the target field. AdsSetDouble will round decimals to the precision of the field in the table whose value is being set. If AdsSetDouble is used to set a Money field, the double value will be rounded to the fourth decimal.

Example

AdsTable1.FieldByName( Salary ).AsFloat := 4.95;

See Also

[AdsGetDouble](ade_adsgetdouble.md)

[AdsSetField](ade_adssetfield.md)
