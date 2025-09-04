AdsSetJulian




Advantage Database Server 12  

TAdsTable.AdsSetJulian

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetJulian  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetJulian Advantage TDataSet Descendant ade\_Adssetjulian Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetJulian  Advantage TDataSet Descendant |  |  |  |  |

Stores the given Julian date in the given field.

Syntax

procedure AdsSetJulian( strFieldName : String; lDate : Longint );

Parameters

|  |  |
| --- | --- |
| strFieldName | Name of field to set. |
| lDate | Julian representation of the date. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetJulian can be used to store the Julian date representation of a date into date, short date, ModTime, and timestamp fields. A Julian date is a signed long integer representation of the number of days since January 1, 4713 B.C.

Example

AdsTable1.FieldByName( BirthDay ).AsDateTime = dtDateOfBirth;

See Also

[AdsGetJulian](ade_adsgetjulian.htm)

[AdsSetDate](ade_adssetdate.htm)