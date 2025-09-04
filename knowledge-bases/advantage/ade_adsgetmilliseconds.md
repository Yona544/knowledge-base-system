AdsGetMilliseconds




Advantage Database Server 12  

TAdsTable.AdsGetMilliseconds

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetMilliseconds  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetMilliseconds Advantage TDataSet Descendant ade\_Adsgetmilliseconds Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetMilliseconds  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the time value from the given time or timestamp field as the number of milliseconds since midnight.

Syntax

function AdsGetMilliseconds( const strFieldName: string ): Longint;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field to retrieve |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetMilliseconds returns the number of milliseconds since midnight stored in a time field, ModTime field, or in the time portion of a timestamp field.

Example

dtTime := AdsTable1.FieldByName( TimeEntered ).AsDateTime;

See Also

[AdsGetField](ade_adsgetfield.htm)

[AdsGetTime](ade_adsgettime.htm)

[AdsSetMilliseconds](ade_adssetmilliseconds.htm)