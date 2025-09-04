---
title: Ade Adssetdate
slug: ade_adssetdate
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetdate.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ed4c87218cdc5ba6a02f1a5e7ad7f75d269a1a63
---

# Ade Adssetdate

AdsSetDate

TAdsTable.AdsSetDate

| TAdsTable.AdsSetDate |  |  |  |  |

Stores given date in the given date field or the date portion of a timestamp field.

Syntax

procedure AdsSetDate( strFieldName : String; strDate : String );

Parameter

| StrFieldName | Name of field to set. |
| StrDate | Date value as a string. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetDate can be used to set values for date, short date, ModTime, and the date portion of timestamp fields. The date given must be in the form of the current date format as defined by [DateFormat](ade_dateformat.md). The Advantage Client Engine does recognize leap years.

If the date format includes only two digits for the year, it will be assumed 1900. It is recommended that your date format contains yyyy (or ccyy) and that the full four digit year designation is used in setting the date field.

Note If using AdsSetDate to set parameters in an SQL statement the date format CCYY-MM-DD can always be used. Alternatively, the global date format (see [TadsSettings.DateFormat](ade_dateformat.md)) can be used to specify the date value.

Example

AdsTable1.FieldByName( BirthDay ).AsString := 10/21/80;

See Also

[AdsGetDate](ade_adsgetdate.md)

[AdsSetField](ade_adssetfield.md)

[AdsSetTime](ade_adssettime.md)
