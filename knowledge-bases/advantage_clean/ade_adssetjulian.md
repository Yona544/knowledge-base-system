---
title: Ade Adssetjulian
slug: ade_adssetjulian
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetjulian.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9a39ae5e0ba29cea145b909901b4f95be3b5dd73
---

# Ade Adssetjulian

AdsSetJulian

TAdsTable.AdsSetJulian

Advantage TDataSet Descendant

| TAdsTable.AdsSetJulian  Advantage TDataSet Descendant |  |  |  |  |

Stores the given Julian date in the given field.

Syntax

procedure AdsSetJulian( strFieldName : String; lDate : Longint );

Parameters

| strFieldName | Name of field to set. |
| lDate | Julian representation of the date. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetJulian can be used to store the Julian date representation of a date into date, short date, ModTime, and timestamp fields. A Julian date is a signed long integer representation of the number of days since January 1, 4713 B.C.

Example

AdsTable1.FieldByName( BirthDay ).AsDateTime = dtDateOfBirth;

See Also

[AdsGetJulian](ade_adsgetjulian.md)

[AdsSetDate](ade_adssetdate.md)
