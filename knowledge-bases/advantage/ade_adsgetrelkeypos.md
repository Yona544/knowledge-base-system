AdsGetRelKeyPos




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsGetRelKeyPos

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsGetRelKeyPos  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsGetRelKeyPos Advantage TDataSet Descendant ade\_Adsgetrelkeypos Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsGetRelKeyPos  Advantage TDataSet Descendant |  |  |  |  |

Returns the relative position of the current record in given index order.

Syntax

function AdsGetRelKeyPos : Double;

Description

AdsGetRelKeyPos returns an estimation of the position in the current key in the indicated index order. The value returned will be between 0.0 and 1.0, inclusive. If there are scopes set on the index order, the position returned will be relative to the visible records.

Example

AdsTable1.FindKey( ['Smith'] );

dPercentage := AdsTable1.AdsGetRelKeyPos;

{ dPercentage equals .785 to indicate that Smith was locaed at about 78% through the entire index }

See Also

[AdsGetKeyCount](ade_adsgetkeycount.htm)

[AdsGetKeyNum](ade_adsgetkeynum.htm)

[AdsGetRecordNum](ade_adsgetrecordnum.htm)

[AdsSetRelKeyPos](ade_adssetrelkeypos.htm)