AdsGetField




Advantage Database Server 12  

TAdsTable.AdsGetField

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetField  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetField Advantage TDataSet Descendant ade\_Adsgetfield Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetField  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the text string version of the given field from the given table.

Syntax

type TAdsTrimOptions = ( optNONE, optLTRIM, optRTRIM, optTRIM );

 

function AdsGetField( strFieldName : String; enumTrimOptions : TAdsTrimOptions ) : String;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field to retrieve. |
| enumTrimOptions | Option to trim spaces from the returned data. optNONE, optTRIM (trims leading and trailing spaces), optLTRIM (trims trailing spaces), and optRTRIM (trims leading spaces). |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Example

strSalary := AdsTable1.FieldByName( Salary ).AsString;

strDate := AdsTable1.FieldByName( Birthday ).AsString;

Description

AdsGetField can be used to retrieve strings, numerics, dates, logicals, Money, Floats, integers, times, timestamps, RowVersion, ModTime, and memos. For numerics, Money, times, timestamps, and dates, it converts the result to a string (instead of storing the IEEE numeric data in the buffer). Dates are formatted according to the date mask set by [DateFormat](ade_dateformat.htm). Binary data cannot be retrieved using AdsGetField, see [AdsGetBinary](ade_adsgetbinary.htm).

See Also

[AdsGetBinary](ade_adsgetbinary.htm)

[AdsGetDate](ade_adsgetdate.htm)

[AdsGetDouble](ade_adsgetdouble.htm)

[AdsGetLogical](ade_adsgetlogical.htm)

[AdsGetLong](ade_adsgetlong.htm)

[AdsGetString](ade_adsgetstring.htm)