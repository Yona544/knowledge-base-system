AdsSetLong




Advantage Database Server 12  

TAdsTable.AdsSetLong

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetLong  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetLong Advantage TDataSet Descendant ade\_Adssetlong Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetLong  Advantage TDataSet Descendant |  |  |  |  |

Stores the given signed long integer in the given field.

Syntax

procedure AdsSetLong( strFieldName : String; lValue : Longint );

Parameters

|  |  |
| --- | --- |
| strFieldName | Name of field to set. |
| lValue | Long value to be stored in table. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsInteger. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetLong can be used to set values for numeric, integer, short integer, double, CurDouble, RowVersion, and Money fields. If there are decimals in a numeric field, the decimals are padded with character zeros.

Example

AdsTable1.FieldByName( RecordID ).AsInteger = 93;

See Also

[AdsGetLong](ade_adsgetlong.htm)

[AdsSetField](ade_adssetfield.htm)