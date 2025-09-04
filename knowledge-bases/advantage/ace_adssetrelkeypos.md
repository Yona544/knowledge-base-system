AdsSetRelKeyPos




Advantage Database Server 12  

AdsSetRelKeyPos

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetRelKeyPos  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetRelKeyPos Advantage Client Engine ace\_Adssetrelkeypos Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetRelKeyPos  Advantage Client Engine |  |  |  |  |

Sets the current record to the given relative position in the given index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetRelKeyPos (ADSHANDLE hIndex, DOUBLE dPos); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| dPos (I) | Set relative key positions. The value specified in the dPos parameter must be in the range from 0.0 to 1.0, where 0.0 would indicate the top of the index and 1.0 refers to the bottom. |

Remarks

AdsSetRelKeyPos approximates the position of the indicated percentage in the index order based on the given value. If there is a scope set, AdsSetRelKeyPos calculates and sets the relative position relative to the current scope.

Example

[Click Here](ace_examples.htm#adssetrelkeyposexample)

See Also

[AdsGetRelKeyPos](ace_adsgetrelkeypos.htm)

[AdsGetKeyCount](ace_adsgetkeycount.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)