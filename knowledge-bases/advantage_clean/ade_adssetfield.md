---
title: Ade Adssetfield
slug: ade_adssetfield
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetfield.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 722b93c5285d16d53db78e7f98c59641897f372f
---

# Ade Adssetfield

AdsSetField

TAdsTable.AdsSetField

Advantage TDataSet Descendant

| TAdsTable.AdsSetField  Advantage TDataSet Descendant |  |  |  |  |

Stores the given data into the specified field.

Syntax

procedure AdsSetField( strFieldName : String; strBuffer : String );

Parameter

| strFieldName | Name of field to set. |
| StrBuffer | Data to store in field. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetField can be used to store logical, string, memo, numeric, date, short date, double, CurDouble, Money, integer, short integer, time, time stamp, image, binary, RowVersion, ModTime, and raw data.

Dates, times, timestamps, numerics, and Money values are expected to be given as text strings. Dates are expected to be formatted the same as the [DateFormat](ade_dateformat.md) setting. For example, to set a timestamp field, the value could be "7/28/1996 14:30:25". To set empty or null values in fields, use [AdsSetEmpty](ade_adssetempty.md). Setting the value of a field requires a data lock on the table, either a record lock or a file lock. If no lock is held on the current record or table, the Advantage Client Engine will attempt to get an implicit lock on the record. Implicit locks are released when the record is updated on the server.

Example

AdsTable1.FieldByName( Salary ).AsString = 4.95;

AdsTable1.FieldByName( BirthDay ).AsString = 10/21/80;

See Also

[AdsGetField](ade_adsgetfield.md)

[AdsSetBinary](ade_adssetbinary.md)

[AdsSetDate](ade_adssetdate.md)

[AdsSetDouble](ade_adssetdouble.md)

[AdsSetLogical](ade_adssetlogical.md)

[AdsSetLong](ade_adssetlong.md)

[AdsSetString](ade_adssetstring.md)
