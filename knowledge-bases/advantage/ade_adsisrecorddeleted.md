AdsIsRecordDeleted




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsIsRecordDeleted

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsIsRecordDeleted  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsIsRecordDeleted Advantage TDataSet Descendant ade\_Adsisrecorddeleted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsIsRecordDeleted  Advantage TDataSet Descendant |  |  |  |  |

Determines the deleted status of the current record in a DBF dataset.

Syntax

function AdsIsRecordDeleted( ulRecNum : Longint ) : Boolean;

Parameter

|  |  |
| --- | --- |
| ulRecNum | Pass the physical record number to check. If the passed record number is 0 then the current record will be checked. |

Description

The first byte of every record in a DBF dataset is reserved for use as a deleted byte. This byte signals whether the record is deleted and/or encrypted. The result of this function can be used to implement a recycling algorithm for deleted records, or a periodic [AdsPackTable](ade_adspacktable.htm) can be used to remove deleted records from the table. To check the current record pass a 0 as the record number.

Note AdsIsRecordDeleted will generally return False in the pbDeleted parameter for Advantage proprietary ADT tables. Records that are deleted in ADT tables are permanently deleted and can never be retrieved by a client application once they have been written. It is possible to call AdsIsRecordDeleted just after calling [AdsDeleteRecord](ade_adsdeleterecord.htm) and before the record is written. This function will return True in that case.

Example

{ this is an OnFilterRecord event handler for AdsTable1 }

procedure TForm1.AdsTable1FilterRecord(DataSet: TDataSet;

var Accept: Boolean);

begin

if ( NOT bFilterDeletedRecords ) AND

( DataSet is TAdsTable ) AND

(( DataSet as TAdsTable ).AdsIsRecordDeleted(0) ) then

Accept := FALSE;

end;

See Also

[AdsDeleteRecord](ade_adsdeleterecord.htm)

[AdsPackTable](ade_adspacktable.htm)

[AdsRecallRecord](ade_adsrecallrecord.htm)