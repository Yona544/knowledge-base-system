AdsGotoBottom




Advantage Database Server 12  

AdsGotoBottom

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGotoBottom  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGotoBottom Advantage Client Engine ace\_Adsgotobottom Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGotoBottom  Advantage Client Engine |  |  |  |  |

Positions the given table to the last record

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGotoBottom (ADSHANDLE hObj); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. If hObj is the handle of a table, then it is positioned to the last physical record. If it is an index order handle, it is positioned to the last record of the index order. Filters and scopes are respected. |

Remarks

If the handle passed to AdsGotoBottom is a table handle or cursor, the table (or cursor) is positioned at the last record in natural order, obeying the current filter. If an index order handle is passed, the table is positioned at the last logical record in the order that passes both filters or scopes that are set.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_examples.htm#adsgotobottomexample)

See Also

[AdsGotoTop](ace_adsgototop.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)

[AdsGetRecordCount](ace_adsgetrecordcount.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)

[AdsSkip](ace_adsskip.htm)