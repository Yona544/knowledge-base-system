AdsIsEmpty




Advantage Database Server 12  

TAdsTable.AdsIsEmpty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsEmpty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsEmpty Advantage TDataSet Descendant ade\_Adsisempty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsIsEmpty  Advantage TDataSet Descendant |  |  |  |  |

Determines if a given field is empty (null).

Syntax

function AdsIsEmpty( strFieldName : String ) : Boolean;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field to query. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.IsNull. See your Delphi documentation for more information about this native Delphi method.

Description

Use AdsIsEmpty to determine if the indicated field is NULL for ADTs or empty for DBFs. The NULL/empty value can vary between data types. Therefore, AdsIsEmpty can be used to be certain whether the current field value is NULL/empty.

Example

bEmpty := AdsTable1.FieldByName( Salary ).IsNull;

See Also

[AdsSetEmpty](ade_adssetempty.htm)

[AdsSetField](ade_adssetfield.htm)