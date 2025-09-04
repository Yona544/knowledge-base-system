AdsGotoRecord




Advantage Database Server 12  

AdsGotoRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGotoRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGotoRecord Advantage Client Engine ace\_Adsgotorecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGotoRecord  Advantage Client Engine |  |  |  |  |

Positions the given table to the given record number

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGotoRecord (ADSHANDLE hTable,  UNSIGNED32 ulRec); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| ulRec (I) | Record number. |

Remarks

AdsGotoRecord ignores filters, relations, and scopes. If ulRec is zero, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to 0. If ulRec is greater than the number of records in the table, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to the number of records in the table + 1.

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

Example

[Click Here](ace_examples.htm#adsgotorecordexample)

See Also

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsGotoTop](ace_adsgototop.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)

[AdsGetRecordCount](ace_adsgetrecordcount.htm)

[AdsSkip](ace_adsskip.htm)

[AdsWriteRecord](ace_adswriterecord.htm)