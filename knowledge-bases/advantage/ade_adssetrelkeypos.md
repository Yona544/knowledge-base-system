AdsSetRelKeyPos




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsSetRelKeyPos

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsSetRelKeyPos  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsSetRelKeyPos Advantage TDataSet Descendant ade\_Adssetrelkeypos Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsSetRelKeyPos  Advantage TDataSet Descendant |  |  |  |  |

Sets the current record to the given relative position in the given index order.

Syntax

procedure AdsSetRelKeyPos( dPos : Double );

Parameter

|  |  |
| --- | --- |
| dPos | Set relative key positions. The value specified in the dPos parameter must be in the range from 0.0 to 1.0, where 0.0 would indicate the top of the index and 1.0 refers to the bottom. |

Description

AdsSetRelKeyPos approximates the position in the index order based on the given value. If there is a scope set, AdsSetRelKeyPos calculates and sets the relative position relative to the current scope.

Example

AdsTable1.Active := TRUE;

{ go to the approximate center of the current index }

AdsTable1.AdsSetRelKeyPos( 0.50 );

See Also

[AdsGetKeyCount](ade_adsgetkeycount.htm)

[AdsGetRelKeyPos](ade_adsgetrelkeypos.htm)

[AdsGotoRecord](ade_adsgotorecord.htm)