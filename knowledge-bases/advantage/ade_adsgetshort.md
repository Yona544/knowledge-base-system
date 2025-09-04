AdsGetShort




Advantage Database Server 12  

TAdsTable.AdsGetShort

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetShort  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetShort Advantage TDataSet Descendant ade\_Adsgetshort Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetShort  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the short (two-byte) integer value from the given field.

Syntax

function TAdsTable.AdsGetShort( const strFieldName: string ): SmallInt;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsInteger. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetShort returns the signed short (2-byte) value stored in the numeric, long integer, short integer, double, CurDouble, short, RowVersion, or auto-increment field. It is possible to either overflow the value or lose decimal precision by using this function. If more precision is desired, use [AdsGetDouble](ade_adsgetdouble.htm). If AdsGetShort is used to retrieve a Money field, the four decimal digits will be rounded to the nearest whole number.

Example

iID := AdsTable1.FieldByName( RecordID ).AsInteger;

See Also

[AdsGetField](ade_adsgetfield.htm)

[AdsSetShort](ade_adssetshort.htm)