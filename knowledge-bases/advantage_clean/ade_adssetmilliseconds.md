---
title: Ade Adssetmilliseconds
slug: ade_adssetmilliseconds
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetmilliseconds.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 86af7a67f72964033a0c7570ac1f576542ed48f3
---

# Ade Adssetmilliseconds

AdsSetMilliseconds

TAdsTable.AdsSetMilliseconds

Advantage TDataSet Descendant

| TAdsTable.AdsSetMilliseconds  Advantage TDataSet Descendant |  |  |  |  |

Stores the given value representing milliseconds since midnight in the given time or timestamp field.

Syntax

procedure AdsSetMilliseconds( const strFieldName : string; lTime: LongInt );

Parameters

| strFieldName | Name of field to set. |
| lTime | Long value to be stored in table. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetMilliseconds can be used to set the number of milliseconds since midnight in a time field, ModTime field, or in the time portion of a timestamp field.

Example

AdsTable1.FieldByName( TimeEntered ).AsDateTime := dtTime;

See Also

[AdsGetMilliseconds](ade_adsgetmilliseconds.md)

[AdsSetField](ade_adssetfield.md)

[AdsSetTime](ade_adssettime.md)
