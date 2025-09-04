AdsGotoBottom




Advantage Database Server 12  

TAdsTable.AdsGotoBottom

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGotoBottom  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGotoBottom Advantage TDataSet Descendant ade\_Adsgotobottom Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGotoBottom  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the last record.

Syntax

procedure AdsGotoBottom;

Description

If no index has been set, the table is positioned at the last record in natural order, obeying the current filter. If an index is set, the table is positioned at the last logical record in the order that passes both filters or scopes that are set.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsGotoBottom;

{ this function is identical to AdsTable1.Last }

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.htm)

[AdsGotoRecord](ade_adsgotorecord.htm)

[AdsGotoTop](ade_adsgototop.htm)

[AdsSkip](ade_adsskip.htm)