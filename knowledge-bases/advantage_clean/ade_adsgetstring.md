---
title: Ade Adsgetstring
slug: ade_adsgetstring
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetstring.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a39c61b416db92c0fc187333a85856a5aaf47432
---

# Ade Adsgetstring

AdsGetString

TAdsTable.AdsGetString

Advantage TDataSet Descendant

| TAdsTable.AdsGetString  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the text string version of the given field from the given table.

Syntax

type TAdsTrimOptions = ( optNONE, optLTRIM, optRTRIM, optTRIM );

 

function AdsGetString( strFieldName : String; enumTrimOptions : TAdsTrimOptions ) : String;

Parameter

| strFieldName | Name of field to retrieve. |
| enumTrimOptions | Options to trim spaces from the returned data. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetString may be used to retrieve strings, numerics, dates, logicals, ModTime, and memos. Dates are formatted according to [DateFormat](ade_dateformat.md). Binary data cannot be retrieved using AdsGetString, see [AdsGetBinary](ade_adsgetbinary.md). In addition, this function does not support short dates, floats, integers, short, time, or timestamp.

When called on a logical field, the value returned will be a T, an F, or a space representing a NULL value.

For memo fields use AdsGetMemoLength to get the size in bytes that will be returned if needed.

Example

strSalary := AdsTable1.FieldByName( Salary ).AsString;

strDate := AdsTable1.FieldByName( BirthDay ).AsString;

See Also

[AdsGetBinaryLength](ade_adsgetbinarylength.md)

[AdsGetField](ade_adsgetfield.md)

[AdsGetMemoLength](ade_adsgetmemolength.md)

[AdsSetString](ade_adssetstring.md)
