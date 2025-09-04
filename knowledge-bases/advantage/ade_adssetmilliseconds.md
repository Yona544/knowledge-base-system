AdsSetMilliseconds




Advantage Database Server 12  

TAdsTable.AdsSetMilliseconds

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetMilliseconds  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetMilliseconds Advantage TDataSet Descendant ade\_Adssetmilliseconds Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetMilliseconds  Advantage TDataSet Descendant |  |  |  |  |

Stores the given value representing milliseconds since midnight in the given time or timestamp field.

Syntax

procedure AdsSetMilliseconds( const strFieldName : string; lTime: LongInt );

Parameters

|  |  |
| --- | --- |
| strFieldName | Name of field to set. |
| lTime | Long value to be stored in table. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetMilliseconds can be used to set the number of milliseconds since midnight in a time field, ModTime field, or in the time portion of a timestamp field.

Example

AdsTable1.FieldByName( TimeEntered ).AsDateTime := dtTime;

See Also

[AdsGetMilliseconds](ade_adsgetmilliseconds.htm)

[AdsSetField](ade_adssetfield.htm)

[AdsSetTime](ade_adssettime.htm)