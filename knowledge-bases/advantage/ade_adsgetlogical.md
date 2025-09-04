AdsGetLogical




Advantage Database Server 12  

TAdsTable.AdsGetLogical

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetLogical  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetLogical Advantage TDataSet Descendant ade\_Adsgetlogical Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetLogical  Advantage TDataSet Descendant |  |  |  |  |

Retrieves a logical value from the given field.

Syntax

function AdsGetLogical( strFieldName : String ) : Boolean;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsBoolean. See your Delphi documentation for more information about this native Delphi method.

Description

The value returned will be either True (1) or False (0). AdsGetLogical also returns False if the logical field contains a NULL value. To determine if a False return type is NULL or assigned to False, call [AdsIsEmpty](ade_adsisempty.htm) or [AdsGetString](ade_adsgetstring.htm) on the numeric field.

Example

bValue := AdsTable1.FieldByName( IsMarried ).AsBoolean;

See Also

[AdsGetField](ade_adsgetfield.htm)

[AdsSetLogical](ade_adssetlogical.htm)