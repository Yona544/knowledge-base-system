AdsRecallRecord




Advantage Database Server 12  

AdsRecallRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRecallRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRecallRecord Advantage Client Engine ace\_Adsrecallrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRecallRecord  Advantage Client Engine |  |  |  |  |

Restores the current record in the given DBF table to normal visibility.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRecallRecord (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |

Remarks

Calling AdsRecallRecord on a deleted record in a DBF table will clear the deleted flag in the first byte of the record.

Note AdsRecallRecord has little effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved nor can they be recalled by a client application. If AdsRecallRecord is called after a call to AdsDeleteRecord and before the record is written, then the record will not be deleted. Once a deleted record has been written either through a call to [AdsWriteRecord](ace_adswriterecord.htm) or implicitly through some record movement, then that record cannot be recalled.

Example

[Click Here](ace_examples.htm#adsrecallrecordexample)

See Also

[AdsShowDeleted](ace_adsshowdeleted.htm)

[AdsDeleteRecord](ace_adsdeleterecord.htm)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.htm)