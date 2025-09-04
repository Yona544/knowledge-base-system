AdsGetJulian




Advantage Database Server 12  

TAdsTable.AdsGetJulian

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetJulian  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetJulian Advantage TDataSet Descendant ade\_Adsgetjulian Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetJulian  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the Julian date representation from the given field.

Syntax

function AdsGetJulian( strFieldName : String ) : Longint;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsDateTime. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetJulian can be used to retrieve the Julian date representation of a date from date, short date, ModTime fields, and timestamp fields. A Julian date is a signed long integer representation of the number of days since January 1, 4713 B.C.

Example

dtDate := AdsTable1.FieldByName( BirthDay ).AsDateTime;

See Also

[AdsGetDate](ade_adsgetdate.htm)

[AdsSetJulian](ade_adssetjulian.htm)