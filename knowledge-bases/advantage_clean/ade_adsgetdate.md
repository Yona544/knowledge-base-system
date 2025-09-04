---
title: Ade Adsgetdate
slug: ade_adsgetdate
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetdate.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7c8f2118f3ca74cc133ae16aea5b66d4bb0ccce8
---

# Ade Adsgetdate

AdsGetDate

TAdsTable.AdsGetDate

Advantage TDataSet Descendant

| TAdsTable.AdsGetDate  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the date value from the given field formatted according to the format defined in [DateFormat](ade_dateformat.md).

Syntax

function AdsGetDate( strFieldName : String ) : String;

Parameter

| strFieldName | Name of the field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsString or TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetDate returns dates according to the date format set in [DateFormat](ade_dateformat.md). It can be used to retrieve dates from date fields, short date fields, ModTime fields, and the date portion of timestamp fields.

Example

strDate := AdsTable1.FieldByName( BirthDay ).AsString;

or

dtDate := AdsTable1.FieldByName( BirthDay ).AsDateTime

See Also

[AdsGetJulian](ade_adsgetjulian.md)

[AdsSetDate](ade_adssetdate.md)

[AdsSetField](ade_adssetfield.md)

[AdsGetTime](ade_adsgettime.md)
