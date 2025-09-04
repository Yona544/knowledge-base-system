---
title: Ade Adsgetjulian
slug: ade_adsgetjulian
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetjulian.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4f057229a05ff4a4d49142305fc9c1bd4aed8f70
---

# Ade Adsgetjulian

AdsGetJulian

TAdsTable.AdsGetJulian

Advantage TDataSet Descendant

| TAdsTable.AdsGetJulian  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the Julian date representation from the given field.

Syntax

function AdsGetJulian( strFieldName : String ) : Longint;

Parameter

| strFieldName | Name of the field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetJulian can be used to retrieve the Julian date representation of a date from date, short date, ModTime fields, and timestamp fields. A Julian date is a signed long integer representation of the number of days since January 1, 4713 B.C.

Example

dtDate := AdsTable1.FieldByName( BirthDay ).AsDateTime;

See Also

[AdsGetDate](ade_adsgetdate.md)

[AdsSetJulian](ade_adssetjulian.md)
