AdsGetDate




Advantage Database Server 12  

TAdsTable.AdsGetDate

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetDate  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetDate Advantage TDataSet Descendant ade\_Adsgetdate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetDate  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the date value from the given field formatted according to the format defined in [DateFormat](ade_dateformat.htm).

Syntax

function AdsGetDate( strFieldName : String ) : String;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsString or TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetDate returns dates according to the date format set in [DateFormat](ade_dateformat.htm). It can be used to retrieve dates from date fields, short date fields, ModTime fields, and the date portion of timestamp fields.

Example

strDate := AdsTable1.FieldByName( BirthDay ).AsString;

or

dtDate := AdsTable1.FieldByName( BirthDay ).AsDateTime

See Also

[AdsGetJulian](ade_adsgetjulian.htm)

[AdsSetDate](ade_adssetdate.htm)

[AdsSetField](ade_adssetfield.htm)

[AdsGetTime](ade_adsgettime.htm)