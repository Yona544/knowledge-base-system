AdsGetTime




Advantage Database Server 12  

TAdsTable.AdsGetTime

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetTime  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetTime Advantage TDataSet Descendant ade\_Adsgettime Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetTime  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the time value from the given time or timestamp field.

Syntax

function AdsGetTime( const strFieldName : string ) : string;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field to retrieve |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetTime returns the time value formatted in 12 hour time with hours, minutes, seconds and an AM/PM indicator as appropriate from either a time field, ModTime field, or the time portion of a timestamp field. If, for example, the time field contains 5415000 milliseconds (since midnight), the string value returned will be "01:30:15 AM". If the exact number of milliseconds is required, use [AdsGetMilliseconds](ade_adsgetmilliseconds.htm)

Example

strTime := AdsTable1.FieldByName( TimeEntered ).AsString;

See Also

[AdsSetTime](ade_adssettime.htm)

[AdsGetField](ade_adsgetfield.htm)

[AdsGetMilliseconds](ade_adsgetmilliseconds.htm)