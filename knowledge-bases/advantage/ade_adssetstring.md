AdsSetString




Advantage Database Server 12  

TAdsTable.AdsSetString

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetString  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetString Advantage TDataSet Descendant ade\_Adssetstring Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetString  Advantage TDataSet Descendant |  |  |  |  |

Sets a field value in a table to a string value.

Syntax

procedure AdsSetString( strFieldName : String; strValue : String );

Parameters

|  |  |
| --- | --- |
| strFieldName | Name of field to set. |
| strValue | Store this data in the field. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsString. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetString can be used to set values for character, memo, logical, and fields. To set numeric and date fields with string values, use AdsSetField.

Example

AdsTable1.Edit;

AdsTable1.FieldByName( LastName ).AsString := Smith;

AdsTable1.FieldByName( Salary ).AsString = 4.95;

AdsTable1.FieldByName( BirthDay ).AsString = 10/21/80;

See Also

[AdsGetString](ade_adsgetstring.htm)

[AdsSetField](ade_adssetfield.htm)