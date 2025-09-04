AdsSetLogical




Advantage Database Server 12  

TAdsTable.AdsSetLogical

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetLogical  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetLogical Advantage TDataSet Descendant ade\_Adssetlogical Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetLogical  Advantage TDataSet Descendant |  |  |  |  |

Stores the given logical value in the given field.

Syntax

procedure AdsSetLogical( strFieldName : String; bValue : Boolean );

Parameters

|  |  |
| --- | --- |
| strFieldName | Name of field to set. |

|  |  |
| --- | --- |
| bValue | Store this value in the field ( False/True ) . |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TField.AsBoolean. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetLogical can set the value of the logical field to True or False. To set a logical field to NULL, use [AdsSetEmpty](ade_adssetempty.htm).

Example

AdsTable1.FieldByName( IsMarried ).AsBoolean := TRUE;

See Also

[AdsGetLogical](ade_adsgetlogical.htm)

[AdsSetField](ade_adssetfield.htm)