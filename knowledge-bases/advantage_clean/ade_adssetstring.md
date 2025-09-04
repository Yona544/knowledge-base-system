---
title: Ade Adssetstring
slug: ade_adssetstring
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetstring.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c84e73b970179f2b72b751e3f71c958158358e29
---

# Ade Adssetstring

AdsSetString

TAdsTable.AdsSetString

Advantage TDataSet Descendant

| TAdsTable.AdsSetString  Advantage TDataSet Descendant |  |  |  |  |

Sets a field value in a table to a string value.

Syntax

procedure AdsSetString( strFieldName : String; strValue : String );

Parameters

| strFieldName | Name of field to set. |
| strValue | Store this data in the field. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetString can be used to set values for character, memo, logical, and fields. To set numeric and date fields with string values, use AdsSetField.

Example

AdsTable1.Edit;

AdsTable1.FieldByName( LastName ).AsString := Smith;

AdsTable1.FieldByName( Salary ).AsString = 4.95;

AdsTable1.FieldByName( BirthDay ).AsString = 10/21/80;

See Also

[AdsGetString](ade_adsgetstring.md)

[AdsSetField](ade_adssetfield.md)
