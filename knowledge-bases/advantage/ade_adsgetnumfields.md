AdsGetNumFields




Advantage Database Server 12  

TAdsTable.AdsGetNumFields

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetNumFields  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetNumFields Advantage TDataSet Descendant ade\_Adsgetnumfields Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetNumFields  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the number of fields in the given table.

Syntax

function AdsGetNumFields : Word;

Description

The returned field count does not include the deleted byte.

Example

AdsTable1.Active := TRUE;

wNumFields := AdsTable1.AdsGetNumFields;

wFieldCount := AdsTable1.FieldCount;

{ wNumFields is equal to the wFieldCount because both methods are identical }

See Also

[AdsCreateTable](ade_adscreatetable.htm)

[AdsGetFieldName](ade_adsgetfieldname.htm)