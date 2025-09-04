---
title: Ade Adssettime
slug: ade_adssettime
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssettime.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9b3c26e3b985a47f9a7b439c9472a6739b06e888
---

# Ade Adssettime

AdsSetTime

TAdsTable.AdsSetTime

Advantage TDataSet Descendant

| TAdsTable.AdsSetTime  Advantage TDataSet Descendant |  |  |  |  |

Stores the given time value in the given time or timestamp field.

Syntax

procedure AdsSetTime( const strFieldName, strTime: string );

Parameters

| strFieldName | Name of field to set. |
| strTime | Store this data in the field. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetTime can be used to set the time value in a time field, ModTime, or in the time portion of a timestamp field. The time given can be in twelve-hour time or twenty-four hour time format. Valid examples include "12:30 am", "1:45:22 PM", "3:00", and "16:55". In addition, milliseconds can be included if desired. For example "1:30:15.444" represents 5,415,444 milliseconds since midnight. Note that if no "am" or "pm" is included with the time, it is assumed to be twenty-four hour time. This means that the value "12:00" is assumed to represent noon (not midnight).

Note If using AdsSetTime to set parameters in an SQL statement, the required time format is HH:MM:SS or HH:MM:SS.MMM on a twenty-four hour clock cycle.

Example

AdsTable1.FieldByName( TimeEntered ).AsString := 3:14:56 PM;

See Also

[AdsSetField](ade_adssetfield.md)

[AdsGetTime](ade_adsgettime.md)

[AdsSetMilliseconds](ade_adssetmilliseconds.md)
