AdsSetDate




Advantage Database Server 12  

TAdsTable.AdsSetDate

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetDate |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetDate ade\_Adssetdate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetDate |  |  |  |  |

Stores given date in the given date field or the date portion of a timestamp field.

Syntax

procedure AdsSetDate( strFieldName : String; strDate : String );

Parameter

|  |  |
| --- | --- |
| StrFieldName | Name of field to set. |
| StrDate | Date value as a string. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetDate can be used to set values for date, short date, ModTime, and the date portion of timestamp fields. The date given must be in the form of the current date format as defined by [DateFormat](ade_dateformat.htm). The Advantage Client Engine does recognize leap years.

If the date format includes only two digits for the year, it will be assumed 1900. It is recommended that your date format contains yyyy (or ccyy) and that the full four digit year designation is used in setting the date field.

Note If using AdsSetDate to set parameters in an SQL statement the date format CCYY-MM-DD can always be used. Alternatively, the global date format (see [TadsSettings.DateFormat](ade_dateformat.htm)) can be used to specify the date value.

Example

AdsTable1.FieldByName( BirthDay ).AsString := 10/21/80;

See Also

[AdsGetDate](ade_adsgetdate.htm)

[AdsSetField](ade_adssetfield.htm)

[AdsSetTime](ade_adssettime.htm)