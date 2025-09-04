AdsSetShort




Advantage Database Server 12  

TAdsTable.AdsSetShort

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetShort  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetShort Advantage TDataSet Descendant ade\_Adssetshort Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetShort  Advantage TDataSet Descendant |  |  |  |  |

Stores the given signed short (two-byte) integer in the given field.

Syntax

procedure AdsSetShort( const strFieldName : string; sValue : SmallInt );

Parameters

|  |  |
| --- | --- |
| strFieldName | Name of field to set |
| sValue | Short value to be stored in table |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsInteger. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetShort can be used to set values for numeric, long integer, short integer, double, CurDouble, RowVersion, and Money fields. If there are decimals in a numeric field, the decimals are padded with character zeros. If the number of sValue is too large to fit in a numeric field, ADS\_DATA\_TOO\_LONG is returned.

Example

AdsTable1.FieldByName( RecordID ).AsInteger := 22;

See Also

[AdsGetShort](ade_adsgetshort.htm)

[AdsSetField](ade_adssetfield.htm)