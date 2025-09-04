---
title: Ade Adsgetmilliseconds
slug: ade_adsgetmilliseconds
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetmilliseconds.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3e36f8b4e298683b8ceccae703d0918ef476c597
---

# Ade Adsgetmilliseconds

AdsGetMilliseconds

TAdsTable.AdsGetMilliseconds

Advantage TDataSet Descendant

| TAdsTable.AdsGetMilliseconds  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the time value from the given time or timestamp field as the number of milliseconds since midnight.

Syntax

function AdsGetMilliseconds( const strFieldName: string ): Longint;

Parameter

| strFieldName | Name of field to retrieve |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetMilliseconds returns the number of milliseconds since midnight stored in a time field, ModTime field, or in the time portion of a timestamp field.

Example

dtTime := AdsTable1.FieldByName( TimeEntered ).AsDateTime;

See Also

[AdsGetField](ade_adsgetfield.md)

[AdsGetTime](ade_adsgettime.md)

[AdsSetMilliseconds](ade_adssetmilliseconds.md)
