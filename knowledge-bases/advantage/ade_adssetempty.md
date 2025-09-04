AdsSetEmpty




Advantage Database Server 12  

TAdsTable.AdsSetEmpty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetEmpty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetEmpty Advantage TDataSet Descendant ade\_Adssetempty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetEmpty  Advantage TDataSet Descendant |  |  |  |  |

Sets the given field to its NULL value when using ADTs or to its empty value when using DBFs.

Syntax

procedure AdsSetEmpty( strFieldName : String );

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field to set to empty/null. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.Clear. See your Delphi documentation for more information about this native Delphi method.

Description

Null and empty values vary by field type. AdsSetEmpty ensures that the value set in the field is what Advantage expects as a NULL value for ADTs or an empty value for DBFs.

Example

AdsTable1.FieldByName( LastName ).Clear;

See Also

[AdsIsEmpty](ade_adsisempty.htm)

[AdsSetField](ade_adssetfield.htm)