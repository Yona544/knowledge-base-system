AdsGotoTop




Advantage Database Server 12  

AdsGotoTop

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGotoTop  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGotoTop Advantage Client Engine ace\_Adsgototop Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGotoTop  Advantage Client Engine |  |  |  |  |

Positions the given table to the first record

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGotoTop (ADSHANDLE hObj); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. |

Remarks

If the handle given as hObj is the handle of a table or cursor, the table (or cursor) is positioned at the top of its natural order. The record on which it positions is the first record starting from record 1 (one) that satisfies current filter conditions. If the handle passed is an index order handle, the table is positioned at the top of the current logical order, obeying both current filters and scopes.

Example

[Click Here](ace_examples.htm#adsgototopexample)

See Also

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)

[AdsGetRecordCount](ace_adsgetrecordcount.htm)

[AdsSkip](ace_adsskip.htm)