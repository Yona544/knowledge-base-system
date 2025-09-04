AdsDeleteRecord




Advantage Database Server 12  

AdsDeleteRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDeleteRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDeleteRecord Advantage Client Engine ace\_Adsdeleterecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDeleteRecord  Advantage Client Engine |  |  |  |  |

Marks the current record in the given table as deleted.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsDeleteRecord (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |

Remarks

In DBF tables, AdsDeleteRecord does not actually remove the current record from the table. The record is marked in the first byte of the record image as deleted. The record can be recalled using [AdsRecallRecord](ace_adsrecallrecord.htm). Query the deleted status of a record by using [AdsIsRecordDeleted](ace_adsisrecorddeleted.htm). Deleted records can be removed from tables completely by using [AdsPackTable](ace_adspacktable.htm).

In Advantage proprietary ADT tables, AdsDeleteRecord will permanently delete the current record. The record cannot be recalled using [AdsRecallRecord](ace_adsrecallrecord.htm) after the record has been written.

Note Deleted ADT records are automatically placed in a record re-use list. Because of this, the server unlocks them even if the user has an explicit lock on the record.

Example

[Click Here](ace_examples.htm#adsdeleterecordexample)

See Also

[AdsRecallRecord](ace_adsrecallrecord.htm)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.htm)

[AdsPackTable](ace_adspacktable.htm)

[AdsAtEOF](ace_adsateof.htm)