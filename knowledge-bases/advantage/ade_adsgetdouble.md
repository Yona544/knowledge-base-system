AdsGetDouble




Advantage Database Server 12  

TAdsTable.AdsGetDouble

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetDouble  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetDouble Advantage TDataSet Descendant ade\_Adsgetdouble Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetDouble  Advantage TDataSet Descendant |  |  |  |  |

Retrieves an 8-byte double value from the given field.

Syntax

function AdsGetDouble( strFieldName : String ) : Double;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsFloat. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetDouble returns the IEEE 64-bit double representation of the value in a numeric, integer, short integer, double, CurDouble, Money, RowVersion, or autoincrement field. This function provides the most precision available in the Advantage Client Engine for retrieving numeric values.

Example

fValue := AdsTable1.FieldByName( Salary ).AsFloat;

See Also

[AdsGetField](ade_adsgetfield.htm)

[AdsGetLong](ade_adsgetlong.htm)

[AdsSetDouble](ade_adssetdouble.htm)