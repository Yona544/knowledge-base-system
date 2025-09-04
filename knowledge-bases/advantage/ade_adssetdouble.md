AdsSetDouble




Advantage Database Server 12  

TAdsTable.AdsSetDouble

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetDouble  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetDouble Advantage TDataSet Descendant ade\_Adssetdouble Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetDouble  Advantage TDataSet Descendant |  |  |  |  |

Stores the given floating point value (IEEE 64-bit double format) in the given field.

Syntax

procedure AdsSetDouble( strFieldName : String; dValue : Double );

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field to set. |
| dValue | Store this data in the field. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsFloat. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetDouble can be used to set values for numeric, integer, short integer, double, CurDouble, RowVersion, and Money fields. It is possible to lose decimal precision using AdsSetDouble depending on the size and number of decimals in the target field. AdsSetDouble will round decimals to the precision of the field in the table whose value is being set. If AdsSetDouble is used to set a Money field, the double value will be rounded to the fourth decimal.

Example

AdsTable1.FieldByName( Salary ).AsFloat := 4.95;

See Also

[AdsGetDouble](ade_adsgetdouble.htm)

[AdsSetField](ade_adssetfield.htm)