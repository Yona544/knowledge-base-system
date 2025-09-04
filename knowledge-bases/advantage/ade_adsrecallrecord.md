AdsRecallRecord




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsRecallRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsRecallRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsRecallRecord Advantage TDataSet Descendant ade\_Adsrecallrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsRecallRecord  Advantage TDataSet Descendant |  |  |  |  |

Restores the current record in the given DBF dataset to normal visibility.

Syntax

procedure AdsRecallRecord;

Description

Calling AdsRecallRecord on a deleted record in a DBF dataset will clear the deleted flag in the first byte of the record.

Note AdsRecallRecord has little effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved nor can they be recalled by a client application. If AdsRecallRecord is called after a call to AdsDeleteRecord and before the record is written, the record will not be deleted. Once a deleted record has been written either through a call to [AdsWriteRecord](ade_adswriterecord.htm) or implicitly through some record movement, that record cannot be recalled.

Example

AdsSettings1.ShowDeleted := TRUE;

AdsTable1.Next;

if AdsTable1.AdsIsRecordDeleted(0) then

AdsTable1.AdsRecallRecord;

See Also

[AdsDeleteRecord](ade_adsdeleterecord.htm)

[AdsIsRecordDeleted](ade_adsisrecorddeleted.htm)