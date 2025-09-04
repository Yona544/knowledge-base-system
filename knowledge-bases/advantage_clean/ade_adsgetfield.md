---
title: Ade Adsgetfield
slug: ade_adsgetfield
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfield.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4e47f1678bc0aa9b96d3c04c8af9264187bc78e4
---

# Ade Adsgetfield

AdsGetField

TAdsTable.AdsGetField

Advantage TDataSet Descendant

| TAdsTable.AdsGetField  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the text string version of the given field from the given table.

Syntax

type TAdsTrimOptions = ( optNONE, optLTRIM, optRTRIM, optTRIM );

 

function AdsGetField( strFieldName : String; enumTrimOptions : TAdsTrimOptions ) : String;

Parameter

| strFieldName | Name of field to retrieve. |
| enumTrimOptions | Option to trim spaces from the returned data. optNONE, optTRIM (trims leading and trailing spaces), optLTRIM (trims trailing spaces), and optRTRIM (trims leading spaces). |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Example

strSalary := AdsTable1.FieldByName( Salary ).AsString;

strDate := AdsTable1.FieldByName( Birthday ).AsString;

Description

AdsGetField can be used to retrieve strings, numerics, dates, logicals, Money, Floats, integers, times, timestamps, RowVersion, ModTime, and memos. For numerics, Money, times, timestamps, and dates, it converts the result to a string (instead of storing the IEEE numeric data in the buffer). Dates are formatted according to the date mask set by [DateFormat](ade_dateformat.md). Binary data cannot be retrieved using AdsGetField, see [AdsGetBinary](ade_adsgetbinary.md).

See Also

[AdsGetBinary](ade_adsgetbinary.md)

[AdsGetDate](ade_adsgetdate.md)

[AdsGetDouble](ade_adsgetdouble.md)

[AdsGetLogical](ade_adsgetlogical.md)

[AdsGetLong](ade_adsgetlong.md)

[AdsGetString](ade_adsgetstring.md)
