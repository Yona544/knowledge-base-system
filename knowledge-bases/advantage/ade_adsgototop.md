AdsGotoTop




Advantage Database Server 12  

TAdsTable.AdsGotoTop

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGotoTop  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGotoTop Advantage TDataSet Descendant ade\_Adsgototop Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGotoTop  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the first record.

Syntax

procedure AdsGotoTop;

Description

If no index has been set, the table is positioned at the top of its natural order. The record on which it positions is the first record starting from record 1 that satisfies current filter conditions. If an index is set, the table is positioned at the top of the current logical order, obeying both current filters and scopes.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsGotoTop;

{ note that this method is identical to the native Delphi method First }

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.htm)

[AdsGotoBottom](ade_adsgotobottom.htm)

[AdsGotoRecord](ade_adsgotorecord.htm)

[AdsSkip](ade_adsskip.htm)